# pynome
---------------------------

Make Genome Plots in Python

---------------------------

## Functions

* [`scatter()`](#scatter)

### scatter

```
pynome.scatter(ax, df, ref
		chromA, posA,
		chromB, posB,
		fontsize, xrotation,
		remove_chr, bgcol, bgalpha,
		skip_x, skip_y, skip_m,
		**kwargs
		)
```

#### `pynome.scatter()` Arguments

* ax: matplotlib.pyplot axes object 
  * default: `matplotlib.pyplot.axes()`

* df: Pandas DataFrame object

* ref: string of reference build or the path to a genome file
  * accepted strings: `hg38, b37, hg19, hg18, mm10, mm9, mm8`
  * genome file must be either tab or comma separated. formatted as `chromosome name,physical length in base pairs`
  
  * default: `hg38`

* chromA, posA: the DataFrame column name for the chromosome and physical position for the X axis
  * default: `chromA`, `posA`

* chromB, posB: the DataFrame column name for the chromosome and physical position for the Y axis
  * default: `chromB`, `posB`

* fontsize: integer font size for the X and Y axis labels
  * default: `12`

* xrotation: degrees to rotate the X axis labels
  * default: `0`

* remove_chr: boolean to remove the 'chr' prefix in chromosome names
  * default: `False`

* bgcol: background color for alternating chromosomes
  * default: `#bbbbbb`

* bgalpha: background transparency
  * default: `1.0`

* skip_x, skip_y, skip_m: booleans to remove chrX, chrY, and chrM respectively 
  * default: `False`, `True`, `True`

* `kwargs`: other keyword arguments are passed directly to `matplotlib.pyplot.scatter()`

--------------------------------- 
