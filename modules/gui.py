# Omar Ameer 
# class methods: 
# StartUI


# ! https://github.com/rdbende/Azure-ttk-theme

# class attributes:
# SearchLevel
from tkinter import Tk, Entry, Label, Scale, StringVar, Frame, LEFT, RIGHT, X, Y, TOP, SOLID, DoubleVar, ttk, Button, Scrollbar, HORIZONTAL, VERTICAL, BOTTOM, NO, W

from ttkthemes import ThemedTk
class GUI(ThemedTk):


    def __init__(self):
        super().__init__()
        self.Themes = [
            'adapta', 'alt', 'aquativo', 'arc', 'breeze', 'black', 'blue', 'clam', 'classic', 'clearlooks',
            'default',
            'equilux', 'itft1', 'keramik', 'keramik_alt', 'kroc', 'plastik', 'radiance', 'scidblue',
            'scidgreen',
            'scidgrey', 'scidmint', 'scidpink', 'scidpurple', 'scidsand', 'smog', 'winxpblue', 'yaru'
            ]
        self.theme = self.Themes[18]
        self.SelectedTheme = StringVar()
        self.ThemesCombo = ttk.Combobox()
        self.ThemeLabel = ttk.Label()
        self.style = ttk.Style()
        
        self.ThemesCombo.pack()        
        self.ThemeLabel.place(x=230, y=1)
        self.ThemesCombo.config(values=self.Themes,
                                textvariable=self.SelectedTheme,
                                state='readonly')
        self.ThemesCombo.current(18)
        self.SelectedTheme.trace('w',
                            self.change_theme)
        
        # creating window

        # setting width and height for window
        self.geometry('1350x690+1+1')
        # setting title for window
        self.title("Rummage")
        # variables for storing input
        self.__FullSearch = StringVar()
        self.__fname = StringVar()
        self.__Name = StringVar()
        self.__Phone = StringVar()



        # creating frames for layout
        # topview frame for heading
        TopViewForm = Frame(self, width=600, bd=1, relief=SOLID)
        
        # first left frame for registration from
        self.FullSearchForm = Frame(self, width="350", bg="#15244C")
        self.FullSearchForm.pack(side=LEFT, fill=Y)
        # second left frame for search form
        self.SearchForm = Frame(self, width=500, bg="#0B4670")
        self.SearchForm.pack(side=LEFT, fill=Y)
        # mid frame for displaying Names record
        MidViewForm = Frame(self, width=600)
        MidViewForm.pack(side=RIGHT)
        # label for heading
        lbl_text = Label(TopViewForm, text="Rummage", font=('verdana', 18), width=600, bg="cyan")
        lbl_text.pack(fill=X)
        # creating registration form in first left frame
        Label(self.FullSearchForm, text="Full Search  ", font=("Arial", 16, "bold"), bg="#15244C", fg="white").pack(side=TOP)
        Label(self.FullSearchForm, text="Name  ", font=("Arial", 12), bg="#15244C", fg="white").pack(side=TOP)
        Entry(self.FullSearchForm, font=("Arial", 10, "bold"), textvariable=self.__fname).pack(side=TOP, padx=10, fill=X)
        Label(self.FullSearchForm, text="Email ", font=("Arial", 12), bg="#15244C", fg="white").pack(side=TOP)
        Entry(self.FullSearchForm, font=("Arial", 10, "bold"), textvariable=self.__Name).pack(side=TOP, padx=10, fill=X)
        Label(self.FullSearchForm, text="Visa Card ", font=("Arial", 12), bg="#15244C", fg="white").pack(side=TOP)
        Entry(self.FullSearchForm, font=("Arial", 10, "bold"), textvariable=self.__Name).pack(side=TOP, padx=10, fill=X)
        hVar1 = DoubleVar()  # left handle variable
        hVar2 = DoubleVar()  # right handle variable

        # search_level = Scale(self, [hVar1, hVar2], Width=400, Height=60, min_val=0, max_val=400, show_value=True)
        # search_level.pack()

        Label(self.FullSearchForm, text="Country ", font=("Arial", 12), bg="#15244C", fg="white").pack(side=TOP)
        Label(self.FullSearchForm, text="Phone Number", font=("Arial", 12), bg="#15244C", fg="white").pack(side=TOP)
        Entry(self.FullSearchForm, font=("Arial", 10, "bold"), textvariable=self.__Phone).pack(side=TOP, padx=10, fill=X)
        Button(self.FullSearchForm, text="Search", font=("Arial", 10, "bold"),  bg="#15244C", fg="white").pack(
            side=TOP, padx=10, pady=5, fill=X)

        # creating search label and entry in second frame
        lbl_txtsearch = Label(self.SearchForm, text="Search By ", font=('verdana', 10), bg="#0B4670", fg="white")
        lbl_txtsearch.pack()
        combo_search = ttk.Combobox(self.SearchForm, justify='left', state='readonly')
        self.search_by1 = combo_search
        combo_search['value'] = ('Name', 'Email', 'Phone Number', 'Visa Card')
        combo_search.pack(side=TOP, padx=10, fill=X)
        lbl_txtsearch = Label(self.SearchForm, text="Enter Value To Search", font=('verdana', 10), bg="#0B4670", fg="white")
        lbl_txtsearch.pack()
        __FullSearch = Entry(self.SearchForm, textvariable=self.__FullSearch, font=('verdana', 15), width=10)
        __FullSearch.pack(side=TOP, padx=10, fill=X)
        # creating search button
        btn_search = Button(self.SearchForm, text="Search",  bg="cyan")
        btn_search.pack(side=TOP, padx=10, pady=10, fill=X)
        # creating view button
        btn_view = Button(self.SearchForm, text="View All",  bg="cyan")
        btn_view.pack(side=TOP, padx=10, pady=10, fill=X)
        # creating reset button
        btn_reset = Button(self.SearchForm, text="Reset",  bg="cyan")
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
        
    def __SetDefaultValues(self):
        pass


    def change_theme(self, *args):
        self.theme = self.Themes[self.Themes.index(self.SelectedTheme.get())]
        self.config(theme=self.theme, themebg=True)
        self.style.theme_use(self.theme)
        self.ThemeLabel.config(background=self.style.lookup('TFrame', 'background'),
                            foreground=self.style.lookup('TFrame', 'foreground')
                            )
        

gui = GUI()

gui.mainloop()
# TopViewForm.pack(side=TOP, fill=X)