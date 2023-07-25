#!/usr/bin/node
const request = require('request');

request(process.argv[2], (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const todos = JSON.parse(body);
    const completedTasksByUserId = todos.reduce((acc, todo) => {
      if (todo.completed) acc[todo.userId] = (acc[todo.userId] || 0) + 1;
      return acc;
    }, {});
    console.log(completedTasksByUserId);
  } else {
    console.error('Error:', error || `Status code: ${response.statusCode}`);
  }
});
