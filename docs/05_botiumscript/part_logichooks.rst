.. _logichooks:

Using Logic Hooks
=================

Logic Hooks are used to inject advanced conversation logic into the conversation flow. They can be added at any position inside the convo file.

PAUSE 
-----

* argument: pause time in milliseconds
* used in a #me section, will pause after text is sent to bot.

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
* Can be used in #begin, #me, and #bot sections, and in botium,json as global.
* You should start the variable name usually without "$" (Use "$" if you want to use logic hook argument replacement)
* It is executed in the end of the section.

So this wont work as expected::

  #me
  SET_SCRIPTING_MEMORY orderNum|111
  pls tell me the status for $orderNum

But you can do it this way::

  #begin
  SET_SCRIPTING_MEMORY orderNum|111

  #me
  pls tell me the status for $orderNum

ASSIGN_SCRIPTING_MEMORY
-----------------------

* arguments: name of the variable, JSON-Path expression
* Sets/overwrites a variable from message content
* Can be used in #bot sections only, and in botium,json as global.
* You should start the variable name usually without "$" (Use "$" if you want to use logic hook argument replacement)
* It is executed in the end of the section.

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
* It is executed in the end of the section as SET_SCRIPTING_MEMORY.

UPDATE_CUSTOM
-------------

* arguments: custom action, custom field, custom value
* This logic hook is used for triggering custom actions in a connector. You have to consult the connector documentation for the supported custom actions. 
* When used in the #begin section, the custom action is called for all convo steps

