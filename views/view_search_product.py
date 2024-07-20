from tkinter import Frame, Entry, Label,Listbox
from const import *

class ViewSearchProduct:
    def __init__(self, MasterView) -> None:
        self.view = MasterView


        self.view.clean_content()
        self.view.view = MODE_SEARCH_PRODUCT

        self.content_search = Frame(self.view.content,bg=COLOR_TEXT,highlightbackground=COLOR_THEME,highlightthickness=4)
        self.content_search.grid(column=0, row=1,sticky="ew")
        self.content_search.grid_columnconfigure(1, weight=1, uniform="foo")
        
        Label( self.content_search, text="BUSCA UN PRODUCTO",bg=COLOR_THEME,fg=COLOR_TEXT, font=TEXT_TITLE).grid(column=0, row=0,columnspan=6,sticky="ew",padx=0,ipady=15)

        Label( self.content_search, text="PRODUCTO",bg=COLOR_THEME,fg=COLOR_TEXT, font=TEXT_NORMAL).grid(column=0, row=1,sticky="ew") 

        self.view.input_search=Entry(self.content_search)
        self.view.input_search.grid(column=1, row=1,sticky="ew") 
        self.view.input_search.focus()

        self.view.response_search=Listbox(self.content_search,width=40,font=TEXT_NORMAL,bg=COLOR_THEME,fg=COLOR_TEXT,relief="flat",highlightbackground=COLOR_TEXT,selectbackground="#afaeb1",activestyle="none",highlightthickness="0",)

        self.view.response_search.grid(column=0, row=2,columnspan=2,sticky="ew")   
