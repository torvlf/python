from ChickenUtil import ChickenStore
# 정규 표현식 모듈
import re
############################################듈
brandName = 'nene'
base_url = 'https://nenechicken.com/17_new/sub_shop01.asp'
#############################################

def getData():

    # 엑셀로 저장될 리스트
    savedData = []

    for page_idx in range(1, 46+1):
       url = base_url + '?page=%d' % page_idx
       chnkStore = ChickenStore(brandName, url)
       soup = chnkStore.getSoup()
       #print(type(soup))

       tablelists = soup.findAll('table',attrs={'class', 'shopTable'})
       #print(len(tablelists))

       shopExists = False

       for onetable in tablelists:
           shopExists = True
           store = onetable.select_one('.shopName').string
           # print(store)

           temp = onetable.select_one('.shopAdd').string
           if temp == None:
               # shopAdd가 없으면 다음으로 넘어감
               continue
           # print('temp')
           # print(temp)

           imsi = temp.split()
           sido = imsi[0]
           gungu = imsi[1]

           # print(sido + '/' + gungu)

           # 주소 접미사
           im_address = onetable.select_one('.shopMap')
           im_address = im_address.a['href']
           # print(im_address)

           # 정규 표현식으로 숫자가 처음으로 나오는 위치부터 문자열 추출
           # 숫자로 시작하는..
           regex = '\d\S*'
           pattern = re.compile(regex)
           mymatch = pattern.search(im_address)
           addr_suffinx = mymatch.group().replace("');",'')
           # print(addr_suffinx)

           address = temp + ' ' + addr_suffinx

           phone = onetable.select_one('.tooltiptext').string

           if phone == 'NotPhone':
               phone = '전화번호 없음'

           # print(phone)

           mydata = [brandName, store, sido, gungu, address, phone]
           savedData.append(mydata)

       chnkStore.save2Csv(savedData)
############################################

print(brandName + '매장 크롤링 시작')
getData()
print(brandName + '매장 크롤링 끝')