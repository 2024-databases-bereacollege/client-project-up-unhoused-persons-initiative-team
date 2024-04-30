<template>
    <v-data-table
      :headers="headers"
      :items="desserts"
      :sort-by="[{ key: items, order: 'asc' }]"
    >
      <template v-slot:top>
        <v-toolbar
          flat
        >
          <v-toolbar-title>Services</v-toolbar-title>
          <v-divider
            class="mx-4"
            inset
            vertical
          ></v-divider>
          <v-spacer></v-spacer>
          <v-dialog v-model="dialog" max-width="500px">
    <template v-slot:activator="{ on, attrs }">
      <v-btn class="mb-2" color="primary" dark v-bind="attrs" v-on="on">
        New Item
      </v-btn>
    </template>
    <v-card>
      <v-card-title>
        <span class="text-h5">{{ formTitle }}</span>
      </v-card-title>

      <v-card-text>
        <v-container>
          <v-row>
            <v-col cols="12" md="4" sm="6" v-for="(value, key) in editedItem" :key="key">
              <v-text-field
                v-model="editedItem[key]"
                :label="capitalizeFirstLetter(key)"
              ></v-text-field>
            </v-col>
          </v-row>
        </v-container>
      </v-card-text>

      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn color="blue darken-1" text @click="close">Cancel</v-btn>
        <v-btn color="blue darken-1" text @click="save">Save</v-btn>
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
  //import axios from 'axios';

  export default {
    
    data: () => ({
      dialog: false,
      dialogDelete: false,
      headers: [], // Now it will be dynamically set
      desserts: [],
      editedIndex: -1,
      editedItem: {},
      defaultItem: {},
    }),
  
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
        // Assume you're fetching data dynamically. Adjust accordingly.
        // Example static data for demonstration
        const fetchedData = [
          {
            name: 'Frozen Yogurt',
            calories: 159,
            fat: 6.0,
            carbs: 24,
            protein: 4.0,
          },
          {
            name: 'Ice cream sandwich',
            calories: 237,
            fat: 9.0,
            carbs: 37,
            protein: 4.3,
          },
        ];
        this.desserts = fetchedData;
        if (fetchedData.length > 0) {
          // Dynamically create headers based on keys of the first item
          this.headers = Object.keys(fetchedData[0]).map(key => ({
            text: this.capitalizeFirstLetter(key),
            value: key,
          }));
          // For actions, if needed
          this.headers.push({ text: 'Actions', value: 'actions', sortable: false });
        }
      },
  
      capitalizeFirstLetter(string) {
        return string.charAt(0).toUpperCase() + string.slice(1);
      },
  
      editItem(item) {
        this.editedIndex = this.desserts.indexOf(item);
        this.editedItem = Object.assign({}, item); // Now works dynamically
        this.dialog = true;
      },
  
      deleteItem(item) {
        this.editedIndex = this.desserts.indexOf(item);
        this.dialogDelete = true;
      },
  
      deleteItemConfirm() {
        this.desserts.splice(this.editedIndex, 1);
        this.closeDelete();
      },
  
      close() {
        this.dialog = false;
        this.$nextTick(() => {
          this.editedItem = Object.assign({}, this.defaultItem); // Resets to dynamic default
          this.editedIndex = -1;
        });
      },
  
      closeDelete() {
        this.dialogDelete = false;
      },
  
      save() {
        if (this.editedIndex > -1) {
          Object.assign(this.desserts[this.editedIndex], this.editedItem);
        } else {
          this.desserts.push(this.editedItem);
        }
        this.close();
      },
    },
  };
  </script>
  