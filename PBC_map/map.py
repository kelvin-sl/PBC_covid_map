
'''
所有國家的屬性應該要是一個class
folium 套件可以
1. 插標誌
2. 放地圖


'''

import folium
import io
from PIL import Image
import tkinter as tk
'''

 把map轉成圖片檔存下來
 存在圖上or 網頁上
 圖上優勢：可以直接放入圖形化界面
 網頁上：所有標點都可以直接安插

'''

m = folium.Map(location=[25.016771, 121.533446], zoom_start = 16)
m.add_child(folium.Marker(location=[25.016771, 121.533446],
                             popup='NTU'))
m.save('m.html')
m



'''
img_data = m._to_png(5)
img = Image.open(io.BytesIO(img_data))
img.save('image.png')
'''
