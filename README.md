# ES6 Exercises Project

## Table of Contents
1. [Introduction](#introduction)
2. [Learning Objectives](#learning-objectives)
3. [Requirements](#requirements)
4. [Setup and Installation](#setup-and-installation)
5. [Configuration Files](#configuration-files)
6. [Usage](#usage)
7. [Testing](#testing)
8. [Contributing](#contributing)
9. [License](#license)

## Introduction

This project is designed to help you understand and practice the new features introduced in ECMAScript 2015 (ES6). ES6 brought significant improvements to JavaScript, making the language more powerful and easier to use.

## Learning Objectives

By the end of this project, you should be able to:

- Explain what ES6 is and its significance.
- Identify and use new features introduced in ES6.
- Understand the difference between constants and variables.
- Work with block-scoped variables.
- Utilize arrow functions and their default parameters.
- Handle rest and spread parameters in functions.
- Use string templating in ES6.
- Create and manipulate objects and their properties in ES6.
- Understand and use iterators and for-of loops.

## Requirements

- All files will be executed on Ubuntu 18.04 LTS using NodeJS 12.11.x.
- Editors allowed: vi, vim, emacs, Visual Studio Code.
- All files should end with a new line.
- A `README.md` file at the root of the project folder is mandatory.
- Code should use the `.js` extension.
- Code will be tested using the Jest Testing Framework.
- Code will be analyzed using ESLint with specific rules provided.
- All functions must be exported.

## Setup and Installation

### Installing NodeJS 20.x.x

1. Download the NodeSource setup script:
   ```bash
   curl -sL https://deb.nodesource.com/setup_20.x -o nodesource_setup.sh

1. Run the setup script:

```
sudo bash nodesource_setup.sh
```
2. Install NodeJS:

```
sudo apt install nodejs -y
```
3. Verify the installation:

```
nodejs -v
```
# Expected output: v20.15.1
npm -v
# Expected output: 10.7.0
Installing Jest, Babel, and ESLint<br>
Navigate to your project directory.

4. Install Jest:

```
npm install --save-dev jest
```
5. Install Babel:

```
npm install --save-dev babel-jest @babel/core @babel/preset-env
```

6. Install ESLint:

```
npm install --save-dev eslint
```
Configuration Files:
`package.json`
`json`

Copy code:
```
{
  "scripts": {
    "test": "jest"
  },
  "devDependencies": {
    "babel-jest": "^27.0.1",
    "@babel/core": "^7.14.6",
    "@babel/preset-env": "^7.14.7",
    "eslint": "^7.29.0",
    "jest": "^27.0.1"
  }
}
```
babel.config.js
```
module.exports = {
  presets: [
    [
      '@babel/preset-env',
      {
        targets: {
          node: 'current',
        },
      },
    ],
  ],
};
```
.eslintrc.js:
```
module.exports = {
  env: {
    browser: false,
    es6: true,
    jest: true,
  },
  extends: [
    'eslint:recommended',
    'plugin:jest/recommended',
  ],
  parserOptions: {
    ecmaVersion: 2018,
    sourceType: 'module',
  },
  plugins: ['jest'],
  rules: {},
};
```
## Usage
To use this project, clone the repository and navigate to the project directory.<br>
Run npm install to install all necessary dependencies.<br>You can then start writing your ES6 code in the provided files.

## Testing
To run tests, use the following command:

```
npm test
```
This will execute all tests using the Jest framework.