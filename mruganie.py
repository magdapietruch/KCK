import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import aseegg as ag
import warnings


dane = pd.read_csv("sub-01-trial-006.csv", delimiter=',', engine='python')

# t = np.linspace (0, 37.94, 200*37.94)
#
# sygnal = dane['kol2']
# przefiltrowanySygnal = ag.pasmowozaporowy(sygnal, 200, 49, 51)
# przefiltrowanySygnal = ag.pasmowoprzepustowy(sygnal, 200, 1, 50)
#
# plt.plot(t, przefiltrowanySygnal)
# plt.xlabel("Czas [s]")
# plt.ylabel("Amplituda [-]")
# plt.show()

#konieczne było zastosowanie tej metody, gdyż wyświetlał się warning związany z nowym sposobem zapisu w przyszłej wersji anacondy
with warnings.catch_warnings():
    amplitudaSyg = dane['kol2']
    cyfra = dane['kol6']

    odczytane = ["wymrugane cyfry:"]

    for i in range(len(dane['kol1'])):
         if amplitudaSyg[i] > -0.9:
             if cyfra[i] != odczytane[len(odczytane) - 1]:
                odczytane.append(cyfra[i])

print(odczytane)
