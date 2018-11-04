label street_gas_station_s2:
    $ print "enter_street_gas_station"
    $ miniMapData = []

    $ scene_name = "street_gas_station_s2"
    $ sceneIsStreet = True
    $ scene_caption = _("Gas Station")
    $ clear_scene_from_objects(scene_name)


    if cloth_type == "Whore":
        $ scene_image = "scene_Street_Gas_Station_Monica_AfterJail" + day_suffix
    else:
        $ scene_image = "scene_Street_Gas_Station_Monica_" + cloth + day_suffix
    $ add_object_to_scene("Monica", {"type":2, "base":"Street_Gas_Station_Monica_" + cloth + day_suffix, "click" : "street_gas_station2_environment", "actions" : "l", "zorder" : 15})

    $ add_object_to_scene("Fuel1", {"type":2, "base":"Street_Gas_Station_Fuel1", "click" : "street_gas_station2_environment", "actions" : "l", "zorder" : 0})
    $ add_object_to_scene("Fuel2", {"type":2, "base":"Street_Gas_Station_Fuel2", "click" : "street_gas_station2_environment", "actions" : "l", "zorder" : 0})
    $ add_object_to_scene("Logo", {"type":2, "base":"Street_Gas_Station_Logo", "click" : "street_gas_station2_environment", "actions" : "l", "zorder" : 0})
    $ add_object_to_scene("Station_Building", {"type":2, "base":"Street_Gas_Station_Station_Building", "click" : "street_gas_station2_environment", "actions" : "l", "zorder" : 0})
    $ add_object_to_scene("Teleport_Inside", {"type":2, "base":"street_gas_station_teleport_Inside", "click" : "street_gas_station2_teleport", "actions" : "lw", "zorder" : 1})
    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label street_gas_station2_teleport(obj_name, obj_data):
    if obj_name == "Teleport_Inside":
        if obj_data["action"] == "l":
            m "Вход в здание заправки..."
        if obj_data["action"] == "w":
            call change_scene("gas_station_view1")
            return
    return
label street_gas_station2_environment(obj_name, obj_data):
    if obj_name == "Monica":
        if gameStage == 2:
            if gameSubStage == 1:
                mt "Что я здесь делаю? Мне надо к Дику!"
                return
            mt "Мне надо где-то переночевать. Не думаю что заправка - то место что я ищу..."
            return
        if gameStage == 3 and gameSubStage == 2:
            mt "Что я здесь делаю? Мне надо к Дику!"
            return

    if obj_name == "Fuel1" or obj_name == "Fuel2":
        m "Пистолеты для заправки бензина."
        "Мне они сейчас ни к чему!"
    if obj_name == "Logo":
        m "Модная запрака?"
    if obj_name == "Station_Building":
        m "Здание заправки.
        Здесь должнен быть где-то вход..."
    return
