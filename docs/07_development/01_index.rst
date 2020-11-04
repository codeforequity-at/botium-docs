Extending Botium
****************

.. _develop-connector:

Developing Botium Connectors
============================


https://botium.atlassian.net/wiki/spaces/BOTIUM/pages/38502401/Howto+develop+your+own+Botium+Connector

https://botium.atlassian.net/wiki/spaces/BOTIUM/pages/744783879/Howto+develop+your+own+HTTP+JSON+Botium+Connector

https://botium.atlassian.net/wiki/spaces/BOTIUM/pages/761004038/Howto+deploy+my+own+Botium+Connector


.. _develop-asserter:

Developing Custom Asserters
===========================

https://botium.atlassian.net/wiki/spaces/BOTIUM/pages/24477705/Developing+Custom+Asserters

.. _develop-logichook:

Developing Botium Logic Hooks
=============================

https://botium.atlassian.net/wiki/spaces/BOTIUM/pages/642908193/Developing+Custom+Logic+Hooks


.. _develop-customhook:

Developing Custom Hooks
=======================



Custom Hooks
------------

There are capabilities for running your custom logic, developed in
Javascript, during Botium script execution.

-  CUSTOMHOOK_ONBUILD

-  CUSTOMHOOK_ONSTART

-  CUSTOMHOOK_ONUSERSAYS

-  CUSTOMHOOK_ONBOTRESPONSE

-  CUSTOMHOOK_ONSTOP

-  CUSTOMHOOK_ONCLEAN

There are several options how to inject our Javascript code here. The
functions are called with arguments from Botium as nested structure.

-  **container**: the currently executing Botium container

-  **meMsg** (only for CUSTOMHOOK_ONUSERSAYS): message sent to bot

-  **botMsg** (only for CUSTOMHOOK_ONBOTRESPONSE): message received from
      bot

As NPM module
~~~~~~~~~~~~~

Your custom NPM module has to export exactly one function.

"CUSTOMHOOK_ONUSERSAYS": "my-own-module",

As Javascript file
~~~~~~~~~~~~~~~~~~

Your file has to export exactly one function.

"CUSTOMHOOK_ONUSERSAYS": "path/to/your/javascript/file.js",

Example function in file.js

module.exports = ({ container, meMsg }) => {

console.log('in userSays hook');

meMsg.CUSTOM_VALUE = 'something'

}

As Javascript code
~~~~~~~~~~~~~~~~~~

Add javascript code snippets to the capability value.

"CUSTOMHOOK_ONUSERSAYS": "meMsg.CUSTOM_VALUE='something'",



