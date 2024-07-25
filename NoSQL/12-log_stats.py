#!/usr/bin/env python3
"""Python script that provides some stats about Nginx logs
stored in MongoDB"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient("mongodb://localhost")
    db = client["logs"]
    c = db["nginx"]  # collection
    print(f"{c.count_documents({})} logs")
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        print(f"\tmethod {method}: {c.count_documents({'method': method})}")
    msg = "status check"
    print(f"{c.count_documents({'method': 'GET', 'path': '/status'})} {msg}")
