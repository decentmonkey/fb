default gas_station_view1_s2_visited = False

label gas_station_view1_s2:
    $ print "enter_gas_station_view1"
    $ miniMapData = []

    $ scene_name = "gas_station_view1_s2"
    $ scene_caption = _("Gas Station")
    $ clear_scene_from_objects(scene_name)

    if saleWomanAtCashier == True:
        $ scene_image = "scene_Gas_Station_View1_OilTrader_Monica"
        $ add_object_to_scene("SalesWoman", {"type":2, "base":"Gas_Station_View1_OilTrader", "click" : "gas_station_view1_environment2", "actions" : "lw", "zorder" : 10})
    else:
        $ scene_image = "scene_Gas_Station_View1_Monica"

    $ add_object_to_scene("Monica", {"type":2, "base":"Gas_Station_View1_Monica_" + cloth, "click" : "gas_station_view1_environment2", "actions" : "l", "zorder" : 10})

    $ add_object_to_scene("Cashier", {"type":2, "base":"Gas_Station_View1_Cashier", "click" : "gas_station_view1_environment2", "actions" : "lw", "zorder" : 0})

    $ add_object_to_scene("Books_Stand", {"type":2, "base":"gas_station_view1_teleport_View2", "click" : "gas_station_view1_environment2", "actions" : "lw", "zorder" : 0})
    $ add_object_to_scene("Cakes_Stand", {"type":2, "base":"gas_station_view1_teleport_View3", "click" : "gas_station_view1_environment2", "actions" : "lw", "zorder" : 0})
    $ add_object_to_scene("Beverages_Stand", {"type":2, "base":"gas_station_view1_teleport_View4", "click" : "gas_station_view1_environment2", "actions" : "lw", "zorder" : 0})
    $ add_object_to_scene("Flower", {"type":2, "base":"Gas_Station_View1_Flower", "click" : "gas_station_view1_environment2", "actions" : "l", "zorder" : 0})

    $ add_object_to_scene("Logo", {"type":2, "base":"Gas_Station_View1_Logo", "click" : "street_gas_station_environment", "actions" : "l", "zorder" : 0})

    $ add_object_to_scene("Teleport_Street_Gas_Station", {"type":3, "text" : _("НА УЛИЦУ"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "gas_station_view1_teleport2", "xpos" : 960, "ypos" : 956, "zorder":11})
    if gas_station_view1_s2_visited == False and gameStage < 3:
        $ gas_station_view1_s2_visited = True
        $ autorun_to_object("gas_station_view1_s2", "gas_station_view1_environment2_a")
    music Groove2_85
    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label gas_station_view1_teleport2(obj_name, obj_data):
    if obj_name == "Teleport_Street_Gas_Station":
        call change_scene("street_gas_station")
        return
    return
label gas_station_view1_environment2(obj_name, obj_data):
    if obj_name == "SalesWoman":
        if obj_data["action"] == "l":
            mt "Это кассирша, которую я так долго искала."
        if obj_data["action"] == "w":
            mt "Я не собираюсь подходить к ней. Чем она может мне помочь?"
            "У нее же нет мозгов!"
            return
    if obj_name == "Flower":
        m "Полудохлое растение."
    if obj_name == "Monica":
        if gameStage == 3:
            mt "Что я здесь делаю?"
            return
        if gameSubStage == 1:
            mt "Что я здесь делаю? Мне надо к Дику!"
            return
        mt "Что я здесь делаю?"
        "Может здесь можно было бы переночевать, но эта дура будет работать всю ночь!"
    if obj_name == "Cashier":
        if obj_data["action"] == "l":
            mt "Это касса..."
        if obj_data["action"] == "w":
            mt "Я не хочу туда подходить."
            "Мне нечего делать здесь!"
            return
    if obj_name == "Books_Stand":
        if obj_data["action"] == "l":
            m "Прилавок с книгами..."
        if obj_data["action"] == "w":
            mt "Я не хочу туда подходить."
            "Мне нечего делать здесь!"
            return
    if obj_name == "Cakes_Stand":
        if obj_data["action"] == "l":
            m "Прилавок с пирожными!!!"
        if obj_data["action"] == "w":
            mt "Я не хочу туда подходить."
            "Мне нечего делать здесь!"
            return
    if obj_name == "Beverages_Stand":
        if obj_data["action"] == "l":
            m "Прилавки с напитками..."
        if obj_data["action"] == "w":
            mt "Я не хочу туда подходить."
            "Мне нечего делать здесь!"
            return
    return

label gas_station_view1_environment2_a:
    if gameSubStage == 1:
        mt "Что я здесь делаю? Мне надо к Дику!"
        return
    mt "Что я здесь делаю?"
    "Может здесь можно было бы переночевать, но эта дура будет работать всю ночь!"
    return
