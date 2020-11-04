.. _userinputs:

Using User Inputs
=================

Main communication channel between a user and chatbot is text. Some chatbots provide simple user interface elements such as buttons.

Not all user inputs are supported by all connectors. Some connectors only allow text input, others allow file uploads, and others allow filling out forms - it depends on the used technology.

BUTTON
------

* Will simulate a button click if the connector supports it.
* first argument: button payload
* second argument (optional): button text

Example::

  sending button

  #me
  BUTTON Help|Displays Help

MEDIA
-----

* Will simulate user sending a picture (url resolved relative to the baseUri or to the convo file) if the connector supports it.
* arguments: pathes to a media files

  * Can include wildcards to run same convo multiple times for multiple files (only loading from folders supported, not from HTTP servers)

* global argument **baseUri**: base media location as URI (for HTTP downloads)
* global argument **baseDir**: base media location directory (default: directory where convo file is located)
* global argument **downloadMedia**: flag if media should be downloaded and attached to message (see Connector documentation if this is required or not)

Example (one file)::

  sending picture file

  #me
  MEDIA send_this_file.png

Example (wildcards)::

  sending audio files

  #me
  MEDIA audiodirectory/*.wav

Most common use case is to send recorded audio files instead of text files for testing voice bots. This is supported by several Botium connectors.

* Dialogflow
* Lex
* Directline (just attachment)

FORM
-----

* To simulate a user filling out a form, typically followed by a simulated button click. 
* first argument: field name
* second argument: field value (If second argument is empty, form value will be set to “true”)

Example::

  sending form

  #me
  FORM text1|something entered
  FORM text2|something else
  BUTTON Submit

Global Arguments
----------------

Global arguments can be set in botium.json::

  {
    "botium": {
      "Capabilities": {
        ...
        "USER_INPUTS": [
          {
            "ref": "MEDIA",
            "src": "MediaInput",
            "args": {
              "downloadMedia": true
            }
          }
        ]
      }
    }
  }