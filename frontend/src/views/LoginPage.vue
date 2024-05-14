<template>
  <div class="login-page">
    <div class="login-box">
      <h1>Login</h1>
      <form @submit.prevent="submitLogin">
        <div class="form-group">
          <label for="username">Username:</label>
          <input type="text" id="username" v-model="username" placeholder="Enter your username" required>
        </div>
        <div class="form-group">
          <label for="password">Password:</label>
          <input type="password" id="password" v-model="password" placeholder="Enter your password" required>
        </div>
        <button type="submit">Login</button>
      </form>
      <div v-if="errorMessage" class="error-message">{{ errorMessage }}</div>
      <div class="logout-container">
        <button class="logout-button" @click="logout">Logout</button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import { mapActions } from 'vuex';

export default {
  data() {
    return {
      username: '',
      password: '',
      errorMessage: '',
    };
  },
  methods: {
    ...mapActions('auth', ['login', 'setVolunteer', 'setHasRecordAccess', 'logout']),
    async submitLogin() {
  const loginData = {
    username: this.username,
    password: this.password,
  };
  try {
    const response = await axios.post('http://127.0.0.1:5000/api/login', loginData);
    const volunteer = response.data.volunteer;
    await this.$store.dispatch('auth/setVolunteer', volunteer);
    await this.$store.dispatch('auth/login');
    await this.$store.dispatch('auth/setHasRecordAccess', volunteer.has_record_access);

    // Store the login information in local storage
    localStorage.setItem('loggedInVolunteer', JSON.stringify(volunteer));

    this.$router.push('/home');
  } catch (error) {
        console.error('Login failed:', error);
        if (error.response && error.response.status === 401) {
          this.errorMessage = 'Invalid username or password. Please try again.';
        } else {
          this.errorMessage = 'An error occurred. Please try again later.';
        }
      }
    },
  },
};
</script>

<style scoped>
.login-page {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background-color: #f2f2f2;
}

.error-message {
  color: red;
  margin-top: 10px;
}

.login-box {
  max-width: 400px;
  padding: 40px;
  background-color: #fff;
  border-radius: 5px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

h2 {
  text-align: center;
  margin-bottom: 20px;
}

.form-group {
  margin-bottom: 20px;
}

label {
  display: block;
  margin-bottom: 5px;
}

input[type="text"], input[type="password"] {
  width: 100%;
  padding: 12px;
  font-size: 16px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

button {
  width: 100%;
  padding: 12px;
  font-size: 16px;
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.logout-container {
  display: flex;
  justify-content: center;
  margin-top: 20px;
}

.logout-button {
  padding: 8px 16px;
  font-size: 14px;
  background-color: #dc3545;
  color: #fff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.logout-button:hover {
  background-color: #c82333;
}

a {
  color: #007bff;
  text-decoration: none;
}
</style>
