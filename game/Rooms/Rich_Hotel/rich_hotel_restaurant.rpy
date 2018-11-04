default richHotelRestaurantState = 0
default richHotelEmptyTableWatched = False
default richHotelTableChairsSeen = False

label rich_hotel_restaurant:

    $ print "enter_rich_hotel_restaurant"
    $ miniMapData = []

    $ scene_name = "rich_hotel_restaurant"
    $ scene_caption = _("Restaurant")
    $ clear_scene_from_objects(scene_name)

    if richHotelRestaurantState == 0:
        $ scene_image = "scene_rich_hotel_restaurant_Waitress"
        $ add_object_to_scene("Waitress", {"type":2, "base":"rich_hotel_restaurant_Waitress", "click" : "rich_hotel_restaurant_environment", "actions" : "lt", "zorder" : 15})
        $ add_object_to_scene("TableChairs", {"type":2, "base":"rich_hotel_restaurant_TableChairs", "click" : "rich_hotel_restaurant_environment", "actions" : "lh", "zorder" : 1})
    if richHotelRestaurantState == 1:
        $ scene_image = "scene_rich_hotel_restaurant_Monica_Dick_Waitress_1"
        $ add_object_to_scene("Waitress", {"type":2, "base":"rich_hotel_restaurant_Monica_Dick_Waitress_1_Waitress", "click" : "rich_hotel_restaurant_environment", "actions" : "lt", "zorder" : 15})
        $ add_object_to_scene("Monica", {"type":2, "base":"rich_hotel_restaurant_Monica_Dick_Waitress_1_Monica" , "click" : "rich_hotel_restaurant_environment", "actions" : "l", "zorder" : 11})
        $ add_object_to_scene("DickTheLawyer", {"type":2, "base":"rich_hotel_restaurant_Monica_Dick_Waitress_1_Dick", "click" : "rich_hotel_restaurant_environment", "actions" : "lt", "zorder" : 10, "icon_t":"/Icons/talk" + res.suffix +".png", "b":0.14, "s":1.3, "tint":[1.0, 1.0, 0.8]})
        $ add_object_to_scene("Table", {"type":2, "base":"rich_hotel_restaurant_Table", "click" : "rich_hotel_restaurant_environment", "actions" : "l", "zorder" : 1})
    if richHotelRestaurantState == 2:
        $ scene_image = "scene_rich_hotel_restaurant_Monica_Dick"
        $ add_object_to_scene("Monica", {"type":2, "base":"rich_hotel_restaurant_Monica_Dick_Monica" , "click" : "rich_hotel_restaurant_environment", "actions" : "l", "zorder" : 11})
        $ add_object_to_scene("DickTheLawyer", {"type":2, "base":"rich_hotel_restaurant_Monica_Dick_Dick", "click" : "rich_hotel_restaurant_environment", "actions" : "lt", "zorder" : 10, "icon_t":"/Icons/talk" + res.suffix +".png", "b":0.14, "s":1.3, "tint":[1.0, 1.0, 0.8]})
        $ add_object_to_scene("Table", {"type":2, "base":"rich_hotel_restaurant_Table", "click" : "rich_hotel_restaurant_environment", "actions" : "l", "zorder" : 1})
    if richHotelRestaurantState == 3:
        $ scene_image = "scene_rich_hotel_restaurant_Monica_Dick_Waitress_1"
        $ add_object_to_scene("Waitress", {"type":2, "base":"rich_hotel_restaurant_Monica_Dick_Waitress_2_Waitress", "click" : "rich_hotel_restaurant_environment", "actions" : "lt", "zorder" : 15})
        $ add_object_to_scene("Monica", {"type":2, "base":"rich_hotel_restaurant_Monica_Dick_Waitress_2_Monica" , "click" : "rich_hotel_restaurant_environment", "actions" : "l", "zorder" : 11})
        $ add_object_to_scene("DickTheLawyer", {"type":2, "base":"rich_hotel_restaurant_Monica_Dick_Waitress_2_Dick", "click" : "rich_hotel_restaurant_environment", "actions" : "lt", "zorder" : 10, "icon_t":"/Icons/talk" + res.suffix +".png", "b":0.14, "s":1.3, "tint":[1.0, 1.0, 0.8]})
        $ add_object_to_scene("Table", {"type":2, "base":"rich_hotel_restaurant_Table", "click" : "rich_hotel_restaurant_environment", "actions" : "l", "zorder" : 1})


    $ add_object_to_scene("Bar", {"type":2, "base":"rich_hotel_restaurant_Bar", "click" : "rich_hotel_restaurant_environment", "actions" : "l", "zorder" : 1})
    $ add_object_to_scene("EmptyTable1", {"type":2, "base":"rich_hotel_restaurant_EmptyTable1", "click" : "rich_hotel_restaurant_environment", "actions" : "l", "zorder" : 1})
    $ add_object_to_scene("EmptyTable2", {"type":2, "base":"rich_hotel_restaurant_EmptyTable2", "click" : "rich_hotel_restaurant_environment", "actions" : "l", "zorder" : 1})
    $ add_object_to_scene("EmptyTable3", {"type":2, "base":"rich_hotel_restaurant_EmptyTable3", "click" : "rich_hotel_restaurant_environment", "actions" : "l", "zorder" : 1})
    $ add_object_to_scene("EmptyTable4", {"type":2, "base":"rich_hotel_restaurant_EmptyTable4", "click" : "rich_hotel_restaurant_environment", "actions" : "l", "zorder" : 1})
    $ add_object_to_scene("EmptyTable5", {"type":2, "base":"rich_hotel_restaurant_EmptyTable5", "click" : "rich_hotel_restaurant_environment", "actions" : "l", "zorder" : 1})
    $ add_object_to_scene("EmptyTable6", {"type":2, "base":"rich_hotel_restaurant_EmptyTable6", "click" : "rich_hotel_restaurant_environment", "actions" : "l", "zorder" : 1})
    $ add_object_to_scene("EmptyTable7", {"type":2, "base":"rich_hotel_restaurant_EmptyTable7", "click" : "rich_hotel_restaurant_environment", "actions" : "l", "zorder" : 1})
    $ add_object_to_scene("EmptyTable8", {"type":2, "base":"rich_hotel_restaurant_EmptyTable8", "click" : "rich_hotel_restaurant_environment", "actions" : "l", "zorder" : 1})
    $ add_object_to_scene("EmptyTable9", {"type":2, "base":"rich_hotel_restaurant_EmptyTable9", "click" : "rich_hotel_restaurant_environment", "actions" : "l", "zorder" : 1})
    $ add_object_to_scene("EmptyTable10", {"type":2, "base":"rich_hotel_restaurant_EmptyTable10", "click" : "rich_hotel_restaurant_environment", "actions" : "l", "zorder" : 1})

    $ add_object_to_scene("Teleport_Reception", {"type":3, "text" : _("РЕЦЕПШИН"), "larrow" : "arrow_left_2", "base":"rich_hotel_restaurant_Teleport_Reception", "click" : "rich_hotel_restaurant_teleport", "xpos" : 954, "ypos" : 138, "zorder":11})

    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label rich_hotel_restaurant_teleport(obj_name, obj_data):
    if obj_name == "Teleport_Reception":
        if richHotelDickMeetingExitClosed == True:
            dick "Дорогая, ты уже хочешь уходить?
            Давай немного посидим!"
            return
        call change_scene("rich_hotel_reception")
        return
    return
label rich_hotel_restaurant_environment(obj_name, obj_data):
    if obj_name == "Bar":
        m "Бар. Но бармена там уже нет."
    if obj_name == "EmptyTable1" or obj_name == "EmptyTable2" or obj_name == "EmptyTable3" or obj_name == "EmptyTable4" or obj_name == "EmptyTable5" or obj_name == "EmptyTable6" or obj_name == "EmptyTable7" or obj_name == "EmptyTable8" or obj_name == "EmptyTable9" or obj_name == "EmptyTable10":
        if richHotelEmptyTableWatched == False:
            $ richHotelEmptyTableWatched = True
            m "Пустой столик..."
        else:
            m "Еще один пусток столик..."
        m "В ресторане уже никого нет."
    if obj_name == "Waitress":
        if obj_data["action"] == "l":
            if richHotelRestaurantState == 0 or richHotelRestaurantState == 1:
                mt "У этой официантки глупое и смешное лицо."
                "Одета в дешевую униформу.
                А чулки?
                Разве можно на работе носить такие чулки?"
            if richHotelRestaurantState == 3:
                call dick_meeting1_restaurant_waitress_interaction(obj_data)

        if obj_data["action"] == "t":
            if richHotelRestaurantState == 0:
                call dick_meeting1_restaurant_enter1_letsit()
                return
            call dick_meeting1_restaurant_waitress_interaction(obj_data)

    if obj_name == "TableChairs":
        if obj_data["action"] == "l":
            mt "Какой-то маленький столик..."
            "Хотя они все тут такие маленькие."
            "Официантка предлагает сесть сюда?"
            "Возможно это не худший вариант.
            Отсюда хороший обзор."
            "Меня смущает только то что не я выбрала это место!"
            $ richHotelTableChairsSeen = True
        if obj_data["action"] == "h":
            if richHotelTableChairsSeen == False:
                mt "Какой-то маленький столик..."
                "Хотя они все тут такие маленькие."
                "Официантка предлагает сесть сюда?"
                "Возможно это не худший вариант.
                Отсюда хороший обзор."
                "Меня смущает только то что не я выбрала это место!"
            m "Так уж и быть!
            Я позволю вам нас посадить за этот столик."
            "..."
            "Дик!"
            dick "Да, дорогая?"
            m "Дик, что ты там встал?
            Садись за тот большой стул.
            Все-равно ты больше никуда не поместишься здесь!"
            dick "Хорошо, дорогая!"
            music Last_Kiss_Goodnight
            $ richHotelRestaurantState = 1
            $ scene_transition = "Fade_long"
            $ scene_sound = "highheels_short_walk"
            call refresh_scene()
            return
    if obj_name == "Table":
        mt "Маленький неудобный столик!"
        "Это место начинает разочаровывать меня!"
    if obj_name == "Monica":
        call dick_meeting1_restaurant_monica_interaction(obj_data)
    if obj_name == "DickTheLawyer":
        call dick_meeting1_restaurant_dick_interaction(obj_data)
        return
    return
