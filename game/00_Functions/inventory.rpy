init python:
    def define_inventory_object(name, data):
        inventory_objects[name] = data
        return

    def get_inventory_index_by_name(name):
        for idx in range(0, len(inventory)):
            if inventory[idx][0] == name:
                return idx
        return -1

    def add_inventory(name, amount, notification = False):
        global inventory
        idx = get_inventory_index_by_name(name)
        if idx != -1:
            inventory[idx][1] += amount
        else:
            inventory.insert(0, [name, amount])
        if notification == True:
            if amount > 0:
                renpy.show_screen("notify", str(amount) + "x " + __(inventory_objects[name]["description"]) + " received")
            else:
                renpy.show_screen("notify", inventory_objects[name]["description"] + " received")
        return

    def remove_inventory(name, amount, notification = False):
        global inventory
        idx = get_inventory_index_by_name(name)
        if idx == -1: return
        if amount == 0 or inventory[idx][1] <= amount:
            inventory.pop(idx)
        else:
            inventory[idx][1] -= amount
        if notification == True:
            if amount > 0:
                renpy.show_screen("notify", str(amount) + "x " + __(inventory_objects[name]["description"]) + " decreased")
            else:
                renpy.show_screen("notify", inventory_objects[name]["description"] + " decreased")
        return

    def check_inventory(name, amount = 1):
        idx = get_inventory_index_by_name(name)
        if idx == -1: return False
        if inventory[idx][1] >= amount: return True
        return False
