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
      <!--Service attributes-->
      <v-text-field v-model="editedItem.ServiceType" label="Service Type"></v-text-field>
      <v-text-field v-model="editedItem.ServiceDescription" label="Service Description"></v-text-field>
      <!--Service provider attributes-->
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
          <v-textarea
            v-model="newService.ServiceDescription"
            label="Service Description"
            variant="solo-filled"
            rows="3"
            auto-grow
          ></v-textarea>
          <ServiceProviderSelect
            :items="serviceProviders"
            label="Select Service Provider"
            @update:model-value="newService.OrganizationID = $event"
          />
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
      <v-text-field v-model="newServiceProvider.DateOfStart" label="Date Of Start" type="date"></v-text-field>
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
  components: {
    ServiceProviderSelect,
  },
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
      serviceProviders: [],
      loading: true,
      deleteDialog: false,
      editDialog: false,
      addServiceDialog: false,
      addServiceProviderDialog: false,
      selectedItem: null,
      editedIndex: -1,
      editedItem: {
        ServiceID: '',
        ServiceType: '',
        ServiceDescription: '',
        OrganizationID: '',
        ContactPerson: '',
        Email: '',
        Phone: '',
      },
      defaultItem: {
    ServiceID: '',
    ServiceType: '',
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
    ServiceType: item.ServiceType,
    ServiceDescription: item.ServiceDescription,
    OrganizationID: item.OrganizationID ? item.OrganizationID.OrganizationID : '',
    Organization_Name: item.OrganizationID ? item.OrganizationID.Organization_Name : '',
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
    ServiceType: '',
    ServiceDescription: '',
    OrganizationID: '',
    Organization_Name: '',
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

async saveService() {
  try {
    const serviceRequestData = {
  ServiceID: this.editedItem.ServiceID,
  ServiceType: this.editedItem.ServiceType,
  OrganizationID: this.editedItem.OrganizationID,
  ServiceDescription: this.editedItem.ServiceDescription,
};

const serviceProviderRequestData = {
  OrganizationID: this.editedItem.OrganizationID,
  Organization_Name: this.editedItem.Organization_Name,
  ContactPerson: this.editedItem.ContactPerson,
  Email: this.editedItem.Email,
  Phone: this.editedItem.Phone,
  DateOfStart: this.editedItem.DateOfStart,
};


    console.log('Service Request Data:', serviceRequestData);
    console.log('Service Provider Request Data:', serviceProviderRequestData);

    // Update service
    const serviceResponse = await axios.put(
      `http://127.0.0.1:5000/api/services/${serviceRequestData.ServiceID}`,
      serviceRequestData
    );
    console.log('Service updated successfully:', serviceResponse.data);

    // Update service provider
    const serviceProviderResponse = await axios.put(
      `http://127.0.0.1:5000/api/service_providers/${serviceProviderRequestData.OrganizationID}`,
      serviceProviderRequestData
    );
    console.log('Service provider updated successfully:', serviceProviderResponse.data);

    // Handle success response
    this.fetchServices();
    this.fetchServiceProviders();
    this.closeEditDialog();
    window.dispatchEvent(new Event('refreshData'));
  } catch (error) {
    console.error('Error updating service or service provider:', error);
    // Handle error
  }
},

async addService() {
  try {
    const requestData = {
      ServiceType: this.newService.ServiceType,
      OrganizationID: this.newService.OrganizationID ? this.newService.OrganizationID.value : null,
      ServiceDescription: this.newService.ServiceDescription,
    };
    console.log('Request Data:', requestData);
    const response = await axios.post('http://127.0.0.1:5000/api/services', requestData);
    console.log('Service added successfully:', response.data);
    // Handle success response
    this.fetchServices();
    this.closeAddServiceDialog();
    window.dispatchEvent(new Event('refreshData'));
  } catch (error) {
    console.error('Error adding service:', error);
    // Handle error
  }
},
async addServiceProvider() {
  try {
    const requestData = {
      Organization_Name: this.newServiceProvider.Organization_Name,
      ContactPerson: this.newServiceProvider.ContactPerson,
      Email: this.newServiceProvider.Email,
      Phone: this.newServiceProvider.Phone,
      DateOfStart: this.newServiceProvider.DateOfStart,
    };
    console.log('Request Data:', requestData);
    const response = await axios.post('http://127.0.0.1:5000/api/service_providers', requestData);
    console.log('Service provider added successfully:', response.data);
    // Handle success response
    this.fetchServiceProviders();
    this.closeAddServiceProviderDialog();
    window.dispatchEvent(new Event('refreshData'));
  } catch (error) {
    console.error('Error adding service provider:', error);
    // Handle error
  }
},

  // Utility functions
  formatDate(date) {
    return new Date(date).toLocaleDateString();
  },
  onProviderSelected(providerId) {
      this.newService.OrganizationID = providerId;
},
},
};
</script>

