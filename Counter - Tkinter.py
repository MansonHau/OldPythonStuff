from tkinter import *

class Window(Frame):
    

    def __init__(self, master=None):
        Frame.__init__(self, master)               
        self.master = master
        self.init_window()
        self.fluff_count = 0
        
        self.countButton = Button(self, text = 'Uh... ', 
                             command = self.count_the_fluff)
        self.countButton.pack()
        master.bind('u', lambda event: self.count_the_fluff())
        
        self.displayButton = Button(self, text = 'Display Results', 
                             command = self.display_results)
        self.displayButton.pack()
        master.bind('d', lambda event: self.display_results())
        
        self.displayButton = Button(self, text = 'Current Results (shell)', 
                             command = self.display_results_shell)
        self.displayButton.pack()
        master.bind('c', lambda event: self.display_results_shell())
        
        self.clearButton = Button(self, text = 'Reset', 
                             command = self.clear)
        self.clearButton.pack()
        master.bind('r', lambda event: self.clear())
        
    
    def init_window(self):
        self.master.title('Uh Counter')
        
        self.pack(fill = BOTH, expand = 1)
      

    def count_the_fluff(self):
            
        self.fluff_count = self.fluff_count + 1


    def display_results(self):

        self.text = Label(self, text = str(self.fluff_count) + ' fluff words.')
        self.text.pack()
        
    def clear(self):
        self.text.destroy()
        self.fluff_count = 0
        
    def display_results_shell(self):
        print(self.fluff_count)
                    
root = Tk()

root.geometry('200x200')

app = Window(root)

root.mainloop()
