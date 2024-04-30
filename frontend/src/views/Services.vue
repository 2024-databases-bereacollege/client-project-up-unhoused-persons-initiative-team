<template>
  <v-data-table
    :headers="headers"
    :items="tableData"
    :sort-by="[{ key: 'calories', order: 'asc' }]"
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
import axios from 'axios';

export default {
  data() {
    return {
      dialog: false,
      dialogDelete: false,
      headers: [], // Will be dynamically set based on fetched data
      tableData: [], // Renamed from 'desserts' for clarity and consistency
      editedIndex: -1,
      editedItem: {},
      defaultItem: {},
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

  mounted() {
    this.fetchData();
  },

  methods: {
    fetchData() {
      axios.get('http://127.0.0.1:5000/api/services')
        .then(response => {
          this.tableData = response.data;
          // Dynamically create headers based on keys of the first item if data exists
          if (this.tableData.length > 0) {
            this.headers = Object.keys(this.tableData[0]).map(key => ({
              text: this.capitalizeFirstLetter(key),
              value: key,
            }));
            // For actions, if needed
            this.headers.push({ text: 'Actions', value: 'actions', sortable: false });
          }
        })
        .catch(error => console.error(error));
    },

    capitalizeFirstLetter(string) {
      return string.charAt(0).toUpperCase() + string.slice(1);
    },

    editItem(item) {
      this.editedIndex = this.tableData.indexOf(item);
      this.editedItem = Object.assign({}, item);
      this.dialog = true;
    },

    deleteItem(item) {
      this.editedIndex = this.tableData.indexOf(item);
      this.dialogDelete = true;
    },

    deleteItemConfirm() {
      this.tableData.splice(this.editedIndex, 1);
      this.closeDelete();
    },

    close() {
      this.dialog = false;
      this.$nextTick(() => {
        this.editedItem = Object.assign({}, this.defaultItem);
        this.editedIndex = -1;
      });
    },

    closeDelete() {
      this.dialogDelete = false;
    },

    save() {
      if (this.editedIndex > -1) {
        Object.assign(this.tableData[this.editedIndex], this.editedItem);
      } else {
        this.tableData.push(this.editedItem);
      }
      this.close();
    },
  },
};
</script>


<style>
table {
  width: 100%;
  border-collapse: collapse;
}
th, td {
  padding: 8px;
  border: 1px solid #ccc;
}
thead {
  background-color: #eee;
}
</style>
