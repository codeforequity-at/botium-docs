Quickstart
**********

If you cannot wait to start, get a quick glimpse of Botium by starting your command line of choice and start typing (**Node.js installation is required**).

... with Mocha
==============

The following commands will install Botium Bindings, extend your Mocha specs with the Botium test case runner and run a sample Botium test::

  npm init -y
  npm install --save-dev mocha botium-bindings
  npx botium-bindings init mocha
  npm install && npm run mocha

**What’s happening here**:

* A fresh Node.js project is created with mocha and botium-bindings
* The *package.json* file is extended with a "botium"-Section and some devDependencies
* A *botium.json* file is created in the root directory of your project
* A *botium.spec.js* file is created in the *spec* folder to dynamically create test cases out of your Botium scripts
* A sample convo file is created in the *spec/convo* folder
* A first test run is started

... with Botium CLI
===================

::

  npm install -g botium-cli
  botium-cli init
  botium-cli run

**What’s happening here**:

* The first command installs the Botium CLI on your workstation
* The second command initializes a Botium project in the current directory (a *botium.json* file and a *convo file*)
* Finally, the Botium project runs and the test report is shown


