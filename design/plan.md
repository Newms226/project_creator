1. init
    a. separate all of the JSON roots
        * folders, files, project, git, sync 
    b. create temp dir
    c. create sync & temp mapping locations
2. make folders
    * work with **temp**
    * loop through all of the folders
        a. generate dir
        b. generate sub dir
        c. parse git & sync strategy
            * map to valid location
3. make files
    * loop through all of the files
        a. init file
        b. (optional) generate header
        c. (optional)import text
            * from URL/path
        d. parse git & sync strategy
            * map to valid location
4. un-temp
    * copy to actual location
        ? copy to sync location?
5. sync
    * define/generate .gitignore
    * sync to all locations