# DSA8670 – Week 7 Codex CLI Hands-On
# Business Analytics Appl & Proj

### Repository Name:  LFrager-AmesHousing

The question I asked:

"I want to know which features predict whether a house sells for above or below the median price using the following features,
Year Built, Gr Liv Area, Bedroom AbvGr, TotRms AbvGrd, Garage Area, Garage Type, Kitchen Qual, Overall Qual, Overall Cond. 
Create the code in python, using the AmesHousingClean.csv data set.  Include figuring the median of the Sale Price with
this code."

### Date of session was 10.14.2026


### What I found out.
After cleaning the data, I ended up with 2,413 rows of data. Using the summary statistics for several of the features, 
the mean year the homes were built was 1969, the ground floor living area is 1,477 sq.ft., the average garage area is 461.25 sq.ft.

### I asked the question:
"I want to know which features predict whether a house sells for above or below the median price using the following features,
Year Built, Gr Liv Area, Bedroom AbvGr, TotRms AbvGrd, Garage Area, Garage Type, Kitchen Qual, Overall Qual, Overall Cond. 
Create the code in python, using the AmesHousingClean.csv data set.  Include figuring the median of the Sale Price with
this code."

It gave me the Confusion Matrix with the test accuracy of 0.894. Good results using these selected predictors.
Additional predictors would have given me better. It also gave me the odds ratio and looking at that, 
there were certain predictors that had significant positive association on the sale price. Kitchen Quality, 
Overall quality and Garage Type Built-in.  If the garage was detached or the kitchen was only in fair condition, 
those had a negative influence on the sale price. These are some of the items that stood out to me.

I also asked it to run the linear regression model using the same predictors on the same data set. 
The Kitchen Quality- Excellent was the highest coefficient to getting more money on the sale. 2nd in line was
the Ground Level Living Area. I can see why the ground level living area would be higher. As people get older
they don't want to go up steps and new parents don't want to worry about babies and toddlers falling down steps.




















