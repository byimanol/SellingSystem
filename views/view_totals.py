from tkinter import Frame, StringVar, Label
from const import *

class Totals:
    def __init__(self,MasterView) -> None:
        self.view = MasterView

        self.content_totals = Frame(self.view.main_content,bg=BG)
        self.content_totals.grid(column=0, row=2,sticky=("w"),padx=30,pady=60) 

        self.view.text_taxs = StringVar()
        self.view.text_taxs.set(f"ITEBIS\n{0.0}")

        Label(self.content_totals,font=TEXT_TITLE,bg=BG,fg=COLOR_TEXT,textvariable=self.view.text_taxs).grid(column=0, row=0,ipadx=50,ipady=10)


        self.view.text_sub_total = StringVar()
        self.view.text_sub_total.set(f"SUB TOTAL\n{0.0}")

        Label(self.content_totals,font=TEXT_TITLE,bg=BG,fg=COLOR_TEXT,textvariable=self.view.text_sub_total).grid(column=0, row=1,ipadx=50,ipady=10)


        self.view.text_discount = StringVar()
        self.view.text_discount.set(f"DESCUENTO\n{0.0}")

        Label(self.content_totals,font=TEXT_TITLE,bg=BG,fg=COLOR_TEXT,textvariable=self.view.text_discount).grid(column=1, row=0,ipadx=50,ipady=10)


        self.view.text_total= StringVar()
        self.view.text_total.set(f"TOTAL\n{0.0}")

        Label(self.content_totals,font=TEXT_TITLE,bg=COLOR_THEME,fg=COLOR_TEXT,textvariable=self.view.text_total).grid(column=1, row=1,ipadx=50,ipady=10)
    





    
        
