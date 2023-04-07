// App.js

import React, { useState } from 'react';

const App = () => {
  const [greeting, setGreeting] = useState('');

  const handleGreet = async () => {
    try {
      const response = await fetch('/greet', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: new URLSearchParams({ name: 'Nadge Sachin' }), // Pass the user's name as data
      });

      const data = await response.json();
      setGreeting(data.greeting);
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <div>
      <button onClick={handleGreet}>Hello Server</button>
      <p>{greeting}</p>
    </div>
  );
};

export default App;
