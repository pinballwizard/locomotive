import scipy
import pandas
import xlrd


mileage_dt = pandas.read_excel(io='test_LT.xlsx', sheetname='Пробег')
rate_dt = pandas.read_excel(io='test_LT.xlsx', sheetname='Ставка за км')
# print(mileage_dt.iloc[1])

rate = rate_dt[rate_dt['Серия'] == 'ВЛ65ви']['Ставка'].values[0]
# print(rate)
# rate = rate.values
# print(mileage_dt.columns.values[2:])
# print(mileage_dt.iloc[1][2017])

# for i in mileage_dt.index:
# for year in mileage_dt.columns[2:]:
#     year_value = mileage_dt.iloc[1][year]
#     print(year, year_value)

print(mileage_dt.loc[1][1])

for index in mileage_dt.iloc[:]:
#     branch_name = mileage_dt.iloc[index]['Филиал']
    print(mileage_dt.loc[index])