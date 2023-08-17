#!/usr/bin/env python
# coding: utf-8

# In[3]:


import OilStockProjectFunctions as function
import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pds


# In[6]:


def DisplaySeriesCountAndRedundancies \
        (inputSeriesParameter,
         seriesDescriptionStringParameter):
    
    numberOfTickersIntegerVariable \
        = inputSeriesParameter.count()

    numberOfRedundanciesIntegerVariable \
        = function \
            .NumberOfRedundanciesInSeries \
                (inputSeriesParameter)

    print \
        (f'There are now {numberOfTickersIntegerVariable} stock tickers '
         + f'with {numberOfRedundanciesIntegerVariable} '
         + f'redundancies in {seriesDescriptionStringParameter}.')
    
    
def DisplaySummaryStatisticsBoxPlot \
        (boxPlotDataFrameParameter, \
         columnNameStringParameter, \
         captionStringParameter):
    
    boxPlotAxes \
        = boxPlotDataFrameParameter.boxplot \
            (by \
                 ='Industry', \
             column \
                 = [columnNameStringParameter], 
             fontsize \
                 = 12,
             rot \
                 = 0,
             grid \
                 = True,
             figsize \
                 = (9,6),
             vert \
                 = False,
             widths \
                 = 0.7,
             meanline \
                 = True,
             showmeans \
                 = True)

    
    plt \
        .suptitle \
            (captionStringParameter, 
             fontsize \
                 = 'xx-large',
             fontstyle \
                 = 'italic',
             fontweight \
                 = 'bold', 
             y \
                = 1.01)
    
    plt \
        .xlabel('')
    
    plt \
        .ylabel('')
    
    boxPlotAxes \
        .get_figure() \
        .gca() \
        .set_xlabel('')
    
    
    plt \
        .show() 

    
def DisplayLinesGraph \
        (frameDictionaryParameter,
         colorDictionaryParameter,
         captionStringParameter,
         percentFlagBooleanParameter = False):
        
    lineDataFrame \
        = pds \
            .DataFrame \
                (frameDictionaryParameter)
    
    
    lineDataFrame \
        .plot \
            (kind \
                 = 'line',
             figsize \
                 = (9,6),
             grid \
                 = True, 
             legend \
                 = True, 
             fontsize \
                 = 12,
             color \
                 = colorDictionaryParameter)

    plt \
        .suptitle \
            (captionStringParameter, 
             fontsize \
                = 'xx-large',
             fontstyle \
                 = 'italic',
             fontweight \
                 = 'bold', 
             y \
                = 0.95)
    

    
    if percentFlagBooleanParameter == False:
        
        plt \
            .xlabel('Date', 
                fontsize \
                    = 12)
        
        plt \
            .ylabel('Price (USD)', \
                    fontsize \
                        = 12)
        
    elif percentFlagBooleanParameter == True:
        
        plt \
            .xlabel('Date', 
                fontsize \
                    = 12)
        
        plt \
            .ylabel('% Change In Price', \
                    fontsize \
                        = 12)

        
        
        
        
    plt \
        .show()    


    
def DisplayOneLineGraph \
    (inputDataFrameParameter,
     colorStringParameter,
     captionStringParameter):
    
    inputDataFrameParameter \
        .plot \
            (kind \
                 = 'line', 
             color \
                 = colorStringParameter, 
             figsize \
                 = (9,6),
             grid \
                 = True, 
             legend \
                 = False, 
             fontsize \
                 = 12)


    plt \
        .suptitle \
            (captionStringParameter, 
             fontsize \
                = 'xx-large',
             fontstyle \
                 = 'italic',
             fontweight \
                 = 'bold', 
             y \
                = 0.95)
    
    plt \
        .xlabel('Date', 
                fontsize \
                    = 12)
    
    plt \
        .ylabel('Price (USD)', \
                fontsize \
                    = 12)
    
    
    plt \
        .show()
    
    
def DisplayScatterPlot \
        (xSeriesParameter, 
         ySeriesParameter, 
         captionStringParameter,
         optionalDegreeIntegerParameter = None):
    
    plt \
        .scatter \
            (xSeriesParameter, 
             ySeriesParameter, 
             marker = 'o', 
             s=40,
             color='lime', 
             linewidth = 1.0,
             edgecolors='black',
             alpha=0.8)

    plt \
        .suptitle \
            (captionStringParameter, 
             fontsize \
                = 'xx-large',
             fontstyle \
                 = 'italic',
             fontweight \
                 = 'bold', 
             y \
                = 0.98)
    
    plt \
        .xlabel(xSeriesParameter.name, 
                fontsize \
                    = 14)
    
    plt \
        .ylabel(ySeriesParameter.name, \
                fontsize \
                    = 14)
    
    if optionalDegreeIntegerParameter == None:
        
        degreeIntegerVariable \
            = function \
                .CalculateRegressionDegree \
                    (xSeriesParameter, 
                     ySeriesParameter)
    else :
        
        degreeIntegerVariable \
            = optionalDegreeIntegerParameter
    
    
    modelEquationList \
        = function \
            .CalculateModelEquation \
                (xSeriesParameter, 
                 ySeriesParameter,
                 degreeIntegerVariable)
    
    polynomialLineSeries \
        = function \
            .CalculatePolynomialLine \
                (xSeriesParameter, 
                 ySeriesParameter)
    
    
    plt \
        .plot \
            (polynomialLineSeries, 
             modelEquationList \
                 (polynomialLineSeries),
             linewidth \
                 = 3,
             alpha \
                 = 1.0)
    
    
    xCoordinateIntegerVariable \
        =int((ySeriesParameter.max() + ySeriesParameter.min())/2) + 5
    
    yCoordinateIntegerVariable \
        = int \
            ((ySeriesParameter.max() - ySeriesParameter.min())*(1/3)) \
             + ySeriesParameter.min()
    
    
    rValueFloatVariable \
        = math \
            .sqrt \
             (function \
                  .PolynomialFit \
                    (xSeriesParameter, 
                     ySeriesParameter, \
                     degreeIntegerVariable) \
                          ['r_squared'])
    
    correlationFloatVariable \
        = xSeriesParameter \
            .corr \
                (ySeriesParameter, 
                 method \
                     = 'pearson')
    
    
    plt \
        .show()
    
    
    print(f'equation:  {modelEquationList}')
    
    print()
    
    print('r-value:      ' + '{:.5f}'.format(rValueFloatVariable))
    
    print('r-squared:    ' + '{:.5f}'.format(rValueFloatVariable*rValueFloatVariable))
    
    print('correlation:  ' + '{:.5f}'.format(correlationFloatVariable))
    
    
def DisplayTwoSubPlots \
        (topSeriesParameter, 
         bottomSeriesParameter, 
         captionStringVariable):
    
    fig, axs \
        = plt \
            .subplots \
                (2)

    
    fig \
        .suptitle \
                (captionStringVariable, 
                 fontsize = 14)
    
    
    axs \
        [0] \
            .plot \
                (topSeriesParameter, 
                 color \
                     = 'slateblue')
    
    axs \
        [0] \
            .set_xticklabels \
                (labels = [], 
                 rotation=90)
    
    axs \
        [0] \
            .set_title \
                (topSeriesParameter.name)
    
    
    
    axs \
        [1] \
            .plot \
                (bottomSeriesParameter, 
                 color = 'green')

    axs \
        [1] \
            .tick_params \
                (axis='x', 
                 rotation = 90)

    axs \
        [1] \
            .set_title \
                (bottomSeriesParameter.name)
    


# In[ ]:




