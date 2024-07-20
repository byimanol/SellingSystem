from models.db_manager import Mannager
from models.print import Print
from views.view_cart import ViewCart
from const import *

import json


class ControllerConfig:
    def __init__(self,MasterView,MasterController,event):
        self.view=MasterView
        self.controller=MasterController
        self.event = event
        self.db=Mannager()

    def action_config(self): 
        if (self.event.keysym == KEY_ENTER): return self.save_config()
        if(self.event.keysym == KEY_BACK): return ViewCart(self.view,self.controller)
        if(self.event.widget == self.view.print_select): return self.view_prints()

    def action_password(self):
        if(self.event.keysym == KEY_BACK): return ViewCart(self.view,self.controller)

        if(self.event.keysym == KEY_ENTER): 
            if(self.controller.config):
                if(self.controller.config["password"] == self.view.permiss_password.get()): 
                    self.controller.config["unloker"]=False
                    ViewCart(self.view,self.controller)

    def is_allow(self):
        if not(self.controller.config): return True
        if (self.controller.config["password"]==""): return True
        is_locker=self.controller.config["unloker"]

        if (is_locker):
            if(self.view.view == MODE_PASSWORD): return True

            if (self.event.keysym == BIND_CONFIG): return False

            if(self.controller.config["pass_invetory"] and self.event.keysym == BIND_INVENTORY): return False

            if(self.controller.config["pass_discount"] and self.event.keysym == BIND_DISCOUNTS): return False

            if(self.controller.config["pass_registerCash"] and self.event.keysym == BIND_CASH_REGISTER): return False

        return True

    def load_config(self):
        there_config=self.db.there_config()
        if(there_config): 
            there_config=there_config[0][0]
            self.controller.config=json.loads(there_config)
            return

        self.controller.config={
            "pass_invetory":False, 
            "pass_discount":False, 
            "pass_registerCash":False, 
            "print_select": "", 
            "password": "",
            "unloker": True
        }
  
    def save_config(self):
        self.controller.config={
            "pass_invetory":self.view.pass_invetory.get(), 
            "pass_discount":self.view.pass_discount.get(), 
            "pass_registerCash":self.view.pass_registerCash.get(), 
            "print_select": self.view.print_select.get(), 
            "password": self.view.input_pass.get(),
            "unloker": True
        }

        there_config=self.db.there_config()
        if(there_config): self.db.update_config(self.controller.config)
        if not (there_config): self.db.insert_config(self.controller.config)

        self.db.close()

        return ViewCart(self.view,self.controller)
        
    def view_prints(self):
        self.view.print_select['values'] = tuple(Print(self.controller).view_all_print())


