#!/usr/bin/env python3
"""
    Inserts a new document in a collection based on args
"""


def insert_school(mongo_collection, **kwargs):
    """
        returns id of inserteted objects
    """
    res = mongo_collection.insert_many(kwargs)
    return result.inserted_ids
