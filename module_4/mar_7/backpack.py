class Item:
    def __init__(self, name, weight, height, width, length):
        self.name = name
        self.weight = weight
        self.height = height
        self.width = width 
        self.length = length

class Backpack:

    def __init__(self, height, width, length):
        self._container = []
        self._height = height
        self._width = width
        self._length = length
        self.__secret_pocket = []

        # Public - no underscore
        # Protected - Single underscore means protected do not touch
        # Private - double underscore means private do not touch
        # To access a private variable => <Instance name>._<Class name><Private var name>

    def add_item(self, item: Item):

        backpack_specs = [self._height, self._width, self._length]
        item_specs = [item.height, item.width, item.length]

        # 1) find the closest backpack spec value that is greater then  
        
        if item.width > self._height:
            if item.width > self._width:
                if item.width > self._length:
                    raise Exception("Item is too big!")
        
        if item.width > self._height:
            if item.width > self._width:
                if item.width > self._length:
                    raise Exception("Item is too big!")

        if item.width > self._height:
            if item.width > self._width:
                if item.width > self._length:
                    raise Exception("Item is too big!")

    def remove_item(self, item: Item):
        pass

    def get_weight(self) -> float:
        return 0

    def capacity(self) -> float:
        return 0

my_backpack = Backpack(20, 10, 10)
