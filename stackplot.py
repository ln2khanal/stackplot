
import matplotlib.pylab as plt
import numpy as np
import glob
import random
import sys

COLOR_SET = [
    "k",
    "y",
    "r"
]

BASE_DIR = ""


def initialize_plot():
    """
    initializes the plot
    :return: None 
    """
    font = {
        'family': 'Times New Roman',
        'weight': 'bold',
        'size': 10
    }

    plt.rc('font', **font)
    plt.rc('xtick', labelsize=16)
    plt.rc('ytick', labelsize=16)

    plt.rcParams['axes.linewidth'] = 2


def get_filename_from_file_path(file_path):
    """
    returns file name if file_path includes it    
    :param file_path: file path
    :return: file name, string
    """
    directory_filename = str(file_path).rsplit('/', 1)
    if len(directory_filename) == 2:
        file_name = directory_filename[1].replace('.xy', '')
    else:
        file_name = file_path
    return file_name


def read_target_files():
    """
    reads a directory and returns all the files matching a pattern
    :return: list
    """
    return glob.glob("%s/*.xy" % BASE_DIR)


def get_subplots(count):
    """
    initializes the plot
    :return: None
    """
    f, sub_plots = plt.subplots(int(count), sharex=True, sharey=True)
    f.text(0.5, 0.02, 'Angle, $2\Theta$', ha='center', va='center', fontsize=18)
    f.text(0.09, 0.5, 'Intensity, Counts', ha='center', va='center', rotation='vertical', fontsize=18)

    return sub_plots


def arrange_plots(sub_plot, file_path):
    """
    arranges the plot
    :return: None
    """
    file_name = get_filename_from_file_path(file_path)
    np_object_from_text = np.genfromtxt(file_path, delimiter='', skip_header=2, skip_footer=0)
    t = np_object_from_text[:, 0]
    np_object_from_text = np_object_from_text[:, 1]
    sub_plot.plot(t, np_object_from_text, label=file_name, color=COLOR_SET[random.randint(0, len(COLOR_SET) - 1)])
    sub_plot.legend(loc='upper right')
    sub_plot.grid()


def show_plot():
    """
    plots the plot
    :return: None
    """
    plt.show()


def main():
    print 'reading target directory=%s' % BASE_DIR
    file_list = read_target_files()

    print 'initializing plot'
    initialize_plot()

    file_count = len(file_list)
    if file_count == 0:
        print "worthless zero subplots, exiting now!"
        sys.exit(1)

    print 'generating subplots'
    sub_plots = get_subplots(file_count)

    print 'arranging the plots one by one'
    for index, sub_plot in enumerate(sub_plots):
        print 'Working with file=%s' % file_list[index]
        arrange_plots(sub_plot, file_list[index])

    print 'showing the results'
    show_plot()


if __name__ == "__main__":
    main()
