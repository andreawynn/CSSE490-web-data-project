import json
from os import path


class HashtagFilter:
    '''Important:
        JSON doesn't like having tuples as dictionary keys
        For that reason, the format that I've chosen: first hashtag + ',' + second hashtag
        Example: data['food' + ',' + 'love'] += 0.1'''

    @staticmethod
    def read_json(filename='user_feedback.json'):
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
        except json.decoder.JSONDecodeError:
            data = {}
        return data

    @staticmethod
    def write_json(dict_data, filename='user_feedback.json'):
        with open(filename, 'w') as f:
            json.dump(dict_data, f)

    @staticmethod
    def collect_feedback(self, hashtag):
        print("Feedback registered")
        print(hashtag)
        # TODO eventually make this write user feedback to some file and read from it to get data
        # Every time there's a new occurrence of a pair in the tweet - add 0.03,
        # Every time it's confirmed as a good pair - add  0.1,
        # Every time it's selected as a bad pair - subtract 0.1
        # Default value for pairs that occur first time - 0.5


    @staticmethod
    def filter(hashtags):
        print("Finding relevant hashtags")
        # TODO: implement this method

        data = dict(HashtagFilter.read_json())

        print(data, "read from json")

        data['food' + ',' + 'love'] = 0.6

        HashtagFilter.write_json(data)

        return hashtags
