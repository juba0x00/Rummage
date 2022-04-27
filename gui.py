# #!/usr/bin/env python3
import tkinter as tk
import tkinter.font as tkFont
# from modules.search import Search
# from modules.leaksfinder import LeaksFinder
# # countries: Egypt, Cameroon, Algeria,  Austria,  Bahrain,  Belgium, Canada,  China, Cameroon, ShittyIsrael
# from modules.validateinput import CheckinputType
# import datetime
# from threading import Thread
# from os import system


class App(tk.Tk):
    
    def __configure_root_window(self):
        self.title("Rummage")
        self.config(background='#202124')
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
                                activebackground='#0061dc', 
                                anchor='center', 
                                bg='#0a56b9',
                                fg='white', 
                                justify='center', 
                                text='Search', 
                                font=self.font,
                                command=self.SearchBtn_command
                            )
        self.SearchBtn.place(x=520,y=110,width=130,height=30)

    def __configure_switch_mode_btn(self):
        self.AnotherMode = tk.StringVar()
        self.AnotherMode.set('Full Search')
        self.SwitchModeBtn = tk.Button()
        self.SwitchModeBtn.config(
                                activebackground='#0061dc', 
                                anchor='center', 
                                bg='#0a56b9',
                                fg='white', 
                                justify='center', 
                                font=self.font,
                                textvariable=self.AnotherMode,
                                command=self.switch_mode
                            )
        self.SwitchModeBtn.place(x=520,y=170,width=130,height=30)
        
    def clicked(self, event):
        print(self.ClickedWidget)
        self.ClickedWidget.delete(0, tk.END)
        
    def __configure_single_search_entry(self):
        self.SingleSearchEntry = tk.Entry()
        self.SingleSearchEntry.config(  
                                        borderwidth='1px',
                                        font=self.font, 
                                        bg='#303134',
                                        fg='red', 
                                        justify='center',
                                    )
        self.SingleSearchEntry.insert(0, 'Enter a Search Key')
        self.ClickedWidget = self.SingleSearchEntry
        self.SingleSearchEntry.bind('<Button-1>', self.clicked)
        self.SingleSearchEntry.place(x=380,y=20,width=411,height=31)
        
        
    def __configure_email_entry(self):
        self.EmailEntry = tk.Entry()
        self.EmailEntry.config(  
                                        borderwidth='1px',
                                        font=self.font, 
                                        bg='#303134',
                                        fg='red', 
                                        justify='center', 
                                        
                                    )
        
        
        
    def __configure_phone_entry(self):
        self.PhoneEntry = tk.Entry()
        self.PhoneEntry.config(  
                                        borderwidth='1px',
                                        font=self.font, 
                                        bg='#303134',
                                        fg='red', 
                                        justify='center'
                                    )


    def __configure_visa_entry(self):
        self.VisaEntry = tk.Entry()
        self.VisaEntry.config(  
                                        borderwidth='1px',
                                        font=self.font, 
                                        bg='#303134',
                                        fg='red'
                                    )

        
        
    def __configure_username_entry(self):
        self.UsernameEntry = tk.Entry()
        self.UsernameEntry.config(  
                                        borderwidth='1px',
                                        font=self.font, 
                                        bg='#303134',
                                        fg='red', 
                                        justify='center'                                        
                                    )


    def __show_full_search_widgets(self):
        self.EmailEntry.place(x=10,y=110,width=390,height=30)
        self.PhoneEntry.place(x=10,y=170,width=390,height=30)
        self.VisaEntry.place(x=770,y=110,width=390,height=30)
        self.UsernameEntry.place(x=770,y=170,width=390,height=30)
        
        
    def __remove_full_search_widgets(self):
        for Widget in self.FullSearchWidgets:
            Widget.destroy()
            
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
        self.__configure_switch_mode_btn()


    def SearchBtn_command(self):
        pass


    def switch_mode(self):
        
        if self.AnotherMode.get() == 'Full Search':
            self.AnotherMode.set('Single Search')
            self.SingleSearchEntry.destroy()
            self.__configure_email_entry()
            self.__configure_phone_entry()
            self.__configure_visa_entry()
            self.__configure_username_entry()
            self.__show_full_search_widgets()
            self.FullSearchWidgets = [self.EmailEntry, self.PhoneEntry, self.VisaEntry, self.UsernameEntry]
            
        elif self.AnotherMode.get() == 'Single Search':
            self.AnotherMode.set('Full Search')
            self.__remove_full_search_widgets()
            self.__configure_single_search_entry()

app = App()
app.mainloop()
