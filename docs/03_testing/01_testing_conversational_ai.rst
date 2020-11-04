Testing Conversational AI
*************************

Parts of this guide have been published in the book `ACCELERATING SOFTWARE QUALITY - Machine Learning & Artificial Intelligence in the Age of DevOps <https://www.perfecto.io/resources/accelerating-devops-quality>`_ by `Eran Kinsbruner <https://www.linkedin.com/in/eran-kinsbruner-4b47a81/>`_.

Special Challenges when Testing Chatbots
========================================

The combination of machine learning, natural language processing an
adaptive programming is the opposite of well defined, deterministic
behaviour software testers are used to rely on, resulting in flaky
tests. Testing a chatbot has some fundamental differences to testing a
website or smartphone app, on a technical level, on a scope level and on
the test engineering level. Knowing the differences is vital when
sharpening your skills for testing a chatbot.

Technical difference: Input/Output Methods
------------------------------------------

Compared to most desktop, web and smartphone applications out there a
chatbot usually provides rudimentary options for user interactions - in
the case of a text-based chatbot, a single text input field with a text
output area, in the case of a voice-enabled chatbot a simple microphone
with a speaker.

|image1|

Depending on the channel the chatbot is operating on, often there are
some additional user interaction options available. Here are some
examples.

Quick Responses
~~~~~~~~~~~~~~~

Quick Responses enable the user to quickly select one of the most likely
user inputs. The options are typically rendered as buttons or bubbles.

Carousel
~~~~~~~~

For presenting multimedia content a carousel is the most common user
interface element. It allows the chatbot to show pictures, rich text and
buttons.

Microphone, Speaker and Display
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Voice-enabled devices (like Amazon Echo) can optionally be extended
display components (Echo Show) to present graphical content instead of
relying on voice commands only.

|image2|

.. _section-2:

Scope difference: Test Levels
-----------------------------

Due to the nature of conversational AI it is vital to understand the
concept of test levels to design efficient test strategies. This picture
shows a typical chatbot architecture:

|image3|

-  There is a user frontend hosted as chat widget on a website

-  The frontend connects to a backend service (often called
      Orchestration Service) with web-protocols — HTTP(S), JSON,
      Websockets

-  Somewhere behind, there is an NLP model to convert user input to
      structured data with intents and entities

-  An additional component is handling the dialogue sessions.

-  And finally, there are some kind of business services, often backed
      by business databases

*Note that in most cases the NLP engine and the Dialogue engine are
combined, for example with IBM Watson Assistant, or Dialogflow. For
Microsoft LUIS and Azure Bot Service, those components are separated
though.*

The architecture diagram above shows 6 integration points for test
cases. The remaining part of this chapter will go into details on the
challenges for each test level.

(1) User Interface Level / E2E Testing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Botium supports End-To-End-Testing with a `Webdriver
Connector <https://github.com/codeforequity-at/botium-connector-webdriverio>`__,
combining the power of Selenium's web browser automation with Botiums
chatbot testing superpowers. The chatbot is tested by doing pointing and
clicking and typing on a website just as a real user would do.

**Scenarios**

-  Validating browser/client compatibility

-  Smoke Tests before going live

**Pros**

-  Testing end user experience

-  Works for all kind of chatbots, independent of the backend technology
      (in theory)

**Cons**

-  Requires Selenium infrastructure setup which is not a piece of cake
      (or use a Selenium cloud provider)

-  Usually, Webdriver scripting is required (in Javascript)

-  Very slow compared to the other testing levels

(2) API Level / Orchestration Service Testing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Typically, the Orchestration Service is published as an HTTP/JSON or
Websocket endpoint. Most chatbot engine providers support such
endpoints, and Botium also includes a generic HTTP/JSON connector and a
generic Websocket connector adaptable to a wide range of endpoints.

**Scenarios**

-  Conversational Flow Testing is usually done on API level

-  Integration Testing

**Pros**

-  Testing on API level reduces flakiness and increases speed

-  Testing near end user experience

**Cons**

-  No standard API available, has to be adapted for every custom
      endpoint schema out there

(3) + (4): Backend Level / Dialogue and NLP Engine Testing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There are lots of dialogue engines out there, some of them even offer
free plans as SaaS or on-premise installation. In some cases, those
engines include an NLP engine. Examples for combined dialogue engines
are Google Dialogflow, IBM Watson Assistant and Microsoft Bot Framework.
Examples for specialized NLP engines are wit.ai and Microsoft LUIS.

**Scenarios**

-  Regression testing for intent/utterance resolution

-  NLP analytics

**Pros**

-  Supported out-of-the-box with well-documented APIs and SDKs

-  Allows very deep analysis of NLP data such as intents and entities

**Cons**

-  Depending on the implementation, far away from the end-user
      experience

(5) Business Logic Level / Business Service Testing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Usually there is some kind of business service involved, the core to
providing value with a chatbot. Botium includes an HTTP/JSON endpoint
asserter to make sure a test case actually had an impact on business
data. For example:

-  By using an eCommerce chatbot, Botium places a test order with the
      help of an order service in the backend

-  The order service persists the order in the business database

-  Botium asks the order service for details about the order to verify
      that the order has been persisted

(6) Business Data Level / Business Database Testing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is a special case for the Business Service Testing case above —
Botium includes asserters for most common business databases (Oracle,
PostgreSQL, Microsoft SQL Server, MySQL) to query for test case outcome.

Test engineering difference
---------------------------

There are well established software testing techniques and metrics, but
what makes testing chatbots different ? What’s the difference to testing
a website or smartphone app ? There are at least 4 major differences.

Learning cloud services
~~~~~~~~~~~~~~~~~~~~~~~

Most chatbots are built on top a learning cloud services, which by
definition keeps changing its behaviour. NLP-Services (Natural language
understanding and processing) like Dialogflow, Wit.ai or LUIS are
subject to constant training and improvement. Having a non-deterministic
component in the system under test will make software testing useless,
as soon as you cannot tell the reason for a failed test case — a defect
in the chatbot software or an improvement in the cloud service.

And even more important, the test itself can and will have an impact on
the cloud services as well: presenting a cloud service with the same
test cases over and over again will distort the cloud services
assumption of “real-life interactions”, giving the test cases higher
priority than they should have.

❌ Cloud service training has impact on software tests. Deal with this
dependency.

Non-linear input
~~~~~~~~~~~~~~~~

This only applies to chatbots operated with a voice interface. There are
7,5 billion humans out there, and there are 7,5 billion different voices
out there. For a website, it doesn’t matter who clicks a button — Elon
Musk himself or King Louie, the website doesn’t notice a difference. But
for a chatbot, it does matter what voice is in action.

✔️ Speech recognition technologies are evolving fast. Chatbot developers
can rely on industry leaders to provide acceptable solutions.

Non-deterministic user interactions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Dealing with non-determinism is a critical topic in software testing.
Due to the nature of human language it is impossible for software tests
to cover all possible situations.

❌ Give up the 100%-test-coverage goal. Make sure the tests cover the
most common situations.

No barriers for users
~~~~~~~~~~~~~~~~~~~~~

When using a chatbot, either with voice or with text interface, there
are no interaction barriers for users. Websites and smartphone apps
allow predefined means of interaction with common user interface
components (clickable hyperlinks, buttons, text entry boxes, …).
Chatbots have to cover all kind of unexpected user input in a decent
way.

✔️ Design test cases with robustness for unexpected user input in mind.

|image4|

.. _botium-basics:

Testing Conversational Flow
===========================

This section starts with some technical background on Botium and then
demonstrates a methodology to identify and formalize test cases for the
conversational flow of a chatbot. The conversational flow, often called
“user stories”, can be visualized in a flow chart.

|image5|

Hello, World! The Botium Basics
-------------------------------

The most basic test case in Botium consists of

-  submitting a phrase possibly entered by a real user to the chatbot

-  checking the response of the chatbot with the expected outcome

BotiumScript
~~~~~~~~~~~~

In Botium, the test cases are described by conversational flows the
chatbot is supposed to follow. For a sample “greeting” scenario, the
Botium test case looks like this — also known as “BotiumScript”:::

   #me
   hello bot!

   #bot
   Hello, meat bag! How can I help you ?

You can write BotiumScript in several file formats

-  plain text file with Notepad or any other text editor

-  Excel file

-  CSV file (comma separated values)

-  JSON

-  YAML

Convos and Utterances
~~~~~~~~~~~~~~~~~~~~~

So, let’s elaborate the “Hello, World!”-example from above. While some
users will say “hello”, others maybe prefer “hi”:::

   #me
   hi bot!

   #bot
   Hello, meat bag! How can I help you ?

Another user may enter the conversation with “hey dude!”::

   #me
   hey dude

   #bot
   Hello, meat bag! How can I help you ?

And there are plenty of other phrases we can think of. For this most
simple use case, there are now at least three or more BotiumScripts to
write. So let’s rewrite it. We name this file hello.convo.txt:::

   TC01 - Greeting

   #me
   HELLO_UTT

   #bot
   Hello, meat bag! How can I help you ?

You may have noticed the additional lines at the beginning of the
BotiumScript. The first line contains a reference name for the test case
to make it easier for you to locate the failing conversation within your
test case library. And we add another file hello_utt.utterances.txt:::

   HELLO_UTT
   hello bot!
   hi bot!
   hey dude
   good evening
   hey are you here
   anyone at home ?

-  The first BotiumScript is a **convo file** — it holds the structure
      of the conversation you expect the chatbot to follow.

-  The second BotiumScript is an **utterances file** — it holds several
      phrases for greeting someone, and you expect your chatbot to be
      able to recognize every single one of them as a nice greeting from
      the user.

Botium will take care that the convo and utterances files are combined
to verify every response of your chatbot to every greeting phrase. So
now let’s assume that your chatbot uses several phrases for greeting the
user back. In the morning it is:::

   #me
   HELLO_UTT

   #bot
   Good morning, meat bag! How can I help you this early ?

And in the evening it is:::

   #me
   HELLO_UTT

   #bot
   Good evening, meat bag! How can I help you at this late hour ?

Let’s extract the bot responses to another utterances file:::

   BOT_GREETING_UTT
   Good evening
   Good morning
   Hello
   Hi

And now comes the magic, we change the convo file to:::

   #me
   HELLO_UTT

   #bot
   BOT_GREETING_UTT

Utterances files can be used to verify chatbot responses as well. To
summarize:

-  An utterance referenced in a #me-section means: Botium, send every
      single phrase to the chatbot and check the response

-  An utterance referenced in a #bot-section means: Botium, my chatbot
      may use any of these answers, all of them are fine

Identification of Test Cases
----------------------------

If the flow chart is available, identification of the test cases is
actually straightforward: Each path through the flow chart from top to
bottom is a test case. Here is the path for the user story “User
composes customized bouquet”.

|image6|

And here is the path for “User selects anniversary bouquet”.

|image7|

Scripting Test Cases for a conversational flow
----------------------------------------------

In BotiumScript, the conversational flow for user story “User composes
customized bouquet” can be expressed like this:::

   #me
   I want to buy a bouquet

   #bot
   OK, do you want to compose a bouquet yourself ?

   #me
   Yes

   #bot
   OK, what kind of flowers would you like to add first ?

   #me
   Please add 5 red roses

   #bot
   Alright, I put 5 red roses in your lovely bouquet. Should I add anything else ?

   #me
   No, thanks.

   #bot
   Super!

As soon as a chatbot doesn’t respond as expected, the test case is
considered as failed and reported.

Scripting Utterance Lists
-------------------------

What the flow charts don’t show are the endless possibilities for a user
to express an intent. For each node in the flow chart, there are various
input and output utterances to consider. The flow chart typically
pictures a “happy path” in the conversation, in a real-world scenario
the same conversation path and test case should be satisfied with most
usual utterances and utterance combinations.

|image8|

For the “I want to buy a bouquet”, there are plenty of other ways for a
user to express this intent:

-  “Give me some flowers”

-  “To the flower shop, please”

-  “purchase a bouquet”

-  …

All of these user examples are valid input for the same test case, and
in Botium these user examples are collected within an utterance list in
a text file:::

   UTT_USER_ORDER_FLOWERS
   I want to buy a bouquet
   Give me some flowers
   To the flower shop, please purchase a bouquet

What the flow charts don’t show as well are the utterances used on the
other side, by the chatbot itself: a well-designed chatbot provides some
variance in conversation responses.

For example instead of “Okay! Would you like to compose a bouquet
yourself” the chatbot might as well respond with:

-  “Do you want me to suggest a composition?”

-  “Is it for a special occasion” ?

-  …

These utterances can be collected in another utterance list and used in
the test cases to allow the chatbot all responses matching one in this
list. The first part of the user story “User composes customized
bouquet” would then look like this:::

   #me
   UTT_USER_ORDER_FLOWERS

   #bot
   UTT_BOT_COMPOSE_YN

The conversational flow remains the same, but there are many user
examples and chatbot responses allowed now.

Dealing with Uncertainty
------------------------

When using Botium, there are many options for asserting the chatbots
behaviour - the most simple one, assertion of the text response, is
shown above.

-  Asserting the presence of user interface elements, such as quick
      response buttons, media attachments, form input elements

-  Asserting with regular expressions and utterance lists

-  Asserting tone with a tone analyzer

   -  Validation that the chatbot tone matches the intended brand
         communication style

-  Asserting availability of hyperlinks presented to the user

-  Asserting custom message payload with JSONPath queries

-  Asserting business logic with API and data storage queries

Generating a Test Report
------------------------

There are several frontends available for generating a test report with
Botium.

Option 1: Botium CLI
~~~~~~~~~~~~~~~~~~~~

Run Botium CLI like this:::

  botium-cli run

Botium CLI will build up a communication channel with your chatbot and
run all of your test cases. Status information and a summary are
displayed in the command line window.

Option 2: Botium Bindings
~~~~~~~~~~~~~~~~~~~~~~~~~

With Botium Bindings an established test runner like Mocha, Jest or
Jasmine can be used for running Botium test cases.::

  mocha ./spec

Option 3: Botium Box
~~~~~~~~~~~~~~~~~~~~

Use the Quickstart Wizard to connect your chatbot to your test sets and
run them.

|image9|

Testing an NLP model
====================

Natural Language Processing (NLP) is mainly a text classification and
extraction problem. Given user input as text, the purpose of the NLP
model is to

1. detect the most likely user intent from a pre-trained library of user
      intents

2. extract entities such as dates and numbers for refining the detected
      user intent

|image10|

Note that this concept also applies to voice applications by putting a
speech-to-text-engine in front of the NLP component.

A test engineer now should already have spotted the obvious way for
testing an NLP model - provide the input text and assert on the NLP
outcome. This is correct but not the full truth - there are two more
important aspects often overlooked, and that is conversation context and
separation of training and test data.

Conversational Context
----------------------

In human conversations, context is everything. A conversation is not
only a simple series of statements, but between those statements some
knowledge is exchanged, and the meaning of a statement can vary
depending on the exchanged knowledge.

Take the statement “thirtytwo” - without any context, this is merely a
number. Take the same statement - “thirtytwo” - as a response to the
question “What’s the temperature outside ?”, and now the meaning is not
merely a random number but a precise temperature. And, on a side note,
depending on the season it is also possible to deduct if it’s Celsius or
Fahrenheit.

|image11|

It’s a common pitfall to not taking conversational context into
consideration when testing an NLP model.

Separation of Training data and Test data
-----------------------------------------

Training data is the labeled data used for training the NLP engine. It
typically consists of a large list of user examples for each intent or
entity type the NLP engine should be able to handle. The NLP engine will
learn the correct classification and extraction parameters from those
user examples and the

Test data is the unlabeled data used for testing the NLP engine after it
has been trained with the training data.

Using the same data for training a conversational AI as well as for
testing purposes has some flaws — most important, there is no challenge
for an artificial intelligence to correctly classify something it
already knows. It is a challenge for an artificial intelligence to
classify something it hasn’t seen before, though. Take care to always
have separate set of test data not used for training. For cases where
this is not possible there is a method called Cross-Validation - see
later in this chapter.

*This principle applies to most machine learning algorithms, not only to
text classification.*

Scripting Test Cases for an NLP model
-------------------------------------

Manual testing has its place, even in the age of artificial
intelligence. But as this book is about test automation this section
shows the building blocks for automated testing (and improving) an NLP
model.

NLP model Training and Testing Cycle
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A typical workflow for training and testing an NLP model is like this:

1. Run all test cases

   a. Set conversation context

   b. Send text or speech input to NLP model

   c. Evaluate the predicted intent and entities

2. Collect and analyze the results

   d. Use common quality metrics like precision, recall and F1 (see next
         section)

   e. Exit if quality KPIs are met, otherwise continue

3. Adapt NLP model to deliver better quality metrics

   f. Provide additional training data for the NLP model

   g. Rebalance training data in the NLP model

   h. Sometimes it is required to remove training data to get rid of
         biased results

4. Back to step 1

This workflow is not meant as a one-time event, but this should happen
continuously on a regular basis - over time, the training data and test
coverage will get better, as real input from the chatbot users will be
part of the improvements.

Defining NLP test data with Botium
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Botium has all tools included for testing an NLP model. The user
examples to send to the NLP model for evaluation are organized in
utterance lists as simple text files. Here are two utterance lists, one
for positive consent (“yes”), and the other for rejection (“no”) - here
is the file UTT_YES.utterances.txt:::

   UTT_YES
   yes
   yes please
   sure
   do it
   exactly
   confirm
   of course
   sounds good
   that's correct
   I don't mind
   I agree
   ok

And here is the file UTT_NO.utterances.txt:::

   UTT_NO
   don't do it
   definitely not
   not really
   thanks but no
   not interested
   I don't think so
   I disagree
   I don't want that
   nok
   nope
   no thanks

Asserting NLP predictions with Botium
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Now that the test data is defined, the next step is to actually write
the test cases with user input and assertions. In Botium, this is done
with simple text files as well (or any other of the supported file
formats). A test case named “T01_YES” is defined in a file
T01_YES.convo.txt:::

   T01_YES

   #me
   UTT_YES

   #bot
   INTENT intent_yes
   INTENT_CONFIDENCE 0.8

And a second test case named “T02_NO” in a file T02_NO.convo.txt:::

   T01_NO

   #me
   UTT_NO

   #bot
   INTENT intent_no
   INTENT_CONFIDENCE 0.8

These test cases are to be read like this:

1. First line is the name of the test case

2. Every single user example from the UTT_YES resp UTT_NO utterance list
      is sent to the NLP model

3. A prediction of the intent intent_yes resp intent_no is expected,
      together with a confidence score of at least 0.8, otherwise the
      test case is reported as failure

The INTENT and INTENT_CONFIDENCE words are “magic words” in Botium which
trigger special behaviour. In this case, the assertion behaviour is
triggered to evaluate the predicted intent and the confidence score as
returned from the NLP model.

*There are additional magic words for NLP assertions available in Botium
- see Botium
Wiki*\ https://botium.atlassian.net/wiki/spaces/BOTIUM/pages/2293815/Botium+Asserters

The whole test suite can be run with one of the Botium frontends (Botium
Box, Botium Bindings or Botium CLI).

Conversational Context with Botium
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In order to set the conversational context in the NLP test cases, add
some additional steps to the test case files to set the context.::

   TC78_TEMP_NEWYORK

   #me
   tell me about the weather

   #bot
   Where are you located ?

   #me
   UTT_CITIES

   #bot
   In \*, there are \* degrees Celsius
   INTENT intent_weather
   ENTITIES location

So this test case makes sure that the NLP is in the “ask for weather”
mode before sending the locations from the UTT_CITIES utterance list to
the NLP model.

Test Result Analytics
---------------------

While the previous section showed how easy it is to define NLP model
test cases with Botium, it is clear that even for chatbots with small
functional scope the high number of potential test cases makes it
difficult to compare individual test results and make a clear statement
on the NLP model quality. The basic question to answer is: did the
latest changes have a positive or negative impact on the NLP model
performance ? Even when dealing with a small to medium chatbot project
with 30 intents and 70 user examples per intent, there are thousands of
test results to validate and compare to the previous training cycles —
impossible when relying on quick feedback cycles. What we need are a
rather small amount of comparable numbers (or metrics) — in best case
exactly one number — to tell us about the general NLP model performance,
and some other numbers telling us the hot spots to give attention.

In one sentence: Quality Metrics make NLP model training cycles
comparable and point out areas of interest.

The Confusion Matrix
~~~~~~~~~~~~~~~~~~~~

A Confusion Matrix shows and overview of the predicted intent vs the
expected intent. It answers questions like “When sending user example X,
I expect the NLP model to predict intent Y, what did it actually predict
?”.

|image12|

The expected intents are shown as rows, the predicted intents are shown
as columns. User examples are sent to the NLP model, and the cell value
for the expected intent row and the predicted intent column is increased
by 1. So whenever predicted and expected intent is a match, the cell
value in the diagonal is increased — these are our successful test
cases. All other cell values not on the diagonal are our failed test
cases.

Evaluating the Confusion Matrix
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Here is a small extract from a large confusion matrix

|image13|

This matrix lets deduct statements like these:

-  There are 53 (52 + 1) user examples for the affirm intent. But for
      one of them, the NLP model predicted the enter_data intent
      instead.

-  The NLP model predicted the ask_faq_platform intent for 21 (18 + 3)
      user examples, but it was only expected in 18 of them, for the
      remaining 3 the expected intent was contact_sales, so prediction
      was wrong.

-  For the ask_faq_platform intent there are 19 (18 + 1) user examples,
      but only 18 of them have been recognized by the NLP model.

-  For 38 user examples, the ask_howold intent was expected, and the NLP
      model predicted it for exactly these 38 user examples.

And from these statements, there are several conclusions:

-  The ask_howold and how_to_get_started intents are trained perfectly

-  There are 3 user examples where the NLP model predicted
      ask_faq_platform, but the test data expected the intent
      contact_sales — find out the 3 user examples and refine training
      data for them

-  enter_data intent was predicted for 3 (1 + 1 + 1) user examples where
      another intent was expected. On the other hand there are 682 user
      examples correctly identified as enter_data, so the trade-off for
      this intent is acceptable

Precision, Recall and F1-Score
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The statements above are logically flawless, but not totally intuitive.

-  How to decide if an intent or an intent pair needs refinement and
      additional training?

-  How to actually compare the total NLP model performance to a previous
      training cycle ?

-  How to compare the performance for the most important intents to the
      previous training cycle ?

-  How to decide if the training data is good enough for production
      usage ?

That’s where the statistical concept of precision and recall comes into
play, and the F1-Score representing the trade-off between the two.

**Precision**

In the example above, the NLP model recognized the intent
ask_faq_platform for 21 (18 + 3) user examples. For 3 of them, the
expected intent was another intent, so 3 out of 21 predictions are
wrong. The precision is ~ 0.85 (18 / 21), number of correct predictions
for intent ask_faq_platform shared by total number of predictions for
intent ask_faq_platform.

The question answered by the precision rate is: How many predictions of
an intent are correct ?

**Recall / Sensitivity**

In the example above, we have 121 (1 + 117 + 3) user examples for we
expect the intent contact_sales. The NLP model predicted the intent
contact_sales for 117 user examples only. The recall is ~0.97 (117 /
121), number of correct predictions for intent contact_sales shared by
total number of expectations for intent contact_sales.

The question answered by the recall rate is: How many intents are
correctly predicted ?

**Precision vs Recall — F1-Score**

While those two sound pretty much the same, they are not. In fact, it is
not possible to evaluate the NLP model performance with just one of
those two metrics.

Again, from the example above:

-  The contact_sales intent has been predicted 117 times, and 117 of the
      predictions are correct. The precision rate is 1.0, perfect.

-  There are 4 more user examples for which the NLP predicted another
      intent. The recall rate is ~0.97, which is pretty good, but not
      perfect.

In theory, it is possible to get a perfect precision rate by making a
very low amount of predictions for an intent (for example, by setting
the confidence level very high). But the recall rate will dramatically
decrease in this case, as the NLP model will make no prediction (or a
wrong prediction) in many cases.

On the other hand, it is possible to get a perfect recall rate for an
intent by resolving EVERY user example to this intent. The precision
will be very low than.

The trade-off between recall and precision is called F1-Score, which is
the harmonic mean between the two. Most important, the F1-Score is a
comparable metric for measuring the impact of NLP model training. The
rule of thumb is:

*Increasing F1-Score means increasing NLP model performance, decreasing
F1-Score means decreasing NLP model performance, within your test data.*

An F1-Score of 0.95 usually is a good value, meaning the NLP model is
working pretty good on your test data.

*An F1-Score of 1.0 means that all your test data is perfectly resolved
by your NLP model, the perfect NLP performance. This may be pleasant for
regression testing, but typically it’s a sign for overfitting.*

Cross-Validation
----------------

As mentioned above, these performance metrics only make sense on clear
separation of training data and test data. As this is sometimes not
possible, a method called cross validation can be used to get good
quality metrics for an NLP model. The basic principle is easy to
understand:

-  Split the data into two parts. First part is used for training the
      NLP model, the other part is used for testing.

-  To remove flakiness, do this several times and average the outcome.

In chatbot terms, this means:

-  For each intent, remove some of the user examples and train a new NLP
      model

-  Evaluate the removed user examples and compare the predicted intent
      to the expected intent

-  Calculate precision, recall and F1 and average over all intents

E2E Testing with Selenium or Appium
===================================

Testing the user experience end-to-end has to be part of every test
strategy. Apart from the conversation flow, which is best tested on API
level, it has to be verified that a chatbot published on a company
website works on most used end user devices.

The special challenges when doing E2E tests for a chatbot are the high
amount of test data needed (> 100.000 utterances for a medium sizes
chatbot) and the slow execution time - in an E2E scenario tests are
running in real time. The good news are that for testing device
compatibility, a small subset of test cases is sufficient.

Safe Assumptions when testing a chatbot with Selenium
-----------------------------------------------------

When testing a chatbot with Selenium, there are some safe assumptions
you can rely on to reduce effort when coding test cases:

1. The chatbot is accessible on a website and there maybe is some kind
      of click-through to actually open the chatbot window. The
      procedure to navigate and open the chatbot window is always the
      same for all test cases.

2. Somewhere in the chatbot window there is an input field for text
      messages. When hitting “Enter” or clicking on a button besides the
      input field the text will be sent to the chatbot.

3. Somewhere in the window the chatbot responds in some kind of list
      view. The text sent from the user is mirrored there as well.

   a. The chatbot response contains text, pictures, hyperlinks and maybe
         quick response buttons to click

|image14|

Based on these assumptions an experienced Selenium developer will build
a page object model to reuse for all of the chatbot test cases.

Botium Webdriver Connector
--------------------------

If you ever worked with Selenium, you are aware that writing an
automation script usually is a time-consuming task. Botium helps you in
writing automation scripts for a chatbot widget embedded on a website
and speeds up the development process by providing a parameterizable,
default configuration for adapting it to your actual chatbot website
with Selenium selectors and pluggable code snippets:

-  Website address to launch for accessing the chatbot

-  Selenium selector for identification of the input text field

-  Selenium selector for identification of the "Send"-Button (if
      present, otherwise message to the chatbot is sent with "Enter"
      key)

-  Selenium selector for identification of the chatbot output elements

-  Selenium capabilities for device or browser selection or any other
      Selenium specific settings

*Note: Botium can work with any Selenium or Appium endpoint available -
either with a virtual browser like PhantomJS, an integrated standalone
Selenium service, your own custom Selenium grid, or with cloud providers
like Perfecto Labs.*

If there are additional steps (mouse clicks) to do on the website before
the chatbot is accessible, you will have to extend the pre-defined
Selenium scripts with custom behaviour as Javascript code.::

  module.exports = async (container, browser) => {
    const ccBtn = await browser.$('#onetrust-accept-btn-handler')
    await ccBtn.waitForClickable({ timeout: 20000 })
    await ccBtn.click()

    const startChat = await browser.$('#StartChat')
    await startChat.waitForClickable({ timeout: 20000 })
    await startChat.click()
  }

This code snippet does the following:

1. Waiting for a “Cookie Consent” button to appear on the website

2. Clicking this button to make the website usable

3. Waiting for a “Start Chat” button to appear and clicking it when
      available

4. Waiting until the basic chatbot interaction elements are visible

The full Botium configuration for this scenario looks like this:::

  {
    "botium": {
      "Capabilities": {
        "PROJECTNAME": "WebdriverIO Plugin Sample",
        "CONTAINERMODE": "webdriverio",
        "WEBDRIVERIO_OPTIONS": {
          "capabilities": {
            "browserName": "chrome"
          }
        },
        "WEBDRIVERIO_URL": "https://www.my-company.com",
        "WEBDRIVERIO_OPENBOT": "./snippets/openbot",
        "WEBDRIVERIO_INPUT_ELEMENT": "//input[@id='textInput']",
        "WEBDRIVERIO_INPUT_ELEMENT_SENDBUTTON": "//button[contains(@class,'bot__send')]",
        "WEBDRIVERIO_OUTPUT_ELEMENT": "//div[contains(@class,'from-watson')]"
      }
    }
  }

With this configuration, all of your convo and utterances files can be
used to run test cases with Botium and Selenium.

Testing Voice-Enabled Chatbots
==============================

When testing voice apps, all of the principles from the previous
sections apply as well. Some of the available voice-enabled chatbot
technologies natively support both text and voice input and output, such
as Google Dialogflow or Amazon Lex. Others are working exclusively with
voice input and output, such as Alexa Voice Service. And all the other
technologies can be extended with voice capabilities by inserting
speech-to-text and text-to-speech engines in the processing pipeline.

For doing serious tests at least the chatbot response has to be
available as text to use text assertions. Botium supports several
text-to-speech and speech-to-text engines for doing the translations.

*In addition to the well-known cloud services from Google and Amazon,
Botium also has its own free and open source speech service included -
Botium Speech Processing.*

There is one good reason for using voice instead of text as input to
your test cases, if there are historic recordings available when
transitioning from a legacy IVR system. Such libraries often are a
valuable resource for test data.

How to collect training and test data
=====================================

Most chatbots are poor quality because they either do no training at all
or use bad or very little training data. It’s easy to make a poor
chatbot — just connect some APIs, write (or copy/paste) some lines of
code, that’s it. The difficulty and high effort comes from implementing
a process for training and testing the bot, and that’s where lots of
companies are failing: chatbots are only as good as the training and
testing they are given by their makers, and the quality of the training
and testing is only as good as the data is.

Comparison Matrix
-----------------

Each of the described methods has strengths and weaknesses.

|image15|

Criteria 1: Duration
~~~~~~~~~~~~~~~~~~~~

The “time to market” is one of the most important criteria for project
owners, and proper training is required before your chatbot is ready for
publication.

Criteria 2: Setup Effort
~~~~~~~~~~~~~~~~~~~~~~~~

Before training begins, there is effort involved — typically this effort
is located in software development.

Criteria 3: Training Effort
~~~~~~~~~~~~~~~~~~~~~~~~~~~

And then there is the effort in the training phase itself. High manual
effort means high training effort, in short.

Criteria 4: Price
~~~~~~~~~~~~~~~~~

The total price depends on the other criteria: high manual effort means
high personnel costs, high software development effort as well.
Licensing costs have to be included in the calculation as well.

Criteria 5: Quality
~~~~~~~~~~~~~~~~~~~

Finally, the outcome in quality differs over the training methods, and
it’s up to the project owners to balance the involved costs with the
expected overall quality.

Method 1: Mechanical Turk (“be the bot yourself”)
-------------------------------------------------

The “Mechanical Turk” was a fake chess-playing machine constructed in
the 18th century. The Turk was in fact a mechanical illusion that
allowed a human chess master hiding inside to operate the machine.
Instead of a chatbot software a human agent responds to user request,
while the user is kept in dark about it. A valid attempt for PoCs,
market research and user acceptance verifications, due to nearly no
setup costs. High effort involved during the training phase, as each
user request has to be handled manually.

✔ good quality (experience real users)

✖ long training phase with huge manual effort

Method 2: Friendly User
-----------------------

As soon as the basics of the chatbot are available, friendly users are
motivated to interact with the chatbot. Training data is collected
whenever someone interacts, and constant training makes the bot smarter
with each conversation by a friendly user. In a large company, motivate
co-workers to take part in testing.

✔ low setup effort

✖ low quality due to “biased” users (most likely with domain knowledge)

✖ high manual effort and high price for personnel costs

Method 3: Use the Crowd
-----------------------

Publish the chatbot and let the crowd do the rest: training is carried
out by a number of different testers from different places, not by hired
consultants and professionals. Potential users of your chatbot provide
realistic usage scenarios and training data.

✔ good quality if done right (crowd tester pre-selection)

✖ external costs for crowd testing

Method 4: Previous Communication
--------------------------------

Archived former communication from the chatbot domain is a real treasure
— emails, white mail, meeting protocols, everything is potentially
valuable training data. Obviously, there is effort involved in gathering
the files from several archives, transforming it into a format usable
for chatbot training (annotated plain text), which is partially
automatable, but you have to expect lots of manual effort for adding
text annotations.

✔ good quality due to domain specific data

✖ high setup effort for data preparation (text annotation)

Method 5: Training Datasets
---------------------------

Having access to domain-specific datasets collected and shared by
chatbot developer teams all over the world — this clearly is the fastest
approach for getting a chatbot to acceptable quality.

✔ “quick win” in all aspects

✖ selection of an additional training method obligatory, because dataset
may be too generic for the chatbot business case

Comparison Details: Costs over Time
-----------------------------------

For the training methods involving manual effort, the costs are
constantly high over the training phase, while for the automated
training methods, the upfront costs are higher, but the manual methods
are outperformed quickly.

|image16|

Comparison Details: Quality over Time
-------------------------------------

The manual approaches take some time to reach good quality, and the
learning rate is expected to flatten down over time — user input will
repeat after several cycles — but that’s actually a good thing, as it is
an indicator that training the most common utterances and conversations
is coming to an end. The automated approaches will lead to the expected
quality almost immediately.

|image17|

Comparison Summary
------------------

Best quality of the training data is guaranteed if collected in
conversations with real users and real customers — it easily outperforms
data collected by asking company employees biased to their company
culture and domain knowledge. The price is higher effort in collecting
and evaluating this training data, and it could easily take months of
effort to gather a reasonable amount. A good combination of these
strategies is the best way to success.

Chatbot Training Never Ends!
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The key to success is to constantly monitor your chatbot and continue
training to get smarter — either by doing constant training with human
effort, or by scheduling regular training cycles, incorporating new
utterances and conversations from real users.

Designing a Test Strategy from Scratch
======================================

Testing and training an NLP engine to provide a good user experience is
a challenging task. In almost every project there is a clear separation
between the short-tail topics, the long-tail topics and the topics where
human handover is required.

First Steps: Short-Tail Topics
------------------------------

The recommendations for the first steps in a chatbot project are to
concentrate training and testing on the short-tail topics - typically,
with a customer support chatbot, which are the majority of the chatbots
out there, there are a handful of topics only for which you have to
provide a good test coverage. Apart from that, leave the long-tail
topics aside at first and design a clear human handover process.

The challenge is how to get a good test coverage for the short-tail
topics (see previous section). This is the real hard work in a chatbot
project. Tools like Botium can help in this process with file format
converters, import/export interfaces, audio processing, NLP analytics,
sentence paraphrasers and more.

Continuous Training
-------------------

As soon as the chatbot is live, there is continuous re-training required
- this process involves manual work to evaluate real user conversations
that for some reason went wrong and to deduct the required training
steps. During this process, the test coverage will be increased - for
the short-tail topics you can expect a near 100% test coverage within
several weeks after launch: those are the topics asked over and over
again, and as complex as human language may be, there is only a finite
number of options how to express an intent in a reasonable short way.

Fill in the Long-Tail Topics
----------------------------

As last step, add more and more of the long-tail topics to the
continuous training process.

.. _section-3:

Final Remarks
=============

For testing conversational AI, test automation engineers require
additional skills - most important, extend your toolbelt with basic
knowledge on text classification, machine learning and statistical
measures. Tools like Botium can help in design and automated execution
of test cases. As opposed to testing websites, desktop apps or
smartphone apps, there is nearly no boilerplate code required for
automated testing, but the effort lies in collecting, analyzing and
organizing test and training data.

.. |image0| image:: media/image10.png
   :width: 6.27083in
   :height: 3.22222in
.. |image1| image:: media/image17.png
   :width: 6.27083in
   :height: 5.18056in
.. |image2| image:: media/image3.png
   :width: 4.31979in
   :height: 3.07981in
.. |image3| image:: media/image18.png
   :width: 6.27083in
   :height: 4.44444in
.. |image4| image:: media/image12.png
   :width: 3.05729in
   :height: 6.47823in
.. |image5| image:: media/image14.png
   :width: 6.27083in
   :height: 6.375in
.. |image6| image:: media/image6.png
   :width: 6.27083in
   :height: 6.375in
.. |image7| image:: media/image15.png
   :width: 6.27083in
   :height: 6.375in
.. |image8| image:: media/image7.png
   :width: 6.27083in
   :height: 6.68056in
.. |image9| image:: media/image16.png
   :width: 6.27083in
   :height: 2.55556in
.. |image10| image:: media/image11.png
   :width: 3.61458in
   :height: 7.67699in
.. |image11| image:: media/image4.png
   :width: 4.54688in
   :height: 5.1919in
.. |image12| image:: media/image13.png
   :width: 6.27083in
   :height: 4.33333in
.. |image13| image:: media/image8.png
   :width: 4.64583in
   :height: 2.875in
.. |image14| image:: media/image5.png
   :width: 5.80729in
   :height: 3.62053in
.. |image15| image:: media/image1.png
   :width: 6.27083in
   :height: 1.05556in
.. |image16| image:: media/image9.png
   :width: 6.27083in
   :height: 4.19444in
.. |image17| image:: media/image2.png
   :width: 6.27083in
   :height: 3.97222in
