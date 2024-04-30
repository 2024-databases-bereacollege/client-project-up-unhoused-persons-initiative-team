<template>
    <div class="neighbor-profile">
      <h1>Neighbor Profile</h1>
      <template v-if="neighbor">
        <h2>{{ neighbor.FullName }}</h2>
        <table>
          <tr>
            <th><font-awesome-icon icon="faBirthdayCake" /> Date of Birth</th>
            <td>{{ formatDate(neighbor.DateOfBirth) }}</td>
          </tr>
          <tr>
            <th><font-awesome-icon icon="faPhone" /> Phone</th>
            <td>{{ neighbor.Phone }}</td>
          </tr>
          <tr>
            <th><font-awesome-icon icon="faMapMarkerAlt" /> Location</th>
            <td>{{ neighbor.Location }}</td>
          </tr>
          <tr>
            <th><font-awesome-icon icon="faEnvelope" /> Email</th>
            <td>{{ neighbor.Email }}</td>
          </tr>
          <tr>
            <th><font-awesome-icon icon="faCalendarPlus" /> Created Date</th>
            <td>{{ formatDate(neighbor.Created_date) }}</td>
          </tr>
          <tr>
            <th><font-awesome-icon icon="faIdCard" /> Has State ID</th>
            <td>{{ neighbor.HasStateID ? 'Yes' : 'No' }}</td>
          </tr>
          <tr>
            <th><font-awesome-icon icon="faPaw" /> Has Pet</th>
            <td>{{ neighbor.HasPet ? 'Yes' : 'No' }}</td>
          </tr>
        </table>
  
        <h3>Visit Log</h3>
        <div class="visit-log">
          <table>
            <thead>
              <tr>
                <th>Visit Date</th>
                <th>Service Name</th>
                <th>Volunteer Name</th>
                <th>Description</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(visit, index) in visitLogData" :key="index">
                <td>{{ formatDate(visit.VisitDate) }}</td>
                <td>{{ visit.ServiceName }}</td>
                <td>{{ visit.VolunteerName }}</td>
                <td>{{ visit.Description }}</td>
              </tr>
            </tbody>
          </table>
        </div>
      </template>
      <template v-else>
        <p>Loading neighbor details...</p>
      </template>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  import '@fortawesome/fontawesome-svg-core/styles.css';
  import { library } from '@fortawesome/fontawesome-svg-core';
  import { faBirthdayCake, faPhone, faMapMarkerAlt, faEnvelope, faCalendarPlus, faIdCard, faPaw } from '@fortawesome/free-solid-svg-icons';
  import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
  
  library.add(faBirthdayCake, faPhone, faMapMarkerAlt, faEnvelope, faCalendarPlus, faIdCard, faPaw);
  
  export default {
    components: {
      FontAwesomeIcon,
    },
    props: ['ID'],
    data() {
      return {
        neighbor: null,
        visitLogData: [] // Initialize with an empty array
      };
    },
    mounted() {
      const neighborID = this.ID;
      axios.get(`http://127.0.0.1:5000/api/neighbors/${neighborID}`)
        .then(response => {
          this.neighbor = response.data;
        })
        .catch(error => {
          console.error('Error fetching neighbor:', error);
        });
  
      axios.get(`http://127.0.0.1:5000/api/IndividualVisitLog?neighborID=${neighborID}`)
        .then(response => {
          this.visitLogData = response.data;
        })
        .catch(error => {
          console.error('Error fetching visit log data:', error);
        });
    },
    methods: {
      formatDate(dateString) {
        const options = { year: 'numeric', month: 'long', day: 'numeric' };
        return new Date(dateString).toLocaleDateString(undefined, options);
      },
    },
  };
  </script>
