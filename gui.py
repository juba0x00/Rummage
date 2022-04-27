import tkinter as tk
import tkinter.font as tkFont

class App(tk.Tk):
    
    def __configure_root_window(self):
        self.title("Rummage")
        #setting window size
        width=1174
        height=731
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)
        self.resizable(width=False, height=False)
        
    def __configure_search_btn(self):        
        self.SearchBtn=tk.Button()
        self.SearchBtn.config(
                                activebackground='#331717', 
                                activeforeground='#924a4a', 
                                anchor='center', 
                                bg='#204c62',
                                fg='#f2f0ed', 
                                justify='center', 
                                text='Search', 
                                font=self.font,
                                command=self.SearchBtn_command
                            )
        self.SearchBtn.place(x=520,y=110,width=130,height=30)

        
        
    def __configure_single_search_entry(self):
        
        self.SingleSearchEntry = tk.Entry()
        self.SingleSearchEntry.config(  
                                        borderwidth='1px',
                                        font=self.font, 
                                        fg='#cfcac2', 
                                        justify='center', 
                                        text='Enter a Search Key',
                                        relief='groove'
                                    )

        self.SingleSearchEntry.place(x=380,y=20,width=411,height=31)
        
    def __configureureEmailEntry(self):
        self.EmailEntry = tk.Entry()
        self.EmailEntry.config(  
                                        borderwidth='1px',
                                        font=self.font, 
                                        fg='#cfcac2', 
                                        justify='center', 
                                        text='Enter a Search Key',
                                        relief='groove'
                                    )
        
    def __configure_phone_entry(self):
        self.PhoneEntry = tk.Entry()
        self.PhoneEntry.config(  
                                        borderwidth='1px',
                                        font=self.font, 
                                        fg='#cfcac2', 
                                        justify='center', 
                                        text='Enter a Search Key',
                                        relief='groove'
                                    )



    def __show_full_search_widgets(self):
        self.EmailEntry.place(x=10,y=110,width=390,height=30)
        self.PhoneEntry.place(x=10,y=170,width=390,height=30)
        
        
    def __configure_status_output(self):
        self.StatusOutput=tk.Text()
        self.StatusOutput.config(
            bg='red', 
            font=self.font, 
            fg='black',
            state='disabled'
        )
        self.StatusOutput.config()
        self.StatusOutput.place(x=10,y=270,width=573,height=453)
        
        
    def __configure_result_output(self):
        self.ResultOutput=tk.Text()
        self.ResultOutput.config(

            bg='red', 
            font=self.font, 
            fg='black',
            state='disabled'
        )
        self.ResultOutput.place(x=590,y=270,width=576,height=452)


        
        
    def append_status(self):
        self.StatusOutput.config(state='normal')
        self.StatusOutput.insert(tk.END) #! add status 
        self.StatusOutput.config(state='disabled')


    def __init__(self):
        super().__init__()

        self.font = tkFont.Font(family='Times',size=16)
        
        self.__configure_root_window()
        self.__configure_search_btn()
        self.__configure_single_search_entry()
        self.__configure_status_output()
        self.__configure_result_output()

        GLineEdit_726=tk.Entry(self)
        GLineEdit_726["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_726["font"] = ft
        GLineEdit_726["fg"] = "#cfcac2"
        GLineEdit_726["justify"] = "center"
        GLineEdit_726["text"] = "Entry"
        GLineEdit_726.place(x=770,y=110,width=390,height=30)

        GLineEdit_103=tk.Entry(self)
        GLineEdit_103["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_103["font"] = ft
        GLineEdit_103["fg"] = "#cfcac2"
        GLineEdit_103["justify"] = "center"
        GLineEdit_103["text"] = "Entry"
        GLineEdit_103.place(x=770,y=170,width=390,height=30)

        GButton_927=tk.Button(self)
        GButton_927["bg"] = "#0e1011"
        ft = tkFont.Font(family='Times',size=10)
        GButton_927["font"] = ft
        GButton_927["fg"] = "#f2f0ed"
        GButton_927["justify"] = "center"
        GButton_927["text"] = "Button"
        GButton_927.place(x=520,y=170,width=130,height=30)
        GButton_927["command"] = self.GButton_927_command

    def SearchBtn_command(self):
        print("command")


    def GButton_927_command(self):
        print("command")

app = App()
app.mainloop()
