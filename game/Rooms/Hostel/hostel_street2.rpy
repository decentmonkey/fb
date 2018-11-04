label hostel_street2:
    $ print "enter_hostel_street2"
    $ miniMapData = []

    $ scene_name = "hostel_street2"
    $ sceneIsStreet = True
    $ scene_caption = _("HOSTEL ENTRANCE")
    $ clear_scene_from_objects(scene_name)


    $ scene_image = "scene_hostel_street2" + day_suffix

    $ add_object_to_scene("Teleport_hostel_reception", {"type":2, "base":"Hostel_Street2_Door", "click" : "hostel_street2_teleport", "actions" : "lw", "zorder" : 0, "b":0.13, "tint":[1.0, 1.0, 0.7]})
    $ add_object_to_scene("Poster", {"type":2, "base":"Hostel_Street2_Poster", "click" : "hostel_street2_environment", "actions" : "l", "zorder" : 0, "b":0.13, "tint":[1.0, 1.0, 0.7]})
    $ add_object_to_scene("Pipes", {"type":2, "base":"Hostel_Street2_Pipes", "click" : "hostel_street2_environment", "actions" : "l", "zorder" : 0, "b":0.13, "tint":[1.0, 1.0, 0.7]})

#    $ add_object_to_scene("Car", {"type":2, "base":"hostel_street2_Car", "click" : "hostel_street2_environment", "actions" : "l", "zorder" : 0})

    $ add_object_to_scene("Teleport_Hostel_Street", {"type":3, "text" : _("НАЗАД"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "hostel_street2_teleport", "xpos" : 960, "ypos" : 956, "zorder":11})

    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label hostel_street2_teleport(obj_name, obj_data):
    if obj_name == "Teleport_Hostel_Street":
        if cloth_type == "Nude":
            call change_scene("hostel_street", "Fade", "snd_walk_barefoot")
            return
        call change_scene("hostel_street")
        return
    if obj_name == "Teleport_hostel_reception":
        if act == "l":
            mt "Это вход в хостел..."
        if act == "w":
            if hostelReceptionStage == 0:
                music Stealth_Groover
                $ autorun_to_object("hostel_reception", "hostelAfterJail_dialogue1")
            if hostelReceptionStage > 1:
                music Groove2_85

            call change_scene("hostel_reception", "Fade_long", "snd_jail_door")
            return
        return
    if obj_name == "Teleport_hostel_street22":
        if act == "l":
            if gameStage == 2 and gameSubStage == 2:
                call hostel_street2_dialogue1()
                return
        if act == "w":
            $ autorun_to_object("hostel_street22", "hostel_street2_dialogue1")
            call change_scene("hostel_street22")
            return
    return
label hostel_street2_environment(obj_name, obj_data):
    if obj_name == "Poster":
        if hostelStreetStage == 0:
            mt "Это такая рекламная вывеска отеля?"
            "Они что, пытаются рассмешить меня???"
    if obj_name == "Pipes":
        if hostelStreetStage == 0:
            mt "Это что за канализация?"
            "Надеюсь мне не придется из этого пить там?"
            "Я надеюсь у них хорошая бутилированная вода?"
            "Как может быть иначе?"

    return
