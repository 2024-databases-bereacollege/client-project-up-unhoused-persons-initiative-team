<template>
  <div class="get-started">
    <header>
  <!--    <nav>
        <ul>
          <li><a href="/">Home</a></li>
        </ul>
      </nav> -->
    </header>
    <main>
      <section class="instructions">
        <h1>Getting Started with the UP Initiative Database</h1>
        <p>Follow these step-by-step instructions to set up and work with the database:</p>
        <div class="instruction-list">
          <div class="instruction-item">
            <div class="instruction-header">
              <h2>1. Add Visit</h2>
            </div>
            <div class="instruction-content">
              <p>Fill the necessary fields for your visit to update your database.</p>
            </div>
          </div>
          <div class="instruction-item">
            <div class="instruction-header">
              <h2>2. Volunteers Information</h2>
            </div>
            <div class="instruction-content">
              <p>Click "New Entry" on the right corner to create a new "Volunteer".</p>
              <p>Click the pen icon to edit a volunteer information, or the X to delete it.</p>
            </div>
          </div>
          <div class="instruction-item">
            <div class="instruction-header">
              <h2>3. Neighbors Information</h2>
            </div>
            <div class="instruction-content">
              <p>Check all of the neighbors and sort them based on different characteristics, like having state ID or not.</p>
            </div>
          </div>
          <div class="instruction-item">
            <div class="instruction-header">
              <h2>4. Visit Record</h2>
            </div>
            <div class="instruction-content">
              <p>See what has been happening with UP and who has been helped.</p>
            </div>
          </div>
          <div class="instruction-item">
            <div class="instruction-header">
              <h2>5. Inventory</h2>
            </div>
            <div class="instruction-content">
              <p>Add items to the inventory and modify it according to your needs.</p>
            </div>
          </div>
        </div>
        <p>That's it! You should now have a basic understanding of how to work with the database in your application. Feel free to explore more advanced features and customize the instructions based on your specific needs.</p>
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
