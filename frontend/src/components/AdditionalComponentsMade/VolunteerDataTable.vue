<!--This is used as a child component of VolunteerTable.vue in views-->

<template>
  <v-data-table
    :headers="headers"
    :items="items"
    :sort-by="[{ key: sortBy, order: sortOrder }]"
  >
    <template v-slot:top>
      <v-toolbar flat>
        <v-toolbar-title>{{ tableTitle }}</v-toolbar-title>
        <v-divider class="mx-4" inset vertical></v-divider>
        <v-spacer></v-spacer>
        <v-dialog v-model="dialog" max-width="500px">
          <template v-slot:activator="{ props }">
            <v-btn class="mb-2" color="primary" dark v-bind="props">
              New Entry
            </v-btn>
          </template>
          <v-card>
            <v-card-title>
              <span class="text-h5">{{ formTitle }}</span>
            </v-card-title>
            <v-card-text>
      <v-container>
        <v-row>
          <v-col cols="12" sm="6">
            <v-text-field
              :value="editedItem.FirstName"
              @input="$emit('update:editedItem', { ...editedItem, FirstName: $event.target.value })"
              label="First Name"
              required
            ></v-text-field>
          </v-col>
          <v-col cols="12" sm="6">
            <v-text-field
              :value="editedItem.LastName"
              @input="$emit('update:editedItem', { ...editedItem, LastName: $event.target.value })"
              label="Last Name"
              required
            ></v-text-field>
          </v-col>
          <v-col cols="12">
            <v-text-field
              :value="editedItem.Password"
              @input="$emit('update:editedItem', { ...editedItem, Password: $event.target.value })"
              label="Password"
              type="password"
              required
            ></v-text-field>
          </v-col>
          <v-col cols="12">
            <v-text-field
              :value="editedItem.Email"
              @input="$emit('update:editedItem', { ...editedItem, Email: $event.target.value })"
              label="Email"
              required
            ></v-text-field>
          </v-col>
          <v-col cols="12">
            <v-text-field
              :value="editedItem.Phone"
              @input="$emit('update:editedItem', { ...editedItem, Phone: $event.target.value })"
              label="Phone"
              required
            ></v-text-field>
          </v-col>
          <v-col cols="12">
            <v-checkbox
  v-model="hasRecordAccess"
  label="Has Record Access"
></v-checkbox>

          </v-col>
        </v-row>
      </v-container>
      </v-card-text>
  
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn
                  color="blue-darken-1"
                  variant="text"
                  @click="close"
                >
                  Cancel
                </v-btn>
                <v-btn
                  color="blue-darken-1"
                  variant="text"
                  @click="save"
                >
                  Save
                </v-btn>
              </v-card-actions>
            </v-card>
          </v-dialog>
          <v-dialog v-model="dialogDelete" max-width="500px">
            <v-card>
              <v-card-title class="text-h5">Are you sure you want to delete this item?</v-card-title>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="blue-darken-1" variant="text" @click="closeDelete">Cancel</v-btn>
                <v-btn color="blue-darken-1" variant="text" @click="deleteItemConfirm">OK</v-btn>
                <v-spacer></v-spacer>
              </v-card-actions>
            </v-card>
          </v-dialog>
        </v-toolbar>
      </template>
<!-- eslint-disable-next-line vue/valid-v-slot -->
<template v-slot:item.actions="{ item }">
        <v-icon
          class="me-2"
          size="small"
          @click="editItem(item)"
        >
          mdi-pencil
        </v-icon>
        <v-icon
          size="small"
          @click="deleteItem(item)"
        >
          mdi-delete
        </v-icon>
      </template>
      <template v-slot:no-data>
        <v-btn
          color="primary"
          @click="initialize"
        >
          Reset
        </v-btn>
      </template>
    </v-data-table>
  </template>

<script>
export default {
  props: {
    tableTitle: {
      type: String,
      default: 'Template table'
    },
    headers: {
      type: Array,
      required: true,
    },
    items: {
      type: Array,
      required: true,
    },
    onEdit: {
      type: Function,
      required: true,
    },
    editedItem: {
      type: Object,
      required: true,
    },
    defaultItem: {
      type: Object,
      required: true,
    },
    onSave: {
      type: Function,
      required: true,
    },
    onDelete: {
      type: Function,
      required: true,
    },
    onClose: {
      type: Function,
      required: true,
    },
    onCloseDelete: {
      type: Function,
      required: true,
    },
    sortBy: {
      type: String,
      default: '',
    },
    sortOrder: {
      type: String,
      default: 'asc',
    },
  },
  data() {
    return {
      dialog: false,
      hasRecordAccess: false,

      // ...
      // editedItem: {
      //   FirstName: '',
      //   LastName: '',
      //   Password: '',
      //   Email: '',
      //   Phone: '',
      //   HasRecordAccess: false,
      // },
      // defaultItem: {
      //   FirstName: '',
      //   LastName: '',
      //   Password: '',
      //   Email: '',
      //   Phone: '',
      //   HasRecordAccess: false,
      // },
    };
  },
  computed: {
    formTitle() {
      return this.editedIndex === -1 ? 'New Item' : 'Edit Item';
    },
  },
  watch: {
    dialog(val) {
      val || this.close();
    },
    dialogDelete(val) {
      val || this.closeDelete();
    },
  },
  created() {
    this.initialize();
  },
  methods: {
    initialize() {
// does this need items? 
    },
    editItem(item) {
    console.log('Edit button clicked for item:', item);
    this.editedIndex = this.items.indexOf(item);
    this.onEdit(item);
    this.dialog = true;
  },

    deleteItem(item) {
    console.log('Delete button clicked for item:', item);
    this.editedIndex = this.items.indexOf(item);
    this.onDelete(item);
    this.dialogDelete = true; 
    },
    deleteItemConfirm() {
    this.$emit('delete-item-confirm', this.editedIndex);
    this.closeDelete();
    },
    close() {
    this.dialog = false;
    this.$nextTick(() => {
      this.editedIndex = -1;
      this.$emit('close');
    });
    },
    closeDelete() {
      this.dialogDelete = false;
      this.$nextTick(() => {
        this.editedIndex = -1;
        this.$emit('close-delete');
      });
    },
    save() {
    const updatedItem = {
      ...this.editedItem,
      HasRecordAccess: this.hasRecordAccess,
    };
    this.$emit('save', updatedItem);
    this.close();
  },
    watch: {
  editedItem(newValue) {
    console.log('editedItem changed:', newValue);
    },
  },

  },
};
</script>

<!-- <script>
export default {
  props: {
    headers: {
      type: Array,
      required: true,
    },
    items: {
      type: Array,
      required: true,
    },
    editedItem: {
      type: Object,
      required: true,
    },
    defaultItem: {
      type: Object,
      required: true,
    },
    onSave: {
      type: Function,
      required: true,
    },
    onDelete: {
      type: Function,
      required: true,
    },
    onClose: {
      type: Function,
      required: true,
    },
    onCloseDelete: {
      type: Function,
      required: true,
    },
    sortBy: {
      type: String,
      default: '',
    },
    sortOrder: {
      type: String,
      default: 'asc',
    },
  
      computed: {
        formTitle () {
          return this.editedIndex === -1 ? 'New Item' : 'Edit Item'
        },
      },
  
      watch: {
        dialog (val) {
          val || this.close()
        },
        dialogDelete (val) {
          val || this.closeDelete()
        },
      },
  
      created () {
        this.initialize()
      },
  
      methods: {
        initialize () {
          this.desserts = [
            {
              name: 'Frozen Yogurt',
              calories: 159,
              fat: 6.0,
              carbs: 24,
              protein: 4.0,
            }
          ]
        },
  
        editItem(item) {
    this.$emit('edit-item', item);
  },
  deleteItem(item) {
    this.$emit('delete-item', item);
  },
  deleteItemConfirm() {
    this.$emit('delete-item-confirm');
  },
  close() {
    this.$emit('close');
  },
  closeDelete() {
    this.$emit('close-delete');
  },
  save() {
    this.$emit('save', this.editedItem);
  },
      },
    },
  }

      // deleteItem(item) {
    //   console.log('Delete button clicked for item:', item);
    //   this.editedIndex = this.items.indexOf(item);
    //   this.$emit('delete-item', { item, index: this.editedIndex });
    // },
  </script> -->
