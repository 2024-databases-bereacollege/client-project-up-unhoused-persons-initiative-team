
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
