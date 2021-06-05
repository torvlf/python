import folium
import requests
import pandas as pd

url_header = 'https://dapi.kakao.com/v2/local/search/address.json?query='

# Kakao Rest API key값
api_key = '39cbcf528bea62f2adf38d8f28db5cde'
header = {'Authorization': 'KakaoAK ' + api_key}

def getGeocoder(address):
	result = ''

	url = url_header + address
	r = requests.get(url, headers=header)

	if r.status_code == 200:
		try:
			result_address = r.json()["documents"][0]["address"]
			result = result_address['y'], result_address['x']
		except Exception as err:
			return None
	else:
		result = 'Error[' + str(r.status_code) + ']'

	return result


def makeMap(gudan, geoInfo):
	shopInfo = brand_dict[gudan]

	latitude, longitude = float(geoInfo[0]), float(geoInfo[1])

	# 마커 그리기
	folium.Marker([latitude, longitude], tooltip=shopInfo,
				  icon=folium.Icon(color='r', icon='info-sign')).add_to(mapObject)

brand_dict = {'kcc':'전주KCC', 'kgc':'안양KGC', 'kt':'부산KT', 'goyangorion':'고양오리온', 'phdebus':'울산현대모비스',
			  'souelsamsung':'서울삼성', 'souelsk':'서울SK', 'dbpromy':'원주DB', 'changwonlg':'창원LG',
			  'incheonelepants':'인천전자랜드'}

# 지도의 임시 기준점
mylatitude = 37.56
mylongitude = 126.92
mapObject = folium.Map(location=[mylatitude, mylongitude], zoom_start=13)

csv_file = 'allgudan.csv'
myframe = pd.read_csv(csv_file, encoding='utf-8')
# print(myframe.info())

where = '동래구'
gudanName = 'kt'

condition1 = myframe['Gungu'] == where
condition2 = myframe['GudanName'] == gudanName

mapData01 = myframe.loc[condition1 & condition2]
# print('-'*50, brandName, '-'*50)
# print(mapData01)

where = '전주시'
gudanName = 'kcc'

condition1 = myframe['Gungu'] == where
condition2 = myframe['GudanName'] == gudanName

mapData02 = myframe.loc[condition1 & condition2]
# print('-'*50, brandName, '-'*50)
# print(mapData02)

where = '동안구'
gudanName = 'kgc'

condition1 = myframe['Gungu'] == where
condition2 = myframe['GudanName'] == gudanName

mapData03 = myframe.loc[condition1 & condition2]
# print('-'*50, brandName, '-'*50)
# print(mapData03)

where = '중구'
gudanName = 'phdebus'

condition1 = myframe['Gungu'] == where
condition2 = myframe['GudanName'] == gudanName

mapData04 = myframe.loc[condition1 & condition2]
# print('-'*50, brandName, '-'*50)
# print(mapData04)

where = '송파구'
gudanName = 'souelsamsung'

condition1 = myframe['Gungu'] == where
condition2 = myframe['GudanName'] == gudanName

mapData05 = myframe.loc[condition1 & condition2]
# print('-'*50, brandName, '-'*50)
# print(mapData05)

where = '송파구'
gudanName = 'souelsk'

condition1 = myframe['Gungu'] == where
condition2 = myframe['GudanName'] == gudanName

mapData06 = myframe.loc[condition1 & condition2]
# print('-'*50, brandName, '-'*50)
# print(mapData06)

where = '원주시'
gudanName = 'dbpromy'

condition1 = myframe['Gungu'] == where
condition2 = myframe['GudanName'] == gudanName

mapData07 = myframe.loc[condition1 & condition2]
# print('-'*50, brandName, '-'*50)
# print(mapData07)

where = '창원시'
gudanName = 'changwonlg'

condition1 = myframe['Gungu'] == where
condition2 = myframe['GudanName'] == gudanName

mapData08 = myframe.loc[condition1 & condition2]
# print('-'*50, brandName, '-'*50)
# print(mapData08)

where = '부평구'
gudanName = 'incheonelepants'

condition1 = myframe['Gungu'] == where
condition2 = myframe['GudanName'] == gudanName

mapData09 = myframe.loc[condition1 & condition2]
# print('-'*50, brandName, '-'*50)
# print(mapData09)

where = '고양시'
gudanName = 'goyangorion'

condition1 = myframe['Gungu'] == where
condition2 = myframe['GudanName'] == gudanName

mapData10 = myframe.loc[condition1 & condition2]
# print('-'*50, brandName, '-'*50)
# print(mapData10)

# mapData01 ~ mapData04 데이터 저장할 리스트
mylist = []

# mylist에 추가
mylist.append(mapData01)
mylist.append(mapData02)
mylist.append(mapData03)
mylist.append(mapData04)
mylist.append(mapData05)
mylist.append(mapData06)
mylist.append(mapData07)
mylist.append(mapData08)
mylist.append(mapData09)
mylist.append(mapData10)

# mylist의 값을 연속적으로 저장
mapData = pd.concat(mylist, axis=0)
# print(mapData)

# 위도, 경도의 값이 잘들어오면 ok, 그렇지 않으면 notok
ok, notok = 0, 0

for idx in range(len(mapData.index)):
	gudan = mapData.iloc[idx]['GudanName']
	address = mapData.iloc[idx]['Address']

	geoInfo = getGeocoder(address)

	if geoInfo == None:
		print('notok:' + address)
		notok += 1
	else:
		print('ok:' + address)
		ok += 1

		makeMap(gudan, geoInfo)
	print('-'*50)

total = ok + notok
print('ok: ', ok)
print('notok: ', notok)
print('total: ', total)

filename = '/home/junhwan/Work/python/python/visual_project/kblGudan.html'
mapObject.save(filename)
print('파일 저장 완료')