class Item():
    def __init__(self, name, status, position):
       self.name = name
       self.status = status
       self.position = position

    def pick_up_item(self,other):
        if len(other.inventory) > 10:
            print('Your inventory is full. Use some items and try again.')
        else:
            other.inventory.append(self)

class Weapon(Item):
    def __init__(self, name, status, position,damage,crit_chance):
        super().__init__(name, status, position)
        self.crit_chance = crit_chance
        self.damage = damage

class AddBuff(Item):
    def __init__(self, name, status, position,effect):
        super().__init__(name, status, position)
        self.effect = effect

class Keys(Item):
    def __init__(self, name, status, position,number):
        super().__init__(name, status, position)
        self.number = number

    def pick_up_item(self, room):
         print('You picked up a key')
         if self.number == room.number:
            room.locked = False

    