#!/usr/bin/env python3
"""
    Update using pymongo
"""


def update_topics(mongo_collection, name, topics):
    """
        Changes all topics of a collection's document based on name
    """
    mongo_collection.update_many(
            {'name': name},
            {'$set': {'topics': topics}}
            )
