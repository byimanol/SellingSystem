
# from controllers.print import Print
from const import *
from views.view_search_product import ViewSearchProduct
from views.view_discount import ViewDiscount
from views.view_inventory import ViewInventory
from views.view_cash_register import ViewCashRegister
from views.view_config import ViewConfig
from views.view_password import ViewPassword
from controllers.controller_cart import ControllerCart
from controllers.controller_inventory import ControllerInventory
from controllers.controller_discount import ControllerDiscount
from controllers.controller_cash_register import ControllerCashRegister
from controllers.controller_checkout import ControllerCheckeout
from controllers.controller_config import ControllerConfig


class Controller:
    def __init__(self, MasterView):
        self.view = MasterView

        self.products_cart=[]
        self.find_invetory=[]
        self.calendarDays=[]

        self.config={}

        self.discounts=0
        self.total=0
        self.taxs=0
        self.subtotal=0
        self.capital=0

        ControllerConfig(self.view,self,"").load_config()

        self.view.bind_all("<Key>",self.ListenEvent)
   
    def set_selection_tree(self,tree):
        if not(tree.focus()): 
            children = tree.get_children()
            tree.focus_set()
            if children :
                tree.focus(children[0])
                tree.selection_set(children[0])

    def is_decimal(self,s):
        try:
            float(s)
            if(s.isnumeric()): return True
            return '.' in s 
        except ValueError:
            return False

    def ListenEvent(self,event):   

        if not ( ControllerConfig(self.view,self,event).is_allow()): return ViewPassword(self.view)

        if(self.view.view == MODE_TABLET_CART and event.keysym == BIND_DISCOUNTS): return ViewDiscount(self.view)
        
        if(self.view.view == MODE_TABLET_CART and event.keysym == BIND_SEARCH_PRODUCTO): return ViewSearchProduct(self.view)

        if(self.view.view == MODE_TABLET_CART and event.keysym == BIND_CONFIG): return ViewConfig(self.view,self)
        
        if(self.view.view == MODE_TABLET_CART and event.keysym == BIND_INVENTORY ): return ViewInventory(self.view)

        if(self.view.view == MODE_TABLET_CART and event.keysym == BIND_CASH_REGISTER): return ViewCashRegister(self.view,self)
        
        

        if(self.view.view == MODE_PRODUCT_INVENTORY or self.view.view ==MODE_PRODUCT_INVENTORY_NEW): return ControllerInventory(self.view,self,event).action_show_invetory()

        if(self.view.view == MODE_TABLET_CART): return ControllerCart(self.view,self,event).action_cart()
            
        if(self.view.view == MODE_INVENTORY): return ControllerInventory(self.view,self,event).action_invetory()

        if(self.view.view == MODE_CHECKOUT): return ControllerCheckeout(self.view,self,event).action_checkout()
        
        if(self.view.view == MODE_FINISH): return ControllerCheckeout(self.view,self,event).action_finish()

        if(self.view.view == MODE_CONFIG): return ControllerConfig(self.view,self,event).action_config()

        if(self.view.view == MODE_SEARCH_PRODUCT): return ControllerCart(self.view,self,event).search_product()   

        if(self.view.view == MODE_DISCOUNT): return ControllerDiscount(self.view,self,event).action_discount()

        if(self.view.view == MODE_CASH_REGISTER): return ControllerCashRegister(self.view,self,event).action_cash_Register()
        
        if(self.view.view == MODE_PASSWORD): return ControllerConfig(self.view,self,event).action_password()

        
        



    














    # def action_config(self,event):
    #     if not (event.keysym == KEY_ENTER): return

    #     #continua al aqui

