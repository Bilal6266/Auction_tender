import sys

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

import pymongo

url = "mongodb+srv://bilalahmed:N1zfwQZZrw8LetbE@auctiontender.cc5nxin.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(url)
# client = pymongo.MongoClient("mongodb+srv://hamza:asdfg@cluster0.7gpgsz7.mongodb.net/?retryWrites=true&w=majority")
db = client.auction_tender


class Tender(APIView):
    def get(self, request):
        collection = db["Tender"]
        documents = list(collection.find())
        if documents:
            for doc in documents:
                del doc['_id']
        return Response(documents)

    def post(self, request):
        json = request.data
        collection = db["Tender"]
        documents = list(collection.find())
        tender_id = len(documents) + 1
        json['tender_id'] = tender_id
        collection.insert_one(json)
        return Response({"status": "tender created successfully"})

    def put(self, request):
        json = request.data
        collection = db["Tender"]
        documents = list(collection.find())
        for doc in documents:
            if json['tender_id'] == doc['tender_id']:
                collection.replace_one({'_id': doc['_id']}, json)
                return Response({"status": "tender updated successfully"})
        return Response({"status": "key not found"}, status=409)

    def delete(self, request):
        tender_id = request.GET.get('tender_id')
        collection = db["Tender"]
        documents = list(collection.find())
        for doc in documents:
            if int(tender_id) == doc['tender_id']:
                collection.delete_one({'_id': doc['_id']})
                return Response({"status": "tender delete successfully"})
        return Response({"status": "key not found"}, status=409)


class Auction(APIView):
    def get(self, request):
        collection = db["Auction"]
        documents = list(collection.find())
        if documents:
            for doc in documents:
                del doc['_id']
        return Response(documents)

    def post(self, request):
        json = request.data
        collection = db["Auction"]
        documents = list(collection.find())
        auction_id = len(documents) + 1
        json['auction_id'] = auction_id
        collection.insert_one(json)
        return Response({"status": "auction created successfully"})

    def put(self, request):
        json = request.data
        collection = db["Auction"]
        documents = list(collection.find())
        for doc in documents:
            if json['auction_id'] == doc['auction_id']:
                collection.replace_one({'_id': doc['_id']}, json)
                return Response({"status": "auction updated successfully"})
        return Response({"status": "key not found"}, status=409)

    def delete(self, request):
        auction_id = request.GET.get('auction_id')
        collection = db["Auction"]
        documents = list(collection.find())
        for doc in documents:
            if int(auction_id) == doc['auction_id']:
                collection.delete_one({'_id': doc['_id']})
                return Response({"status": "auction delete successfully"})
        return Response({"status": "key not found"}, status=409)


class HealthCheckView(APIView):
    def get(self, request):
        return Response({"status": "ok"})


class Login(APIView):
    def post(self, request):
        json = request.data
        email, password, role = json['email'], json['password'], json['role']
        collection = db[role.upper()]
        documents = collection.find()
        if documents is not None:
            for record in documents:
                if record["email"] == json["email"] and record["password"] == json["password"]:
                    del record["_id"]
                    return Response(record)
        return Response({"status": "User not found"}, status=409)


class SignUp(APIView):
    def post(self, request):
        json = request.data
        collection = db[json['role'].upper()]
        documents = collection.find()
        if documents is not None:
            for doc in documents:
                if json["email"] == doc["email"]:
                    return Response({"status": "User already exists"}, status=409)
        collection.insert_one(json)
        return Response({"status": "user created successfully"})

class User(APIView):
    def post(self, request):
        json = request.data
        collection = db[json['role'].upper()]
        documents = list(collection.find())
        for document in documents:
            if document['email'] == json['email']:
                if json.get('password', '') != '' and json.get('password', '') is not None:
                    document['password'] = json['password']
                if json.get('firstName', '') != '' and json.get('firstName', '') is not None:
                    document['firstName'] = json['firstName']
                if json.get('lastName', '') != '' and json.get('lastName', '') is not None:
                    document['lastName'] = json['lastName']
                collection.replace_one({'_id': document['_id']}, document)
                return Response({"status": "user updated"})
        return Response({"status": "user not found"})
