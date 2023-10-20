#!/usr/bin/env python3
"""mmodule contains insert_school function"""


def insert_school(mongo_collection, **kwargs):
    """function that inserts a new document
    in a collection based on kwargs"""
    insertion = mongo_collection.insert_one(kwargs)
    return insertion.inserted_id
