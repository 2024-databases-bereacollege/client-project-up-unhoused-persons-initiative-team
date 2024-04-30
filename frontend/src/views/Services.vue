<template>
  <div>
    <data-table
      tableTitle="Services"
      :edited-item="editedItem"
      @update:edited-item="updateEditedItem"
      @update:has-state-id="updateHasStateID"
      @update:has-pet="updateHasPet"
      @save="saveItem"
      :headers="tableHeaders"
      :items="neighbors"
      :default-item="defaultItem"
      :on-edit="editItem"
      :on-delete="deleteItem"
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
import DataTable from '@/components/NeighborDataTable.vue';

export default {
  components: {
    DataTable,
  },
  data() {
    return {
      tableHeaders: [
      {
    title: 'Neighbor ID',
    key: 'NeighborID',
    sortable: true,
    cellRenderer: this.renderNeighborIDLink,
  },
        { title: 'First Name', key: 'FirstName' },
        { title: 'Last Name', key: 'LastName' },
        { title: 'Date of Birth', key: 'DateOfBirth' },
        { title: 'Phone', key: 'Phone' },
        { title: 'Location', key: 'Location' },
        { title: 'Email', key: 'Email' },
        { title: 'Created Date', key: 'Created_date' },
        { title: 'Has State ID', key: 'HasStateID' },
        { title: 'Has Pet', key: 'HasPet' },
        { title: 'Actions', key: 'actions', sortable: false },

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
        Created_date: '',
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
        Created_date: '',
        HasStateID: false,
        HasPet: false,
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
    saveItem(item) {
  if (this.editedIndex > -1) {
    // Update an existing neighbor
    const neighborID = this.neighbors[this.editedIndex].NeighborID;
    axios.put(`http://127.0.0.1:5000/api/neighbors/${neighborID}`, item)
      .then(response => {
        Object.assign(this.neighbors[this.editedIndex], response.data);
        this.close();
      })
      .catch(error => {
        console.error('Error updating neighbor:', error);
      });
  } else {
    // Create a new neighbor
    // eslint-disable-next-line no-unused-vars
    const { NeighborID, ...newNeighbor } = item; // Exclude NeighborID from the item object

    newNeighbor.Created_date = new Date().toISOString();

    axios.post('http://127.0.0.1:5000/api/neighbors', newNeighbor)
      .then(response => {
        this.neighbors.push(response.data);
        this.close();
      })
      .catch(error => {
        console.error('Error creating neighbor:', error);
      });
      }
    },
    deleteItemConfirm(index) {
      const neighborID = this.neighbors[index].NeighborID;
      axios.delete(`http://127.0.0.1:5000/api/neighbors/${neighborID}`)
        .then(() => {
          this.neighbors.splice(index, 1);
          this.closeDelete();
        })
        .catch(error => {
          console.error('Error deleting neighbor:', error);
        });
    },
    editItem(item) {
      this.editedIndex = this.neighbors.indexOf(item);
      this.editedItem = Object.assign({}, item);
    },
    renderNeighborIDLink(neighborID) {
    return `<router-link to="/neighbors/${neighborID}">${neighborID}</router-link>`;
  },
    deleteItem(item) {
      this.editedIndex = this.neighbors.indexOf(item);
      this.editedItem = Object.assign({}, item);
    },
    updateHasStateID(value) {
      this.editedItem.HasStateID = value;
    },
    updateHasPet(value) {
      this.editedItem.HasPet = value;
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
  },
};
</script>
