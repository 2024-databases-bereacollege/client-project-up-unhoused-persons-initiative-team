<template>
  <div>
    <v-card>
      <v-data-table
        :headers="VDataTableHeaders"
        :items="services"
        :loading="loading"
        class="elevation-1"
      >
        <!-- eslint-disable-next-line vue/valid-v-slot -->
        <template v-slot:item.DateOfStart="{ item }">
          {{ formatDate(item.DateOfStart) }}
        </template>
      </v-data-table>
    </v-card>
  </div>
</template>

<script>

export default {

  data() {
    return {
      headers: [
        { text: 'Service Type', value: 'ServiceType' },
        { text: 'Organization Name', value: 'Organization_Name' },
        { text: 'Contact Person', value: 'ContactPerson' },
        { text: 'Email', value: 'Email' },
        { text: 'Phone', value: 'Phone' },
        { text: 'Date of Start', value: 'DateOfStart' },
        { text: 'Total Neighbors', value: 'TotalNeighbors' },
      ],
      services: [],
      loading: true,
    };
  },
  mounted() {
    this.fetchServices();
  },
  methods: {
    fetchServices() {
      fetch('http://127.0.0.1:5000/api/ServicesAndProviders')
        .then(response => response.json())
        .then(data => {
          this.services = data;
          this.loading = false;
        })
        .catch(error => {
          console.error('Error fetching services:', error);
          this.loading = false;
        });
    },
    formatDate(date) {
      return new Date(date).toLocaleDateString();
    },
  },
};
</script>
