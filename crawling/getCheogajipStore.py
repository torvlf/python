from ChickenUtil import ChickenStore
from itertools import count
############################################듈
brandName = 'cheogajip'
base_url = 'http://www.cheogajip.co.kr/bbs/board.php'
#############################################
def getData():
    savedData = []

    for page_idx in count():
        url = base_url
        url += '?bo_table=store'
        url += '&page=%s' % str(page_idx)

        chknStore = ChickenStore(brandName, url)
        soup = chknStore.getSoup()

        mytbody = soup.find('tbody')
        shopExists = False
        
        for mytr in mytbody.findAll('tr'):
            shopExists = True

            try:
                store = mytr.select_one('td:nth-of-type(2)').string

                address = mytr.select_one('.td_subject').string
                imsi = address.split()
                sido = imsi[0]
                gungu = imsi[1]

                phone = mytr.select_one('td:nth-of-type(4)').string

                savedData.append([brandName, store, sido, gungu, address, phone])
            except AttributeError as err:
                print(err)
                shopExists = False
                break

        # print(savedData)

        if shopExists == False:
            chknStore.save2Csv(savedData)
            break

############################################

print(brandName + '매장 크롤링 시작')
getData()
print(brandName + '매장 크롤링 끝')