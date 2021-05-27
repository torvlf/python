import json

from pandas import DataFrame

jsonfile = '부산시 의료 기관, 약국 운영 시간 정보.json'

myfile = open(jsonfile, 'rt', encoding='utf-8')

myfile = myfile.read()

jsonData = json.loads(myfile)
# print(type(jsonData)) - list type
# print('-'*30)

totallist = []

# 컬럼명
mycolumns = []
idx = 0
for oneitem in jsonData:
    # print(type(oneitem)) - dict type

    # print(oneitem.keys())
    # print(len(oneitem.keys()))

    sublist = []

    for key in oneitem.keys():

        if(idx == 0):
            mycolumns.append(key)

        sublist.append(oneitem[key])

    idx += 1

    totallist.append(sublist)


# print(totallist)

# pandas DataFrame을 이용해서 csv 파일 생성
myfram = DataFrame(totallist, columns=mycolumns)
filename = 'pusanHospitalExcel.csv'

myfram.to_csv(filename, encoding='utf-8', index=False)

print('finished')
