#!/usr/bin/env python3
"""
    lists all documents in a collection
"""


def list_all(mongo_collection):
    """
        Returns a list of documents in a collection
    """
    return [doc for doc in mongo_collection.find()]
