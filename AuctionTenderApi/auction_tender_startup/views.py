import sys

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

import pymongo

url = "mongodb+srv://bilalahmed:N1zfwQZZrw8LetbE@auctiontender.cc5nxin.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(url)
db = client.auction_tender


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


class updatedb(APIView):
    def get(self, request):
        collection = db["data_collection"]
        first_document = collection.find_one()
        if first_document is None:
            ob = {"data": {"auction": [], "tender": []}}
            collection.insert_one(ob)
            return Response(ob["data"])
        else:
            return Response(first_document["data"])

    def post(self, request):
        json = request.data
        collection = db["data_collection"]
        first_document = collection.find_one()
        if first_document is None:
            ob = {"data": json}
            collection.insert_one(ob)
        else:
            first_document['data'] = json
            collection.replace_one({'_id': first_document['_id']}, first_document['data'])
        return Response({"status": "db updated"})
