from tkinter import Frame,Entry,Label
from const import *

class ViewCheckout:
    def __init__(self,MasterView,MasterController) -> None:
        self.view=MasterView
        self.controller=MasterController
        self.view.clean_content()
        self.view.view=MODE_CHECKOUT

        self.checkout_content  = Frame(self.view.content,bg=COLOR_THEME,bd=20)
        self.checkout_content.grid(padx=80,pady=80)

        Label( self.checkout_content, text="PAGO CON:",bg=COLOR_THEME,fg=COLOR_TEXT_BG, font=TEXT_TITLE).grid(column=0, row=0,sticky="w")

        self.view.input_checkout=Entry(self.checkout_content,bg=COLOR_THEME,fg=COLOR_TEXT_BG, font=TEXT_TITLE)
        self.view.input_checkout.grid(column=1, row=0)
        self.view.input_checkout.focus()

        Label( self.checkout_content,bg=COLOR_THEME,text="TOTAL:",fg=COLOR_TEXT_BG, font=TEXT_TITLE).grid(column=0, row=1,sticky="w")

        Label( self.checkout_content,bg=COLOR_THEME,text=f"TOTAL\n{"RD${:,.2f}".format(self.controller.total)}",fg=COLOR_TEXT_BG, font=TEXT_BIG).grid(column=1, row=1,sticky="w")  


        Label ( self.checkout_content,bg=COLOR_CANCEL,fg=COLOR_TEXT,text="[ESC] Cancelar ",relief="flat",font=TEXT_TITLE).grid(column=0, row=2,padx=10,pady=10,ipadx=10,ipady=10)

        Label ( self.checkout_content,bg=COLOR_TEXT_BG,fg=COLOR_THEME,text="[ENTER] Aceptar",relief="flat",font=TEXT_TITLE).grid(column=1, row=2,padx=10,pady=10,ipadx=10,ipady=10)