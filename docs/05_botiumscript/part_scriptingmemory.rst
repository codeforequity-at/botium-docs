.. _scripting-memory:

Using the Scripting Memory
==========================

Convos, and utterances are the static. You can't send with them a random number to the bot. Assert that the bot answers the current year, or uses your name if you told it before. But you can do it with scripting memory.

You can think of Scripting Memory as collection of system functions like current year, and variables like your name.

*The scripting memory is enabled by setting the :ref:`SCRIPTING_ENABLE_MEMORY capability <cap-scripting-enable-memory>`.*

.. _scripting-memory-variables:

Scripting Memory Variables
--------------------------

Within a single Botium conversation, it is possible to push some information items to a memory and reuse it later. For example:

* an eCommerce chatbot tells some kind of "order number" ("Your order number is X-1235123")
* BotiumScript asks the bot later for the order status ("pls tell me the status for X-1235123")

For a conversation step originating from the chatbot, use $varname as a placeholder. The scripting memory is filled from this part of the chatbot output text::

  #bot
  Your order number is $orderNum

For a conversation step originating from the user, again use $varname as a placeholder. The scripting memory will be used to complete the text sent to the chatbot.::

  #me
  pls tell me the status for $orderNum

There are some restrictions when choosing a variable name:

* They are all starting with a $, followed by a character (lowercase or uppercase)
* Followed by an arbitrary number of lowercase/uppercase characters and numbers

Using variables
~~~~~~~~~~~~~~~

They have two functions, depending on the usage. Lets say you already set a variable $username to Joe. Then you can send my name is Joe to bot in the #me section::

  #me
  my name is $username

Or you can use it to assert the response of the bot in #bot section. Did bot answered your name is Joe?::

  #bot
  your name is $username

As you see variables are starting with '$' to distinguish them from normal text.

Set variables
~~~~~~~~~~~~~

But how gets scripting memory data? You have to chose depending on your use case. Most basic case if you set them in convo::

  #me
  what is your name?

  #bot
  my name is $botname.

  #me
  Hello $botname!

You can use this way if the variable is coming from the bot. 

It is not always obious how long is the variable. For example botium will extract &@#? as password from sentence my password is &@#? but there is a :ref:`capability <cap-scripting-memory-matching-mode>` to tune this behavior.

Other case is, when you want to multiply your conversations.

Set the variable from file::

        |$toEat           |$toDrink |$costs
  Case1 |Two salami pizza |Two cola |30
  Case2 |Cheeseburger     |nothing  |8

And use it from convo::

  #bot
  Do you want to eat something?

  #me
  yes, $toEat please!

  #bot
  And some drink?

  #me
  $toDrink

  #bot
  It's $costs dollar.

This way we defined two conversations.

Third way is to use logic hooks.::

  #begin
  SET_SCRIPTING_MEMORY name|joe

  #bot
  what is your name?

  #me
  $name

  #bot
  hello $name!

As you see this conversation is still static. But can help you to create better managable conversations. 

And if you want to clear a variable, you can use CLEAR_SCRIPTING_MEMORY logichook.

.. _scripting-memory-functions:

Scripting Memory Functions
--------------------------

They are the pretty functions provided by botium, like current year (*$year*), or uniqid (*$uniqid*). Can be send to bot in #me sections, and can be used as asserters in #bot sections same way as variables.

Some of them can even used with parameters - for example *$number(5)* generates 5 digit long random number.

You can assert the response of the bot with functions::

  #me
  What is the current year?

  #bot
  $year

Or you can send them to bot::

  #me
  Current year is $year.

You can use parameters::

  #me
  Please call me $random(5).

You can use system environment variables::

  #me
  Please authenticate my token $env(MY_PERSONAL_TOKEN)

And can execute javascript code with func::

  #me
  What costs 5 beer?

  #bot
  They costs $func(5*2) dollar

List of Functions
~~~~~~~~~~~~~~~~~

* $func(<some javascript code>): Executes JavaScript code. It can has multiple lines. The result of the last row will be injected.
* $env(MY_ENV_VAR): Reads sytem environment variables
* $cap(MY_CAP): Reads Botium capabilities
* $msg(JSONPATH): Reads something from the current Botium message with a JSONPath expression, for example: $msg($.messageText)
* $projectname: Test Project Name
* $testsessionname: Test Session Name
* $testcasename: Test Case Name (Convo Name)
* $date(<date pattern like hh:mm:ss or YYYY-MM-DD>): Pattern specific. You can use this to display date, and/or time.
* $now: date and time. Local specific.
* $now_ISO: date and time in ISO format. Example: "2019-04-13T19:27:31.882Z"
* $now_EN: Example: "4/13/2019, 7:24:48 PM"
* $now_DE: Example: "03.07.2019, 08:33:06”
* $date: Locale specific.
* $date_EN: Example: "4/13/2019"
* $date_DE: Example: "03.07.2019”
* $date_ISO: Example: "2019-4-13”
* $time: Local specific.
* $time_EN: Example: "7:44:11 PM"
* $time_DE: Example: "08:33:06"
* $time_ISO: Example: "19:45:12"
* $time_HH_MM: Example: "19:45" or “01:01“
* $time_HH: Example: "19" or “01“
* $time_H_A: Example: "7 PM"
* $timestamp: 13 digit long timestamp (in ms) like 1557386297267
* $day_of_month: day of month. Example: "26" if the date is 2019-3-26
* $day_of_week: day of week. Local specific. Example: "Monday"
* $month: current month. Local specific. Example: "March"
* $month_MM: current month. Local specific. Example: "03"
* $year: Example: "2019"
* $random10: 10 digit long random number. Example: "6084037818"
* $random(<length>): <length> digit long random number.
* $uniqid:  V1. Example: "2e65c580-4fb4-11e9-b543-bf076857f1d1"

.. _scripting-memory-files:

Scripting Memory Files
----------------------

You can reuse the same convo more times with Scripting Memory. You have to enable this feature, depending on what Botium Flavour you are using:

* In Botium CLI, use the --expandscriptingmemory flag
* In Botium Bindings, add the expandScriptingMemoryToConvos setting to package.json
* In Botium Box, enable it in the Advanced Scripting Settings

If you don’t enable it explicitly, the scripting variables won’t get pre-filled from the scripting memory file.

Example 1, 4 convos expanded, dynamic variations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Scripting memory for product::

          |$productName
  product1|Bread
  product2|Beer

Scripting memory for order number::

              |$orderNumber
  orderNumber1|1
  orderNumber2|100

Convo::

  #me
  Hi Bot, i want to order $orderNumber $productName

Example 2, 3 convos expanded, scripted variations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Scripting memory for order::

          |$productName|$orderNumber
  order1  |Bread       |1
  order1  |Beer        |1
  order2  |Beer        |100

Convo::

  #me
  Hi Bot, i want to order $orderNumber $productName
