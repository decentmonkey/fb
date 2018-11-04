default driverOnHouseYard = True
default houseStreetFenceLocationOpened = False
default neighborAsked = False
default driverMode = 0

default streetHouseMainYardStage = 0

label street_house_main_yard:
    $ print "enter_street_house_main_yard"
    $ miniMapData = []
    call miniMapHouseGenerate()

    $ scene_name = "street_house_main_yard"
    $ sceneIsStreet = True
    $ scene_caption = _("House Yard")
    $ clear_scene_from_objects(scene_name)

    if streetHouseMainYardStage == 0:
        $ scene_image = "scene_Street_House_Monica_" + cloth + day_suffix
        $ add_object_to_scene("Monica", {"type" : 2, "base" : "Street_House_Monica_" + cloth + day_suffix, "click" : "street_house_main_yard_environment", "actions" : "l", "zorder":10, "tint": monica_tint})
        if driverOnHouseYard == True:
            $ add_object_to_scene("Car", {"type" : 2, "base" : "Street_House_Car", "click" : "street_house_main_yard_environment", "actions" : "l", "zorder":0, "b":0.15})
            $ add_object_to_scene("Driver", {"type" : 2, "base" : "Street_House_Driver" + day_suffix, "click" : "street_house_main_yard_environment", "actions" : "lt", "zorder":10, "b":0.15, "icon_t":"/Icons/talk" + res.suffix +".png"})
        else:
            $ add_object_to_scene("Car", {"type" : 2, "base" : "Street_House_Car", "click" : "street_house_main_yard_environment", "actions" : "l", "zorder":0, "b":0.15})

        $ add_object_to_scene("Teleport_House", {"type":3, "text" : _("В ДОМ"), "rarrow" : "arrow_up_2", "base":"Street_House_Teleport_House", "click" : "street_house_main_yard_teleport", "xpos" : 1683, "ypos" : 858, "zorder":11, "b":-0.05, "tint":[1.0, 1.0, 0.85]})

    if streetHouseMainYardStage == 1:
        $ scene_image = "scene_Street_House_Driver_Family_Monica_Whore"
        $ add_object_to_scene("Monica", {"type" : 2, "base" : "Street_House_Driver_Family_Monica_Whore_Monica", "click" : "street_house_main_yard_environment", "actions" : "l", "zorder":10, "tint": monica_tint})
        $ add_object_to_scene("Car", {"type" : 2, "base" : "Street_House_Car", "click" : "street_house_main_yard_environment", "actions" : "l", "zorder":0, "b":0.15})
        $ add_object_to_scene("Driver", {"type" : 2, "base" : "Street_House_Driver_Family_Monica_Whore_Driver", "click" : "street_house_main_yard_environment", "actions" : "lt", "zorder":10, "b":0.15, "icon_t":"/Icons/talk" + res.suffix +".png"})
        $ add_object_to_scene("Family", {"type" : 2, "base" : "Street_House_Driver_Family_Monica_Whore_Family", "click" : "street_house_main_yard_environment", "actions" : "lw", "zorder":10, "tint": monica_tint})

    if streetHouseMainYardStage == 2:
        $ scene_image = "scene_Street_House_Monica_" + cloth + day_suffix
        $ add_object_to_scene("Monica", {"type" : 2, "base" : "Street_House_Monica_" + cloth + day_suffix, "click" : "street_house_main_yard_environment", "actions" : "l", "zorder":10, "tint": monica_tint})
        $ add_object_to_scene("Car", {"type" : 2, "base" : "Street_House_Car", "click" : "street_house_main_yard_environment", "actions" : "l", "zorder":0, "b":0.15})
        $ add_object_to_scene("Driver", {"type" : 2, "base" : "Street_House_Driver" + day_suffix, "click" : "street_house_main_yard_environment", "actions" : "lt", "zorder":10, "b":0.15, "icon_t":"/Icons/talk" + res.suffix +".png"})
        $ add_object_to_scene("Teleport_House", {"type":3, "text" : _("В ДОМ"), "rarrow" : "arrow_up_2", "base":"Street_House_Teleport_House", "click" : "street_house_main_yard_teleport", "xpos" : 1683, "ypos" : 858, "zorder":11, "b":-0.05, "tint":[1.0, 1.0, 0.85]})

    if bardieLocation == "Street_Yard":
        $ add_object_to_scene("Bardie", {"type" : 2, "base" : "Street_House_Bardie" + day_suffix, "click" : "bardieInteract1", "actions" : "lt", "zorder":10, "icon_t":"/Icons/talk" + res.suffix +".png"})


    if houseStreetFenceLocationOpened == True:
        $ add_object_to_scene("Teleport_Fence", {"type":3, "text" : _("К ЗАБОРУ"), "larrow" : "arrow_left_2", "base":"Street_House_Teleport_Fence", "click" : "street_house_main_yard_teleport", "xpos" : 758, "ypos" : 154, "zorder":11, "b":0.15, "tint":[1.0, 1.0, 0.9]})

    $ add_object_to_scene("Teleport_Gate", {"type":3, "text" : _("К ВОРОТАМ"), "larrow" : "arrow_left_2", "base":"Street_House_Teleport_Gate", "click" : "street_house_main_yard_teleport", "xpos" : 433, "ypos" : 660, "zorder":11, "b":0.15, "tint":[1.0, 1.0, 0.85]})


    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label street_house_main_yard_teleport(obj_name, obj_data):
    if obj_name == "Teleport_Fence":
        call change_scene("street_house_fence", "Fade", "highheels_run2") from _call_change_scene_47
        return
    if obj_name == "Teleport_Gate":
        call change_scene("street_house_gate", "Fade", "highheels_run2") from _call_change_scene_48
        return
    if obj_name == "Teleport_House":
        music casualMusic
        call change_scene("floor1", "Fade_long", "highheels_run2") from _call_change_scene_49
        return
    return
label street_house_main_yard_environment(obj_name, obj_data):
    if obj_name == "Car":
        if gameStage > 2:
            mt "Моя бывшая машина..."
            "Но я верну все назад, клянусь!"
            "Я устроим им всем АД!!!"
            return
        call look_at_car(0) from _call_look_at_car_1
        return
    if obj_name == "Driver":
        if obj_data["action"] == "l":
            if gameStage > 2:
                mt "Фред... Мой бывший водитель..."
                "Редкий ублюдок..."
                "Он не избежит своей участи!"
                return
            call monica_looking_to_fred1() from _call_monica_looking_to_fred1
            return
        if obj_data["action"] == "t":
            if streetHouseMainYardStage == 2:
                call afterJailHouseFamily_dialogue2a()
                return
            if streetHouseMainYardStage == 1:
                call afterJailHouseFamily_dialogue2()
                return
            if driverMode == 1:
                call monica_fred_day1_evening_dialogue2()
                return
            if driverMode == 2:
                call monica_fred_day2_morning_dialogue1()
                return
            if neighborAsked == False:
                $ neighborAsked = True
                call neighbor_quest1() from _call_neighbor_quest1
                $ scene_transition = "Fade_long"
                music casualMusic
                call refresh_scene() from _call_refresh_scene_22
                return
            else:
                call get_to_drive_dialogue() from _call_get_to_drive_dialogue_2
                return
    if obj_name == "Monica":
        if streetHouseMainYardStage == 1 or streetHouseMainYardStage == 2:
            mt "(хмык)"
            return
        m "Мой уютный дворик."
        "За домом есть бассейн, где я люблю расслабляться.
        Но сейчас нет на это времени."
        if day_time == "evening":
            m "Но сейчас уже слишком темно."

    if obj_name == "Family":
        if act == "l":
            if streetHouseMainYardStage == 1:
                mt "Мне надо подойти к ним..."
                "Мне надо где-то ночевать!!!"
        if act == "w":
            if streetHouseMainYardStage == 1:
                call afterJailHouseFamily_dialogue3()
                return
    return

















#
