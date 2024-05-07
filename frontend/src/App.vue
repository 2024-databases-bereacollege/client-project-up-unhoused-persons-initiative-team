<template>
  <div class="app">
    <TopBar />
    <div v-if="isAuthenticated" class="sidebar">
      <Sidebar />
    </div>
    <div class="main-content">
      <!-- Main content goes here -->
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';
import TopBar from './components/TopBar.vue';
import Sidebar from './components/Sidebar.vue';

export default {
  name: 'MainLayout',
  components: {
    TopBar,
    Sidebar
  },
  computed: {
  ...mapGetters('auth', ['isAuthenticated'])
}
}
</script>

<style>
/* Styles from App.vue */
#app {
  text-align: center;
  margin-top: 50px;
}

/* Styles from Main.vue, adjusted if necessary */
.Main .content {
  margin-left: 16rem; /* Push content to the right of the sidebar */
  padding: 1rem; /* Padding around content */
  flex-grow: 1; /* Allow the content area to fill the remaining space */
  background-color: #e7e7e7; /* Background color for the content */
  height: auto; /* Adjust height as needed */
}

/* Additional styles from Main.vue */
.about {
  display: flex; /* Keep this to align items horizontally */
}

.links {
  display: flex;
  flex-direction: column; /* Stack links vertically */
  padding: 0; /* Adjust padding as needed */
  margin-right: 2rem; /* Space between links and content */
}

.links a {
  padding: 0.5rem; /* Adjust padding to your liking */
  text-decoration: none;
  background-color: #e7e7e7;
  color: #000000;
  margin-bottom: 1rem; /* Space between links */
}

.links .router-link-exact-active {
  background-color: #cc0000;
  color: #FFFFFF;
}
</style>
