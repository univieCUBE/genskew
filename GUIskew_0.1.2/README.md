This is the GUI for Genskew_univiecube, which will automatically be installed when installing Genskew_univiecube.

If you need anything beyond this description or the windows executable, take a look at the website: genskew.csb.univie.ac.at/guiskew

In order to use this program, tkinter HAS to be installed. It should come preinstalled with python, but if not use the command apt-get install python-tk for Debian-based systems.

GenSkew is an application for computing and plotting nucleotide skew data.

GenSkew calculates the incremental and the cumulative skew of two selectable nucleotides for a given sequence according to this formula:
Skew = (nucleotide1 - nucleotide2) / (nucleotide1 + nucleotide2)

The results are provided as data table and as graphical plot. The global minimum and maximum are displayed in the cumulative graph. The minimum and maximum of a GC-skew can be used to predict the origin of replication (minimum) and the terminus location (maximum) in prokaryotic genomes.

There are three versions of this Program: Genskew_univiecube (the python library described below), Genskew_cc (a commandline client) and GUIskew (the Graphical Version of Genskew). 

Installing the program with the command you can copy above will install all three of them. By calling python3 -m genskew -h you will see a detailed description how to use the commandline interface. It can analyze multiple sequences in one command.

The graphical version of Genskew is started by the command python -m GUIskew. When pressing on the "Browse" button, you can select the sequence you want to use. With the two drop-down menus you can select the two nucleotides. Stepsize and windowsize can be left out, in which case they will be calculated by the program. The last drop down menu selects the file type in which you will save the Graph. Pressing calculate will display the graph in the window, but not save it. Calculate will only work for singular sequences, when multiple sequences are selected it will not display anything.

By using the dropdown-menu on the top right, you can select between Genskew and SkewIT¹. This will change how the graph looks.

The use of the library is explained in detail on the pipy site of Genskew_univiecube.

Updatelog GUIskew

Version 0.1.2

fixed the SkewIT graph sometimes not displaying the right nucleotide on the axis label

Version 0.1.1

Updated readme

added references

Version 0.1.0

Added the SkewIT¹ algorithm to GUIskew

Added new Dropdown Menu on the far top right, with the values GenSkew and SkewIT.

Version 0.0.4

first finnished release of GUIskew
	
REFERENCES:

1: SkewIT, https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1008439 (06.04.2022), SkewIT: The Skew Index Test for large scale GC Skew analysis of bacterial genomes, Jennifer Lu, Steven L. Salzberg
