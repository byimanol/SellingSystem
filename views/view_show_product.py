from tkinter import Frame, Entry, Label,StringVar
from const import *

class ViewShowProduct:
    def __init__(self, MasterView, mode=MODE_PRODUCT_INVENTORY_NEW) -> None:
        self.view = MasterView
        self.view.clean_content()
        self.view.view=mode

        self.content_product = Frame(self.view.content,bg='white',highlightbackground=COLOR_THEME,highlightthickness=4)
        self.content_product.grid(column=0, row=1,sticky="ew")
        self.content_product.grid_columnconfigure(1, weight=1, uniform="foo")


        self.view.title_var = StringVar()
        Label( self.content_product, textvariable=self.view.title_var,bg=COLOR_THEME,fg=COLOR_TEXT_BG, font=TEXT_TITLE).grid(column=0, row=0,columnspan=6,sticky="ew",padx=0,ipady=15)


        Label(self.content_product, text="CODIGO",bg=COLOR_THEME,fg=COLOR_TEXT_BG, font=TEXT_NORMAL).grid(column=0, row=1,ipadx=10,ipady=10,sticky="ew")
        
        self.view.input_code =Entry(self.content_product)
        self.view.input_code.grid(column=1, row=1,sticky="ew",ipadx=10,ipady=10) 


        Label( self.content_product, text="DESCRIPCION",bg=COLOR_THEME,fg=COLOR_TEXT_BG, font=TEXT_NORMAL).grid(column=0, row=2,ipadx=10,ipady=10,sticky="ew")

        self.view.input_descr=Entry(self.content_product)
        self.view.input_descr.grid(column=1, row=2,sticky="ew",ipadx=10,ipady=10) 


        Label( self.content_product, text="COSTO",bg=COLOR_THEME,fg=COLOR_TEXT_BG, font=TEXT_NORMAL).grid(column=0, row=3,ipadx=10,ipady=10,sticky="ew")

        self.view.input_cost=Entry(self.content_product)
        self.view.input_cost.grid(column=1, row=3,sticky="ew",ipadx=10,ipady=10) 


        Label( self.content_product, text="PRECIO",bg=COLOR_THEME,fg=COLOR_TEXT_BG, font=TEXT_NORMAL).grid(column=0, row=4,ipadx=10,ipady=10,sticky="ew")

        self.view.input_price=Entry(self.content_product, font=TEXT_NORMAL) 
        self.view.input_price.grid(column=1, row=4,sticky="ew",ipadx=10,ipady=10)


        Label( self.content_product, text="CANTIDAD",bg=COLOR_THEME,fg=COLOR_TEXT_BG, font=TEXT_NORMAL).grid(column=0, row=6,ipadx=10,ipady=10,sticky="ew")
        
        self.view.input_amount=Entry(self.content_product)
        self.view.input_amount.grid(column=1, row=6,sticky="ew",ipadx=10,ipady=10) 


        Label( self.content_product, text="ITEBIS",bg=COLOR_THEME,fg=COLOR_TEXT_BG, font=TEXT_NORMAL).grid(column=0, row=7,ipadx=10,ipady=10,sticky="ew")

        self.view.input_tax=Entry(self.content_product)
        self.view.input_tax.grid(column=1, row=7,sticky="ew",ipadx=10,ipady=10)  


        Label( self.content_product, text="GANACIA EN %",bg=COLOR_THEME,fg=COLOR_TEXT_BG, font=TEXT_NORMAL).grid(column=0, row=8,ipadx=10,ipady=10,sticky="ew")

        self.view.input_gainer=Entry(self.content_product)
        self.view.input_gainer.grid(column=1, row=8,sticky="ew",ipadx=10,ipady=10)  

    
