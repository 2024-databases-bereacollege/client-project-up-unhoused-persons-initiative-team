<template>
  <div class="neighbor-profile">
    <h1>Neighbor Profile</h1>
    <template v-if="neighbor">
      <h2>{{ neighbor.FullName }}</h2>
      <table>
        <tr>
  <th><font-awesome-icon :icon="['fas', 'birthday-cake']" /> Date of Birth</th>
  <td v-if="neighbor.DateOfBirth">{{ formatDate(neighbor.DateOfBirth) }}</td>
  <td v-else>N/A</td>
</tr>
        <tr>
          <th><font-awesome-icon :icon="['fas', 'phone']" /> Phone</th>
          <td>{{ neighbor.Phone }}</td>
        </tr>
        <tr>
          <th><font-awesome-icon :icon="['fas', 'map-marker-alt']" /> Location</th>
          <td>{{ neighbor.Location }}</td>
        </tr>
        <tr>
          <th><font-awesome-icon :icon="['fas', 'envelope']" /> Email</th>
          <td>{{ neighbor.Email }}</td>
        </tr>
        <tr>
          <th><font-awesome-icon :icon="['fas', 'calendar-plus']" /> Created Date</th>
          <td>{{ formatDate(neighbor.Created_date) }}</td>
        </tr>
        <tr>
          <th><font-awesome-icon :icon="['fas', 'id-card']" /> Has State ID</th>
          <td>{{ neighbor.HasStateID ? 'Yes' : 'No' }}</td>
        </tr>
        <tr>
          <th><font-awesome-icon :icon="['fas', 'paw']" /> Has Pet</th>
          <td>{{ neighbor.HasPet ? 'Yes' : 'No' }}</td>
        </tr>
        <tr>
          <th><font-awesome-icon :icon="['fas', 'child']" /> Has Children</th>
          <td>{{ neighbor.HasChildren ? 'Yes' : 'No' }}</td>
        </tr>
        <tr>
          <th><font-awesome-icon :icon="['fas', 'prescription']" /> Has Medication</th>
          <td>{{ neighbor.HasMedication ? 'Yes' : 'No' }}</td>
        </tr>
        <tr>
          <th><font-awesome-icon :icon="['fas', 'utensils']" /> Has Food Insecurity</th>
          <td>{{ neighbor.HasFoodInsecurity ? 'Yes' : 'No' }}</td>
        </tr>
        <tr>
          <th><font-awesome-icon :icon="['fas', 'bus']" /> Has Transportation</th>
          <td>{{ neighbor.HasTransportation ? 'Yes' : 'No' }}</td>
        </tr>
        <tr>
          <th><font-awesome-icon :icon="['fas', 'briefcase']" /> Has Job</th>
          <td>{{ neighbor.HasJob ? 'Yes' : 'No' }}</td>
        </tr>
        <tr>
          <th><font-awesome-icon :icon="['fas', 'home']" /> Has Housing</th>
          <td>{{ neighbor.HasHousing ? 'Yes' : 'No' }}</td>
        </tr>
        <tr>
          <th><font-awesome-icon :icon="['fas', 'heartbeat']" /> Has Insurance</th>
          <td>{{ neighbor.HasInsurance ? 'Yes' : 'No' }}</td>
        </tr>
        <tr>
          <th><font-awesome-icon :icon="['fas', 'dollar-sign']" /> Has Income</th>
          <td>{{ neighbor.HasIncome ? 'Yes' : 'No' }}</td>
        </tr>
        <tr>
          <th><font-awesome-icon :icon="['fas', 'sticky-note']" /> Notes</th>
          <td>{{ neighbor.Notes }}</td>
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
import {
  faBirthdayCake,
  faPhone,
  faMapMarkerAlt,
  faEnvelope,
  faCalendarPlus,
  faIdCard,
  faPaw,
  faChild,
  faPrescription,
  faUtensils,
  faBus,
  faBriefcase,
  faHome,
  faHeartbeat,
  faDollarSign,
  faStickyNote,
} from '@fortawesome/free-solid-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';

library.add(
  faBirthdayCake,
  faPhone,
  faMapMarkerAlt,
  faEnvelope,
  faCalendarPlus,
  faIdCard,
  faPaw,
  faChild,
  faPrescription,
  faUtensils,
  faBus,
  faBriefcase,
  faHome,
  faHeartbeat,
  faDollarSign,
  faStickyNote
);

export default {
  components: {
    FontAwesomeIcon,
  },
  props: ['ID'],
  data() {
    return {
      neighbor: null,
      visitLogData: [], // Initialize with an empty array
    };
  },
  computed: {
    neighborID() {
      return this.$route.params.ID;
    }
  },
  mounted() {
    this.fetchNeighborDetails();
  },
  methods: {
    formatDate(dateString) {
      const options = { year: 'numeric', month: 'long', day: 'numeric' };
      return new Date(dateString).toLocaleDateString(undefined, options);
    },
    fetchNeighborDetails() {
      const neighborID = this.neighborID;
      axios
        .get(`http://127.0.0.1:5000/api/neighbors/${neighborID}`)
        .then((response) => {
          this.neighbor = response.data;
        })
        .catch((error) => {
          console.error('Error fetching neighbor:', error);
        });

      axios
        .get(`http://127.0.0.1:5000/api/IndividualVisitLog?neighborID=${neighborID}`)
        .then((response) => {
          this.visitLogData = response.data;
        })
        .catch((error) => {
          console.error('Error fetching visit log data:', error);
        });
    },
  },
};
</script>
<style scoped>
.neighbor-profile {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  background-color: #f8f8f8;
  border-radius: 5px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

h1 {
  font-size: 24px;
  font-weight: bold;
  margin-bottom: 20px;
  color: #333;
}

h2 {
  font-size: 20px;
  font-weight: bold;
  margin-bottom: 10px;
  color: #555;
}

table {
  width: 100%;
  border-collapse: collapse;
  margin-bottom: 20px;
}

th {
  font-weight: bold;
  text-align: left;
  padding: 10px;
  background-color: #f0f0f0;
  color: #333;
}

td {
  padding: 10px;
  background-color: #fff;
  color: #555;
}

.visit-log {
  margin-top: 20px;
}

.visit-log table {
  width: 100%;
  border-collapse: collapse;
}

.visit-log th,
.visit-log td {
  padding: 8px;
  border-bottom: 1px solid #ddd;
}

.visit-log th {
  background-color: #f0f0f0;
  color: #333;
}

.visit-log td {
  background-color: #fff;
  color: #555;
}
</style>
