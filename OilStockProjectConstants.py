#!/usr/bin/env python
# coding: utf-8

# In[7]:


CSV_FILE_PATH \
    = './Resources/OilCompanyMarketCapitalization.csv'

CSV_COVID_FILE_PATH \
    = './Resources/COVIDDataFromOurWorldInData.csv'

START_DATE \
    = '2020-01-01'

END_DATE \
    = '2022-12-31'


GENERAL_FORMAT \
    = '{:}'

INTEGER_FORMAT \
    = '{:,}'

FLOAT_FORMAT \
    = '{:,.2f}'

FLOAT_AS_INTEGER_FORMAT \
    = '{:,.0f}'

CURRENCY_INTEGER_FORMAT \
    = '$' + INTEGER_FORMAT

CURRENCY_FLOAT_FORMAT \
    = '$' + FLOAT_FORMAT

CURRENCY_FLOAT_AS_INTEGER_FORMAT \
    = '$' + FLOAT_AS_INTEGER_FORMAT

PERCENT_FORMAT \
    = FLOAT_FORMAT + '%'

