// Importation des modules nécessaires
const express = require('express');
const fs = require('fs');
const path = require('path');

// Création de l'application Express
const app = express();
// Définition du port d'écoute
const port = 1245;

// Route pour la racine ('/')
app.get('/', (req, res) => {
  // Réponse avec un texte simple
  res.send('Hello Holberton School!');
});

// Route pour '/students'
app.get('/students', (req, res) => {
  // Récupération du nom de la base de données depuis les arguments de la ligne de commande
  const database = process.argv[2];
  if (!database) {
    // Si aucun fichier de base de données n'est fourni, réponse avec un message d'erreur
    res.status(500).send('This is the list of our students\nCannot load the database');
    return;
  }

  // Construction du chemin absolu vers le fichier de base de données
  const filePath = path.resolve(database);
  // Lecture du fichier de base de données de manière asynchrone
  fs.readFile(filePath, 'utf8', (err, data) => {
    if (err) {
      // En cas d'erreur de lecture, réponse avec un message d'erreur
      res.status(500).send('This is the list of our students\nCannot load the database');
      return;
    }

    try {
      // Séparation des lignes du fichier et filtrage des lignes vides
      const lines = data.split('\n').filter((line) => line.trim() !== '');
      // Extraction des données des étudiants à partir des lignes
      const students = lines.slice(1).map((line) => line.split(','));

      // Filtrage des étudiants par filière (CS et SWE)
      const csStudents = students.filter((student) => student[3] === 'CS');
      const sweStudents = students.filter((student) => student[3] === 'SWE');

      // Construction du texte de réponse
      let responseText = 'This is the list of our students\n';
      responseText += `Number of students: ${students.length}\n`;
      responseText += `Number of students in CS: ${csStudents.length}. List: ${csStudents.map((student) => student[0]).join(', ')}\n`;
      responseText += `Number of students in SWE: ${sweStudents.length}. List: ${sweStudents.map((student) => student[0]).join(', ')}`;

      // Envoi de la réponse
      res.send(responseText);
    } catch (error) {
      // En cas d'erreur de traitement des données, réponse avec un message d'erreur
      res.status(500).send('This is the list of our students\nCannot load the database');
    }
  });
});

// Démarrage du serveur et écoute sur le port défini
app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});

// Exportation de l'application pour utilisation externe
module.exports = app;