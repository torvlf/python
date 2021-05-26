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


def makeMap(brand, store, geoInfo):
	shopInfo = store +'(' + brand_dict[brand] + ')'
	mycolor = brand_color[brand]

	latitude, longitude = float(geoInfo[0]), float(geoInfo[1])

	# 마커 그리기
	folium.Marker([latitude, longitude], popup=row[shopInfo], icon=folium.Icon(color=mycolor, icon='info-sign')).add_to(mapObject)

brand_dict = {'cheogajip':'처갓집', 'goobne':'굽네', 'nene':'네네', 'pelicana':'페리카나'}
brand_color = {'cheogajip':'red', 'goobne':'green', 'nene':'blue', 'pelicana':'orange'}

# 지도의 기준점
mylatitude = 37.56
mylongitude = 126.92
mapObject = folium.Map(location=[mylatitude, mylongitude], zoom_start=13)

csv_file = '../crawling/allstoreModified.csv'
myframe = pd.read_csv(csv_file, index_col=0, encoding='utf-8')
# print(myframe.info())

where = '서대문구'
brandName = 'cheogajip'

condition1 = myframe['gungu'] == where
condition2 = myframe['brand'] == brandName

mapData01 = myframe.loc[condition1 & condition2]
# print('-'*50, brandName, '-'*50)
# print(mapData01)


brandName = 'nene'

condition1 = myframe['gungu'] == where
condition2 = myframe['brand'] == brandName

mapData02 = myframe.loc[condition1 & condition2]
# print('-'*50, brandName, '-'*50)
# print(mapData02)


brandName = 'goobne'

condition1 = myframe['gungu'] == where
condition2 = myframe['brand'] == brandName

mapData03 = myframe.loc[condition1 & condition2]
# print('-'*50, brandName, '-'*50)
# print(mapData03)


brandName = 'pelicana'

condition1 = myframe['gungu'] == where
condition2 = myframe['brand'] == brandName

mapData04 = myframe.loc[condition1 & condition2]
# print('-'*50, brandName, '-'*50)
# print(mapData04)

# mapData01 ~ mapData04 데이터 저장할 리스트
mylist = []

# mylist에 추가
mylist.append(mapData01)
mylist.append(mapData02)
mylist.append(mapData03)
mylist.append(mapData04)

# mylist의 값을 연속적으로 저장
mapData = pd.concat(mylist, axis=0)
# print(mapData)

# 위도, 경도의 값이 잘들어오면 ok, 그렇지 않으면 notok
ok, notok = 0, 0

for idx in range(len(mapData.index)):
	brand = mapData.iloc[idx]['brand']
	store = mapData.iloc[idx]['store']
	address = mapData.iloc[idx]['address']

	geoInfo = getGeocoder(address)

	if geoInfo == None:
		print('notok:' + address)
		notok += 1
	else:
		print('ok:' + address)
		ok += 1

		makeMap(brand, store, geoInfo)
	print('-'*50)

total = ok + notok
print('ok: ', ok)
print('notok: ', notok)
print('total: ', total)

filename = '/home/junhwan/Work/python/imsi/mapresult.html'
mapObject.save(filename)
print('파일 저장 완료')