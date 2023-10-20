#!/usr/bin/env python3
"""module contains schools_by_topic function"""


def schools_by_topic(mongo_collection, topic):
    """function that returns the list
    of school having a specific topic"""
    schools = mongo_collection.find({"topics": topic})
    return schools
