<template>
  <v-combobox
    v-model="selectedItem"
    :items="formattedItems"
    :label="label"
    item-title="text"
    item-value="value"
    @update:modelValue="$emit('update:model-value', $event)"
    chips
    multiple
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
  },
  emits: ['update:model-value'],
  computed: {
    formattedItems() {
      return this.items.map(item => ({
        text: item.FullName || item.ServiceType || item.NameOfItem,
        value: item.NeighborID || item.VolunteerID || item.ServiceID || item.InventoryID,
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
