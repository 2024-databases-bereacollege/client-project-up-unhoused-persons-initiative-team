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

    <!-- Edit Dialog -->
    <v-dialog v-model="editDialog" max-width="500px">
      <v-card>
        <v-card-title class="text-h5">Edit Service</v-card-title>
        <v-card-text>
          <!-- Add form fields for editing the service -->
          <v-text-field v-model="editedItem.ServiceType" label="Service Type"></v-text-field>
          <v-text-field v-model="editedItem.ServiceDescription" label="Service Description"></v-text-field>
          <!-- Add more form fields as needed -->
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="blue darken-1" text @click="closeEditDialog">Cancel</v-btn>
          <v-btn color="blue darken-1" text @click="saveItem">Save</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <!-- Delete Dialog -->
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

    <!-- Add Service Dialog -->
    <v-dialog v-model="addServiceDialog" max-width="500px">
      <v-card>
        <v-card-title class="text-h5">Add Service</v-card-title>
        <v-card-text>
          <!-- Add form fields for creating a new service -->
          <v-text-field v-model="newService.ServiceType" label="Service Type"></v-text-field>
          <v-text-field v-model="newService.ServiceDescription" label="Service Description"></v-text-field>
          <!-- Add more form fields as needed -->
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
          <!-- Add form fields for creating a new service provider -->
          <v-text-field v-model="newServiceProvider.OrganizationName" label="Organization Name"></v-text-field>
          <v-text-field v-model="newServiceProvider.ContactPerson" label="Contact Person"></v-text-field>
          <!-- Add more form fields as needed -->
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
        ServiceType: '',
        ServiceDescription: '',
        Organization_Name: '',
        ContactPerson: '',
        Email: '',
        Phone: '',
        DateOfStart: '',
        TotalNeighbors: 0,
      },
      defaultItem: {
        ServiceType: '',
        ServiceDescription: '',
        Organization_Name: '',
        ContactPerson: '',
        Email: '',
        Phone: '',
        DateOfStart: '',
        TotalNeighbors: 0,
      },
      newService: {
        ServiceType: '',
        ServiceDescription: '',
        // Add more properties as needed
      },
      newServiceProvider: {
        OrganizationName: '',
        ContactPerson: '',
        // Add more properties as needed
      },
    };
  },
  mounted() {
    this.fetchServices();
  },
  methods: {
    fetchServices() {
  fetch('http://127.0.0.1:5000/api/ServicesAndProviders')
    .then(response => response.json())
    .then(data => {
      this.services = data;
      this.loading = false;
    })
    .catch(error => {
      console.error('Error fetching services:', error);
      this.loading = false;
    });
},
formatDate(date) {
  return new Date(date).toLocaleDateString();
},
openEditDialog(item) {
      this.selectedItem = item;
      this.editedItem = Object.assign({}, item);
      this.editDialog = true;
    },
    closeEditDialog() {
      this.selectedItem = null;
      this.editedItem = {
        ServiceType: '',
        ServiceDescription: '',
        // Reset other properties as needed
      };
      this.editDialog = false;
    },
    saveItem() {
      // Make an API call to update the service
      axios.put(`http://127.0.0.1:5000/api/ServicesAndProviders/${this.selectedItem.ServiceID}`, this.editedItem)
        .then(() => {
          const index = this.services.findIndex(service => service.ServiceID === this.selectedItem.ServiceID);
          if (index !== -1) {
            this.services.splice(index, 1, this.editedItem);
          }
          this.closeEditDialog();
        })
        .catch(error => {
          console.error('Error updating service:', error);
        });
    },
    openDeleteDialog(item) {
      this.selectedItem = item;
      this.deleteDialog = true;
    },
    closeDeleteDialog() {
      this.selectedItem = null;
      this.deleteDialog = false;
    },
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
    openAddServiceDialog() {
      this.addServiceDialog = true;
    },
    closeAddServiceDialog() {
      this.newService = {
        ServiceType: '',
        ServiceDescription: '',
        // Reset other properties as needed
      };
      this.addServiceDialog = false;
    },
    addService() {
      // Make an API call to create a new service
      axios.post('http://127.0.0.1:5000/api/ServicesAndProviders', this.newService)
        .then(response => {
          this.services.push(response.data);
          this.closeAddServiceDialog();
        })
        .catch(error => {
          console.error('Error adding service:', error);
        });
    },
    openAddServiceProviderDialog() {
      this.addServiceProviderDialog = true;
    },
    closeAddServiceProviderDialog() {
      this.newServiceProvider = {
        OrganizationName: '',
        ContactPerson: '',
        // Reset other properties as needed
      };
      this.addServiceProviderDialog = false;
    },
    addServiceProvider() {
  // Make an API call to create a new service provider
  axios.post('http://127.0.0.1:5000/api/service_providers', this.newServiceProvider)
    //.then(response => {
      .then(() => {
      // Update the services list by fetching the updated data from the API
      this.fetchServices();
      this.closeAddServiceProviderDialog();
    })
    .catch(error => {
      console.error('Error adding service provider:', error);
    });
    },
  },
};
</script>
