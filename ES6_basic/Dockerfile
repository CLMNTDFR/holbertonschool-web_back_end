# Utiliser l'image de base Ubuntu 18.04
FROM ubuntu:18.04

# Mettre à jour les dépôts et installer les dépendances
RUN apt-get update && apt-get install -y \
  curl \
  vim \
  git \
  build-essential \
  && curl -sL https://deb.nodesource.com/setup_12.x | bash - \
  && apt-get install -y nodejs

# Vérifier les versions installées de Node.js et npm
RUN node -v
RUN npm -v

# Définir le répertoire de travail dans le conteneur
WORKDIR /usr/src/app

# Copier le fichier package.json et package-lock.json dans le répertoire de travail
COPY package*.json ./

# Installer les dépendances du projet
RUN npm install

# Installer Jest, Babel, et ESLint
RUN npm install --save-dev jest babel-jest @babel/core @babel/preset-env eslint

# Copier tout le contenu du projet dans le répertoire de travail
COPY . .

# Exposer le port 8080 (si nécessaire pour votre application)
EXPOSE 8080

# Commande par défaut pour exécuter l'application
CMD ["npm", "run", "dev"]