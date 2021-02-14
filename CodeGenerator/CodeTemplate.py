import json

class CodeTemplate:
    def __init__(self, path):
        self.__template = None
        
        with open(path, 'r') as template_file:
            self.__template = json.load(template_file)
 
    def get_template(self):
        return self.__template