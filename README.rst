Git migrate
===========

Execute commands from shell file, storing last successful execution in
detached git branch.

How it works
------------

You have some bash file(-s) with few commands inside. Each on it's own
line. If you will run it in shell -- it will execute all of them.

During deploy you need to run only new commands, that was added to this
file. Think of it as a one way DB migrations that will get commands to
execute from ``git diff``.

Git to the resque! System will store successfull commands executions in
detached branch named ``.gitmigrate``. Then if we will have 5 commands
and only 3 of them was successful, on next run we will not run them.

Always run/include some code?
-----------------------------

First lines until two new lines will be always executed. So when you
have shebang and then 2 new lines (as it usual) -- it will be executed.
Also you can add some includes after your 1st line, that will allow you
to have DSL-like functions inside your script. After which you shoudl
have two new lines.

Conventions and configurations
------------------------------

Configuration values are in file ``.gitmigrate``.

Configuration values with defaults
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

See ``.gitmigrate.dist`` as an example

-  Detached branch name ``_gitmigrate``.
-  Path to command file(s) is ``.gitmigrate.*``. It could be both
   ``.gitmigrate.sh`` or ``.gitmigrate.py`` or ``.gitmigrate.d/``
   directory.
