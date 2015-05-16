from modeller import *

env = environ()
aln = alignment(env)
for (pdb, chain) in (('1fgk', 'A'), ('1fmk', 'A'), ('1gz8', 'A'),
                     ('1nxk', 'A'), ('1nxk', 'B'), ('1ua2', 'A'),
                     ('1uwh', 'A'), ('1xjd', 'A'), ('1ywr', 'A'), ('2src', 'A')):
    m = model(env, file=pdb, model_segment=('FIRST:'+chain, 'LAST:'+chain))
    aln.append_model(m, atom_files=pdb, align_codes=pdb+chain)
aln.malign()
aln.malign3d()
aln.compare_structures()
aln.id_table(matrix_file='family.mat')
env.dendrogram(matrix_file='family.mat', cluster_cut=-1.0)
