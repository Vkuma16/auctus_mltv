from operator import lt, truediv
import pandas as pd
holidaySpend = pd.read_csv("C:/Users/USER/Downloads/Holiday_Spend_FinalData.csv")
ltvData = pd.read_csv("C:/Users/USER/Downloads/Member_LTV_Data.csv")

holidaySpend['RevenueDate']= pd.to_datetime(holidaySpend['RevenueDate'], yearfirst= True)
holidaySpend["Year"] = pd.DatetimeIndex(holidaySpend['RevenueDate']).year
holidaySpend.rename(columns={'nContractID': 'ContractID'}, inplace= True)

ltvData['dtSalesPosted']= pd.to_datetime(ltvData['dtSalesPosted'], dayfirst= True)
ltvData["SalesYear"] = pd.DatetimeIndex(ltvData['dtSalesPosted']).year
cleanLtv = ltvData[['ContractID','tproductname','nContractStatus','SalesYear']]
cleanLtv = cleanLtv.drop_duplicates()

#finalData = pd.merge(holidaySpend,cleanLtv, on='ContractID', how = 'left')
output1 = holidaySpend.groupby(['ContractID', 'Year']).agg(
                                                YearlyTotalSpend = ('TotalSpend', 'sum'),
                                                TransactionCount = ('TotalSpend', 'count'))
output1 = output1.reset_index()
output2 = pd.merge(output1,cleanLtv, on='ContractID', how = 'left')
output2['Vintage'] = output2['Year'] - output2['SalesYear'] + 1
#print(output2)
# print(output2['Vintage'].nunique())
# print(output2['Vintage'].unique())
# output2.to_csv("Output5.csv")

cmh25Output = output2[output2['tproductname'].str.contains('25', na= False)]

cmh25SummaryHolidaySpends = cmh25Output.groupby(['Vintage', 'Year']).agg(
                                                AvgYearlyTotalSpend = ('YearlyTotalSpend', 'mean'),
                                                TotTransactionCount = ('TransactionCount', 'sum'),
                                                MemberCount = ('YearlyTotalSpend','count'))
cmh25SummaryHolidaySpends.reset_index()
print(cmh25SummaryHolidaySpends)
cmh25SummaryHolidaySpends.to_csv('Output6.csv')