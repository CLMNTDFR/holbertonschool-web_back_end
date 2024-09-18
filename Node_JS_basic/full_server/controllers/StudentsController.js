const { readDatabase } = require('../utils');

class StudentsController {
  static getAllStudents(req, res) {
    const databaseFile = process.argv[2];
    readDatabase(databaseFile)
      .then((students) => {
        let responseText = 'This is the list of our students\n';
        Object.keys(students).sort().forEach((field) => {
          responseText += `Number of students in ${field}: ${students[field].length}. List: ${students[field].join(', ')}\n`;
        });
        res.status(200).send(responseText.trim());
      })
      .catch(() => {
        res.status(500).send('Cannot load the database');
      });
  }

  static getAllStudentsByMajor(req, res) {
    const databaseFile = process.argv[2];
    const { major } = req.params;
    if (major !== 'CS' && major !== 'SWE') {
      res.status(500).send('Major parameter must be CS or SWE');
      return;
    }
    readDatabase(databaseFile)
      .then((students) => {
        if (!students[major]) {
          res.status(500).send('Cannot load the database');
          return;
        }
        res.status(200).send(`List: ${students[major].join(', ')}`);
      })
      .catch(() => {
        res.status(500).send('Cannot load the database');
      });
  }
}

module.exports = StudentsController;