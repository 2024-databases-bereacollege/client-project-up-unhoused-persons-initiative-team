<template>
    <div>
      <v-data-table
        :headers="headers"
        :items="neighbors"
        :sort-by="['Created_date']"
        :sort-desc="[true]"
        class="elevation-1"
      >
        <template v-slot:top>
          <v-toolbar flat>
            <v-toolbar-title>Neighbors</v-toolbar-title>
            <v-divider class="mx-4" inset vertical></v-divider>
            <v-spacer></v-spacer>
            <v-dialog v-model="dialog" max-width="500px">
              <template v-slot:activator="{ on, attrs }">
                <v-btn color="primary" dark v-bind="attrs" v-on="on">
                  New Neighbor
                </v-btn>
              </template>
              <v-card>
                <v-card-title>
                  <span class="text-h5">{{ formTitle }}</span>
                </v-card-title>
                <v-card-text>
                  <v-container>
                    <!-- Add input fields for neighbor properties -->
                    <v-text-field v-model="editedItem.FirstName" label="First Name"></v-text-field>
                    <v-text-field v-model="editedItem.LastName" label="Last Name"></v-text-field>
                    <v-menu v-model="dateMenu" :close-on-content-click="false" :nudge-right="40" transition="scale-transition" offset-y min-width="auto">
                      <template v-slot:activator="{ on, attrs }">
                        <v-text-field v-model="editedItem.DateOfBirth" label="Date of Birth" prepend-icon="mdi-calendar" readonly v-bind="attrs" v-on="on"></v-text-field>
                      </template>
                      <v-date-picker v-model="editedItem.DateOfBirth" @input="dateMenu = false"></v-date-picker>
                    </v-menu>
                    <v-text-field v-model="editedItem.Phone" label="Phone"></v-text-field>
                    <v-textarea v-model="editedItem.Location" label="Location"></v-textarea>
                    <v-text-field v-model="editedItem.Email" label="Email"></v-text-field>
                    <v-checkbox v-model="editedItem.HasStateID" label="Has State ID"></v-checkbox>
                    <v-checkbox v-model="editedItem.HasPet" label="Has Pet"></v-checkbox>
                  </v-container>
                </v-card-text>
                <v-card-actions>
                  <v-spacer></v-spacer>
                  <v-btn color="blue darken-1" text @click="close">Cancel</v-btn>
                  <v-btn color="blue darken-1" text @click="save">Save</v-btn>
                </v-card-actions>
              </v-card>
            </v-dialog>
          </v-toolbar>
        </template>
        <!-- eslint-disable-next-line vue/valid-v-slot -->
        <template v-slot:item.actions="{ item }">
          <v-icon small class="mr-2" @click="editItem(item)">mdi-pencil</v-icon>
          <v-icon small @click="deleteItem(item)">mdi-delete</v-icon>
        </template>
        <template v-slot:no-data>
          <v-btn color="primary" @click="initialize">Reset</v-btn>
        </template>
      </v-data-table>
    </div>
  </template>
  
  
  <!-- <template>
    <div>
      <v-data-table
        :headers="headers"
        :items="neighbors"
        :sort-by="['Created_date']"
        :sort-desc="[true]"
        class="elevation-1"
      >
        <template v-slot:top>
          <v-toolbar flat>
            <v-toolbar-title>Neighbors</v-toolbar-title>
            <v-divider class="mx-4" inset vertical></v-divider>
            <v-spacer></v-spacer>
            <v-dialog v-model="dialog" max-width="500px">
    <template v-slot:activator="{ on, attrs }">
      <v-btn color="primary" dark v-bind="attrs" v-on="on">
        New Neighbor
      </v-btn>
    </template>
    <v-card>
      <v-card-title>
        <span class="text-h5">{{ formTitle }}</span>
      </v-card-title>
      <v-card-text>
        <v-container>
          <-- Add input fields for neighbor properties --
          <v-text-field v-model="editedItem.FirstName" label="First Name"></v-text-field>
          <v-text-field v-model="editedItem.LastName" label="Last Name"></v-text-field>
          <v-menu v-model="dateMenu" :close-on-content-click="false" :nudge-right="40" transition="scale-transition" offset-y min-width="auto">
            <template v-slot:activator="{ on, attrs }">
              <v-text-field v-model="editedItem.DateOfBirth" label="Date of Birth" prepend-icon="mdi-calendar" readonly v-bind="attrs" v-on="on"></v-text-field>
            </template>
            <v-date-picker v-model="editedItem.DateOfBirth" @input="dateMenu = false"></v-date-picker>
          </v-menu>
          <v-text-field v-model="editedItem.Phone" label="Phone"></v-text-field>
          <v-textarea v-model="editedItem.Location" label="Location"></v-textarea>
          <v-text-field v-model="editedItem.Email" label="Email"></v-text-field>
          <v-checkbox v-model="editedItem.HasStateID" label="Has State ID"></v-checkbox>
          <v-checkbox v-model="editedItem.HasPet" label="Has Pet"></v-checkbox>
        </v-container>
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn color="blue darken-1" text @click="close">Cancel</v-btn>
        <v-btn color="blue darken-1" text @click="save">Save</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
          </v-toolbar>
        </template>
        <-- eslint-disable-next-line vue/valid-v-slot --
        <template v-slot:item.actions="{ item }">
          <v-icon small class="mr-2" @click="editItem(item)">mdi-pencil</v-icon>
          <v-icon small @click="deleteItem(item)">mdi-delete</v-icon>
        </template>
        <template v-slot:no-data>
          <v-btn color="primary" @click="initialize">Reset</v-btn>
        </template>
      </v-data-table>
    </div>
  </template> -->
  
  <script>
  import axios from 'axios';
  
  export default {
    data: () => ({
      dialog: false,
      dialogDelete: false,
      headers: [
        { text: 'Neighbor ID', value: 'NeighborID'}, // needs to be a custom slot
        { text: 'First Name', value: 'FirstName' },
        { text: 'Last Name', value: 'LastName' },
        { text: 'Date of Birth', value: 'DateOfBirth' },
        { text: 'Phone', value: 'Phone' },
        { text: 'Location', value: 'Location' },
        { text: 'Email', value: 'Email' },
        { text: 'Created Date', value: 'Created_date' },
        { text: 'Has State ID', value: 'HasStateID' },
        { text: 'Has Pet', value: 'HasPet' },
        { text: 'Actions', value: 'actions', sortable: false },
      ],
      neighbors: [],
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
      },
      dateMenu: false,
    }),
  
    computed: {
      formTitle() {
        return this.editedIndex === -1 ? 'New Neighbor' : 'Edit Neighbor';
      },
    },
  
    watch: {
      dialog(val) {
        val || this.close();
      },
      dialogDelete(val) {
        val || this.closeDelete();
      },
    },
  
    created() {
      this.initialize();
    },
  
    methods: {
      initialize() {
        this.getResponse();
      },
  
      // Fetch neighbor data from backend
      getResponse() {
        const path = 'http://127.0.0.1:5000/api/neighbors';
        axios
          .get(path)
          .then((response) => {
            this.neighbors = response.data;
          })
          .catch((error) => {
            console.error(error);
          });
      },
  
      editItem(item) {
        this.editedIndex = this.neighbors.indexOf(item);
        this.editedItem = Object.assign({}, item);
        this.dialog = true;
      },
  
      deleteItem(item) {
        this.editedIndex = this.neighbors.indexOf(item);
        this.editedItem = Object.assign({}, item);
        this.dialogDelete = true;
      },
  
      deleteItemConfirm() {
        const neighborID = this.neighbors[this.editedIndex].NeighborID;
        axios
          .delete(`http://127.0.0.1:5000/api/neighbors/${neighborID}`)
          .then(() => {
            this.neighbors.splice(this.editedIndex, 1);
            this.closeDelete();
          })
          .catch((error) => {
            console.error('Error deleting neighbor:', error);
          });
      },
  
      close() {
        this.dialog = false;
        this.$nextTick(() => {
          this.editedItem = Object.assign({}, this.defaultItem);
          this.editedIndex = -1;
        });
      },
  
      closeDelete() {
        this.dialogDelete = false;
        this.$nextTick(() => {
          this.editedItem = Object.assign({}, this.defaultItem);
          this.editedIndex = -1;
        });
      },
  
      save() {
        if (this.editedIndex > -1) {
          const neighborID = this.neighbors[this.editedIndex].NeighborID;
          axios
            .put(`http://127.0.0.1:5000/api/neighbors/${neighborID}`, this.editedItem)
            .then((response) => {
              Object.assign(this.neighbors[this.editedIndex], response.data);
              this.close();
            })
            .catch((error) => {
              console.error('Error updating neighbor:', error);
            });
        } else {
          axios
            .post('http://127.0.0.1:5000/api/neighbors', this.editedItem)
            .then((response) => {
              this.neighbors.push(response.data);
              this.close();
            })
            .catch((error) => {
              console.error('Error creating neighbor:', error);
            });
        }
      },
    },
  };
  </script>
  