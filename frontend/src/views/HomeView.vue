<template>
  <div class="homepage">
  <header>
  <h1>Welcome to the UP Initiative Database!</h1>
  </header>
  <main>
  <section class="hero">
  <h1></h1>
  <a href="/Instructions" class="cta-button">Get Started</a>
  </section>
  <section class="features">
  <div class="feature">
  <i class="fas fa-rocket"></i>
  <h2>Centralized Information</h2>
  <p>Discover everything you need in one convenient location!</p>
  <p>Explore the side tabs to access comprehensive details about your organization and its operations.</p>
  <p>It's all designed to be right at your fingertips, simplifying how you connect with the information that matters most.</p>
  <p>Visit the Queries page to view specialized information about our neighbors and gain valuable insights!</p>
  </div>
  <div class="feature">
  <i class="fas fa-shield-alt"></i>
  <h2>Visit Various Pages to Manage Profiles</h2>
  <p>Navigate to the Neighbors, Organizations, and Users pages to quickly create, update, and delete profiles for various entities.</p>
  <p>Our intuitive tools make it simple to manage crucial information and keep your database up-to-date.</p>
  </div>
  <div class="feature">
  <i class="fas fa-book"></i>
  <h2>Keep a Complete Visit Log of Every UP Interaction</h2>
  <p>We understand the importance of tracking and documenting each interaction with our neighbors.</p>
  <p>That's why we securely store every relevant aspect of these interactions in a comprehensive visit log.</p>
  <p>Access to the visit log is tailored to each user's role, ensuring that sensitive information remains protected while still providing valuable insights for our team.</p>
  </div>
  </section>
  </main>
  <footer>
  <p>&copy; 2024 UP Initiative. All rights reserved.</p>
  </footer>
  </div>
  </template>

<script>
export default {
  name: 'HomePage',
}
</script>

<style scoped>
.homepage {
  font-family: Arial, sans-serif;
  color: #333;
}

header {
  background-color: #f8f8f8;
  padding: 20px;
}

nav ul {
  list-style: none;
  display: flex;
  justify-content: center;
}

nav ul li {
  margin: 0 10px;
}

nav ul li a {
  text-decoration: none;
  color: #333;
  font-weight: bold;
}

.hero {
  text-align: center;
  padding: 100px 0;
  background-image: url('../assets/madisonCounty.jpeg');
  background-size: 40% auto;
  background-position: center;
  color: #fff;
}

.hero h1 {
  font-size: 36px;
  margin-bottom: 20px;
}

.hero p {
  font-size: 18px;
  margin-bottom: 30px;
}

.cta-button {
  display: inline-block;
  padding: 10px 20px;
  background-color: #333;
  color: #fff;
  text-decoration: none;
  border-radius: 4px;
}

.features {
  display: flex;
  justify-content: space-around;
  padding: 50px 0;
}

.feature {
  text-align: center;
  max-width: 300px;
}

.feature i {
  font-size: 48px;
  margin-bottom: 20px;
  color: #333;
}

.feature h2 {
  font-size: 24px;
  margin-bottom: 10px;
}

.feature p {
  font-size: 16px;
}

footer {
  background-color: #333;
  color: #fff;
  text-align: center;
  padding: 20px;
}
</style>
