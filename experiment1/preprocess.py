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

result = pd.merge(left, JH[['time','state','Confirmed','Deaths']], how='left', on=['time'])
result=result.rename(columns={"Confirmed": "JH_Confirmed", "Deaths": "JH_Deaths"})



NT=pd.read_csv('NT.csv')
for row in NT.itertuples():
    if NT.at[row.Index, 'state']:
        NT.at[row.Index, 'state'] = us_state_abbrev[NT.at[row.Index, 'state']]

result = pd.merge(result, NT[['time','state','cases','deaths']], how='left', on=['time','state'])
result=result.rename(columns={"cases": "NT_cases", "deaths": "NT_deaths"})



T=pd.read_csv('T.csv')
result = pd.merge(result, T[['time','state','positive','death']], how='left', on=['time','state'])
result=result.rename(columns={"positive": "T_positive", "death": "T_death"})



result.to_csv("plot.csv")
