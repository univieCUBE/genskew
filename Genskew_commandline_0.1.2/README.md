This is the commandline client for Genskew_univiecube, which will automatically be installed when installing Genskew_univiecube.

For the online version of genskew and a more detailed description, please visit the website: genskew.csb.univie.ac.at/genskew_cc

GenSkew is an application for computing and plotting nucleotide skew data.

GenSkew calculates the incremental and the cumulative skew of two selectable nucleotides for a given sequence according to this formula:
Skew = (nucleotide1 - nucleotide2) / (nucleotide1 + nucleotide2)

The results are provided as data table and as graphical plot. The global minimum and maximum are displayed in the cumulative graph. The minimum and maximum of a GC-skew can be used to predict the origin of replication (minimum) and the terminus location (maximum) in prokaryotic genomes.

There are three versions of this Program: Genskew_univiecube (the python library described below), Genskew_cc (a commandline client) and GUIskew (the Graphical Version of Genskew). 

Installing the program with the command you can copy above will install all three of them. By calling python3 -m genskew -h you will see a detailed description how to use the commandline client. It can analyze multiple sequences in one command.

The graphical version of Genskew is started by the command python -m GUIskew. When pressing on the "Browse" button, you can select the sequence you want to use. With the two drop-down menus you can select the two nucleotides. Stepsize and windowsize can be left out, in which case they will be calculated by the program. The last drop down menu selects the file type in which you will save the Graph. Pressing calculate will display the graph in the window, but not save it. Calculate will only work for singular sequences, when multiple sequences are selected it will not display anything.

The use of the library is explained in detail on the pipy site of Genskew_univiecube.

Updatelog GenSkew_commandline

Version 0.1.2:

Added references to readme

Version 0.1.1:

General bug fix

Version 0.1.0:

Added the SkewIT¹ algorithm to GenSkew_cc.

Added a new parameter: --skewIT or -sk which, if set to "true", activates the SkewIT algorithm.

Version 0.0.5:

First finnished release of GenSkew_cc

REFERENCES:
1: SkewIT, https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1008439 (06.04.2022), SkewIT: The Skew Index Test for large scale GC Skew analysis of bacterial genomes, Jennifer Lu, Steven L. Salzberg
