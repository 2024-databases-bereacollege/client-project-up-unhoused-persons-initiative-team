<template>
  <div class="homepage">
    <header>
      <h1>Welcome to the UP Initiative Application!</h1>
    </header>

    <main>
      <section class="hero">
        <h1></h1>
     <!--   <p>This database is a robust solution that can streamline the <br>
          storage, management, and retrieval of your data, <br>
          enhancing operational efficiency and supporting informed decision-making <br>
          across your organization.
        </p> -->
        <a href="/Instructions" class="cta-button">Get Started</a>
      </section>

      <section class="features">
        <div class="feature">
          <i class="fas fa-rocket"></i>
          <h2>Centralized Information</h2>
          <p>Discover everything you need in one convenient location! </p>
          <p>Explore the side tabs to access comprehensive details about your organization and its operations.  </p>
          <p> It's all designed to be right at your fingertips, simplifying how you connect with the information that matters most. </p>
        </div>
        <div class="feature">
          <i class="fas fa-mobile-alt"></i>
          <h2>Keep Track of Your Inventory</h2>
          <p>Managing your inventory has never been easier!  </p>
          <p> Add or remove items with just a few clicks, and instantly see which items are most needed. </p>
          <p> This streamlined view helps you stay prepared and responsive, ensuring you always have the essentials for those we serve. </p>
        </div>
        <div class="feature">
          <i class="fas fa-shield-alt"></i>
          <h2>Create, Follow Up, and Edit Files with a Single Click</h2>
          <p> Visit the Neighbors page to quickly create and update profiles for new neighbors.  </p>
          <p> Here, you can access crucial information and review their recent interactions with UP. </p>
          <p> Our intuitive tools make it simple to follow each neighbor's journey and provide support every step of the way. </p>
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
