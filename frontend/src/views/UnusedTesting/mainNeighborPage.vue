<!--This is a test page, that allows the user to click on a neighbors first name to go to their individual page.-->
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
