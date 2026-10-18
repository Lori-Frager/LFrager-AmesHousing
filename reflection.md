# DSA8670 – Week 7 Codex CLI Hands-On
# Reflection

### Repository Name:  LFrager-AmesHousing


I did not have any problems starting the terminal and changing directories to start Codex in the correct folder.

### 10.13.2026

The initial summarization output I asked Codex to produce for the whole data set was extremely messy.  Very hard to read. 
I should have included instructions to place the data in a table or in a column.  It attempted to put the
information side by side until it ran out of room and started the next line. Again, it was a very messy output. 

This was the first time I used Codex on something this big.

### 10.14.2026  Started 7:15 pm.

I started with cleaning the data.

I asked Codex: "In the AmesHousing.csv file, remove all rows where the variable Sales Condition != normal and 
save the file with a new name, ***AmesHousingClean.csv.***"
I was totally blown away by how quickly it did it and saved the data in the new data set. It was done in seconds, 
and it gave me the details on how many rows I now had.  I opened the file in Excel and confirmed the 
other options for sale condition were not there.

So I knew I needed to be specific with the Codex instructions, so each time I included "use the AmesHousingClean.csv data set
and told it to write the code using Python". What I don't know is, if I had not included those instructions each time, would
it have kept on using Python and would it pull the data from the clean data set or the initial data set?
That is something I need to check.


### I asked: 

Write the code using Python to give me the summary statistics for the following variables:
***Year Built, Gr Liv Area, Bedroom AbvGr, TotRms AbvGr, Garage Area*** using the AmesHousingClean.csv data set."  I cut
back on the number of features since all of the features were overwhelming. 

Codex saved over the information it gathered the previous night and gave me the new updated information for the summary. If I 
would have needed that information that I did on the 13th, I would have lost it, since I did not indicate
for Codex to save the code with a new file name.



### I asked:

Create the histogram using Python of the SalePrice using the AmesHousingClean.csv data set."
Again, it was done in no time and had saved the code file and picture file before I realized with a new file name. I should
indicate file names in the process of the ask.  It did a good job naming the file correctly - histogram vs graph. 
I liked that it knew to do that. The picture of the graph was open on my computer screen and I thought I had to save
it in the folder.  I started doing that and saw it was already there. 

This was just a question I wanted to know before setting up the next question to run the code.
I asked Codex to figure the median of the SalePrice since I was looking at the question dealing with features and the
median SalePrice and it gave me $159,000.

### The question I asked:

"I want to know which features predict whether a house sells for above or below the median price using the following features,
Year Built, Gr Liv Area, Bedroom AbvGr, TotRms AbvGrd, Garage Area, Garage Type, Kitchen Qual, Overall Qual, Overall Cond. 
Create the code in Python, using the AmesHousingClean.csv data set.  Include figuring the median of the Sale Price with
this code."

Since I had asked for the median sale price in a separate question, I figured I needed to include
that question in the code. I also used the features that I initially started with and then added a few more to the list. 
The file it created was the predict_saleprice_class.py.  It first gave me the median sale price, how many home above and below the median
the confusion matrix, accuracy, precision, recall and f1-score  It also gave me the coefficient and odds ratio for these features.
The accuracy was 0.894, which is pretty good with the 9 features I selected. I obviously did not select all the features that make the 
largest difference. We just learned about feature selection in the other class.  That would have been good to use to distinguish 
between the features that are just average vs the features that can be used to make a difference in which home to purchase and renovate.


Below is what I received from the question I asked. 

Median SalePrice: $159,000
Target: 1 = Above median; 0 = At or below median
Homes above median: 1,196
Homes at or below median: 1,217
Test accuracy: 0.894

Confusion matrix (rows = actual, columns = predicted; 0 then 1):
[[225  19]
 [ 32 207]]

Classification report:
                    precision    recall  f1-score   support

At or below median       0.88      0.92      0.90       244
      Above median       0.92      0.87      0.89       239

          accuracy                           0.89       483
         macro avg       0.90      0.89      0.89       483
      weighted avg       0.90      0.89      0.89       483


Model feature effects (sorted by absolute coefficient):
-                          Feature  Coefficient  Odds ratio
-             numeric__Gr Liv Area     2.684452   14.650164
-            numeric__Overall Qual     1.437387    4.209683
-  categorical__Garage Type_2Types    -1.229741    0.292368
-              numeric__Year Built     1.075751    2.932193
-  categorical__Garage Type_Detchd    -0.922786    0.397410
- categorical__Garage Type_BuiltIn     0.779614    2.180631
-  categorical__Garage Type_Attchd     0.679312    1.972521
-             numeric__Garage Area     0.661405    1.937512
-            numeric__Overall Cond     0.567953    1.764652
- categorical__Garage Type_CarPort     0.411376    1.508893
-     categorical__Kitchen Qual_Ex     0.391656    1.479429
-     categorical__Kitchen Qual_Fa    -0.391176    0.676261
-           numeric__Bedroom AbvGr    -0.376240    0.686438
- categorical__Garage Type_Basment     0.339374    1.404068
-     categorical__Kitchen Qual_Gd     0.251889    1.286453
-     categorical__Kitchen Qual_TA    -0.195219    0.822655
-           numeric__TotRms AbvGrd     0.024306    1.024603

Coefficient note: numeric features were standardized; categorical features were one-hot encoded.


### I also asked: 

"Create the code in Python to create the linear regression model using these same variables and data set, 
with the output SalePrice." Again, I probably should have used all the features to figure out which ones were the best indicators
of getting a good house, renovating it and selling it. 

Predictors: Year Built, Gr Liv Area, Bedroom AbvGr, TotRms AbvGrd, Garage Area, Overall Qual, Overall Cond, Garage Type, Kitchen Qual
Test R-squared: 0.854
Test mean absolute error: $19,340.89
Test root mean squared error: $26,501.81

Intercept: $181,780.49

Model coefficients (sorted by absolute value):
                         Feature   Coefficient
-    categorical__Kitchen Qual_Ex  44653.608329
-            numeric__Gr Liv Area  37971.370954
-    categorical__Kitchen Qual_TA -20111.996297
-           numeric__Overall Qual  16617.839916
-    categorical__Kitchen Qual_Gd -16083.128305
- categorical__Garage Type_2Types -15846.879508
-             numeric__Year Built  14016.713181
- categorical__Garage Type_Attchd  13318.473394
-            numeric__Garage Area  10959.042162
-    categorical__Kitchen Qual_Fa  -8458.483727
-          numeric__Bedroom AbvGr  -7922.699417
-           numeric__Overall Cond   7187.199278
- categorical__Garage Type_Detchd   3686.290231
- categorical__Garage Type_Basment  -2873.060013
-           numeric__TotRms AbvGrd  -2581.449621
- categorical__Garage Type_BuiltIn   1596.607222
- categorical__Garage Type_CarPort    118.568674

Numeric predictors were standardized, and categorical predictors were one-hot encoded. 
Coefficients describe model associations, not causation.

I wanted to see the difference in the information it would give me, especially since we have been looking at this
kind of information in our other class. 

After each ask, I would go and find the file in my folder and run it in the terminal I had open in JupyterLab, reviewing 
the results as well as the formatting.

If I was to run this again, I would use the Wrapper:Forward Selection approach we just learned about in the other class.
I would have seen which features were the best, since it lists the features in order from best to worst for calculating a 
better AUC each time it did another iteration. Then I could have easily selected the ones it did, or just selected and 
used the top 10 or 15. I noticed the more I worked with it, before I would click on enter, I would think of something additional
to add to the question. The cursor does not move backward easily, so that was a little bit of a challenge.  
I had tried typing the question out in Word first, but it did not take the copy and paste option at all. 

One thing it did for me. I had used a plural for the column name that I requested, and it corrected it to the column name 
that was not plural. I made sure that was the correct column.

I tried using ***/transcript*** to get the log of the prompt history from Codex, but that did not work.  I had to use ***/export.***
I did this at the end, not at each prompt. I will definitely use it after every prompt. Since I couldn't get 
/ transcript to work, I was afraid I was going to lose the information.



### Finished around 9 pm on 10.14.2026.


I tried to get this to run in Windows PowerShell, but it would not. It said Python was not available in this environment.
I was able to run the code using Anaconda, JupyterLab and opening a Terminal there. 








