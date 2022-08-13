# Surfs Up Analysis

## Overview
The purpose of this analysis is to provide W. Avy a proper analysis with information about temperature trends in preparation for opening a new surf shop. In order to determine if the surf and ice cream shop is sustainable year round, W. Avy wanted summary statiscis of the months of June and Decemeber in Oahu. Providing this information for these two months will give W. Avy an idea of any variation of temperatures throughout the year.

## Data
The data used for this analysis is from the [Surfs Up](https://www.surfsup.com/) website.

In order to provide this information to W. Avy, I used Python, Pandas functions & methods, and SQLAlchemy to filter the date column of the Measurements table of the already existing `hawaii.sqlite` database. I used this to retrieve all of the temperatures for the month of June and December.

To build this data out, I wrote a query that filters the `date` column from the `Measurement` table to retrieve all the temps for the month of June.
```ruby
session.query(Measurement.date, Measurement.tobs).filter(extract('month',Measurement.date)==6).all()
```

I then converted the June temperature for the month.

```ruby
results = session.query(Measurement.date, Measurement.tobs).filter(extract('month',Measurement.date)==6).all()
```

After converting the temperatures, I created a DataFrame from the list of temperatures for the month of June.

```ruby
df = pd.DataFrame(results, columns=['date','June Temps'])
df.set_index(df['date'], inplace=True)
```
And finally, with this information I simply generated a summary statistics report for the month. 

I applied the same steps from the month of June to the month of December. 

Summary Stats for June
--- 
---
```ruby
            June Temps  
count       1700.000000
mean        74.944118  
std         3.257417 
min	        64.000000
25%	        73.000000
50%	        75.000000
75%     	77.000000
max	        85.000000
```
Summary Stats for December
---
```ruby
            December Temps
count	    1517.000000
mean	    71.041529
std	        3.745920
min	        56.000000
25%	        69.000000
50%	        71.000000
75%	        74.000000
max	        83.000000
```
---

Results: Three Key Differences
---
After retrieving the summary stats for both months of June and Dec I found three key differences. 

* The difference in June and Decembers lowest temperatures was a difference of **8°**.
* The difference in average temperatures between the two months is only **4°**. 
* And lastly, the difference in June and Decembers highest temperatures turned out to be only **2°**.

---
## Summary

With the two queries above, W. Avy now has all the data they need to make a decision of whether or not to build and open up a shop in Oahu. Considering the very small differences in min, median and max temperatures, the data shows that the temperature stays pretty consistent throughout the year. W. Avy would not have to worry about too drastic of temperature swings throughout the year. I say, build the shop!
