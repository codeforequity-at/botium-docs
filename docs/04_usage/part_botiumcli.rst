.. _botium-cli:

Botium CLI Documentation
========================

**Botium CLI** is the command line tool to access Botium Core functionality (and more).

Installation
------------

Botium CLI is available as Node.js module and as Docker image.

**Installing as global Node.js module**::

  npm install -g botium-cli botium-core

**Installing into an existing NPM project (package.json exists)**::

  npm install --save-dev botium-cli

**Using the Botium CLI docker image**

Instead of installing the NPM package, you can use the Botium CLI docker image instead::

  docker run --rm -v $(pwd):/app/workdir botium/botium-cli

Special considerations:

* You cannot use absolute pathes, but all pathes should be given relative to the current working directory. The current working directory is mapped to the docker container with the *-v* switch (above this is mapped to the current working directory)
* For running the console emulator, you will have to add the *-it* flag to the docker command to enable terminal interactions

::

  docker run --rm -v \$(pwd):/app/workdir -it botium/botium-cli emulator console

Docker Usage under Windows
~~~~~~~~~~~~~~~~~~~~~~~~~~

When using the above command under Windows, especially with *git bash*, you may receive an error like this::

  C:\Program Files\Docker\Docker\Resources\bin\docker.exe: Error response from daemon: Mount denied:
  The source path "C:/dev/xxxxx;C"
  doesn't exist and is not known to Docker.

In this case you have to disable the bash path conversion::

  export MSYS_NO_PATHCONV=1

Usage
-----

Prepare and run a simple Botium test case::

  botium-cli init
  botium-cli run

Get help on the command line options::

  botium-cli help

Get help on an invididual command::

  botium-cli run help

Botium Capabilities configuration
---------------------------------

The chatbot capabilities are described in a configuration file. By default, the file named "botium.json" in the current directory is used, but it can be specified with the "--config" command line parameter.
The configuration file holds capabilities, envs and sources. Configuration via environment variables is supported as well.

::

  {
    "botium": {
      "Capabilities": {
        "PROJECTNAME": "botium-sample1",
        ....
      },
      "Sources: {
        ....
      },
      "Envs": {
        "NODE_TLS_REJECT_UNAUTHORIZED": 0,
        ....
      }
    }
  }

Commands
--------

botium-cli init
~~~~~~~~~~~~~~~

Prepare a directory for Botium usage:

* Adds a simple botium.json
* Adds a sample convo file

botium-cli init-dev [connector|asserter|logichook]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Setup a boilerplate development project for Botium connectors, asserters or logic hooks in the current directory:
* Adds a Javascript source file with the skeleton code
* Adds a botium.json with connector/asserter/logic hook registration
* Adds a sample convo file

botium-cli run
~~~~~~~~~~~~~~

Automatically run all your scripted conversations against your chatbot and output a test report

botium-cli hello
~~~~~~~~~~~~~~~~

Runs a connectivity check against your chatbot by sending a message (by default 'hello') 
and waiting for an answer from bot.

botium-cli nlpanalytics <algorithm>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Runs NLP analytics with the selected algorithm.

* **validate** - run one-shot training and testing of NLP engine
* **k-fold** - run k-fold training and testing of NLP engine

See `this article <https://chatbotslife.com/tutorial-benchmark-your-chatbot-on-watson-dialogflow-wit-ai-and-more-92885b4fbd48>`_ for further information.

botium-cli nlpextract
~~~~~~~~~~~~~~~~~~~~~

Extract utterances from selected Botium connector and write to Botium Utterances files. Supported not by all connectors, please check connector documentation. Supported at least by:

* Dialogflow
* IBM Watson
* Amazon Lex
* Wit.ai
* NLP.js

and more to come.

botium-cli \*import
~~~~~~~~~~~~~~~~~~~

Import conversation scripts or utterances from some source (for example, from IBM Watson workspace)

botium-cli inbound-proxy
~~~~~~~~~~~~~~~~~~~~~~~~

Launch an HTTP/JSON endpoint for inbound messages, forwarding them to Redis to make them consumable by Botium Core.

See :ref:`here <simplerest-inbound>` how to use.


botium-cli emulator
~~~~~~~~~~~~~~~~~~~

The Botium Console Emulator is a basic command line interface to your chatbot running within Botium. You can record and save your conversation files.::

  botium-cli emulator console

botium-cli crawler-run / botium-cli crawler-feedbacks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Botium Crawler is command line interface to generate conversations along buttons.

The simplest way you can use it from the same folder where you a `botium.json` file placed. 
In this case the crawler is going to start with `hello` and `help` entry points, 
and by default try to make the all possible conversation 5 depth along buttons. 
By default the result is stored in the `./crawler-result` folder::

  botium-cli crawler-run

The Botium Crawler is able to ask user for feedbacks in case of there are no buttons in the bot answer, 
so the conversation is stucked before the depth is reached. 
By default the user feedbacks are stored in `./crawler-result/userFeedback.json` file, 
and these feedbacks are reused in the next runs. 
With the following command you can edit (`add`, `remove`, `overwrite`) your stored feedbacks::

  botium-cli crawler-feedbacks
 
There are many other configuration parameters. For more information see :ref:`Botium Crawler <botium-crawler>`.
