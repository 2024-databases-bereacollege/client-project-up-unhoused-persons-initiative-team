<template>
    <div class="insufficient-access-page">
      <div class="message-container">
        <h1>Invalid Access</h1>
        <p>Please ask to have Record Access if you need to view this page!</p>
        <router-link to="/" class="btn">Go Back to Home</router-link>
      </div>
    </div>
  </template>
  
  <style scoped>
  .insufficient-access-page {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    background-color: #f5f5f5;
  }
  
  .message-container {
    text-align: center;
    padding: 40px;
    background-color: #ffffff;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  }
  
  h1 {
    font-size: 24px;
    color: #333333;
    margin-bottom: 20px;
  }
  
  p {
    font-size: 18px;
    color: #666666;
    margin-bottom: 30px;
  }
  
  .btn {
    display: inline-block;
    padding: 10px 20px;
    font-size: 16px;
    font-weight: bold;
    text-decoration: none;
    color: #ffffff;
    background-color: #007bff;
    border-radius: 4px;
    transition: background-color 0.3s ease;
  }
  
  .btn:hover {
    background-color: #0056b3;
  }
  </style>
