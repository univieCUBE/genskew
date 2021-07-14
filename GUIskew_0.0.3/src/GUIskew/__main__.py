from tkinter import *
import tkinter as tk
import Genskew_univiecube as gs
from tkinter.filedialog import askopenfilename
from tkinter import filedialog as fd
from tkinter.ttk import Combobox
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler

# noch  zu tun: größe des grund fensters umändern(wirklich notwendig?)
window = Tk()
global filenames
global output_folder


# functions that controll what the Buttons do
def save():
    global filenames
    global output_folder
    output_folder = fd.askdirectory()
    out_filetype = file_type_box.get()
    nuc_1 = nuc_1_box.get()
    nuc_2 = nuc_2_box.get()
    try:
        stepsize = int(stepsize_input.get())
        if stepsize < 100:
            stepsize = 100
    except:
        stepsize = None

    try:
        windowsize = int(windowsize_input.get())
        if windowsize < 100:
            windowsize = 100
    except:
        windowsize = None

    try:
        sequence_list = []
        for file in filenames:
            sequence1 = gs.gen_sequence(file)
            sequence_list.append(sequence1)
        # making an object
        a = 0
        variable_list = []
        results_list = []
        for sequence in sequence_list:
            dpi = None
            variable_list.append('genskew' + str(a))
            results_list.append('result' + str(a))
            variable_list[a] = gs.Object(sequence, nuc_1, nuc_2, stepsize, windowsize)
            results_list[a] = gs.Object.gen_results(variable_list[a])
            print(str(a + 1) + " out of " + str(len(sequence_list)) + " graphs calculated...")
            gs.plot_sequence(results_list[a], filenames[a], output_folder, out_filetype, dpi)
            print(str(a + 1) + " out of " + str(len(sequence_list)) + " graphs saved...")
            a = a + 1
    except:
        lbel.configure(text='Something went wrong, maybe your file is faulty or empty?')


def browse():
    global filenames
    filenames = fd.askopenfilenames(filetypes=[('Fasta files','*.fasta'), ('genbank files','*.gb'), ('Gzip files', '*.gz')])
    files = []
    for file in filenames:
        if len(filenames) > 1:
            files.append(file.split('/')[-1] + ',')
        else:
            files.append(file.split('/')[-1])
    label.configure(text=files)
    lbel.configure(text='')


def calculate():
    global filenames
    if len(filenames) == 1:
        nuc_1 = nuc_1_box.get()
        nuc_2 = nuc_2_box.get()
        if 1 == 1:
            sequence = gs.gen_sequence(filenames[0])
            try:
                stepsize = int(stepsize_input.get())
                if stepsize < 100:
                    stepsize = 100
            except:
                stepsize = None

            try:
                windowsize = int(windowsize_input.get())
                if windowsize < 100:
                    windowsize = 100
            except:
                windowsize = None
            # calculating and displaying the figure
            skew_calculation = gs.Object(sequence, nuc_1, nuc_2, stepsize, windowsize)
            results = gs.Object.gen_results(skew_calculation)
            fig = Figure(figsize=(9, 6), facecolor="white")
            axis = fig.add_subplot(111)
            axis.plot(results.x, results.skew, color="blue", linewidth=0.3)
            axis.plot(results.x, results.cumulative, color="red", linewidth=0.3)
            axis.axvline(x=int(results.max_cm_position), color="green", linewidth=0.3,
                         label="maximum, at " + str(results.max_cm_position))
            axis.axvline(x=int(results.min_cm_position), color="green", linewidth=0.3,
                         label="minimum, at " + str(results.min_cm_position))
            axis.set_title("Gen-skew plot for sequence: " + filenames[0].split('/')[-1] + ", with stepsize: " + str(
                # + q_variables[b].description
                results.stepsize) + " and windowsize: " + str(results.windowsize))
            axis.set_xlabel("position in sequence")
            axis.set_ylabel(results.nuc_1 + " " + results.nuc_2 + " skew")
            axis.grid(b=None, which='major', axis='both')
            axis.ticklabel_format(axis='x', style='plain')
            axis.legend()

# das Problem liegt hier
            canvas = FigureCanvasTkAgg(fig, master=window)  # A tk.DrawingArea.
            canvas.draw()
            canvas.get_tk_widget().grid(column=0, row=2, columnspan=8)
        #except:
        #    lbel.configure(text='Something went wrong, maybe your file is faulty or empty?')


# Widgets in the tk window
window.title("GUIskew")

Browse_btn = Button(window, text="Browse", command=browse)
Browse_btn.grid(column=0, row=0)

nuc_1_box = Combobox(window)
nuc_1_box['values'] = ("A", "C", "G", "T")
nuc_1_box.current(2)
nuc_1_box.grid(column=1, row=0)

nuc_2_box = Combobox(window)
nuc_2_box['values'] = ("A", "C", "G", "T")
nuc_2_box.current(1)
nuc_2_box.grid(column=2, row=0)

lbl = Label(window, text=" Stepsize, Windowsize:")
lbl.grid(column=3, row=0)

stepsize_input = Entry(window, width=10)
stepsize_input.grid(column=4, row=0)

windowsize_input = Entry(window, width=10)
windowsize_input.grid(column=5, row=0)

file_type_box = Combobox(window)
file_type_box['values'] = ("jpg", "png",)
file_type_box.current(0)
file_type_box.grid(column=6, row=0)


label = Label(window, text='')
label.grid(column=0, row=1, columnspan=6)

calculate_btn = Button(window, text="View", command=calculate)
calculate_btn.grid(column=6, row=1)

lbel = Label(window, text='')
lbel.grid(column=0, row=3, columnspan=5)

save_btn = Button(window, text="Save", bg="green", command=save)
save_btn.grid(column=6, row=3)

window.mainloop()
