default saleWomanAtCashier = False
default gasStationFlowerLooked = False

default gasStationRoomsBlocked = False

default gasStationDoorLooked = False
default gasStationSaleswomanCalledOut = False #продавщицу позвали
default gasStationSaleswomanMischiefed = False #продавщице напакостили
default gasStationMonicaLied = False
default gasStationSaleswomanMischiefInProgress = False #пакость в процессе
default gasStationSaleswomanAlmostCummed = True #продавщица чуть не кончила

default gasStationQuestCompletedJust = False
default gasStationQuestCompleted = False

default gasStationBeerLooked = False
default gasStationBeer6Looked = False
default gasStationBottle2Looked = False
default gasStationBottle2Broken = False

label gas_station_view1:
    $ print "enter_gas_station_view1"
    $ miniMapData = []

    $ scene_name = "gas_station_view1"
    $ scene_caption = _("Gas Station")
    $ clear_scene_from_objects(scene_name)

    if saleWomanAtCashier == True:
        $ scene_image = "scene_Gas_Station_View1_OilTrader_Monica"
        $ add_object_to_scene("SalesWoman", {"type":2, "base":"Gas_Station_View1_OilTrader", "click" : "gas_station_view1_environment", "actions" : "lw", "zorder" : 10})
    else:
        $ scene_image = "scene_Gas_Station_View1_Monica"

    $ add_object_to_scene("Monica", {"type":2, "base":"Gas_Station_View1_Monica_" + cloth, "click" : "gas_station_view1_environment", "actions" : "l", "zorder" : 10})

    $ add_object_to_scene("Cashier", {"type":2, "base":"Gas_Station_View1_Cashier", "click" : "gas_station_view1_environment", "actions" : "lw", "zorder" : 0})

    $ add_object_to_scene("Books_Stand", {"type":2, "base":"Gas_Station_View1_Teleport_View2", "click" : "gas_station_view1_environment", "actions" : "lw", "zorder" : 0})
    $ add_object_to_scene("Cakes_Stand", {"type":2, "base":"Gas_Station_View1_Teleport_View3", "click" : "gas_station_view1_environment", "actions" : "lw", "zorder" : 0})
    $ add_object_to_scene("Beverages_Stand", {"type":2, "base":"Gas_Station_View1_Teleport_View4", "click" : "gas_station_view1_environment", "actions" : "lw", "zorder" : 0})
    $ add_object_to_scene("Flower", {"type":2, "base":"Gas_Station_View1_Flower", "click" : "gas_station_view1_environment", "actions" : "l", "zorder" : 0})

    $ add_object_to_scene("Logo", {"type":2, "base":"Gas_Station_View1_Logo", "click" : "street_gas_station_environment", "actions" : "l", "zorder" : 0})

    $ add_object_to_scene("Teleport_Street_Gas_Station", {"type":3, "text" : _("НА УЛИЦУ"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "gas_station_view1_teleport", "xpos" : 960, "ypos" : 956, "zorder":11})
    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label gas_station_view1_teleport(obj_name, obj_data):
    if obj_name == "Teleport_Street_Gas_Station":
        call change_scene("street_gas_station") from _call_change_scene_55
        return
    if obj_name == "Teleport_Gas_Station_View1":
        call change_scene("gas_station_view1") from _call_change_scene_56
        return

    return
label gas_station_view1_environment(obj_name, obj_data):
    if obj_name == "SalesWoman":
        if obj_data["action"] == "l":
            if gasStationSaleswomanMischiefed == True and gasStationMonicaLied == True:
                m "А, это та жалкая кассирша?"
            else:
                m "Это кассирша, которую я так долго искала."
        if obj_data["action"] == "w":
            call change_scene("gas_station_view_cashier") from _call_change_scene_57
            return
    if obj_name == "Flower":
        m "Полудохлое растение."
        "Сразу видно что за ним не ухаживают..."
        "Одно это уже повод для наказания, как я считаю..."
        $ gasStationFlowerLooked = True
    if obj_name == "Monica":
        if gasStationQuestCompleted == True:
            if gasStationSaleswomanMischiefed == True:
                if gasStationMonicaLied == True:
                    m "Она теперь долго будет работать за бесплатно.
                    Хи-хи."
                else:
                    m "Мне придется заплатить за бутылку, зато как было весело!"
            else:
                m "Смотрю эта кассирша на рабочем месте? Ок..."
            return
        m "Нигде нет этой кассирши!"
        "Чем-то эта ситуация напоминает мне ситуацию с Юлией сегодня утром."
        if juliaPunished == True or juliaPunishedLow == True:
            "Так что я уже прямо сейчас могу охарактеризовать этого продавца."
    if obj_name == "Cashier":
        if obj_data["action"] == "l":
            m "Это касса, там за ней есть прилавки и дверь..."
        if obj_data["action"] == "w":
            call change_scene("gas_station_view_cashier") from _call_change_scene_58
            return
    if obj_name == "Books_Stand":
        if obj_data["action"] == "l":
            m "Прилавок с книгами..."
        if obj_data["action"] == "w":
            if gasStationRoomsBlocked == True:
                call gas_station_rooms_blocked_comment() from _call_gas_station_rooms_blocked_comment
                return
            call change_scene("gas_station_view2") from _call_change_scene_59
            return
    if obj_name == "Cakes_Stand":
        if obj_data["action"] == "l":
            m "Прилавок с пирожными!!!"
        if obj_data["action"] == "w":
            if gasStationRoomsBlocked == True:
                call gas_station_rooms_blocked_comment() from _call_gas_station_rooms_blocked_comment_1
                return
            call change_scene("gas_station_view3") from _call_change_scene_60
            return
    if obj_name == "Beverages_Stand":
        if obj_data["action"] == "l":
            m "Прилавки с напитками..."
        if obj_data["action"] == "w":
            if gasStationRoomsBlocked == True:
                call gas_station_rooms_blocked_comment() from _call_gas_station_rooms_blocked_comment_2
                return
            call change_scene("gas_station_view4") from _call_change_scene_61
            return
    return

label gas_station_no_saleswoman_caption:
    m "Странно, а где кассир?"
    call question_helper_enable("question_gas_trader1")
    $ add_objective("find_gas_cashier", _("Найти кассира"), c_blue, 30)
    $ gasStationFindingFuelQuestStage = 1
    $ gasStationRoomsBlocked = True
    $ autorun_to_object("gas_station_view_cashier", "gas_station_no_saleswoman_caption2")
    return

label gas_station_rooms_blocked_comment:
    m "Я думаю сначала надо поискать возле кассовой стойки..."
    return

label gas_station_no_saleswoman_caption2:
    m "Хм...
    В рабочее время кассир должна находиться здесь..."
    if bitchmeterValue > maxBitchness /2:
        "Гже же она?
        Черт бы побрал эту сучку!!!"
    else:
        "Где же она?
        Почему она не здесь?"

    return



label gas_station_view2:
    $ print "enter_gas_station_view2"
    $ miniMapData = []

    $ scene_name = "gas_station_view2"
    $ scene_caption = _("Gas Station")
    $ clear_scene_from_objects(scene_name)

    $ scene_image = "scene_Gas_Station_View2"
    $ add_object_to_scene("Water", {"type":2, "base":"Gas_Station_View2_Water", "click" : "gas_station_view2_environment", "actions" : "l", "zorder" : 0})
    $ add_object_to_scene("Cakes_Stand", {"type":2, "base":"Gas_Station_View2_Cakes_Stand", "click" : "gas_station_view1_environment", "actions" : "lw", "zorder" : 0})
    $ add_object_to_scene("Book1", {"type":2, "base":"Gas_Station_View2_Book1", "click" : "gas_station_view2_environment", "actions" : "l", "zorder" : 0, "b":0.15})
    $ add_object_to_scene("Book2", {"type":2, "base":"Gas_Station_View2_Book2", "click" : "gas_station_view2_environment", "actions" : "l", "zorder" : 0, "b":0.15})
    $ add_object_to_scene("Book3", {"type":2, "base":"Gas_Station_View2_Book3", "click" : "gas_station_view2_environment", "actions" : "l", "zorder" : 0, "b":0.15})
    $ add_object_to_scene("Book4", {"type":2, "base":"Gas_Station_View2_Book4", "click" : "gas_station_view2_environment", "actions" : "l", "zorder" : 0, "b":0.15})
    $ add_object_to_scene("Book5", {"type":2, "base":"Gas_Station_View2_Book5", "click" : "gas_station_view2_environment", "actions" : "l", "zorder" : 0, "b":0.15})
    $ add_object_to_scene("Book6", {"type":2, "base":"Gas_Station_View2_Book6", "click" : "gas_station_view2_environment", "actions" : "l", "zorder" : 0, "b":0.15})
    $ add_object_to_scene("Book7", {"type":2, "base":"Gas_Station_View2_Book7", "click" : "gas_station_view2_environment", "actions" : "l", "zorder" : 0, "b":0.15})
    $ add_object_to_scene("Book8", {"type":2, "base":"Gas_Station_View2_Book8", "click" : "gas_station_view2_environment", "actions" : "l", "zorder" : 0, "b":0.15})
    $ add_object_to_scene("Book9", {"type":2, "base":"Gas_Station_View2_Book9", "click" : "gas_station_view2_environment", "actions" : "l", "zorder" : 0, "b":0.15})
    $ add_object_to_scene("Book10", {"type":2, "base":"Gas_Station_View2_Book10", "click" : "gas_station_view2_environment", "actions" : "l", "zorder" : 0, "b":0.15})
    $ add_object_to_scene("Book11", {"type":2, "base":"Gas_Station_View2_Book11", "click" : "gas_station_view2_environment", "actions" : "l", "zorder" : 0, "b":0.15})
    $ add_object_to_scene("Book12", {"type":2, "base":"Gas_Station_View2_Book12", "click" : "gas_station_view2_environment", "actions" : "l", "zorder" : 0, "b":0.15})
    $ add_object_to_scene("Book13", {"type":2, "base":"Gas_Station_View2_Book13", "click" : "gas_station_view2_environment", "actions" : "l", "zorder" : 0, "b":0.15})
    $ add_object_to_scene("Book14", {"type":2, "base":"Gas_Station_View2_Book14", "click" : "gas_station_view2_environment", "actions" : "l", "zorder" : 0, "b":0.15})
    $ add_object_to_scene("Book15", {"type":2, "base":"Gas_Station_View2_Book15", "click" : "gas_station_view2_environment", "actions" : "l", "zorder" : 0, "b":0.15})
    $ add_object_to_scene("Book16", {"type":2, "base":"Gas_Station_View2_Book16", "click" : "gas_station_view2_environment", "actions" : "l", "zorder" : 0, "b":0.15})
    $ add_object_to_scene("Book17", {"type":2, "base":"Gas_Station_View2_Book17", "click" : "gas_station_view2_environment", "actions" : "l", "zorder" : 0, "b":0.15})
    $ add_object_to_scene("Book18", {"type":2, "base":"Gas_Station_View2_Book18", "click" : "gas_station_view2_environment", "actions" : "l", "zorder" : 0, "b":0.15})
    $ add_object_to_scene("Book19", {"type":2, "base":"Gas_Station_View2_Book19", "click" : "gas_station_view2_environment", "actions" : "l", "zorder" : 0, "b":0.15})
    $ add_object_to_scene("Book20", {"type":2, "base":"Gas_Station_View2_Book20", "click" : "gas_station_view2_environment", "actions" : "l", "zorder" : 0, "b":0.15})

    $ add_object_to_scene("Teleport_Gas_Station_View1", {"type":3, "text" : _("НАЗАД"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "gas_station_view1_teleport", "xpos" : 960, "ypos" : 956, "zorder":11})
    return

label gas_station_view2_environment(obj_name, obj_data):
    if obj_name == "Water":
        m "Здесь можно попить воды...
        Наверняка невкусной!"
        return
    if obj_name == "Book20":
        m "Книга про кофе??
        Да что этот автор может знать про кофе!!!"
        "Никчемные люди пишут никчемные книги!!!"
        call bitch(1, "book20") from _call_bitch_56
        return
    if obj_name == "Book9":
        m "Озеро..."
        "Помню в детстве рядом с моим домом было озеро."
        "Я была такой счастливой!
        Все мне казалось добрым и красивым!"
        call bitch(-1, "book9") from _call_bitch_57
        return
    m "Какая-то скучная книга...
    Фи!"

    return

label gas_station_view3:
    $ print "enter_gas_station_view3"
    $ miniMapData = []

    $ scene_name = "gas_station_view3"
    $ scene_caption = _("Gas Station")
    $ clear_scene_from_objects(scene_name)

    $ scene_image = "scene_Gas_Station_View3"
    $ add_object_to_scene("Water", {"type":2, "base":"Gas_Station_View3_Water", "click" : "gas_station_view2_environment", "actions" : "l", "zorder" : 0})
    $ add_object_to_scene("Cashier", {"type":2, "base":"Gas_Station_View3_Cashier", "click" : "gas_station_view1_environment", "actions" : "lw", "zorder" : 0})
    $ add_object_to_scene("Books_Stand", {"type":2, "base":"Gas_Station_View3_Books_Stand", "click" : "gas_station_view1_environment", "actions" : "lw", "zorder" : 0})

    $ add_object_to_scene("Cakes1", {"type":2, "base":"Gas_Station_View3_Cakes1", "click" : "gas_station_view3_environment", "actions" : "l", "zorder" : 1})
    $ add_object_to_scene("Cakes2", {"type":2, "base":"Gas_Station_View3_Cakes2", "click" : "gas_station_view3_environment", "actions" : "l", "zorder" : 1})
    $ add_object_to_scene("Cakes3", {"type":2, "base":"Gas_Station_View3_Cakes3", "click" : "gas_station_view3_environment", "actions" : "l", "zorder" : 1})
    $ add_object_to_scene("Cakes4", {"type":2, "base":"Gas_Station_View3_Cakes4", "click" : "gas_station_view3_environment", "actions" : "l", "zorder" : 1})
    $ add_object_to_scene("Cakes5", {"type":2, "base":"Gas_Station_View3_Cakes5", "click" : "gas_station_view3_environment", "actions" : "l", "zorder" : 1})
    $ add_object_to_scene("Cakes6", {"type":2, "base":"Gas_Station_View3_Cakes6", "click" : "gas_station_view3_environment", "actions" : "l", "zorder" : 1})
    $ add_object_to_scene("Cakes7", {"type":2, "base":"Gas_Station_View3_Cakes7", "click" : "gas_station_view3_environment", "actions" : "l", "zorder" : 1})
    $ add_object_to_scene("Cakes8", {"type":2, "base":"Gas_Station_View3_Cakes8", "click" : "gas_station_view3_environment", "actions" : "l", "zorder" : 1})
    $ add_object_to_scene("Cakes9", {"type":2, "base":"Gas_Station_View3_Cakes9", "click" : "gas_station_view3_environment", "actions" : "l", "zorder" : 1})

    $ add_object_to_scene("Teleport_Gas_Station_View1", {"type":3, "text" : _("НАЗАД"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "gas_station_view1_teleport", "xpos" : 960, "ypos" : 956, "zorder":11})
    return

label gas_station_view3_environment(obj_name, obj_data):
    if obj_name == "Cakes1":
        m "Чем эти ватрушки политы?
        Шоколадом?"
    if obj_name == "Cakes2" or obj_name == "Cakes4":
        m "Выглядит невкусно!"
    if obj_name == "Cakes3" or obj_name=="Cakes5":
        m "Пирожные...
        От них полнеешь, я такие не ем!"
    if obj_name == "Cakes6":
        m "Пирожные...
        От них полнеешь, я такие не ем!"
        "Хотя у меня прямо текут слюнки!!!"
    if obj_name == "Cakes7":
        m "Я детстве любила лакомиться такими!
        Как было здорово!"
        call bitch(-1, "cakes7") from _call_bitch_58
    if obj_name == "Cakes8":
        m "Жуткие лепешки...
        Жирные..."
    if obj_name == "Cakes9":
        m "Этим печеньем пусть кормят бездомных!
        Я такое бы есть не стала!"
        call bitch(1, "cakes9") from _call_bitch_59

    return

label gas_station_view4:
    $ print "enter_gas_station_view4"
    $ miniMapData = []

    $ scene_name = "gas_station_view4"
    $ scene_caption = _("Gas Station")
    $ clear_scene_from_objects(scene_name)

    $ scene_image = "scene_Gas_Station_View4"
    $ add_object_to_scene("Far_Counter", {"type":2, "base":"Gas_Station_View4_Far_Counter", "click" : "gas_station_view4_environment", "actions" : "l", "zorder" : 0})
    $ add_object_to_scene("Juice", {"type":2, "base":"Gas_Station_View4_Juice", "click" : "gas_station_view4_environment", "actions" : "lw", "zorder" : 0})

    $ add_object_to_scene("Cans1", {"type":2, "base":"Gas_Station_View4_Cans1", "click" : "gas_station_view4_environment", "actions" : "l", "zorder" : 0, "b":0.15})
    $ add_object_to_scene("Cans2", {"type":2, "base":"Gas_Station_View4_Cans2", "click" : "gas_station_view4_environment", "actions" : "l", "zorder" : 0, "b":0.15})
    $ add_object_to_scene("Cans3", {"type":2, "base":"Gas_Station_View4_Cans3", "click" : "gas_station_view4_environment", "actions" : "l", "zorder" : 0, "b":0.15})
    $ add_object_to_scene("Cans4", {"type":2, "base":"Gas_Station_View4_Cans4", "click" : "gas_station_view4_environment", "actions" : "l", "zorder" : 0, "b":0.15})
    $ add_object_to_scene("Cans5", {"type":2, "base":"Gas_Station_View4_Cans5", "click" : "gas_station_view4_environment", "actions" : "l", "zorder" : 0, "b":0.15})
    $ add_object_to_scene("Cans6", {"type":2, "base":"Gas_Station_View4_Cans6", "click" : "gas_station_view4_environment", "actions" : "l", "zorder" : 0, "b":0.15})
    $ add_object_to_scene("Cans7", {"type":2, "base":"Gas_Station_View4_Cans7", "click" : "gas_station_view4_environment", "actions" : "l", "zorder" : 0, "b":0.15})
    $ add_object_to_scene("Cans8", {"type":2, "base":"Gas_Station_View4_Cans8", "click" : "gas_station_view4_environment", "actions" : "l", "zorder" : 0, "b":0.15})
    $ add_object_to_scene("Cans9", {"type":2, "base":"Gas_Station_View4_Cans9", "click" : "gas_station_view4_environment", "actions" : "l", "zorder" : 0, "b":0.15})
    $ add_object_to_scene("Cans10", {"type":2, "base":"Gas_Station_View4_Cans10", "click" : "gas_station_view4_environment", "actions" : "l", "zorder" : 0, "b":0.15})
    $ add_object_to_scene("Cans11", {"type":2, "base":"Gas_Station_View4_Cans11", "click" : "gas_station_view4_environment", "actions" : "l", "zorder" : 0, "b":0.15})
    $ add_object_to_scene("Cans12", {"type":2, "base":"Gas_Station_View4_Cans12", "click" : "gas_station_view4_environment", "actions" : "l", "zorder" : 0, "b":0.15})

    $ add_object_to_scene("Wine1", {"type":2, "base":"Gas_Station_View4_Wine1", "click" : "gas_station_view4_environment", "actions" : "l", "zorder" : 0, "b":0.15})
    $ add_object_to_scene("Wine2", {"type":2, "base":"Gas_Station_View4_Wine2", "click" : "gas_station_view4_environment", "actions" : "l", "zorder" : 0, "b":0.15})
    $ add_object_to_scene("Wine3", {"type":2, "base":"Gas_Station_View4_Wine3", "click" : "gas_station_view4_environment", "actions" : "l", "zorder" : 0, "b":0.15})
    $ add_object_to_scene("Wine4", {"type":2, "base":"Gas_Station_View4_Wine4", "click" : "gas_station_view4_environment", "actions" : "l", "zorder" : 0, "b":0.15})
    $ add_object_to_scene("Wine5", {"type":2, "base":"Gas_Station_View4_Wine5", "click" : "gas_station_view4_environment", "actions" : "l", "zorder" : 0, "b":0.15})
    $ add_object_to_scene("Wine6", {"type":2, "base":"Gas_Station_View4_Wine6", "click" : "gas_station_view4_environment", "actions" : "l", "zorder" : 0, "b":0.15})
    $ add_object_to_scene("Wine7", {"type":2, "base":"Gas_Station_View4_Wine7", "click" : "gas_station_view4_environment", "actions" : "l", "zorder" : 0, "b":0.15})
    $ add_object_to_scene("Wine8", {"type":2, "base":"Gas_Station_View4_Wine8", "click" : "gas_station_view4_environment", "actions" : "l", "zorder" : 0, "b":0.15})
    $ add_object_to_scene("Wine9", {"type":2, "base":"Gas_Station_View4_Wine9", "click" : "gas_station_view4_environment", "actions" : "l", "zorder" : 0, "b":0.15})
    $ add_object_to_scene("Wine10", {"type":2, "base":"Gas_Station_View4_Wine10", "click" : "gas_station_view4_environment", "actions" : "l", "zorder" : 0, "b":0.15})
    $ add_object_to_scene("Wine11", {"type":2, "base":"Gas_Station_View4_Wine11", "click" : "gas_station_view4_environment", "actions" : "l", "zorder" : 0, "b":0.15})
    $ add_object_to_scene("Wine12", {"type":2, "base":"Gas_Station_View4_Wine12", "click" : "gas_station_view4_environment", "actions" : "l", "zorder" : 0, "b":0.15})
    $ add_object_to_scene("Wine13", {"type":2, "base":"Gas_Station_View4_Wine13", "click" : "gas_station_view4_environment", "actions" : "l", "zorder" : 0, "b":0.15})

    $ add_object_to_scene("Teleport_Gas_Station_View1", {"type":3, "text" : _("НАЗАД"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "gas_station_view1_teleport", "xpos" : 960, "ypos" : 956, "zorder":11})
    return

label gas_station_view4_environment(obj_name, obj_data):
    if obj_name == "Far_Counter":
        m "Там вдалеке еще стеллаж с алкоголем.
        Мне не видно отсюда..."
        return
    if obj_name == "Juice":
        if obj_data["action"] == "l":
            m "Там какие-то соки..."
        if obj_data["action"] == "w":
            call change_scene("gas_station_view5") from _call_change_scene_62
            return

    if obj_name == "Cans1":
        m "Пиво...
        В зеленой банке..."
    if obj_name == "Cans2":
        m "Пиво...
        В красной банке..."
    if obj_name == "Cans3":
        m "Пиво...
        В желтой банке..."
    if obj_name == "Cans4":
        m "Пиво Pale Ale"
    if obj_name == "Cans5":
        m "Пиво Lager"
    if obj_name == "Cans6":
        m "Пиво из солода Pilsen?"
    if obj_name == "Cans7":
        m "Пиво, малиновое?"
    if obj_name == "Cans8":
        m "Пиво яблочное, хи-хи!"
    if obj_name == "Cans9":
        m "О! Цитрусовое пиво?"
    if obj_name == "Cans10":
        m "А тут что нарисовано?
        Пиво из еловых шишек?"
    if obj_name == "Cans11":
        m "Какое-то незнакомое пиво."
    if obj_name == "Cans12":
        m "Пиво из... слона???
        Бедный слон ((("

    if obj_name == "Wine1" or obj_name == "Wine4" or obj_name == "Wine8" or obj_name == "Wine10":
        m "Красное сухое вино."
        call gas_station_wine_cheap() from _call_gas_station_wine_cheap
    if obj_name == "Wine2" or obj_name == "Wine5" or obj_name == "Wine11":
        m "Белое полусладкое вино."
        call gas_station_wine_cheap() from _call_gas_station_wine_cheap_1
    if obj_name == "Wine3" or obj_name == "Wine9" or obj_name == "Wine13":
        m "Красное сладкое вино."
        call gas_station_wine_cheap() from _call_gas_station_wine_cheap_2
    if obj_name == "Wine6" or obj_name == "Wine7" or obj_name == "Wine12":
        m "Белое сухое вино."
        call gas_station_wine_cheap() from _call_gas_station_wine_cheap_3

    if gasStationBeerLooked == False:
        m "Когда я была маленькой, взрослые любили пиво.
        А я любила взрослых, любила с ними играть..."
        "Поэтому, как ни странно, я хорошо отношусь к тем кто его пьет!"
        $ gasStationBeerLooked = True

    return

label gas_station_wine_cheap:
    m "Дешевое..."
    return

label gas_station_view5:
    $ print "enter_gas_station_view5"
    $ miniMapData = []

    $ scene_name = "gas_station_view5"
    $ scene_caption = _("Gas Station")
    $ clear_scene_from_objects(scene_name)

    $ scene_image = "scene_Gas_Station_View5"
    $ add_object_to_scene("Left_Counter", {"type":2, "base":"Gas_Station_View5_Left_Counter", "click" : "gas_station_view5_environment", "actions" : "lw", "zorder" : 0})
    $ add_object_to_scene("Far_Counter", {"type":2, "base":"Gas_Station_View5_Far_Counter", "click" : "gas_station_view5_environment", "actions" : "lw", "zorder" : 0})
    $ add_object_to_scene("Flower", {"type":2, "base":"Gas_Station_View5_Flower", "click" : "gas_station_view1_environment", "actions" : "l", "zorder" : 0})
    $ add_object_to_scene("Sofa", {"type":2, "base":"Gas_Station_View5_Sofa", "click" : "gas_station_view5_environment", "actions" : "l", "zorder" : 0})

    $ add_object_to_scene("Juice", {"type":2, "base":"Gas_Station_View5_Juice", "click" : "gas_station_view5_environment", "actions" : "l", "zorder" : 0})
    $ add_object_to_scene("Desk", {"type":2, "base":"Gas_Station_View5_Desk", "click" : "gas_station_view5_environment", "actions" : "l", "zorder" : 0})

    $ add_object_to_scene("Teleport_Gas_Station_View1", {"type":3, "text" : _("НАЗАД"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "gas_station_view1_teleport", "xpos" : 960, "ypos" : 956, "zorder":11})
    return

label gas_station_view5_environment(obj_name, obj_data):
    if obj_name == "Sofa":
        m "Какой-то дешевый диван, такой же дешевый как и заправка!"
    if obj_name == "Left_Counter":
        if obj_data["action"] == "l":
            m "Прилавки с напитками..."
        if obj_data["action"] == "w":
            call change_scene("gas_station_view4") from _call_change_scene_63
            return
    if obj_name == "Juice":
        m "Апельсиновый сок...
        Только апельсиновый..."
    if obj_name == "Desk":
        m "Могу поспорить что в этом ящике тоже апельсиновый сок!"
        "Даже не буду проверять!"

    if obj_name == "Far_Counter":
        if obj_data["action"] == "l":
            m "Там вдалеке еще стеллаж с алкоголем.
            Мне не видно отсюда..."
            "Можно подойти посмотреть."

        if obj_data["action"] == "w":
            call change_scene("gas_station_view6") from _call_change_scene_64
            return

    return

label gas_station_view6:
    $ print "enter_gas_station_view6"
    $ miniMapData = []

    $ scene_name = "gas_station_view6"
    $ scene_caption = _("Gas Station")
    $ clear_scene_from_objects(scene_name)

    if gasStationBottle2Broken == False:
        $ scene_image = "scene_Gas_Station_View6"
    else:
        $ scene_image = "scene_Gas_Station_View6_nobottle"
    $ add_object_to_scene("Sofa", {"type":2, "base":"Gas_Station_View6_Sofa", "click" : "gas_station_view5_environment", "actions" : "l", "zorder" : 0})
    $ add_object_to_scene("Flower", {"type":2, "base":"Gas_Station_View6_Flower", "click" : "gas_station_view1_environment", "actions" : "l", "zorder" : 0})

    $ add_object_to_scene("Beer1", {"type":2, "base":"Gas_Station_View6_Beer1", "click" : "gas_station_view6_environment", "actions" : "l", "zorder" : 0, "b":0.15})
    $ add_object_to_scene("Beer2", {"type":2, "base":"Gas_Station_View6_Beer2", "click" : "gas_station_view6_environment", "actions" : "l", "zorder" : 0, "b":0.15})
    $ add_object_to_scene("Beer3", {"type":2, "base":"Gas_Station_View6_Beer3", "click" : "gas_station_view6_environment", "actions" : "l", "zorder" : 0, "b":0.15})
    $ add_object_to_scene("Beer4", {"type":2, "base":"Gas_Station_View6_Beer4", "click" : "gas_station_view6_environment", "actions" : "l", "zorder" : 0, "b":0.15})
    $ add_object_to_scene("Beer5", {"type":2, "base":"Gas_Station_View6_Beer5", "click" : "gas_station_view6_environment", "actions" : "l", "zorder" : 0, "b":0.15})
    $ add_object_to_scene("Beer6", {"type":2, "base":"Gas_Station_View6_Beer6", "click" : "gas_station_view6_environment", "actions" : "l", "zorder" : 0, "b":0.15})
    $ add_object_to_scene("Beer7", {"type":2, "base":"Gas_Station_View6_Beer7", "click" : "gas_station_view6_environment", "actions" : "l", "zorder" : 0, "b":0.15})
    $ add_object_to_scene("Beer8", {"type":2, "base":"Gas_Station_View6_Beer8", "click" : "gas_station_view6_environment", "actions" : "l", "zorder" : 0, "b":0.15})
    $ add_object_to_scene("Beer9", {"type":2, "base":"Gas_Station_View6_Beer9", "click" : "gas_station_view6_environment", "actions" : "l", "zorder" : 0, "b":0.15})
    $ add_object_to_scene("Beer10", {"type":2, "base":"Gas_Station_View6_Beer10", "click" : "gas_station_view6_environment", "actions" : "l", "zorder" : 0, "b":0.15})
    $ add_object_to_scene("Beer11", {"type":2, "base":"Gas_Station_View6_Beer11", "click" : "gas_station_view6_environment", "actions" : "l", "zorder" : 0, "b":0.15})
    $ add_object_to_scene("Beer12", {"type":2, "base":"Gas_Station_View6_Beer12", "click" : "gas_station_view6_environment", "actions" : "l", "zorder" : 0, "b":0.15})

    $ add_object_to_scene("Bottle1", {"type":2, "base":"Gas_Station_View6_Bottle1", "click" : "gas_station_view6_environment", "actions" : "l", "zorder" : 0, "b":0.15})
    if gasStationBottle2Broken == False:
        if gasStationSaleswomanMischiefInProgress == True:
            $ add_object_to_scene("Bottle2", {"type":2, "base":"Gas_Station_View6_Bottle2", "click" : "gas_station_view6_environment", "actions" : "lh", "zorder" : 0, "b":0.15})
        else:
            $ add_object_to_scene("Bottle2", {"type":2, "base":"Gas_Station_View6_Bottle2", "click" : "gas_station_view6_environment", "actions" : "l", "zorder" : 0, "b":0.15})

    $ add_object_to_scene("Teleport_Gas_Station_View5", {"type":3, "text" : _("НАЗАД"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "gas_station_view6_teleport", "xpos" : 960, "ypos" : 956, "zorder":11})
    return

label gas_station_view6_teleport(obj_name, obj_data):
    if obj_name == "Teleport_Gas_Station_View5":
        call change_scene("gas_station_view5") from _call_change_scene_65
        return

label gas_station_view6_environment(obj_name, obj_data):
    if obj_name == "Bottle1":
        m "А это виски!"
        "Что он здесь делает на стеллаже с пивом?"
        "Да еще и без ценника!"
        return
    if obj_name == "Bottle2":
        if obj_data["action"] == "l":
            "О. Chateau Lafleur.
            Я люблю это вино!"
            if gasStationSaleswomanMischiefInProgress == True:
                "Что оно здесь делает на стеллаже с пивом?
                Да еще на такой дешевой заправке!"
                "Да еще и без ценника!"
                "Но пить я сейчас не буду.
                А вот разбить что-нибудь я была бы не против."

                "Учитывая что продавца так и нет.
                Может быть это сможет привлечь внимание?"
                $ gasStationBottle2Looked = True
        if obj_data["action"] == "h":
            if gasStationBottle2Looked == False:
                "О. Chateau Lafleur.
                Я люблю это вино!"
                "Что оно здесь делает на стеллаже с пивом?
                Да еще на такой дешевой заправке!"
                "Да еще и без ценника!"
                "Но пить я сейчас не буду.
                А вот разбить что-нибудь я была бы не против."

                "Учитывая что продавца так и нет.
                Может быть это сможет привлечь внимание?"
            menu:
                "Разбить бутылку.":
                    call question_helper_disable()
                    call gas_saleswoman_scene3() from _call_gas_saleswoman_scene3
                    $ gasStationBottle2Broken = True
                    $ saleWomanAtCashier = True
                    $ remove_objective("find_gas_cashier")
                    $ remove_objective("gas_cashier_mischief")
                    call change_scene("gas_station_view_cashier") from _call_change_scene_66
                    $ gasStationFindingFuelQuestStage = 3
                    return

                "Не трогать":
                    return
        return

    m "Пиво, бутылочное..."
    return


label gas_station_view_cashier:
    $ print "enter_gas_station_view_cashier"
    $ miniMapData = []

    $ scene_name = "gas_station_view_cashier"
    $ scene_caption = _("Gas Station")
    $ clear_scene_from_objects(scene_name)

    if saleWomanAtCashier == True:
        if gasStationSaleswomanMischiefed == True:
            $ add_object_to_scene("SalesWoman", {"type":2, "base":"Gas_Station_View_CashierCashier_Sorry_Hard", "click" : "gas_station_view_cashier_environment", "actions" : "lt", "zorder" : 10})
            $ scene_image = "scene_Gas_Station_View_CashierCashier_Sorry_Hard"
        else:
            $ add_object_to_scene("SalesWoman", {"type":2, "base":"Gas_Station_View_CashierCashier_Sorry_Soft", "click" : "gas_station_view_cashier_environment", "actions" : "lt", "zorder" : 10})
            $ scene_image = "scene_Gas_Station_View_CashierCashier_Sorry_Soft"
    else:
        $ scene_image = "scene_Gas_Station_View_Cashier"

        $ add_object_to_scene("Cakes_Stand", {"type":2, "base":"Gas_Station_View_Cashier_Cakes_Stand", "click" : "gas_station_view1_environment", "actions" : "lw", "zorder" : 0})
        $ add_object_to_scene("Card_Terminal", {"type":2, "base":"Gas_Station_View_Cashier_Card_Terminal", "click" : "gas_station_view_cashier_environment", "actions" : "l", "zorder" : 0})
#    $ add_object_to_scene("Cash_Desk", {"type":2, "base":"Gas_Station_View_Cashier_Cash_Desk", "click" : "gas_station_view_cashier_environment", "actions" : "l", "zorder" : 0})
        $ add_object_to_scene("Cash_Register", {"type":2, "base":"Gas_Station_View_Cashier_Cash_Register", "click" : "gas_station_view_cashier_environment", "actions" : "l", "zorder" : 0})

        $ add_object_to_scene("Door", {"type":2, "base":"Gas_Station_View_Cashier_Door", "click" : "gas_station_view_cashier_environment", "actions" : "lw", "zorder" : 0})


        $ add_object_to_scene("Oil", {"type":2, "base":"Gas_Station_View_Cashier_Oil", "click" : "gas_station_view_cashier_environment", "actions" : "l", "zorder" : 0})

        $ add_object_to_scene("Food1", {"type":2, "base":"Gas_Station_View_Cashier_Food1", "click" : "gas_station_view_cashier_environment", "actions" : "l", "zorder" : 0})
        $ add_object_to_scene("Food2", {"type":2, "base":"Gas_Station_View_Cashier_Food2", "click" : "gas_station_view_cashier_environment", "actions" : "l", "zorder" : 0})
        $ add_object_to_scene("Food3", {"type":2, "base":"Gas_Station_View_Cashier_Food3", "click" : "gas_station_view_cashier_environment", "actions" : "l", "zorder" : 0})
        $ add_object_to_scene("Food4", {"type":2, "base":"Gas_Station_View_Cashier_Food4", "click" : "gas_station_view_cashier_environment", "actions" : "l", "zorder" : 0})
        $ add_object_to_scene("Food5", {"type":2, "base":"Gas_Station_View_Cashier_Food5", "click" : "gas_station_view_cashier_environment", "actions" : "l", "zorder" : 0})
        $ add_object_to_scene("Food6", {"type":2, "base":"Gas_Station_View_Cashier_Food6", "click" : "gas_station_view_cashier_environment", "actions" : "l", "zorder" : 0})
        $ add_object_to_scene("Food7", {"type":2, "base":"Gas_Station_View_Cashier_Food7", "click" : "gas_station_view_cashier_environment", "actions" : "l", "zorder" : 0})
        $ add_object_to_scene("Food8", {"type":2, "base":"Gas_Station_View_Cashier_Food8", "click" : "gas_station_view_cashier_environment", "actions" : "l", "zorder" : 0})

        $ add_object_to_scene("Yogurt1", {"type":2, "base":"Gas_Station_View_Cashier_Yogurt1", "click" : "gas_station_view_cashier_environment", "actions" : "l", "zorder" : 0})
        $ add_object_to_scene("Yogurt2", {"type":2, "base":"Gas_Station_View_Cashier_Yogurt2", "click" : "gas_station_view_cashier_environment", "actions" : "l", "zorder" : 0})
        $ add_object_to_scene("Yogurt3", {"type":2, "base":"Gas_Station_View_Cashier_Yogurt3", "click" : "gas_station_view_cashier_environment", "actions" : "l", "zorder" : 0})
        $ add_object_to_scene("Yogurt4", {"type":2, "base":"Gas_Station_View_Cashier_Yogurt4", "click" : "gas_station_view_cashier_environment", "actions" : "l", "zorder" : 0})
        $ add_object_to_scene("Yogurt5", {"type":2, "base":"Gas_Station_View_Cashier_Yogurt5", "click" : "gas_station_view_cashier_environment", "actions" : "l", "zorder" : 0})
        $ add_object_to_scene("Yogurt6", {"type":2, "base":"Gas_Station_View_Cashier_Yogurt6", "click" : "gas_station_view_cashier_environment", "actions" : "l", "zorder" : 0})
        $ add_object_to_scene("Yogurt7", {"type":2, "base":"Gas_Station_View_Cashier_Yogurt7", "click" : "gas_station_view_cashier_environment", "actions" : "l", "zorder" : 0})
        $ add_object_to_scene("Yogurt8", {"type":2, "base":"Gas_Station_View_Cashier_Yogurt8", "click" : "gas_station_view_cashier_environment", "actions" : "l", "zorder" : 0})
        $ add_object_to_scene("Yogurt9", {"type":2, "base":"Gas_Station_View_Cashier_Yogurt9", "click" : "gas_station_view_cashier_environment", "actions" : "l", "zorder" : 0})
        $ add_object_to_scene("Yogurt10", {"type":2, "base":"Gas_Station_View_Cashier_Yogurt10", "click" : "gas_station_view_cashier_environment", "actions" : "l", "zorder" : 0})
        $ add_object_to_scene("Yogurt11", {"type":2, "base":"Gas_Station_View_Cashier_Yogurt11", "click" : "gas_station_view_cashier_environment", "actions" : "l", "zorder" : 0})

        $ add_object_to_scene("Logo", {"type":2, "base":"Gas_Station_View_Cashier_Logo", "click" : "street_gas_station_environment", "actions" : "l", "zorder" : 0})

    $ add_object_to_scene("Teleport_Gas_Station_View1", {"type":3, "text" : _("НАЗАД"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "gas_station_view1_teleport", "xpos" : 960, "ypos" : 956, "zorder":11})
    return

label gas_station_view_cashier_teleport(obj_name, obj_data):
    if obj_name == "Teleport_Gas_Station_View5":
        call change_scene("gas_station_view5") from _call_change_scene_67
        return

label gas_station_view_cashier_environment(obj_name, obj_data):
    if obj_name == "SalesWoman":
        if obj_data["action"] == "l":
            if gasStationSaleswomanMischiefed == True and gasStationMonicaLied == True:
                m "А, это та жалкая кассирша?"
            else:
                m "Это кассирша, которую я так долго искала."
        if obj_data["action"] == "t":
            call gas_salewoman_sorry_dialogue() from _call_gas_salewoman_sorry_dialogue
            return

    if obj_name == "Door":
        if obj_data["action"] == "l":
            m "Какая-то дверь."
        if obj_data["action"] == "w":
            call change_scene("gas_station_view_door") from _call_change_scene_68
            return
    if obj_name == "Oil":
        m "Какие-то банки.
        Может что-то для автомобилей?"
    if obj_name == "Food1" or obj_name == "Food2" or obj_name == "Food3" or obj_name == "Food4" or obj_name == "Food5" or obj_name == "Food6" or obj_name == "Food7" or obj_name == "Food8":
        m "Здесь продаются некоторые продукты..."
    if obj_name == "Yogurt1" or obj_name == "Yogurt2" or obj_name == "Yogurt3" or obj_name == "Yogurt4" or obj_name == "Yogurt5" or obj_name == "Yogurt6" or obj_name == "Yogurt7" or obj_name == "Yogurt8" or obj_name == "Yogurt9" or obj_name == "Yogurt10" or obj_name == "Yogurt11":
        m "На этом прилавке молочные продукты и йогурты..."
    if obj_name == "Card_Terminal":
        m "Терминал для пластиковых карточек."
        "Значит они не принимают карты?"
    if obj_name == "Cash_Register":
        m "Кассовый аппарат.
        Фред сказал он у них сломан."

    return

label gas_station_view_door:
    $ print "enter_gas_station_view_door"
    $ miniMapData = []

    $ scene_name = "gas_station_view_door"
    $ scene_caption = _("Gas Station")
    $ clear_scene_from_objects(scene_name)

    $ scene_image = "scene_Gas_Station_View_Door"

    $ add_object_to_scene("Flower", {"type":2, "base":"Gas_Station_View_Door_Flower", "click" : "gas_station_view1_environment", "actions" : "l", "zorder" : 0})
    $ add_object_to_scene("Cashier", {"type":2, "base":"Gas_Station_View_Door_Cashier", "click" : "gas_station_view1_environment", "actions" : "lw", "zorder" : 0})
    $ add_object_to_scene("Door", {"type":2, "base":"Gas_Station_View_Door_Door", "click" : "gas_station_view_door_environment", "actions" : "lt", "zorder" : 0})

    $ add_object_to_scene("Teleport_Gas_Station_View_Cashier", {"type":3, "text" : _("НАЗАД"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "gas_station_view_door_environment", "xpos" : 960, "ypos" : 956, "zorder":11})

    return
label gas_station_view_door_environment(obj_name, obj_data):
    if obj_name == "Teleport_Gas_Station_View_Cashier":
        call change_scene("gas_station_view_cashier") from _call_change_scene_69
        return
    if obj_name == "Door":
        if obj_data["action"] == "l":
            m "Мне кажется я что-то слышу там..."
            if gasStationDoorLooked == False:
                $ gasStationDoorLooked = True
                call gas_saleswoman_scene1() from _call_gas_saleswoman_scene1
            else:
                m "Или мне просто показалось?..."
            return
        if obj_data["action"] == "t":
            if gasStationDoorLooked == False:
                $ gasStationDoorLooked = True
                m "Мне кажется я что-то слышу там..."
                call gas_saleswoman_scene1() from _call_gas_saleswoman_scene1_1
            else:
                jump gas_station_door_talk


    return

label gas_station_door_talk:
    menu:
        "Привлечь внимание кассира какой-нибудь пакостью!":
#                    call bitch(10, "gas_saleswoman_decision")
            call question_helper_enable("question_gas_trader2")
            $ gasStationSaleswomanMischiefInProgress = True
            $ gasStationRoomsBlocked = False
            mt "Там она или нет, но надо привлечь ее внимание."
            "Попробую осмотреться вокруг, вдруг что-то найду?"
            $ add_objective("gas_cashier_mischief", _("Привлечь внимание кассира какой-нибудь пакостью!"), c_red, 35)
#                    $ autorun_to_object("gas_station_view2", "gas_saleswoman_scene1_1")
#                    $ autorun_to_object("gas_station_view3", "gas_saleswoman_scene1_2")
#                    $ autorun_to_object("gas_station_view6", "gas_saleswoman_scene1_3")
            return
        "Вежливо позвать, вдруг она за дверью?":
            call question_helper_disable()
            $ gasStationSaleswomanCalledOut = True
            call bitch(-10, "gas_saleswoman_decision") from _call_bitch_60
            m "ЭЙ!
            ЗДЕСЬ КТО-НИБУДЬ ЕСТЬ?!"
            call gas_saleswoman_scene2() from _call_gas_saleswoman_scene2
            $ saleWomanAtCashier = True
            $ gasStationRoomsBlocked = False
            call gas_saleswoman_dialogue1() from _call_gas_saleswoman_dialogue1
#                    $ autorun_to_object("gas_station_view_cashier", "gas_saleswoman_dialogue1")
            $ remove_objective("find_gas_cashier")
            $ remove_objective("gas_cashier_mischief")
            call change_scene("gas_station_view_cashier") from _call_change_scene_70
            $ gasStationFindingFuelQuestStage = 3
            return
    return
