from tkinter import Frame, Entry, Label
from const import *

class ViewDiscount:
    def __init__(self,MasterView) -> None:
        self.view=MasterView
        self.view.clean_content()
        self.view.view=MODE_DISCOUNT

        self.content_discount = Frame(self.view.content,bg=COLOR_THEME,highlightbackground=COLOR_THEME)
        self.content_discount.grid(column=0, row=1,sticky="ew",padx=80,pady=80)
        self.content_discount.grid_columnconfigure(0, weight=1, uniform="foo")
        
        Label(self.content_discount, text="DIGITE EL DESCUENTO (EN %)",bg=COLOR_THEME,fg=COLOR_TEXT_BG, font=TEXT_TITLE).grid(column=0, row=0,sticky="ew",columnspan=2) 

        self.view.input_discount=Entry(self.content_discount,font=TEXT_BIG,justify="center")
        self.view.input_discount.grid(column=0, row=1,sticky="ew",ipady=20) 
        self.view.input_discount.focus() 
        
        Label(self.content_discount,text="CANCELAR [ESC]",font=TEXT_TITLE,relief="flat",bg=COLOR_CANCEL,fg='white').grid(column=0, row=2,sticky="w",ipadx=10,ipady=10,padx=10,pady=10) 
        Label(self.content_discount,text="APLICAR [ENTER]",font=TEXT_TITLE,relief="flat",bg=COLOR_TEXT_BG,fg=COLOR_THEME).grid(column=0, row=2,sticky="e",ipadx=10,ipady=10,padx=10,pady=10) 
