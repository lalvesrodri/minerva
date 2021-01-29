#Telemetria Final

from tkinter import *
import pandas as pd
from pandastable import Table, TableModel


class TestApp(Frame):

        def __init__(self, parent=None):
                
            self.parent = parent
            Frame.__init__(self)
            self.main = self.master
            self.main.geometry('600x400+200+100')
            self.main.title('Table app')
            f = Frame(self.main)
            f.pack(fill=BOTH,expand=1)

            teste = pd.read_csv('C:/Users/marin/Documents/ezracing capacitacao/Telemetria apresentacao/ajuste2.csv',encoding = 'UTF-8', sep = ';', nrows=1023)
            
            self.table = pt = Table(f, dataframe=teste,
                                    showtoolbar=True, showstatusbar=True)

            pt.show()
            return

app = TestApp()
app.mainloop()

