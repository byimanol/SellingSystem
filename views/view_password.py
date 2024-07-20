from tkinter import Frame,Label,Entry
from const import *

class ViewPassword:
    def __init__(self,MasterView) -> None:
        self.view = MasterView
        self.view.clean_content()
        self.view.view = MODE_PASSWORD

        self.content_password=Frame(self.view.content,background=COLOR_THEME,bd=20)
        self.content_password.grid(padx=10,pady=10)

        Label(self.content_password,text="Introduce La contrasena",font=TEXT_BIG,background=COLOR_THEME,foreground=COLOR_TEXT).grid(row=0)

        self.view.permiss_password=Entry(self.content_password,bg=COLOR_THEME,fg=COLOR_TEXT_BG, font=TEXT_TITLE)
        self.view.permiss_password.grid(row=1)
        self.view.permiss_password.focus() 

        Label(self.content_password,text="ACEPTAR [ENTER]",font=TEXT_TITLE,background=COLOR_TEXT,foreground=COLOR_THEME).grid(row=2,padx=10,pady=10)

