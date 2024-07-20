from tkinter import ttk,Frame, Entry, Label
from const import *

class ViewInventory:
    def __init__(self,MasterView) -> None:
        self.view = MasterView
        self.view.clean_content()
        self.view.view=MODE_INVENTORY

        self.content_inventory = Frame(self.view.content,bg='white',highlightbackground=COLOR_THEME,highlightthickness=4)
        self.content_inventory.grid(column=0, row=0,sticky="ew")
        self.content_inventory.columnconfigure(0, weight=1)

        Label( self.content_inventory, text="INVENTARIO",bg=COLOR_THEME,fg=COLOR_TEXT_BG, font=TEXT_TITLE).grid(column=0, row=0,sticky="ew",padx=0,ipady=15)

        self.view.input_find=Entry(self.content_inventory)
        self.view.input_find.grid(column=0, row=1,sticky="ew",ipadx=10,ipady=10) 
        self.view.input_find.focus()

        columns = ("code","amount","descr","cost","price","tax","total")

        style = ttk.Style()
        style.theme_use("default")
        style.map("Treeview.Heading", background=[('active', COLOR_THEME)])
        style.configure("Treeview", font=("Helvetica", 12))
        style.configure("Treeview.Heading", background=COLOR_THEME, foreground="white", font=TEXT_NORMAL, borderwidth=0,padding=(0, 5))
        self.view.tablet_inventory = ttk.Treeview(self.content_inventory,columns=columns,show="headings",selectmode="browse")

        self.view.tablet_inventory.tag_configure("item",foreground="white",background=COLOR_SELECTION)
        self.view.tablet_inventory.tag_configure("empty",foreground="white",background=COLOR_CANCEL)


        self.view.tablet_inventory.heading("code",text="CODE")
        self.view.tablet_inventory.heading("amount",text="CANT.")
        self.view.tablet_inventory.heading("descr",text="DESCRIPCION")
        self.view.tablet_inventory.heading("cost",text="COSTO")
        self.view.tablet_inventory.heading("price",text="PRECIO")
        self.view.tablet_inventory.heading("tax",text="ITEBIS")
        self.view.tablet_inventory.heading("total",text="TOTAL CAPITAL")


        self.view.tablet_inventory.column("code", anchor='w')
        self.view.tablet_inventory.column("amount",  anchor='center')
        self.view.tablet_inventory.column("descr", anchor='w')
        self.view.tablet_inventory.column("cost", anchor='center')
        self.view.tablet_inventory.column("price", anchor='center')
        self.view.tablet_inventory.column("tax", anchor='center')
        self.view.tablet_inventory.column("total",  anchor='center')

        self.view.tablet_inventory.grid(column=0, row=2,sticky="ew")