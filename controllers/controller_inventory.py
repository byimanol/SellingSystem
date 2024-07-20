from const import *
from views.view_show_product import ViewShowProduct
from views.view_cart import ViewCart
from views.view_inventory import ViewInventory
from models.db_manager import Mannager


class ControllerInventory:  
    def __init__(self,MasterView,MasterController,event):
        self.view=MasterView
        self.controller=MasterController
        self.event = event

        self.db=Mannager()


    def action_invetory(self):
        tablet=self.view.tablet_inventory

        if(self.event.keysym == BIND_ADD_PRODUCTO): return self.new_product()
        if(self.event.keysym == KEY_BACK): return ViewCart(self.view,self.controller)
        if(self.event.keysym == KEY_ENTER and tablet.selection()): return self.edit_product()
        if(self.event.keysym == KEY_DELETER and tablet.selection()): return self.deleter_product()

        if(self.event.keysym == KEY_UP or self.event.keysym == KEY_DOWN): return self.controller.set_selection_tree(tablet)

        self.view.input_find.focus()

        # Eliminar todo el contenido de la tabla inventario
        for row in tablet.get_children(): tablet.delete(row)
        
        # Busqueda y inserccion de datos en la tabla inventario
        result=self.db.search_product(self.view.input_find.get())
        for p in result:
            code,description,cost,price,amount,tax = p  
            
            # Si el producto ya se ha acabado
            tag="empty" if int(amount)<=0 else "item"

            tablet.insert("", "end", values=(code, int(amount), description, float(cost), float(price), float(tax), float(amount)*float(cost) ),tags=(tag,) )

    def action_show_invetory(self):
        if(self.event.keysym == KEY_BACK): return ViewInventory(self.view)
        
        cost = self.view.input_cost
        price= self.view.input_price
        gainer = self.view.input_gainer
        widget = self.event.widget

        if (widget==gainer and self.event.keysym == KEY_ENTER): 
            if not(self.controller.is_decimal(gainer.get())): return
            if not(self.controller.is_decimal(price.get())): return
            if not(self.controller.is_decimal(cost.get())): return 
            
            # Aqui va la formula para carcula la ganancia
            gainer_money=( float(gainer.get()) / 100 ) * float(cost.get())
            new_value=float(price.get())+gainer_money

            price.delete(0,"end")
            price.insert(0,new_value)
            return

        if (self.event.keysym == KEY_ENTER): 
            product = self.view.input_code.get()
            descrt = self.view.input_descr.get()
            cost = self.view.input_cost.get()
            price = self.view.input_price.get()
            amount = self.view.input_amount.get()
            tax = self.view.input_tax.get()
            gainer = self.view.input_gainer.get()
        


            
            if not (product.isnumeric()): return self.view.alert.showwarning(title="Alerta", message="[CODIGO] SE PUEDE INTRODUCIR NUMERO EJEMPLO: 1234")

            if not (amount.isnumeric()): return self.view.alert.showwarning(title="Alerta", message="[CANTIDAD] SE PUEDE INTRODUCIR NUMERO EJEMPLO: 1234")

            if not (self.controller.is_decimal(cost)): return self.view.alert.showwarning(title="Alerta", message="[COSTO] SOLO SE PUEDE INTRODUCIR NUMERO O DECIMALES EJEMPLO: 12.34")

            if not (self.controller.is_decimal(price)):return self.view.alert.showwarning(title="Alerta", message="[PRECIO] SOLO SE PUEDE INTRODUCIR NUMERO O DECIMALES EJEMPLO: 12.34")

            if not (self.controller.is_decimal(tax)): return self.view.alert.showwarning(title="Alerta", message="[ITEBIS] SOLO SE PUEDE INTRODUCIR NUMERO O DECIMALES EJEMPLO: 12.34")

            if(self.view.view == MODE_PRODUCT_INVENTORY_NEW ): 
                r=self.db.insert_product(product,descrt,cost,price,amount,tax)
                if not (r): return self.view.alert.showwarning(title="Alerta", message="ESTE CODIGO YA LO TIENE UN PRODUCTO")

            elif(self.view.view == MODE_PRODUCT_INVENTORY): 
                self.db.update_product(product,descrt,cost,price,amount,tax)

            ViewInventory(self.view)
            self.action_invetory()
        
    def deleter_product(self):
        tablet=self.view.tablet_inventory
        if(tablet.selection()):
            code,*_=tablet.item(tablet.selection())["values"]

            self.db.deleter_product(code)
            ViewInventory(self.view)

    def edit_product(self):
        tablet=self.view.tablet_inventory
        if(tablet.selection()):
            code,amount,description,cost,price,tax,_=tablet.item(tablet.selection())["values"]

            ViewShowProduct(self.view,MODE_PRODUCT_INVENTORY)
            self.view.title_var.set("MODIFICAR PRODUCTO")

            self.view.input_code.config(state='normal')
            self.view.input_code.insert(0,code)
            self.view.input_code.config(state='disabled')
            
            self.view.input_amount.insert(0,amount)
            self.view.input_descr.insert(0,description)
            self.view.input_cost.insert(0,cost)
            self.view.input_price.insert(0,price)
            self.view.input_tax.insert(0,tax)


    def new_product(self):
        if(self.event.keysym == BIND_ADD_PRODUCTO):
            ViewShowProduct(self.view)
            self.view.title_var.set("NUEVO PRODUCTO")
 
