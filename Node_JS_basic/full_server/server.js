const express = require('express');
const routes = require('./routes/index');

const app = express();
const port = 1245;

// Récupérer le chemin du fichier de la base de données passé en argument
const database = process.argv[2];
app.set('database', database);

app.use(routes);

app.listen(port, () => {
  console.log(`Server running on port ${port}`);
});

module.exports = app;