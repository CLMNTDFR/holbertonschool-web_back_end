const http = require('http');
const fs = require('fs');

// Helper function to read and parse the CSV file
const countStudents = (databasePath) => new Promise((resolve, reject) => {
  fs.readFile(databasePath, 'utf8', (err, data) => {
    if (err) {
      reject(new Error('Cannot load the database'));
    } else {
      const lines = data.split('\n').filter((line) => line.trim() !== ''); // Remove empty lines
      const students = lines.slice(1).map((line) => line.split(',')); // Skip the first line (header)

      // Filter valid lines (those with 4 elements)
      const validStudents = students.filter((student) => student.length === 4);

      // Count the total number of students
      const totalStudents = validStudents.length;

      // Group students by their field (CS, SWE)
      const csStudents = validStudents.filter((student) => student[3] === 'CS');
      const sweStudents = validStudents.filter((student) => student[3] === 'SWE');

      // Resolve with the student counts and lists
      resolve({
        totalStudents,
        cs: {
          count: csStudents.length,
          list: csStudents.map((student) => student[0]),
        },
        swe: {
          count: sweStudents.length,
          list: sweStudents.map((student) => student[0]),
        },
      });
    }
  });
});

// Create the HTTP server
const app = http.createServer(async (req, res) => {
  const { url } = req;

  // Handle the root route "/"
  if (url === '/') {
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.end('Hello Holberton School!');
  } else if (url === '/students') {
    const databasePath = process.argv[2]; // The CSV file is passed as an argument

    if (!databasePath) {
      res.writeHead(500, { 'Content-Type': 'text/plain' });
      res.end('No database provided');
      return;
    }

    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.write('This is the list of our students\n');

    try {
      const studentsData = await countStudents(databasePath);

      // Ensure that the resolved data is in the expected format
      if (studentsData) {
        res.write(`Number of students: ${studentsData.totalStudents}\n`);
        res.write(`Number of students in CS: ${studentsData.cs.count}. List: ${studentsData.cs.list.join(', ')}\n`);
        res.write(`Number of students in SWE: ${studentsData.swe.count}. List: ${studentsData.swe.list.join(', ')}`);
      } else {
        throw new Error('Cannot parse students data');
      }
    } catch (error) {
      res.write(error.message);
    }

    res.end(); // End the response properly
  } else {
    res.writeHead(404, { 'Content-Type': 'text/plain' });
    res.end('Not Found');
  }
});

// Make the server listen on port 1245
app.listen(1245);

// Export the app for testing or further usage
module.exports = app;