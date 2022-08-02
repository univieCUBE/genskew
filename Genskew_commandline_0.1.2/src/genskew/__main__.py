import Genskew_univiecube as gs
import argparse
import matplotlib.pyplot as plt


def check_size(value):
    ivalue = int(value)
    if ivalue <= 100:
        ivalue = 100
    return ivalue


def check_upper(value):
    return str(value).upper()


parser = argparse.ArgumentParser(
    description='This program calculates the nucleotide skew of a given genome. You can use it by calling python3 -m genskew and then using the arguments displayed here. Every Argument with * is required. If the '
                'stepsize or windowsize are too small, they will be set to 100. For multiple inputs separate the file '
                'locations by a space or input a folder name. If multiple sequences are processed, specifying '
                'stepsize and windowsize can lead to issues.  The following input file types are supported: genbank ('
                'gb or gbk) and fasta. They can also be .gz files. The following output file types are supported: {0}.'.format(
                str(plt.gcf().canvas.get_supported_filetypes()).replace("{", "").replace("}", "").replace(
                     ":", "").replace("'", "")))
# automatische file erkennung + embl

parser.add_argument('file_location', metavar='FL', type=str,
                    help='*the location of the file', nargs="+")
parser.add_argument('--stepsize', '-s', default=None, metavar='S', type=check_size,
                    help='the stepsize, has to be above 100 (default is calculated by the length of the genome)')
parser.add_argument('--windowsize', '-w', default=None, metavar='W', type=check_size,
                    help='the windowsize, has to be above 100 (default is calculated by the length of the genome)')
parser.add_argument('--out_file_type', '-o', choices=plt.gcf().canvas.get_supported_filetypes(),#
                    default='png', metavar='O', type=str,
                    help='the filetype in which the graph should be created (default: png)')
parser.add_argument('--nuc_1', '-n1', metavar='N', default='G', choices=['a', 'A', 'c', 'C', 'g', 'G', 't', 'T'],
                    type=check_upper, help='the first nucleotide (has to be A, C, G or T)')
parser.add_argument('--nuc_2', '-n2', metavar='N', default='C', choices=['a', 'A', 'c', 'C', 'g', 'G', 't', 'T'],
                    type=check_upper, help='the second nucleotide (has to be A, C, G or T)')
parser.add_argument('--dpi', '-d', type=int,
                    help='the resolution of the output file')
parser.add_argument('--output_folder', '-of', type=str, default=None,
                    help='the folder the graphs should be saved to')
parser.add_argument('--skewIT', '-sk',
                    help='The skewIT algorithm will be used for the graph. Use -sk true to activate this feature.')

args = parser.parse_args()

inputfiles = gs.input_files(args.file_location)
# defining the sequence
sequence_list = []
for file in inputfiles:
    sequence1 = gs.gen_sequence(file)
    sequence_list.append(sequence1)
# making an object
a = 0
variable_list = []
results_list = []
skewi = False
if args.skewIT != None:
    skewi = True
for sequence in sequence_list:
    variable_list.append('genskew' + str(a))
    results_list.append('result' + str(a))
    variable_list[a] = gs.Object(sequence, args.nuc_1, args.nuc_2, args.stepsize, args.windowsize)
    results_list[a] = gs.Object.gen_results(variable_list[a])
    print(str(a + 1) + " out of " + str(len(sequence_list)) + " graphs calculated...")
    gs.plot_sequence(results_list[a], inputfiles[a], args.output_folder, args.out_file_type, args.dpi, skewi)
    print(str(a + 1) + " out of " + str(len(sequence_list)) + " graphs saved...")
    a = a + 1
print('Done!')
# /home/julius/Downloads/sequence.fasta
