from const import *
from views.view_cart import ViewCart
from views.view_cash_register import ViewCashRegister
from models.db_manager import Mannager
from models.ticket_register import TicketRegister
from models.print import Print

class ControllerCashRegister:  
    def __init__(self,MasterView,MasterController,event):
        self.view=MasterView
        self.controller=MasterController
        self.event = event

        self.db=Mannager()

    def action_cash_Register(self):
        i_year=self.view.year_register
        i_month=self.view.month_register

        if(self.event.keysym == KEY_BACK): return ViewCart(self.view,self.controller)
             
        if(self.event.keysym == KEY_ENTER and self.controller.calendarDays):
            allDay=['']
        
            for day,value in self.controller.calendarDays:
                if(value.get()): allDay.append(str(day))
                
            if(len(allDay)<=1): return 
            
            # IMPRIMIR REGISTRO DE VENTA
            result=self.db.find_all_day(i_year.get(),i_month.get(),allDay)
            if not (result): return
            
            register=TicketRegister(result,i_month.get())
            register.generate_shop_ticket()

            generate_text=register.print()
            print_execute=Print(self.controller).print_ticket(generate_text)

            if not (print_execute): return self.view.alert.showwarning(title="Alerta", message="ASEGURA HABER SELECIONADO LA IMPRESSORA EN CONFIG")
            return 
        

        if not(self.event.keysym == "??"): return

        if not ( len(i_year['values'])>0): 
            i_year['values'] = tuple(self.db.find_year())
            return
        
        if (i_year.get() and len(i_month['values'])<=0):
            i_month['values'] = tuple(self.db.find_month(i_year.get()))
            return
        
        if ( i_year.get() and i_month.get() ):
            r=self.db.find_day(i_year.get(),i_month.get())
            self.controller.calendarDays=ViewCashRegister(self.view,self.controller,r).allDay
