# Import libraries
import os, sys, glob
import pandas as pd
import numpy as np
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
        # For known population mean and standard deviation
        return(sampleMean-populationMean)/(sigma*m.sqrt(sampleSize))
    
    def mean_t(populationMean,sampleMean,sampleSD,sampleSize,significanceLevel=0.01):
        # populationMean - nu (from claim), sampleMean - x bar, s - population standard deviation, sampleSize - n
        # Calculate t-score for mean
        # For unknown population mean and standard deviation
        # n > 30 or the population is normally distributed
        STAT.mean_t.value = (sampleMean-populationMean)/(sampleSD/m.sqrt(sampleSize))
    
    def replace_placeholder(dataframe, placeholderValue):
        dataframe.replace(placeholderValue,np.nan,inplace=True)
    
    def append_csv(pathToFile, dropNaN=False):
        STAT.append_csv.df = pd.read_csv(pathToFile, header=0, encoding='utf-8',index_col=None)
        STAT.replace_placeholder(STAT.append_csv.df,99999999999)
        STAT.replace_placeholder(STAT.append_csv.df,99999996)
        STAT.replace_placeholder(STAT.append_csv.df,99999999)
        if dropNaN == True:
            STAT.append_csv.df.dropna(inplace=True)
        STAT.append_csv.df.to_csv('./data/new_data.csv', index=False, encoding='utf-8',index_label=False)

    def get_parameters(pathToFile, attributeName):
        STAT.get_parameters.df = pd.read_csv(pathToFile, header=0, encoding='utf-8',index_col=None)
        STAT.get_parameters.mean = STAT.get_parameters.df[attributeName].mean()
        STAT.get_parameters.std = STAT.get_parameters.df[attributeName].std()
