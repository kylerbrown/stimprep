#!/usr/bin/env python
from __future__ import division
from scipy.io import wavfile
from scipy.signal import filtfilt, bessel
import argparse
from numpy import int16, mean, sqrt, array, max, abs

__version__ = "0.1"


def sliding_rms(x, N):
    x = x.astype(float)
    return array([sqrt(mean(x[i:i+N]**2)) for i in range(0, len(x)-N)])


def rms_peak_ratio(x, N):
    return max(sliding_rms(x, N)) / max(abs(x))


def ms_to_samples(ms, sr):
    return int(ms/1000*sr)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Use a zero-phase Bessel filter to high \
    pass the data, normalize by peak RMS, optionally create reversed version.')
    parser.add_argument('file', help='name input file')
    parser.add_argument('-o', '--out', dest='ofile',
                        help='name of output file', default=None)
    parser.add_argument('-c', '--cutoff', type=float, dest='cutoff',
                        default=300, help='cutoff frequency')
    parser.add_argument('-N', '--order', type=int, dest='order',
                        default=3, help='Order of the filter')
    parser.add_argument("-v, --verbose", dest='verbose',
                        help="increase output verbosity",
                        action="store_true")
    parser.add_argument("--plot", dest='plot', help="visually verify computation",
                        action="store_true")
    defwin = 50
    parser.add_argument("--win",
                        help="length of RMS window, in milliseconds, default={}\
     changing is not recommended"
                        .format(defwin), default=defwin, type=float)
    parser.add_argument("--reverse", help="outputs a reverse file if also --out",
                        action="store_true")

    args = parser.parse_args()

    RMS_SCALING = 0.2

    if args.verbose:
        print('reading %s' % (args.file))
    rate, data = wavfile.read(args.file)
    N = ms_to_samples(args.win, rate)
    rms_ratio = rms_peak_ratio(data, N)
    if rms_ratio < RMS_SCALING:
        print("WARNING: RMS scaling clipped the output wav, \
        check output file. If this continues, reduce RMS_SCALING term \
        in the source")
    if args.verbose or True:
        print("rms to peak ratio: {}".format(rms_ratio))
    Wn = args.cutoff/(rate/2.)
    if args.verbose:
        print('sample rate\t%s\ncutoff\t%s\nWn\t%s' % (rate, args.cutoff, Wn))
    b, a = bessel(args.order, Wn, btype='highpass')
    filtered_data = filtfilt(b, a, data)
    writedata = int16(filtered_data / max(sliding_rms(filtered_data, N))
                      * 32767 * RMS_SCALING)
    if args.ofile:
        if args.verbose:
            print('saving filtered data in %s' % (args.ofile))
        wavfile.write(args.ofile, rate, writedata)
        if args.reverse:
            if args.verbose:
                print('saving filtered data in %s' % ('rev_' + args.ofile))
            wavfile.write('rev_' + args.ofile, rate, writedata[::-1])
    if args.plot:
        import matplotlib.pyplot as plt
        plt.subplot(221)
        plt.plot(data)
        plt.title('input')
        plt.subplot(223)
        plt.title('output')
        plt.plot(writedata)
        plt.plot(sliding_rms(writedata, N))
        plt.subplot(222)
        plt.psd(data, Fs=rate, NFFT=512)
        plt.subplot(224)
        plt.psd(writedata, Fs=rate, NFFT=512)
        plt.show()
    if args.verbose:
        print('done')
