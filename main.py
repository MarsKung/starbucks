import http.client
import os
import random
import json
from dotenv import load_dotenv

load_dotenv()

class tmpmail():
    def __init__(self):
        self.conn = http.client.HTTPSConnection("mailsac.com")
        self.headers = { 'Mailsac-Key': os.getenv("MAILSAC_KEY") }
        

    def create_address(self):
        self.address = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=20))
        self.conn.request("GET", f"/api/addresses/{self.address}@mailsac.com/message-count", headers=self.headers)

        res = self.conn.getresponse()
        data = json.loads(res.read().decode("utf-8"))
        print(data)
        if data["count"] >= 1:
            self.create_address()
        
        
        return self.address

    def get_message(self):

        conn = http.client.HTTPSConnection("mailsac.com")

        conn.request("GET", f"/api/addresses/{self.address}@mailsac.com/messages", headers=self.headers)

        res = conn.getresponse()
        data = res.read()

        print(data.decode("utf-8"))

if __name__ == "__main__":
    mail = tmpmail()
    mail.create_address()
    mail.get_message()