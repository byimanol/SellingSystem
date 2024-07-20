from tkinter import ttk,Frame,Label,BooleanVar
from const import *

class ViewCashRegister:
    def __init__(self,MasterView,MasterController,arr=[]): 
        self.view=MasterView  
        self.controller=MasterController  
        self.view.view=MODE_CASH_REGISTER

        if(arr):
            for x in self.view.content_calendar.winfo_children(): x.destroy()
            
            self.allDay=[]
            for x in arr:self.allDay.append((str(x[0]),BooleanVar()))

            for text,value in self.allDay:
                ttk.Checkbutton(self.view.content_calendar, text=text, variable=value, style="Red.TCheckbutton").grid(padx=3,pady=3) 

            return
       
        self.view.clean_content()
        self.content_cash_register = Frame(self.view.content,bg=COLOR_THEME,highlightbackground=COLOR_THEME,highlightthickness=4)
        self.content_cash_register.grid(column=0, row=1,sticky="ew")
        self.content_cash_register.grid_columnconfigure(1, weight=1, uniform="foo")

        Label( self.content_cash_register, text="SELECIONA LAS FACTURAS",bg=COLOR_THEME,fg=COLOR_TEXT_BG, font=TEXT_TITLE).grid(row=0,columnspan=6,sticky="ew",padx=0)

        self.view.option_add('*TCombobox*Listbox.font', TEXT_TITLE)

        self.view.year_register=ttk.Combobox( self.content_cash_register,font=TEXT_TITLE)
        self.view.year_register.grid( row=1,sticky="ew",columnspan=6)
        self.view.year_register.state(['readonly'])

        self.view.month_register=ttk.Combobox( self.content_cash_register,font=TEXT_TITLE)
        self.view.month_register.grid(row=2,sticky="ew",columnspan=6)
        self.view.month_register.state(['readonly'])

        self.view.year_register.bind('<Button-1>',  lambda event: self.controller.ListenEvent(event))
        self.view.month_register.bind('<Button-1>', lambda event: self.controller.ListenEvent(event))

        self.view.content_calendar = Frame(self.content_cash_register,bg=COLOR_THEME, height =200)
        self.view.content_calendar.grid(row=3,columnspan=2,pady=60)

        
        style = ttk.Style()
        style.configure(
            "Red.TCheckbutton",
            background="#3498db",
            foreground="white",
            font=TEXT_TITLE,
            padding=10,
            relief="flat"
        )
        style.map(
            "Red.TCheckbutton",
            background=[('active', '#165b89'), ('selected', '#165b89')],
            foreground=[('active', 'white'), ('selected', 'white')]
        )
        
