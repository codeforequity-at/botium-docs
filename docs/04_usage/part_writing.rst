Writing Chatbot Test Cases
==========================

The :ref:`previous section <botium-basics>` demonstrated how to write Botium Test Cases in :ref:`BotiumScript <botium-scripting>`. Botium test projects are organized in a directory structure which is

1. extendable
2. overviewable
3. and git-friendly

Anatomy of a Botium Project
---------------------------

The **recommended** directory structure is like this:

* botium.json
* package.json (*Botium Bindings only*)
* spec/

 * botium.spec.js (*Botium Bindings only*)
 * convo/

  * some.convo.txt
  * some.utterances.txt
  * subfolder1/

   * another.convo.txt
   * another.utterances.txt
   * ...

  * subfolder2/

   * onemore.convo.txt
   * ...

  * ...

Starting from the base directory (in the example above *spec/convo*), Botium will recursivly traverse the directory tree. You can choose any directory structure you think is useful in your project.

Utterance Expansion
-------------------

Utterance and scripting memory expansion is done dynamically when running test cases.

