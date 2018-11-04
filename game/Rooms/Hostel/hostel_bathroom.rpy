default hostelBathTaken = False
default hostelBathroomPissed = False
default hostelBathroomStage = 0
label hostel_bathroom:
    $ print "enter_hostel_bathroom"
    $ miniMapData = []

    $ scene_name = "hostel_bathroom"
    $ scene_caption = _("HOSTEL BATHROOM")
    $ clear_scene_from_objects(scene_name)

    $ scene_image = "scene_Hostel_Bathroom_Monica_Nude" + day_suffix
    $ add_object_to_scene("Monica", {"type":2, "base":"Hostel_Bathroom_Monica_Nude" + day_suffix, "click" : "hostel_bathroom_environment", "actions" : "l", "zorder" : 10})

    if day_time == "evening":
        $ add_object_to_scene("Bottle", {"type":2, "base":"Hostel_Bathroom_Bottle", "click" : "hostel_bathroom_environment", "actions" : "l", "zorder" : 0, "b":0.13})
        $ add_object_to_scene("Shower", {"type":2, "base":"Hostel_Bathroom_Shower", "click" : "hostel_bathroom_environment", "actions" : "lh", "zorder" : 0, "b":0.13})
        $ add_object_to_scene("Toilet", {"type":2, "base":"Hostel_Bathroom_Toilet_Object", "click" : "hostel_bathroom_environment", "actions" : "lw", "zorder" : 0, "b":0.13})
        $ add_object_to_scene("Window", {"type":2, "base":"Hostel_Bathroom_Window", "click" : "hostel_bathroom_environment", "actions" : "l", "zorder" : 0, "b":0.13})
    else:
        $ add_object_to_scene("Bottle", {"type":2, "base":"Hostel_Bathroom_Bottle", "click" : "hostel_bathroom_environment", "actions" : "l", "zorder" : 0})
        $ add_object_to_scene("Shower", {"type":2, "base":"Hostel_Bathroom_Shower", "click" : "hostel_bathroom_environment", "actions" : "lh", "zorder" : 0})
        $ add_object_to_scene("Toilet", {"type":2, "base":"Hostel_Bathroom_Toilet_Object", "click" : "hostel_bathroom_environment", "actions" : "lw", "zorder" : 0})
        $ add_object_to_scene("Window", {"type":2, "base":"Hostel_Bathroom_Window", "click" : "hostel_bathroom_environment", "actions" : "l", "zorder" : 0})

    $ add_object_to_scene("Teleport_Hostel_Bedroom", {"type":3, "text" : _("ОБЩАЯ СПАЛЬНЯ"), "rarrow" : "arrow_right_2", "base":"Hostel_Bathroom_Teleport_Hostel_Bedroom", "click" : "hostel_bathroom_teleport", "xpos" : 520, "ypos" : 240, "zorder":0})

    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label hostel_bathroom_teleport(obj_name, obj_data):
    if obj_name == "Teleport_Hostel_Bedroom":
        if hostelBedroomStage == 0:
            music snd_moderate_rain_music
        call change_scene("hostel_bedroom", "Fade", "snd_walk_barefoot")
        return

    return
label hostel_bathroom_environment(obj_name, obj_data):
    if obj_name == "Monica":
        mt "Какое жуткое место!"
        return

    if obj_name == "Bottle":
        mt "Какая-то пустая емкость."
        "Наивно было бы рассчитывать на моющие принадлежности в таком месте..."
        "Я привыкла использовать около сотни различных гигиенических средств!"
    if obj_name == "Window":
        mt "Здесь такие открытые окна..."
        "Надеюсь меня не будет видно с улицы?"
    if obj_name == "Toilet":
        if act == "l":
            mt "Жуткий унитаз."
        if act == "w":
            call change_scene("hostel_bathroom_toilet", "Fade", "snd_walk_barefoot")
            return

    if obj_name == "Shower":
        if act == "l":
            mt "А вот и душ."
        if act == "h":
            call hostelAfterJail_bathroom_dialogue2()
            return
    return
