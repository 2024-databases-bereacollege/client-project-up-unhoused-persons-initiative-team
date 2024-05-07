<template>
    <v-card>
      <v-tabs bg-color="deep-purple-darken-4" center-active>
        <v-tab>Has State ID</v-tab>
        <v-tab>Has Pet</v-tab>
        <v-tab>Has Children</v-tab>
        <v-tab>Has Medication</v-tab>
        <v-tab>Has Food Insecurity</v-tab>
        <v-tab>Has Transportation</v-tab>
        <v-tab>Has Job</v-tab>
        <v-tab>Has Housing</v-tab>
        <v-tab>Has Income</v-tab>
      </v-tabs>
      
      <v-tab-item>
      <!-- Content for "Has State ID" tab -->
      <v-card flat>
        <v-card-title>Neighbors with State ID</v-card-title>
        <v-card-text>
          <v-data-table
            :headers="headers"
            :items="neighborsWithStateID"
            :items-per-page="10"
          ></v-data-table>
          <p>Total: {{ totalWithStateID }}</p>
        </v-card-text>
      </v-card>
    </v-tab-item>


    <v-tab-item>
      <!-- Content for "Has Pet" tab -->
      <v-card flat>
        <v-card-title>Neighbors with Pets</v-card-title>
        <v-card-text>
          <v-data-table
            :headers="headers"
            :items="neighborsWithPet"
            :items-per-page="10"
          ></v-data-table>
          <p>Total: {{ totalWithPet }}</p>
        </v-card-text>
      </v-card>
    </v-tab-item>

<v-tab-item>
  <!-- Content for "Has Children" tab -->
  <v-card flat>
    <v-card-text>
      <!-- Add your content for "Has Children" here -->
    </v-card-text>
  </v-card>
</v-tab-item>

<v-tab-item>
  <!-- Content for "Has Medication" tab -->
  <v-card flat>
    <v-card-text>
      <!-- Add your content for "Has Medication" here -->
    </v-card-text>
  </v-card>
</v-tab-item>

<v-tab-item>
  <!-- Content for "Has Food Insecurity" tab -->
  <v-card flat>
    <v-card-text>
      <!-- Add your content for "Has Food Insecurity" here -->
    </v-card-text>
  </v-card>
</v-tab-item>

<v-tab-item>
  <!-- Content for "Has Transportation" tab -->
  <v-card flat>
    <v-card-text>
      <!-- Add your content for "Has Transportation" here -->
    </v-card-text>
  </v-card>
</v-tab-item>

<v-tab-item>
  <!-- Content for "Has Job" tab -->
  <v-card flat>
    <v-card-text>
      <!-- Add your content for "Has Job" here -->
    </v-card-text>
  </v-card>
</v-tab-item>

<v-tab-item>
  <!-- Content for "Has Housing" tab -->
  <v-card flat>
    <v-card-text>
      <!-- Add your content for "Has Housing" here -->
    </v-card-text>
  </v-card>
</v-tab-item>

<v-tab-item>
  <!-- Content for "Has Income" tab -->
  <v-card flat>
    <v-card-text>
      <!-- Add your content for "Has Income" here -->
    </v-card-text>
  </v-card>
</v-tab-item>
</v-card>
</template>


<script>
import axios from 'axios';

export default {
  data() {
    return {
      neighbors: [],
      headers: [
        { text: 'ID', value: 'NeighborID' },
        { text: 'First Name', value: 'FirstName' },
        { text: 'Last Name', value: 'LastName' },
      ],
    };
  },
  computed: {
    neighborsWithStateID() {
      return this.neighbors.filter(neighbor => neighbor.HasStateID);
    },
    totalWithStateID() {
      return this.neighborsWithStateID.length;
    },
    neighborsWithPet() {
      return this.neighbors.filter(neighbor => neighbor.HasPet);
    },
    totalWithPet() {
      return this.neighborsWithPet.length;
    },
    // Repeat the pattern for the remaining attributes
    // ...
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
  },
  created() {
    this.fetchData();
  },
};
</script>
