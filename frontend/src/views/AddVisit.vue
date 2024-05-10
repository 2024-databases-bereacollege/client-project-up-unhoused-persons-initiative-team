<template>
  <div>
    <h2>Add Visit Log</h2>
    <div>
      <ComboboxSelect
        :items="neighbors"
        label="Select Neighbor"
        @update:model-value="selectedValues.Neighbors = $event"
      />
      <ComboboxSelect
        :items="services"
        label="Select Service"
        @update:model-value="selectedValues.ServiceID = $event"
      />
      <ComboboxSelect
        :items="volunteers"
        label="Select Volunteer"
        @update:model-value="selectedValues.Volunteers = $event"
      />
      <v-text-field
        v-model="selectedValues.Date"
        label="Visit Date"
        type="date"
      ></v-text-field>
      <v-textarea
        v-model="visitDescription"
        label="Description of Visit"
        variant="solo-filled"
        rows="3"
        auto-grow
      ></v-textarea>
      <button @click="submitData">Submit</button>
    </div>
  </div>
</template>

<script>
import ComboboxSelect from '@/components/ComboboxSelect.vue';
import axios from 'axios';

export default {
  components: {
    ComboboxSelect,
  },
  data() {
    return {
      neighbors: [],
      services: [],
      volunteers: [],
      selectedValues: {
        Neighbors: null,
        ServiceID: null,
        Volunteers: null,
        Date: '',
      },
      visitDescription: '',
    };
  },
  mounted() {
    this.fetchData();
    window.addEventListener('refreshData', this.fetchData);
  },
  beforeUnmount() {
    window.removeEventListener('refreshData', this.fetchData);
  },
  methods: {
    async fetchData() {
      try {
        const [neighborsResponse, servicesResponse, volunteersResponse] = await Promise.all([
          axios.get('http://127.0.0.1:5000/api/neighbors'),
          axios.get('http://127.0.0.1:5000/api/services'),
          axios.get('http://127.0.0.1:5000/api/volunteers'),
        ]);

        this.neighbors = neighborsResponse.data;
        this.services = servicesResponse.data;
        this.volunteers = volunteersResponse.data;
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    },
    async submitData() {
  try {
    const requestData = {
      NeighborID: this.selectedValues.Neighbors ? this.selectedValues.Neighbors.value : null,
      ServiceID: this.selectedValues.ServiceID ? this.selectedValues.ServiceID.value : null,
      VolunteerID: this.selectedValues.Volunteers ? this.selectedValues.Volunteers.value : null,
      Description: this.visitDescription,
      Date: this.selectedValues.Date,
    };

    console.log('Request Data:', requestData);

    const response = await axios.post('http://127.0.0.1:5000/api/visit_logs', requestData);

    console.log('Visit log submitted successfully:', response.data);
    // Handle success response

    // Emit a custom event
    this.$emit('reloadApp');
  } catch (error) {
    console.error('Error submitting visit log:', error);
    // Handle error
  }
},
  },
};
</script>
