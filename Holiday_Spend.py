from operator import lt, truediv
import pandas as pd
holidaySpend = pd.read_csv("C:/Users/USER/Downloads/Holiday_Spend_FinalData.csv")
ltvData = pd.read_csv("C:/Users/USER/Downloads/Member_LTV_Data.csv")

holidaySpend['RevenueDate']= pd.to_datetime(holidaySpend['RevenueDate'], yearfirst= True)
holidaySpend["Year"] = pd.DatetimeIndex(holidaySpend['RevenueDate']).year
holidaySpend.rename(columns={'nContractID': 'ContractID'}, inplace= True)

ltvData['dtSalesPosted']= pd.to_datetime(ltvData['dtSalesPosted'], dayfirst= True)
ltvData["SalesYear"] = pd.DatetimeIndex(ltvData['dtSalesPosted']).year
cleanLtv = ltvData[['ContractID','tproductname','SalesYear']]
cleanLtv = cleanLtv.drop_duplicates()

finalData = pd.merge(holidaySpend,cleanLtv, on='ContractID', how = 'left')
output1 = finalData.groupby(['ContractID', 'Year']).agg(
                                                YearlyTotalSpend = ('TotalSpend', 'sum'),
                                                TransactionCount = ('TotalSpend', 'count'))
output1 = output1.reset_index()
output2 = pd.merge(output1,cleanLtv, on='ContractID', how = 'left')
output2['Vintage'] = output2['Year'] - output2['SalesYear']
print(output2)
output2.to_csv("Output4.csv")