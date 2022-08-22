import pandas as pd
ltvData = pd.read_csv("C:/Users/USER/Downloads/Member_LTV_Data.csv")

ltvData['dtSalesPosted']= pd.to_datetime(ltvData['dtSalesPosted'], dayfirst= True)
ltvData["SalesYear"] = pd.DatetimeIndex(ltvData['dtSalesPosted']).year

# Use cancellation date data whenever applicable
# ltvData['dtCancellationPosted']= pd.to_datetime(ltvData['dtCancellationPosted'], dayfirst= True)
# ltvData["SalesYear"] = pd.DatetimeIndex(ltvData['dtSalesPosted']).year

cleanLtv = ltvData[['ContractID','tproductname','nContractStatus','SalesYear']]
cleanLtv = cleanLtv.drop_duplicates()
#print(cleanLtv)
#print(cleanLtv['SalesYear'].nunique())
#print(cleanLtv['SalesYear'].unique())

cmh25Output = cleanLtv[cleanLtv['tproductname'].str.contains('25', na= False)]

# frequency = cmh25Output.groupby(['SalesYear']).agg(Frequency = ('ContractID','count'))
# print(frequency)
# frequency.to_csv('SalesFrequency25.csv')

cmh25Output['Vintage'] = 2016 - cmh25Output['SalesYear']
print(cmh25Output)

cmh25SummaryVintage = cmh25Output.groupby(['Vintage']).agg(MemberCount = ('ContractID','count'))
print(cmh25SummaryVintage)
cmh25SummaryVintage.to_csv('SalesFrequency2015.csv')