from tkinter import Frame,Label
from const import *

class ViewFinish:
    def __init__(self,MasterView,money=0,total=0) -> None:
        self.view = MasterView
        self.view.clean_content()
        self.view.view = MODE_FINISH

        self.alert_finish  = Frame(self.view.content,bg=COLOR_THEME,bd=20)
        self.alert_finish.grid(padx=80,pady=80)

        Label( self.alert_finish, text="TOTAL:",bg=COLOR_THEME,fg=COLOR_TEXT_BG, font=TEXT_TITLE).grid(column=0, row=1,sticky="nw")

        Label( self.alert_finish,bg=COLOR_THEME,text=f"{total}",fg=COLOR_TEXT_BG, font=TEXT_BIG).grid(column=1, row=1,sticky="W")

        Label( self.alert_finish, text="PAGO CON:",bg=COLOR_THEME,fg=COLOR_TEXT_BG, font=TEXT_TITLE).grid(column=0, row=2,sticky="nw")

        Label( self.alert_finish, text=f"{money}",bg=COLOR_THEME,fg=COLOR_TEXT_BG, font=TEXT_BIG).grid(column=1, row=2,sticky="nw")

        Label( self.alert_finish, text="DEVUELTA:",bg=COLOR_THEME,fg=COLOR_TEXT_BG, font=TEXT_TITLE).grid(column=0, row=3,sticky="nw")

        Label( self.alert_finish, text=f"{money-total}",bg=COLOR_THEME,fg=COLOR_TEXT_BG, font=TEXT_BIG).grid(column=1, row=3,sticky="nw")

        Label(self.alert_finish,bg="white",fg=COLOR_THEME,text="Aceptar[ENTER]",relief="flat",font=TEXT_TITLE).grid(column=0, row=4,sticky="EW",padx=20,pady=20,ipadx=10,ipady=10)

