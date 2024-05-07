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
        <tr>
          <th><font-awesome-icon icon="faChild" /> Has Children</th>
          <td>{{ neighbor.HasChildren ? 'Yes' : 'No' }}</td>
        </tr>
        <tr>
          <th><font-awesome-icon icon="faPrescription" /> Has Medication</th>
          <td>{{ neighbor.HasMedication ? 'Yes' : 'No' }}</td>
        </tr>
        <tr>
          <th><font-awesome-icon icon="faUtensils" /> Has Food Insecurity</th>
          <td>{{ neighbor.HasFoodInsecurity ? 'Yes' : 'No' }}</td>
        </tr>
        <tr>
          <th><font-awesome-icon icon="faBus" /> Has Transportation</th>
          <td>{{ neighbor.HasTransportation ? 'Yes' : 'No' }}</td>
        </tr>
        <tr>
          <th><font-awesome-icon icon="faBriefcase" /> Has Job</th>
          <td>{{ neighbor.HasJob ? 'Yes' : 'No' }}</td>
        </tr>
        <tr>
          <th><font-awesome-icon icon="faHome" /> Has Housing</th>
          <td>{{ neighbor.HasHousing ? 'Yes' : 'No' }}</td>
        </tr>
        <tr>
          <th><font-awesome-icon icon="faHeartbeat" /> Has Insurance</th>
          <td>{{ neighbor.HasInsurance ? 'Yes' : 'No' }}</td>
        </tr>
        <tr>
          <th><font-awesome-icon icon="faDollarSign" /> Has Income</th>
          <td>{{ neighbor.HasIncome ? 'Yes' : 'No' }}</td>
        </tr>
        <tr>
          <th><font-awesome-icon icon="faStickyNote" /> Notes</th>
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

<!-- <template>
  <div class="neighbor-profile">
    <h1>Neighbor Profile</h1>
    <h2>{{ neighbor.FullName }}</h2>
    <table>
      <tr>
        <th><font-awesome-icon icon="faBirthdayCake" /> Date of Birth</th>
        <td>{{ neighbor.DateOfBirth }}</td>
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
        <td>{{ neighbor.Created_date }}</td>
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
    <h3>Visit Records</h3>
    <IndividualVisitLog :visits="visitRecords" />
  </div>
</template>

<script>
import axios from 'axios';

//import IndividualVisitLog from './IndividualVisitLog.vue';
import { library } from '@fortawesome/fontawesome-svg-core';
import { faBirthdayCake, faPhone, faMapMarkerAlt, faEnvelope, faCalendarPlus, faIdCard, faPaw } from '@fortawesome/free-solid-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';

library.add(faBirthdayCake, faPhone, faMapMarkerAlt, faEnvelope, faCalendarPlus, faIdCard, faPaw);

export default {
  components: {
    // IndividualVisitLog,
    FontAwesomeIcon,
  },
  props: ['ID'],
  data() {
    return {
      neighbor: {
        NeighborID: null,
        VolunteerID: null,
        OrganizationID: null,
        FirstName: '',
        LastName: '',
        DateOfBirth: null,
        Phone: '',
        Location: '',
        Email: '',
        Created_date: null,
        HasStateID: false,
        HasPet: false,
      },
      visitRecords: [],
    };
  },
  mounted() {
    const neighborID = this.$route.params.ID;
    axios.get(`http://127.0.0.1:5000/api/neighbors/${neighborID}`)
      .then(response => {
        this.neighbor = response.data;
      })
      .catch(error => {
        console.error(error);
      });
  },
};
</script>
-- 
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
</style> -- -->




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
