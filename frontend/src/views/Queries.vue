<template>
  <div class="title-section">
    <h3 class="title">
      On this page we can find two rows of tabs. One displaying a set of tables with different attributes,<br>
      and the other displaying tables without those attributes.
    </h3>
  </div>
  <v-card>
    <v-tabs v-model="activeTab" bg-color="deep-purple-darken-4" center-active>
      <v-tab v-for="(tab, index) in tabs" :key="index">{{ tab.title }}</v-tab>
    </v-tabs>
    <v-card-text>
      <div class="total-count">
        <h3>Total: {{ currentTabTotal }} out of {{ totalNeighbors }} Neighbors</h3>
        <v-btn color="primary" @click="exportToExcel(currentTabItems, tabs[activeTab].title)">Export to Excel</v-btn>
      </div>
      <v-data-table
        :headers="headers"
        :items="currentTabItems"
        :items-per-page="10"
        class="elevation-1"
      ></v-data-table>
    </v-card-text>
  </v-card>
  <v-row>
    <v-card cols="12">
      <v-tabs v-model="activeWithoutTab" bg-color="deep-purple-darken-4" center-active>
        <v-tab v-for="(tab, index) in withoutTabs" :key="index">{{ tab.title }}</v-tab>
      </v-tabs>
      <v-card-text>
        <div class="total-count">
          <h3>Total: {{ currentWithoutTabTotal }} out of {{ totalNeighbors }} Neighbors</h3>
          <v-btn color="primary" @click="exportToExcel(currentWithoutTabItems, withoutTabs[activeWithoutTab].title)">Export to Excel</v-btn>
        </div>
        <v-data-table
          :headers="headers"
          :items="currentWithoutTabItems"
          :items-per-page="100"
          class="elevation-1"
        ></v-data-table>
      </v-card-text>
    </v-card>
  </v-row>
</template>
<script>
import axios from 'axios';
import * as XLSX from 'xlsx';

export default {
  data() {
    return {
      activeTab: 0,
      activeWithoutTab: 0,
      neighbors: [],
      headers: [
        { title: 'ID', value: 'NeighborID' },
        { title: 'First Name', value: 'FirstName' },
        { title: 'Last Name', value: 'LastName' },
      ],
      tabs: [
        { title: 'Neighbors with State ID', attribute: 'HasStateID' },
        { title: 'Neighbors with Pets', attribute: 'HasPet' },
        { title: 'Neighbors with Children', attribute: 'HasChildren' },
        { title: 'Neighbors with Medication', attribute: 'HasMedication' },
        { title: 'Neighbors with Food Insecurity', attribute: 'HasFoodInsecurity' },
        { title: 'Neighbors with Transportation', attribute: 'HasTransportation' },
        { title: 'Neighbors with Job', attribute: 'HasJob' },
        { title: 'Neighbors with Housing', attribute: 'HasHousing' },
        { title: 'Neighbors with Income', attribute: 'HasIncome' },
      ],
      withoutTabs: [
        { title: 'Neighbors without State ID', attribute: 'HasStateID' },
        { title: 'Neighbors without Pets', attribute: 'HasPet' },
        { title: 'Neighbors without Children', attribute: 'HasChildren' },
        { title: 'Neighbors without Medication', attribute: 'HasMedication' },
        { title: 'Neighbors without Food Insecurity', attribute: 'HasFoodInsecurity' },
        { title: 'Neighbors without Transportation', attribute: 'HasTransportation' },
        { title: 'Neighbors without Job', attribute: 'HasJob' },
        { title: 'Neighbors without Housing', attribute: 'HasHousing' },
        { title: 'Neighbors without Income', attribute: 'HasIncome' },
      ],
    };
  },
  computed: {
    currentTabItems() {
      const currentTab = this.tabs[this.activeTab];
      return this.neighbors.filter(neighbor => neighbor[currentTab.attribute]);
    },
    currentTabTotal() {
      return this.currentTabItems.length;
    },
    currentWithoutTabItems() {
      const currentWithoutTab = this.withoutTabs[this.activeWithoutTab];
      return this.neighbors.filter(neighbor => !neighbor[currentWithoutTab.attribute]);
    },
    currentWithoutTabTotal() {
      return this.currentWithoutTabItems.length;
    },
    totalNeighbors() {
      return this.neighbors.length;
    },
  },
  created() {
    this.fetchData();
  },
  methods: {
    fetchData() {
      axios.get('http://127.0.0.1:5000/api/neighbors')
        .then(response => {
          this.neighbors = response.data;
        })
        .catch(error => {
          console.error('Error fetching data:', error);
        });
    },
    exportToExcel(data, title) {
      const worksheet = XLSX.utils.json_to_sheet(data);
      const workbook = XLSX.utils.book_new();
      XLSX.utils.book_append_sheet(workbook, worksheet, 'Sheet1');
      XLSX.writeFile(workbook, `${title}.xlsx`);
    },
  },
};
</script>
<style scoped>
.total-count {
  margin-bottom: 16px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.total-count h3 {
  font-size: 20px;
  font-weight: bold;
}

.v-data-table {
  margin-top: 16px;
}

.title-section {
  background-color: #f5f5f5;
  padding: 20px;
  text-align: center;
  border-bottom: 1px solid #e0e0e0;
}

.title {
  font-size: 1.2rem;
  font-weight: bold;
  color: #333;
  line-height: 1.5;
}
</style>
