This Repository is where a Upload my "TPs" from: 
	 
	https://openclassrooms.com/courses/apprenez-a-programmer-en-python

Feel free to have a look/see and leave a comment.

Those are symple exercices from the cours. I always try to work by versions. 
	
	= .v1      is the exercice straight from the cours "as I" understand it.
	= .v2      is usually the way I try to improve on what "I understood" (without too much research). 
	= .v3      is the the version I re-worked after a bit of research on the net. (mostly after lots and lots of trial & error ^^)
	= .final   is the final version after I see the comments (if there are any) and/or talk to friends (Devs for the most parts) 

So if you see sommething that can be improved upon, don't be shy! however all I ask is to always explain the reasoning behind your improvements.
After all, I am trying to learn :-P.

Example #1: 

	me:	#! /usr/bin/python
		import os
		import sys
		import time
		import math

	you:    #! /usr/bin/python
		import os, sys, time, math     #This is more elegant and "cleaner looking"

Example #2

	me:	#! /usr/bin/python
                T = 1
		print(T)
		T = 2
                print(T)
		T = 3
		print(T)

	you:	#! /usr/bin/python
		for T in range(1,4): print(T)   #We create a Loop from a range, starting at 1 and finishing at 4, then we "print" the result.
