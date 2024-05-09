<template>
  <div>
    <v-card>
      <v-card-title class="d-flex justify-space-between align-center">
        <div>
          <v-btn color="primary" @click="openAddVolunteerDialog">Add Volunteer</v-btn>
          <span class="text-h5 mx-4">Volunteers</span>
        </div>
      </v-card-title>
      <v-data-table
        :headers="headers"
        :items="volunteers"
        :items-per-page="100"
        :loading="loading"
        class="elevation-1"
      >
        <!-- eslint-disable-next-line vue/valid-v-slot -->
        <template v-slot:item.actions="{ item }">
          <v-icon small class="mr-2" @click="openEditDialog(item)">mdi-pencil</v-icon>
          <v-icon small @click="openDeleteDialog(item)">mdi-delete</v-icon>
        </template>
      </v-data-table>
    </v-card>

    <!-- Delete Volunteer Dialog -->
    <v-dialog v-model="deleteDialog" max-width="500px">
      <v-card>
        <v-card-title class="text-h5">Delete Volunteer</v-card-title>
        <v-card-text>Are you sure you want to delete this volunteer?</v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="blue darken-1" text @click="closeDeleteDialog">Cancel</v-btn>
          <v-btn color="blue darken-1" text @click="deleteVolunteer">Delete</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <!-- Edit Volunteer Dialog -->
    <v-dialog v-model="editDialog" max-width="500px">
      <v-card>
        <v-card-title class="text-h5">Edit Volunteer</v-card-title>
        <v-card-text>
          <v-text-field v-model="editedItem.FirstName" label="First Name"></v-text-field>
          <v-text-field v-model="editedItem.LastName" label="Last Name"></v-text-field>
          <v-text-field v-model="editedItem.Email" label="Email"></v-text-field>
          <v-text-field v-model="editedItem.Phone" label="Phone"></v-text-field>
          <v-checkbox v-model="editedItem.HasRecordAccess" label="Has Record Access"></v-checkbox>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="blue darken-1" text @click="closeEditDialog">Cancel</v-btn>
          <v-btn color="blue darken-1" text @click="saveVolunteer">Save</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <!-- Add Volunteer Dialog -->
    <v-dialog v-model="addVolunteerDialog" max-width="500px">
      <v-card>
        <v-card-title class="text-h5">Add Volunteer</v-card-title>
        <v-card-text>
          <v-text-field v-model="newVolunteer.FirstName" label="First Name"></v-text-field>
          <v-text-field v-model="newVolunteer.LastName" label="Last Name"></v-text-field>
          <v-text-field v-model="newVolunteer.Email" label="Email"></v-text-field>
          <v-text-field v-model="newVolunteer.Phone" label="Phone"></v-text-field>
          <v-checkbox v-model="newVolunteer.HasRecordAccess" label="Has Record Access"></v-checkbox>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="blue darken-1" text @click="closeAddVolunteerDialog">Cancel</v-btn>
          <v-btn color="blue darken-1" text @click="addVolunteer">Add</v-btn>
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
      { title: 'First Name', key: 'FirstName' },
      { title: 'Last Name', key: 'LastName' },
      { title: 'Email', key: 'Email' },
      { title: 'Phone', key: 'Phone' },
      { title: 'Has Record Access', key: 'HasRecordAccess' },
      { title: 'Actions', key: 'actions', sortable: false },
    ],
    volunteers: [],
    loading: true,
    deleteDialog: false,
    editDialog: false,
    addVolunteerDialog: false,
    selectedItem: null,
    editedIndex: -1,
    editedItem: {
      FirstName: '',
      LastName: '',
      Email: '',
      Phone: '',
      HasRecordAccess: false,
    },
    defaultItem: {
      FirstName: '',
      LastName: '',
      Email: '',
      Phone: '',
      HasRecordAccess: false,
    },
    newVolunteer: {
      FirstName: '',
      LastName: '',
      Email: '',
      Phone: '',
      HasRecordAccess: false,
    },
  };
},

mounted() {
  this.fetchVolunteers();
},

methods: {
  // Fetching data
  fetchVolunteers() {
    fetch('http://127.0.0.1:5000/api/volunteers')
      .then(response => response.json())
      .then(data => {
        this.volunteers = data;
        console.log('Updated Volunteers:', this.volunteers);
        this.loading = false;
      })
      .catch(error => {
        console.error('Error fetching volunteers:', error);
        this.loading = false;
      });
  },

  // Dialog management
  openEditDialog(item) {
    this.selectedItem = item;
    this.editedItem = {
      VolunteerID: item.VolunteerID,
      FirstName: item.FirstName,
      LastName: item.LastName,
      Email: item.Email,
      Phone: item.Phone,
      HasRecordAccess: item.HasRecordAccess,
    };
    this.editDialog = true;
  },
  closeEditDialog() {
    this.selectedItem = null;
    this.editedItem = {
      VolunteerID: '',
      FirstName: '',
      LastName: '',
      Email: '',
      Phone: '',
      HasRecordAccess: false,
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
  openAddVolunteerDialog() {
    this.addVolunteerDialog = true;
  },
  closeAddVolunteerDialog() {
    this.newVolunteer = {
      FirstName: '',
      LastName: '',
      Email: '',
      Phone: '',
      HasRecordAccess: false,
    };
    this.addVolunteerDialog = false;
  },
// CRUD operations
deleteVolunteer() {
const volunteerID = this.selectedItem.VolunteerID;
axios.delete(`http://127.0.0.1:5000/api/volunteers/${volunteerID}`)
  .then(() => {
    const index = this.volunteers.findIndex(volunteer => volunteer.VolunteerID === volunteerID);
    if (index !== -1) {
      this.volunteers.splice(index, 1);
    }
    this.closeDeleteDialog();
  })
  .catch(error => {
    console.error('Error deleting volunteer:', error);
  });
},
saveVolunteer() {
const volunteerID = this.editedItem.VolunteerID;
console.log('Edited Item:', this.editedItem);
console.log('Volunteer ID:', volunteerID);
if (volunteerID) {
  // Update volunteer details
  axios.put(`http://127.0.0.1:5000/api/volunteers/${volunteerID}`, {
    FirstName: this.editedItem.FirstName,
    LastName: this.editedItem.LastName,
    Email: this.editedItem.Email,
    Phone: this.editedItem.Phone,
    HasRecordAccess: this.editedItem.HasRecordAccess,
  })
    .then(() => {
      // Refresh the volunteers data after successful update
      this.fetchVolunteers();
      this.closeEditDialog();
    })
    .catch(error => {
      console.error('Error updating volunteer:', error);
    });
} else {
  console.error('Invalid volunteerID');
}
},
addVolunteer() {
axios.post('http://127.0.0.1:5000/api/volunteers', this.newVolunteer)
  .then(response => {
    this.volunteers.push(response.data);
    this.closeAddVolunteerDialog();
  })
  .catch(error => {
    console.error('Error adding volunteer:', error);
  });
},
},
};
</script>
