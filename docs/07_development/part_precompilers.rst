.. _develop-precompilers:

Custom File Format Precompiler
==============================

If you have custom file format, then you have to use a precompiler to convert it to any standard file format.

Supported input and output file extensions are same as supported file extensions of Botium: 

* .convo.txt, 
* .utterances.txt, 
* .pconvo.txt, 
* .scriptingmemory.txt, 
* .xlsx, 
* .convo.csv, 
* .pconvo.csv, 
* .yaml, 
* .yml, 
* .json
* .md

You dont have to keep the file extension. (It is possible to convert .md to .json for example)

Output file format can be any standard Botium Script format, but we suggest to use JSON (or YAML) file format. They can contain all parts of a script in a single file, and it is easy to work with.

*There is a limitation with precompilers. It is not possible to create more files from one. Using JSON output file format can help handle this limitation.*

Configuration capabilities
--------------------------

The preformatters are dynamic. You can use more precompilers, even from the same type. The capabilities are dynamic too, there are many ways to structure them:

Just for one precompiler::

  {
    "PROJECTNAME": "Precompiler",
    "CONTAINERMODE": "echo",
    "PRECOMPILERS.NAME": "<precompilername>",
    "PRECOMPILERS.VARIABLE1": "..."
  }

or::

  {
    "PROJECTNAME": "Precompiler",
    "CONTAINERMODE": "echo",
    "PRECOMPILERS": {
      "NAME": "<precompilername>",
      "VARIABLE1": "..."
    }
  }

same as string::

  {
    "PROJECTNAME": "Precompiler",
    "CONTAINERMODE": "echo",
    "PRECOMPILERS": "{\"NAME\": \"<precompilername>\",\"VARIABLE1\": \"...\"}"
  }

For more precompilers::

  {
    "PROJECTNAME": "Precompiler",
    "CONTAINERMODE": "echo",
    "PRECOMPILERS.0.NAME": "<precompilername>",
    "PRECOMPILERS.0.VARIABLE1": "...",
    "PRECOMPILERS.1.NAME": "<precompilername>",
    "PRECOMPILERS.1.VARIABLE1": "..."
  }

or::

  {
    "PROJECTNAME": "Precompiler",
    "CONTAINERMODE": "echo",
    "PRECOMPILERS.0": {
      "NAME": "<precompilername>",
      "VARIABLE1": "..."
    },
    "PRECOMPILERS.1": {
      "NAME": "<precompilername>",
      "VARIABLE1": "..."
    }
  }

or::

  {
    "PROJECTNAME": "Precompiler",
    "CONTAINERMODE": "echo",
    "PRECOMPILERS": [
      {
        "NAME": "<precompilername>",
        "VARIABLE1": "..."
      },
      {
        "NAME": "<precompilername>",
        "VARIABLE1": "..."
      }
    ]
  }

same as string::

  {
    "PROJECTNAME": "Precompiler",
    "CONTAINERMODE": "echo",
    "PRECOMPILERS": "[{\"NAME\": \"<precompilername>\",\"VARIABLE1\": \"...\"},{\"NAME\": \"<precompilername>\",\"VARIABLE1\": \"...\"}]"
  }

JSON_TO_JSON_JSONPATH Precompiler
---------------------------------

* Compiles not-standard-json using JsonPath. 
* This precompiler just supports extraction of utterances.

Capabilities
~~~~~~~~~~~~

**NAME**

Set to JSON_TO_JSON_JSONPATH to use this compiler.

**CHECKER_JSONPATH**

Optional. If the precompiler does not found anything using this JsonPath, then ignores the source json file.

**ROOT_JSONPATH**

Optional. Maps the source JSON to utterance struct array. (One entry in map can be mapped to one utterance reference name)

**UTTERANCE_REF_JSONPATH**

JsonPath to the utterance reference name

**UTTERANCES_JSONPATH**

JsonPath to the utterances

Example
~~~~~~~

Source Json::

  {
    "domains": [
      {
        "name": "Banking",
        "intents": [
          {
            "name": "Transfer",
            "sentences": [
              {
                "text": "Send 2 bucks to savings!"
              }
            ]
          }
        ]
      }
    ]
  }

Capabilities::

  {
    PRECOMPILERS: {
      "NAME": "JSON_TO_JSON_JSONPATH",
      "CHECKER_JSONPATH": "$.domains[*].intents[*]",
      "ROOT_JSONPATH": "$.domains[*].intents[*]",
      "UTTERANCE_REF_JSONPATH": "$.name",
      "UTTERANCES_JSONPATH": "$.sentences[*].text"
    }
  }

SCRIPTED Precompiler
--------------------

Compiles not-standard Text, Excel, CSV, YAML, JSON, Markdown file toBotiumScript File Formats using JavaScript code.

Capabilities
~~~~~~~~~~~~

**NAME**

Set to SCRIPT to use this precompiler.

**SCRIPT**

The JavaScript code - it is not a function, do not use *return* there, but set the module.exports variable.

Example
~~~~~~~

For the sake of simplicity we use JSON file with just utterances as output. But of course all features of all file types can be used.

**Basic example, json**

::

  {
    "PROJECTNAME": "Precompiler",
    "CONTAINERMODE": "echo",
    "PRECOMPILERS": {
      "NAME": "SCRIPT",
      "SCRIPT": "const utterances = {};for (const entry of scriptData) {;utterances[entry.intent] = entry.sentences;};module.exports = { scriptBuffer:{utterances} };"
    }
  }

**Basic example**

::

  const utterances = {}
  for (const entry of scriptData) {
    utterances[entry.intent] = entry.sentences
  }
  module.exports = { scriptBuffer: { utterances } }

*scriptData* is a predefined variable with the contents of the file. It is string, or JSON, depending on file format.

Set *module.exports* variable with the compiled contents. You can use two fields if you want to process the current file:

* *scriptBuffer* with the compiled content (text or json). Falsy value means, precompiler does not want to change anything.
* *filename* with this field you can change filename, and extension.

Or put the compiled contents direct into result field::

  module.exports = { utterances }

**Filtering by filename**

::

  if (filename.endsWith('.json')) {
    module.exports = ...
  }

*filename* is a predefined variable. If you dont process the content, simply dont set *module.exports* field.

**Filtering by content**

::

  if (scriptData.utterances) {
    const utterances = {}
    for (const entry of scriptData.utterances) {
      utterances[entry.intent] = entry.sentences
    }
    module.exports = ...
  }

**Change file extension**

Lets suppose we have a json in a text file. And its format is different as Botium standard JSON format. So we have to change the content, and the extension too::

  const utterances = {}
  // creating utterances from scriptData
  module.exports = { scriptBuffer:{utterances}, filename: filename + ".json" }
