// Step 2: Use Fetch API to read the data from data.json
fetch('data.json')
  .then((response) => response.json())
  .then((jsonData) => {
    // Step 3: Use forEach() method to display fields in the browser console
    jsonData.forEach((record) => {
      console.log(`Name: ${record.name}, Age: ${record.age}, City: ${record.city}`);
    });
  })
  .catch((error) => {
    console.error('Error fetching data:', error);
  });