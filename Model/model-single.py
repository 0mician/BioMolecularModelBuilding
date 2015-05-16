from modeller import *
from modeller.automodel import *

env = environ()
a = automodel(env, alnfile='lrrk2-1gz8.ali',
              knowns='1gz8', sequence='lrrk2',
              assess_methods=(assess.DOPE, assess.GA341))
a.starting_model = 1
a.ending_model = 5
a.make()
