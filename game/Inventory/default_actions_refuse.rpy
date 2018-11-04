label cant_use(name, item_inventory, item_inventory_data, object_data):
    $ item_description = item_inventory_data["description"]
    "[item_description!t] and It? I can't use that!"
    return
