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
        except (json.decoder.JSONDecodeError, FileNotFoundError) :
            data = {}
        return data

    @staticmethod
    def write_json(dict_data, filename='user_feedback.json'):
        with open(filename, 'w') as f:
            json.dump(dict_data, f)

    @staticmethod
    def find_relevant_hashtags(hashtags, feedback):
        # Take in the posts, update the relevance values for each pair
        print("Feedback registered")

        # hashtags is a list of hashtags on a single post
        for post_hashtag_1 in hashtags:
            post_hashtag_1 = post_hashtag_1.lower()
            for post_hashtag_2 in hashtags:
                post_hashtag_2 = post_hashtag_2.lower()
                min_hashtag = min(post_hashtag_1, post_hashtag_2)
                max_hashtag = max(post_hashtag_1, post_hashtag_2)
                # make sure the key is concatenated in alphabetical order
                key = min_hashtag + "," + max_hashtag

                # if the hashtags are different, update the feedback
                if post_hashtag_1 != post_hashtag_2:
                    if key in feedback.keys():
                        feedback[key] = feedback[key] + 0.03
                    else:
                        feedback[key] = 0.5

        return feedback

        # TODO eventually make this write user feedback to some file and read from it to get data
        # Every time there's a new occurrence of a pair in the tweet - add 0.03,
        # Every time it's confirmed as a good pair - add  0.1,
        # Every time it's selected as a bad pair - subtract 0.1
        # Default value for pairs that occur first time - 0.5

    @staticmethod
    def user_feedback(hashtag_pair, is_good):
        min_hashtag = min(hashtag_pair[0].lower(), hashtag_pair[1].lower())
        max_hashtag = max(hashtag_pair[0].lower(), hashtag_pair[1].lower())
        # make sure the key is concatenated in alphabetical order
        key = min_hashtag + "," + max_hashtag

        # get existing feedback
        data = dict(HashtagFilter.read_json())

        if key not in data.keys():
            return

        if is_good:
            data[key] = data[key] + 0.1
        else:
            data[key] = data[key] - 0.1

        print("Hashtag pair score updated: " + key + " with score " + str(data[key]))

        HashtagFilter.write_json(data)

    @staticmethod
    def filter(hashtags):
        print("Finding relevant hashtags")
        # TODO: implement this method - actually filter out relevant hashtags based on the data

        data = dict(HashtagFilter.read_json())
        print(data, "read from json")

        data = HashtagFilter.find_relevant_hashtags(hashtags, data)
        HashtagFilter.write_json(data)

        return hashtags
