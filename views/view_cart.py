from tkinter import ttk
from const import *


class ViewCart:
    def __init__(self,MasterView,MasterController) -> None:
        self.controller=MasterController
        self.view=MasterView

        self.view.clean_content()
        self.view.view=MODE_TABLET_CART

        columns = ("amount","descr","price","tax","total")

        style = ttk.Style()
        style.theme_use("default")
        style.map("Treeview.Heading", background=[('active', COLOR_THEME)])
        style.configure("Treeview.Heading", background=COLOR_THEME, foreground="white", font=TEXT_NORMAL, borderwidth=0,padding=(0, 5))

        self.view.tablet_cart = ttk.Treeview(self.view.content,columns=columns,show="headings",selectmode="browse")

        self.view.tablet_cart.tag_configure("item",foreground="white",background=COLOR_SELECTION)

        self.view.tablet_cart.heading("amount",text="CANTID")
        self.view.tablet_cart.heading("descr",text="DESCRIPCION")
        self.view.tablet_cart.heading("price",text="UNIT")
        self.view.tablet_cart.heading("tax",text="ITBIS")
        self.view.tablet_cart.heading("total",text="TOTAL")

        self.view.tablet_cart.column("amount", anchor='e')
        self.view.tablet_cart.column("descr",  anchor='w')
        self.view.tablet_cart.column("price", anchor='center')
        self.view.tablet_cart.column("tax", anchor='center')
        self.view.tablet_cart.column("total", anchor='center')
        self.view.tablet_cart.grid(sticky="ew")
        
        style.configure('Treeview', fieldbackground=BG, background=BG,rowheight=50, font=("Helvetica bold", 16))

        for p in self.controller.products_cart:
            self.view.tablet_cart.insert("", "end", values=(p["amount"], p["description"], p["price"], p["tax"], p["total"]),tags=("item",))