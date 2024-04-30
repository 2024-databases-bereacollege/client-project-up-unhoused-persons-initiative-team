<template>
  <div>
    <data-table
  tableTitle="Volunteers"  
  :edited-item="editedItem"
  @update:edited-item="updateEditedItem"
  @update:has-record-access="updateHasRecordAccess"
  @save="saveItem"
  :headers="tableHeaders"
  :items="volunteers"
  :default-item="defaultItem"
  :on-edit="editItem"
  :on-delete="deleteItem"
  @delete-item-confirm="deleteItemConfirm($event)"
  @close="close"
  @close-delete="closeDelete"
  sort-by="VolunteerID"
  sort-order="asc"
></data-table>
  </div>
</template>

<script>
// default item above may be edited item instead
import axios from 'axios';
import DataTable from '@/components/DataTable.vue';

export default {
  components: {
    DataTable,
  },
  data() {
    return {
      tableHeaders: [ //keeping this with this name keeps this order, as opposed to 'headers'
        { title: 'Volunteer ID', key: 'VolunteerID' },
        { title: 'First Name', key: 'FirstName' },
        { title: 'Last Name', key: 'LastName' },
        { title: 'Email', key: 'Email' },
        { title: 'Phone', key: 'Phone' },
        { title: 'Has Record Access', key: 'HasRecordAccess' },
        { title: 'Actions', key: 'actions', sortable: false },
      ],
      volunteers: [],
      editedIndex: -1,
      editedItem: {
        VolunteerID: '',
        FirstName: '',
        LastName: '',
        Email: '',
        Phone: '',
        HasRecordAccess: false,
      },
      defaultItem: {
        VolunteerID: '',
        FirstName: '',
        LastName: '',
        Email: '',
        Phone: '',
        HasRecordAccess: false,
      },
    };
  },
  created() {
    this.fetchData();
  },
  methods: {
    fetchData() {
      axios.get('http://127.0.0.1:5000/api/volunteers')
        .then(response => {
          this.volunteers = response.data;
        })
        .catch(error => {
          console.error('Error fetching data:', error);
        });
    },
    saveItem(item) {
    if (this.editedIndex > -1) {
      // Update an existing volunteer
      const volunteerID = this.volunteers[this.editedIndex].VolunteerID;
      axios.put(`http://127.0.0.1:5000/api/volunteers/${volunteerID}`, item)
        .then(response => {
          Object.assign(this.volunteers[this.editedIndex], response.data); //TODO: Maybe this? this.$set(this.volunteers, this.editedIndex, response.data);
          this.close();
        })
        .catch(error => {
          console.error('Error updating volunteer:', error);
        });
    } else {
      // Create a new volunteer
      axios.post('http://127.0.0.1:5000/api/volunteers', item)
        .then(response => {
          this.volunteers.push(response.data);
          this.close();
        })
        .catch(error => {
          console.error('Error creating volunteer:', error);
        });
      }
    },

    deleteItemConfirm(index) {
      const volunteerID = this.volunteers[index].VolunteerID;
      axios.delete(`http://127.0.0.1:5000/api/volunteers/${volunteerID}`)
        .then(() => {
          this.volunteers.splice(index, 1);
          this.closeDelete();
        })
        .catch(error => {
          console.error('Error deleting volunteer:', error);
        });
    },

    editItem(item) {
      this.editedIndex = this.volunteers.indexOf(item);
      this.editedItem = Object.assign({}, item);
    },

    deleteItem(item) {
      this.editedIndex = this.volunteers.indexOf(item);
      this.editedItem = Object.assign({}, item);
    },

    updateHasRecordAccess(value) {
      this.editedItem.HasRecordAccess = value;
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

