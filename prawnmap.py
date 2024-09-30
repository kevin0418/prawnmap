
import folium

# 기본 지도 생성
m = folium.Map(location=[37.5665, 126.9780], color='red', popup='Yong Sale', zoom_start=12)
m.save('index.html')
