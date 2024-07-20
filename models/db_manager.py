import sqlite3
import time
import json

class Mannager:
    def __init__(self):

        self.conn = sqlite3.connect('data/database.db')
        self.cursor = self.conn.cursor()

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS productos
                    (codigo PRIMARY KEY,descripcion,costo,precio,cantidad,itebis)''')   
        
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS facturas
                    (codigo PRIMARY KEY,fecha,total,totalcapital,subtotal,descuento,producto,pagocon,cliente,numero,itebis)''')   

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS configs
                    (id PRIMARY KEY,config)''')   


    def search_product(self,text):
        self.cursor.execute(f"SELECT * FROM productos WHERE codigo LIKE '{text}%' OR descripcion LIKE '{text}%'")
        r=self.cursor.fetchall()
        return r 
    
    def update_amount_product(self,code,decrease):
        self.cursor.execute(f"SELECT * FROM productos WHERE codigo LIKE '{code}%'")
        r=self.cursor.fetchall()[0]

        code,description,cost,price,amount,tax=r
        descr_amount=int(amount)-int(decrease)

        self.update_product(code,description,cost,price,descr_amount,tax)


    def insert_product(self,product,descrt,costo,precio,cantidad,itebis):
        try:
            self.cursor.execute(f"INSERT INTO productos (codigo, descripcion, costo, precio, cantidad, itebis) VALUES ('{product}', '{descrt}', '{costo}', '{precio}', '{cantidad}', '{itebis}')")
            self.conn.commit()
        except:
            return False
        else:
            return True

    def update_product(self,product,descrt,costo,precio,cantidad,itebis):
        self.cursor.execute(f"UPDATE productos SET descripcion = '{descrt}', costo = '{costo}', precio = '{precio}', cantidad = '{cantidad}', itebis = '{itebis}' WHERE codigo = '{product}'")
        self.conn.commit()

    def deleter_product(self,product):        
        self.cursor.execute(f"DELETE FROM productos WHERE codigo = '{product}'")
        self.conn.commit()

    def save_invoice(self,total,capital,subtotal,discount,products_cart,pagocon,itebis):
        try:
            date=int(time.time())
            self.cursor.execute(f"""INSERT INTO facturas (codigo,fecha, total, totalcapital, subtotal, descuento, producto, pagocon, itebis) VALUES ( '{date}', '{date}', '{total}', '{capital}', '{subtotal}', '{discount}', '{json.dumps(products_cart)}', '{pagocon}', '{itebis}')""")
            self.conn.commit()

        except:
            return False
        else:
            return True
        
    def find_year(self):
        self.cursor.execute(f"SELECT DISTINCT strftime('%Y', datetime(fecha, 'unixepoch')) AS anio FROM facturas ORDER BY anio;")
        r=self.cursor.fetchall()
        return r 

    def find_month(self,year):
        self.cursor.execute(f"SELECT DISTINCT strftime('%m', datetime(fecha, 'unixepoch', 'localtime')) AS month FROM facturas WHERE strftime('%Y', datetime(fecha, 'unixepoch', 'localtime')) = '{year}' ORDER BY month;")
        r=self.cursor.fetchall()
        return r 
    
    def find_day(self,year,month):
        self.cursor.execute(f"SELECT DISTINCT strftime('%d', datetime(fecha, 'unixepoch', 'localtime')) AS dia FROM facturas WHERE strftime('%Y', datetime(fecha, 'unixepoch', 'localtime')) = '{year}' AND strftime('%m', datetime(fecha, 'unixepoch', 'localtime')) = '{month}';")
        r=self.cursor.fetchall()
        return r 

    def find_all_day(self,year,month,allDay):
        self.cursor.execute( f"SELECT * FROM facturas WHERE strftime('%Y', datetime(fecha, 'unixepoch', 'localtime')) = '{year}' AND strftime('%m', datetime(fecha, 'unixepoch', 'localtime')) = '{month}' AND strftime('%d', datetime(fecha, 'unixepoch', 'localtime')) IN {tuple(allDay)};" )
        r=self.cursor.fetchall()
        return r 

    def there_config(self):
        self.cursor.execute("SELECT config FROM configs WHERE id = '1'")
        r=self.cursor.fetchall()
        return r
    
    def update_config(self,config):
        self.cursor.execute(f"UPDATE configs SET config = '{json.dumps(config)}' WHERE id = '1'")
        self.conn.commit()

    def insert_config(self,config):
        self.cursor.execute(f"INSERT INTO configs (id, config) VALUES ('1', '{json.dumps(config)}')")
        self.conn.commit()



