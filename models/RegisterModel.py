import pymongo
from pymongo import MongoClient

class RegisterModel:

    def __init__(self):
        self.client = MongoClient()
       # self.db = self.client. #need to register!

    def insert_user(self, data):
        print("data is ", data)