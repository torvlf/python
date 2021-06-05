import pandas as pd
from pandas import DataFrame

myencoding = 'utf-8'
gudanList = ['kt','kcc','kgc','phdebus', 'souelsamsung', 'souelsk', 'dbpromy', 'changwonlg', 'incheonelepants', 'goyangorion']

# chickenList = ['pelicana']

newframe = DataFrame()

for onegudan in gudanList:
    filename = onegudan + '.csv'
    myframe = pd.read_csv(filename, encoding=myencoding)
    # 맨 앞에 5개만 출력할 때 .head()를 붙혀주면 된다.
    # print(myframe.head())
    # print('-'*30)

    newframe = pd.concat([newframe, myframe], axis=0, ignore_index=False)

print(newframe.info())

totalfile = 'allgudan.csv'
newframe.to_csv(totalfile, encoding=myencoding)
print(totalfile + '파일이 저장됨')
