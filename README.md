# Iterative Rock Paper Scissors #
## MS&T CS348 FS2013 Assignment Series 2 ##
- - -
To run with default.cfg, execute:
python irps.py

Or with a custom .cfg:
python irps.py -c custom.cfg

Extra Credit:
In assignment.py, line 112, the program checks to see if the average fitness is worse than the previous best fitness.
If this is the case, then cycling is detected and the tree in the current population with the lowest fitness is replaced with another previous member of the 'hall of fame'
