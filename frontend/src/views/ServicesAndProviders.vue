<template>
  <div>
    <v-card>
      <v-card-title>
        <span class="text-h5">Services and Providers</span>
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
          <v-icon small class="mr-2" @click="editItem(item)">mdi-pencil</v-icon>
          <v-icon small @click="openDeleteDialog(item)">mdi-delete</v-icon>
        </template>
      </v-data-table>
    </v-card>

    <v-dialog v-model="deleteDialog" max-width="500px">
      <v-card>
        <v-card-title class="text-h5">Delete Service?</v-card-title>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="blue darken-1" text @click="closeDeleteDialog">Cancel</v-btn>
          <v-btn color="blue darken-1" text @click="deleteService">OK</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <v-dialog v-model="deleteProviderDialog" max-width="500px">
      <v-card>
        <v-card-title class="text-h5">Delete Service Provider?</v-card-title>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="blue darken-1" text @click="closeDeleteProviderDialog">Cancel</v-btn>
          <v-btn color="blue darken-1" text @click="deleteServiceProvider">OK</v-btn>
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
      deleteProviderDialog: false,
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
editItem(item) {
      this.editedIndex = this.services.indexOf(item);
      this.editedItem = Object.assign({}, item);
      // Open a dialog or form to edit the item
      // You can use Vuetify's v-dialog component or create a separate form component
      // Pass the editedItem to the dialog or form for editing
      // Example:
      // this.$refs.editDialog.open(this.editedItem);
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
          this.openDeleteProviderDialog();
        })
        .catch(error => {
          console.error('Error deleting service:', error);
        });
    },
    openDeleteProviderDialog() {
      this.deleteProviderDialog = true;
    },
    closeDeleteProviderDialog() {
      this.selectedItem = null;
      this.deleteProviderDialog = false;
    },
    deleteServiceProvider() {
      const organizationID = this.selectedItem.OrganizationID;
      axios.delete(`http://127.0.0.1:5000/api/service_providers/${organizationID}`)
        .then(() => {
          // Remove the service provider from the services array
          this.services = this.services.filter(service => service.OrganizationID !== organizationID);
          this.closeDeleteProviderDialog();
        })
        .catch(error => {
          console.error('Error deleting service provider:', error);
        });

      this.closeDeleteProviderDialog();
    },
    saveItem() {
      if (this.editedIndex > -1) {
        // Make an API call to update the item on the server
        fetch(`http://127.0.0.1:5000/api/ServicesAndProviders/${this.editedItem.ServiceID}`, {
          method: 'PUT',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(this.editedItem),
        })
          .then(response => {
            if (response.ok) {
              // Update the item in the services array if the update was successful
              Object.assign(this.services[this.editedIndex], this.editedItem);
            } else {
              // Handle error if the update failed
              console.error('Failed to update item');
            }
          })
          .catch(error => {
            console.error('Error updating item:', error);
          });
      } else {
        // Make an API call to create a new item on the server
        fetch('http://127.0.0.1:5000/api/ServicesAndProviders', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(this.editedItem),
        })
          .then(response => response.json())
          .then(data => {
            // Add the new item to the services array if the creation was successful
            this.services.push(data);
          })
          .catch(error => {
            console.error('Error creating item:', error);
          });
      }
      this.close();
    },
    close() {
      this.editedIndex = -1;
      this.editedItem = Object.assign({}, this.defaultItem);
      // Close the dialog or form
      // Example:
      // this.$refs.editDialog.close();
    },
  },
};
</script>

