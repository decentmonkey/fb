default laundry2_box2_empty = False
default laundry2_box2_iron_looked = False

label basement_laundry2_box1:
    $ miniMapData = []
    call miniMapHouseGenerate()
    $ scene_name = "basement_laundry2_box1"
    $ scene_caption = _("Laundry")
    $ clear_scene_from_objects(scene_name)
    $ scene_image = "scene_Laundry2_Box1"

    $ add_object_to_scene("Clothes_Pin", {"type":2, "base":"Basement_Laundry2_Box1_Clothes_Pin", "click" : "basement_laundry_environment", "actions" : "l", "zorder" : 0})
    $ add_object_to_scene("Detergents", {"type":2, "base":"Basement_Laundry2_Box1_Detergents", "click" : "basement_laundry2_environment", "actions" : "l", "zorder" : 0})
    $ add_object_to_scene("Towels", {"type":2, "base":"Basement_Laundry2_Box1_Towels", "click" : "basement_laundry2_environment", "actions" : "l", "zorder" : 0})

    $ add_object_to_scene("Teleport_Basement2_Laundry", {"type":3, "text" : _("НАЗАД"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "basement_laundry2_boxes_teleport", "xpos" : 960, "ypos" : 956, "zorder":11})
    return

label basement_laundry2_box2:
    $ miniMapData = []
    call miniMapHouseGenerate()
    $ scene_name = "basement_laundry2_box2"
    $ scene_caption = _("Laundry")
    $ clear_scene_from_objects(scene_name)
    if laundry2_box2_empty == False:
        $ scene_image = "scene_Laundry2_Box2"
        if laundrySearchingForIron == True:
            $ add_object_to_scene("Iron", {"type":2, "base":"Basement_Laundry2_Box2_Iron", "click" : "basement_laundry2_boxes_environment", "actions" : "lh", "zorder" : 0})
        else:
            $ add_object_to_scene("Iron", {"type":2, "base":"Basement_Laundry2_Box2_Iron", "click" : "basement_laundry2_boxes_environment", "actions" : "l", "zorder" : 0})
    else:
        $ scene_image = "scene_Laundry2_Box2_Empty"

    $ add_object_to_scene("Teleport_Basement2_Laundry", {"type":3, "text" : _("НАЗАД"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "basement_laundry2_boxes_teleport", "xpos" : 960, "ypos" : 956, "zorder":11})
    return

label basement_laundry2_boxes_teleport(obj_name, obj_data):
    call change_scene("basement_laundry2", "Fade", "desk_close") from _call_change_scene_11
    return

label basement_laundry2_boxes_environment(obj_name, obj_data):
    if obj_name == "Iron":
        if obj_data["action"] == "l":
            if laundrySearchingForIron == True:
                m "Отлично!
                Я нашла утюг."
            else:
                m "Какой-то утюг."
                "Зачем он мне?"
            $ laundry2_box2_iron_looked = True
        if obj_data["action"] == "h":
            sound take_iron
            $ autorun_to_object("basement_laundry2_box2", "basement_laundry2_box2_take_iron")
            $ laundry2_box2_empty = True
            call refresh_scene() from _call_refresh_scene
            return
    return

label basement_laundry2_box2_take_iron:
    $ define_inventory_object("iron", {"description" : _("Утюг"), "label_suffix" : "_use_iron", "default_label" : False, "default_nolabel" : "cant_use", "icon" : "Inventory/iron" + res.suffix + ".png"})
    $ add_inventory("iron", 1, True)
    $ remove_objective("laundry_find_iron")
    $ laundryIronFound = True
    $ laundrySearchingForIron = False

    imgc Monica_HomeCloth1_Happy
    m "Отлично!
    Я нашла утюг."

    imgc Monica_HomeCloth1_Thinking1
    "Теперь надо погладить платье."

    $ add_objective("iron_dress", _("Погладить платье"), c_pink, 20)
    $ landryIroningActive = True
    $ laundryBoxesActive = False

    return



















#
