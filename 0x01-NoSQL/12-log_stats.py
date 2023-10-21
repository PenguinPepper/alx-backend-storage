#!/usr/bin/env python3
"""mmodule contains  list_all function"""

from pymongo import MongoClient
list_all = __import__('8-all').list_all


if __name__ == "__main__":
    """script that provides some stats
    about Nginx logs stored in MongoDB"""
    client = MongoClient("mongodb://localhost:27017")
    log = client.logs.nginx
    print("{} logs".format(log.count_documents({})))
    print(f"Methods:")
    print(f"\tmethod GET: {log.count_documents({'method': 'GET'})}")
    print(f"\tmethod POST: {log.count_documents({'method': 'POST'})}")
    print(f"\tmethod PUT: {log.count_documents({'method': 'PUT'})}")
    print(f"\tmethod PATCH: {log.count_documents({'method': 'PATCH'})}")
    print(f"\tmethod DELETE: {log.count_documents({'method': 'DELETE'})}")
    print("{} status check".format(
            (log.count_documents({'method': 'GET', 'path': '/status'}))))
    client.close()
