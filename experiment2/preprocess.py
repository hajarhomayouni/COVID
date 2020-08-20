#preprocess
import pandas as pd
import sys
import csv


us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'American Samoa': 'AS',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'District of Columbia': 'DC',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Guam': 'GU',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Northern Mariana Islands':'MP',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Puerto Rico': 'PR',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virgin Islands': 'VI',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
    'Diamond Princess': 'Diamond Princess',
    'Grand Princess':'Grand Princess'
}


i = pd.date_range('1/23/2020', periods=930, freq='D')
left = pd.DataFrame({'time': i})
left['time'] = left['time'].dt.strftime('%m/%d/%y')
                    
print(left)

JH=pd.read_csv('JH.csv')
for row in JH.itertuples():
    if JH.at[row.Index, 'state']:
        JH.at[row.Index, 'state'] = us_state_abbrev[JH.at[row.Index, 'state']]

T=pd.read_csv('T.csv')
result = pd.merge(left, T[['time','state','recovered','testing_rate','hospitalization_rate']], how='left', on=['time'])
result=result.rename(columns={"recovered": "T_Recovered", "testing_Rate": "T_Testing_Rate","hospitalization_rate":"T_Hospitalization_Rate"})

result = pd.merge(result, JH[['time','state','Recovered','Testing_Rate','Hospitalization_Rate']], how='left', on=['time','state'])
result=result.rename(columns={"Recovered": "JH_Recovered", "Testing_Rate": "JH_Testing_Rate","Hospitalization_Rate":"JH_Hospitalization_Rate"})





result.to_csv("plot.csv")
