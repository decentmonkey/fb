default map_source_scene = ""
default map_source_scene_hud_preset = ""
default map_scene = "House"
default target_map_scene = ""
default movingByCar = True
default visitedPlaces = {}
default mapFocusedObjects = []
default mapChangedFlag = True
default map_hud_preset_current = "map"
default mapStreetCheckShowing = False

default mapSubstMonicaOfficeToSteve = False
default mapSubstClothingShopToStreetCorner = False
default mapSubstMonicaOfficeToPolice = False
default teleportDickOfficeEveningFlag = False
default teleportDickOfficeHeavyRainFlag = False
default teleportHomeFredBlowjobFlag = False

init python:
    def checkMapVisited(scene_name):
        if visitedPlaces.has_key(scene_name):
            return True
        return False

label map_street_scene_visibility_check: #проверка того надо-ли показывать значок вызова карты в локациях не улица
    if gameStage < 2:
        if sceneIsStreet == True:
            $ mapStreetCheckShowing = True
            return
        if scene_name == "bedroom1" or scene_name == "bedroom2":
            $ mapStreetCheckShowing = True
            return
        $ mapStreetCheckShowing = False
        return
    if gameStage >=2:
        if sceneIsStreet == True:
            $ mapStreetCheckShowing = True
            return
        $ mapStreetCheckShowing = False
    return

label map_show(car=False):
    $ miniMapData = []
    $ print "checkDialogueExists"
    $ print checkDialogueExists()
    if checkDialogueExists() == True:
        return
    $ movingByCar = car
    call define_autorun() from _call_define_autorun_1

    $ map_source_scene = scene_name
    if hud_preset_current != map_hud_preset_current:
        $ map_source_scene_hud_preset = hud_preset_current
    $ hud_preset_current = map_hud_preset_current
    call change_scene("map", "Fade", "open_map") from _call_change_scene_22
    $ scene_refresh_flag = True
    $ show_scene_loop_flag = True
    return

label map_close:
    $ hud_preset_current = map_source_scene_hud_preset
    call change_scene(map_source_scene, "Fade", "open_map") from _call_change_scene_29
    return

label map:
    $ scene_name = "map"
    $ scene_caption = ""
    $ clear_scene_from_objects(scene_name)
    $ scene_image = "scene_Map" + day_suffix

    call define_hudpresets() from _call_define_hudpresets_1

    if hud_presets[hud_preset_current]["display_closemap"] == True:
        $ add_object_to_scene("Close", {"type" : 2, "img_overlay": "map_close" + res.suffix, "base":"map_close_hover" + res.suffix, "click" : "map_environment", "actions" : "l", "zorder":10, "xsprite":1839, "ysprite":17})

    python:
        for key, val in map_objects.items():
            stateSuffix = {
                "invisible": False,
                "visible" : "",
                "active" : "_active",
                "disabled" : "_disabled",
            }
            if stateSuffix[val["state"]] != False:
                add_object_to_scene(key, {"type":3, "text" : val["text"], "xpos" : val["xpos"], "ypos" : (val["ypos"] - 95), "xsprite":val["xpos"], "ysprite":val["ypos"], "img_overlay": val["base"] + stateSuffix[val["state"]] + res.suffix, "base":val["base"] + stateSuffix[val["state"]] + "_hover" + res.suffix, "click" : "map_environment", "sprite_align":"dc", "high_sprite_hover": True, "layout" : "map" + stateSuffix[val["state"]]})

#    $ add_object_to_scene("Teleport_Office", {"type":3, "text" : _("ОФИС МОНИКИ"), "xpos" : 921, "ypos" : 337, "xsprite":921, "ysprite":432, "img_overlay": "map_marker" + res.suffix, "base":"map_marker_hover" + res.suffix, "click" : "map_environment", "sprite_align":"dc", "high_sprite_hover": True, "layout" : "map"})
#    $ add_object_to_scene("Teleport_Office", {"type":3, "text" : _("ОФИС МОНИКИ"), "xpos" : 921, "ypos" : 337, "xsprite":921, "ysprite":432, "img_overlay": "map_marker_disabled" + res.suffix, "base":"map_marker_disabled_hover" + res.suffix, "click" : "map_environment", "sprite_align":"dc", "high_sprite_hover": True, "layout" : "map_disabled"})
#    $ add_object_to_scene("Teleport_Office", {"type":3, "text" : _("ОФИС МОНИКИ"), "xpos" : 921, "ypos" : 337, "xsprite":921, "ysprite":432, "img_overlay": "map_marker_active" + res.suffix, "base":"map_marker_active_hover" + res.suffix, "click" : "map_environment", "sprite_align":"dc", "high_sprite_hover": True, "layout" : "map_active"})

    return


label map_environment(obj_name, obj_data):
    if obj_name == "Close":
        call map_close() from _call_map_close
        return
    if obj_name == "Teleport_" + map_scene:
        call map_close() from _call_map_close_1
        return
    if movingByCar == False and bFredFollowingMonica == True:
        m "Я что, ненормальная идти пешком по дороге?"
        if day_time == "evening":
            m "Тем более в такую темень!!"
        "У меня есть водитель!"
        "Пусть он и везет!"
        return

    if obj_name == "Teleport_House":
        if teleportHomeFredBlowjobFlag == True:
            call afterJailFredDialogue3()
            call process_drive_teleport("House", "street_house_main_yard")
            return
        if gameStage == 2 or gameStage == 3:
            call process_drive_teleport("House", "street_house_outside")
            return
        call process_drive_teleport("House", "street_house_main_yard")
        return
    if obj_name == "Teleport_Monica_Office":
        if mapSubstMonicaOfficeToPolice == True:
            $ obj_name = "Teleport_Police"
            $ map_objects["Teleport_Police"]["state"] = "visible"
            $ mapSubstMonicaOfficeToPolice = False
        else:
            if mapSubstMonicaOfficeToSteve == False:
                call process_drive_teleport("Monica_Office", "street_monica_office") from _call_process_drive_teleport_1
                return
            else:
                $ obj_name = "Teleport_Steve_Office"
                $ mapSubstMonicaOfficeToSteve = False
    if obj_name == "Teleport_Gas_Station":
        call process_drive_teleport("Gas_Station", "street_gas_station") from _call_process_drive_teleport_2
        return
    if obj_name == "Teleport_Dick_Office":
        if teleportDickOfficeHeavyRainFlag == True:
            $ teleportDickOfficeHeavyRainFlag = False
            $ rainIntencity = 3
        if teleportDickOfficeEveningFlag == True and mapChangedFlag == True:
            $ teleportDickOfficeEveningFlag = False
            $ changeDayTime("evening")

        call process_drive_teleport("Dick_Office", "street_dick_office") from _call_process_drive_teleport_3
        return
    if obj_name == "Teleport_Cloth_Shop":
        if mapSubstClothingShopToStreetCorner == False:
            call process_drive_teleport("Cloth_Shop", "street_cloth_shop")
            return
        else:
            $ obj_name = "Teleport_Street_Corner"
            $ map_objects["Teleport_Street_Corner"]["state"] = "visible"
            $ mapSubstClothingShopToStreetCorner = False
    if obj_name == "Teleport_Rich_Hotel":
        call process_drive_teleport("Rich_Hotel", "street_rich_hotel")
        return
    if obj_name == "Teleport_Fitness":
        call process_drive_teleport("Fitness", "street_fitness")
        return
    if obj_name == "Teleport_Bank":
        call process_drive_teleport("Bank", "street_bank")
        return
    if obj_name == "Teleport_Steve_Office":
        call process_drive_teleport("Steve_Office", "street_steve_office")
        return
    if obj_name == "Teleport_Street_Corner":
        call process_drive_teleport("Street_Corner", "street_corner")
        return
    if obj_name == "Teleport_Police":
        call process_drive_teleport("Police", "street_police")
        return
    m "drive!"
    return


label process_drive_teleport(in_target_map_scene, in_target_scene):
    $ target_map_scene = in_target_map_scene
    $ target_scene = in_target_scene
    python:
        for item1 in map_objects:
            if map_objects[item1]["state"] == "active":
                map_objects[item1]["state"] = "visible"
#    $ map_objects["Teleport_" + map_scene]["state"] = "visible"
    $ map_objects["Teleport_" + target_map_scene]["state"] = "active"
    $ map_scene = target_map_scene
    $ hud_preset_current = map_source_scene_hud_preset
    if bFredFollowingMonica == True:
        call start_drive() from _call_start_drive
        if driveCanceled == True:
            return
    else:
        $ mapChangedFlag = True
        call start_walk_direct()
    $ mapChangedFlag = True
    return

label process_drive_teleport_direct(in_target_map_scene, in_target_scene):
    $ target_map_scene = in_target_map_scene
    $ target_scene = in_target_scene
    python:
        for item1 in map_objects:
            if map_objects[item1]["state"] == "active":
                map_objects[item1]["state"] = "visible"
#    $ map_objects["Teleport_" + map_scene]["state"] = "visible"
    $ map_objects["Teleport_" + target_map_scene]["state"] = "active"
    $ hud_preset_current = map_source_scene_hud_preset
    call start_drive_direct() from _call_start_drive_direct
    if driveCanceled == True:
        return
    $ visitedPlaces[target_map_scene] = True
    $ mapChangedFlag = True
    return
label process_change_map_location(target_map_scene):
    $ map_objects["Teleport_" + map_scene]["state"] = "visible"
    $ map_objects["Teleport_" + target_map_scene]["state"] = "active"
    $ map_scene = target_map_scene
    $ mapChangedFlag = True
    return
