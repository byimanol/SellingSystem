class ControllerTotals:
    def __init__(self,MasterView,MasterController):
        self.view=MasterView
        self.controller=MasterController
    
        self.controller.total=0
        self.controller.taxs=0
        self.controller.subtotal=0
        self.controller.capital=0

        for p in self.controller.products_cart:
            self.controller.total+=p["total"]
            self.controller.taxs+=(p["tax"] * p["amount"])
            self.controller.subtotal+=p["total"]  
            self.controller.capital+=(p["cost"] * p["amount"])

        if(self.controller.discounts>0): self.controller.total=self.controller.total-(self.controller.total*self.controller.discounts/100)


        self.view.text_taxs.set(f"ITEBIS\n{"RD${:,.2f}".format(self.controller.taxs)}")
        self.view.text_sub_total.set(f"SUB TOTAL\n{"RD${:,.2f}".format(self.controller.subtotal)}")
        self.view.text_discount.set(f"DESCUENTO\n{self.controller.discounts} %")
        self.view.text_total.set(f"TOTAL\n{"RD${:,.2f}".format(self.controller.total)}")

 