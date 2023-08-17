# Project-1-group-4
---
### file name: effect_oilPrice_covid_on_oilStockMarket.ipynb
### Question : How much does US gasoline prices affect the stock market in the US oil industry?
* Use the library 'yfinance' to retrieve oil companies information such as address, market capitalization and gross profits and stock prices trend.
* Filtered  the companies out to the Unites States and the United Kingdom, and sort them by gross profits.
* Use geoapify_key to create maps that plot 30 major companies in the world and 6 selected companies.
* Create a scatter plot to show the relation between gas prices and stock prices for selected top 6 oil companies.
* Compute r-values and linear regression for each relationship.

### Question : How much does COVID-19 affect the stock market in the US oil industry?
* Extract US data from COVID-19 data worldwide and clean them. 
* Create a figure that displays new COVID-19 cases trend.
* Create a scatter plot to show the relation between weekly cumulated new COVID-19 cases and stock prices for selected 6 oil companies.
* Compute r-values and linear regression for each relationship.
---- 
## The Impact of the COVID-19 Pandemic on Oil Stock Prices

### Section 3: Correlation between the Demand for Oil and Stock Prices
![maksym-kaharlytskyi-u13zBF4r56A-unsplash](https://github.com/SIWhang213/Project-1-group-4/assets/137141385/500f11cf-8bc1-478b-837d-383e914413e9)

Gathering data from the Energy Information Administration's open data server through the use of an API key, we find that the demand for oil in the U.S. (i.e., total consumption) dropped significantly during the first four months of 2020. In fact, this decline closely follows the timeline of the pandemic. Following the detection of a novel coronavirus in Wuhan, China in December 2019, the World Health Organization (WHO) formally announced this revelation in January 9th, 2020 (AJMC, 2021). In the same month, the first case of the virus is detected in the U.S., and by the end of the month the WHO issues a global health emergency. Consequently, global air travel is restricted. By early March, the WHO declares a COVID-19 pandemic, effectively bringing our globalized world to a standstill. 

<img width="1388" alt="oil_trend" src="https://github.com/SIWhang213/Project-1-group-4/assets/137141385/322298b7-e501-4008-8f44-4d7d3e56e821">

As seen here, the impact of the pandemic is most evident in the line representing the year 2020. By 2022, the consumption of oil returns to pre-pandemic levels as travel restrictions and social distancing rules were either relaxed or lifted completely. How did this fluctuation in oil consumption in the U.S. affect the stock prices of oil companies? In other words, is there a correlation between oil consumption and oil stock prices? In an attempt to answer this, the average stock price of four oil companies were calculated based on the month for the years 2019-2022. Using these data, four scatterplots were created with the x-axis as the oil consumption (in thousand barrels) and the y-axis as the average stock price (in USD). 

<img width="880" alt="Screenshot 2023-08-17 at 17 01 11" src="https://github.com/SIWhang213/Project-1-group-4/assets/137141385/4adf064a-754f-43e9-89b5-61ee17a9e16f">

The r-values in the ranges of 0.47 - 0.55 indicate that there is a low positive correlation between the two variables. Stated differently, while there are other factors that may influence the price of oil stocks, there is still a small tendency of the two variables to move together in a positive/upward direction. The equation of the linear regression reflects the large difference in the scale range between the two variables. Likewise, the line appears to be an upward slope when in fact it should be more or less horizontal. Lastly, what is particularly interesting is the way in which the markers of the scatterplot are visually distributed in roughly the same manner. This would indicate that these four particular stocks generally move together. 
=======

---
### Attached files :
* Three jupyter notebook files
* One REDME file
* One .gitignore file

