label street_corner:
    $ print "enter_street_corner"
    $ miniMapData = []

    $ scene_name = "street_corner"
    $ sceneIsStreet = True
    $ scene_caption = _("Street Edge")
    $ clear_scene_from_objects(scene_name)
    if bFredFollowingMonica == True and map_scene == "Street_Corner":
        $ scene_image = "scene_street_Whores_Place_Car_Stop_Monica_Driver_" + cloth + day_suffix
        $ add_object_to_scene("Driver", {"type":2, "base":"Street_Whores_Place_Car_Stop_Driver", "click" : "street_corner_environment", "actions" : "lt", "zorder" : 0, "icon_t":"/Icons/talk" + res.suffix +".png" , "b":0.2, "s":1.3, "tint":[1.0, 1.0, 0.8]})
        $ add_object_to_scene("Car", {"type":2, "base":"Street_Whores_Place_Car_Stop_Car", "click" : "street_house_main_yard_environment", "actions" : "l", "zorder" : 0, "b":0.1, "tint":[1.0, 1.0, 0.9]})
        $ add_object_to_scene("Monica", {"type":2, "base":"Street_Whores_Place_Car_Stop_Monica_Driver_" + cloth + day_suffix, "click" : "street_corner_environment", "actions" : "l", "zorder" : 10})
    else:
        $ scene_image = "scene_street_Whores_Place_Car_Stop_Monica_" + cloth + day_suffix
        $ add_object_to_scene("Monica", {"type":2, "base":"Street_Whores_Place_Car_Stop_Monica_" + cloth + day_suffix, "click" : "street_corner_environment", "actions" : "l", "zorder" : 10})



    $ add_object_to_scene("Teleport_Street1", {"type":3, "text" : _("ВНИЗ ПО УЛИЦЕ"), "larrow" : "arrow_left_2", "base":"Street_Whores_Place_Car_Stop_Teleport_Street1", "click" : "street_corner_teleport", "xpos" : 200, "ypos" : 644, "zorder":15})
    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label street_corner_teleport(obj_name, obj_data):
    if obj_name == "Teleport_Street1":
        call change_scene("whores_place_street1", "Fade_long", "highheels_run2")
        return
    return
label street_corner_environment(obj_name, obj_data):
    if obj_name == "Driver":
        if obj_data["action"] == "l":
            call monica_looking_to_fred1()
            return
        if obj_data["action"] == "t":
            if returnDressInProgress == True:
                mt "Я никуда не поеду пока не верну это платье! Из принципа!"
                return
            call get_to_drive_dialogue()
            return
    if obj_name == "Monica":
        if gameStage ==2 or gameStage == 3:
            mt "Что за грязное место?"
            "Мне противно находиться здесь!"
            return
        mt "Что за грязное место?"
        "Фред специально нарывается?"
        "Мне противно находиться здесь!"

    return
