import http.client
import os
from dotenv import load_dotenv

load_dotenv()

class tmpmail():
    def __init__(self,address):
        self.conn = http.client.HTTPSConnection("mailsac.com")
        self.headers = { 'Mailsac-Key': os.getenv("MAILSAC_KEY") }
        self.address = address

    def create_address(self,mail):
        self.conn.request("GET", f"/api/addresses/{self.address}@mailsac.com/message-count", headers=self.headers)

        res = self.conn.getresponse()
        data = res.read()

        print(data.decode("utf-8"))

    def get_message(self):

        conn = http.client.HTTPSConnection("mailsac.com")

        conn.request("GET", f"/api/addresses/{self.address}@mailsac.com/messages", headers=self.headers)

        res = conn.getresponse()
        data = res.read()

        print(data.decode("utf-8"))