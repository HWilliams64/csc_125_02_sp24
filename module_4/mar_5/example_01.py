class Crate:
    # color = "red"
    # size = (10, 10, 10)
    # shape = "cube"
    # health = -100
    # augment = 0.0

    def __init__(self, color="transparent", size=(0, 0, 0), shape="cube", health=0, augment=1):

        if len(size) != 3:
            raise ValueError("Size must be a 3-tuple")
        
        if shape not in ["cube", "sphere"]:
            raise ValueError("Shape must be either 'cube' or'sphere'")

        self.color = color
        self.size = size
        self.shape = shape
        self.health = health
        self.augment = augment

    def set_health(self, new_health):
        self.health = new_health

    def power_up(self):
        if self.health < 0:
            print(f"You lost {self.health} health!")
        elif self.health > 0:
            print(f"You gained {self.health} health!")

        if self.augment < 1:
            print(f"You shrunk {self.augment*100}%")
        elif self.augment > 1:
            print(f"You grew {self.augment*100}%")

    def __str__(self):
        to_ret = f"A {self.color} {self.shape} Crate that is {self.size} "
        
        if self.health < 0:
            to_ret += f"that will hurt you "
        elif self.health > 0:
            to_ret += f"that will give you health "

        if self.augment < 1:
            to_ret += f"that will shrink you "
        elif self.augment > 1:
            to_ret += f"that will grow you larger "

        return to_ret


exploding_crate = Crate(color="red", size=(10, 10, 10), shape="sphere", health=-10)
print(exploding_crate)
exploding_crate.set_health(100)
print(exploding_crate)
# exploding_crate = Crate()
# print("The Color of the Crate is: ", exploding_crate.color)
# exploding_crate.color = "green"
# exploding_crate.health = 100
# print("The Color of the Crate is: ", exploding_crate.color)
# print("The Health of the Crate is: ", exploding_crate.health)

# mario_mushroom_crate = Crate()
# mario_mushroom_crate.augment = 1.7
# mario_mushroom_crate.health = 0
# mario_mushroom_crate.power_up()

# print("exploding_crate", exploding_crate)
# print("mario_mushroom_crate", mario_mushroom_crate)
