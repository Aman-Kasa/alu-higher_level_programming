#!/usr/bin/node
const request = require('request');

// Get the API URL from the command line argument
const apiUrl = process.argv[2];

// Send a GET request to the API URL
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error); // Print error if there's any
  } else {
    // Parse the response body (it's JSON data)
    const tasks = JSON.parse(body);
    const completedTasks = {};

    // Iterate through each task
    tasks.forEach(task => {
      if (task.completed) {
        if (completedTasks[task.userId] === undefined) {
          completedTasks[task.userId] = 0;
        }
        completedTasks[task.userId] += 1;
      }
    });

    // Print the completed tasks count for each user
    console.log(completedTasks);
  }
});
