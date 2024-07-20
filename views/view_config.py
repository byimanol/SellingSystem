from tkinter import ttk,Frame,BooleanVar,Label,Entry
from const import *

class ViewConfig:
    def __init__(self,MasterView,MasterController) -> None:
        self.view = MasterView
        self.controller = MasterController
        self.view.clean_content()
        self.view.view = MODE_CONFIG

        self.content_config = Frame(self.view.content,bg=BG)
        self.content_config.grid(padx=20,pady=20)

        style = ttk.Style()
        style.theme_use("alt")

        self.view.pass_invetory = BooleanVar()
        self.view.pass_invetory.set(self.controller.config["pass_invetory"])
        
        ttk.Checkbutton(self.content_config, text="Solicitad contraseñas para poder ver el inventario", variable=self.view.pass_invetory, style='Custom.TCheckbutton').grid(row=0,padx=5,pady=5,sticky="w") 

        self.view.pass_discount = BooleanVar()
        self.view.pass_discount.set(self.controller.config["pass_discount"])

        ttk.Checkbutton(self.content_config, text="Solicitad contraseñas para poder aplicar descuento", variable=self.view.pass_discount, style='Custom.TCheckbutton').grid(row=1,padx=5,pady=5,sticky="w") 

        self.view.pass_registerCash = BooleanVar()
        self.view.pass_registerCash.set(self.controller.config["pass_registerCash"])

        ttk.Checkbutton(self.content_config, text="Solicitad contraseñas para poder hacer un cuadre", variable=self.view.pass_registerCash, style='Custom.TCheckbutton').grid(row=3,padx=5,pady=5,sticky="w") 

        Label( self.content_config, text="Seleciona una impresora",bg=COLOR_THEME,fg=COLOR_TEXT_BG, font=TEXT_NORMAL).grid(row=4,sticky="nw")
        
        self.view.print_select = ttk.Combobox( self.content_config,font=TEXT_TITLE)
        self.view.print_select.grid( row=5,sticky="ew",columnspan=6)
        self.view.print_select.state(['readonly'])

        self.view.print_select.bind('<Button-1>', lambda event: self.controller.ListenEvent(event))

        Label( self.content_config, text="Introduce una contrasena para proteger el sistema",bg=COLOR_THEME,fg=COLOR_TEXT_BG, font=TEXT_NORMAL).grid(row=6,sticky="nw")

        self.view.input_pass=Entry(self.content_config)
        self.view.input_pass.grid(row=7,sticky="ew",ipadx=10,ipady=10) 
        self.view.input_pass.insert(0,self.controller.config["password"])
 


        style = ttk.Style()
        style.configure("Custom.TCheckbutton", font=TEXT_NORMAL,background=BG,foreground="#7d8597")

        style.map("Custom.TCheckbutton",background=[("active", BG)])