import urllib.request
import datetime
import json
import math

def getRequestUrl(url):
    req = urllib.request.Request(url)

    try:
        response = urllib.request.urlopen(req)
        if(response.getcode() == 200):
            # print('[%s] success' % (datetime.datetime.now()))
            return response.read().decode('utf-8')
    except Exception as e:
        print('[%s] failure' % (datetime.datetime.now()))
        print(e)
        return None
# End of getRequestUrl(url)


def getHospitalData(pageNo, numOfRows):
    end_point = 'http://apis.data.go.kr/6260000/MedicInstitService/MedicalInstitInfo'

    access_key = 'XdevpcDIIQos%2BPBYspGGSQy4ATyT0KbWZLvWPW4kdYE%2Bqos7xA5XWTbl8bbrj4P9lXHARRstDgKG9remMcl8dg%3D%3D'

    parameters = '?resultType=json'
    parameters += '&serviceKey=' + access_key
    parameters += '&pageNo=' + str(pageNo)
    parameters += '&numOfRows=' + str(numOfRows)

    url = end_point + parameters
    print('url: ')
    print(url)

    result = getRequestUrl(url)

    if(result == None):
        return None
    else:
        return json.loads(result)

# End of getHospital(pageNo, numOfRows)


jsonResult = []

# 페이지 번호
pageNo = 1
# 1번에 조회할 최대 행수
numOfRow = 100
nPage = 0

while(True):
    print('pageNo : %d, nPage : %d' % (pageNo, nPage))
    jsonData = getHospitalData(pageNo, numOfRow)
    # print(jsonData)

    if(jsonData['MedicalInstitInfo']['header']['code'] == '00'):
        totalCount = jsonData['MedicalInstitInfo']['totalCount']
        # print('데이터 총 갯수 : %d' % totalCount)

        if(totalCount == 0):
            break

        for item in jsonData['MedicalInstitInfo']['item']:
            jsonResult.append(item)

        nPage = math.ceil(totalCount/numOfRow)
        if(pageNo == nPage):
            # 마지막 페이지 입니다.
            break

        pageNo += 1

    else:
        break

    # Json에 저장하는 방법
    savedFilename = '부산시 의료 기관, 약국 운영 시간 정보.json'
    with open(savedFilename, mode='w', encoding='utf-8') as outfile:
        retJson = json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)
        outfile.write(retJson)

    print(savedFilename + '파일 저장됨')


# End of while

# print(len(jsonResult))

print('finished')