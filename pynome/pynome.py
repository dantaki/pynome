#!/usr/bin/env python
import os,sys
import matplotlib
import matplotlib.pyplot as plt
class Genome():

	def __init__(self,ref=None,
				skip_x=None,skip_y=None,skip_m=False):
		if not os.path.isfile(ref): ref = get_path()+'/{}.txt'.format(ref)
		self.ref = ref
		self.genome_end=0    #end of the genome in floating positions
		self.chrom = []      #list of chromosomes
		self.labs  = []      #chromosome labels
		self.tix   = []      #chromosome axis ticks
		self.chrom_dict = {} #dictionary of chromosomes
		self.skip_x,self.skip_y,self.skip_m=skip_x,skip_y,skip_m
		self.load_reference()
		self.make_axis()

	def load_reference(self):
		"""
		load the reference file and chromosomes
		"""
		if not os.path.isfile(self.ref):
			sys.stderr.write('FATAL ERROR {} NOT FOUND\n'.format(self.ref))
			sys.exit(1)
		with open(self.ref,'r') as f:
			for line in f:
				row = line.rstrip().split('\t')
				if len(row) != 2: row = line.rstrip().split(',')
				if len(row) != 2: 
					sts.stderr.write('FATAL ERROR {} BAD FORMAT!\nAccepted format: chrom,length OR chrom<tab>length\n'.format(line.rstrip()))
					sys.exit(1)
				if self.skip_x==True and 'X' in row[0]: continue
				if self.skip_y==True and 'Y' in row[0]: continue
				if self.skip_m==True and 'M' in row[0]: continue

				self.chrom.append(Chromosome(row))

	def make_axis(self):
		"""determine the positions of the chromosome labels"""
		pos=0
		for Chrom in self.chrom:
			Chrom.start=pos
			pos += Chrom.length
			Chrom.end=pos
			pos+=1
			self.labs.append(Chrom.label)
			self.tix.append(pos - int(Chrom.length/2.))
			self.chrom_dict[Chrom.label]=Chrom
		self.genome_end=pos

class Chromosome():
	def __init__(self,entry):
		self.length = int(entry[1])    #chromosome length
		self.label  = entry[0]    #chromosome name
		self.start,self.end = 0,0 #floating start and end for chromosome

def scatter(ax=plt.axes(),df=None, ref='hg38',
			chromA='chromA',posA='posA',
			chromB='chromB',posB='posB',
			fontsize=12, xrotation=0,
			remove_chr=False,bgcol='#bbbbbb',
			bgalpha=1.0,
			skip_x=False,skip_y=True,skip_m=True,
			**kwargs):
	"""
	scatter plot function
		chromA is the X axis, chromB is the Y axis
		posA is the position for X and vice-versa

		keyword arguments are passed to matplotlib.pyplot scatter
	"""

	Gen = Genome(ref,skip_x,skip_y,skip_m)
	X,Y = [],[] # X and Y positions
	# axis ticks
	ax.set_xticks(Gen.tix)
	ax.set_yticks(Gen.tix)
	# remove 'chr' prefix
	if remove_chr==True:
		Gen.labs = [x.replace('chr','') for x in Gen.labs]
		for Chrom in Gen.chrom:
			Gen.chrom_dict[str(Chrom.label.replace('chr',''))]=Chrom
	# axis labels
	ax.set_xticklabels(Gen.labs,fontsize=fontsize,rotation=xrotation)
	ax.set_yticklabels(Gen.labs,fontsize=fontsize)
	# background
	for ind,Chrom in enumerate(Gen.chrom):
		if ind % 2 == 1: ax.axvspan(xmin=Chrom.start,xmax=Chrom.end,color=bgcol,zorder=1,alpha=bgalpha)
	# plot points
	for ind,ele in df.iterrows():
		x_chrom, y_chrom = str(ele[chromA]),str(ele[chromB])
		x_pos = ele[posA]+Gen.chrom_dict[x_chrom].start
		y_pos = ele[posB]+Gen.chrom_dict[y_chrom].start
		X.append(x_pos)
		Y.append(y_pos)

	ax.scatter(x=X,y=Y,**kwargs)
	
	ax.set_xlim(0,Gen.genome_end)
	ax.set_ylim(0,Gen.genome_end)

	return ax

def get_path():
	"""function to get the root directory for genome files"""
	try:
		root = __file__
		if os.path.islink(root): root = os.path.realpath(root)
		return os.path.dirname(os.path.abspath(root))
	except:
		sys.stderr.write('FATAL ERROR {} NOT FOUND\n'.format(__file__))
		sys.exit(1)
