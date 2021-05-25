.. _botium-crawler:

Botium Crawler
==============

The **Botium Crawler** is doing the work of detecting the conversation flows supported by your chatbot by itself. It does so by analyzing the **quick responses** offered by your chatbot and **simulating clicks on all of the options** in parallel, following all pathes down **until it reaches the end of the conversation**.

All detected conversation flows along all pathes are saved as Botium test cases and utterance lists and can be used as base for a **regression test set**.

Installation
------------

Install as CLI tool
~~~~~~~~~~~~~~~~~~~

Install :ref:`Botium CLI <botium-cli>` (botium crawler is included)::

  npm install -g botium-cli

Or you can install directly Botium Crawler::

  npm install -g botium-crawler

Install as Node.js module
~~~~~~~~~~~~~~~~~~~~~~~~~

You can install botium crawler as library in your own project::

  npm install botium-crawler

Using as CLI tool with Botium CLI
---------------------------------

Botium CLI using Botium Crawler is able crawl your chatbot various way according to the parameters,
and it is able to generate and store all possible conversations.

Basically there are two command in Botium CLI to use Botium Crawler `crawler-run` and `crawler-feedbacks`.

crawler-run command
-------------------

Get help on the available parameters::

  botium-cli crawler-run --help

The parameters can be applied in two different ways:

* One is the classic way to add these as command line parameters after the `crawler-run` command.
* The other way is to store these parameters into `botium-crawler.json` file into the root of you working directory and reuse them for the next run. In this case the parameters are read from the `botium-crawler.json` as default.

*You are able to generate `botium-crawler.json` file with `--storeParams` flag.* 

**--config**

You can set the path of a json configuration file (e.g.: `botium.json`)::

  botium-cli crawler-run --config ./custom-path/botium.json

**--output**

You can set the output folder of the crawler result. By default the path is `./crawler-result`. A `scripts` folder is going to be created under the output path, and the generated convos and utterances are going to be stored here::

  botium-cli crawler-run --config ./botium.json --output ../custom-output

**--entryPoints**

In the entry points array you can define one or more 'user message' from where the crawler is going to start the conversations. 
* By default the crawler is going to start with `['hello', 'help']` entry points, if the chatbot has no auto welcome message(s). 
* If the chatbot has auto welcome messages, than these welcome messages are going to be taken as entry points, if the user do not specify others in this parameter. (see `--numberOfWelcomeMessages` parameter)

::

  botium-cli crawler-run --config ./botium.json --entryPoints 'Good Morning' 'Next conversation'
    
**--numberOfWelcomeMessages**

You have to specify the number of auto welcome messages exactly, because the crawler has to wait for these welcome messages
before each conversation. By default this is 0. 
If the bot has auto welcome messages, each generated conversation will start with the auto welcome messages.::

  botium-cli crawler-run --config ./botium.json --numberOfWelcomeMessages 2
  
**--depth**

You can specify the depth of the crawling, by default it is 5.::

  botium-cli crawler-run --config ./botium.json --depth 3
  
**--ignoreSteps**

You can specify here the array of messages has to be ignore during the crawling process.::

  botium-cli crawler-run --config ./botium.json --ignoreSteps 'this message is ignored'
    
**--incomprehension**

You can specify here the array of messages, which has to be considered during incomprehension validation.
The result of the validation is going to be stored in `error.log` file in the `output` folder.::
    
  botium-cli crawler-run --config ./botium.json --incomprehension 'Unkown command'

**--mergeUtterances**

Setting this flag `true` the same bot answers are going to be merged in one utterance file.
By default the flag is `true` to avoid high number of utterance files.::

  botium-cli crawler-run --config ./botium.json --mergeUtterances false

**--recycleUserFeedback**

When the crawler stuck at a point in the conversation, before `depth` is reached, then the crawler is able to ask the user for answers. 
If this flag is true, then these feedbacks are going to be stored in `userFeedback.json` file in the `output` folder, and these answers are automatically used during the next run of the crawler.
By default the flag is `true`.::

  botium-cli crawler-run --config ./botium.json --recycleUserFeedback false

**--waitForPrompt**

Milliseconds to wait for the bot to present the prompt ore response. Useful if the bot sends multiple responses at once.::

  botium-cli crawler-run --waitForPrompt 1000

**--storeParams**

If you would like to generate/overwrite the `./botium-crawler.json` file with you currect parameters, you can turn this flag on. This way the parameter are going to be read from this file for the next run.  
By default the flag is `false`.::

  botium-cli crawler-run --config ./botium.json --storeParams true
    
Content of ./botium-crawler.json::

  {
    "recycleUserFeedback": true,
    "output": "./crawler-result",
    "incomprehension": [],
    "config": "./botium.json",
    "entryPoints": [],
    "numberOfWelcomeMessages": 0,
    "depth": 5,
    "ignoreSteps": [],
    "mergeUtterances": true,
    "waitForPrompt": 100
  }
    
Example of crawler-run usage
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In this example the botium echo connector will be used, which basically just echoing back what you say. 
The `botium.json` configuration file looks like this::

  {
    "botium": {
      "Capabilities": {
        "SCRIPTING_MATCHING_MODE": "wildcardIgnoreCase",
        "CONTAINERMODE": "echo"
      },
      "Envs": {}
    }
  }

Keeping it simple I set just 'hi' as entry points. The commandline will look like this::

  $ botium-cli crawler-run --config ./botium.json --entryPoints 'hi'
  Crawler started...

  ---------------------------------------

      hi

  #me
  hi

  #bot
  You said: hi

      
  ---------------------------------------

  This path is stucked before reaching depth. 
  Would you like to continue with your own answers?  [yes, no, no all]: yes
  Enter your 1. answer: I said hi   
  Do you want to add additional answers? [y/n]: n

  ---------------------------------------

      hi_I said hi

  #me
  hi

  #bot
  You said: hi

  #me
  I said hi

  #bot
  You said: I said hi

      
  ---------------------------------------

  This path is stucked before reaching depth. 
  Would you like to continue with your own answers?  [yes, no, no all]: no
  Saving testcases...
  The 'crawler-result/scripts/1.1_HI_I-SAID-HI.convo.txt' file is persisted
  Crawler finished successfully

The `crawler-result` folder will look like this::

  crawler-result
      ├── scripts
      │   ├── 1.1_HI_I-SAID-HI.convo.txt
      │   ├── UTT_1.1_HI_I-SAID-HI_BOT_1.utterances.txt
      │   └── UTT_1.1_HI_I-SAID-HI_BOT_2.utterances.txt
      └── userFeedback.json

In the next run nothing is asked from the user, 
because the previous feedbacks are stored in `userFeedback.json`. 
(Before next run the `crawler-result/scripts` folder has to be emptied.)
So now the commandline much simpler than at the previous run::

  $ botium-cli crawler-run --config ./botium.json --entryPoints 'hi'
  Crawler started...
  Saving testcases...
  The 'crawler-result/scripts/1.1_HI_I-SAID-HI.convo.txt' file is persisted
  Crawler finished successfully

* The convo file is going to be created, despite something goes wrong with any conversation, but it will be differentiated by a `FAILED` postfix in convo name and filename ( e.g.: `1.1_HI_I-SAID-HI_FAILED.convo.txt` ).*
 
crawler-feedback command
-------------------------

With crawler-feedback command you can edit (`add`, `remove`, `overwrite`) your stored feedbacks in `userFeedback.json`::

  botium-cli crawler-feedback --help

**--input**

You can specify the path of the json file, where the user feedbacks are stored.
By default it reads the `./crawler-result/userFeedback.json` if it exits.

**--output**

You can specify the output path, where the edited feedback has to be stored.
By default it is the same as input, so basically the input file is going to be overwritten.

Example of crawler-feedback usage
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In this example you have to edit in the previous example stored `userFeedback.json` file.
You will overwrite the previously set `I said hi` answer with `I said hello` and then skip the rest::

  $ botium-cli crawler-feedbacks

  ---------------------------------------
  hi

  #me
  hi

  #bot
  You said: hi

      
  ---------------------------------------

  User answers:
  1: I said hi


  What would you like to do with these answers? [add, remove, overwrite, skip, skip all]: overwrite
  Enter your 1. answer: I said hello
  Do you want to add additional answers? [y/n]: n

  ---------------------------------------
  hi_I said hi

  #me
  hi

  #bot
  You said: hi

  #me
  I said hi

  #bot
  You said: I said hi

      
  ---------------------------------------

  User answers:


  What would you like to do with these answers? [add, remove, overwrite, skip, skip all]: skip
  Edit finished, exiting... Do you want to save your modifications? [y/n]: y

Now if I run again the crawler from the previous *crawler-run* example, then the `crawler-result` folder will look like this::

  botium-cli crawler-run --config ./botium.json --entryPoints 'hi'

::

  crawler-result
      ├── scripts
      │   ├── 1.1_HI_I-SAID-HELLO.convo.txt
      │   ├── UTT_1.1_HI_I-SAID-HELLO_BOT_1.utterances.txt
      │   └── UTT_1.1_HI_I-SAID-HELLO_BOT_2.utterances.txt
      └── userFeedback.json

*You can use Botium Crawler as individual CLI tool pretty similar as with Botium CLI*

Using as library - API Docs
---------------------------

The Botium Crawler is publishing a `Crawler` and a `ConvoHandler`. See `Github Repository <https://github.com/codeforequity-at/botium-crawler/tree/master/samples/api>`_ for an example.

Crawler Object
~~~~~~~~~~~~~~

The `Crawler` need an initialized `BotiumDriver` from Botium Core or a `config` parameter, 
which is a json object with the corresponding `Capabilities`.
Two callback function can be passed as well. 
The first for ask user to give feedback for the stucked conversations.
The second for validating bot answers.
You can find example for these callback functions in the sample code as well.

The `Crawler` has a `crawl` function, with that the crawling process can be triggered. 
This function parameters are identical with the CLI parameters::

  crawl ({ entryPoints = [], numberOfWelcomeMessages = 0, depth = 5, ignoreSteps = [] })

ConvoHandler Object
~~~~~~~~~~~~~~~~~~~

The `ConvoHandler` can decompile the result of the `crawl` function with `decompileConvos` function.
The `decompileConvos` function result is an object with a `scriptObjects` array and a `generalUtterances` array property.
