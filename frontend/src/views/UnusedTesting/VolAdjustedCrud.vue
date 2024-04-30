<template>
    <v-data-table
      :headers="headers"
      :items="items"
      :sort-by="[{ key: 'FirstName', order: 'asc' }]"
    >
      <template v-slot:top>
        <v-toolbar
          flat
        >
          <v-toolbar-title>Volunteers</v-toolbar-title>
          <v-divider
            class="mx-4"
            inset
            vertical
          ></v-divider>
          <v-spacer></v-spacer>
          <v-dialog
            v-model="dialog"
            max-width="500px"
          >
            <template v-slot:activator="{ props }">
              <v-btn
                class="mb-2"
                color="primary"
                dark
                v-bind="props"
              >
                New Item
              </v-btn>
            </template>
            <v-card>
              <v-card-title>
                <span class="text-h5">{{ formTitle }}</span>
              </v-card-title>
  
              <v-card-text>
                <v-container>
                  <v-row>
                    <v-col
                      cols="12"
                      md="4"
                      sm="6"
                    >
                      <v-text-field
                        v-model="editedItem.FirstName"
                        label="First Name"
                      ></v-text-field>
                    </v-col>
                    <v-col
                      cols="12"
                      md="4"
                      sm="6"
                    >
                      <v-text-field
                        v-model="editedItem.LastName"
                        label="Last Name"
                      ></v-text-field>
                    </v-col>
                    <v-col
                      cols="12"
                      md="4"
                      sm="6"
                    >
                      <v-text-field
                        v-model="editedItem.Password"
                        label="Password"
                      ></v-text-field>
                    </v-col>
                    <v-col
                      cols="12"
                      md="4"
                      sm="6"
                    >
                      <v-text-field
                        v-model="editedItem.Email"
                        label="Email"
                      ></v-text-field>
                    </v-col>
                    <v-col
                      cols="12"
                      md="4"
                      sm="6"
                    >
                      <v-text-field
                        v-model="editedItem.Phone"
                        label="Phone"
                      ></v-text-field>
                    </v-col>
                    <v-checkbox v-model="newVolunteer.HasRecordAccess" label="Has Record Access"></v-checkbox>
                  </v-row>
                </v-container>
              </v-card-text>
  
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn
                  color="blue-darken-1"
                  variant="text"
                  @click="close"
                >
                  Cancel
                </v-btn>
                <v-btn
                  color="blue-darken-1"
                  variant="text"
                  @click="save"
                >
                  Save
                </v-btn>
              </v-card-actions>
            </v-card>
          </v-dialog>
          <v-dialog v-model="dialogDelete" max-width="500px">
            <v-card>
              <v-card-title class="text-h5">Are you sure you want to delete this item?</v-card-title>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="blue-darken-1" variant="text" @click="closeDelete">Cancel</v-btn>
                <v-btn color="blue-darken-1" variant="text" @click="deleteItemConfirm">OK</v-btn>
                <v-spacer></v-spacer>
              </v-card-actions>
            </v-card>
          </v-dialog>
        </v-toolbar>
      </template>
  <!-- eslint-disable-next-line vue/valid-v-slot -->
  <template v-slot:item.actions="{ item }">
        <v-icon
          class="me-2"
          size="small"
          @click="editItem(item)"
        >
          mdi-pencil
        </v-icon>
        <v-icon
          size="small"
          @click="deleteItem(item)"
        >
          mdi-delete
        </v-icon>
      </template>
      <template v-slot:no-data>
        <v-btn
          color="primary"
          @click="initialize"
        >
          Reset
        </v-btn>
      </template>
    </v-data-table>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        dialog: false,
        headers: [
        { text: 'Volunteer ID', value: 'VolunteerID' },
        { text: 'First Name', value: 'FirstName' },
        { text: 'Last Name', value: 'LastName' },
        { text: 'Password', value: 'Password', sortable: false }, // Typically not displayed or editable directly for security
        { text: 'Email', value: 'Email' },
        { text: 'Phone', value: 'Phone' },
        { text: 'Has Record Access', value: 'HasRecordAccess' }
      ],
      tableData: [],
      newVolunteer: {
        VolunteerID: null, // Assuming ID is auto-generated by the backend and not needed on creation
        FirstName: '',
        LastName: '',
        Password: '', // Consider security implications and proper handling
        Email: '',
        Phone: '',
        HasRecordAccess: false
      }
      };
    },
    methods: {
      showDialog() {
        this.dialog = true;
      },
      closeDialog() {
        this.dialog = false;
      },
      saveVolunteer() {
    console.log("Data being sent:", this.newVolunteer);
    axios.post('http://127.0.0.1:5000/api/volunteers', this.newVolunteer)
      .then(response => {
        this.tableData.push(response.data);
        this.newVolunteer = { FirstName: '', LastName: '', Email: '', Phone: '', HasRecordAccess: false };
        this.dialog = false;
      })
      .catch(error => {
        console.error('Error saving volunteer:', error);
        alert('Failed to save the volunteer. Please check the console for more details.');
      });
  },
      fetchData() {
        axios.get('http://127.0.0.1:5000/api/volunteers')
          .then(response => {
            this.tableData = response.data;
            if (this.tableData.length > 0) {
              this.headers = Object.keys(this.tableData[0]).map(key => ({
                text: key.charAt(0).toUpperCase() + key.slice(1),
                value: key
              }));
            }
          })
          .catch(error => console.error('Error fetching volunteers:', error));
      }
    },
    mounted() {
      this.fetchData();
    }
  }
  </script>
  