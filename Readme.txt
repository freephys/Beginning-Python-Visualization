Accompanying source code for the book
"Beginning Python Visualization
Crafting Visual Transformation Scripts"
ISBN 978-1-4302-1843-2
Apress
Author: Shai Vaingast, February 2009

The following files are source listings of most of the code in the book.
Some code listings require additional data files which should be downloaded separately; consult with the text in the book as to where to obtain the data files.
The directory structure follows the structure presented in the book.  See chapter 2 for a full account.

Details listings:

Chapter 1
---------

Directory src:
gps.py              A script to draw a GPS plot including annotation (the final example in the chapter)
list_commands.py    A function that counts the number of times a GPS command is observed
record_gps.py       A script to record GPS data.  Be sure to change the serial port settings to match yours.
scanport.py         A script to list active COM ports.

Directory data:
GPS-2008-05-30-09-00-50.csv A sample GPS data file.

Chapter 2
---------
No source listings in this chapter.

Chapter 3
---------

Directory src:
genodd.py           Several function implementations of the function odd.
odd.py              The Odd class.

Chapter 4
---------

Directory src:
cmp_fd.py           A script to compare three different algorithms to search for duplicate files.  The script also includes the definition of the function get_all_files() that retrieves the names of all the files in a folder, recursively, including path, name and size.  Be sure to change the variable srchpath to point to a directory of your choosing.
create_catalog.py   A script to create a catalog of files with extension "py".
get_all_files.py    A function to retrieve all the files in a folder, recursively, including path, name and size.
read_ini.py         A script to read INI (ConfigParser) files.
read_write_structs.py   A script to read structure of binary data.
running_index.py    A script to create unique filenames using a running index.
stock_charts.py     A script to plot Yahoo! stock charts data.  Requires downloading the file charts.xls, refer to the example in the book.
unique.py           A script to create unique filenames based on title, date and time stamp and an extension.
write_ini.py        A script to write INI (ConfigParser) files.
yahoo_data.py       A script to automatically retrieve and plot Yahoo! financial data.  Will create an image file in directory data.

Directory data:
Must exist for some of the scripts to run.

Chapter 5
---------

Directory src:
base_conversion.py  Base conversion helper functions.
combine_epoch.py    A script to combine data based on the epoch.
end-of-day.py       A script implementing an end-of-day report.
head_large.py       A function implementing head functionality for very large files.
head_tail.py        Function implementations of head and tail functionality.
hebrew.py           The Hebrew alphabet.
increment_contents.py   A script to increments the numeric values in a file.
locale_date.py      A script to write today's date in a different locale.
nonce.py            A function to find words only used once in a file.
split_combine.py    Functions to split files into smaller chunks and combine the chunks back to form the original file.
srchcomments.py     A function to search inside Python source comments.
srchfile.py         Functions to search for text inside a file.
testbases.py        A function to test the implementation of the base conversion functions (see base_conversion.py)
wc.py               A function that returns the number of characters, words and lines in a file.
wc_large.py         A function that returns the number of characters, words and lines in a large file.
word_line_count.py  A function that returns the number of words and the numbers of lines in a string.
writelog.py         A script to create a log file.

Directory data:
SystemALogs.txt     Data file for end-of-day.py script.
SystemBLogs.txt     Data file for combine_epoch.py script.
SystemCLogs.txt     Data file for combine_epoch.py script.


Chapter 6
---------

Directory src:
arrows.py           Arrows patch example.
gdp_bar.py          A bar chart.  Requires world factbook file, see Chapter 6 for details.
gdp_hist.py         A histogram.  Requires world factbook file, see Chapter 6 for details.
gdp_pie.py          A pie chart.  Requires world factbook file, see Chapter 6 for details.
logplot.py          A logarithmic plot.
number_subplots.py  Numbers the subplots in a figure.
patches.py          Matplotlib patches example.
polarplot.py        A polar plot.
quivplot.py         A quiver plot.
read_world_data.py  A function to read and parse world data.  Requires world factbook file, see Chapter 6 for details.
subplots.py         A subplot example.
summary_plot.py     A summary plot.
specplot.py         A specgram plot.

Chapter 7
---------

Directory src:
fourier_expansion.py    A Fourier expansion graph.
fractal.py          A fractal implementation.
friends.py          Friends meeting visualization.
magicsq.py          Returns a magic square of size n; n must be odd.
ndflat.py           An example showing n dimension array usage (comparing mortgage example)

Directory images:
Must exist for the fractal scripts to work properly.

Chapter 8
---------

Directory src:
exponential.py      Fitting exponential data.
detect.py           Signal detection in noise example.
filter_design.py    Filter design example.
int_circle.py       Integrating half a circle.
int_spline.py       Spline interpolation.
int_trapz.py        Trapezoidal integration.
hr_sim.py           Heart rate simulation.
linear.py           Linear regression.
moving_average.py   Filtering using a moving average.
windowing.py        A signal with a Hamming window.

Chapter 9
---------

Directory src:
convert_all_to_jpeg.py  A function to convert all images in a directory to JPG format.
convert_to_jpeg.py  A function to convert an image file to a JPG file.
flood_fill.py       Flood fill function implementation.
fractal_collage.py  A fractal collage, requires fractal_func.py.
fractal_func.py     A function to generate fractal images.
image_catalog.py    Creates a catalog file named srchpath.cat.csv.
nightsky.py         Creates a fictitious night sky.
process_stars.py    Counts the number of stars.  Run script nightsky.py first.
rotate.py           Rotate example.
star_examples.py    Show case some star patch examples.
star_patch.py       Two implementations of star patches.
text_annotation.py  A text annotation example.
thumb_catalog.py    A function that implements a thumbnail index.

Directory images:
Must exist for the some of the examples to work properly.

Chapter 10
----------

Directory src:
binary_time.py      Creates a binary epoch time based file.
cmp_dirs.py         Compare directory contents.  Uses files generated by script compression.py.
cmp_files.py        Compare files.
combine_epoch.py    A command line script to combine several files based on the epoch.  Example: python combine_epoch.py ../../Ch5/data/SystemBLogs.txt ../../Ch5/data/SystemCLogs.txt (in Windows, replace '/' with '\')
compression.py      Archiving and compression example.
empty_file.py       A stand-alone script to create an empty file of arbitrary size.
empty_opt.py        A stand-alone script to create an empty file of arbitrary size using OptionParser module.
extract.py          Extracting all files from a compressed archive.  Uses files generated by script compression.py.
extract3.py         Extracting select files from a compressed archive.  Uses files generated by script compression.py.
parse_args.py       Parsing command line arguments.
pickle_dump.py      Pickling variables.
pickle_load.py      Loading pickled variables.  Uses the output file generated by script pickle_dump.py.
read_bin_time.py    Reading an epoch based binary data file.  Uses the output generated by script binary_time.py
seek_tell.py        Seek and tell example.
srchfiles.py        A stand-alone script to search for strings in multiple files.
tail_large.py       Tail functionality for very large files.

Directory data:
Must exist for some of the scripts to run.

Appendix
--------

Directory src:
magicsq_arrows.py   Visualization of magic square creation.
nudge_subplot.py    Nudging subplots.
nudge_subplot_old.py    Nudging subplots (older version of matplotlib).
For function fractal_func.py, see Chapter 9.

