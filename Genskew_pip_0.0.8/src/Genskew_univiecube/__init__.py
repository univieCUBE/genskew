import math
import argparse
import matplotlib.pyplot as plt
import sys
from Bio import SeqIO
from collections import namedtuple
import os
import gzip
import shutil


class NoValidFile(Exception):
    pass


class Object:
    def __init__(self, sequence, nuc_1, nuc_2, stepsize=None, windowsize=None):
        self.stepsize = stepsize if stepsize is not None else None
        self.windowsize = windowsize if windowsize is not None else None
        self.sequence = sequence
        self.nuc_1 = nuc_1
        self.nuc_2 = nuc_2

    def gen_stepsize(self):
        stepsize = int(len(self.sequence) / 1000)
        if stepsize < 100:
            stepsize = 100
        return stepsize

    def gen_windowsize(self):
        windowsize = int(len(self.sequence) / 1000)
        if windowsize < 100:
            windowsize = 100
        return windowsize

    def gen_results(self):
        if not self.stepsize:
            self.stepsize = self.gen_stepsize()
            if self.stepsize < 100:
                self.stepsize = 100
        if not self.windowsize:
            self.windowsize = self.gen_windowsize()
            if self.windowsize < 100:
                self.windowsize = 100
        x = []
        y1 = []
        y2 = []
        y2_scaled = []
        cumulative_unscaled = 0
        cm_list = []
        i = int(self.windowsize / 2)
        for each in range(math.ceil(len(self.sequence) / self.stepsize)):
            if i < len(self.sequence):
                a = self.sequence[i - int(self.windowsize / 2):i + int(self.windowsize / 2)].count(self.nuc_1)
                b = self.sequence[i - int(self.windowsize / 2):i + int(self.windowsize / 2)].count(self.nuc_2)
                skew = (a - b) / (a + b)
                y1.append(skew)
                cumulative_unscaled = cumulative_unscaled + skew
                y2.append(cumulative_unscaled)
                x.append(i + 1)
                cm_list.append(cumulative_unscaled)
                i = i + self.stepsize
        cm = max(cm_list)
        m = max(y1)
        scale = m / cm
        max_position = y2.index(max(y2)) * self.stepsize
        min_position = y2.index(min(y2)) * self.stepsize
        for j in cm_list:
            y2_scaled.append(j * scale)
        results = namedtuple("results",
                             ['x', 'skew', 'cumulative', 'cumulative_unscaled', 'max_cumulative', 'min_cumulative',
                              'max_cm_position', 'min_cm_position', 'stepsize', 'windowsize', 'nuc_1', 'nuc_2'])
        return results(x, y1, y2_scaled, cm_list, max(y2), min(y2), max_position, min_position, self.stepsize,
                       self.windowsize,
                       self.nuc_1, self.nuc_2)


def input_files(file_location_list):
    is_directory = False
    c = 0
    file_location_processed = []
    file_types = ['fasta', 'gb']
    for file_location in file_location_list:
        if os.path.isdir(file_location):
            # os.scandir anstatt listdir
            for entry in os.listdir(file_location):
                if os.path.isfile(os.path.join(file_location, entry)):
                    is_directory = True
                    if os.path.join(file_location, entry).split('.')[-1] in file_types:
                        file_location_processed.append(os.path.join(file_location, entry))
                    if os.path.join(file_location, entry).split('.')[-1] == 'gz':
                        if os.path.join(file_location, entry).split('.')[-2] in file_types:
                            file_location_processed.append(os.path.join(file_location, entry))
        if not is_directory:
            if file_location.split('.')[-1] in file_types:
                file_location_processed.append(file_location)
            if file_location.split('.')[-1] == 'gz':
                if file_location.split('.')[-2] in file_types:
                    file_location_processed.append(file_location)
        is_directory = False
        c = c + 1
    if len(file_location_processed) == 0:
        raise NoValidFile('your input did not contain any valid fasta or gb files')
    return file_location_processed


def gen_sequence(file_location):
    path, file = os.path.split(file_location)
    if file.split('.')[-1] == 'gz':
        file_type = file.split('.')[-2]
        sequence = ''.join(
            [str(elem) for elem in
             [seq_record.seq for seq_record in SeqIO.parse(gzip.open(file_location, "rt"), file_type)]])
    else:
        file_type = file.split('.')[-1]
        with open(file_location) as handle:
            sequence = ''.join(
                [str(elem) for elem in [seq_record.seq for seq_record in SeqIO.parse(handle, file_type)]])
    if len(sequence) == sequence.count("N"):
        sys.exit("There seems to be no sequence in your file!")
    return sequence


def plot_sequence(results, filelocation, outputfolder=None, out_file_type=None, dpi=None):
    path, file = os.path.split(filelocation)
    if file.split('.')[-1] == 'gz':
        file_type = file.split('.')[-2]
    else:
        file_type = file.split('.')[-1]
    if not outputfolder:
        outputfolder = path
    if not out_file_type:
        out_file_type = 'png'
    fig, ax = plt.subplots()
    # plotting the graph
    ax.plot(results.x, results.skew, color="blue", linewidth=0.3)
    ax.plot(results.x, results.cumulative, color="red", linewidth=0.3)
    ax.axvline(x=int(results.max_cm_position), color="green", linewidth=0.3,
               label="maximum, at " + str(results.max_cm_position))
    ax.axvline(x=int(results.min_cm_position), color="green", linewidth=0.3,
               label="minimum, at " + str(results.min_cm_position))
    ax.set_title("Gen-skew plot for sequence: " + file + ", with stepsize: " + str(
        results.stepsize) + " and windowsize: " + str(results.windowsize))
    ax.set_xlabel("position in sequence")
    ax.set_ylabel(results.nuc_1 + " " + results.nuc_2 + " skew")
    ax.grid(b=None, which='major', axis='both')
    ax.ticklabel_format(axis='x', style='plain')
    ax.legend()
    fig.savefig(
        os.path.join(outputfolder,
                     file.replace("." + file_type, "") + results.nuc_1 + results.nuc_2 + "skew." + out_file_type),
        bbox_inches='tight', dpi=dpi)
