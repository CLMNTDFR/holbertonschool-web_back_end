Étape 1 : Installer Docker

Si Docker n'est pas déjà installé sur votre machine, vous pouvez l'installer en suivant les instructions ci-dessous.

Pour Ubuntu :

bash

sudo apt-get update sudo apt-get install -y apt-transport-https ca-certificates curl software-properties-common curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add - sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" sudo apt-get update sudo apt-get install -y docker-ce

Vérifiez que Docker est bien installé :

bash

docker --version
Docker version 20.10.x, build xxxxx

Étape 2 : Créer un Dockerfile

Créez un fichier nommé Dockerfile dans le répertoire racine de votre projet avec le contenu suivant :

dockerfile
Utiliser l'image de base Ubuntu 18.04

FROM ubuntu:18.04
Mettre à jour les dépôts et installer les dépendances

RUN apt-get update && apt-get install -y
curl
vim
git
build-essential
Installer Node.js 12.11.x

RUN curl -sL https://deb.nodesource.com/setup_12.x | bash - &&
apt-get install -y nodejs
Vérifier les versions installées

RUN node -v RUN npm -v
Définir le répertoire de travail dans le conteneur

WORKDIR /usr/src/app
Copier le fichier package.json et package-lock.json dans le répertoire de travail

COPY package*.json ./
Installer les dépendances du projet

RUN npm install
Copier tout le contenu du projet dans le répertoire de travail

COPY . .
Exposer le port 8080

EXPOSE 8080
Commande par défaut pour exécuter l'application

CMD ["npm", "run", "dev"]

Étape 3 : Créer les fichiers de configuration du projet

Créez les fichiers suivants dans le répertoire racine de votre projet : package.json

json

{ "scripts": { "lint": "./node_modules/.bin/eslint", "check-lint": "lint [0-9].js", "dev": "npx babel-node", "test": "jest", "full-test": "./node_modules/.bin/eslint [0-9].js && jest" }, "devDependencies": { "@babel/core": "^7.6.0", "@babel/node": "^7.8.0", "@babel/preset-env": "^7.6.0", "eslint": "^6.4.0", "eslint-config-airbnb-base": "^14.0.0", "eslint-plugin-import": "^2.18.2", "eslint-plugin-jest": "^22.17.0", "jest": "^24.9.0" } }

babel.config.js

javascript

module.exports = { presets: [ [ '@babel/preset-env', { targets: { node: 'current', }, }, ], ], };

.eslintrc.js

javascript

module.exports = { env: { browser: false, es6: true, jest: true, }, extends: [ 'airbnb-base', 'plugin:jest/all', ], globals: { Atomics: 'readonly', SharedArrayBuffer: 'readonly', }, parserOptions: { ecmaVersion: 2018, sourceType: 'module', }, plugins: ['jest'], rules: { 'no-console': 'off', 'no-shadow': 'off', 'no-restricted-syntax': [ 'error', 'LabeledStatement', 'WithStatement', ], }, overrides:[ { files: ['*.js'], excludedFiles: 'babel.config.js', } ] };

Étape 4 : Construire l'image Docker

Dans le terminal, naviguez vers le répertoire de votre projet où se trouve le Dockerfile et exécutez la commande suivante pour construire l'image Docker :

bash

docker build -t mon_projet_es6 .

Étape 5 : Créer et exécuter un conteneur à partir de l'image

Après avoir construit l'image, créez et exécutez un conteneur :

bash

docker run -it --rm -p 8080:8080 -v $(pwd):/usr/src/app mon_projet_es6

Cette commande va :

Exécuter le conteneur en mode interactif (-it).
Supprimer le conteneur lorsque vous quittez (--rm).
Mapper le port 8080 de votre machine hôte au port 8080 du conteneur (-p 8080:8080).
Monter le répertoire de votre projet sur votre machine hôte dans le répertoire de travail du conteneur (-v $(pwd):/usr/src/app).

Vérification finale

Vous devriez maintenant avoir un environnement Docker configuré avec NodeJS 12.11.x et les dépendances nécessaires pour exécuter et tester votre projet. Vous pouvez vérifier cela en exécutant vos scripts NPM à l'intérieur du conteneur.

dans le terminal du contenaire si non installé npm install -g jest eslint

Exécuter le test dans le conteneur Docker

Assurez-vous que les fichiers 3-default-parameter.js et 3-main.js sont présents dans votre répertoire de travail.

Démarrez le conteneur interactif Docker :

bash

docker run -it --rm -v $(pwd):/usr/src/app mon_projet_es6 /bin/bash

Dans le conteneur, exécutez la commande suivante pour tester les modifications :

bash

npm run dev 3-main.js

Exemple de session dans le conteneur

Voici comment la session devrait se dérouler dans le conteneur :

bash

root@ab95a025bc48:/usr/src/app# npm run dev 3-main.js

    mon_projet_es6@1.0.0 dev /usr/src/app npx babel-node 3-main.js

142 56 41