import random
class Person():
    def __init__(self, name, health, defense, atk, crit):
        self.name = name
        self.health = health
        self.defense = defense
        self.atk = atk
        self.crit = crit
        self.inventory = []
        

    def death(self): 
        print(f'{self.name} died an untimely death!!')

    def attack(self,other):
        if self.crit != 1:
            print(f'{self.name} attacked you!! (-{self.atk} health)')
            other.health -= self.atk
        else:
            print(f'{self.name} dealt a NASTY blow!! (-{self.atk + 10} health)')
            other.health -= self.atk + 10


class Player(Person):
    def __init__(self, name, health, defense, atk, crit, current_room, pieces_found):
        super().__init__(name, health, defense, atk, crit)
        self.current_room = current_room
        self.pieces_found = pieces_found

    def open_inventory(self):
        print('inventory:')
        index = 0
        for items in self.inventory:
            print(f'{index}) {items.name}, {items.status}')
            index += 1

    def show_stats(self):
        print(f'Health: {self.health}\nDefense: {self.defense} ATK: {self.atk}')

    def use_item(self):
        while True:
            try:
                choose_item = int(input('Equip or use an item, enter item index: '))
                item = self.inventory[choose_item]
            except (IndexError, ValueError):
                print('Enter a valid inventory index')
            else:
                print(item.name)
                if item.status == 'health buff':
                    print(f'(+{item.effect} health)')
                    self.health += item.effect
                    self.inventory.remove(item)
                elif item.status == 'defense':
                    print(f'(+{item.effect} defense)')
                    self.defense += item.effect
                    self.inventory.remove(item)
                elif item.status == 'weapon':
                    print(f'You equipped {item.name}')
                    self.atk = item.damage
                else:
                    print("You'll use this later on.")
                break

    def next_room(self,room):
        if room.locked == False:
            print('you progressed to the next room')
            self.current_room += 1
        elif room.locked == True:
            print('this area is locked')

    def interact(self,other):
        print(other.speech)

    def give_item(self,other):
        while True:
            try:
                choose_item = input('enter the item index: ')
                item = self.inventory[choose_item]
            except(IndexError, ValueError):
                print('Enter a valid inventory index')
            else:
                self.inventory.remove(item)
                other.inventory.append(item)
                