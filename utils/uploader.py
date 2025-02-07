import json
import os
import sys

from filestack import Client

if not os.path.isfile("config.json"):
    sys.exit("'config.json' not found! Please add it and try again.")
else:
    with open("config.json") as file:
        config = json.load(file)


class FileSharer:
    def __init__(self, filepath, api_key=config["filestack_key"]):
        """
        The __init__ function is the constructor for a class. It sets up or "initializes" the object.

        :param self: Used to refer to the object itself.
        :param filepath: Used to store the path of the file that is uploaded.
        :param api_key=config["filestack_key"]: Used to set the api key for the filepicker.
        :return: the instantiation of the class, in this case an instance of the Filelink class.
        :doc-author: Trelent
        """
        self.filepath = filepath
        self.api_key = api_key

    def share(self):
        """
        The share function creates a new filelink object that is then used to share the file with other users.
        The function takes in the api key and uses it to create a client object, which is then used to create a new
        filelink object. The link of this newly created filelink is returned.

        :param self: Used to access the attributes and methods of the class in python.
        :return: the share link.
        :doc-author: Trelent
        """
        client = Client(self.api_key)
        new_filelink = client.upload(filepath=self.filepath)
        return new_filelink.url
