#! python3

inv = {'rope':1,'torch':6,'gold':42,'dagger':1,'arrow':12}

def display_inv(inv):
    print('Inventory:')
    item_total = 0
    for k,v in inv.items():
        print(str(v) + ' ' + k)
        item_total += v
    print()
    print("The total number of items: " + str(item_total))

display_inv(inv)
