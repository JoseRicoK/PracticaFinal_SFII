import random

print('Welcome to the Guess My Word App')
game_dict = {'sports':['cycling', 'swimming', 'football', 'tennis', 'basketball', 'badminton' ] ,'colors':['red', 'orange', 'yellow', 'green', 'blue', 'purple'] ,'fruits':['apple', 'orange', 'lemon', 'cherry', 'pear', 'kiwi'] ,'classes':['history', 'language', 'math', 'science', 'english', 'french']}
game_keys = []
for keys in game_dict:
    game_keys.append(keys)

comprobante = True
while comprobante:
    game_category = random.choice(game_keys)
    