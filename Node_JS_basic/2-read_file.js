const fs = require('fs');

function countStudents(filePath) {
  try {
    // Lire le fichier de manière synchrone
    const data = fs.readFileSync(filePath, 'utf8');
    // Diviser les lignes par retour à la ligne
    const lines = data.split('\n').filter((line) => line.trim() !== '');

    // Vérifier qu'il y a des étudiants
    if (lines.length <= 1) {
      console.log('Number of students: 0');
      return;
    }

    // Enlever l'en-tête et créer un tableau pour les étudiants
    const students = lines.slice(1).map((line) => {
      const [firstname, , , field] = line.split(','); // Ignorer lastname et age
      return { firstname, field };
    });

    // Compter les étudiants par domaine
    const fieldCount = {};
    students.forEach((student) => {
      if (!fieldCount[student.field]) {
        fieldCount[student.field] = [];
      }
      fieldCount[student.field].push(student.firstname);
    });

    // Afficher le nombre total d'étudiants
    console.log(`Number of students: ${students.length}`);

    // Afficher les étudiants par domaine
    for (const [field, names] of Object.entries(fieldCount)) {
      console.log(`Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`);
    }
  } catch (error) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;