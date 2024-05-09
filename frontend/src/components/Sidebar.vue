<template>
  
<div class="sidebar-links">
  <div class="logo">
    <img :src="require('../assets/upClouds.png')" alt="UP Initiative Logo" class="logo-image" />
  </div>
  <router-link to="/" class="sidebar-link">
    <font-awesome-icon :icon="faHome" />
    <span>Home Page</span>
  <!-- </router-link>
  <router-link to="/Instructions" class="sidebar-link">
    <font-awesome-icon :icon="faInfoCircle" />
    <span>Instructions</span> -->
  </router-link>
  <router-link to="/Add_Visit" class="sidebar-link">
    <font-awesome-icon :icon="faPlusCircle" />
    <span>Add Visit</span>
  <!-- </router-link>
  <router-link to="/login_page" class="sidebar-link">
    <font-awesome-icon :icon="faSignInAlt" />
    <span>Login Page</span> -->
  </router-link>
  <router-link to="/Volunteers" class="sidebar-link">
    <font-awesome-icon :icon="faUserFriends" />
    <span>Volunteers</span>
  </router-link>
  <router-link to="/Neighbors" class="sidebar-link">
    <font-awesome-icon :icon="faUsers" />
    <span>Neighbors</span>
  </router-link>
  <!-- <router-link to="/Visit_Records" class="sidebar-link">
    <font-awesome-icon :icon="faClipboardList" />
    <span>Visit Record</span>
  </router-link> -->
  <router-link to="/Visit_Logs" class="sidebar-link">
    <font-awesome-icon :icon="faClipboardList" />
    <span>All Visit Logs</span>
  </router-link>
  <router-link to="/ServicesAndProviders" class="sidebar-link">
    <font-awesome-icon :icon="faHandHoldingHeart" />
    <span>Services and Providers</span>
  <!-- </router-link>
  <router-link to="/Service_Providers" class="sidebar-link">
    <font-awesome-icon :icon="faBuilding" />
    <span>Service Providers</span> -->
  </router-link>
  <!-- <router-link to="/Inventory" class="sidebar-link"> TODO need to add inventory back
    <font-awesome-icon :icon="faBox" />
    <span>Inventory</span>
  </router-link> -->
  <router-link to="/Queries" class="sidebar-link">
    <font-awesome-icon :icon="faClipboardList" />
    <span>Queries</span>
  </router-link>
  <!-- <router-link to="/Neighbors/MNP" class="sidebar-link">
    <font-awesome-icon :icon="faUsers" />
    <span>Individual Neighbor Records Links</span>
  </router-link> -->
  <!-- <router-link to="/Neighbors/#ID" class="sidebar-link">
    <font-awesome-icon :icon="faUsers" />
    <span>Individual Neighbor Records</span>
  </router-link> -->
  
</div>
</template>

<script>
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { faHome, faPlusCircle, faSignInAlt, faUserFriends, faUsers, faClipboardList, faHandHoldingHeart, faBuilding, faBox, faInfoCircle } from '@fortawesome/free-solid-svg-icons'
//import logo from '../assets/UPLOGO.PNG';

export default {
  components: {
    FontAwesomeIcon
  },
  data() {
    return {
      faHome,
      faPlusCircle,
      faSignInAlt,
      faUserFriends,
      faUsers,
      faClipboardList,
      faHandHoldingHeart,
      faBuilding,
      faBox,
      faInfoCircle,
      //logo,
    }
  }
}
</script>

<style>

.logo-image {
  width: 200px; 
  height: auto; /* Maintain the aspect ratio */
}

.sidebar {
  width: 16rem;
  background-color: #333;
  height: 100vh;
  position: fixed;
  left: 0;
  top: 0;
  display: flex;
  flex-direction: column;
  padding: 1rem;
  color: #fff;
  z-index: 1000; /* Adds a higher z-index value */
}

.sidebar-header {
  margin-bottom: 1rem;
}

.sidebar-links {
  display: flex;
  flex-direction: column;
}

.sidebar-link {
  display: flex;
  align-items: center;
  padding: 0.5rem 1rem;
  text-decoration: none;
  color: #fff;
  transition: background-color 0.3s ease;
  border-radius: 0.25rem;
  margin-bottom: 0.5rem;
}

.sidebar-link:hover {
  background-color: #555;
}

.sidebar-link svg {
  margin-right: 0.5rem;
}

/* Adds a new class for the main content */
.main-content {
  margin-left: 16rem; /* Add a left margin equal to the width of the sidebar */
  padding: 1rem;
}

</style>
