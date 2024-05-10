<template>
  <div>
    <h2>Add visit information</h2>
    <div v-for="(items, category) in apiData" :key="category">
      <ComboboxSelect
        :items="Object.values(items)"
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
  },
  methods: {
    async fetchData() {
      try {
        const response = await axios.get('http://127.0.0.1:5000/api/Add_Visit');
        this.apiData = response.data;
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    },
    async submitData() {
      try {
        const requestData = {
          selectedValues: this.selectedValues,
          visitDescription: this.visitDescription,
        };
        const response = await axios.post('http://127.0.0.1:5000/api/IndividualVisitLog', requestData);
        console.log('Data submitted successfully:', response.data);
        // Handle success response
      } catch (error) {
        console.error('Error submitting data:', error);
        // Handle error
      }
    },
  },
};
</script>
