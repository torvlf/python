from ChickenUtil import ChickenStore
from itertools import count
#############################################
brandName = 'goobne'
base_url = 'https://www.goobne.co.kr/store/search_store.jsp'
#############################################
def getData():
    savedData = []

    chknStore = ChickenStore(brandName, base_url)

    for page_idx in count():
        print('%s번째 페이지가 호출됨' % str(page_idx + 1))

        # 마지막 페이지이면 True
        bEndPage = False

        cmdJavaScript = "javascript:store.getList('%s')" % str(page_idx + 1)
        soup = chknStore.getWebDriver(cmdJavaScript)

        store_list = soup.find('tbody', attrs={'id':'store_list'})
        mytrlists = store_list.findAll('tr')

        for onestore in mytrlists:
            mytrlists = onestore.findAll('td')
            if len(mytrlists) > 1:
                store = onestore.select_one('td:nth-of-type(1)').string
                im_phone = onestore.select_one('td:nth-of-type(2)')
                phone = im_phone.a.string

                im_address = onestore.select_one('td:nth-of-type(3)')
                address = im_address.a.string

                imsi = str(address).split(' ')

                sido = imsi[0]
                gungu = imsi[1]

                savedData.append([brandName, store, sido, gungu, address, phone])
            else:
                bEndPage = True
                break



        # print(savedData)
        if bEndPage == True:
            break

    chknStore.save2Csv(savedData)

############################################

print(brandName + '매장 크롤링 시작')
getData()
print(brandName + '매장 크롤링 끝')