<template>
    <v-select
      v-model="selectedProvider"
      :items="serviceProviders"
      item-text="Organization_Name"
      item-value="OrganizationID"
      label="Service Provider"
      @change="emitSelectedProvider"
    ></v-select>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        selectedProvider: null,
        serviceProviders: [],
      };
    },
    mounted() {
      this.fetchServiceProviders();
    },
    methods: {
      fetchServiceProviders() {
        axios.get('http://127.0.0.1:5000/api/service_providers')
          .then(response => {
            this.serviceProviders = response.data;
          })
          .catch(error => {
            console.error('Error fetching service providers:', error);
          });
      },
      emitSelectedProvider() {
        this.$emit('provider-selected', this.selectedProvider);
      },
    },
  };
  </script>
