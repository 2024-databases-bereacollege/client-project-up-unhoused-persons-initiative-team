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
        text: this.getDisplayName(item),
        value: item.NeighborID || item.ServiceID || item.VolunteerID,
      }));
    },
  },
  data() {
    return {
      selectedItem: this.modelValue,
    };
  },
  methods: {
    getDisplayName(item) {
      if (item.FirstName && item.LastName) {
        return `${item.FirstName} ${item.LastName}`;
      } else if (item.FirstName) {
        return item.FirstName;
      } else if (item.ServiceType) {
        return item.ServiceType;
      } else {
        return '';
      }
    },
  },
};
</script>
