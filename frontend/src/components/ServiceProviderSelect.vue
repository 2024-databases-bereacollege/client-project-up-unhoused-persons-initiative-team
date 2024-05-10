
<template>
  <v-combobox
    v-model="selectedItem"
    :items="formattedItems"
    :label="label"
    item-title="text"
    item-value="value"
    @update:model-value="$emit('update:model-value', $event)"
    :multiple="multiple"
    variant="outlined"
  ></v-combobox>
</template>
<script>
export default {
  props: {
    items: {
      type: Array,
      required: true,
    },
    label: {
      type: String,
      default: 'Select',
    },
    modelValue: {
      type: [String, Number, Object, Array],
      default: null,
    },
    multiple: {
      type: Boolean,
      default: false,
    },
  },
  emits: ['update:model-value'],
  computed: {
    formattedItems() {
      return this.items.map((item) => ({
        text: item.Organization_Name,
        value: item.OrganizationID,
      }));
    },
  },
  data() {
    return {
      selectedItem: this.modelValue,
    };
  },
};
</script>


<!-- <template>
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
  </script> -->
