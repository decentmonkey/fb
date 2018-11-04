default gasStationBuildingComment1 = True
default gasStationFindingFuelQuest = False
default gasStationFindingFuelQuestStage = 0

label street_gas_station:
    $ print "enter_street_gas_station"
    $ miniMapData = []

    $ scene_name = "street_gas_station"
    $ sceneIsStreet = True
    $ scene_caption = _("Gas Station")
    $ clear_scene_from_objects(scene_name)


    if bFredFollowingMonica == True:
        $ scene_image = "scene_Street_Gas_Station_Driver_Monica_" + cloth + day_suffix
        $ add_object_to_scene("Driver", {"type":2, "base":"Street_Gas_Station_Driver", "click" : "street_gas_station_environment", "actions" : "lt", "zorder" : 5, "icon_t":"/Icons/talk" + res.suffix +".png", "b":0.2, "s":1.3, "tint":[1.0, 1.0, 0.8]})
        $ add_object_to_scene("Car", {"type":2, "base":"Street_Gas_Station_Car", "click" : "street_gas_station_environment", "actions" : "l", "zorder" : 0})
        $ add_object_to_scene("Monica", {"type":2, "base":"Street_Gas_Station_Driver_Monica_" + cloth + day_suffix, "click" : "street_gas_station_environment", "actions" : "l", "zorder" : 10})
    else:
        $ scene_image = "scene_Street_Gas_Station_Monica_" + cloth + day_suffix
        $ add_object_to_scene("Monica", {"type":2, "base":"Street_Gas_Station_Monica_" + cloth + day_suffix, "click" : "street_gas_station_environment", "actions" : "l", "zorder" : 15})

    $ add_object_to_scene("Fuel1", {"type":2, "base":"Street_Gas_Station_Fuel1", "click" : "street_gas_station_environment", "actions" : "l", "zorder" : 0})
    $ add_object_to_scene("Fuel2", {"type":2, "base":"Street_Gas_Station_Fuel2", "click" : "street_gas_station_environment", "actions" : "l", "zorder" : 0})
    $ add_object_to_scene("Logo", {"type":2, "base":"Street_Gas_Station_Logo", "click" : "street_gas_station_environment", "actions" : "l", "zorder" : 0})
    $ add_object_to_scene("Station_Building", {"type":2, "base":"Street_Gas_Station_Station_Building", "click" : "street_gas_station_environment", "actions" : "l", "zorder" : 0})
    $ add_object_to_scene("Teleport_Inside", {"type":2, "base":"Street_Gas_Station_Teleport_Inside", "click" : "street_gas_station_teleport", "actions" : "lw", "zorder" : 1})
    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label street_gas_station_teleport(obj_name, obj_data):
    if obj_name == "Teleport_Inside":
        if obj_data["action"] == "l":
            m "Вход в здание заправки..."
        if obj_data["action"] == "w":
            call change_scene("gas_station_view1") from _call_change_scene_82
            return
    return
label street_gas_station_environment(obj_name, obj_data):
    if obj_name == "Monica":
        if gasStationFindingFuelQuest == False:
            m "Дурацкая заправка.
            На которой работает никчемный продавец!"
            "Я помню!"
            return
        m "Я застряла на этой дурацкой заправке."
        if fredOffendedRefuel2 == True:
            m "И все потому что этот тупица Фред не может позаботиться о бензине!"
            "Он плохо работает!"
        else:
            m "Фред пытался, но не смог залить бензин.
            Думаю я должна справиться сама!
            Уверена что справлюсь!"

    if obj_name == "Fuel1" or obj_name == "Fuel2":
        m "Пистолеты для заправки бензина.
        От них такой неприятный запах!"
        "В любом случае, я не собираюсь к ним приближаться ближе чем сейчас."
        "И я не собираюсь сама заправлять машину, у меня маникюр!!!"
    if obj_name == "Logo":
        m "Модная запрака?"
        "Хи-хи."
    if obj_name == "Station_Building":
        m "Здание заправки.
        Здесь должнен быть где-то вход..."

    if obj_name == "Car":
        call look_at_car(0) from _call_look_at_car_2
        return

    if obj_name == "Driver":
        if gasStationFindingFuelQuest == True:
            if obj_data["action"] == "l":
#                if gasStationFindingFuelQuestStage == 0:
                if fredOffendedRefuel2 == True:
                    m "Этот тупица не может даже залить бензин!"
                else:
                    m "У Фреда не получилось залить бензин.
                    Попробую решить этот вопрос сама."
                return

            if obj_data["action"] == "t":
                if gasStationFindingFuelQuestStage == 0:
                    fred "Мэм, бензина пока так и нет."
                    if fredOffendedRefuel2 == True:
                        m "Я знаю, заткнись!"
                    else:
                        m "Я знаю, Фред."
                    return
                if gasStationFindingFuelQuestStage == 1:
                    if fredOffendedRefuel2 == True:
                        m "Фред! Ты идиот?
                        Там нет кассира!"
                    else:
                        m "Там нет кассира, Фрэд."

                    fred "Там была девушка кассир, Мэм."
                    "Может быть она отошла?
                    Может быть чем-то надо привлечь ее внимание?"
                    return
                if gasStationFindingFuelQuestStage == 3:
                    imgr Driver_Stand
                    fred "Мэм, я удивился, но из пистолета пошел бензин!"

                    "Я заправил полный бак."

                    if gasStationSaleswomanMischiefed == True and gasStationMonicaLied == True:
                        imgl Monica_BusinessCloth1_Gloat2
                        m "Знаешь что, Фрэд."

                        "Я была злая на тебя, но мне здесь очень подняли настроение."

                        "Так что я даже не ругаюсь на тебя."

                        fred "Хорошо, Мэм!"

                        "Спасибо!"

                        "Мы можем ехать?"
                    else:
                        "Мы можем ехать!"
                    $ remove_objective("fuel_car")
                    $ gasStationQuestCompletedJust = False
                    $ map_enabled = True
                    $ gasStationFindingFuelQuest = False
                    $ dickRefuelPlanned = True
                    $ map_objects["Teleport_House"]["state"] = "visible"
                    $ subst_to_object("Teleport_House", False)
                    $ map_objects["Teleport_Dick_Office"]["state"] = "visible"
                    $ subst_to_object("Teleport_Dick_Office", False)
                    $ map_objects["Teleport_Monica_Office"]["state"] = "visible"
                    $ subst_to_object("Teleport_Monica_Office", False)
                    $ map_scene = "Gas_Station"
                    $ hud_preset_current = "default"
                    $ scene_transition = "Fade"
                    call refresh_scene() from _call_refresh_scene_23
                return

        if obj_data["action"] == "l":
            call monica_looking_to_fred1() from _call_monica_looking_to_fred1_2
            return
        if obj_data["action"] == "t":
            call get_to_drive_dialogue() from _call_get_to_drive_dialogue_4
            return


    return
