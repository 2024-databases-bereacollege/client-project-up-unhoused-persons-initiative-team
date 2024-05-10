<template>
  <div>
    <h2>Add Visit Log</h2>
    <div v-for="(items, category) in apiData" :key="category">
      <ComboboxSelect
        :items="items"
        :label="`Select ${category}`"
        @update:model-value="selectedValues[category] = $event"
      />
    </div>
    <v-textarea
      v-model="visitDescription"
      label="Description of Visit"
      variant="solo-filled"
      rows="3"
      auto-grow
    ></v-textarea>
    <button @click="submitData">Submit</button>
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
      apiData: {},
      selectedValues: {},
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

        this.apiData = {
          Neighbors: neighborsResponse.data,
          Services: servicesResponse.data,
          Volunteers: volunteersResponse.data,
        };
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    },
    async submitData() {
      try {
        const requestData = {
          ...this.selectedValues,
          Description: this.visitDescription,
        };

        const response = await axios.post('http://127.0.0.1:5000/api/visit_logs', requestData);

        console.log('Visit log submitted successfully:', response.data);
        // Handle success response
      } catch (error) {
        console.error('Error submitting visit log:', error);
        // Handle error
      }
    },
  },
};
</script>
