from tkinter import NW, ttk, Button, Listbox, CENTER, Tk, StringVar, Entry, LEFT, TOP



class Gui(Tk):
    
        # ? Trace the writing case of SelectedTheme object to  change the theme
    def __ConfigureSearchBox(self):
        self.SearchKey = StringVar()
        self.Searchbox= Entry(self, highlightthickness=1, font=('arial', 12, 'normal'))
        self.Searchbox.config(textvariable=self.SearchKey, width=50, highlightbackground = "blue", highlightcolor= "blue", )
        self.Searchbox.place(relx=.5, rely=.1,anchor= CENTER)
    
    def __ConfigureSearchBtn(self):
        self.SearchBtn = Button()
        self.SearchBtn.config(highlightbackground='blue', text='Search', width=10)
        self.SearchBtn.place(relx=0.5, rely=0.4, anchor=CENTER)
        
    def __ConfigureProgressBar(self):
        self.ProgressBar_style = ttk.Style()
        self.ProgressBar_style.theme_use('clam')
        self.ProgressBar_style.configure('ProgressBar.Horizontal.TProgressbar', foreground='#8A2BE2', background='#8A2BE2')
        self.ProgressBar=ttk.Progressbar(
                                            self,
                                            style='ProgressBar.Horizontal.TProgressbar',
                                            orient='horizontal',
                                            length=461,
                                            mode='determinate',
                                            maximum=100,
                                            value=1
                                            )
        self.ProgressBar.place(relx=.5, rely=.3,anchor=CENTER, width=600)
        

    def __ConfigureListBox(self):
        self.list = Listbox(self, bg='#303134', font=('arial', 12, 'normal'), width=0, height=0)
        self.list.insert('0', 'Single Search')
        self.list.insert('1', 'Full Search')
        self.list.place(relx=0.001, rely=0.001, anchor=NW)
        
        
        
    def __init__(self):
        super().__init__()

        self.geometry('1200x800')
        self.title('Rummage')  
        self.resizable(False, False)
        self.configure(background='#202124')
        self.__ConfigureSearchBox()
        self.__ConfigureProgressBar()
        self.__ConfigureSearchBtn()
        self.__ConfigureListBox()

        
        self.mainloop()
        

    # this is a function to get the user input from the text input box
    def getInputBoxValue(self):
        userInput = self.Searchbox.get()
        return userInput


    # This is a function which increases the progress bar value by the given increment amount
    def makeProgress(self):
        self.ProgressBar['value'] = self.ProgressBar['value'] + 1
        self.update_idletasks()


    # this is a function to get the selected list box value
    def getListboxValue(self):
        itemSelected = self.list.curselection()
        return itemSelected




    # This is the section of code which creates the main window



    # This is the section of code which creates a text input box
    


    # This is the section of code which creates a color style to be used with the progress bar


    # This is the section of code which creates a progress bar



    # This is the section of code which creates a listbox



test = Gui()
