const fs = require('fs').promises;

async function countStudents(filePath) {
  try {
    // Read the file asynchronously
    const data = await fs.readFile(filePath, 'utf8');

    // Split the CSV data into lines
    const lines = data.split('\n');

    // Initialize an object to store the count for each field
    const fieldCounts = {};

    // Iterate through each line
    lines.forEach((line) => {
      // Skip empty lines
      if (line.trim() !== '') {
        // Split the line into fields
        const fields = line.split(',');

        // Extract the field name (assuming it's the first element in each line)
        const fieldName = fields[0];

        // Increment the count for the field in the fieldCounts object
        fieldCounts[fieldName] = (fieldCounts[fieldName] || 0) + 1;
      }
    });

    // Log the results
    console.log('Number of students:', lines.length - 1); // Subtract 1 to exclude the header
    Object.keys(fieldCounts).forEach((field) => {
      const count = fieldCounts[field];
      const list = lines
        .filter((line) => line.startsWith(field))
        .map((line) => line.split(',')[1])
        .join(', ');

      console.log(`Number of students in ${field}: ${count}. List: ${list}`);
    });

    // Return a resolved Promise
    return Promise.resolve();
  } catch (error) {
    // Log and throw an error if reading the file fails
    console.error('Cannot load the database:', error.message);
    throw error;
  }
}

// Example usage
countStudents('database.csv')
  .then(() => {
    console.log('Done!');
  })
  .catch((error) => {
    console.log(error);
  });

console.log('After!');
module.exports = countStudents;