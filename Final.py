#Telemetria Final

from tkinter import *
import pandas as pd
from pandastable import Table


class Program(Frame):

        def __init__(self, parent=None):
                
            self.parent = parent
            Frame.__init__(self)
            self.main = self.master
            self.main.geometry('850x500+200+100')
            self.main.title('Program')
            
            body = Frame(self.main)
            body.pack(fill=BOTH,expand=1)

            teste = pd.read_csv('C:/Users/marin/Documents/ezracing capacitacao/Telemetria apresentacao/ajuste2.csv',encoding = 'UTF-8', sep = ';', nrows=1023)
            
            self.table = executor = Table(body, dataframe=teste,
                                    showtoolbar=True, showstatusbar=True)

            executor.show()
            return

app = Program()
app.mainloop()

