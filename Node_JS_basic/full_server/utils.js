const fs = require('fs').promises;

async function readDatabase(filePath) {
  try {
    const data = await fs.readFile(filePath, 'utf-8');
    const lines = data.trim().split('\n').slice(1); // Ignorer la première ligne
    const result = {};

    for (const line of lines) {
      const [firstName, , , field] = line.split(','); // Extraire les valeurs des colonnes
      if (!result[field]) {
        result[field] = [];
      }
      result[field].push(firstName);
    }

    return result;
  } catch (error) {
    throw new Error(error.message);
  }
}

module.exports = { readDatabase };