label hostel_bathroom_toilet:
    $ print "enter_hostel_bathroom_toilet"
    $ miniMapData = []

    $ scene_name = "hostel_bathroom_toilet"
    $ scene_caption = _("HOSTEL BATHROOM")
    $ clear_scene_from_objects(scene_name)

    $ scene_image = "scene_hostel_bathroom_toilet_Monica_Nude" + day_suffix
    $ add_object_to_scene("Monica", {"type":2, "base":"hostel_bathroom_toilet_Monica_Nude" + day_suffix, "click" : "hostel_bathroom_toilet_environment", "actions" : "l", "zorder" : 10})

    $ add_object_to_scene("Toilet", {"type":2, "base":"Hostel_Bathroom_Toilet_Toilet", "click" : "hostel_bathroom_toilet_environment", "actions" : "lh", "zorder" : 0, "b":0.13})

    $ add_object_to_scene("Teleport_Hostel_Bathroom", {"type":3, "text" : _("НАЗАД"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "hostel_bathroom_toilet_teleport", "xpos" : 960, "ypos" : 956, "zorder":11})

    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label hostel_bathroom_toilet_teleport(obj_name, obj_data):
    if obj_name == "Teleport_Hostel_Bathroom":
        call change_scene("hostel_bathroom", "Fade", "snd_walk_barefoot")
        return

    return
label hostel_bathroom_toilet_environment(obj_name, obj_data):
    if obj_name == "Monica":
        mt "(хмык)"
        return
    if obj_name == "Toilet":
        if act == "l":
            mt "Жуткий унитаз."
            "Я боюсь прикасаться к нему..."
            if hostelBathroomPissed == False:
                "Или, может быть, все-же пописать?"
                "Я уже давно хочу писать..."
                "Еще этот дождь снаружи..."
        if act == "h":
            if hostelBathroomPissed == True:
                mt "Я уже писала только что..."
                return
            if hostelBathroomStage == 0:
                stop music fadeout 0.2
                sound snd_piss
                img 5631
                with fadelong
                w
                music snd_moderate_rain_music2
                call refresh_scene_fade()
                $ hostelBathroomPissed = True
                return
            if hostelBathroomStage == 1:
                stop music fadeout 0.2
                sound snd_piss
                img 5632
                with fadelong
                w
                music Cheery_Monday
                call refresh_scene_fade()
                $ hostelBathroomPissed = True
                return

            return

    return
