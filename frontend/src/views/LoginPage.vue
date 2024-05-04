

<!-- <template>
  <div class="login-page">
    <div class="login-box">
      <h1>Login</h1>
      <form @submit.prevent="login">
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
      <p>Don't have an account? <a href="/register">Register</a></p>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      username: '',
      password: '',
    };
  },
  methods: {
    login() {
      const loginData = {
        username: this.username,
        password: this.password,
      };

      axios.post('http://127.0.0.1:5000/api/login', loginData)
        .then(response => {
          // Login successful
          const volunteer = response.data.volunteer;
          console.log('Logged in as:', volunteer);
          // TODO: Store the volunteer data in Vuex store or local storage
          // TODO: Redirect to a logged-in page or perform other actions
        })
        .catch(error => {
          console.error('Login failed:', error);
          // TODO: Display an error message to the user
        });
    },
  },
};
</script> -->

<!-- <template>
  <div class="login-page">
    <div class="login-box">
      <h1>Login</h1>
      <form @submit.prevent="onLogin">
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
      <p>Don't have an account? <a href="/register">Register</a></p>
    </div>
  </div>
</template>

<script>
import { mapActions } from 'vuex';

export default {
  data() {
    return {
      username: '',
      password: '',
    };
  },
  methods: {
    ...mapActions(['login']),
    onLogin() {
      const credentials = {
        username: this.username,
        password: this.password,
      };
      this.login(credentials)
        .then(() => {
          // Redirect to a protected page or perform other actions upon successful login
          this.$router.push('/home');
        })
        .catch(error => {
          // Handle login error
          console.error('Login failed:', error);
        });
    },
  },
};
</script> -->

<template>
  <div class="login-page">
    <div class="login-box">
      <h1>Login</h1>
      <form @submit.prevent="login">
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
      <p>Don't have an account? <a href="/register">Register</a></p>
      <div v-if="errorMessage" class="error-message">{{ errorMessage }}</div>
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
    ...mapActions(['setVolunteer']),
    login() {
      const loginData = {
        username: this.username,
        password: this.password,
      };

      axios.post('http://127.0.0.1:5000/api/login', loginData)
        .then(response => {
          // Login successful
          const volunteer = response.data.volunteer;
          this.setVolunteer(volunteer);
          // Redirect to a logged-in page or perform other actions
          this.$router.push('/dashboard');
        })
        .catch(error => {
          console.error('Login failed:', error);
          this.errorMessage = 'Invalid username or password. Please try again.';
        });
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

input[type="text"],
input[type="password"] {
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

a {
  color: #007bff;
  text-decoration: none;
}
</style>
