<template>
    <div class="visit-log">
      <table>
        <thead>
          <tr>
            <th>Description</th>
            <th>Service Name</th>
            <th>Visit Date</th>
            <th>Volunteer Name</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(visit, index) in visits" :key="index">
            <td>{{ visit.Description }}</td>
            <td>{{ visit.ServiceName }}</td>
            <td>{{ formatDate(visit.VisitDate) }}</td>
            <td>{{ visit.VolunteerName }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </template>
  
  <script>
  export default {
    name: 'VisitLog',
    props: {
      visits: {
        type: Array,
        required: true
      }
    },
    methods: {
      formatDate(dateString) {
        const date = new Date(dateString);
        return date.toLocaleDateString();
      }
    }
  };
  </script>
  
  <style scoped>
  table {
    width: 100%;
    border-collapse: collapse;
  }
  
  th,
  td {
    padding: 8px;
    text-align: left;
    border-bottom: 1px solid #ddd;
  }
  
  th {
    background-color: #f2f2f2;
  }
  </style>
