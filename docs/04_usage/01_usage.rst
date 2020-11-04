Botium Usage
************

Writing Chatbot Tests
=====================

Anatomy of a Botium Project
---------------------------




Utterance Expansion
-------------------






Automating Chatbot Tests
========================


Botium CLI vs Botium Bindings
-----------------------------



Using Botium CLI
----------------




Using Botium Bindings
---------------------

expand-convos etc





Configuration with Capabilities
===============================

This section describes how to configure Botium. **Capabilities** are similar to the "DesiredCapabilities" as used in Selenium and Appium: they describe in what context a Chatbot runs (or should run) and how Botium can connect to it.

Configuration Source
--------------------

Botium reads configuration from several configuration sources:

-  *botium.json* in the current directory
-  In case *NODE_ENV* environment variable is set *botium.<node-env>.json* in the current directory
-  *botium.local.json* in the current directory - can be used to extract sensitive information out of the botium.json file and should be added to .gitignore
-  In case *NODE_ENV* environment variable is set *botium.<node-env>.local.json* in the current directory
-  In case the environment variable "BOTIUM_CONFIG" points to a file, same files read as above (botium.json, botium.<node-env>.json, botium.local.json, botium.<node-env>.local.json)
-  Environment variables "BOTIUM_capability name" are read and considered

Every step overwrites the configuration capabilities from the previous step.

*When using Botium in continuous build / testing / deployment environment, it is generally advised to not include passwords or other secrets in the configuration files, but handing it over with environment variables*

The configuration files are JSON files with this anatomy:::

  {
    "botium": {
      "Capabilities": {
        "PROJECTNAME": "My Botium Project",
        "CONTAINERMODE": "echo",
        "SOME_OTHER_CAPABILITIY": "..."
      }
    }
  }

CONTAINERMODE
-------------

This is one of the most important settings, as it defines the Botium Connector to use. Botium will try to load the connector by several means, in this order:

-  If it refers to a relative filename of a custom connector (see `Howto develop your own Botium Connector <https://botium.atlassian.net/wiki/spaces/BOTIUM/pages/38502401/Howto+develop+your+own+Botium+Connector>`_) in the current working directory, this file is loaded and used as connector
-  Botium tries to load an NPM module with this name
-  Botium tries to load an NPM module named with a “botium-connector-” prefix

A list of well-known Botium Connectors is available here: `Botium Connectors <https://botium.atlassian.net/wiki/spaces/BOTIUM/pages/360553/Botium+Connectors>`__

**Examples:**::

  "CONTAINERMODE": "src/myconnector.js"

  "CONTAINERMODE": "echo"

  "CONTAINERMODE": "botium-connector-echo"

Generic Capabilities
--------------------

Those capabilities apply to all Chatbot types for all Botium Connectors.

PROJECTNAME
~~~~~~~~~~~

*Default: "defaultproject"*

The name of the chatbot project. This will be shown in logfiles and
reports.

TEMPDIR
~~~~~~~

*Default: "botiumwork"*

The working directory for Botium (relative or absolute). For each
session there will be a separate unique working directory created in
this directory. It will be created if it doesn't exist.

CLEANUPTEMPDIR
~~~~~~~~~~~~~~

*Default: "true"*

Botium will remove the unique working directory after each session,
including all created logfiles and docker containers. In case Botium or
a Chatbot doesn't work as expected, this value should be changed to
"false" to keep the logfiles, making it able to investigate.

WAITFORBOTTIMEOUT
~~~~~~~~~~~~~~~~~

*Default: "10000" (10 seconds)*

When waiting for a Chatbot response, this is the default timeout (in
milliseconds). An error will be thrown if Chatbot doesn't answer in
time. This can be overruled when using the Botium API (in case long
waiting period is expected).

SIMULATE_WRITING_SPEED
~~~~~~~~~~~~~~~~~~~~~~

*Default: "false"*

Simulates human typing speed. Falsy, or ms/keystroke. (Average typing
speed is about 290 ms/keystroke)

SECURITY_ALLOW_UNSAFE
~~~~~~~~~~~~~~~~~~~~~

*Default: "true"*

If turned off then some features which may damage the run environment,
are deactivated.

So is not possible

-  to execute own JavaScript code

-  change environment variable

Specific Capabilities
---------------------

Capabilities which are specific to a Botium Connector are documented :ref:`for each Botium Connector separately <botium-connectors>`.

Scripting Capabilities
----------------------

These capabilities are for fine-tuning the :ref:`Botium Scripting behaviour <botium-scripting>`.

SCRIPTING_MATCHING_MODE
~~~~~~~~~~~~~~~~~~~~~~~

*Default: "wildcardIgnoreCase”*

Logic to use for comparing the bot response to the utterances:

-  **wildcard** to use the asterisk \* as wildcard (case sensitive)
-  **wildcardIgnoreCase** to use the asterisk \* as wildcard (case insensitive)
-  **regexp** to use `regular expressions <https://developer.mozilla.org/de/docs/Web/JavaScript/Reference/Global_Objects/RegExp>`_ (case sensitive)
-  **regexpIgnoreCase** to use `regular expressions <https://developer.mozilla.org/de/docs/Web/JavaScript/Reference/Global_Objects/RegExp>`_  (case insensitive)
-  **include** to do a substring matching (case sensitive)
-  **includeIgnoreCase** (or includeLowerCase - legacy value) to do a substring matching (case insensitive)

SCRIPTING_ENABLE_MEMORY
~~~~~~~~~~~~~~~~~~~~~~~

*Default: false*

Enable the :ref:`scripting memory <scripting-memory>`.

SCRIPTING_NORMALIZE_TEXT
~~~~~~~~~~~~~~~~~~~~~~~~

*Default: true*

All texts can be "normalized" (cleaned by HTML tags, multiple spaces, line breaks etc)

SCRIPTING_ENABLE_MULTIPLE_ASSERT_ERRORS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Default for Botium Core: false*
*Default for Botium Box: true*

Collect all asserter errors for a conversation step and return all with
one test failure (instead of failing on first failure)

SCRIPTING_TXT_EOL
~~~~~~~~~~~~~~~~~

*Default: \\n*

Line ending character for text files.

SCRIPTING_UTTEXPANSION_MODE
~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Default: all*

Logic to use for utterances expansion:

-  *all*: using all utterances (number of scripts grows exponential)
-  *first*: only take first utterance
-  *random*: select random utterances (count: see below)

SCRIPTING_UTTEXPANSION_RANDOM_COUNT
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Default: 1*

Number of utterances to select by random

SCRIPTING_UTTEXPANSION_INCOMPREHENSION
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Default: empty*

When expanding utterances, Botium can be instructed to add an
INCOMPREHENSION asserter to make sure the chatbot answers with something
meaningful. One of the utterances is noted as INCOMPREHENSION.

For example, the INCOMPREHENSION utterance looks like this:::

  INCOMPREHENSION
  sorry i don't understand
  i didn't get that
  can you please repeat

Expanded convos will look like this:

test case 1

#me

sending some text

#bot

!INCOMPREHENSION

SCRIPTING_UTTEXPANSION_USENAMEASINTENT
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Default: false*

In many data collections, the utterance name is the same as the intent
the NLU engine should predict. For these cases, this flag can be used to
add an `INTENT
asserter <https://botium.atlassian.net/wiki/spaces/BOTIUM/pages/17334319>`__
when expanding the utterances to convos.

For example, an utterance looks like this:

MY_INTENT_NAME

user example 1

user example 2

user example 3

Expanded convos will look like this:

MY_INTENT_NAME.L

#me

MY_INTENT_NAME

#bot

INTENT MY_INTENT_NAME

SCRIPTING_MEMORYEXPANSION_KEEP_ORIG
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Default: "false"*

Used while reading scripting memory from file. If it is set to true then
the original convo will be kept

SCRIPTING_MEMORY_MATCHING_MODE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Determines how the variables are extracted from text.

*Default: "non_whitespace"*

*non_whitespace*: captures every non whitespace characters:

====================== ================== ============
**botsays**            **capturing text** **captured**
====================== ================== ============
Your name is Joe.      Your name is $name Joe.
Your name is John Doe. Your name is $name John
Today is 02/15/2019    Today is $today    02/15/2019
====================== ================== ============

*word*: only take captures word characters:

====================== ================== ============
**botsays**            **capturing text** **captured**
====================== ================== ============
Your name is Joe.      Your name is $name Joe
Your name is John Doe. Your name is $name John
Today is 02/15/2019    Today is $today    02
====================== ================== ============

*joker*: capture everything (result is not trimmed!)

====================== ================== ============
**botsays**            **capturing text** **captured**
====================== ================== ============
Your name is Joe.      Your name is $name Joe.
Your name is John Doe. Your name is $name John Doe.
Today is 02/15/2019    Today is $today    02/15/2019
====================== ================== ============

Excel Parsing Capabilities
--------------------------

See `Composing in Excel
files <file:///C:/wiki/spaces/BOTIUM/pages/48922649/Composing+in+Excel+files>`__

CSV Parsing Capabilities
------------------------

See `Composing in CSV
files <file:///C:/wiki/spaces/BOTIUM/pages/48463903/Composing+in+CSV+files>`__

Rate Limiting
-------------

Some cloud-based APIs are subject to rate limiting and only allow a
fixed number of requests in a defined time period. Botium Core can limit
the number of requests sent to the Botium connector.

When running in Botium Box on multiple agents in parallel, these
settings are applied to each agent separately.

See `Bottleneck project page <https://github.com/SGrondin/bottleneck>`__
for details.

RATELIMIT_USERSAYS_MINTIME
~~~~~~~~~~~~~~~~~~~~~~~~~~

The minimum number of milliseconds between two UserSays calls.

Example: use 333 to limit rate to at most 3 calls per second.

RATELIMIT_USERSAYS_MAXCONCURRENT
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The maximum number of concurrent calls.

Configuring Generic Retry Behaviour
-----------------------------------

Botium can be configured to retry test cases on certain error
conditions. This is an optional behaviour, but it can help you to avoid
flaky tests. Some examples where it makes sense:

-  Connection to the chatbot engine is somehow unstable, leading to
      failing test cases, where not the chatbot engine itself is the
      source of the problem, but the infrastructure

-  Maybe chatbot engine itself occasionally fails on high load, but only
      in test environment. Using the retry mechanism it can be avoided
      to fail in these cases.

The following capabilities are available for various connector
operations:

-  BUILD

-  START

-  USERSAYS

-  STOP

-  CLEAN

-  ASSERTER

-  LOGICHOOK

-  USERINPUT

RETRY_<operation>_ONERROR_REGEXP
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Default: nothing*

Configure a regular expression or a list of regular expressions (JSON
array) to trigger the retry behaviour. Often, a simple substring
matching is enough.

RETRY_<operation>_NUMRETRIES
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Default: 1*

Number of retries in case a retry-able error has been identified

RETRY_<operation>_FACTOR
~~~~~~~~~~~~~~~~~~~~~~~~

*Default: 1*

If more than one retry, you can decide to increase wait times between
retries by applying a factor higher than 1 for calculating the time to
wait for the next retry

RETRY_<operation>_MINTIMEOUT
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Default: 1000 (1 sec)*

Given in milliseconds. The minimum timeout to wait for the next retry.


.. _botium-scripting:

Writing Test Cases with BotiumScript
====================================


.. _scripting-memory:

Using the Scripting Memory
==========================


