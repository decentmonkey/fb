default hostelStreetStage = 0

label hostel_street:
    $ print "enter_hostel_street"
    $ miniMapData = []

    $ scene_name = "hostel_street"
    $ sceneIsStreet = True
    $ scene_caption = _("HOSTEL STREET")
    $ clear_scene_from_objects(scene_name)


    $ scene_image = "scene_Hostel_Street" + day_suffix
    if gameStage == 2:
        $ add_object_to_scene("Monica", {"type":2, "base":"Hostel_Street_Monica_" + cloth + day_suffix, "click" : "hostel_street_environment", "actions" : "l", "zorder" : 10})
    if gameStage == 3:
        $ add_object_to_scene("Monica", {"type":2, "base":"Hostel_Street_Monica2_" + cloth + day_suffix, "click" : "hostel_street_environment", "actions" : "l", "zorder" : 10})

    $ add_object_to_scene("Teleport_Hostel_Street2", {"type":2, "base":"Hostel_Street_Teleport_Hostel_Street2", "click" : "hostel_street_teleport", "actions" : "lw", "zorder" : 0, "b":0.13, "tint":[1.0, 1.0, 0.7]})

#    $ add_object_to_scene("Car", {"type":2, "base":"hostel_street_Car", "click" : "hostel_street_environment", "actions" : "l", "zorder" : 0})

    $ add_object_to_scene("Teleport_Hostel_Edge_C", {"type":3, "text" : _("УГОЛ ДОМА"), "rarrow" : "arrow_right_2", "base":"Hostel_Street_Teleport_Hostel_Edge_C", "click" : "hostel_street_teleport", "xpos" : 1655, "ypos" : 822, "zorder":15})
    $ add_object_to_scene("Teleport_Shawarma", {"type":3, "text" : _("НАЗАД К ШАВЕРМЕ"), "rarrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "hostel_street_teleport", "xpos" : 210, "ypos" : 956, "zorder":15})

    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label hostel_street_teleport(obj_name, obj_data):
    if obj_name == "Teleport_Hostel_Edge_C":
        if cloth_type == "Nude":
            call change_scene("hostel_edge_1_c", "Fade", "snd_walk_barefoot")
            return
        call change_scene("hostel_edge_1_c", "Fade", "highheels_run2")
        return
    if obj_name == "Teleport_Shawarma":
        call change_scene("whores_place_shawarma", "Fade_long", "highheels_run2")
        return
    if obj_name == "Teleport_Hostel_Street2":
        if act == "l":
            if gameStage == 3:
                mt "Я не пойду туда! Там насильники! И я теперь должна $10.000 управляющей этой дыры."
                return
            if gameStage == 2 and gameSubStage == 2:
                call hostel_street_dialogue1()
                return
        if act == "w":
            if gameStage == 3:
                mt "Я не пойду туда! Там насильники! И я теперь должна $10.000 управляющей этой дыры."
                return
            if gameStage == 2:
                $ autorun_to_object("hostel_street2", "hostel_street_dialogue1")
            if cloth_type == "Nude":
                call change_scene("hostel_street2", "Fade", "snd_walk_barefoot")
                return
            call change_scene("hostel_street2")
            return
    return
label hostel_street_environment(obj_name, obj_data):
    if obj_name == "Monica":
        if gameStage == 2 and gameSubStage == 2:
            call hostel_street_dialogue1()
            return
        if gameStage == 3 and gameSubStage == 0:
            call hostelAfterJail_street_dialogue0()
            return
        if gameStage == 3 and gameSubStage == 1:
            mt "Мне надо убираться отсюда!"
            "Насильники могут быть рядом!"
            return
            call hostelAfterJail_street_dialogue3()
            return


    return
