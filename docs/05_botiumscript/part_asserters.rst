.. _asserters:

Using Asserters
===============

Asserter are additional validators for conversations. For Example if you want to check if the links send by the bot are valid references you can use and asserter called HyperLinkAsserter, which is trying to reach the sent links. 

Buttons Asserter
----------------

Some Chatbots are responding not only with text, but provide simple interaction elements such as buttons, to trigger special or predefined functionality. Botium can assert the existance of such buttons in the chatbot response.

It is possible to use this asserter without parameter. In this case asserter will fail if there are no buttons at all.

*Processing button responses depends on the Botium connector to support it. For example, it is supported by the Directline and the Dialogflow connector. Please check the connector documentation.*

Example
~~~~~~~

Imagine a chatbot taking orders for pizza delivery. It has a well-defined inventory of possible pizza sizes and toppings. The user interface should present those options to the user as simple buttons::

  #me
  please send me two salami pizza

  #bot
  Please select the size of the pizza
  BUTTONS Kids|Normal|Family

The BUTTONS asserter (arguments: button texts to look out for), used in #bot section, will assert that buttons with text are present in response.

Media Asserter
--------------

Some Chatbots are responding not only with text, but with pictures, videos or other media content. Botium can assert the existance of media attachments in the chatbot response.

It is possible to use this asserter without parameter. In this case asserter will fail if there is no media at all.

*Processing media responses depends on the Botium connector to support it. For example, it is supported by the Directline and the Dialogflow connector. Please check the connector documentation.*

Example
~~~~~~~

Imagine a chatbot taking orders for pizza delivery. It has a well-defined inventory of possible pizza sizes and toppings. The user interface should visualize the different sizes by using pictures::

  #me
  please send me two salami pizza

  #bot
  Please select the size of the pizza
  MEDIA kids_pizza.png|normal_pizza.png|family_pizza.png

The MEDIA asserter (arguments: media uri to look out for), used in #bot section, will assert that media files are attached in the response.

Forms Asserter
--------------

Some Chatbots are responding with form. You can assert the fields of the form using this asserter.

It is possible to use this asserter without parameter. In this case asserter will fail if there are no forms at all.

*Processing forms depends on the Botium connector to support it. For example, it is supported by the Directline connector. Please check the connector documentation.*

Example
~~~~~~~

Imagine a chatbot taking orders for pizza delivery using form. Form has two fields, type to set pizza type, and a count field for its count. You can check those fields::

  #me
  i want to order a pizza

  #bot
  FORMS type|count

It means that you excpect two fields, “type”, and “count”, and no more. 

Fields have a name, or an ID, and most of them a label before. If you expect ‘type’, and there is a field with label ‘Type of the pizza’ then asserter will accept it, even if its name is not 'type'.

JSONPath Asserter
-----------------

This is a generic asserter to assert existance or the value of JSONPath expressions within the underlying chatbot response data. The structure of the data depends on the nature of the connector used - for example, with IBM Watson, the underlying response data is the API response from the Watson HTTP/JSON API.

You can use this asserter for adding your custom assertion logic to BotiumScript.

Example
~~~~~~~

Imagine an eCommerce chatbot - the response contains the shopping cart in session variables. The following BotiumScript asserts that the cart is available in the session, and the ordered item is in the cart::

  #me
  add to cart 5 bananas

  #bot
  JSON_PATH $.session.cart
  JSON_PATH $.session.cart.item[0].count | 5
  JSON_PATH $.session.cart.item[0].name | banana

The JSON_PATH asserter takes one or two arguments:

* First argument is the JSONPath expression to query
* If a second argument is given, the value is compared to the outcome of the JSONPath expression (if the expression results in multiple values, then it is compared to all of them). If not given, then only the existance of the element is asserted.

This asserter always works on the sourceData field of the botMsg, not on the botMsg as a whole.

Extending JSONPath Asserter
---------------------------

JSONPath Asserter can optionally be configured with global args in botium.json. Arguments from convo file are handed over and used as specified.

- **argCount** - Number of arguments to expect in the convo file
- **path** - predefined JSONPath expression
- **pathTemplate** - Mustache template for predefined JSONPath expression (based on args)
- **assertTemplate** - Mustache template for assertion value (based on args)

Example 1 - WATSONV1_HAS_CONTEXT
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

  {
    "botium": {
      "Capabilities": {
        ...
        "ASSERTERS": [
          {
            "ref": "WATSONV1_HAS_CONTEXT",
            "src": "JsonPathAsserter",
            "args": {
              "argCount": 1,
              "pathTemplate": "$.context['{{args.0}}']"
            }
          }
        ]
      }
    }
  }

Usage::

  #bot
  WATSONV1_HAS_CONTEXT my-context-variable

Example 1 - WATSONV1_CONTEXT
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

  {
    "botium": {
      "Capabilities": {
        ...
        "ASSERTERS": [
          {
            "ref": "WATSONV1_CONTEXT",
            "src": "JsonPathAsserter",
            "args": {
              "argCount": 2,
              "pathTemplate": "$.context['{{args.0}}']",
              "assertTemplate": "{{args.1}}"
            }
          }
        ]
      }
    }
  }

Usage::

  #bot
  WATSONV1_CONTEXT my-context-variable|expected-value

Response Length Asserter
------------------------

This asserter checks the length of the response, and the count of the responses (if there are multiple delivered at once). Typically, a chatbot shouldn’t deliver too much information at once.

Example
~~~~~~~

Imagine a user asking a chatbot for help::

  #me
  please help

  #bot
  RESPONSE_LENGTH 200|5

This asserter takes one or two arguments:

* First argument is maximum length of the bot response
* Second argument is the maximum count of the bot responses - some bots deliver multiple responses at once.

NLP Asserter (Intents, Entities, Confidence)
--------------------------------------------

Natural language enabled chatbots are using some kind of NLP engine in the background to recognize intents and entities for the user input.

This information is not shown to the user directly. It may make sense to assert for the recognized intents and entities instead of the text response of the chatbot - or you can even use it in parallel (assert text and intent confidence for example).

Some NLP engines are pure stateless NLP engines without conversation flow (Like Microsoft Luis). They just returning this NLP information. For this engines you cant assert the responded message (text, buttons, etc), just this NLP information using NLP Asserters.

It is possible to extract statistics with the help of this asserters, comparing expectation with the responses from the NLP engine. You can do it on your own, or you can use the our Botium Coach to do it. (Botium Coach is not published yet. It wont be a standalone tool, will work just in the top of the Botium Box)

*Not all Botium connectors support these asserters. It depends if the use chatbot technology exposes this information to Botium. For example, it is supported by the Dialogflow and IBM Watson connectors. Please check the connector documentation.*

* **INTENT** (arguments: intent name to look out for), used in #bot section, will assert that bot answered with the specified intent.
* **INTENT_CONFIDENCE** (arguments: minimal accepted confidence, like "70" for 70%), used in #bot section, will assert that bot answered with at least the specified minimal confidence.
* **INTENT_UNIQUE** (no arguments), used in #bot section, will assert that the recognized intent is unique (not alternate intent with same confidence identified). 
* **ENTITIES** (arguments: expected entities like "from|to", or minimal entities like "from|..." ), used in #bot section, will assert that bot answered with the specified entities.
* **ENTITY_VALUES** (arguments: expected entity values like "2018|2019", or minimal entity values like "2018|..." ), used in #bot section, will assert that bot answered with the specified entity values.
* **ENTITY_CONTENT** (arguments: entity and expected values like location|Budapest|Vienna)

  * One ENTITY_CONTENT asserter checks only one entity. Use more asserters to check more.
  * Does not fail if the response has more values as specified in arguments.

The INTENT_CONFIDENCE asserter can be used as global asserter to make sure the recognized confidence is always higher than a defined threshold.

Example
~~~~~~~

Imagine a chatbot taking orders for pizza delivery. It has a well-defined inventory of possible pizza sizes and toppings. The recognized intent, entities and the confidence should be asserter::

  #me
  please send me two salami pizza

  #bot
  INTENT I_ORDER_PIZZA
  INTENT_CONFIDENCE 70
  ENTITIES E_PIZZA_TYPE|E_FOOD
  ENTITY_VALUES salami|pizza
  Please select the size of the pizza
 
Using ENTITY_VALUES asserter can be confusing sometimes. This assertation will be valid::

  #me
  I want to travel from Berlin to Vienna.

  #bot
  Im happy to hear it. And where are you now?
  INTENT travel

  #me
  in Münich.

  #bot
  So you are in Münich, and want to travel from Berlin to Vienna? 
  You will travel to Berlin on your own?
  INTENT travel
  ENTITY_VALUES Berlin|Vienna|Münich

But maybe it is not what you want. You can be more specific using ENTITY_CONTENT asserter::

  ...
  ENTITY_CONTENT FROM|Berlin
  ENTITY_CONTENT TO|Vienna
  ENTITY_CONTENT LOCATION|Münich

(This example works just on Dialogflow, it aggregates entities)

Using the Intent Confidence Asserter globally
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A very common use case is to use the Intent Confidence Asserter as global asserter, to make sure to filter out the weakly resolved intents. To make all conversation steps fail where the intent falls below a confidence of 80, add this section to your botium.json::

  {
    "botium": {
      "Capabilities": {
        ...
        "ASSERTERS": [
          {
            "ref": "INTENT_CONFIDENCE",
            "src": "IntentConfidenceAsserter",
            "global": true,
            "args": {
              "expectedMinimum": 80
            }
          }
        ]
      }
    }
  }

Text Asserters
--------------

You can set globally how to assert response using :ref:`SCRIPTING_MATCHING_MODE capability <cap-scripting-matching-mode>`. You can extend/override this behavior using Text Asserters for each response.

Asserter names
~~~~~~~~~~~~~~

There are more text asserters

* Asserter names are starting with TEXT

  * TEXT…

* The matching mode can be wildcard, regexp, include, and exact match 

  * TEXT_WILDCARD…, 
  * TEXT_REGEXP…, 
  * TEXT_CONTAINS…, 
  * TEXT_EQUALS… or simple TEXT…

* You can decide to use more args. With AND (…_ALL…) or OR (…_ANY…). 

  * Exact match supports just OR, this postfix ist not allowed there
  * Example names: 

    * TEXT…, (ALL or ANY is not allowed)
    * TEXT_CONTAINS_ALL…
    * TEXT_REGEXP_ANY…

* Each asserter can work case insensitive (optional _IC prefix) 

  * Example names:

    * TEXT_IC, 
    * TEXT_CONTAINS_ALL_IC

Features
~~~~~~~~

Utterances as argument::

  convos:
    - name: example
      steps:
        - me:
            - Hello!
        - bot:
            - "!TEXT_IC GOODBYE|bye bye"
  utterances:
    GREETING:
      - Goodbye
      - Bye

This is conversation is in yaml format, because utterances. It will fail if bot says goodbye (bye bye, goodbye, or bye) for greeting. Check is case insensitive, but exact. Wont fail for byebye, or for bye Joe .

Starting ! is used to denote the YAML, so negation is quoted.

TEXT_IC is an alternative of TEXT_EQUALS_IC

Matching modes
~~~~~~~~~~~~~~

Exact match works on the text part of the response. All other asserters on the whole response object (on response json as string).

**Matching using joker**

You can expect any text::

  TEXT

or no text at all::

  !TEXT

using exact match asserter.

Examples
~~~~~~~~

::

  TEXT_WILDCARD_ALL id2_*3|1*4

will not accept “Im Joe, my number is 12345, and my ID is id1_123”, because noting found for regexp id2_*3 

::

  TEXT_REGEXP_ALL id1_\d\d\d|[0-9]+ 

will accept “Im Joe, my number is 12345, and my ID is id1_123”, because booth regexps are found 

::

  TEXT_CONTAINS_ANY Joe|Jane|George

will accept “Im Joe, my number is 12345, and my ID is id1_123”, because Joe is there

::

  convos:
    - name: example
      steps:
        - me:
            - Hello!
        - bot:
            - "!TEXT_IC GOODBYE|bye bye"
  utterances:
    GREETING:
      - Goodbye
      - Bye

This is conversation is in yaml format, because utterances. It will fail if bot says goodbye (bye bye, goodbye, or bye) for greeting. Check is case insensitive, but exact. Wont fail for byebye, or for bye Joe .

Starting ! is used to denote the YAML, so negation is quoted.

TEXT_IC is an alternative of TEXT_EQUALS_IC

Cards Asserter
--------------

Some Chatbots are responding not only with text, but with grouped UI elements. If the grouping is not just visual, but has some extra function like paging, or hiding, then it called Card. Botium can assert the existence of such Cards in the chatbot response.

It is possible to use this asserter without parameter. In this case asserter will fail if there are no cards at all.

*Processing card responses depends on the Botium connector to support it. For example, it is supported by the Directline and the Dialogflow connector.*

Example
~~~~~~~

Imagine a chatbot taking food orders. In the response there are cards for paging with titles Soup, Pizza, and Dessert. You can assert them::

  #me
  What can i order pls?

  #bot
  Please choose something from our Menu Card!
  CARDS Soup|Pizza|Dessert

Negation
---------

It is possible to negate asserters. If you dont expect Button1 and Button2 in response::

  #bot
  !BUTTONS Button1|Button2

Some asserters are working without args (see asserter documentation)::

  #bot
  BUTTONS

Which means, it must be at least one button. It is possible to negate those assertions::

  #bot
  !BUTTONS

It will throw error if bot responds with any button.

Register Asserter as Global Asserter
------------------------------------

A Global Asserter is called at every convo step. This doesn’t make sense for all asserters, but there are some where this makes sense. To use one of the integrated asserters as global asserter, you have to register it as global asserter in botium.json::

  "ASSERTERS": [
    {
      "ref": "RESPONSE_LENGTH",
      "src": "ResponseLengthAsserter",
      "global": true,
      "args": {
          "globalArg1": 17
      }
    }
  ]
