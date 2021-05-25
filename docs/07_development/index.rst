Community
*********

Botium Champions
================

Botium champion is the award we set up to give out as our appreciation to those who are making an impact on our projects.

Community is the heart of Botium and our champions are driving the community! We would like to express our gratitude to those nerds by giving out some shiny stuffs and the privilege of being our champion!
 
There are several ways of contribution.
 
* Are you a restless developer? You can support us by writing code and catching bugs
* Do you have a big network? Share your Botium use cases and experience with your mates
* Are you an expert? Answer community questions on stackoverflow or github (+links)
* Do you have tester genes? Help us by pointing out flaws or suggesting new features
* Are you a researcher? Support us with the scientific proof of coolness

.. _contribution-guide:

Contribution Guide
==================

We love Open Source software. Open Source software helped us in our professional careers for the last 20 years, and we are giving back to the community.

All Botium Core code (Botium Core, Botium Bindings, Botium CLI) and most connectors are `hosted on Github <https://github.com/codeforequity-at>` and open for contributions.

Prerequisites
-------------

* Good knowledge of Node.js and Javascript
* Knowledge on Git and Github
* In case you have some troubles, please __ALWAYS__ attach the debug output from Botium
* Please don't post any secret information (like access keys for Dialogflow or IBM Watson)

Guidelines for code contributions
---------------------------------

Of course, code contributions are welcome! There are many possible ways of extending Botium.

Contributions to Botium Core
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Please fork the repository
* Please create an issue and refer to it in the pull request
* Add unit tests for implemented behaviour
* The NPM script "npm run build" has to succeed before posting a pull request
    * it will run unit tests
    * it will enforce eslint and rollup build
* Someone from the core team will review and give feedback within 1-2 days

Contribute Botium Connectors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* There is a Developer Guide available below
* Tell us about your work! We are happy to include your connector in Botium Core and thank you in our release notes!

Contribute Botium Asserters
~~~~~~~~~~~~~~~~~~~~~~~~~~~

* There is a Developer Guide available below
* Tell us about your work! We are happy to include your asserter in Botium Core and thank you in our release notes!

**We want to recognise everyone making positive influence in our community. We are doing our part of the job by tracking every possible Botium champion out there, but if you feel like that we are missing someone, let us know!**


First Steps - Botium Core
-------------------------

Botium Core is the core library for Botium. Some core connectors and BotiumScript is implemented in Botium Core. 

Clone and Run Tests
~~~~~~~~~~~~~~~~~~~

Here are the commands to clone the Botium Core repository, install the dependencies, running the build and running the test suite::

  git clone https://github.com/codeforequity-at/botium-core.git
  cd botium-core
  npm install
  npm run build
  npm test

Pull Requests
~~~~~~~~~~~~~

As usual on Github, you can fork the repository and create a Pull Request with your changes. One of the core developers will get in contact. 

We expect that any code changes are covered by unit tests.

Make sure that the commands npm run build and npm test are working with your changes, otherwise the Pull Request will be declined for sure!

Important Files
~~~~~~~~~~~~~~~

**src/BotDriver.js** - the main entry file

Reads the botium.json and other configuration sources

Initializes scripting and containers

**src/Capabilities.js** - capability names

Holds the list of supported capability names

**src/Defaults.js** - default capability values

Holds the list of default capability values

**src/scripting/ScriptingProvider.js** - entry point for BotiumScript

Initializes BotiumScript runtime

Holds context for scripting runtime

Reads BotiumScript files

**src/scripting/Compiler\*.js** - BotiumScript parsers

Parsing the supported BotiumScript file formats

**src/scripting/logichooks/asserters/\*Asserter.js** - integrated asserters

Media asserter, NLP asserters, …

**src/scripting/logichooks/logichooks/\*LogicHook.js** - integrated logic hooks

Pause, Wait, …

**src/scripting/logichooks/userinputs/\*Input.js** - integrated user input methods

Buttons, Forms, …


.. _develop-connector:

Developing Botium Connectors
============================

Howto develop your own Botium Connector - see `Botium Wiki <https://wiki.botiumbox.com/developer-section/howto-develop-your-own-botium-connector/>`__

Howto develop your own HTTP/JSON Botium Connector - see `Botium Wiki <https://wiki.botiumbox.com/developer-section/howto-develop-your-own-http-json-botium-connector/>`__

Howto deploy my own Botium Connector - see `Botium Wiki <https://wiki.botiumbox.com/developer-section/howto-deploy-my-own-botium-connector/>`__

.. _develop-asserter:

Developing Custom Asserters
===========================

Developing Custom Asserters - see `Botium Wiki <https://wiki.botiumbox.com/developer-section/developing-custom-asserters/>`__

.. _develop-logichook:

Developing Botium Logic Hooks
=============================

Developing Custom Logic Hooks - see `Botium Wiki <https://wiki.botiumbox.com/developer-section/developing-custom-logic-hooks/>`__

.. include:: part_customhooks.rst
.. include:: part_precompilers.rst