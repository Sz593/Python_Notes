#! python3

def display_inv(inv):
    print('Inventory:')
    item_total = 0
    for k,v in inv.items():
        print(str(v) + ' ' + k)
        item_total += v
    print()
    print("The total number of items: " + str(item_total))

def addToInv(inv,addedItems):
    for itm in addedItems:
        try:
            inv[itm] += 1
        except KeyError:
            inv.setdefault(itm,1)
    return inv
    


inventory = {'rope':1,'torch':6,'gold':42,'dagger':1,'arrow':12}
dragonLoot = ['gold','dagger','gold','gold','ruby']

display_inv(inventory)
addToInv(inventory,dragonLoot)
display_inv(inventory)
