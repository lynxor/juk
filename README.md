juk
===

Python harness for entelect challenge 
Uses python 2
run like this:

> python game.py /path/to/bot1 /path/to/bot2 

For interactive mode(player A): (#use --interactiveB for player B)
 
> python2 game.py /path/.. /path2/ --interactiveA 


For windows:
change processes.py:
  self._exec = "./run"
to:
  self._exec = "run.bat"  # and then be sure that your file is actually called run.bat and exists in the folder you specified for the bot - duh


