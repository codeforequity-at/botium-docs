.. _botium-bindings:

Botium Bindings
===============

Installation
------------

Botium Bindings is available as Node.js module::

  npm install botium-cli

Usage
-----

You should already have a Node.js project set up with the test runner of your choice (Mocha, Jasmine, Jest supported out of the box). For mocha, you can do it like this::

  cd my-project-dir
  npm init -y
  npm install --save-dev mocha

The following commands will install Botium Bindings, extend your Mocha specs with the Botium test case runner and run a sample Botium test::

  cd my-project-dir
  npm install --save-dev botium-bindings
  npx botium-bindings init mocha
  npm install && npm run mocha

Here is what's happening:

* Your package.json file is extended with a "botium"-Section and some devDependencies
* A botium.json file is created in the root directory of your project
* A botium.spec.js file is created in the "spec" folder to dynamically create test cases out of your Botium scripts
* A sample convo file is created in the "spec/convo" folder

Place your own Botium scripts in the "spec/convo" folder and Mocha will find them on the next run.

Botium Capabilities configuration
---------------------------------

The Botium Capabilities are read from *botium.json*, see :ref:`Botium Capabilities <botium-caps>`.


Botium Bindings configuration
-----------------------------

Configuration settings for Botium Bindings are read from the *botium* section of the *package.json* file. A typical package.json looks like this::

  {
    "name": "custom",
    "version": "1.0.0",
    "scripts": {
      "test": "mocha spec"
    },
    "devDependencies": {
      "botium-bindings": "latest",
      "botium-connector-echo": "latest",
      "mocha": "latest"
    },
    "botium": {
      "convodirs": [
        "spec/convo"
      ],
      "expandConvos": true,
      "expandUtterancesToConvos": false
    }
  }

convodirs
~~~~~~~~~

The folders to look for the :ref:`BotiumScript <botium-scripting>` test cases.

expandConvos
~~~~~~~~~~~~

If you are using BotiumScript with utterances files, enable this to expand the convo files with all possible user examples.

expandUtterancesToConvos
~~~~~~~~~~~~~~~~~~~~~~~~

If you are using BotiumScript with utterance files only, enable this to expand all user examples to simple question/response test cases.

expandScriptingMemoryToConvos
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you are using BotiumScript with :ref:`Scripting Memory Files <scripting-memory-files>`, enable this to expand the scripting memory.

See `this repl.it <https://repl.it/@FlorianTreml/replit-botium-bindings-arun-1>`_ as an example.

Test Runner Configuration
-------------------------

Configuration the test runners (Mocha, Jasmine or Jest) are done in the package.json command line calls to the test runner CLI. For example, to choose another Mocha reporter than the default one, change it in package.json::

  {
    ...
    "scripts": {
      "test": "mocha --reporter json spec"
    },
    ...
  }

Test Runner Timeouts
--------------------

Botium tests can take a rather long time, whereas test runners like Mocha and Jasmine expect the tests to complete within a short period of time. It is possible to extend this period of default 60000ms (60 seconds) by setting the environment variables *BOTIUM_MOCHA_TIMEOUT* / *BOTIUM_JASMINE_TIMEOUT* (milliseconds).
