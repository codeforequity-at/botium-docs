Running Chatbot Test Cases
==========================

Botium CLI vs Botium Bindings
-----------------------------

You should use **Botium Bindings** if:

* you are familiar with Node.js and test runners like Mocha, Jasmine or Jest
* you already have some unit tests in your Node.js project and want to add Botium tests to it

You should use **Botium CLI** if:

* you want to use more Botium Core functionality than just test automation
* you do not want to deploy a new technology (Node.js) to your workstations (Botium CLI is available as Docker)

.. _using-botium-cli:

Using Botium CLI
----------------

::

  botium-cli run

See :ref:`Botium CLI Documentation <botium-cli>`

.. _using-botium-bindings:

Using Botium Bindings
---------------------

::

  npm test

See :ref:`Botium Bindings Documentation <botium-bindings>`
