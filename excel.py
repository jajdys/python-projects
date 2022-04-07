import matplotlib.pyplot as plt
import pandas as pd
var= pd.read_excel('exceel.xlsx')
plt.bar(var['Nazwisko'], var['średnia'])
var.head()
plt.show()