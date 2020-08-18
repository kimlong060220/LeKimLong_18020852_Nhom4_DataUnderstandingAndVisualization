import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as tiker 
import math

data = np.random.rand(5)
a1 = pd.Series(data)
data = pd.read_csv("Du_lieu.csv")
# data["Gia_cu"].replace("." , "")
tmp_1 =[]
tmp_2 =[]
for d in data['Gia_cu']:
    tmp_1.append(int(d.replace("." , "")))
for d in data['Gia_moi']:
    tmp_2.append(int(d.replace("." , "")))
       
data['Gia_cu'] = tmp_1
data["Gia_moi"] = tmp_2
data['discount'] = (1- data['Gia_moi']/data['Gia_cu'])*10000000
print(data) 
plt.xlabel("STT")
plt.suptitle("Biểu đồ thể hiện giá của một số sản phẩm")
plt.plot(data["STT"] , data['discount'] ,color = 'black' , label = "Discount")
plt.bar(data["STT"] , data["Gia_cu"] ,width=.4 ,label = "Old_price")
plt.bar(data["STT"]+.4 , data["Gia_moi"] , width=.4 ,label = "New_price")
plt.legend()
plt.show()