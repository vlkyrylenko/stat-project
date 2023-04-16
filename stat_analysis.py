# Import libraries
import os, sys, glob
import pandas as pd
import numpy
import pathlib
from pathlib import Path
import plotly.express as px
import math as m
from scipy import stats

os.path.dirname(os.path.abspath(__file__))
abs_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(abs_path)

# Test statistics
class STAT:
    def __init__(self):
        self.mean = 0

    def proportion_z(sampleMeasure,populationParameter,standardDeviation,sampleSize):
        # sampleMeasure - P hat, populationParameter - p, q - standard deviation, n - sample size
        # Calculate z-score for proportion
        return (sampleMeasure-populationParameter)*m.sqrt(populationParameter*standardDeviation/sampleSize)
    
    def mean_z(populationMean,sampleMean,sigma,sampleSize):
        # populationMean - nu, sampleMean - x bar, sigma - standard deviation, sampleSize - n
        # Calculate z-score for mean
        return(sampleMean-populationMean)/(sigma*m.sqrt(sampleSize))
    
    def mean_t(populationMean,sampleMean,populationSD,sampleSize):
        # populationMean - nu, sampleMean, s - population standard deviation, sampleSize - n
        # Calculate t-score for mean
        return(sampleMean-populationMean)/(populationSD*m.sqrt(sampleSize))
    

STAT()

