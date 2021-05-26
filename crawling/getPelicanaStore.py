from ChickenUtil import ChickenStore
from itertools import count
############################################
brandName = 'pelicana'
base_url = 'https://pelicana.co.kr/store/stroe_search.html'
#############################################

def getData():

    # 엑셀로 저장될 리스트
    savedData = []

    for page_idx in count():
        url = base_url + '?page=' + str(page_idx + 1)
        chknStore = ChickenStore(brandName, url)
        soup = chknStore.getSoup()
        # print(type(soup))

        if soup != None:
            # table class=table mt20 내용을 가져온다.
            mytable = soup.find('table', attrs={'class':'table mt20'})
    
            # table 안에 tbody의 내용을 가져온다.
            mytbody = mytable.find('tbody')

            # 목록이 없다고 가정
            shopExists = False

            #for문을 사용해서 tbody안에 있는 tr태그를 찾는다.
            for mytr in mytbody.findAll('tr'):
                # 매장이 존재
                shopExists = True

                # mytr 밑에 있는 3번째 td의 값을 가져온다
                imsiphone = mytr.select_one('td:nth-of-type(3)').string
                if imsiphone != None :
                    phone = imsiphone.strip()
                else:
                    phone = ''

                # print(phone)

                mylist = list(mytr.strings)

                store = mylist[1]
                # print(store)
                address = mylist[3]
                # print(address)

                if len(address) >= 2:
                    imsi = address.split()
                    sido = imsi[0]
                    gungu = imsi[1]

                    # print(sido)
                    # print(gungu)

                    mydata = [brandName, store, sido, gungu, address, phone]
                    savedData.append(mydata)

            if shopExists == False:
                chknStore.save2Csv(savedData)
                break
############################################

print(brandName + '매장 크롤링 시작')
getData()
print(brandName + '매장 크롤링 끝')