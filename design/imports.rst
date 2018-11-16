PLAN
=====

Types of imports:
    - resource file (license, .gitignore)
        * Modified w/ variables OR NOT
    - an entire folder structure from the system
    - another template

COMMAND
========

Files
-----
prj import -f [SRC_TYPE] <SRC_PATH> [DEST_TYPE] <DEST_PATH> [OPTIONS]

SRC_TYPE:
    A flag denoting what type of path is denoted by SRC_PATH. By default,
    the path is assumed to be an absolute path on the system.

    Options:
        * --resource:
            a path relative to `./resources` contained within this utility. For
             example, the call::

                $ prj import -f --resource licenses/MIT.rst -node license

            would import the MIT license contained at
            `./resources/licenses/MIT.rst` to the node 'license'

        * --system_path:
            (**DEFAULT**) Import from a path in the system

SRC_PATH:
    The path to the source. Modified by SRC_TYPE.

DEST_TYPE:
    A flag denoting what type of path is denoted by DEST_PATH.

    Options:
        * --node:
            A node within the template. This is the default setting when
            import utility is ran from within the project creator. The
            value of DEST_PATH is the name within the file tree.

        * --system:
            A direct system path. The value of DEST_PATH is the path.
            This is the default setting when the import utility is
            ran from the command line directly.

DEST_PATH:
    Path to the destination.

OPTIONS:
    * -v --variable_replacement
    * -o --stubbed_outline
    * -c --content
    * -s --structure


Directories
-----------
prj import -d <SRC_PATH> [DEST_PATH_FLAG] <DEST_PATH> [OPTIONS]

    SRC_PATH: System path to the directory import


Templates
---------
prj import -t <TEMPLATE_TYPE> <SRC_PATH> [ROOT_NAME] [DEST_PATH_FLAG] <DEST_PATH> [OPTIONS]


TEMPLATE_TYPE:
    Defines the type of template where the source is located

    * --json
    * --xml


OPTIONS
========
-c --content
    (default) Whenever a file is encountered, the full contents are copied


-o --outline
    Whenever a file is encountered, the contents are ignored but the file is
    still generated

-r --recursive [DEPTH=<depth>]
    (default) preforms the import recursively. By default, there is no maximum
    recursive depth defined by this program. As such, depth is constrained
    only by the implementation.

    DEPTH:
        the maximum recursive depth to search.

        0 simply looks at the directory that is passed.

        Default value is infinity

-s --structure
    imports simply the structure of the source, ignoring all content

--stub
    when the process encounters a code file (.py, .java, etc.), generate a
    stubbed outline of the file as its contents

-v --variable_replacement <OLD='NEW'> ...
    Replaces all instances of 'OLD' with 'NEW'. Note that you can
    easily add more than one replacement. However, invalid spaces will cause
    this process to fail. The single quotations are NOT optional as they
    allow spaces within the replacement field 'NEW'.

    Within the document, the `OLD` field should be encosed with `${ }$` . So,
    if the variable NAME would appear as `${NAME}$` within the document.

    Valid Examples:
        Document: ... ${NAME}$ ....
        Options: ... -v NAME='Michael Newman'
        Results in: ... Michael Newman ...

        Document: ... ${NAME}$ ... ${YEAR}$
        Options: ... -v NAME='Michael Newman' YEAR='2018'
        Results in: ... Michael Newman ... 2018



DEFAULT IMPORTS
================

