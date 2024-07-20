from const import *
import datetime
import json

class TicketRegister:
        def __init__(self,list_tickets,month):
                self.total=0
                self.total_taxes=0
                self.total_capital=0
                self.total_ticket=0

                self.list_tickets=list_tickets
                self.list_tickets_text=""
                self.month=month
                self.date="09/07/2024"

        def generate_shop_ticket(self):
                for list_shop in self.list_tickets:
                        _,date,total,capital,_,discounts,list_products,cash,_,_,taxes=list_shop
                        self.total+=float(total)
                        self.total_capital+=float(capital)
                        self.total_taxes+=float(taxes)
                        self.total_ticket+=1

                        dateu = datetime.datetime.fromtimestamp(int(date))
                        hour = dateu.strftime('%I:%M %p')
                        list_products = json.loads(list_products)
                        self.list_tickets_text+=f"""
------------------------------------------------
        [DIA:{dateu.day} HORA:{hour}]
------------------------------------------------
DESCRIPCION                ITBIS        VALOR
------------------------------------------------\n"""
                        for p in list_products:
                                p_description=str(p["description"])
                                p_amount=str(p["amount"])
                                p_price=str(p["price"])
                                p_tax=str(p["tax"])[:MAX_NUM_TIKECT]
                                p_total=str(p["total"])[:MAX_NUM_TIKECT]

                                decription=f"{p_description[:MAX_DESCRIPTION_TIKECT]:<{MAX_DESCRIPTION_TIKECT+SPACIN_COUNT}}"
                                tax=f"{p_tax:<{MAX_NUM_TIKECT+SPACIN_COUNT}}"
                                value=f"{p_total:<{MAX_NUM_TIKECT+SPACIN_COUNT}}"

                                self.list_tickets_text+=decription+tax+value+"\n"

                                if(len(p_description) >= (MAX_DESCRIPTION_TIKECT*2) ): 
                                        self.list_tickets_text+=f"{p_description[MAX_DESCRIPTION_TIKECT:][:MAX_DESCRIPTION_TIKECT][:-3]}"+"..."+"\n"
                                                                
                                self.list_tickets_text+=f"[{p_amount} X PRECIO {p_price}]"+"\n"

                                self.list_tickets_text+=f"""
------------------------------------------------ 
[TOTAL {total}] [DESC {discounts}%] [T.ITBIS {taxes}] 
[GANACIA {float(total)-float(capital)}] [EFECT. {cash}] 
------------------------------------------------\n\n"""     

        def print(self):
                return f"""
                SHOPP NAME
        Address: Lorem Ipsum, 23-10
        Fecha:{self.date}
        Telefono:12234234
------------------------------------------------
                CUADRE DE CAJA
------------------------------------------------
                MES: {self.month} {self.list_tickets_text}
------------------------------------------------
TOTAL       {self.total}
T.ITBIS     {self.total_taxes}
T.CAPITAl   {self.total_capital}
T.GANADO    {self.total-self.total_capital}
T.FACTURAS  {self.total_ticket}
------------------------------------------------
"""

