<template>
    <div>
      <v-card>
        <v-card-title class="d-flex justify-space-between align-center">
          <div>
            <v-btn color="primary" @click="openAddVisitLogDialog">Add Visit Log</v-btn>
            <span class="text-h5 mx-4">Visit Logs</span>
          </div>
        </v-card-title>
        <v-data-table
          :headers="headers"
          :items="visitLogs"
          :items-per-page="100"
          :loading="loading"
          class="elevation-1"
        >
          <!-- Add additional slot templates for displaying data if needed -->
        </v-data-table>
      </v-card>
  
      <!-- Add Visit Log Dialog -->
      <v-dialog v-model="addVisitLogDialog" max-width="500px">
        <v-card>
          <v-card-title class="text-h5">Add Visit Log</v-card-title>
          <v-card-text>
            <v-select
              v-model="newVisitLog.NeighborID"
              :items="neighbors"
              item-text="FullName"
              item-value="NeighborID"
              label="Neighbor"
            ></v-select>
            <v-select
              v-model="newVisitLog.ServiceID"
              :items="services"
              item-text="ServiceName"
              item-value="ServiceID"
              label="Service"
            ></v-select>
            <v-select
              v-model="newVisitLog.VolunteerID"
              :items="volunteers"
              item-text="FullName"
              item-value="VolunteerID"
              label="Volunteer"
            ></v-select>
            <v-text-field v-model="newVisitLog.Date" label="Date" type="date"></v-text-field>
            <v-textarea v-model="newVisitLog.Description" label="Description"></v-textarea>
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="blue darken-1" text @click="closeAddVisitLogDialog">Cancel</v-btn>
            <v-btn color="blue darken-1" text @click="addVisitLog">Add</v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        headers: [
          { title: 'Visit Date', key: 'Date' },
          { title: 'Neighbor Name', key: 'NeighborName' },
          { title: 'Neighbor ID', key: 'NeighborID' },
          { title: 'Service Name', key: 'ServiceName' },
          { title: 'Service Provider', key: 'ServiceProvider' },
          { title: 'Volunteer Name', key: 'VolunteerName' },
          { title: 'Description', key: 'Description' },
        ],
        visitLogs: [],
        loading: true,
        addVisitLogDialog: false,
        neighbors: [],
        services: [],
        volunteers: [],
        newVisitLog: {
          NeighborID: null,
          ServiceID: null,
          VolunteerID: null,
          Date: '',
          Description: '',
        },
      };
    },
    mounted() {
      this.fetchVisitLogs();
      this.fetchNeighbors();
      this.fetchServices();
      this.fetchVolunteers();
    },
    methods: {
      fetchVisitLogs() {
        axios.get('http://127.0.0.1:5000/api/visit_logs')
          .then(response => {
            this.visitLogs = response.data;
            this.loading = false;
          })
          .catch(error => {
            console.error('Error fetching visit logs:', error);
            this.loading = false;
          });
      },
      fetchNeighbors() {
        axios.get('http://127.0.0.1:5000/api/neighbors')
          .then(response => {
            this.neighbors = response.data.map(neighbor => ({
              ...neighbor,
              FullName: `${neighbor.FirstName} ${neighbor.LastName}`,
            }));
          })
          .catch(error => {
            console.error('Error fetching neighbors:', error);
          });
      },
      fetchServices() {
        axios.get('http://127.0.0.1:5000/api/services')
          .then(response => {
            this.services = response.data.map(service => ({
              ...service,
              ServiceName: service.ServiceType,
            }));
          })
          .catch(error => {
            console.error('Error fetching services:', error);
          });
      },
      fetchVolunteers() {
        axios.get('http://127.0.0.1:5000/api/volunteers')
          .then(response => {
            this.volunteers = response.data.map(volunteer => ({
              ...volunteer,
              FullName: `${volunteer.FirstName} ${volunteer.LastName}`,
            }));
          })
          .catch(error => {
            console.error('Error fetching volunteers:', error);
          });
      },
      openAddVisitLogDialog() {
        this.addVisitLogDialog = true;
      },
      closeAddVisitLogDialog() {
        this.newVisitLog = {
          NeighborID: null,
          ServiceID: null,
          VolunteerID: null,
          Date: '',
          Description: '',
        };
        this.addVisitLogDialog = false;
      },
    },
  };
  </script>
