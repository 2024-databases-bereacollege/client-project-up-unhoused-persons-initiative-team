<template>
  <div>
    <v-card>
      <v-card-title class="d-flex justify-space-between align-center">
        <div>
          <v-btn color="primary" @click="openAddServiceDialog">Add Service</v-btn>
          <span class="text-h5 mx-4">Services and Providers</span>
        </div>
        <v-btn color="primary" @click="openAddServiceProviderDialog">Add Service Provider</v-btn>
      </v-card-title>
      <v-data-table
        :headers="headers"
        :items="services"
        :items-per-page="100"
        :loading="loading"
        class="elevation-1"
      >
        <!-- eslint-disable-next-line vue/valid-v-slot -->
        <template v-slot:item.DateOfStart="{ item }">
          {{ formatDate(item.DateOfStart) }}
        </template>
        <!-- eslint-disable-next-line vue/valid-v-slot -->
        <template v-slot:item.actions="{ item }">
          <v-icon small class="mr-2" @click="openEditDialog(item)">mdi-pencil</v-icon>
          <v-icon small @click="openDeleteDialog(item)">mdi-delete</v-icon>
        </template>
      </v-data-table>
    </v-card>

<!-- Delete Service Dialog -->
<v-dialog v-model="deleteDialog" max-width="500px">
  <v-card>
    <v-card-title class="text-h5">Delete Service</v-card-title>
    <v-card-text>Are you sure you want to delete this service?</v-card-text>
    <v-card-actions>
      <v-spacer></v-spacer>
      <v-btn color="blue darken-1" text @click="closeDeleteDialog">Cancel</v-btn>
      <v-btn color="blue darken-1" text @click="deleteService">Delete</v-btn>
    </v-card-actions>
  </v-card>
</v-dialog>


<!-- Edit Service Dialog -->
<v-dialog v-model="editDialog" max-width="500px">
  <v-card>
    <v-card-title class="text-h5">Edit Service</v-card-title>
    <v-card-text>
      <v-text-field v-model="editedItem.ServiceDescription" label="Service Description"></v-text-field>
      <v-text-field v-model="editedItem.ContactPerson" label="Contact Person"></v-text-field>
      <v-text-field v-model="editedItem.Email" label="Email"></v-text-field>
      <v-text-field v-model="editedItem.Phone" label="Phone"></v-text-field>
    </v-card-text>
    <v-card-actions>
      <v-spacer></v-spacer>
      <v-btn color="blue darken-1" text @click="closeEditDialog">Cancel</v-btn>
      <v-btn color="blue darken-1" text @click="saveService">Save</v-btn>
    </v-card-actions>
  </v-card>
</v-dialog>

  <!-- Add Service Dialog -->
  <v-dialog v-model="addServiceDialog" max-width="500px">
    <v-card>
      <v-card-title class="text-h5">Add Service</v-card-title>
      <v-card-text>
        <v-text-field v-model="newService.ServiceType" label="Service Type"></v-text-field>
        <v-text-field v-model="newService.ServiceDescription" label="Service Description"></v-text-field>
        <v-select
          v-model="newService.OrganizationID"
          :items="serviceProviders"
          item-text="Organization_Name"
          item-value="OrganizationID"
          label="Service Provider"
        ></v-select>
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn color="blue darken-1" text @click="closeAddServiceDialog">Cancel</v-btn>
        <v-btn color="blue darken-1" text @click="addService">Add</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>

<!-- Add Service Provider Dialog -->
<v-dialog v-model="addServiceProviderDialog" max-width="500px">
  <v-card>
    <v-card-title class="text-h5">Add Service Provider</v-card-title>
    <v-card-text>
      <v-text-field v-model="newServiceProvider.Organization_Name" label="Organization Name"></v-text-field>
      <v-text-field v-model="newServiceProvider.ContactPerson" label="Contact Person"></v-text-field>
      <v-text-field v-model="newServiceProvider.Email" label="Email"></v-text-field>
      <v-text-field v-model="newServiceProvider.Phone" label="Phone"></v-text-field>
      <v-select
    v-if="serviceProvidersLoaded"
    v-model="newService.OrganizationID"
    :items="serviceProviders"
    item-text="Organization_Name"
    item-value="OrganizationID"
    label="Service Provider"
  ></v-select>
      
      <!-- Add the date picker component here -->
      <v-menu
        v-model="dateMenu"
        :close-on-content-click="false"
        :nudge-right="40"
        transition="scale-transition"
        offset-y
        min-width="auto"
      >
        <template v-slot:activator="{ on, attrs }">
          <v-text-field
            v-model="newServiceProvider.DateOfStart"
            label="Date of Start"
            prepend-icon="mdi-calendar"
            readonly
            v-bind="attrs"
            v-on="on"
          ></v-text-field>
        </template>
        <v-date-picker
          v-model="newServiceProvider.DateOfStart"
          @input="dateMenu = false"
        ></v-date-picker>
      </v-menu>
      
    </v-card-text>
    <v-card-actions>
      <v-spacer></v-spacer>
      <v-btn color="blue darken-1" text @click="closeAddServiceProviderDialog">Cancel</v-btn>
      <v-btn color="blue darken-1" text @click="addServiceProvider">Add</v-btn>
    </v-card-actions>
  </v-card>
</v-dialog>
  </div>
</template>


<script>
 /* eslint-disable */
import ServiceProviderSelect from '../components/ServiceProviderSelect.vue';

import axios from 'axios';
export default {
  data() {
    return {
      headers: [
        { title: 'Service Type', key: 'ServiceType' },
        { title: 'Service Description', key: 'ServiceDescription' },
        { title: 'Organization Name', key: 'Organization_Name' },
        { title: 'Contact Person', key: 'ContactPerson' },
        { title: 'Email', key: 'Email' },
        { title: 'Phone', key: 'Phone' },
        { title: 'Date of Start', key: 'DateOfStart' },
        { title: 'Total Neighbors', key: 'TotalNeighbors' },
        { title: 'Actions', key: 'actions', sortable: false },
      ],

      services: [],
      loading: true,
      deleteDialog: false,
      editDialog: false,
      addServiceDialog: false,
      addServiceProviderDialog: false,
      selectedItem: null,
      editedIndex: -1,
      editedItem: {
        ServiceID: '',
        ServiceDescription: '',
        OrganizationID: '',
        ContactPerson: '',
        Email: '',
        Phone: '',
      },
      defaultItem: {
    ServiceID: '',
    ServiceDescription: '',
    OrganizationID: '',
    ContactPerson: '',
    Email: '',
    Phone: '',
  },
  newService: {
    ServiceType: '',
    ServiceDescription: '',
    OrganizationID: null,
  },
  newServiceProvider: {
    Organization_Name: '',
    ContactPerson: '',
    Email: '',
    Phone: '',
    DateOfStart: '',
  },
  serviceProviders: [],
};
},
mounted() {
this.fetchServices();
this.fetchServiceProviders();
},
methods: {
// Fetching data
fetchServices() {
fetch('http://127.0.0.1:5000/api/ServicesAndProviders')
.then(response => response.json())
.then(data => {
this.services = data;
console.log('Updated Services:', this.services);
this.loading = false;
})
.catch(error => {
console.error('Error fetching services:', error);
this.loading = false;
});
},
fetchServiceProviders() {
axios.get('http://127.0.0.1:5000/api/service_providers')
.then(response => {
this.serviceProviders = response.data;
})
.catch(error => {
console.error('Error fetching service providers:', error);
});
},
// Dialog management
openEditDialog(item) {
  this.selectedItem = item;
  this.editedItem = {
    ServiceID: item.ServiceID,
    ServiceDescription: item.ServiceDescription,
    OrganizationID: item.OrganizationID,
    ContactPerson: item.ContactPerson,
    Email: item.Email,
    Phone: item.Phone,
  };
  console.log('Edited Item:', this.editedItem);
  this.editDialog = true;
},
closeEditDialog() {
  this.selectedItem = null;
  this.editedItem = {
    ServiceID: '',
    ServiceDescription: '',
    OrganizationID: '',
    ContactPerson: '',
    Email: '',
    Phone: '',
  };
  this.editDialog = false;
  console.log('Edit dialog closed'); 
},
openDeleteDialog(item) {
  this.selectedItem = item;
  this.deleteDialog = true;
},
closeDeleteDialog() {
  this.selectedItem = null;
  this.deleteDialog = false;
},
openAddServiceDialog() {
  this.addServiceDialog = true;
},
closeAddServiceDialog() {
  this.newService = {
    ServiceType: '',
    ServiceDescription: '',
    OrganizationID: null,
  };
  this.addServiceDialog = false;
},
openAddServiceProviderDialog() {
  this.addServiceProviderDialog = true;
},
closeAddServiceProviderDialog() {
  this.newServiceProvider = {
    OrganizationName: '',
    ContactPerson: '',
    Email: '',
    Phone: '',
    DateOfStart: '',
  };
  this.addServiceProviderDialog = false;
},

// CRUD operations
deleteService() {
  const serviceID = this.selectedItem.ServiceID;
  axios.delete(`http://127.0.0.1:5000/api/ServicesAndProviders/${serviceID}`)
    .then(() => {
      const index = this.services.findIndex(service => service.ServiceID === serviceID);
      if (index !== -1) {
        this.services.splice(index, 1);
      }
      this.closeDeleteDialog();
    })
    .catch(error => {
      console.error('Error deleting service:', error);
    });
},
saveService() {
  const serviceID = this.editedItem.ServiceID;
  const organizationID = this.editedItem.OrganizationID;
  console.log('Service ID:', serviceID);
  console.log('Organization ID:', organizationID);

  if (serviceID && organizationID) {
    // Update service details
    axios.put(`http://127.0.0.1:5000/api/ServicesAndProviders/${serviceID}`, {
      ServiceDescription: this.editedItem.ServiceDescription,
    })
      .then(() => {
        // Update service provider details
        axios.put(`http://127.0.0.1:5000/api/Service_providers/${organizationID}`, {
          ContactPerson: this.editedItem.ContactPerson,
          Email: this.editedItem.Email,
          Phone: this.editedItem.Phone,
        })
          .then(() => {
            // Refresh the services data after successful update
            this.fetchServices();
            this.fetchServiceProviders();
            this.closeEditDialog();
          })
          .catch(error => {
            console.error('Error updating service provider:', error);
          });
      })
      .catch(error => {
        console.error('Error updating service:', error);
      });
  } else {
    console.error('Invalid serviceID or organizationID');
  }
},

  addService() {
    axios.post('http://127.0.0.1:5000/api/ServicesAndProviders', this.newService)
      .then(response => {
        this.fetchServices();  //this.services.push(response.data);
        this.closeAddServiceDialog();
      })
      .catch(error => {
        console.error('Error adding service:', error);
      });
  },
  addServiceProvider() {
    axios.post('http://127.0.0.1:5000/api/service_providers', this.newServiceProvider)
      .then(() => {
        this.fetchServiceProviders();
        this.closeAddServiceProviderDialog();
      })
      .catch(error => {
        console.error('Error adding service provider:', error);
      });
  },

  // Utility functions
  formatDate(date) {
    return new Date(date).toLocaleDateString();
  },
},
};
</script>

<!-- // saveItem() {
  //   // Make an API call to update the service
  //   axios.put(`http://127.0.0.1:5000/api/ServicesAndProviders/${this.selectedItem.ServiceID}`, this.editedItem)
  //     .then(() => {
  //       const index = this.services.findIndex(service => service.ServiceID === this.selectedItem.ServiceID);
  //       if (index !== -1) {
  //         this.services.splice(index, 1, this.editedItem);
  //       }
  //       this.closeEditDialog();
  //     })
  //     .catch(error => {
  //       console.error('Error updating service:', error);
  //     });
  // }, -->
