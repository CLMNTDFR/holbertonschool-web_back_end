// Affiche un message de bienvenue et demande le nom de l'utilisateur
process.stdout.write('Welcome to Holberton School, what is your name?\n');

// Écoute l'événement 'readable' sur stdin (entrée standard)
process.stdin.on('readable', () => {
  // Lit l'entrée de l'utilisateur
  const input = process.stdin.read();

  // Si l'entrée n'est pas nulle, affiche le nom de l'utilisateur
  if (input !== null) process.stdout.write(`Your name is: ${input}`);
});

// Écoute l'événement 'end' sur stdin (entrée standard)
process.stdin.on('end', () => {
  // Affiche un message de fermeture
  process.stdout.write('This important software is now closing\n');
});