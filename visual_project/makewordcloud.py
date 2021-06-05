import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from wordcloud import WordCloud
from wordcloud import ImageColorGenerator

# 불러올 파일 이름
image_file = 'jordan.png'

# 마스크로 사용할 이미지 열기
jordan_color_mask = np.array(Image.open(image_file))

# 이미지 컬러 생성자
image_colors = ImageColorGenerator(jordan_color_mask)

# 읽어올 텍스트 파일
jordanfile = 'MichaelJordan_history.txt'
# 텍스트 파일을 읽기 모드로 열기
text = open(jordanfile, 'rt', encoding='utf-8')

# 텍스트 파일 읽기어서 text에 저장
text = text.read()

# wordcloud 생성
wc = WordCloud(background_color='white', max_words=2000, mask=jordan_color_mask,
               max_font_size=40, random_state=42)

# text 데이터를 wordcloud로 생성
wc = wc.generate(text)

recolorwc = wc.recolor(color_func=image_colors)

plt.figure()
# 이미지를 어떻게 처리해서 보여줄지 결정
plt.imshow(recolorwc, interpolation='bilinear')
plt.axis('off')
filename = 'MichaelJordan.png'
plt.savefig(filename, dpi=400)
print(filename + '파일 저장')