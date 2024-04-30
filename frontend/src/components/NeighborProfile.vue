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
      <IndividualVisitLog :visits="visitLogData" />
    </template>
    <template v-else>
      <p>Loading neighbor details...</p>
    </template>
  </div>
</template>

<script>
import axios from 'axios';
import IndividualVisitLog from './IndividualVisitLog.vue';
import '@fortawesome/fontawesome-svg-core/styles.css';
import { library } from '@fortawesome/fontawesome-svg-core';
import { faBirthdayCake, faPhone, faMapMarkerAlt, faEnvelope, faCalendarPlus, faIdCard, faPaw } from '@fortawesome/free-solid-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';

library.add(faBirthdayCake, faPhone, faMapMarkerAlt, faEnvelope, faCalendarPlus, faIdCard, faPaw);

export default {
  components: {
    IndividualVisitLog,
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
  },
  methods: {
    formatDate(dateString) {
      const options = { year: 'numeric', month: 'long', day: 'numeric' };
      return new Date(dateString).toLocaleDateString(undefined, options);
    },
  },
};
</script>



<!-- <template>
  <div class="neighbor-profile">
    <h1>Neighbor Profile</h1>
    <template v-if="neighbor">
    <h2>{{ neighbor.FirstName }} {{ neighbor.LastName }}</h2>
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
  </template>
    <template v-else>
      <p>Loading neighbor details...</p>
    </template>
  </div>
</template>


<script>
import axios from 'axios';

//import IndividualVisitLog from './IndividualVisitLog.vue';
import '@fortawesome/fontawesome-svg-core/styles.css';
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
      //neighbor: null,
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
</script> -->


<style scoped>
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
