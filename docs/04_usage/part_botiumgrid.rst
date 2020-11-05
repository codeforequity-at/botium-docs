.. _botium-grid:

Botium Grid Documentation
=========================

The Botium Grid allows you to distribute Botium tests over several machines. Just start the Botium Agent on a remote machine and connect your Botium scripts to the remote agent.

Starting the Botium Grid Agent
------------------------------

... with Botium CLI (recommended)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Install the :ref:`Botium CLI <botium-cli>` and run this command for showing the command line options::

  botium-cli agent help

And this one to start the Botium Agent::

  botium-cli agent

... from Botium Core Source
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Clone the `Botium Core Github repository <https://github.com/codeforequity-at/botium-core>` and run::

  npm install
  npm run agent

This is meant or developers only, as it requires you to setup npm links to botium-core as well.

Using the Botium Agent
----------------------

... from Botium Bindings or Botium CLI
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Set these capabilities:

* BOTIUMGRIDURL to http://remoteservername:46100 (default Botium Agent port)
* BOTIUMAPITOKEN for setting the Botium API Token

And run your script as usual.

... from another client
~~~~~~~~~~~~~~~~~~~~~~~

Botium Agent exports a very simple HTTP/JSON API (see `Swagger definition <https://github.com/codeforequity-at/botium-core/blob/master/src/grid/agent/swagger.json>`_). This can be used from any programming language capable of doing HTTP communication, or from tools like Tricentis Tosca and Postman/Newman.

Security
--------

Botium Agent should be started with security enabled. The environment variable "BOTIUM_API_TOKEN" is expected to contain the API Token ("password") the clients should send in all HTTP requests (in HTTP-Header "BOTIUM_API_TOKEN").