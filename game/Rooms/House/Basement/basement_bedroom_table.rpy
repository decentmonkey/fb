label basement_bedroom_table:
    $ print "enter_basement_bedroom_table"
    $ miniMapData = []

    $ scene_name = "basement_bedroom_table"
    $ scene_caption = _("BASEMENT")
    $ clear_scene_from_objects(scene_name)

    $ scene_image = "scene_Basement_Bedroom_Table"

    $ add_object_to_scene("Book", {"type":2, "base":"Basement_Table_Book", "click" : "basement_bedroom2_environment", "actions" : "l", "zorder" : 0})
    $ add_object_to_scene("Box", {"type":2, "base":"Basement_Table_Box", "click" : "basement_bedroom_table_environment", "actions" : "lh", "zorder" : 0, "b":0.13})
    $ add_object_to_scene("Lamp", {"type":2, "base":"Basement_Table_Lamp", "click" : "basement_bedroom2_environment", "actions" : "l", "zorder" : 0})

    if basementBedroomJournal == True:
        $ add_object_to_scene("Journal", {"type":2, "base":"Basement_Bedroom_Table_Journal", "click" : "basement_bedroom_table_environment", "actions" : "lh", "zorder" : 1})

    $ add_object_to_scene("Teleport_Bedroom_Back", {"type":3, "text" : _("НАЗАД"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "basement_bedroom_table_teleport", "xpos" : 960, "ypos" : 956, "zorder":11})

    return

label basement_bedroom_table_teleport(obj_name, obj_data):
    if obj_name == "Teleport_Bedroom_Back":
        call change_scene("basement_bedroom2")
        return
    return

label basement_bedroom_table_environment(obj_name, obj_data):
    if obj_name == "Box":
        if act == "l":
            mt "Старый ящик в старом столе..."
        if act == "h":
            sound snd_door_locked1
            $ renpy.pause(1.0)
            mt "Закрыт..."
            "Мне неинтересно что там..."

    if obj_name == "Journal":
        if act == "l":
            mt "Это мой журнал."
        if act == "h":
            call afterJailHouse_dialogue21()
            return
    return
