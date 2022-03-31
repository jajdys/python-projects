import matplotlib.pyplot as plt
import numpy as np

wyniki = np.array([24.1, 25.7, 14.8, 11.5,10.3,4.9,8.6])
x = ["CDU/CSU", "SPD", "Sojusz 90/Zieloni", "FDP", "AID", "LEFT PARTY","pozostałe"]

plt.pie(wyniki, labels=x, autopct='%1.1f%%')
plt.show()
plt.legend()
plt.axis('equal')