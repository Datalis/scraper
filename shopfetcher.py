import urllib3
import json
import os
from time import ctime


class ShopFectcher:
    def __init__(self):
        self.headers = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "en-US,en;q=0.9,es;q=0.8",
            "Connection": "keep-alive",
            "Content-Length": 116,
            "Content-Type": "application/json",
            "Host": "dhayservice.cimex.com.cu:1703",
            "Origin": "http://dondehay.cimex.com.cu",
            "Referer": "http://dondehay.cimex.com.cu/",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"
        }
        self.products_url = "http://dhayservice.cimex.com.cu:1703/api/product/text-search"
        self.details_url = "http://dhayservice.cimex.com.cu:1703/api/product-details/"
        self.products_count = 0
        self.products_total = 0
        self.shops_count = 0
        self.shops_ids = []
        self.json_name = "shops.json"
        self.json_name_temp = self.json_name+'.temp'
        self.http = urllib3.PoolManager()

        if os.path.exists(self.json_name):
            os.remove(self.json_name)
        if os.path.exists(self.json_name_temp):
            os.remove(self.json_name_temp)

    def __del__(self):
        print('\n> Found:', len(self.shops_ids), 'shops')
        self.save_shops_as_json()

    def fectch(self):
        payload = {
            "text": " "
        }

        print("--> Sending post")
        response = self.http.request('POST', self.products_url, headers=self.headers, fields=payload)
        products_next_page_url = True
        self.products_total = json.loads(response.data.decode('utf-8')).get("last_page")

        while products_next_page_url:
            products_data = json.loads(response.data.decode('utf-8'))
            products_data_list = products_data.get("data")

            for product_object in products_data_list:
                self.products_count += 1
                print(f"> [{ctime()}] Product {self.products_count}/{self.products_total}")
                product_id = product_object.get("id")
                if product_id:
                    shops = self.get_shop_data(product_id)
                    if shops:
                        try:
                            self.update_shops(shops)
                        except:
                            pass

            products_next_page_url = products_data.get("next_page_url")
            if products_next_page_url:
                response = self.http.request('GET', products_next_page_url, headers=self.headers)

        print(f"Total scanned shop {self.shops_count} on {self.products_count} products")

    def get_shop_data(self, product_id):
        product_details_url = f'{self.details_url}{product_id}'

        details_response = self.http.request('GET', product_details_url, headers=self.headers)
        details_next_page_url = True

        shop_by_products_count = 0
        shops = []
        while details_next_page_url:
            details_data = json.loads(details_response.data.decode('utf-8'))
            details_data_list = details_data.get("data")
            
            for details_object in details_data_list:
                id = details_object.get("id")
                if id not in self.shops_ids:
                    self.shops_count += 1
                    shop_by_products_count +=1
                    
                    self.shops_ids.append(id)

                    print(f'- [{ctime()}] shop {shop_by_products_count} (added: {len(self.shops_ids)})')

                    shops.append({
                        "name": details_object.get("nombre"),
                        "x_cord": details_object.get("x_coordenada"),
                        "y_cord": details_object.get("y_coordenada"),
                        "municipality": details_object.get("municipio"),
                        "province": details_object.get("provincia"),
                        "address": details_object.get("direccion"),
                        "mlc": details_object.get("mlc")
                    })

            details_next_page_url = details_data.get("next_page_url")
            if details_next_page_url:
                details_response = self.http.request('GET', details_next_page_url, headers=self.headers)
        
        return shops

    def update_shops(self, shops):
        if shops:
            with open(self.json_name_temp, 'a') as fd:
                fd.write(',')
                data = json.dumps(shops)
                fd.write(data[1:len(data)-1])

    def save_shops_as_json(self):
        if os.path.exists(self.json_name):
            os.remove(self.json_name)

        if os.path.exists(self.json_name_temp):
            data = ""
            with open(self.json_name_temp) as fd:
                data = fd.read()[1:]
            data = "[" + data + "]"
            data = json.loads(data) # verify correct json

            with open(self.json_name, 'w') as fd:
                json.dump(data, fd)

            os.remove(self.json_name_temp)
        
