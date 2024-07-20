from const import *
from controllers.controller_totals import ControllerTotals
from views.view_cart import ViewCart

class ControllerDiscount:  
    def __init__(self,MasterView,MasterController,event):
        self.view=MasterView
        self.controller=MasterController
        self.event = event


    def action_discount(self):
        if(self.event.keysym == KEY_BACK): return ViewCart(self.view,self.controller) 
           
        input=self.view.input_discount
        
        input.focus()

        # Si el valor no es numerico o decimal sera borrado
        if not (self.controller.is_decimal(input.get())): return input.delete(0, "end")

        if(self.event.keysym == KEY_ENTER):
            if not (len(self.controller.products_cart)): return self.view.alert.showwarning(title="Alerta", message="NO TIENES PRODUCTO EN LA CAJA")
            
            discountsTotal=(self.controller.total*float(input.get())/100)

            # Si el descuento sobre pasa el capital
            if(self.controller.capital>self.controller.total-discountsTotal): return self.view.alert.showwarning(title="Alerta", message="ESTE DESCUENTO ES MUY ALTO")
                    
            self.controller.discounts = float(input.get())

            ControllerTotals(self.view,self.controller)
            return ViewCart(self.view,self.controller)
            