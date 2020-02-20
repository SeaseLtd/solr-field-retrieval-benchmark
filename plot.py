# library &amp;amp;amp; dataset
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
import pickle

n_fields_values = [1, 5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

def plot(stored, docvalues):
    plt.plot( n_fields_values, stored, marker='o', label='docvalues')
    plt.plot( n_fields_values, docvalues, marker='o', label='stored')
    plt.xlabel('number of fields returned')
    plt.ylabel('milliseconds')
    plt.legend(loc="upper left")
    plt.show()

def pickle_results(fields_type, n_results):
    with open('results_{}_{}'.format(fields_type, n_results), 'rb') as fp:
        unpickler = pickle.Unpickler(fp)
        return unpickler.load()

def main():
    stored_100 = pickle_results("stored", 100)
    docv_100 = pickle_results("docv", 100)
    stored_200 = pickle_results("stored", 200)
    docv_200 = pickle_results("docv", 200)

    plot(stored_100, docv_100)
    plot(stored_200, docv_200)

main()