# Q2

import csv
from nltk import text
import pandas as pd
import re
from textblob import TextBlob 

df = pd.read_csv('df_final.csv')

df_purpose = pd.DataFrame(df['Purpose'].astype(str), columns=['Purpose'])

# CLEAN DATA

def clean_data(x):
    x = x.lower()
    x = re.sub('-', '', x)
    return x

df_purpose['Purpose'] = df_purpose['Purpose'].apply(clean_data)

def subjectivity(x):
    return TextBlob(x).sentiment.subjectivity

def polarity(x):
    return TextBlob(x).sentiment.polarity

def trend(x):
    if x > 0:
        return 'Positive'
    elif x == 0:
        return ' Neutral'
    else:
        return 'Negative'

df_purpose['Subjectivity'] = df_purpose['Purpose'].apply(subjectivity)
df_purpose['Polarity'] = df_purpose['Purpose'].apply(polarity)
df_purpose['Trend'] = df_purpose['Polarity'].apply(trend)
#pd.set_option('display.max_rows', None)
#df_purpose.to_csv('a.csv')

print(df_purpose.nlargest(10, ['Polarity']))
print(df_purpose.nsmallest(10, ['Polarity']))

# Q3

# The most challenging part of this type of work, it to convert all the dataset received by teammates 
# in a same format and then merge together to get a unique file composed by all different dataset. 
# In my case, I merged 4 different csv files in one. 
# The main difficulties were to understand the format of them i.e. (how the rows/columns were set up) 
# and find a way to combine them together.
# Then to reproduce a sentiment analysis, I had to understand the final dataset to get how 
# each rows looked. This mean to find if there were some special charachters that might have influnced
# negatively or positively the analysis.
# Finally, using TextBlob I performed a sentiment analysis on my dataset and selected the best 10 
# and worst 10 rows based on Polarity.



