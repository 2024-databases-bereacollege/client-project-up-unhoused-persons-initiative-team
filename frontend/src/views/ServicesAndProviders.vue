<template>
  <div>
    <v-card>
      <v-data-table
        :headers="headers"
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
      { title: 'Service Type', key: 'ServiceType' },
        { title: 'Service Description', key: 'ServiceDescription' },
        { title: 'Organization Name', key: 'Organization_Name' },
        { title: 'Contact Person', key: 'ContactPerson' },
        { title: 'Email', key: 'Email' },
        { title: 'Phone', key: 'Phone' },
        { title: 'Date of Start', key: 'DateOfStart' },
        { title: 'Total Neighbors', key: 'TotalNeighbors' },
        { title: 'Actions', key: 'actions', sortable: false}
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
