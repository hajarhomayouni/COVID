import os
import glob
import pandas as pd
import csv
from datetime import datetime

os.chdir("/c/Users/hhajar/OneDrive - Colostate/Data_Quality_Tests/LSTM/dataset/COVID/JohnHopkins/COVID-19/csse_covid_19_data/csse_covid_19_daily_reports_us/")


#1. combine files
extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
combined_csv.to_csv( "combined_preprocessed.csv", index=False)

#2. Sort by state and time
df=pd.read_csv('combined_preprocessed.csv')  
df=df.sort_values(['Province_State', 'Last_Update'], ascending=[True, True])

#.3.postprocess
df=df.rename(columns={"Last_Update": "time"})
df=df.drop(['Country_Region', 'Lat', 'Long_','FIPS','UID','ISO3'], axis=1)
df = df.reset_index()
df['id'] = df.index
df=df.reindex(['id','time', 'Province_State', 'Confirmed', 'Deaths', 'Recovered', 'Active', 'Incident_Rate', 'People_Tested', 'People_Hospitalized', 'Mortality_Rate', 'Testing_Rate', 'Hospitalization_Rate'],axis=1)

#4.write to csv file
df.to_csv('final.csv', index=False)  
