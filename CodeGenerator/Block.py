class Block:
    def __init__(self, block_type):
        self.__block_type = block_type
        self.__childs = []

    def add_child(self, child):
        self.__childs.append(child)

    def get_childs(self):
        return self.__childs

    def get_type(self):
        return self.block_type
    
    