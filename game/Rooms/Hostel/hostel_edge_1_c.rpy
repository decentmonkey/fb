default hostelWalkStreetEnabled = False
default localDaySuffix = ""

label hostel_edge_1_c:
    $ print "enter_hostel_edge_1_c"
    $ miniMapData = []

    $ scene_name = "hostel_edge_1_c"
    $ sceneIsStreet = True
    $ scene_caption = _("HOSTEL EDGE")
    $ clear_scene_from_objects(scene_name)

    $ localDaySuffix = ""
    if day_suffix != "":
        $ localDaySuffix = day_suffix + "2"
    $ scene_image = "scene_Hostel_Edge_1_c" + localDaySuffix
    $ add_object_to_scene("Monica", {"type":2, "base":"hostel_edge_1_c_Monica_" + cloth + localDaySuffix, "click" : "hostel_edge_1_c_environment", "actions" : "l", "zorder" : 10})

    $ add_object_to_scene("Teleport_Hostel_1_a", {"type":2, "base":"Hostel_Edge_1_c_Teleport_Hostel_Edge_a", "click" : "hostel_edge_1_c_teleport", "actions" : "lw", "zorder" : 11, "b":0.13, "tint":[1.0, 1.0, 0.8]})

    $ add_object_to_scene("Teleport_Hostel_Street", {"type":3, "text" : _("К ХОСТЕЛУ"), "larrow" : "arrow_up_2", "base":"Hostel_Edge_1_c_Teleport_Hostel_Street", "click" : "hostel_edge_1_c_teleport", "xpos" : 1683, "ypos" : 330, "zorder":15})
    $ add_object_to_scene("Teleport_Walk_Street", {"type":3, "text" : _("ГУЛЯТЬ ПО УЛИЦЕ"), "larrow" : "arrow_down_2", "base":"Hostel_Edge_1_c_Teleport_Walk_Streets", "click" : "hostel_edge_1_c_teleport", "xpos" : 1528, "ypos" : 920, "zorder":15})

    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label hostel_edge_1_c_teleport(obj_name, obj_data):
    if obj_name == "Teleport_Hostel_Street":
        if cloth_type == "Nude":
            call change_scene("hostel_street", "Fade", "snd_walk_barefoot")
            return
        call change_scene("hostel_street", "Fade", "highheels_run2")
        return
    if obj_name == "Teleport_Walk_Street":
        if gameStage == 3 and gameSubStage == 0:
            mt "Там люди! Я не могу бежать туда голой! Посреди белого дня!"
            "Да неважно! Дня, ночи! Я голая! Ужас!!!"
            return
        if hostelWalkStreetEnabled == False:
            mt "Там улица, мне там нечего делать!"
            return
        return
    if obj_name == "Teleport_Hostel_1_a":
        if act == "l":
            if gameStage == 3 and gameSubStage == 0:
                mt "Этот двор, тупик."
                "Он какой-то жуткий..."
                "Но здесь я могу одеться!"
                return

            if hostelStreetStage == 0:
                mt "Этот двор, тупик."
                "Он какой-то жуткий..."
                return
        if act == "w":
            if gameStage == 3 and gameSubStage == 0:
                call hostelAfterJail_street_dialogue4()
                return
            if gameStage == 2:
                $ autorun_to_object("hostel_edge_1_a", "hostel_edge_1_a_dialogue1")
            if cloth_type == "Nude":
                call change_scene("hostel_edge_1_a", "Fade", "snd_walk_barefoot")
                return
            call change_scene("hostel_edge_1_a")
            return
    return
label hostel_edge_1_c_environment(obj_name, obj_data):
    if obj_name == "Monica":
        if gameStage == 3 and gameSubStage == 0:
            call hostelAfterJail_street_dialogue0()
            return
        if gameStage == 3 and gameSubStage == 1:
            call hostelAfterJail_street_dialogue3()
            return
        if hostelStreetStage == 0:
            mt "Мне холодно и мокро."
            "Надо найти где укрыться."
            "И это явно не здесь!"

    return
