<template>
  <div class="get-started">
  <header>
  </header>
  <main>
  <section class="instructions">
  <h1>Getting Started with the UP Initiative Database</h1>
  <p>Follow these step-by-step instructions to set up and work with the database:</p>
  <div class="instruction-list">
  <div class="instruction-item">
  <div class="instruction-header">
  <h2>1. Login</h2>
  </div>
  <div class="instruction-content">
  <p>Go to the login page and enter your last name as your username and your password. Remember to always keep your password secure!</p>
  <p>Some users have access to specific pages, while others have full record access. This can be changed at any time by editing that volunteer's record access on the volunteer page.</p>
  </div>
  </div>
  <div class="instruction-item">
  <div class="instruction-header">
  <h2>2. Navigation</h2>
  </div>
  <div class="instruction-content">
  <p>After logging in, all the links are located on the left side of the page.</p>
  </div>
  </div>
  <div class="instruction-item">
  <div class="instruction-header">
  <h2>3. Add Visit</h2>
  </div>
  <div class="instruction-content">
  <p>For every visit that occurs within our organization, navigate to the Add Visit page.</p>
  <p>Fill out all the relevant information about the visit, which will update the information stored in every table. Please ensure that you complete every part of this page.</p>
  <p>You can view the visits in two places: the All Visit Logs page and the individual Neighbor Profiles page. Both are set to display the most recent visit first.</p>
  </div>
  </div>
  <div class="instruction-item">
  <div class="instruction-header">
  <h2>4. Sorting and Editing</h2>
  </div>
  <div class="instruction-content">
  <p>Every aspect of every table is sortable by hovering your mouse over the column titles.</p>
  <p>On the right side of most pages, you can edit the information in each row and delete the row altogether.</p>
  </div>
  </div>
  <div class="instruction-item">
  <div class="instruction-header">
  <h2>5. Neighbors Page</h2>
  </div>
  <div class="instruction-content">
  <p>The Neighbors page contains a lot of information, and you may need to scroll right to view the rest of the columns.</p>
  <p>On the far right, you can delete a neighbor or update their information.</p>
  <p>Clicking on a neighbor's ID number (assigned to each neighbor for database organization) will take you to their personal profile page, which is created every time a neighbor is added. Here, you can view all their individual information and see their full list of visits at the bottom.</p>
  </div>
  </div>
  <div class="instruction-item">
  <div class="instruction-header">
  <h2>6. Queries Page</h2>
  </div>
  <div class="instruction-content">
  <p>The Queries page shows detailed information about our neighbors, making it easier to determine who needs what specific type of help.</p>
  </div>
  </div>
  <div class="instruction-item">
  <div class="instruction-header">
  <h2>7. Support</h2>
  </div>
  <div class="instruction-content">
  <p>If you have any questions or encounter any bugs in the application, please contact us at hamiltonn428@gmail.com.</p>
  </div>
  </div>
  </div>
  </section>
  </main>
  </div>
  </template>
  <script>
  export default {
  name: 'GetStarted',
  }
  </script>
  <style scoped>
  .get-started {
  padding: 2rem;
  }
  
  .instructions {
  max-width: 800px;
  margin: 0 auto;
  }
  
  .instruction-list {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  grid-gap: 2rem;
  margin-top: 2rem;
  }
  
  .instruction-item {
  background-color: #f5f5f5;
  border-radius: 8px;
  padding: 1.5rem;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  }
  
  .instruction-header {
  margin-bottom: 1rem;
  }
  
  .instruction-header h2 {
  font-size: 1.5rem;
  color: #333;
  }
  
  .instruction-content p {
  margin-bottom: 0.5rem;
  color: #666;
  }
  </style>
