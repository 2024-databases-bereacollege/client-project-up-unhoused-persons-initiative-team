<!-- TopBar.vue -->
<template>
  <div class="top-bar">
    <h1 class="organization-name">UP Initiative</h1>
    <div class="menu-buttons">
      <router-link to="/home" class="menu-button">
        <font-awesome-icon :icon="faHome" /> Home
      </router-link>
      <router-link to="/Instructions" class="menu-button">
        <font-awesome-icon :icon="faInfoCircle" /> Instructions
      </router-link>
      <router-link to="/login_page" class="menu-button">
        <font-awesome-icon :icon="faSignInAlt" /> Login
      </router-link>
    </div>
  </div>
</template>

<script>
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
import { faHome, faInfoCircle, faSignInAlt } from '@fortawesome/free-solid-svg-icons';

export default {
  name: 'TopBar',
  components: {
    FontAwesomeIcon,
  },
  data() {
    return {
      faHome,
      faInfoCircle,
      faSignInAlt,
    };
  },
};
</script>

<style scoped>
/* ... (previous styles remain the same) */

.menu-button svg {
  margin-right: 0.5rem;
}

.top-bar {
  margin-left: 16rem; /* Push content to the right of the sidebar */
  display: flex;
  align-items: center;
  justify-content: space-between;
  background-color: #9c97ff;
  padding: 1rem;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  margin: 0;
  width: 100%;
  position: fixed;
  top: 0;
  left: 0;
  z-index: 999;
}

.organization-name {
  margin-left: 16rem;
  font-size: 1.5rem;
  font-weight: bold;
  color: #333;
  margin: 0;
}

.menu-buttons {
  display: flex;
  align-items: center;
}

.menu-button {
  margin-left: 1rem;
  padding: 0.5rem 1rem;
  background-color: #fff;
  color: #333;
  text-decoration: none;
  border-radius: 4px;
  font-weight: bold;
  transition: background-color 0.3s;
}

.menu-button:hover {
  background-color: #f0f0f0;
}
</style>
