hero = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def display_inventory(inventory):
    total = 0
    print('Inventory: ')
    for k, v in hero.items():
        print(str(v) + ' ' + k)
        total += v

    print('Total number of items: {}'.format(total))

def add_to_inventory(inventory, addeditems):
    for n in range(len(addeditems)):
        if (addeditems[n] in inventory.keys()):
            inventory[addeditems[n]] = inventory[addeditems[n]] + 1
        else:
            inventory.setdefault(addeditems[n], 1)


display_inventory(hero)
add_to_inventory(hero, dragon_loot)
display_inventory(hero)
