<template>
    <div>
      <data-table
        :edited-item="editedItem"
        @update:edited-item="updateEditedItem"
        @save="saveItem"
        :headers="headers"
        :items="volunteers"
        :default-item="editedItem"
        @edit-item="editItem($event.item, $event.index)"
        @delete-item="deleteItem($event.item, $event.index)"
        @delete-item-confirm="deleteItemConfirm($event)"
        @close="close"
        @close-delete="closeDelete"
        sort-by="NeighborID"
        sort-order="asc"
      ></data-table>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  import DataTable from '@/components/DataTable.vue';
  
  export default {
    components: {
      DataTable,
    },
    data() {
      return {
        headers: [
            { text: 'Neighbor ID', value: 'NeighborID' },
            { text: 'Volunteer ID', value: 'VolunteerID' },
            { text: 'Organization', value: 'Organization' },
            { text: 'First Name', value: 'FirstName' },
            { text: 'Last Name', value: 'LastName' },
            { text: 'Date of Birth', value: 'DateOfBirth' },
            { text: 'Phone', value: 'Phone' },
            { text: 'Location', value: 'Location' },
            { text: 'Email', value: 'Email' },
            { text: 'Created Date', value: 'Created_date' },
            { text: 'Has State ID', value: 'HasStateID' },
            { text: 'Has Pet', value: 'HasPet' },
          ],
          neighbors: [], // This will hold our neighbor data
          editedIndex: -1,
          editedItem: {
            NeighborID: '',
            VolunteerID: '',
            Organization: '',
            FirstName: '',
            LastName: '',
            DateOfBirth: '',
            Phone: '',
            Location: '',
            Email: '',
            CreatedDate: '',
            HasStateID: false,
            HasPet: false,
          },
  
        },
      };
    },
  
  
    created() {
      this.fetchData();
    },
    
    methods: {
      fetchData() {
        axios.get('http://127.0.0.1:5000/api/neighbors')
          .then(response => {
            this.neighbors = response.data;
          })
          .catch(error => {
            console.error('Error fetching data:', error);
          });
      },
      editItem(item, index) {
      this.editedIndex = index;
      this.editedItem = Object.assign({}, item);
      },
      deleteItem(item, index) {
        this.editedIndex = index;
        this.editedItem = Object.assign({}, item);
      },
      deleteItemConfirm(index) {
        // Perform the delete operation in the database
        // Remove the item from the volunteers array using the index
        this.volunteers.splice(index, 1);
        this.closeDelete();
      },
      close() {
        this.editedIndex = -1;
        this.editedItem = Object.assign({}, this.defaultItem);
      },
      closeDelete() {
        this.editedIndex = -1;
        this.editedItem = Object.assign({}, this.defaultItem);
      },
      updateEditedItem(item) {
        this.editedItem = item;
      },
      saveItem(item) {
        if (this.editedIndex > -1) {
          // Perform the update operation in the database
          Object.assign(this.volunteers[this.editedIndex], item);
        } else {
          // Perform the create operation in the database
          this.volunteers.push(item);
        }
        this.close();
      },
    },
  };
  </script>
  
  
    
    <style>
  .v-container {
    max-width: 1200px;
    margin: auto; /* Center the container */
  }
  </style>
  