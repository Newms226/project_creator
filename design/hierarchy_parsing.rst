* Recursively looping through tree (with curdir set to the current dir)
    #. BASE CASE:
        - If no children, return up recursive call
    #. dir or file?
        - dir
            * generate temp directory
            * parse git strategy
            * recursive call
        - file
            * generate valid file name by combining the extension and the name
            * (optional) add header
            * (optional) add/import text
    #. continue down the file