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

    def add_item(self, item: Item) -> bool:

        backpack_specs = [self._height, self._width, self._length]
        item_specs = [item.height, item.width, item.length]

        if not self.can_fit(item_specs):
            return False
        
        if not self.volume_left() >= (item.height * item.width * item.length):
            return False

        self._container.append(item)
        return True
    
    def can_fit(self, item_dem):
        backpack_dem = (self._height, self._width, self._length)
        count = 0

        for i in range(3):
            backpack_spec = backpack_dem[i]
            item_spec = item_dem[i]

            if backpack_spec >= item_spec:
                count += 1
            else:
                count = 0
                item_dem = self.rotate(item_dem)
            
            if count == 3:
                return True

        return False

    def volume_left(self) -> float:
        total_vol = self._height * self._width *  self._length
        
        return total_vol - self.volume_taken()

    def volume_taken(self) -> float:
        total = 0
        for item in self._container:
            total += item.height * item.width * item.length

        return total

    def rotate(self, dem) -> tuple:
        return (dem[-1], dem[0], dem[1])

    def remove_item(self, item: Item):
        pass

    def get_weight(self) -> float:
        return 0

    def capacity(self) -> float:
        return 0

my_backpack = Backpack(2, 2, 3)

item = Item(f"Too Large", 1, 2, 2, 2.5)

add_result = my_backpack.add_item(item)
print(f"The {item.name} fit in the backpack: {add_result}")

for i in range(20):
    item = Item(f"Item {i}", 1, 1, 1, 1)

    add_result = my_backpack.add_item(item)
    print(f"The {item.name} fit in the backpack: {add_result}")
