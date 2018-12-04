from tkinter import *


class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

        self.text1 = Label(master, text='Stock Concentration (%):').grid(row=0)
        self.text2 = Label(master, text='Final Concentration (%):').grid(row=1)
        self.text3 = Label(master,
                           text='Final Volume Desired (mL):').grid(row=2)

        self.stock_concentration = Entry(master)
        self.stock_concentration.grid(row=0, column=1)

        self.final_concentration = Entry(master)
        self.final_concentration.grid(row=1, column=1)

        self.final_volume = Entry(master)
        self.final_volume.grid(row=2, column=1)

        self.displayButton1 = Button(master, text='Calculate',
                                     command=self.display_results).grid(row=3)
        self.displayButton2 = Button(master, text='Clear',
                                     command=self.clear).grid(row=3, column=1)

    def init_window(self):
        self.master.title('Dilution Calculator')

    def calculate(self):

        try:
            self.initial_conc = float(self.stock_concentration.get()) / 100
            self.result_conc = float(self.final_concentration.get()) / 100
            self.result_vol = float(self.final_volume.get())

        except ValueError:
            return ('Please enter values into all the fields above first. \n' +
                    'Press Clear to remove this message.')

        stock_vol = str((self.result_conc*self.result_vol) /
                        (self.initial_conc))

        water_vol = str((self.result_vol - (float(stock_vol))))

        return ('Volume of stock needed is: ' + stock_vol + ' mL. \n' +
                'Volume of water needed is: ' + water_vol + ' mL.')

    def display_results(self, master=None):

        display = self.calculate()
        self.text = Label(master, text=display)
        self.text.grid(row=4, columnspan=2)

    def clear(self):
        
        try:
            self.text.destroy()
        except:
            pass


root = Tk()

root.geometry('280x160')

app = Window(root)

root.mainloop()
