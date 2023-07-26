import pandas as pd

df = pd.read_csv('us-counties-2020.csv')
#print(df.head())
ny_df = pd.DataFrame(df[df['state'] == 'New York'])
my_ny_df = pd.DataFrame(ny_df, columns = ['date','state','cases'])

my_ny_df.sort_values(by=['date'])
cases_sum = 0
prevdate = '2020-03-01'

nycasesbydate = pd.DataFrame(columns = ['state', 'date', 'casesbydate'])
nycasesbyweek = pd.DataFrame(columns = ['state', 'weekdate', 'casesbyweek'])

def insert(df, row):
    insert_loc = df.index.max()

    if pd.isna(insert_loc):
        df.loc[0] = row
    else:
        df.loc[insert_loc + 1] = row

rowdata = []
for index,row in my_ny_df.iterrows():
    if(row['date'] == prevdate):
        cases_sum = cases_sum + row['cases']
    else:
        rowdata = []
        rowdata.append('New York')
        rowdata.append(prevdate)
        rowdata.append(str(cases_sum))
        insert(nycasesbydate,rowdata)
        cases_sum = 0
        prevdate = row['date']

prevdate = '2020-03-01'
cases_sum = 0
for index,row in nycasesbydate.iterrows():

    if(index % 7 != 0):
        cases_sum = cases_sum + int(row['casesbydate'])
    else:
        rowdata = []
        rowdata.append('New York')
        rowdata.append(row['date'])
        rowdata.append(cases_sum)
        insert(nycasesbyweek,rowdata)
        cases_sum = 0

df_min_max_scaled = nycasesbyweek.copy()
print(df_min_max_scaled)
# apply normalization techniquesZ
df_min_max_scaled['casesbyweek'] = (df_min_max_scaled['casesbyweek'] - df_min_max_scaled['casesbyweek'].min()) / (
                df_min_max_scaled['casesbyweek'].max() - df_min_max_scaled['casesbyweek'].min())

df_min_max_scaled['casesbyweek']  = round(df_min_max_scaled['casesbyweek'] * 100)
# view normalized data
print(df_min_max_scaled)
