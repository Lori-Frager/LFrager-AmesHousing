# DSA8670 – Week 7 Codex CLI Hands-On
# AI Log

### Repository Name:  LFrager-AmesHousing

### Data

I copied the AmesHousing Data to the folder.


### Processes

I added a README file so I can keep track of everything.

I changed directories until I was in my repository directory. Started Codex.

### 10.13.2026
I had asked it to give me the summarization of all the variables, and save the code.  It saved it as summarize_ames.py
That was too much data.  It was very messy to read. I stopped for the night. Did not save the transcript. 

### 10.14.2026

Started Codex at 7:15 pm.

#### I asked Codex: 7:30 pm

"Clean the data from the AmesHousing.csv file, remove all rows that the variable 
Sale Condition != normal and save the file with a new name, AmesHousingClean.csv."

I confirmed that the new file did indeed only have normal for the SaleCondition.

#### I asked: 7:50 pm

"Write the code using Python to give me the summary statistics for the following variables:
Year Built, Gr Liv Area, Bedroom AbvGr, TotRms AbvGr, Garage Area using the AmesHousingClean.csv data set."

It saved over the information it did last night and gave me the new updated information for the summary.

        Year Built  Gr Liv Area  Bedroom AbvGr  TotRms AbvGrd  Garage Area
count  2413.000000  2413.000000    2413.000000    2413.000000  2413.000000
mean   1969.436386  1477.410278       2.854538       6.366763   461.254041
std      29.487943   483.061380       0.813430       1.519145   201.675726
min    1872.000000   334.000000       0.000000       2.000000     0.000000
25%    1953.000000  1100.000000       2.000000       5.000000   315.000000
50%    1971.000000  1431.000000       3.000000       6.000000   472.000000
75%    1998.000000  1724.000000       3.000000       7.000000   576.000000
max    2010.000000  4316.000000       6.000000      13.000000  1488.000000


I took a few minutes and reviewed the summary information for the features I selected. I looked in the data for
some of the actual results to make sure I was getting the correct information.

I attempted to run this in PowerShell terminal several different ways, and it would not run. I received an error message.
I can get this to run in Anaconda, Terminal.

#### I asked: 8 pm

Create a histogram using Python of the SalePrice using the AmesHousingClean.csv data set.

It saved the graph in the folder. SalePriceHistogram.png as well as the code to create the graph.




I asked Codex to figure the median on the salePrice. I did not ask for any code. It gave me $159,000.   8:10 pm

#### The question I asked: 8:20 pm

I want to know which features predict whether a house sells for above or below the median price using the following features,
Year Built, Gr Liv Area, Bedroom AbvGr, TotRms AbvGrd, Garage Area, Garage Type, Kitchen Qual, Overall Qual, Overall Cond. 
Create the code in Python, using the AmesHousingClean.csv data set.  Include figuring the median of the Sale Price with
this code.

It gave me the median sale price, the confusion matrix, how many homes above and below the median, the
accuracy, precision, recall, and f1-score.  It also gave me the coefficient and odds ratio for these features.

#### I also asked: 8:35 pm

"Create the code in Python to figure the linear regression model using these same variables and same data set,
with the output SalePrice."

It gave me the R-squared of 0.854, which is quite good. The model is doing well figuring the overall trend.
It also gave me the coefficients for all the categories and it showed me the 2 items that influence a higher
selling price is if the Kitchen quality is excellent and the amount of ground living area of the features I was using.


I tried using ***/transcript*** to get the log of the prompt history, but that did not work.  I used ***/export.***
I did this at the end, not at each prompt. I was still trying to figure everything out as well as how to get the transcript.

Finished around 9 pm 10.14.2026.














