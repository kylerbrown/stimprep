stimprep
========

Prepare audio files for stimulus presentation.

This script provides funtionality for two things:

1. Removing fan/ambient noise from cage recordings with a high pass filter
2. Normalizing the volume of all sounds. This script scales every sound such the maximum value of a moving RMS window is constant. There are other ways to normalize volume, but this is the method implemented here.
3. (optional) provide an identical but reversed copy of the sound.

The input for the script is a single channel WAV file. The parameters for filtering and volume normalization are adjustable via command-line parameters.


Install
-----------
Simplest method:
+ install [anaconda](https://store.continuum.io/cshop/anaconda/).
+ clone this repository and enter project directory, eg `git clone https://github.com/kylerbrown/stimprep.git; cd stimprep`
+ run `python setup.py install`


Alternately:

    pip install numpy scipy matplotlib
	git clone https://github.com/kylerbrown/stimprep.git
	cd stimprep
	python setup.py install


Usage
-------

Type `stimprep.py` to run. `stimprep.py -h` gives usage help.

    usage: stimprep.py [-h] [-o OFILE] [-c CUTOFF] [-N ORDER] [-v, --verbose]
                   [--plot] [--win WIN] [--reverse]
                   file
    Use a zero-phase Butterworth filter to high pass the data.
    positional arguments:
      file                  name input file
    optional arguments:
      -h, --help            show this help message and exit
      -o OFILE, --out OFILE
                            name of output file
      -c CUTOFF, --cutoff CUTOFF
                            cutoff frequency
      -N ORDER, --order ORDER
                            Order of the filter
      -v, --verbose         increase output verbosity
      --plot                visually verify computation
      --win WIN             length of RMS window, in milliseconds, default=50
                            changing is not recommended
      --reverse             outputs a reverse file if also --out
