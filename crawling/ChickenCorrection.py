import pandas as pd
import numpy as np

pd.options.display.max_columns = 1000
pd.options.display.max_rows = 1000

class ChickenCorrection():
    myencoding = 'utf-8'

    def __init__(self, workfile):
      self.workfile = workfile
      self.myframe = pd.read_csv(self.workfile, encoding= self.myencoding, index_col=0)

      # print(self.myframe.info())

      self.correctionSido()
      self.correctionGungu()
      self.showMergeResult()
      self.correctionAddress()

      self.myframe.to_csv('allstoreModified.csv', encoding=self.myencoding)

      print('파일 저장 완료')

    def correctionSido(self):
        self.myframe = self.myframe[self.myframe['store'] != 'CNTTEST']
        self.myframe = self.myframe[self.myframe['sido'] != '테스트']

        # print('before sido')
        # print(np.sort(self.myframe['sido'].unique()))

        # sido_correction.txt 읽기 모드로 읽어들인다.
        sidofile = open('sido_correction.txt', mode='r', encoding=self.myencoding)
        # readline() 은 한줄만 읽는 것이고 readlines()는 여러줄을 읽어 들인다.
        linelists = sidofile.readlines()
        # print(linelists)

        # 사전 생성
        sido_dict = {}

        for oneline in linelists:
            mydata = oneline.replace('\n', '').split(':')

            # list인 mydata를 sido_dict에 저장 (map.put() 과 같은 의미)
            sido_dict[mydata[0]] = mydata[1]

        # print(sido_dict)

        # 한줄 코드가 길면 '\' 를 사용해서 줄바꿈을 할 수 있다.
        # lambda 함수는 기존의 함수 선언 문법과 달리 함수를 명명하지 않고도 정의할 수 있는 함수입니다.
        # .apply() 적용시키다
        self.myframe.sido = \
            self.myframe.sido.apply(lambda data : sido_dict.get(data, data))


        # print('after sido')
        # print(np.sort(self.myframe['sido'].unique()))
        # print('-'*40)

    def correctionGungu(self):
        # print('before gungu')
        # print(self.myframe['gungu'].unique())
        # print('-'*40)


        gungufile = open('gungu_correction.txt', encoding=self.myencoding, mode='r')
        glinelist = gungufile.readlines()
        # print(gungulist)

        gungu_dict = {}

        for oneline in glinelist:
            gungudata = oneline.replace('\n', '').split(':')

            gungu_dict[gungudata[0]] = gungudata[1]

        self.myframe.gungu = \
            self.myframe.gungu.apply(lambda data : gungu_dict.get(data, data))

        # print('after gungu')
        # print(self.myframe['gungu'].unique())
        # print('-'*40)

    def showMergeResult(self):
        ditrict = pd.read_csv('district.csv', encoding=self.myencoding)
        # print(ditrict.info())

        # on -> 양쪽 데이터의 같은 값을 찾는다.
        # how -> DB의 join과 같다('inner', 'outer')
        # suffixes -> 접미사 오른쪽 값에 '_'를 붙힌다.
        mergedata = pd.merge(self.myframe, ditrict, on=['sido','gungu'], how='outer', suffixes=['','_'], indicator=True)

        # print(mergedata.head(10)

        result = mergedata.query('_merge == "left_only"')
        print('좌측에만 있는 데이터')
        print(result[['sido', 'gungu', 'address']])
        print('-'*50)


    def correctionAddress(self):
        try:
            for idx in range(len(self.myframe)):
                # print(idx)
                imsiseries = self.myframe.iloc[idx]
                # print(imsiseries)
                addrSplit = imsiseries['address'].split(' ')[2:]
                # print('addrSplit: ',addrSplit)

                imsiaddress = [imsiseries['sido'], imsiseries['gungu']]
                imsiaddress = imsiaddress + addrSplit
                # print('imsiaddress: ',imsiaddress)

                address = ' '.join(imsiaddress)
                address = address.replace('  ', ' ')

                self.myframe.iloc[idx]['address'] = address

                # print('-'*30)

        except TypeError as err:
            print(err)


filename = 'allstore.csv'
chknStore = ChickenCorrection(filename)
print('finished')