label hostel_edge_1_b:
    $ print "enter_hostel_edge_1_b"
    $ miniMapData = []

    $ scene_name = "hostel_edge_1_b"
    $ sceneIsStreet = True
    $ scene_caption = _("BLIND ALLEY")
    $ clear_scene_from_objects(scene_name)

    $ localDaySuffix = ""
    if day_suffix != "":
        $ localDaySuffix = day_suffix + "2"
    $ scene_image = "scene_hostel_edge_1_b" + localDaySuffix
    $ add_object_to_scene("Monica", {"type":2, "base":"hostel_edge_1_b_Monica_" + cloth + localDaySuffix, "click" : "hostel_edge_1_b_environment", "actions" : "l", "zorder" : 10})

    $ add_object_to_scene("Door1", {"type":2, "base":"Hostel_Edge_1_b_Door1", "click" : "hostel_edge_1_b_environment", "actions" : "l", "zorder" : 11, "b":0.13})
    $ add_object_to_scene("Door2", {"type":2, "base":"Hostel_Edge_1_b_Door2", "click" : "hostel_edge_1_b_environment", "actions" : "l", "zorder" : 11, "b":0.13})
    $ add_object_to_scene("Door3", {"type":2, "base":"Hostel_Edge_1_b_Door3", "click" : "hostel_edge_1_b_environment", "actions" : "l", "zorder" : 11, "b":0.13})
    $ add_object_to_scene("Fence", {"type":2, "base":"Hostel_Edge_1_b_Fence", "click" : "hostel_edge_1_b_environment", "actions" : "l", "zorder" : 11, "b":0.13})
    $ add_object_to_scene("Trash1", {"type":2, "base":"hostel_edge_1_b_Trash1", "click" : "hostel_edge_1_b_environment", "actions" : "l", "zorder" : 11, "b":0.13})
    $ add_object_to_scene("Trash2", {"type":2, "base":"hostel_edge_1_b_Trash2", "click" : "hostel_edge_1_b_environment", "actions" : "l", "zorder" : 11, "b":0.13})
    $ add_object_to_scene("Trash3", {"type":2, "base":"hostel_edge_1_b_Trash3", "click" : "hostel_edge_1_b_environment", "actions" : "l", "zorder" : 11, "b":0.13})
    $ add_object_to_scene("Trash4", {"type":2, "base":"hostel_edge_1_b_Trash4", "click" : "hostel_edge_1_b_environment", "actions" : "l", "zorder" : 11, "b":0.13})
    $ add_object_to_scene("Trash5", {"type":2, "base":"hostel_edge_1_b_Trash5", "click" : "hostel_edge_1_b_environment", "actions" : "l", "zorder" : 11, "b":0.13})
    $ add_object_to_scene("Window1", {"type":2, "base":"hostel_edge_1_b_Window1", "click" : "hostel_edge_1_b_environment", "actions" : "l", "zorder" : 11, "b":0.13})
    $ add_object_to_scene("Window2", {"type":2, "base":"hostel_edge_1_b_Window2", "click" : "hostel_edge_1_b_environment", "actions" : "l", "zorder" : 11, "b":0.13})
    $ add_object_to_scene("Window3", {"type":2, "base":"hostel_edge_1_b_Window3", "click" : "hostel_edge_1_b_environment", "actions" : "l", "zorder" : 11, "b":0.13})
    $ add_object_to_scene("Window4", {"type":2, "base":"hostel_edge_1_b_Window4", "click" : "hostel_edge_1_b_environment", "actions" : "l", "zorder" : 11, "b":0.13})
    $ add_object_to_scene("Window5", {"type":2, "base":"hostel_edge_1_b_Window5", "click" : "hostel_edge_1_b_environment", "actions" : "l", "zorder" : 11, "b":0.13})
#    $ add_object_to_scene("Teleport_Hostel_1_a", {"type":2, "base":"hostel_edge_1_b_Teleport_Hostel_Edge_a", "click" : "hostel_edge_1_b_teleport", "actions" : "lw", "zorder" : 11, "b":0.13, "tint":[1.0, 1.0, 0.8]})

    $ add_object_to_scene("Teleport_Hostel_1_a", {"type":3, "text" : _("ДРУГАЯ СТОРОНА"), "rarrow" : "arrow_right_2", "base":"Hostel_Edge_1_b_Teleport_Hostel_Edge_A", "click" : "hostel_edge_1_b_teleport", "xpos" : 1670, "ypos" : 910, "zorder":15})
    $ add_object_to_scene("Teleport_Hostel_1_c", {"type":3, "text" : _("УЛИЦА"), "larrow" : "arrow_left_2", "base":"Hostel_Edge_1_b_Teleport_Hostel_Edge_C", "click" : "hostel_edge_1_b_teleport", "xpos" : 600, "ypos" : 963, "zorder":15})

    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label hostel_edge_1_b_teleport(obj_name, obj_data):
    if obj_name == "Teleport_Hostel_1_c":
        if cloth_type == "Nude":
            call change_scene("hostel_edge_1_c", "Fade", "snd_walk_barefoot")
            return
        call change_scene("hostel_edge_1_c")
        return
    if obj_name == "Teleport_Hostel_1_a":
        if cloth_type == "Nude":
            call change_scene("hostel_edge_1_a", "Fade", "snd_walk_barefoot")
            return
        call change_scene("hostel_edge_1_a")
        return
    return
label hostel_edge_1_b_environment(obj_name, obj_data):
    if obj_name == "Monica":
        if gameStage == 3 and gameSubStage == 1:
            call hostelAfterJail_street_dialogue3()
            return
        if hostelStreetStage == 0:
            mt "Мне холодно и мокро."
            "Надо найти где укрыться."
            "И это явно не здесь!"

    if obj_name == "Fence":
        mt "Железный забор..."
        "Нет, я преодолею все заборы в моей жизни!!!"
        "Я не сдамся!!!"

    if obj_name == "Door1":
        mt "Какая-то дверь..."
    if obj_name == "Door2":
        mt "Какая-то дверь..."
    if obj_name == "Door3":
        mt "Какая-то дверь..."

    if obj_name == "Trash1" or obj_name == "Trash2" or obj_name == "Trash3" or obj_name == "Trash4" or obj_name == "Trash5":
        mt "Просто мусор..."
    if obj_name == "Window1" or obj_name == "Window2" or obj_name == "Window3" or obj_name == "Window4":
        mt "Заколоченное окно..."
    if obj_name == "Window5":
        mt "Какое-то окно..."

    return
