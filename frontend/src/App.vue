<template>
  <div class="app">
    <TopBar />
    <div v-if="isAuthenticated" class="sidebar">
      <Sidebar />
    </div>
    <div class="main-content">
      <router-view @reloadApp="reloadApp" />
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
    Sidebar,
  },
  mounted() {
    this.$store.dispatch('auth/checkLocalStorage');
  },
  computed: {
    ...mapGetters('auth', ['isAuthenticated']),
  },
  methods: {
    reloadApp() {
      window.location.reload();
    },
  },
};
</script>

<style>
/* Styles from App.vue */
#app {
  text-align: center;
  margin-top: 50px;
}

.Main .content {
  margin-left: 16rem; /* Push content to the right of the sidebar */
  padding: 1rem; /* Padding around content */
  flex-grow: 1; 
  background-color: #e7e7e7;
  height: auto; 
}

.about {
  display: flex; /* Keep this to align items horizontally */
}

.links {
  display: flex;
  flex-direction: column; /* Stack links vertically */
  padding: 0; 
  margin-right: 2rem; 
}

.links a {
  padding: 0.5rem; 
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
