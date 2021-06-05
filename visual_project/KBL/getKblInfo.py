from getKblUtil import KblGudan

chatname = 'phdebus'
myurl = 'https://phoebus.kbl.or.kr/intro/stadium'

kbllist = KblGudan(chatname, myurl)

soup = kbllist.getWebDriver()

saveData = list()

promy_list = soup.findAll('div', attrs={'class':'info'})

mydd = []

for mydl in promy_list:


    mydd.append(mydl.findAll('dd'))

    # address = mydd[0]

print(mydd[len(mydd)-1])

imsidd = str(mydd[len(mydd)-1])
print(type(imsidd))

address = imsidd.replace('<dd>', '').replace('</dd>', '').replace('[', '').replace(']', '')

imsi = address.split(' ')
sido = imsi[0]
gungu = imsi[1]

saveData.append([chatname, sido, gungu, address])

kbllist.save2Csv(saveData)