from const import *
from views.view_cart import ViewCart
from views.view_checkout import ViewCheckout
from models.db_manager import Mannager
from controllers.controller_totals import ControllerTotals

        
class ControllerCart:
    def __init__(self,MasterView,MasterController,event):
        self.view=MasterView
        self.controller=MasterController
        self.event = event

        self.db=Mannager()

    def action_cart(self):
        if(self.event.keysym == KEY_ENTER and len(self.controller.products_cart)>0 ): return ViewCheckout(self.view,self.controller)
        
        if(self.event.keysym == KEY_UP or self.event.keysym == KEY_DOWN): return self.controller.set_selection_tree(self.view.tablet_cart)

        # Para eliminar un elemento del carrito si esta selecionado
        select=self.view.tablet_cart.selection()
        if(self.event.keysym == KEY_DELETER and select): 
            self.controller.products_cart.pop( self.view.tablet_cart.index(select) )
            
            ControllerTotals(self.view,self.controller)
            ViewCart(self.view,self.controller)

    def search_product(self):
        if(self.event.keysym == KEY_BACK): return ViewCart(self.view,self.controller)
        if(self.event.keysym == KEY_ENTER): return self.add_product_cart()

        if(self.event.keysym == KEY_UP or self.event.keysym == KEY_DOWN): return  self.view.response_search.focus()

        self.view.input_search.focus()
        self.view.response_search.delete(0, "end")

        result=self.db.search_product( self.view.input_search.get())
        for r in result: 
            code,description,*_ = r
            self.view.response_search.insert("end",f'{code} {description}')

    def add_product_cart(self):
        selection=self.view.response_search

        if(selection.curselection()):

            find=selection.get(selection.curselection()[0]).split(" ")[0]
            code,description,cost,price,amount,tax = self.db.search_product(find)[0]
            
            if(int(amount)<=0):return self.view.alert.showwarning(title="Alerta", message="PRODUCTO AGOTADO")

            # Verificacion si ya hay del mismo producto en el carrito
            self.controller.discounts=0
            products=self.controller.products_cart
            for i in range(len(products)):
                if(products[i]["code"]==code):
                    if(products[i]["amount"] >= int(amount)): return self.view.alert.showwarning(title="Alerta", message="LIMITE DE PRODCUTO EXCEDIDOS")   

                    # Unir producto Existente
                    products[i]["amount"]+=1
                    products[i]["total"]=products[i]["amount"]*products[i]["price"]

                    ViewCart(self.view,self.controller)
                    return ControllerTotals(self.view,self.controller)


            # Si es primera vez que se agrega el producto
            products.append(
                {
                    "code":code, 
                    "amount":1, 
                    "cost":float(cost), 
                    "description":description, 
                    "price":float(price), 
                    "tax":float(tax), 
                    "total":float(price)
                }
            )

            ControllerTotals(self.view,self.controller)
            ViewCart(self.view,self.controller)             
