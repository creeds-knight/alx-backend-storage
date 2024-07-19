#!/usr/bin/env python3
"""
    Where can i learn python
"""


def schools_by_topic(mongo_collection, topic):
    """
        Returns a list of schools with a specific topic
    """
    topic_filter = {
        'topics': {
            '$elemMatch':{
                '$eq': topic,
                },
            },
        }
    return [doc for doc in mongo_collection.find(topic_filter)]
