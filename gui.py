# #!/usr/bin/env python3
import tkinter as tk
import tkinter.font as tkFont
from modules.leaksfinder import LeaksFinder 
from modules.search import Search
from threading import Thread 
# countries: Egypt, Cameroon, Algeria,  Austria,  Bahrain,  Belgium, Canada,  China, Cameroon, ShittyIsrael
from multiprocessing import Process
RootBG = '#202124'
class Gui(tk.Tk):

    def __init__(self):
        super().__init__()
        self.Finder = Search()
        self.font = tkFont.Font(family='Times bold',size=16)
        self.__configure_root_window()
        self.__configure_search_btn()
        self.__configure_single_search_entry()
        self.__configure_status_output()
        self.__configure_result_output()
        self.__configure_switch_mode_btn()
        self.__LastStatus = ''
        self.bind('<Return>', self.start_search)
        # test = tk.StringVar(self)
        # message = tk.Message(self)
    
        
    def __configure_root_window(self):
        self.title("Rummage")
        self.config(background=RootBG)
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
                                bg='#0a56ba',
                                fg='white', 
                                justify='center', 
                                text='Search', 
                                font=self.font,
                                command=self.start_search
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
        self.ClickedWidget.delete(0, tk.END)


    def __configure_single_search_entry(self):
        self.SingleSearchEntry = tk.Entry()
        self.SingleSearchEntry.config(  
                                        borderwidth='1px',
                                        font=self.font, 
                                        bg='#303134',
                                        fg='white', 
                                        justify='center',
                                    )
        self.SingleSearchEntry.insert(0, 'Enter a Search Key')
        self.ClickedWidget = self.SingleSearchEntry
        self.SingleSearchEntry.bind('<Button-1>', self.clicked)
        self.SingleSearchEntry.place(x=380,y=20,width=411,height=31)


    def __configure_email_entry(self):
        self.EmailLabel = tk.Label(text='Email: ', 
                                    font=self.font,
                                    fg='white',
                                    background=RootBG)
        self.EmailLabel.place(x=10,y=87)
        self.EmailEntry = tk.Entry()
        self.EmailEntry.config(  
                                        borderwidth='1px',
                                        font=self.font, 
                                        bg='#303134',
                                        fg='white', 
                                        justify='center', 
                                        
                                    )


    def __configure_phone_entry(self):
        self.PhoneLabel = tk.Label(text='Phone Number: ', 
                                    font=self.font,
                                    fg='white',
                                    background=RootBG)
        self.PhoneLabel.place(x=10,y=147)
        self.PhoneEntry = tk.Entry()
        self.PhoneEntry.config(  
                                        borderwidth='1px',
                                        font=self.font, 
                                        bg='#303134',
                                        fg='white',
                                        justify='center'
                                    )


    def __configure_visa_entry(self):
        self.VisaLabel = tk.Label(text='Visa(first 5 number-last 5): *****-*****', 
                                    font=self.font,
                                    fg='white',
                                    background=RootBG)
        self.VisaLabel.place(x=770,y=87)
        self.VisaEntry = tk.Entry()
        self.VisaEntry.config(  
                                        borderwidth='1px',
                                        font=self.font, 
                                        bg='#303134',
                                        fg='white',
                                        justify='center'
                                        
                                    )


    def __configure_username_entry(self):
        self.UsernameLabel = tk.Label(text='Username: ', 
                                    font=self.font,
                                    fg='white',
                                    background=RootBG)
        self.UsernameLabel.place(x=770,y=147)
        self.UsernameEntry = tk.Entry()
        self.UsernameEntry.config(  
                                        borderwidth='1px',
                                        font=self.font, 
                                        bg='#303134',
                                        fg='white', 
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


    def __check_status(self):
        while not LeaksFinder.done:
            if self.__LastStatus != LeaksFinder.GetStatus():
                self.StatusText.config(state='normal')
                self.StatusText.insert(tk.END, (LeaksFinder.GetStatus()))
                self.__LastStatus = LeaksFinder.GetStatus()
                self.StatusText.config(state='disabled')
                
                

    def __configure_status_text(self):
        self.StatusText = tk.Text(
                                    self.StatusOutput,
                                    font=self.font,
                                    bg='#303134',
                                    fg='white'
                                )
        self.StatusText.grid(row=0, column=1)
        
        self.StatusScroll = tk.Scrollbar(self.StatusOutput, command=self.StatusText.yview, background=RootBG, troughcolor=RootBG, activebackground='#e1e1e1')
        self.StatusText.config(yscrollcommand=self.StatusScroll.set, state='disabled')
        self.StatusScroll.grid(row=0, column=0, sticky=tk.NSEW)
        
    



    def __configure_status_output(self):
        self.status = tk.StringVar(self)
        self.StatusOutput = tk.Label()
        self.StatusOutput.config(
            bg='#303134', 
            font=self.font, 
            fg='white',
            textvariable=self.status, 
            anchor='n'
        )
        self.StatusOutput.place(x=10,y=270,width=573,height=453)
        self.__configure_status_text()
        
        self.CheckStatusThread = Thread(target=lambda: self.__check_status())

    


    def __check_result(self):
        while True:
            if LeaksFinder.done:
                self.ResultText.config(state='normal')
                self.ResultText.insert('1.0', LeaksFinder.GetResult())
                self.ResultText.config(state='disabled')
                break
            
            
    def __configure_result_text(self):
        self.ResultText = tk.Text(
                                    self.ResultOutput,
                                    font=self.font,
                                    bg='#303134',
                                    fg='white'
                                )
        self.ResultText.grid(row = 0, column = 1)
        
        self.ResultScroll = tk.Scrollbar(self.ResultOutput, command=self.ResultText.yview, background=RootBG, troughcolor=RootBG, activebackground='#e1e1e1')
        self.ResultText.config(yscrollcommand=self.ResultScroll.set, state='disabled')
        self.ResultScroll.grid(row=0, column=0, sticky=tk.NSEW)



    def __configure_result_output(self):
        self.output = tk.StringVar()
        self.ResultOutput=tk.Label()
        self.CheckOutputThread = Thread(target=lambda: self.__check_result())
        self.ResultOutput.config(
            bg='#303134', 
            font=self.font, 
            fg='white',
            textvariable=self.output, 
            anchor='n'
            
        )
        self.ResultOutput.place(x=590,y=270,width=576,height=452)
        self.__configure_result_text()




    def start_search(self, *event):
        # self.FinderProc = Process(target= lambda: self.Finder.Search(self.SingleSearchEntry.get()))
        # self.FinderProc.start()
        self.StatusText.delete('1.0', tk.END)
        self.ResultText.delete('1.0', tk.END)
        self.FinderThread = Thread(target= lambda: self.Finder.Search(self.SingleSearchEntry.get()))
        self.FinderThread.start()
        self.CheckStatusThread.start()
        self.CheckOutputThread.start()
        
        
    def __switch_to_full_search(self):
            self.AnotherMode.set('Single Search')
            self.SingleSearchEntry.destroy()
            self.__configure_email_entry()
            self.__configure_phone_entry()
            self.__configure_visa_entry()
            self.__configure_username_entry()
            self.__show_full_search_widgets()
            self.FullSearchWidgets = [
                                    self.EmailEntry,
                                    self.PhoneEntry,
                                    self.VisaEntry,
                                    self.UsernameEntry,
                                    self.EmailLabel,
                                    self.PhoneLabel,
                                    self.VisaLabel,
                                    self.UsernameLabel
                                    ]


    def __switch_to_single_search(self):
            self.AnotherMode.set('Full Search')
            self.__remove_full_search_widgets()
            self.__configure_single_search_entry()


    def switch_mode(self):
    
        if self.AnotherMode.get() == 'Full Search':
            self.__switch_to_full_search()
            
        elif self.AnotherMode.get() == 'Single Search':
            self.__switch_to_single_search()
    
    
    # def __del__(self):
        
    #     # self.destroy()
    #     # print('stop now ')
    #     # del self.Finder
    #     # del self.FinderThread

app = Gui()
app.mainloop()