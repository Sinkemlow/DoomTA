from sys import exit
from random import randint


class Character(object):

    def __init__(self, health):
        self.health = health


class Player(Character):
    
    def __init__(self, health, ammo):
        super(Player, self).__init__(health) 
        self.ammo = ammo

    def combat(self):
       
        hit_chance = randint(1, 100)

        # Cheat code!
#        hit_chance = 100
        print "The player has %s hit chance" % hit_chance
        
        if hit_chance >= 75:
            print "You kill your enemy in a single shot!"
            self.ammo -= 1
            print "The player now has %s ammo" % self.ammo
            return 'success'
        elif hit_chance < 75 and hit_chance > 50:
            print "You kill your enemy in 2 shots!"
            self.ammo -= 2
            print "You now have %s ammo" % self.ammo
            return 'success'
        else:
            print "You miss wildly, giving your enemy chance to aim and kill you instantly!"
            return 'failure'


class Enemy(Character):

    def __init__(self, health):
        super(Enemy, self).__init__(health)


class Room(object):
    def enter(self):
        print "To be populated should Rooms need common attributes"
        exit(1)


class Engine(object):
    def __init__(self, room_map):
        self.room_map = room_map

    def play(self):
        current_room = self.room_map.starting_room()
        
        while True:
            print "\n--------"
            next_room_name = current_room.enter()
            current_room = self.room_map.next_room(next_room_name)


class Death(object):
    def enter(self):
        print "You died. GAME OVER!!!"
        exit(1)


class LoadingBay(Room):
    def enter(self):
        print "You enter the Loading Bay."
        action = raw_input("> ")

        if action == "good":
            return 'control_room'
        
        elif action == "bad":
            return 'death'

        else:
            print "I DON'T UNDERSTAND"
            return 'loading_bay'


class ControlRoom(Room):
    def enter(self):
        print "You enter the Control Room, an enemy marine spots you from across the room."

        action = raw_input("> ")

        if action == "attack" or action == "shoot":
            if a_player.combat() == 'success':
                return 'toxic_room'
            else:
                return 'death'
        else:
            print "You hesitate!"
            return 'death'


class ToxicRoom(Room):
    def enter(self):
        print "You enter the Toxic Room, an imp spots you from across the room!"
        
        action = raw_input("> ")

        if action == "attack" or action == "shoot":
            if a_player.combat() == 'success':
                return 'final_room'
            else:
                return 'death'
        else:
            print "You hesitate!"
            return 'death'


class FinalRoom(Room):
    def enter(self):
        print "You enter the Final Room, a marine spots you from across the room!"

        action = raw_input("> ")

        if action == "attack" or action == "shoot":
            if a_player.combat() == 'success':
                return 'elevator'
            else:
                return 'death'
        else:
            print "You hesitate!"
            return 'death'


class Elevator(Room):
    def enter(self):
        print "You enter the Elevator, a large green button flashes on a panel"
        action = raw_input("> ")

        if action == "push button" or action == "press button":
            print "You exit to the next level!"
            exit(1)
        else:
            print "You hesitate!"
            return 'death'


class Map(object):

    rooms = {
        'loading_bay': LoadingBay(),
        'control_room': ControlRoom(),
        'toxic_room': ToxicRoom(),
        'final_room': FinalRoom(),
        'elevator': Elevator(),
        'death': Death()
    }

    def __init__(self, start_room):
        self.start_room = start_room

    def next_room(self, room_name):
        return Map.rooms.get(room_name)

    def starting_room(self):
        return self.next_room(self.start_room)

a_player = Player(100, 20)
a_map = Map('loading_bay')
a_game = Engine(a_map)
a_game.play()
