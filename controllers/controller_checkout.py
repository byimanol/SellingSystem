from const import *
from controllers.controller_totals import ControllerTotals
from models.db_manager import Mannager
from models.ticket_shop import TicketShop
from models.print import Print
from views.view_cart import ViewCart
from views.view_finish import ViewFinish

class ControllerCheckeout:  
    def __init__(self,MasterView,MasterController,event):
        self.view=MasterView
        self.controller=MasterController
        self.event = event

        self.db=Mannager()

    def action_checkout(self):
        if(self.event.keysym == KEY_BACK): return ViewCart(self.view,self.controller)

        cash=self.view.input_checkout
        if not ( self.controller.is_decimal( cash.get() ) ): return cash.delete(0, "end")

        if(self.event.keysym == KEY_ENTER): 
            if(float(cash.get()) < self.controller.total ): return self.view.alert.showwarning(title="Alerta", message="ERROR EL EFECTIVO NO AL CANSA PARA EL TOTAL")

            result=self.db.save_invoice(self.controller.total, self.controller.capital, self.controller.subtotal, self.controller.discounts, self.controller.products_cart,float(cash.get()), self.controller.taxs)

            for p in self.controller.products_cart:
                decrease=p["amount"]
                code=p["code"]
                
                self.db.update_amount_product(code,decrease)

            if not (result): return self.view.alert.showwarning(title="Alerta", message="ERROR AL GENERAR LA FACTURA REVISA TU FECHA")

            # IMPRIMIR FACTURA
            ticket=TicketShop(self.controller.total, self.controller.taxs, cash.get(), self.controller.products_cart)
            ticket.generate_shop_ticket()
            generate_text=ticket.print()
            print_execute=Print(self.controller).print_ticket(generate_text)
  
            if not (print_execute): return self.view.alert.showwarning(title="Alerta", message="ERROR ASEGURATE HABER SELECIONADO UNA IMPRESORA EN CONFIGURACION")

            self.controller.products_cart=[]  
            ControllerTotals(self.view,self.controller)
            return ViewFinish(self.view,float(cash.get()),self.controller.total)

    def action_finish(self):
        if(self.event.keysym == KEY_ENTER): return ViewCart(self.view,self.controller)
