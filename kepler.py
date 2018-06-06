#TrueFalse
import csv
import matplotlib
import numpy
import scipy
import pprint

from matplotlib import pyplot
from scipy.optimize import curve_fit


def main():
    '''Call functions'''
    filename = "planets.csv"
    scatter_plot(filename)
    fit_data(filename)
    filename = "solarsystem.csv"
    fit_solar_system(filename)
    filename = "asteroids.csv"
    fit_asteroids(filename)
    filename = "positions.csv"
    sky_positions(filename)


def scatter_plot(filename):
    '''Read file, make a scatterplot and plot a expected line'''
    with open(filename, 'rb') as csvfile:
        datareader = csv.reader(csvfile, delimiter=',', quotechar='|')
        data = []
        for line in datareader:
            if line[0].startswith('#'):
                continue
            if line[0].startswith('r'):
                continue
            if len(line[2]) == 0 or len(line[3]) == 0:
                continue
            ax = float(line[2])
            pe = float(line[3])
            t = (ax, pe,)
            data.append(t)

    axis = [x[1] for x in data]
    period = [x[0] for x in data]

    axis_val = numpy.linspace(1e-3, 1e3, 50)
    const = 1e5
    period_val =  numpy.sqrt(const*(axis_val**3))

    pyplot.xscale('log')
    pyplot.yscale('log')
    pyplot.xlim(1e-3, 1e3)
    pyplot.ylim(1e-2, 1e6)
    pyplot.scatter(axis, period, color='k', marker='+', label='Exoplanets')
    pyplot.plot(axis_val, period_val)
    pyplot.legend()
    pyplot.title('Kepler exoplanets')
    pyplot.xlabel('Semi-major axis [AU]')
    pyplot.ylabel('Period [Days]')
    pyplot.savefig('kepler.pdf')
    pyplot.show()


def read_data(filename):
    '''Read data'''
    with open(filename, 'rb') as csvfile:
        datareader = csv.reader(csvfile, delimiter=',', quotechar='|')
        data = []
        for line in datareader:
            if line[0].startswith('#'):
                continue
            if line[0].startswith('r'):
                continue
            if len(line[2]) == 0 or len(line[3]) == 0:
                continue
            ax = float(line[2])
            pe = float(line[3])
            t = (ax, pe,)
            data.append(t)
    return data


def read_datas(filename, discovery_method):
    '''Read data by discovery method '''
    with open(filename, 'rb') as csvfile:
        datareader = csv.reader(csvfile, delimiter=',', quotechar='|')
        data = []
        for line in datareader:
            if line[0].startswith('#'):
                continue
            if line[0].startswith('r'):
                continue
            if len(line[2]) == 0 or len(line[3]) == 0:
                continue
            if line[1].startswith(discovery_method):
                a = float(line[2])
                p = float(line[3])
                t = (a, p,)
                data.append(t)
    return data



def fit_data(filename):
    ''' Plot fitted line, plot data sorting by discovery method '''
    data = read_data(filename)
    axis = [x[1] for x in data]
    period = [x[0] for x in data]
    axis_log = numpy.log10(axis)
    period_log = numpy.log10(period)

    def func(x, a, b):
        ''' Linear function for fitting'''
        return b + (a * x)
    popt, pcov = curve_fit(func, axis_log, period_log)

    axis_val = numpy.linspace(-3, 3, 50)
    aa = popt[0]
    bb = popt[1]
    period_val = bb + (aa * axis_val)
    axis_val_exp = 10**axis_val
    period_val_exp = 10**period_val

    discovery_method = 'As'
    data_as = read_datas(filename, discovery_method)
    axis_as = [x[1] for x in data_as]
    period_as = [x[0] for x in data_as]
    discovery_method = 'Ec'
    data_ec = read_datas(filename, discovery_method)
    axis_ec = [x[1] for x in data_ec]
    period_ec = [x[0] for x in data_ec]
    discovery_method = 'Im'
    data_im = read_datas(filename, discovery_method)
    axis_im = [x[1] for x in data_im]
    period_im = [x[0] for x in data_im]
    discovery_method = 'Mi'
    data_mi = read_datas(filename, discovery_method)
    axis_mi = [x[1] for x in data_mi]
    period_mi = [x[0] for x in data_mi]
    discovery_method = 'Or'
    data_or = read_datas(filename, discovery_method)
    axis_or = [x[1] for x in data_or]
    period_or = [x[0] for x in data_or]
    discovery_method = 'Pulsar'
    data_pulsar = read_datas(filename, discovery_method)
    axis_pulsar = [x[1] for x in data_pulsar]
    period_pulsar = [x[0] for x in data_pulsar]
    discovery_method = 'Pulsat'
    data_pulsat = read_datas(filename, discovery_method)
    axis_pulsat = [x[1] for x in data_pulsat]
    period_pulsat = [x[0] for x in data_pulsat]
    discovery_method = 'Ra'
    data_ra = read_datas(filename, discovery_method)
    axis_ra = [x[1] for x in data_ra]
    period_ra = [x[0] for x in data_ra]
    discovery_method = 'Transit'
    data_transit = read_datas(filename, discovery_method)
    axis_transit = [x[1] for x in data_transit]
    period_transit = [x[0] for x in data_transit]
    discovery_method = 'Transit t'
    data_transit_t = read_datas(filename, discovery_method)
    axis_transit_t = [x[1] for x in data_transit_t]
    period_transit_t = [x[0] for x in data_transit_t]


    pyplot.xscale('log')
    pyplot.yscale('log')
    pyplot.xlim(1e-3, 1e3)
    pyplot.ylim(1e-2, 1e6)
    pyplot.scatter(axis_as, period_as, color='k', marker='+', label='Astrometry')
    pyplot.scatter(axis_ec, period_ec, color='b', marker='+', label='Eclipse timing var.')
    pyplot.scatter(axis_im, period_im, color='r', marker='+', label='Imaging')
    pyplot.scatter(axis_mi, period_mi, color='g', marker='+', label='Microlensing')
    pyplot.scatter(axis_or, period_or, color='k', marker='+', label='Or. brightness mod.')
    pyplot.scatter(axis_pulsar, period_pulsar, color='k', marker='+', label='Pulsar Timing')
    pyplot.scatter(axis_pulsat, period_pulsat, color='k', marker='+', label='Pul. timing var.')
    pyplot.scatter(axis_ra, period_ra, color='k', marker='+', label='Radial velocity')
    pyplot.scatter(axis_transit, period_transit, color='b', marker='+', label='Transit')
    pyplot.plot(axis_val_exp, period_val_exp)
    pyplot.legend(loc='lower right')
    pyplot.title('Kepler exoplanets')
    pyplot.xlabel('Semi-major axis [AU]')
    pyplot.ylabel('Period [Days]')
    pyplot.savefig('kepler_fit.pdf')
    pyplot.show()

def fit_solar_system(filename):
    ''' Plot fitted line, scatter plot of Solar system'''
    data = read_data(filename)
    axis = [x[1] for x in data]
    period = [x[0] for x in data]
    axis_log = numpy.log10(axis)
    period_log = numpy.log10(period)

    def func(x, a, b):
        ''' Linear function for fitting'''
        return b + (a * x)
    popt, pcov = curve_fit(func, axis_log, period_log)

    axis_val = numpy.linspace(-3, 3, 50)
    aa = popt[0]
    bb = popt[1]
    period_val = bb + (aa * axis_val)
    axis_val_exp = 10**axis_val
    period_val_exp = 10**period_val

    pyplot.xscale('log')
    pyplot.yscale('log')
    pyplot.xlim(1e-3, 1e3)
    pyplot.ylim(1e-2, 1e6)
    pyplot.scatter(axis, period, color='k', marker='+', label='Planets')
    pyplot.plot(axis_val_exp, period_val_exp)
    pyplot.legend()
    pyplot.title('Solar System')
    pyplot.xlabel('Semi-major axis [AU]')
    pyplot.ylabel('Period [Days]')
    pyplot.savefig('solar_system.pdf')
    pyplot.show()

def fit_asteroids(filename):
    ''' Plot fitted line, scatter plot of Asteroids '''
    data = read_data(filename)
    axis = [x[1] for x in data]
    period = [x[0] for x in data]
    axis_log = numpy.log10(axis)
    period_log = numpy.log10(period)

    def func(x, a, b):
        ''' Linear function for fitting'''
        return b + (a * x)
    popt, pcov = curve_fit(func, axis_log, period_log)

    axis_val = numpy.linspace(-3, 3, 50)
    aa = popt[0]
    bb = popt[1]
    period_val = bb + (aa * axis_val)
    axis_val_exp = 10**axis_val
    period_val_exp = 10**period_val

    pyplot.xscale('log')
    pyplot.yscale('log')
    pyplot.xlim(1e-1, 5e2)
    pyplot.ylim(1e2, 1e4)
    pyplot.scatter(axis, period, color='k', marker='+', label='Asteroids')
    pyplot.plot(axis_val_exp, period_val_exp)
    pyplot.legend()
    pyplot.title('Asteroids')
    pyplot.xlabel('Semi-major axis [AU]')
    pyplot.ylabel('Period [Days]')
    pyplot.savefig('Asteroids.pdf')
    pyplot.show()

def sky_positions(filename):
    ''' Scatter plot positions of all exoplanets'''
    data = read_data(filename)
    ra = [x[0] for x in data]
    dec = [x[1] for x in data]

    pyplot.xlim(0, 360)
    pyplot.ylim(-90, 90)
    pyplot.scatter(ra, dec, color='k', marker='+', label='Exoplanets')
    pyplot.legend()
    pyplot.title('Exoplanet positions at the sky')
    pyplot.xlabel('RA [degrees]')
    pyplot.ylabel('Dec [degrees]')
    pyplot.savefig('sky_positions.pdf')
    pyplot.show()


if __name__=='__main__':
    main()
