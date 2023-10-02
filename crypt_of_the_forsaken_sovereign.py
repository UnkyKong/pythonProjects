"""
The Crypt of the Forsaken Sovereign
is a text-based adventure game.
it contains 8 rooms, 6 items
and 1 boss, the Lich King.
The entrance of the room is the Forsaken Gateway.
South of the Forsaken Gateway is the Decrepit Library, which contains the Ancient Scroll.
To the west of the Decrepit Library is the Cursed Mausoleum, which contains the Stone of the Grave Warden.
To the south of the Decrepit Library is the Hall of Mirrors, which contains the Mirror of True Sight.
To the South of the Cursed Mausoleum is the Lich's Sanctum where the Lich King waits.
To the east of the Hall of Mirrors is the Shrine to Forgotten Deities, which contains the Amulet of the Dawn Bringer.
To the south of the Hall of Mirror is the Torture Chamber, which contains the Chains of Binding.
To the North of the Shrine to Forgotten Deities is the Vault of the Soulless,
which contains the Dagger of Eternity's End.
"""
# Dungeon layout of rooms and connection rooms
dungeon = {
    'Forsaken Gateway': {'south': 'Decrepit Library'},
    'Decrepit Library': {'north': 'Forsaken Gateway', 'south': 'Hall of Mirrors', 'west': 'Cursed Mausoleum'},
    'Hall of Mirrors': {'north': 'Decrepit Library', 'south': 'Torture Chamber', 'east': 'Shrine to Forgotten Deities'},
    'Cursed Mausoleum': {'east': 'Decrepit Library', 'south': 'Lich\'s Sanctum'},
    'Shrine to Forgotten Deities': {'west': 'Hall of Mirrors', 'north': 'Vault of the Soulless'},
    'Torture Chamber': {'north': 'Hall of Mirrors'},
    'Lich\'s Sanctum': {'north': 'Cursed Mausoleum'},
    'Vault of the Soulless': {'south': 'Shrine to Forgotten Deities'}
}

# Items and their locations
items = {
    'Forsaken Gateway': '',
    'Decrepit Library': 'Ancient Scroll',
    'Hall of Mirrors': 'Mirror of True Sight',
    'Cursed Mausoleum': 'Stone of the Grave Warden',
    'Shrine to Forgotten Deities': 'Amulet of the Dawn Bringer',
    'Torture Chamber': 'Chains of Binding',
    'Vault of the Soulless': 'Dagger of Eternity\'s End',
    'Lich\'s Sanctum': 'Lich King',
}

# Dungeons room descriptions
room_descriptions = {
    'Forsaken Gateway': 'A cold, wind-swept entrance with ancient ruins marking the start of the dungeon.',
    'Decrepit Library': 'A large room with shelves upon shelves of decaying books. Dust fills the air, and '
                        'the faint sound of whispering can be heard.',
    'Hall of Mirrors': 'A corridor with walls made entirely of mirrors. As you walk, your reflection seems '
                       'to move in eerie, unexpected ways.',
    'Cursed Mausoleum': 'A dark, stone structure. The walls are adorned with the names of forgotten souls, and '
                        'an ominous energy pervades the air.',
    'Shrine to Forgotten Deities': 'An altar dedicated to gods long lost to time. Flickering candles and offerings '
                                   'suggest recent visitors.',
    'Torture Chamber': 'A grim room filled with devices of pain and torment. Chains hang from the ceiling, and the '
                       'floor is stained with the memories of suffering.',
    'Lich\'s Sanctum': 'The heart of the dungeon. A room dominated by a large throne where the Lich King waits.',
    'Vault of the Soulless': 'A hidden chamber containing treasures beyond imagination, guarded by spirits devoid of '
                             'consciousness.'
}

# Item descriptions
item_descriptions = {
    'Ancient Scroll': 'A scroll, yellowed with age, with cryptic writings that promise arcane knowledge.',
    'Mirror of True Sight': 'A mirror that reflects not just your appearance, but your soul. Gazing into it might '
                            'reveal hidden truths.',
    'Stone of the Grave Warden': 'A dark, cold stone inscribed with protective runes. It emanates a subtle, '
                                 'protective aura.',
    'Amulet of the Dawn Bringer': 'A gold amulet with a gem that gleams like the morning sun. '
                                  'It feels warm to the touch.',
    'Chains of Binding': 'Heavy chains that, when worn, grant the bearer power over the spirits.',
    'Dagger of Eternity\'s End': 'A blade forged from materials not of this world. '
                                 'It shimmers with an otherworldly glow.',
    'Lich King': 'A skeletal figure draped in royal garb, holding a staff that pulses with dark energy.'
}

# list of player commands
commands = ['north', 'south', 'east', 'west', 'pickup', 'exit']


# function to handle encountering the boss
def encounter(inventory):
    print("\nAs you step into the Lich's Sanctum, a chilling wind sweeps through the room.")
    print("From the shadows, the Lich King emerges, his hollow eyes fixed on you.")
    print("Lich King: 'Mortal! You dare to challenge me in my own domain?'")
    # Win condition for beating the Lich
    required_items = ['Ancient Scroll', 'Mirror of True Sight', 'Stone of the Grave Warden',
                      'Amulet of the Dawn Bringer', 'Chains of Binding', 'Dagger of Eternity\'s End']

    missing_items = [item for item in required_items if item not in inventory]
    # If missing items, you lose the game.
    if missing_items:
        print("\nLich King: 'You think you can face me without all the artifacts? Foolish mortal!'")
        print("You realize you're missing the following items:", ', '.join(missing_items))
        print("\nThe Lich King's power overwhelms you, and darkness takes hold...")
        print('YOU LOSE :(')
    else:
        print('\nThe Lich King stumbles backward, sensing the power of the artifacts you carry.')
        print("Lich King: 'No... it cannot be! The artifacts...'")
        print('With the combined strength of the six items, ')
        print('you banish the Lich King, freeing the crypt from his dark influence.')
        print('YOU WIN!!')

    exit()


# function used to handle user inputs
def execute_command(command, current_room, inventory):
    # If player input not in commands let them know and relist commands for reference
    if command not in commands:
        print('Invalid command. Please use one of the following:')
        print(commands)
        return current_room, inventory
    # If command is exit, end game
    if command == 'exit':
        exit()
    _room = dungeon[current_room]
    # If command is pickup, call pickup_item function
    if command == 'pickup':
        inventory = pickup_item(current_room, inventory)
    # if the direction commands are used call the move_between_room function.
    else:
        new_room = move_between_room(command, _room)
        # if the current room had a room in the location of the command return true and update the current room
        if new_room:
            current_room = new_room
    return current_room, inventory


# function used to update users current room
def move_between_room(command, room):
    # check dungeon to see if current room has a room attached in the direction player chose
    if command in room:
        next_room = room[command]
        print('\nMoving {}, you enter {}'.format(command, next_room))
        # adds room description first time the player enters the room.
        if room_descriptions[next_room] != '':
            print(room_descriptions[next_room])
        # updates room description, so it won't be displayed again.
        room_descriptions[next_room] = ''
        return next_room
    # If current room does not have an attached room return to the game loop with no changes
    else:
        print('You can\'t go that way')
        return None


# function used to update user's inventory with item
def pickup_item(current_room, inventory):
    # add current item to inventory.
    inventory.append(items[current_room])
    print('You picked up the {}, and added it to your inventory!'.format(items[current_room]))
    # removes item from the room.
    items[current_room] = ''
    return inventory


# function called for game loop
def the_game():
    # sets the initial location and inventory for the player
    current_room = 'Forsaken Gateway'
    inventory = []
    # Introduction message
    print('\nWelcome to the Crypt of the Forsaken Sovereign!')
    print('A short text based game that will have you exploring the depths of an old abandoned crypt\n')
    '''
    now the player will be given directions on how to move around the dungeon, as well as how to pick up items.  
    They can also exit the game.
    To move from room to room the player will simply type the cardinal direction they wish to go.
    to pick up an item the player will type 'pickup' and the item in the room will be added to their inventory.
    to exit the game the player will type 'exit'.
    '''
    # Directions for the game.
    print('To navigate the dungeon, simply type the direction you wish to go.')
    print('Directions are: north, south, east, west.\n')
    print('To pick up an item, type pickup and the item will be added to your inventory.')
    print('To exit the game, type exit.\n')
    print('To beat the game, you must find all the items before you encounter the Lich King.')
    print('Good luck!\n')

    print('Your journey begins in {} \nThe Forsaken Gateway\n'.format(room_descriptions[current_room]))
    # Actual Game Loop
    while True:
        # If the player enters the Lich's Sanctum run encounter function.
        if current_room == 'Lich\'s Sanctum':
            encounter(inventory)
        # If there is in an item in the current room print the description for the player.
        if items[current_room] != '':
            print('You see {} on the ground'.format(item_descriptions[items[current_room]]))
        # Informs player of current location and items that they have collected in the journey
        print('\nYou are in the {}'.format(current_room))
        print('Your Inventory: {}\n'.format(inventory))
        # Ask for user input.
        command = input('What do you want to do?\n')
        # input command with player location and their inventory into execute command function
        current_room, inventory = execute_command(command, current_room, inventory)


# Launch the Game
the_game()
