default richHotelReceptionistEnabled = False
default richHotelReceptionDickEnabled = True
default richHotelReceptionEntered = True
default richHotelReceptionMonicaDickTalkedOnExit = False
default richHotelReceptionistMode = 0

label rich_hotel_reception:

    $ print "enter_rich_hotel_reception"
    $ miniMapData = []

    $ scene_name = "rich_hotel_reception"
    $ scene_caption = _("Hotel Reception")
    $ clear_scene_from_objects(scene_name)

    if richHotelReceptionistEnabled == False:
        if richHotelReceptionDickEnabled == True:
            if richHotelReceptionEntered == True:
                $ scene_image = "scene_Rich_Hotel_Reception_Monica_DickTheLawyer_" + cloth
                $ add_object_to_scene("Monica", {"type":2, "base":"Rich_Hotel_Reception_Monica_DickTheLawyer_Monica_" + cloth, "click" : "rich_hotel_reception_environment", "actions" : "l", "zorder" : 10})
                $ add_object_to_scene("DickTheLawyer", {"type":2, "base":"Rich_Hotel_Reception_Monica_DickTheLawyer_Dick_" + cloth, "click" : "rich_hotel_reception_environment", "actions" : "lt", "zorder" : 10, "icon_t":"/Icons/talk" + res.suffix +".png", "b":0.14, "s":1.3, "tint":[1.0, 1.0, 0.8]})
            else:
                $ scene_image = "scene_Rich_Hotel_Reception_Monica_DickTheLawyer_" + cloth + "2"
                $ add_object_to_scene("Monica", {"type":2, "base":"Rich_Hotel_Reception_Monica_DickTheLawyer_Monica_" + cloth + "2", "click" : "rich_hotel_reception_environment", "actions" : "l", "zorder" : 10})
                $ add_object_to_scene("DickTheLawyer", {"type":2, "base":"Rich_Hotel_Reception_Monica_DickTheLawyer_Dick_" + cloth + "2", "click" : "rich_hotel_reception_environment", "actions" : "lt", "zorder" : 10, "icon_t":"/Icons/talk" + res.suffix +".png", "b":0.14, "s":1.3, "tint":[1.0, 1.0, 0.8]})
        else:
            $ scene_image = "scene_Rich_Hotel_Reception_Monica_" + cloth
    else:
            $ scene_image = "scene_Rich_Hotel_Reception_Monica_" + cloth
            $ add_object_to_scene("Monica", {"type":2, "base":"Rich_Hotel_Reception_Monica_" + cloth, "click" : "rich_hotel_reception_environment", "actions" : "l", "zorder" : 10})
            if richHotelReceptionistMode == 0:
                $ add_object_to_scene("ReceptionGirl", {"type":2, "base":"Rich_Hotel_Reception_Reception", "click" : "rich_hotel_reception_environment", "actions" : "lt", "zorder" : 10})


    $ add_object_to_scene("Logo", {"type":2, "base":"Rich_Hotel_Reception_Logo", "click" : "street_rich_hotel_environment", "actions" : "l", "zorder" : 3, "tint":[1.0, 1.0, 0.3]})
    $ add_object_to_scene("Clocks", {"type":2, "base":"Rich_Hotel_Reception_Clocks", "click" : "rich_hotel_reception_environment", "actions" : "l", "zorder" : 3})
    $ add_object_to_scene("Door", {"type":2, "base":"Rich_Hotel_Reception_Door", "click" : "rich_hotel_reception_environment", "actions" : "l", "zorder" : 3, "b":0.15})
    $ add_object_to_scene("Flowers", {"type":2, "base":"Rich_Hotel_Reception_Flowers", "click" : "rich_hotel_reception_environment", "actions" : "l", "zorder" : 3})
    $ add_object_to_scene("Jug1", {"type":2, "base":"Rich_Hotel_Reception_Jug1", "click" : "rich_hotel_reception_environment", "actions" : "l", "zorder" : 3})
    $ add_object_to_scene("Jug2", {"type":2, "base":"Rich_Hotel_Reception_Jug2", "click" : "rich_hotel_reception_environment", "actions" : "l", "zorder" : 3})
#    $ add_object_to_scene("Lamps", {"type":2, "base":"Rich_Hotel_Reception_Lamps", "click" : "rich_hotel_reception_environment", "actions" : "l", "zorder" : 3})
    $ add_object_to_scene("Tea", {"type":2, "base":"Rich_Hotel_Reception_Tea", "click" : "rich_hotel_reception_environment", "actions" : "l", "zorder" : 15})
    $ add_object_to_scene("Desk", {"type":2, "base":"Rich_Hotel_Reception_Desk", "click" : "rich_hotel_reception_environment", "actions" : "l", "zorder" : 3})
    $ add_object_to_scene("Chair", {"type":2, "base":"Rich_Hotel_Reception_Chair", "click" : "rich_hotel_reception_environment", "actions" : "l", "zorder" : 3})

    $ add_object_to_scene("Teleport_Restaurant", {"type":3, "text" : _("РЕСТОРАН"), "rarrow" : "arrow_right_2", "base":"Rich_Hotel_Reception_Teleport_Restaurant", "click" : "rich_hotel_reception_teleport", "xpos" : 1018, "ypos" : 103, "zorder":11})
    $ add_object_to_scene("Teleport_Street_Rich_Hotel", {"type":3, "text" : _("НАЗАД НА УЛИЦУ"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "rich_hotel_reception_teleport", "xpos" : 960, "ypos" : 956, "zorder":11})

    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label rich_hotel_reception_teleport(obj_name, obj_data):
    if obj_name == "Teleport_Street_Rich_Hotel":
        if dickWaitingMonica4 == True and richHotelReceptionMonicaDickTalkedOnExit == False:
            $ richHotelReceptionMonicaDickTalkedOnExit = True
            m "Сначала ты меня привел в какую-то дыру, назвав ее магазином."
            "Теперь ты привел меня в пустой ресторан."
            "Дик, ты пытаешься произвести на меня впечатление этим?"
            dick "Дорогая!
            Я...
            Эээээ..."
        if dickWaitingMonica3 == True:
            dick "Дорогая, пойдем в реторан!"
            "Или ты передумала?"
            return
        call change_scene("street_rich_hotel")
        return
    if obj_name == "Teleport_Restaurant":
        if richHotelReceptionEntered == False:
            call change_scene("rich_hotel_restaurant_entrance", "Fade", "highheels_short_walk")
#            m "Я не пойду туда. Ресторан уже закрыт."
            return
        if dickWaitingMonica3 == True:
            call dick_meeting1_restaurant_enter1()
        call change_scene("rich_hotel_restaurant", "Fade_long", "highheels_short_walk")
    return
label rich_hotel_reception_environment(obj_name, obj_data):
    if obj_name == "Clocks":
        m "Часы..."
        "Нью-Йорк, Токио, Лондон..."
        "А Париж? Где Париж? Я люблю Париж!!!"
    if obj_name == "Door":
        m "Какая-то дверь за рецепшином.
        Мне неинтересно что там!"
    if obj_name == "Flowers":
        m "Цветы... Похоже искусственные. Но я не буду трогать их чтобы проверить."
    if obj_name == "Jug1" or obj_name == "Jug2":
        m "Кувшин. На вид недорогой."
        "Это место меня не слишком впечатляет."
    if obj_name == "Tea":
        m "Чайник. Интересно, чай там холодный или нет? Хи-хи."
    if obj_name == "Desk":
        m "Стойка Администратора.
        Здесь мало места, видимо этот отель не слишком посещаемый."
        "Должно быть он очень дорогой...
        Или просто плохой..."
        "Администратора нет на месте. Впрочем я не удивлена."
        "Очередной никчемный бесполезный работник!"
    if obj_name == "Chair":
        m "На вид этот стул не слишком мягкий, но я не собираюсь его проверять!"
        "Я не собираюсь никого ждать на нем, это пусть меня все всегда ждут!"
    if obj_name == "Monica":
        if richHotelReceptionDickEnabled == True:
            if dickWaitingMonica4 == True:
                mt "Дик привел меня в пустой ресторан."
                "Замечательно!"
                return
            m "Это место меня не слишком впечатляет."
            "Но посмотрим как здесь внутри."
        m "Мой дом больше чем все номера вместе взятые в этом отеле!"
    if obj_name == "DickTheLawyer":
        if obj_data["action"] == "l":
            mt "Дик.
            Мой персональный адвокат."
            "Какой же он смешной!"
        if obj_data["action"] == "t":
            if dickWaitingMonica4 == True:
                $ richHotelReceptionMonicaDickTalkedOnExit = True
                m "Сначала ты меня привел в какую-то дыру, назвав ее магазином."
                "Теперь ты привел меня в пустой ресторан."
                "Дик, ты пытаешься произвести на меня впечатление этим?"
                dick "Дорогая!
                Я...
                Эээээ..."
                return
            call dick_meeting1_restaurant_reception_dialogue()
            return
    if obj_name == "ReceptionGirl":
        if obj_data["action"] == "l":
            mt "Администратор.
            Надо же, на рабочем месте!
            Фи!"
        if obj_data["action"] == "t":
            img 4694
            with fade
            reception "Мэм.
            Вы хотели бы заселиться?"
            m "Вот еще!
            Меня не интересует вам занюханный отель!"
    return
