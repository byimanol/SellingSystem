from tkinter import messagebox
from tkinter import Tk,Frame,Label,StringVar
from const import *
from PIL import ImageTk, Image 

from controllers.main import Controller
from views.view_cart import ViewCart
from views.view_totals import Totals


class View(Tk):
    def __init__(self):
        super().__init__()
        self.view=""

        self.attributes('-fullscreen', True)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.main_content = Frame(self,bg=BG)
        self.main_content.grid(sticky=("nsew"))

        self.main_content.columnconfigure(0, weight=1)

        try:
            self.logo = Image.open(LOGO_URL)
            self.logo = ImageTk.PhotoImage(self.logo.resize((200, 120)))

            self.label_logo = Label(self.main_content,image=self.logo,bg=BG)
            self.label_logo.grid(column=0, row=0,padx=10, sticky=("nw"))
        except:
            self.label_logo = Label(self.main_content,text="NOT FOUND \nlogo.png", font=TEXT_BIG,bg="BLACK",fg=COLOR_TEXT)
            self.label_logo.grid(column=0, row=0,padx=10,ipady=20,ipadx=20, sticky=("nw"))



        infor_var = StringVar()
        infor_var.set("[DEL]      Eliminar un producto\n[F1]      Agregar un producto\n[F2]      Aplicar un descuento\n[F3]      Modo Inventario\n[F4]      Cuadre Caja\n[F5]      Configuracion")


        Label(self.main_content,textvariable=infor_var,bg=COLOR_THEME,fg=COLOR_TEXT,bd=20, font=TEXT_NORMAL,justify="left").grid(column=0, row=0,sticky=("ne"),padx=10,pady=10)

        # Contenedor Contendio Dinamico
        self.content = Frame(self.main_content,bg=BG)
        self.content.grid(column=0, row=1,sticky="ew")

        self.content.columnconfigure(0, weight=1)
        self.content.rowconfigure(0, weight=1)

        self.alert=messagebox
        self.c=Controller(self)
        Totals(self)
        ViewCart(self,self.c)



    def clean_content(self):
        for x in self.content.winfo_children():
            x.destroy()
