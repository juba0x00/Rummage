# Omar Ameer 
# class methods: 
# StartUI

# class attributes:
# SearchLevel
from ttkthemes import ThemedTk
class GUI(ThemedTk):
    def __init__(self):
        # import libraries
        # tkinter for GUI
        from tkinter import *
        import tkinter.ttk as ttk

    def __init__(self):
        # creating window
        self.__display_screen = Tk()
        # setting width and height for window
        self.__display_screen.geometry('1350x690+1+1')
        # setting title for window
        self.__display_screen.title("Leaks Finder")
        # variables for storing input
        self.__FullSearch = StringVar()
        self.__fname = StringVar()
        self.__lname = StringVar()
        self.__gender = StringVar()
        self.__address = StringVar()
        self.__phone = StringVar()
        self.__search_by1 = StringVar()
        self.__search_level = StringVar()


        # creating frames for layout
        # topview frame for heading
        TopViewForm = Frame(self.__display_screen, width=600, bd=1, relief=SOLID)
        TopViewForm.pack(side=TOP, fill=X)
        # first left frame for registration from
        LFrom = Frame(self.__display_screen, width="350", bg="#15244C")
        LFrom.pack(side=LEFT, fill=Y)
        # second left frame for search form
        LeftViewForm = Frame(self.__display_screen, width=500, bg="#0B4670")
        LeftViewForm.pack(side=LEFT, fill=Y)
        # mid frame for displaying lnames record
        MidViewForm = Frame(self.__display_screen, width=600)
        MidViewForm.pack(side=RIGHT)
        # label for heading
        lbl_text = Label(TopViewForm, text="Leaks Finder", font=('verdana', 18), width=600, bg="cyan")
        lbl_text.pack(fill=X)
        # creating registration form in first left frame
        Label(LFrom, text="Full Search  ", font=("Arial", 16, "bold"), bg="#15244C", fg="white").pack(side=TOP)
        Label(LFrom, text="Name  ", font=("Arial", 12), bg="#15244C", fg="white").pack(side=TOP)
        Entry(LFrom, font=("Arial", 10, "bold"), textvariable=self.__fname).pack(side=TOP, padx=10, fill=X)
        Label(LFrom, text="Email ", font=("Arial", 12), bg="#15244C", fg="white").pack(side=TOP)
        Entry(LFrom, font=("Arial", 10, "bold"), textvariable=self.__lname).pack(side=TOP, padx=10, fill=X)
        Label(LFrom, text="Visa Card ", font=("Arial", 12), bg="#15244C", fg="white").pack(side=TOP)
        Entry(LFrom, font=("Arial", 10, "bold"), textvariable=self.__lname).pack(side=TOP, padx=10, fill=X)
        hVar1 = DoubleVar()  # left handle variable
        hVar2 = DoubleVar()  # right handle variable

        search_level = scale(__display_screen, [hVar1, hVar2], Width=400, Height=60, min_val=0, max_val=400, show_value=True)
        rs1.pack()

        Label(LFrom, text="Country ", font=("Arial", 12), bg="#15244C", fg="white").pack(side=TOP)
        Entry(LFrom, font=("Arial", 10, "bold"), textvariable=self.__address).pack(side=TOP, padx=10, fill=X)
        Label(LFrom, text="Phone Number", font=("Arial", 12), bg="#15244C", fg="white").pack(side=TOP)
        Entry(LFrom, font=("Arial", 10, "bold"), textvariable=self.__phone).pack(side=TOP, padx=10, fill=X)
        Button(LFrom, text="Search", font=("Arial", 10, "bold"),  bg="#15244C", fg="white").pack(
            side=TOP, padx=10, pady=5, fill=X)

        # creating search label and entry in second frame
        lbl_txtsearch = Label(LeftViewForm, text="Search By ", font=('verdana', 10), bg="#0B4670", fg="white")
        lbl_txtsearch.pack()
        combo_search = ttk.Combobox(LeftViewForm, justify='left', state='readonly')
        self.search_by1 = combo_search
        combo_search['value'] = ('Name', 'Email', 'Phone Number', 'Visa Card')
        combo_search.pack(side=TOP, padx=10, fill=X)
        lbl_txtsearch = Label(LeftViewForm, text="Enter Value To Search", font=('verdana', 10), bg="#0B4670", fg="white")
        lbl_txtsearch.pack()
        __FullSearch = Entry(LeftViewForm, textvariable=self.__FullSearch, font=('verdana', 15), width=10)
        __FullSearch.pack(side=TOP, padx=10, fill=X)
        # creating search button
        btn_search = Button(LeftViewForm, text="Search",  bg="cyan")
        btn_search.pack(side=TOP, padx=10, pady=10, fill=X)
        # creating view button
        btn_view = Button(LeftViewForm, text="View All",  bg="cyan")
        btn_view.pack(side=TOP, padx=10, pady=10, fill=X)
        # creating reset button
        btn_reset = Button(LeftViewForm, text="Reset",  bg="cyan")
        btn_reset.pack(side=TOP, padx=10, pady=10, fill=X)
        # setting scrollbar
        scrollbarx = Scrollbar(MidViewForm, orient=HORIZONTAL)
        scrollbary = Scrollbar(MidViewForm, orient=VERTICAL)
        self.__tree = ttk.Treeview(MidViewForm, columns=("Id", "FirstName", "LastName", "Gender", "Address", "Contact"),
                                   selectmode="extended", height=100, yscrollcommand=scrollbary.set,
                                   xscrollcommand=scrollbarx.set)
        scrollbary.config(command=self.__tree.yview)
        scrollbary.pack(side=RIGHT, fill=Y)
        scrollbarx.config(command=self.__tree.xview)
        scrollbarx.pack(side=BOTTOM, fill=X)
        # setting headings for the columns
        self.__tree.heading('Id', text="Something", anchor=W)
        self.__tree.heading('FirstName', text="Something", anchor=W)
        self.__tree.heading('LastName', text="Something", anchor=W)
        self.__tree.heading('Gender', text="Something", anchor=W)
        self.__tree.heading('Address', text="Something", anchor=W)
        self.__tree.heading('Contact', text="Something", anchor=W)
        # setting width of the columns
        self.__tree.column('#0', stretch=NO, minwidth=0, width=120)
        self.__tree.column('#1', stretch=NO, minwidth=0, width=120)
        self.__tree.column('#2', stretch=NO, minwidth=0, width=120)
        self.__tree.column('#3', stretch=NO, minwidth=0, width=130)
        self.__tree.column('#4', stretch=NO, minwidth=0, width=120)
        self.__tree.pack()
        #self.DisplayData()
        self.__display_screen.mainloop()



        super().__init__()

        self.Themes = [
            'adapta', 'alt', 'aquativo', 'arc', 'breeze', 'black', 'blue', 'clam', 'classic', 'clearlooks',
            'default',
            'equilux', 'itft1', 'keramik', 'keramik_alt', 'kroc', 'plastik', 'radiance', 'scidblue',
            'scidgreen',
            'scidgrey', 'scidmint', 'scidpink', 'scidpurple', 'scidsand', 'smog', 'winxpblue', 'yaru'
            ]
        self.theme = self.Themes[18]
        self.mainloop()
        
        GUI()
