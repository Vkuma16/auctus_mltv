import pandas as pd
from pandasql import sqldf
mysql = lambda q: sqldf(q, globals())
data1 = pd.read_csv("C:/Users/USER/Downloads/Holiday_Spend_FinalData.csv")
data2 = pd.read_csv("C:/Users/USER/Downloads/Member_LTV_Data.csv")
column4 = data1.columns[3]

start_date = "1998-01-15"
end_date = "1998-01-20"
data1[column4]= pd.to_datetime(data1[column4], yearfirst= True)
data1["year"] = pd.DatetimeIndex(data1[column4]).year
#print(data1.head())
#output1 = mysql("SELECT nContractID, year, Sum(TotalSpend), count(*) from data1 group by nContractID, year")
output1 = data1.groupby(['nContractID', 'year']).sum('TotalSpend')
output1.to_csv("Output3.csv")
#mask = (data2[column3] > start_date) & (data2[column3] <= end_date)
#df2 = data2.loc[mask]
#print(df2)
#print(df2.nunique())
#print(data2[column3].unique())