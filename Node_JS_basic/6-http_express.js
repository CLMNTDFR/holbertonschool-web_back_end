// Importer le module Express
const express = require('express');

// Créer une application Express
const app = express();

// Définir une route pour l'endpoint /
app.get('/', (req, res) => {
  res.send('Hello Holberton School!'); // Envoyer la réponse
});

// Faire écouter l'application sur le port 1245
const PORT = 1245;
app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});

// Exporter l'application
module.exports = app;