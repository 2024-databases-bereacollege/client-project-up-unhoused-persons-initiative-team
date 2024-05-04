<template>
    <div class="neighbor-list">
      <h1>Neighbor List</h1>
      <table>
        <thead>
          <tr>
            <th>First Name</th>
            <th>Last Name</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="neighbor in neighbors" :key="neighbor.NeighborID">
            <td>
              <button @click="goToNeighborPage(neighbor.NeighborID)">
                {{ neighbor.FirstName }}
              </button>
            </td>
            <td>{{ neighbor.LastName }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </template>
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        neighbors: [],
      };
    },
    mounted() {
      axios.get('http://127.0.0.1:5000/api/neighbors')
        .then(response => {
          this.neighbors = response.data;
        })
        .catch(error => {
          console.error(error);
        });
    },
    methods: {
      goToNeighborPage(neighborID) {
        this.$router.push(`/${neighborID}`);
      },
    },
  };
  </script>
  <style scoped>
  table {
    width: 100%;
    border-collapse: collapse;
  }
  
  th, td {
    padding: 8px;
    text-align: left;
    border-bottom: 1px solid #ddd;
  }
  
  button {
    background: none;
    border: none;
    color: blue;
    text-decoration: underline;
    cursor: pointer;
  }
  </style>
  <!-- 
      // Fetch visit records from the API based on neighborID
      // Update the `visitRecords` data property with the fetched data
      // Example:
      // axios.get(`/api/neighbors/${neighborID}/visits`)
      //   .then(response => {
      //     this.visitRecords = response.data;
      //   })
      //   .catch(error => {
      //     console.error(error);
      //   }); -->
  
  <!-- <style scoped>
  .neighbor-profile {
    max-width: 600px;
    margin: 0 auto;
    padding: 20px;
  }
  
  h2 {
    font-size: 24px;
    margin-bottom: 20px;
  }
  
  table {
    width: 100%;
    border-collapse: collapse;
    margin-bottom: 20px;
  }
  
  th,
  td {
    padding: 10px;
    text-align: left;
    border-bottom: 1px solid #ddd;
  }
  
  th {
    font-weight: bold;
  }
  
  i {
    margin-right: 5px;
  }
  </style>
  
  
   -->
  
  <!-- <template>
      <div class="neighbor-profile">
        <h2>{{ Neighbor.FirstName }} {{ Neighbor.NastName }}</h2>
        <table>
          -- Display neighbor information in a table --
          <tr>
            <th>Date of Birth</th>
            <td>{{ Neighbor.DateOfBirth }}</td>
          </tr>
          <-- Add more rows for other neighbor information --
        </table>
    
        <h3>Visit Records</h3>
        <VisitRecords :visits="visitRecords" />
      </div>
    </template>
    
    <script>
    import IndividualVisitLog from './IndividualVisitLog.vue';
    
    export default {
      components: {
        IndividualVisitLog,
      },
      data() {
        return {
          Neighbor: {},
          visitRecords: [],
        };
      },
      mounted() {
        const NeighborID = this.$route.params.ID;
        // Fetch neighbor information and visit records from the API
        // Update the `neighbor` and `visitRecords` data properties
      },
    };
    </script> -->
  