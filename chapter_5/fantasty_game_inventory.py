player_inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def display_inventory(inventory):
    print("Inventory:")
    item_count = 0
    for k, v in inventory.items():
        print('{} {}'.format(v, k))
        item_count += v
    print("Total amount of items: {}".format(item_count), end='\n\n')

def add_to_inventory(inventory, added_items):
    for item in added_items:
        inventory.setdefault(item, 0)
        inventory[item] += 1 

display_inventory(player_inventory)
add_to_inventory(player_inventory, dragon_loot)
display_inventory(player_inventory)