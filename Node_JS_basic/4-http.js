const http = require('http');

// Créer le serveur et définir la réponse pour toutes les requêtes
const app = http.createServer((req, res) => {
  res.statusCode = 200; // Définir le code de statut à 200 (OK)
  res.setHeader('Content-Type', 'text/plain'); // Définir le type de contenu comme 'text/plain'
  res.end('Hello Holberton School!'); // Envoyer la réponse
});

// Le serveur écoute sur le port 1245
app.listen(1245, () => {
  console.log('Server is running on port 1245');
});

// Exporter le serveur pour qu'il puisse être utilisé ailleurs
module.exports = app;