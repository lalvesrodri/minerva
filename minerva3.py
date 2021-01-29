import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np

numero = int (input('digite um para exibir o gráfico:'))


if (numero == 1):
    teste = pd.read_csv('/media/sf_c++/minerva-ezracing/Teste01/ajuste2.csv',encoding = 'UTF-8', sep = ';', nrows=1023)
    print(teste)
    plt.plot(teste['Distance [m]' ], teste['volta 1 [km/h]' ], label = 'lap1')
    plt.plot(teste['Distance [m]' ], teste['volta2 [km/h]' ], label = 'lap2')
    plt.plot(teste['Distance [m]' ], teste['volta3 [km/h]' ], label = 'lap3')
    plt.plot(teste['Distance [m]' ], teste['volta4 [km/h]' ], label = 'lap4')
    plt.plot(teste['Distance [m]' ], teste['volta5 [km/h]' ], label = 'lap5')
    plt.plot(teste['Distance [m]' ], teste['volta6 [km/h]' ], label = 'lap6')
    plt.plot(teste['Distance [m]' ], teste['volta7 [km/h]' ], label = 'lap7')
    plt.title('velocidadextempo')
    plt.xlabel('distancia')
    plt.ylabel('velocidae')
    plt.legend()
    plt.show()

else:
    print('numero invalido')