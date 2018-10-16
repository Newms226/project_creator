project
########

Name : The name of the project.
    * Allowed: Spaces, any case, numbers, _
    * parsed to be:
        - camel case
        - project relative (future)


example::

    "project": {
        "name": "Project Creator",
        "license": "MIT",
        "dir": "",
        "programmers": [
          "Michael Newman"
        ]
      }

Relativity
###########

Folders & files are defined *relative to a root dir*. This root directory is
named after the sy

The `root` dir is assumed to precede any directory reference. Lets assume
that our roFor example,
when you type `"/design"` the parser object will parse the absolute path as `

example of a folder in a root dir (root/src/) ::

    {
      "name": "src",
      "git": true,
      "root": null
    }

example of a folder in a sub dir (root/design/strategy/)::

    {
      "name": "strategy",
      "git": true,
      "root": "/design"
    }

