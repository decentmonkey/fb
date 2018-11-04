default catchSteveInProgress = True

label street_steve_office:

    $ print "enter_street_steve_office"
    $ miniMapData = []

    $ scene_name = "street_steve_office"
    $ sceneIsStreet = True
    $ scene_caption = _("STEVE'S OFFICE")
    $ clear_scene_from_objects(scene_name)
    if bFredFollowingMonica == True:
        $ scene_image = "scene_Street_Steve_Office_Driver" + day_suffix
        $ add_object_to_scene("Car", {"type":2, "base":"Street_Steve_Office_Car", "click" : "street_house_main_yard_environment", "actions" : "l", "zorder" : 3})
        $ add_object_to_scene("Driver", {"type":2, "base":"Street_Steve_Office_Driver", "click" : "street_steve_office_environment", "actions" : "lt", "zorder" : 5, "icon_t":"/Icons/talk" + res.suffix +".png", "b":0.2, "s":1.3, "tint":[1.0, 1.0, 0.8]})
    else:
        $ scene_image = "scene_Street_Steve_Office" + day_suffix

    $ add_object_to_scene("Teleport_Building", {"type":2, "base":"Street_Steve_Office_Building", "click" : "street_steve_office_teleport", "actions" : "lw", "zorder" : 1, "b":0.05})
#    $ add_object_to_scene("Monica", {"type":2, "base":"Bank_Street_Driver_Monica_" + cloth + day_suffix, "click" : "street_bank_environment", "actions" : "l", "zorder" : 10})
#    $ add_object_to_scene("Teleport_Street", {"type":3, "text" : _("НАЗАД НА УЛИЦУ"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "street_steve_office_teleport", "xpos" : 960, "ypos" : 956, "zorder":15})
    return

#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label street_steve_office_teleport(obj_name, obj_data):
    if obj_name == "Teleport_Building":
        if obj_data["action"] == "l":
            m "Неплохо устроился Стив!"
            "НА МОИ ДЕНЬГИ!!!"
        if obj_data["action"] == "w":
            if day_time == "evening":
                mt "Уже вечер. Офис Стива закрыт."
                return
            if gameStage >= 2:
                mt "Стив урод."
                "Я разберусь с ним позже."
                "Сейчас мне не до того..."
                return
            call change_scene("steve_office_secretary", "Fade_long", "snd_lift")
            return
    return
label street_steve_office_environment(obj_name, obj_data):
    if obj_name == "Driver":
        if obj_data["action"] == "l":
            call monica_looking_to_fred1()
            return
        if obj_data["action"] == "t":
            if catchSteveInProgress == True:
                mt "Куда я поеду???"
                "Мне надо добраться до Стива!"
                return
            call get_to_drive_dialogue()
            return
    return
