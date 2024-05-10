<template>
  <div>
    <v-card>
      <v-card-title class="d-flex justify-space-between align-center">
        <div>
          <v-btn color="primary" @click="openAddNeighborDialog">Add Neighbor</v-btn>
          <span class="text-h5 mx-4">Neighbors</span>
        </div>
      </v-card-title>
      <v-data-table
        :headers="headers"
        :items="neighbors"
        :items-per-page="100"
        :loading="loading"
        class="elevation-1"
      >
        <!-- Slot for the "Neighbor ID" column -->
                <!-- eslint-disable-next-line vue/valid-v-slot -->
  <template v-slot:item.NeighborID="{ item }">
    <v-btn color="primary" small @click="openNeighborPage(item.NeighborID)">
      {{ item.NeighborID }}
    </v-btn>
  </template>
        <!-- eslint-disable-next-line vue/valid-v-slot -->
        <template v-slot:item.actions="{ item }">
          <v-icon small class="mr-2" @click="openEditDialog(item)">mdi-pencil</v-icon>
          <v-icon small @click="openDeleteDialog(item)">mdi-delete</v-icon>
        </template>
      </v-data-table>
    </v-card>

    <!-- Delete Neighbor Dialog -->
    <v-dialog v-model="deleteDialog" max-width="500px">
      <v-card>
        <v-card-title class="text-h5">Delete Neighbor</v-card-title>
        <v-card-text>Are you sure you want to delete this neighbor?</v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="blue darken-1" text @click="closeDeleteDialog">Cancel</v-btn>
          <v-btn color="blue darken-1" text @click="deleteNeighbor">Delete</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

<!-- Edit Neighbor Dialog -->
<v-dialog v-model="editDialog" max-width="500px">
  <v-card>
    <v-card-title class="text-h5">Edit Neighbor</v-card-title>
    <v-card-text>
      <v-text-field v-model="editedItem.FirstName" label="First Name"></v-text-field>
      <v-text-field v-model="editedItem.LastName" label="Last Name"></v-text-field>
      <v-text-field v-model="editedItem.DateOfBirth" label="Date of Birth" type="date"></v-text-field>
      <v-text-field v-model="editedItem.Phone" label="Phone"></v-text-field>
      <v-text-field v-model="editedItem.Location" label="Location"></v-text-field>
      <v-text-field v-model="editedItem.Email" label="Email"></v-text-field>
      <v-checkbox v-model="editedItem.HasStateID" label="Has State ID"></v-checkbox>
      <v-checkbox v-model="editedItem.HasPet" label="Has Pet"></v-checkbox>
      <v-checkbox v-model="editedItem.HasChildren" label="Has Children"></v-checkbox>
      <v-checkbox v-model="editedItem.HasMedication" label="Has Medication"></v-checkbox>
      <v-checkbox v-model="editedItem.HasFoodInsecurity" label="Has Food Insecurity"></v-checkbox>
      <v-checkbox v-model="editedItem.HasTransportation" label="Has Transportation"></v-checkbox>
      <v-checkbox v-model="editedItem.HasJob" label="Has Job"></v-checkbox>
      <v-checkbox v-model="editedItem.HasHousing" label="Has Housing"></v-checkbox>
      <v-checkbox v-model="editedItem.HasInsurance" label="Has Insurance"></v-checkbox>
      <v-checkbox v-model="editedItem.HasIncome" label="Has Income"></v-checkbox>
      <v-text-field v-model="editedItem.Notes" label="Notes"></v-text-field>
    </v-card-text>
    <v-card-actions>
      <v-spacer></v-spacer>
      <v-btn color="blue darken-1" text @click="closeEditDialog">Cancel</v-btn>
      <v-btn color="blue darken-1" text @click="saveNeighbor">Save</v-btn>
    </v-card-actions>
  </v-card>
</v-dialog>

    <!-- Add Neighbor Dialog -->
    <v-dialog v-model="addNeighborDialog" max-width="500px">
  <v-card>
    <v-card-title class="text-h5">Add Neighbor</v-card-title>
    <v-card-text>
      <v-text-field v-model="newNeighbor.FirstName" label="First Name"></v-text-field>
      <v-text-field v-model="newNeighbor.LastName" label="Last Name"></v-text-field>
      <v-text-field v-model="newNeighbor.DateOfBirth" label="Date of Birth" type="date"></v-text-field>
      <v-text-field v-model="newNeighbor.Phone" label="Phone"></v-text-field>
      <v-text-field v-model="newNeighbor.Location" label="Location"></v-text-field>
      <v-text-field v-model="newNeighbor.Email" label="Email"></v-text-field>
      <v-checkbox v-model="newNeighbor.HasStateID" label="Has State ID"></v-checkbox>
      <v-checkbox v-model="newNeighbor.HasPet" label="Has Pet"></v-checkbox>
      <v-checkbox v-model="newNeighbor.HasChildren" label="Has Children"></v-checkbox>
      <v-checkbox v-model="newNeighbor.HasMedication" label="Has Medication"></v-checkbox>
      <v-checkbox v-model="newNeighbor.HasFoodInsecurity" label="Has Food Insecurity"></v-checkbox>
      <v-checkbox v-model="newNeighbor.HasTransportation" label="Has Transportation"></v-checkbox>
      <v-checkbox v-model="newNeighbor.HasJob" label="Has Job"></v-checkbox>
      <v-checkbox v-model="newNeighbor.HasHousing" label="Has Housing"></v-checkbox>
      <v-checkbox v-model="newNeighbor.HasInsurance" label="Has Insurance"></v-checkbox>
      <v-checkbox v-model="newNeighbor.HasIncome" label="Has Income"></v-checkbox>
      <v-text-field v-model="newNeighbor.Notes" label="Notes"></v-text-field>
    </v-card-text>
    <v-card-actions>
      <v-spacer></v-spacer>
      <v-btn color="blue darken-1" text @click="closeAddNeighborDialog">Cancel</v-btn>
      <v-btn color="blue darken-1" text @click="addNeighbor">Add</v-btn>
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
    { title: 'Neighbor ID', key: 'NeighborID', sortable: true, slot: 'item.NeighborID' },
      { title: 'First Name', key: 'FirstName' },
      { title: 'Last Name', key: 'LastName' },
      { title: 'Date of Birth', key: 'DateOfBirth' },
      { title: 'Phone', key: 'Phone' },
      { title: 'Location', key: 'Location' },
      { title: 'Email', key: 'Email' },
      { title: 'Has State ID', key: 'HasStateID' },
      { title: 'Has Pet', key: 'HasPet' },
      { title: 'Has Children', key: 'HasChildren' },
      { title: 'Has Medication', key: 'HasMedication' },
      { title: 'Has Food Insecurity', key: 'HasFoodInsecurity' },
      { title: 'Has Transportation', key: 'HasTransportation' },
      { title: 'Has Job', key: 'HasJob' },
      { title: 'Has Housing', key: 'HasHousing' },
      { title: 'Has Insurance', key: 'HasInsurance' },
      { title: 'Has Income', key: 'HasIncome' },
      { title: 'Notes', key: 'Notes' },
      { title: 'Actions', key: 'actions', sortable: false },
    ],
    neighbors: [],
    loading: true,
    deleteDialog: false,
    editDialog: false,
    addNeighborDialog: false,
    selectedItem: null,
    editedIndex: -1,
    editedItem: {
      NeighborID: '',
      FirstName: '',
      LastName: '',
      DateOfBirth: '',
      Phone: '',
      Location: '',
      Email: '',
      HasStateID: false,
      HasPet: false,
      HasChildren: false,
      HasMedication: false,
      HasFoodInsecurity: false,
      HasTransportation: false,
      HasJob: false,
      HasHousing: false,
      HasInsurance: false,
      HasIncome: false,
      Notes: '',
    },
    defaultItem: {
      NeighborID: '',
      FirstName: '',
      LastName: '',
      DateOfBirth: '',
      Phone: '',
      Location: '',
      Email: '',
      HasStateID: false,
      HasPet: false,
      HasChildren: false,
      HasMedication: false,
      HasFoodInsecurity: false,
      HasTransportation: false,
      HasJob: false,
      HasHousing: false,
      HasInsurance: false,
      HasIncome: false,
      Notes: '',
    },
    newNeighbor: {
      FirstName: '',
      LastName: '',
      DateOfBirth: '',
      Phone: '',
      Location: '',
      Email: '',
      HasStateID: false,
      HasPet: false,
      HasChildren: false,
      HasMedication: false,
      HasFoodInsecurity: false,
      HasTransportation: false,
      HasJob: false,
      HasHousing: false,
      HasInsurance: false,
      HasIncome: false,
      Notes: '',
    },
  };
},

mounted() {
  this.fetchNeighbors();
},

methods: {
  // Fetching data
  fetchNeighbors() {
    axios.get('http://127.0.0.1:5000/api/neighbors')
      .then(response => {
        this.neighbors = response.data;
        console.log('Updated Neighbors:', this.neighbors);
        this.loading = false;
      })
      .catch(error => {
        console.error('Error fetching neighbors:', error);
        this.loading = false;
      });
  },

  // Dialog management
  openEditDialog(item) {
    this.selectedItem = item;
    this.editedItem = {
      NeighborID: item.NeighborID,
      FirstName: item.FirstName,
      LastName: item.LastName,
      DateOfBirth: item.DateOfBirth,
      Phone: item.Phone,
      Location: item.Location,
      Email: item.Email,
      HasStateID: item.HasStateID,
      HasPet: item.HasPet,
      HasChildren: item.HasChildren,
      HasMedication: item.HasMedication,
      HasFoodInsecurity: item.HasFoodInsecurity,
      HasTransportation: item.HasTransportation,
      HasJob: item.HasJob,
      HasHousing: item.HasHousing,
      HasInsurance: item.HasInsurance,
      HasIncome: item.HasIncome,
      Notes: item.Notes,
    };
    this.editDialog = true;
  },
  closeEditDialog() {
    this.selectedItem = null;
    this.editedItem = {
      NeighborID: '',
      FirstName: '',
      LastName: '',
      DateOfBirth: '',
      Phone: '',
      Location: '',
      Email: '',
      HasStateID: false,
      HasPet: false,
      HasChildren: false,
      HasMedication: false,
      HasFoodInsecurity: false,
      HasTransportation: false,
      HasJob: false,
      HasHousing: false,
      HasInsurance: false,
      HasIncome: false,
      Notes: '',
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
  openAddNeighborDialog() {
    this.addNeighborDialog = true;
  },
  closeAddNeighborDialog() {
    this.newNeighbor = {
      FirstName: '',
      LastName: '',
      DateOfBirth: '',
      Phone: '',
      Location: '',
      Email: '',
      HasStateID: false,
      HasPet: false,
      HasChildren: false,
      HasMedication: false,
      HasFoodInsecurity: false,
      HasTransportation: false,
      HasJob: false,
      HasHousing: false,
      HasInsurance: false,
      HasIncome: false,
      Notes: '',
    };
    this.addNeighborDialog = false;
  },

// CRUD operations
deleteNeighbor() {
  const neighborID = this.selectedItem.NeighborID;
  axios.delete(`http://127.0.0.1:5000/api/neighbors/${neighborID}`)
    .then(() => {
      const index = this.neighbors.findIndex(neighbor => neighbor.NeighborID === neighborID);
      if (index !== -1) {
        this.neighbors.splice(index, 1);
      }
      this.closeDeleteDialog();
    })
    .catch(error => {
      console.error('Error deleting neighbor:', error);
    });
},
saveNeighbor() {
  const neighborID = this.editedItem.NeighborID;
  console.log('Edited Item:', this.editedItem);
  console.log('Neighbor ID:', neighborID);
  if (neighborID) {
    // Update neighbor details
    axios.put(`http://127.0.0.1:5000/api/neighbors/${neighborID}`, {
      FirstName: this.editedItem.FirstName,
      LastName: this.editedItem.LastName,
      DateOfBirth: this.editedItem.DateOfBirth,
      Phone: this.editedItem.Phone,
      Location: this.editedItem.Location,
      Email: this.editedItem.Email,
      HasStateID: this.editedItem.HasStateID,
      HasPet: this.editedItem.HasPet,
      HasChildren: this.editedItem.HasChildren,
      HasMedication: this.editedItem.HasMedication,
      HasFoodInsecurity: this.editedItem.HasFoodInsecurity,
      HasTransportation: this.editedItem.HasTransportation,
      HasJob: this.editedItem.HasJob,
      HasHousing: this.editedItem.HasHousing,
      HasInsurance: this.editedItem.HasInsurance,
      HasIncome: this.editedItem.HasIncome,
      Notes: this.editedItem.Notes,
    })
      .then(() => {
        // Refresh the neighbors data after successful update
        this.fetchNeighbors();
        this.closeEditDialog();
        window.dispatchEvent(new Event('refreshData'));

      })
      .catch(error => {
        console.error('Error updating neighbor:', error);
      });
  } else {
    console.error('Invalid neighborID');
  }
},
addNeighbor() {
  axios.post('http://127.0.0.1:5000/api/neighbors', this.newNeighbor)
    .then(response => {
      this.neighbors.push(response.data);
      this.closeAddNeighborDialog();
      // After successfully adding a new neighbor - This refreshes the Add visit page
      window.dispatchEvent(new Event('refreshData'));
    })
    .catch(error => {
      console.error('Error adding neighbor:', error);
    });
},
// This last section allows us to go to NeighborProfile with ID numbers

renderNeighborIDButton(params) {
    return `<v-btn color="primary" small @click="openNeighborPage(${params.value})">${params.value}</v-btn>`;
  },
  openNeighborPage(neighborID) {
    this.$router.push({ name: 'NeighborProfile', params: { ID: neighborID } });
  },
},
};
</script>
