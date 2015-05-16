from modeller import *

env = environ()
aln = alignment(env)
mdl = model(env, file='1gz8', model_segment=('FIRST:A','LAST:A'))
aln.append_model(mdl, align_codes='1gz8', atom_files='1gz8.pdb')
aln.append(file='lrrk2.ali', align_codes='lrrk2')
aln.align2d()
aln.write(file='lrrk2-1gz8.ali', alignment_format='PIR')
aln.write(file='lrrk2-1gz8.pap', alignment_format='PAP')
