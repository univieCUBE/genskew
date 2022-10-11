# genskew
Genskew is an application for computing and plotting nucleotide skew data.

GenSkew calculates the incremental and the cumulative skew of two selectable nucleotides for a given sequence according to this formula: Skew = (nucleotide1 - nucleotide2) / (nucleotide1 + nucleotide2)

The results are provided as data table and as graphical plot. The global minimum and maximum are displayed in the cumulative graph. The minimum and maximum of a GC-skew can be used to predict the origin of replication (minimum) and the terminus location (maximum) in prokaryotic genomes.

There are four versions of this Program: Genskew_univiecube (the python library), Genskew_cc (a commandline client), GUIskew (the graphical version of genskew) and Webskew (the online version). 

The first three Versions can be found on pipy, where the usage is explained in more detail. The last version, webskew, is the online version of genskew and can be found on the genskew website, which is currently not yet availabe.

To build this yourself, just download the respective directories and run the python build command python3 -m build
