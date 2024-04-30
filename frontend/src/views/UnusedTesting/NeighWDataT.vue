<template>
    <v-container>
      <v-data-table
        :headers="headers"
        :items="neighbors"
        class="elevation-1"
      ></v-data-table>
    </v-container>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    name: 'NeighborTable',
    data() {
      return {
        // Define headers based on the mock neighbor object structure
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
      };
    },
    methods: {
      // Fetch neighbor data from backend
      getResponse() {
        const path = 'http://127.0.0.1:5000/api/neighbors';
        //const path = 'http://localhost:8080/Neighbors'; originial and changed to correct path

        axios.get(path)
          .then(response => {
            // Assuming the response is a single neighbor object
            this.neighbors = [response.data]; // Wrap the object in an array
          })
          .catch(error => {
            console.error(error);
          });
      },
    },
    created() {
      this.getResponse(); // Fetch data when component is created
    },
  };
  </script>
  
  <style>
.v-container {
  max-width: 1200px;
  margin: auto; /* Center the container */
}
</style>
