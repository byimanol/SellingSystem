import win32print
from const import *


class Print:
    def __init__(self,MasterController) -> None:
        self.controller=MasterController

    def view_all_print(self):
        r = win32print.EnumPrinters(win32print.PRINTER_ENUM_LOCAL | win32print.PRINTER_ENUM_CONNECTIONS)

        prints=[]
        for _,name,*_ in r:
            prints.append(name.split(",")[0])
        return  prints
    
    def print_ticket(self,text):
        try:
            # Abrir la impresora
            printer_name = self.controller.config["print_select"]
            PrinterSelect = win32print.OpenPrinter(printer_name)

            # Iniciar el documento
            win32print.StartDocPrinter(PrinterSelect, 1, ("Ticket", None, "RAW"))
            win32print.StartPagePrinter(PrinterSelect)

            # Convertir el texto a bytes
            text_bytes = text.encode('utf-8')

            # Escribir el texto en la impresora
            win32print.WritePrinter(PrinterSelect, text_bytes)

            # Finalizar la página y el documento
            win32print.EndPagePrinter(PrinterSelect)
            win32print.EndDocPrinter(PrinterSelect)
            win32print.ClosePrinter(PrinterSelect)

        except Exception as e:
            return False
        else:
            return True
