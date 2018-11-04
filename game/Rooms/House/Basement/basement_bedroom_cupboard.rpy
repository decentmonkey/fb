default basementBedroom2CupboardReturnScene = False

label basement_bedroom2_cupboard:
    $ print "enter_basement_bedroom2_cupboard"
    $ miniMapData = []

    $ scene_name = "basement_bedroom2_cupboard"
    $ scene_caption = _("BASEMENT")
    $ clear_scene_from_objects(scene_name)

    $ scene_image = "scene_Basement_Bedroom_Cupboard1"

    $ add_object_to_scene("Box", {"type":2, "base":"Basement_Bedroom_Cupboard_Box", "click" : "basement_bedroom2_cupboard_environment", "actions" : "lh", "zorder" : 0})

    $ add_object_to_scene("Teleport_Bedroom_Back", {"type":3, "text" : _("НАЗАД"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "basement_bedroom2_cupboard_teleport", "xpos" : 960, "ypos" : 956, "zorder":11})

    return

label basement_bedroom2_cupboard_teleport(obj_name, obj_data):
    if obj_name == "Teleport_Bedroom_Back":
        call change_scene(basementBedroom2CupboardReturnScene)
        return
    return

label basement_bedroom2_cupboard_environment(obj_name, obj_data):
    if obj_name == "Box":
        if act == "l":
            mt "Старый ящик в старом шкафу..."
        if act == "h":
            sound snd_door_locked1
            $ renpy.pause(1.0)
            mt "Закрыт..."
            "Мне неинтересно что там..."
    return
