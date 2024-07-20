from const import *

class TicketShop:
        def __init__(self,total,total_taxs,cash,list_products):
                self.total=float(total)
                self.total_taxs=float(total_taxs)
                self.cash=float(cash)
                self.list_products=list_products
                self.list_products_text=""
                self.date="09/07/2024"

        def generate_shop_ticket(self):
                for p in self.list_products:
                        p_description=str(p["description"])
                        p_amount=str(p["amount"])
                        p_price=str(p["price"])
                        p_tax=str(p["tax"])[:MAX_NUM_TIKECT]
                        p_total=str(p["total"])[:MAX_NUM_TIKECT]

                        decription=f"{p_description[:MAX_DESCRIPTION_TIKECT]:<{MAX_DESCRIPTION_TIKECT+SPACIN_COUNT}}"
                        tax=f"{p_tax:<{MAX_NUM_TIKECT+SPACIN_COUNT}}"
                        value=f"{p_total:<{MAX_NUM_TIKECT+SPACIN_COUNT}}"

                        self.list_products_text+=decription+tax+value+"\n"

                        if(len(p_description) >= (MAX_DESCRIPTION_TIKECT*2) ): 
                                self.list_products_text+=f"{p_description[MAX_DESCRIPTION_TIKECT:][:MAX_DESCRIPTION_TIKECT][:-3]}"+"..."+"\n"
                        
                        self.list_products_text+=f"{p_amount} x {p_price}"+"\n \n"
       
        def print(self):
                return f"""
              SHOPP NAME
           Fecha:{self.date}
      Address: Lorem Ipsum, 23-10
            Telp. 12234234
------------------------------------------------
        FACTURA PARA CONSUMIDOR FINAL
------------------------------------------------
DESCRIPCION                ITBIS        VALOR
------------------------------------------------
{self.list_products_text}


TOTAL A PAGAR: {self.total}
TOTAL ITBIS: {self.total_taxs}
EFECTTIVO: {self.cash}
DEVUELTA: {self.cash-self.total}

------------------------------------------------

        GRACIAS POR SU COMPRA ESPERO 
            QUE VUELVA PRONTO
"""
