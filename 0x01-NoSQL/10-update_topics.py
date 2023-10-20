#!/usr/bin/env python3
"""mmodule contains update_topics function"""


def update_topics(mongo_collection, name, topics):
    """function that changes all topics of
    a school document based on the name"""
    names = {"name": name}
    mongo_collection.update_many(names, {"$set": {"topics": topics}})
