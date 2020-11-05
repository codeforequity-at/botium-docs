Troubleshooting
***************

Sometimes things just don't work. Here are some generic insights on how to start investigation.



Enable Logging
==============

Botium uses the `Debug <https://github.com/visionmedia/debug>`_ library for logging and debugging purposes. Console output can be enabled by setting an environment variable before starting the Botium session::

  export DEBUG=botium* # to enable Botium logging
  export DEBUG= # to disable Botium logging

Please lookup `Debug library documentation for details <https://github.com/visionmedia/debug>`_.

There should be pretty detailed output in the console now.


Additional logfiles
-------------------

In the "botiumwork"-directory, for each run, there is a temporary work directory created, where some connectors place artifacts, logfiles etc. Usually, this directory is cleaned by Botium after finishing work, but sometimes it can be useful to keep the files for investigation. Setting the **CLEANUPTEMPDIR**-capability to "false" prevents the cleanup.

Problems with Installation
==========================

In case you have troubles with "npm install" in any Botium-related module, this is not a problem with Botium itself, but with your Node.js and npm installation. We won't be able to help you on this. But here are some generic steps you could take:

* remove the files "package-lock.json" and the directory "node_modules" and try again
* remove the global npm-cache with the command "npm cache clean --force" and try again
* sometimes you need to compile native modules for installation, please install the windows build tools first "npm install --global windows-build-tools"
* try the yarn package manager instead of npm (just replace "npm" with "yarn" in all npm-related commands)

Getting help
============

See :ref:`here <getting-help>`
