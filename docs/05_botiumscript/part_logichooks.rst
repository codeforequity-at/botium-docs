.. _logichooks:

Using Logic Hooks
=================

Logic Hooks are used to inject advanced conversation logic into the conversation flow.

They can be put everywhere into the script, except bot section. There the order is the following:
* Botium Logic Hooks
* Requesting bot message
* Botium Asserters
* Asserting bot message
* Botium Asserters and Botium Logic Hooks

Like
  #bot
  PAUSE 100
  BUTTON Option1
  Hello! Please choose Option1 or Option2!
  SET_SCRIPTING_MEMORY secondbutton|Option2
  BUTTON $secondbutton

If you dont have a text to assert, but you have logichook to run after text asserting, use an empty row:
  #me
  Whats your name?
  #bot

  PAUSE 1000

As default the asserters/logichooks are executed in order they are defined. But some special technical logichooks are
forced to execute before, or after this order.
For example with WAITFORBOT is always executed in the beginning.

PAUSE
-----

* argument: pause time in milliseconds
* when used in a #me section, will pause before/after text is sent to bot depending on its position in script
* when used in a #bot section, will pause before/after reply is received from bot depending on its position in script

WAITFORBOT
----------

* argument: wait timeout in milliseconds
* used in a #bot section, will wait for a bot response for given amount of milliseconds (or forever if nothing is given). See also WAITFORBOTTIMEOUT capability.

INCLUDE
-------

* argument: name of a partial conversation
* will insert the referenced partial conversation in the current conversation

SET_SCRIPTING_MEMORY
--------------------

* arguments: name of the variable, new value
* Sets/overwrites a variable
* Can be used in #begin, #me, and #bot sections, and in botium.json as global.
* You should start the variable name usually without "$" (Use "$" if you want to use logic hook argument replacement)
  #me
  SET_SCRIPTING_MEMORY orderNum|111
  pls tell me the status for $orderNum

ASSIGN_SCRIPTING_MEMORY
-----------------------

* arguments: name of the variable, JSON-Path expression
* Sets/overwrites a variable from message content
* Can be used in #bot sections only after the bot message, and in botium,json as global.
* You should start the variable name usually without "$" (Use "$" if you want to use logic hook argument replacement)
* Use this logichook with care. If this logichook is before the bot message, then you will got an error while running your test.

Extract a variable from a card and use it in the next conversation step::

  validate value
  extract value from table and form further utterances based on that value

  #me
  get invoice details for customer number 435643

  #bot

  CARDS INVOICE NUMBER
  ASSIGN_SCRIPTING_MEMORY invoiceNumber|$.cards[0].content

  #me
  get invoice due date for invoice number $invoiceNumber

  #bot
  invoice due date for invoice number $invoiceNumber is 02/12/2020

CLEAR_SCRIPTING_MEMORY
----------------------

* arguments: name of the variable
* Deletes a variable.
* Can be used in #begin, #me, and #bot sections, but not in botium,json as global. (Global clear has no sense. There is nothing to clear there)
* You should start the variable name usually without "$" (Use "$" if you want to use logic hook argument replacement)

.. _logichooks-skip-bot-unconsumed:

SKIP_BOT_UNCONSUMED
-------------------

* no arguments
* will clear all currently unconsumed bot reply messages from the processing queue

UPDATE_CUSTOM
-------------

Add custom data to an outgoing message to trigger custom behaviour in the connector (consult documentation of the Botium Connector).

* arguments: custom action, custom field, custom value
* This logic hook is used for triggering custom actions in a connector. You have to consult the connector documentation for the supported custom actions.
* When used in the #begin section, the custom action is called for all convo steps

Using UPDATE_CUSTOM globally
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To attach custom data to each and every outgoing message, you can make the UPDATE_CUSTOM logic hook act globally::

  {
    "botium": {
      "Capabilities": {
        ...
        "LOGIC_HOOKS": [
          {
            "ref": "UPDATE_CUSTOM",
            "src": "UpdateCustomLogicHook",
            "global": true,
            "args": {
              "name": "SET_DIALOGFLOW_QUERYPARAMS",
              "arg": "payload",
              "value": { "key":"value" }
            }
          }
        ]
      }
    }
  }

