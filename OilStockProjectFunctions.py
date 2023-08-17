#!/usr/bin/env python
# coding: utf-8

# In[1]:


import OilStockProjectConstants as constant

import yahoo_fin.stock_info as si
import yfinance as yf

import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pds

import datetime
from datetime import date
from pathlib import Path


# In[2]:


def ReturnDataFrameOfOilCompanies \
        (tickerListParameter):
    
    tickerList \
        = []
    
    companyNameList \
        = []
    
    industryList \
        = []
    
    minimumMarketCapList \
        = []
    
    maximumMarketCapList \
        = []
    
    meanMarketCapList \
        = []
    
    medianMarketCapList \
        = []
    
    
    print \
        ('Begin retrieving oil company tickers...')
    
    print()
  

    for ticker in tickerListParameter:
    
        try:
            
            if ticker == None \
                or ticker == '':
            
                continue
                

            stockYahooFinanceObject \
                = yf \
                    .Ticker \
                        (tickerListParameter)
            
            
            firstTradingDateTime \
                = datetime \
                    .datetime \
                        .fromtimestamp \
                            (stockYahooFinanceObject \
                                .info \
                                     ['firstTradeDateEpochUtc'])
            
            anaylysisStartDateTime \
                = datetime \
                    .datetime \
                        .strptime \
                            (constant.START_DATE, 
                             '%Y-%m-%d')
            
            if anaylysisStartDateTime < firstTradingDateTime:
                
                print (f'The historical stock trading for the ticker, {ticker}, begins '
                       + f'after the first day of the analysis period.')
                
                print()
                
                continue
            
            
        
            industryStringVariable \
                = stockYahooFinanceObject \
                    .info \
                        ['industry']

            if industryStringVariable.find('Oil') != -1:      
            
                tickerList \
                    .append \
                        (ticker)
                
                companyNameList \
                    .append \
                        (stockYahooFinanceObject \
                            .info
                                ['longName'])
                
                industryList \
                    .append \
                        (stockYahooFinanceObject \
                            .info
                                ['industry'])
                    
                    
                outstandingSharesList \
                    = stockYahooFinanceObject \
                        .get_shares_full \
                            (start = constant.START_DATE, 
                             end = constant.END_DATE) \
                        .astype \
                            (float) \
                        .tolist()
                
                closingStockPriceList \
                    = stockYahooFinanceObject \
                        .history \
                            (start = constant.START_DATE, 
                             end = constant.END_DATE) \
                                ['Close'] \
                        .tolist()
                
                marketCapList \
                    = list \
                        (map \
                            (lambda x, y: x * y, 
                                 outstandingSharesList, 
                                 closingStockPriceList))
                
                
                minimumMarketCapList \
                    .append \
                        (pds \
                            .Series \
                                (marketCapList) \
                            .min())
    
                maximumMarketCapList \
                    .append \
                        (pds \
                            .Series \
                                (marketCapList) \
                            .max())

                meanMarketCapList \
                    .append \
                        (pds \
                            .Series \
                                 (marketCapList) \
                            .mean())
    
                medianMarketCapList \
                    .append \
                        (pds \
                            .Series \
                                (marketCapList) \
                            .median())
            
            
                print \
                    (f'The ticker,{ticker}, is in the '
                     + f'{industryStringVariable} industry.')
        
        except:
        
            print \
                (f'This ticker, {ticker}, did not have company information.' 
                 + f'  Skipping...')
            
            print()
        
            pass
    
    
    print()
    
    print \
        (f'The retrievel of oil company tickers is complete.')
    
    print()
    
    
    companyDataFrame \
        = pds \
            .DataFrame \
                (list \
                     (zip \
                          (tickerList, 
                           companyNameList, 
                           industryList, 
                           minimumMarketCapList, 
                           maximumMarketCapList, 
                           meanMarketCapList, 
                           medianMarketCapList)),
                           columns \
                             = ['Ticker', 
                                'Company Name', 
                                'Industry', 
                                'Market Cap (Min)', 
                                'Market Cap (Max)', 
                                'Market Cap (Mean)', 
                                'Market Cap (Median)'])
    
    
    return \
        companyDataFrame


def ReturnOilSectorMarketIndexSeries \
        (tickerListParameter,
         indexWeightListParameter):

    firstSeriesFlagBooleanValue = True
    
    
    if len(tickerListParameter) != len(indexWeightListParameter):
        
        print('The number of elements in the two function parameters are not equal. Exiting...')
        
        print()
        
        return \
            None
    
    
    print \
        ('Begin calculating oil company stock index Series...')
    
    print()
    
    
    for index, ticker in enumerate(tickerListParameter):
    
        try:
            
            if ticker == None \
                or ticker == '':
            
                continue
                
                
            stockYahooFinanceObject \
                = yf \
                    .Ticker \
                        (ticker)
    
    
            temporarySeries \
                = stockYahooFinanceObject \
                    .history \
                        (start \
                             = constant \
                                 .START_DATE, 
                         end \
                             = constant \
                                 .END_DATE) \
                            ['Close']

            
            if firstSeriesFlagBooleanValue == True:
                
                marketIndexSeries \
                    = temporarySeries * indexWeightListParameter[ index ]
                
                firstSeriesFlagBooleanValue \
                    = False
                    
            else:
                
                marketIndexSeries \
                    = marketIndexSeries \
                        + (temporarySeries * indexWeightListParameter[index])
                
        except:
        
            print \
                (f'This ticker, {ticker}, did not have historical stock prices.' 
                 + f'  Skipping...')
            
            print()
        
            pass
        
        
    print \
        (f'The calculation of the oil company stock index Series is complete.')
    
    print()
        
    return \
        marketIndexSeries


def ReturnHistoricalPricesSeries \
        (tickerStringParameter):
    
    try:
            
        if tickerStringParameter == None \
            or tickerStringParameter == '':
            
            print('The script did not have a symbol passed to it as a parameter.  Exiting...')
             
            print()
            
            return
                
                
        stockYahooFinanceObject \
            = yf \
                .Ticker \
                    (tickerStringParameter)

            
        firstTradingDateTime \
            = datetime \
                .datetime \
                    .fromtimestamp \
                        (stockYahooFinanceObject \
                            .info \
                                ['firstTradeDateEpochUtc'])
            
        anaylysisStartDateTime \
            = datetime \
                .datetime \
                    .strptime \
                        (constant.START_DATE, 
                            '%Y-%m-%d')
            
        if anaylysisStartDateTime < firstTradingDateTime:
                
            print (f'The historical stock trading for this symbol, {ticker}, begins '
                    + f'after the first day of the analysis period.')
                
            print()
            
            
    except:
        
        print \
                (f'This symbol, {ticker}, had a problem retrieving historical prices.' 
                 + f'  Skipping...')
            
        print()
        
        pass
            
            
    return \
        stockYahooFinanceObject \
            .history \
                (start \
                     = constant \
                        .START_DATE, 
                 end \
                    = constant \
                        .END_DATE) \
                            ['Close']

    
def ReturnIndustryMarketCapStatisticsSummary \
        (inputDataFrameParameter,
         columnNameStringParameter):
    
    quantileSeries \
        = inputDataFrameParameter \
            .groupby \
                ('Industry') \
                    [columnNameStringParameter] \
            .quantile \
                ([0.25,
                  0.50,
                  0.75])
    
    
    industryList \
        = []
    
    lowerQuartileList \
        = []
    
    upperQuartileList \
        = []
    
    interquartileRangeList \
        = []
    
    lowerBoundList \
        = []
    
    upperBoundList \
        = []
    
    meanList \
        = []
    
    medianList \
        = []
    
    percentDifferenceList \
        = []
    
    numberOfCompaniesList \
        = []
    
    numberOfOutliersList \
        = []
    
    
    for index, quartile in enumerate(quantileSeries):
        
        modulusConditionIntegerVariable \
            = index % 3
        
        
        if modulusConditionIntegerVariable == 0:
            
            industryListStringVariable \
                = quantileSeries.keys() \
                    [index] \
                    [0]
            
            
            lowerQuartileFloatVariable \
                = quantileSeries \
                    [index]

            upperQuartileFloatVariable \
                = quantileSeries \
                    [index + 2]

            
            interquartileRangeFloatVariable \
                = upperQuartileFloatVariable - lowerQuartileFloatVariable

            
            lowerBoundFloatVariable \
                = lowerQuartileFloatVariable - (1.5*interquartileRangeFloatVariable)

            upperBoundFloatVariable \
                = lowerQuartileFloatVariable + (1.5*interquartileRangeFloatVariable)
            
            
            meanFloatVariable \
                = inputDataFrameParameter \
                    .loc \
                        [inputDataFrameParameter \
                             ['Industry'] \
                         == industryListStringVariable] \
                             [columnNameStringParameter] \
                    .mean()

            medianFloatVariable \
                = quantileSeries \
                    [index + 1]
            
            percentDifferenceFloatVariable \
                = abs \
                    (meanFloatVariable - medianFloatVariable) \
                  / meanFloatVariable
            

            numberOfOutliersIntegerVariable \
                = len \
                    (inputDataFrameParameter \
                         .loc \
                             [(inputDataFrameParameter['Industry'] \
                               == industryListStringVariable) \
                              & ((inputDataFrameParameter[columnNameStringParameter] \
                                  < lowerBoundFloatVariable) \
                              |  (inputDataFrameParameter[columnNameStringParameter] \
                                  > upperBoundFloatVariable))])
            
            industryList \
                .append \
                    (industryListStringVariable)
            
            
            lowerQuartileList \
                .append \
                    (lowerQuartileFloatVariable)
            
            upperQuartileList \
                .append \
                    (upperQuartileFloatVariable)
            
            
            interquartileRangeList \
                .append \
                    (interquartileRangeFloatVariable)
            
            
            lowerBoundList \
                .append \
                    (lowerBoundFloatVariable)
    
            upperBoundList \
                .append \
                    (upperBoundFloatVariable)
        
        
            meanList \
                .append \
                    (meanFloatVariable)
            
            medianList \
                .append \
                    (medianFloatVariable)
            
            percentDifferenceList \
                .append \
                    (percentDifferenceFloatVariable)
        
        
            numberOfCompaniesList \
                .append \
                    (inputDataFrameParameter \
                        .loc \
                            [inputDataFrameParameter['Industry'] \
                             == industryListStringVariable] \
                         ['Ticker'] \
                        .count())
        
        
            numberOfOutliersList.append(numberOfOutliersIntegerVariable)
            

    summaryStatisticsDataFrame \
        = pds \
            .concat({'Industry': pds.Series(industryList), 
                     'Lower Quartile': pds.Series(lowerQuartileList),
                     'Upper Quartile': pds.Series(upperQuartileList),
                     'Interquartile Range': pds.Series(interquartileRangeList),
                     'Lower Boundary': pds.Series(lowerBoundList),
                     'Upper Boundary': pds.Series(upperBoundList),
                     'Mean': pds.Series(meanList),
                     'Median': pds.Series(medianList),
                     '% Difference': pds.Series(percentDifferenceList),
                     'Number of Companies': pds.Series(numberOfCompaniesList),
                     'Number of Outliers': pds.Series(numberOfOutliersList)},
                    axis = 1)

    
    # This line of code returns the summary statistics as a DataFrame.
    return \
        summaryStatisticsDataFrame


def ReturnTopCompanyByIndustry \
        (inputDataFrame, criterionStringVariable):
    
    maximumMedianMarketCapByIndustrySeries \
        = inputDataFrame \
            .groupby \
                ('Industry') \
                    [criterionStringVariable] \
            .max()


    topTickerList \
        = []

    topCompanyList \
        = []

    industryList \
        = []

    medianMarketCapList \
        = []

    
    for index, marketCap in enumerate(maximumMedianMarketCapByIndustrySeries):
    
        topTickerStringVariable \
            = (inputDataFrame \
                  .loc \
                      [inputDataFrame \
                           [criterionStringVariable] \
                       == marketCap] \
                           ['Ticker']) \
              .iloc[0]
    
        topCompanyNameStringVariable \
            = (inputDataFrame \
                    .loc \
                        [inputDataFrame \
                            ['Ticker'] \
                         == topTickerStringVariable] \
                           ['Company Name']) \
              .iloc[0]
    
        industryStringVariable \
            = maximumMedianMarketCapByIndustrySeries \
                .keys() \
                    [index]

    
        topTickerList \
            .append \
                (topTickerStringVariable)
    
        topCompanyList \
            .append \
                (topCompanyNameStringVariable)
    
        industryList \
            .append \
                (industryStringVariable)
    
        medianMarketCapList \
            .append \
                (marketCap)
    
    
    indexWeightList \
        = []

    totalMedianMarketCapFloatVariable \
        = sum \
            (medianMarketCapList)


    for index, marketCap in enumerate(medianMarketCapList):
    
        indexWeightFloatVariable \
            = marketCap \
              / totalMedianMarketCapFloatVariable
    
        indexWeightList \
            .append \
                (indexWeightFloatVariable)

    
    indexWeightDataFrame \
        = pds \
            .DataFrame \
                (list \
                    (zip \
                        (topTickerList, 
                         topCompanyList, 
                         industryList, 
                         medianMarketCapList, 
                         indexWeightList)),
                         columns \
                            = ['Ticker', 
                               'Company Name', 
                               'Industry', 
                               'Market Cap (Median)', 
                               'Index Weight'])
    
    
    return \
        indexWeightDataFrame


def DisplayFormattedMarketCapDataFrame \
        (inputDataFrameParameter,
         captionStringParameter):
    
    inputDataFrame \
        = inputDataFrameParameter \
            .copy()
    
    inputDataFrame \
        .index \
        .name \
            = None

    
    # This line of code formats the DataFrame and returns it to the caller.
    return \
        inputDataFrame \
            .style \
            .set_caption \
                (captionStringParameter) \
            .set_table_styles \
                ([{'selector': 
                       'caption', 
                   'props':
                        [('color', 
                              'black'), 
                         ('font-size', 
                              '20px'),
                         ('font-style', 
                              'bold'),
                         ('text-align', 
                              'center')]}]) \
            .set_properties \
                (**{'text-align':
                        'center',
                    'border':
                        '1.3px solid red',
                    'color':
                        'blue'}) \
            .format \
                ({'Ticker':
                        constant.GENERAL_FORMAT, 
                  'Company Name':
                        constant.GENERAL_FORMAT, 
                  'Industry':
                        constant.GENERAL_FORMAT,
                  'Market Cap (Min)':
                        constant.CURRENCY_FLOAT_FORMAT,
                  'Market Cap (Max)':
                        constant.CURRENCY_FLOAT_FORMAT,
                  'Market Cap (Mean)':
                        constant.CURRENCY_FLOAT_FORMAT,
                  'Market Cap (Median)':
                        constant.CURRENCY_FLOAT_FORMAT}) \
            .hide()


def DisplayFormattedUpdatedMarketCapDataFrame \
        (inputDataFrameParameter,
         captionStringParameter):

    inputDataFrame \
        = inputDataFrameParameter \
            .copy()
    
    inputDataFrame \
        .index \
        .name \
            = None

    
    # This line of code formats the DataFrame and returns it to the caller.
    return \
        inputDataFrame \
            .style \
            .set_caption \
                (captionStringParameter) \
            .set_table_styles \
                ([{'selector': 
                       'caption', 
                   'props':
                        [('color', 
                              'black'), 
                         ('font-size', 
                              '16px'),
                         ('font-style', 
                              'bold'),
                         ('text-align', 
                              'center')]}]) \
            .set_properties \
                (**{'text-align':
                        'center',
                    'border':
                        '1.3px solid red',
                    'color':
                        'blue'}) \
            .format \
                ({'Ticker':
                        constant.GENERAL_FORMAT, 
                  'Company Name':
                        constant.GENERAL_FORMAT, 
                  'Industry':
                        constant.GENERAL_FORMAT,
                  'Market Cap (Median)':
                        constant.CURRENCY_FLOAT_FORMAT}) \
            .hide()


def DisplaySummaryStatistics \
        (inputDataFrameParameter,
         captionStringParameter):
        
    inputDataFrame \
        = inputDataFrameParameter \
            .copy()
    
    inputDataFrame \
        .index \
        .name \
            = None

    
    return \
        inputDataFrame \
            .style \
            .set_caption \
                (captionStringParameter) \
            .set_table_styles \
                ([{'selector': 
                       'caption', 
                   'props':
                        [('color', 
                              'black'), 
                         ('font-size', 
                              '16px'),
                         ('font-style', 
                              'bold'),
                         ('text-align', 
                              'center')]}]) \
            .set_properties \
                (**{'text-align':
                        'center',
                    'border':
                        '1.3px solid red',
                    'color':
                        'blue'}) \
            .format({'Industry':
                            constant.GENERAL_FORMAT, 
                     'Lower Quartile':
                            constant.CURRENCY_FLOAT_AS_INTEGER_FORMAT, 
                     'Upper Quartile':
                            constant.CURRENCY_FLOAT_AS_INTEGER_FORMAT,   
                     'Interquartile Range':
                            constant.CURRENCY_FLOAT_AS_INTEGER_FORMAT, 
                     'Lower Boundary':
                            constant.CURRENCY_FLOAT_AS_INTEGER_FORMAT, 
                     'Upper Boundary':
                            constant.CURRENCY_FLOAT_AS_INTEGER_FORMAT, 
                     'Mean':
                            constant.CURRENCY_FLOAT_AS_INTEGER_FORMAT, 
                     'Median':
                            constant.CURRENCY_FLOAT_AS_INTEGER_FORMAT, 
                     '% Difference':
                            constant.PERCENT_FORMAT, 
                     'Number of Companies':
                            constant.INTEGER_FORMAT, 
                     'Number of Outliers':
                            constant.INTEGER_FORMAT}) \
            .highlight_max \
                (subset \
                    = ['Lower Quartile',
                       'Upper Quartile',
                       'Interquartile Range',
                       'Lower Boundary',
                       'Upper Boundary',
                       'Mean',
                       'Median',
                       '% Difference',
                       'Number of Companies',
                       'Number of Outliers'],
                 color='lime') \
            .highlight_min \
                (subset \
                    = ['Lower Quartile',
                       'Upper Quartile',
                       'Interquartile Range',
                       'Lower Boundary',
                       'Upper Boundary',
                       'Mean',
                       'Median',
                       '% Difference',
                       'Number of Companies',
                       'Number of Outliers'],
                 color='yellow') \
            .hide()


def DisplayOilIndustryPieChart \
        (inputSeriesParameter,
         captionStringParameter):
    
    colorsPieList \
        = ['red',
           'orange',
           'yellow',
           'lightgreen',
           'lightskyblue',
           'violet']

    explodeTuple \
        = (0.01, 
           0.01, 
           0.01, 
           0.01, 
           0.01, 
           0.01)

    startAngleFloatVariable \
        = 45.0

    autoPercentStringVariable \
        = '%1.1f%%'


    inputSeriesParameter \
        .rename \
            (None, 
             inplace \
                 = True)


    inputSeriesParameter \
        .plot \
            (kind='pie',
             colors \
                 = colorsPieList, 
             figsize \
                 = (6,9),
            title \
                 = captionStringParameter,
             explode \
                 = explodeTuple,
             shadow \
                 = True, 
             startangle \
                 = startAngleFloatVariable, 
             autopct \
                 = autoPercentStringVariable,
             legend \
                 = False)

    plt.show()

    
def DisplayFormattedLeadingOilCompanyIndexWeights \
        (inputDataFrameParameter,
         captionStringParameter):
        
    inputDataFrame \
        = inputDataFrameParameter \
            .copy()
    
    inputDataFrame \
        .index \
        .name \
            = None

    
    return \
        inputDataFrame \
            .style \
            .set_caption \
                (captionStringParameter) \
            .set_table_styles \
                ([{'selector': 
                       'caption', 
                   'props':
                        [('color', 
                              'black'), 
                         ('font-size', 
                              '16px'),
                         ('font-style', 
                              'bold'),
                         ('text-align', 
                              'center')]}]) \
            .set_properties \
                (**{'text-align':
                        'center',
                    'border':
                        '1.3px solid red',
                    'color':
                        'blue'}) \
            .format({'Ticker':
                            constant.GENERAL_FORMAT, 
                     'Company Name':
                            constant.GENERAL_FORMAT, 
                     'Industry':
                            constant.GENERAL_FORMAT,   
                     'Market Cap (Median)':
                            constant.CURRENCY_FLOAT_AS_INTEGER_FORMAT, 
                     'Index Weight':
                            constant.FLOAT_FORMAT}) \
            .highlight_max \
                ('Market Cap (Median)',
                 color='lime') \
            .highlight_min \
                ('Market Cap (Median)',
                 color='yellow') \
            .hide()


def ConvertValuesToPercentChange \
        (inputSeriesParameter):
    
    inputSeries \
        = inputSeriesParameter.copy()
    
    finalSeries \
        = inputSeries * 0.0
        
        
    for index, value in enumerate(inputSeries):
        
        
        if index >= len(inputSeries):
            
            continue
            
        elif index > 0:
            
            if inputSeries[ index - 1 ] != 0:
        
                finalSeries[ index ] \
                    = ((value - inputSeries[ index - 1 ]) \
                       / inputSeries[ index - 1 ]) \
                      * 100
            
            else:
                
                finalSeries[ index ] = 0.0
    
    
    finalSeries \
        .drop \
            (finalSeries \
                 .index \
                     [0], 
             inplace \
                 = True)
      
        
    return \
        finalSeries


def ReturnCompleteStockList():

    unprocessedStockList \
        = si.tickers_sp500() \
            + si.tickers_nasdaq() \
                + si.tickers_dow() \
                     + si.tickers_other()
        
    unprocessedStockList.sort()
        
    return \
        [i for n, i in enumerate (unprocessedStockList) \
         if i not in unprocessedStockList [:n]]


def NumberOfRedundanciesInSeries \
        (inputSeriesParameter):
    
    return \
        inputSeriesParameter.count() - inputSeriesParameter.nunique()


def PolynomialFit \
        (xSeriesParameter, 
         ySeriesParameter, 
         degreeIntegerParameter):
    
    resultsDictionary \
        = {}
    
    
    coefficientsFloatArray \
        = np.polyfit \
            (xSeriesParameter, 
             ySeriesParameter, 
             degreeIntegerParameter)
    
    pPoly1D \
        = np \
            .poly1d \
                (coefficientsFloatArray)
    
    
    # These lines of code calculate r-squared.
    yhatList \
        = pPoly1D \
            (xSeriesParameter)
    
    ybarFloatVariable \
        = np \
            .sum \
                (ySeriesParameter) \
                 / len(ySeriesParameter)
    
    
    ssregFloatVariable \
        = np \
            .sum \
                ((yhatList-ybarFloatVariable)**2)
    
    sstotFloatVariable \
        = np \
            .sum \
                ((ySeriesParameter - ybarFloatVariable)**2)
    
    
    resultsDictionary \
        ['r_squared'] \
            = ssregFloatVariable / sstotFloatVariable
    
    
    return \
        resultsDictionary


def CalculateRegressionDegree \
        (xSeriesParameter, 
         ySeriesParameter):

    bestDegreeIntegerVariable \
        = 1
    
    bestRValueFloatVariable \
        = 0.0
    
    
    for i in range(1,4):
        
        temporaryRValueFloatVariable \
            = math \
                .sqrt \
                    (PolynomialFit \
                        (xSeriesParameter, 
                         ySeriesParameter,
                         i) \
                            ['r_squared'])
        
        
        if bestRValueFloatVariable < temporaryRValueFloatVariable:
            
            bestRValueFloatVariable \
                = temporaryRValueFloatVariable
            
            bestDegreeIntegerVariable \
                = i

    return \
        bestDegreeIntegerVariable
        
    
def CalculateModelEquation \
        (xSeriesParameter, 
         ySeriesParameter,
         degreeIntegerVariable):
    
    return \
        np \
            .poly1d \
                (np \
                    .polyfit \
                         (xSeriesParameter, 
                          ySeriesParameter, 
                          degreeIntegerVariable))
        

def CalculatePolynomialLine \
        (xSeriesParameter, 
         ySeriesParameter):
    
    sampleNumberIntegerVariable \
        = abs \
            (int \
                 ((xSeriesParameter.max()-ySeriesParameter.min()) \
            / 2))
    
    return \
        np \
            .linspace \
                (xSeriesParameter.min(), 
                 xSeriesParameter.max(), 
                 sampleNumberIntegerVariable)

def ReturnCovidNewCasesSeries():
    
    COVIDDataToLoadPath \
        = Path \
            (constant.CSV_COVID_FILE_PATH)

    covidDataFrame \
        = pds \
            .read_csv \
                (COVIDDataToLoadPath)
    
    return \
        covidDataFrame['New_cases']


def ReturnCovidNewDeathsSeries():
    
    COVIDDataToLoadPath \
        = Path \
            (constant.CSV_COVID_FILE_PATH)

    covidDataFrame \
        = pds \
            .read_csv \
                (COVIDDataToLoadPath)
    
    return \
        covidDataFrame['New_deaths']


# In[ ]:




