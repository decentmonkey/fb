#default richHotelReceptionistMode = 0

label rich_hotel_reception_s2:

    $ print "enter_rich_hotel_reception_s2"
    $ miniMapData = []

    $ scene_name = "rich_hotel_reception_s2"
    $ scene_caption = _("Hotel Reception")
    $ clear_scene_from_objects(scene_name)

    if richHotelReceptionistMode == 1:
        $ scene_image = "scene_Rich_Hotel_Reception_Monica_Receptionist_AfterJail_1"
        $ add_object_to_scene("Monica", {"type":2, "base":"Rich_Hotel_Reception_Monica_Receptionist_AfterJail_1_Monica", "click" : "rich_hotel_reception_environment2", "actions" : "l", "zorder" : 10})
        $ add_object_to_scene("ReceptionGirl", {"type":2, "base":"Rich_Hotel_Reception_Monica_Receptionist_AfterJail_1_Reception", "click" : "rich_hotel_reception_environment2", "actions" : "lt", "zorder" : 10})
    if richHotelReceptionistMode == 2:
        $ scene_image = "scene_Rich_Hotel_Reception_Monica_Receptionist_AfterJail_2"
        $ add_object_to_scene("Monica", {"type":2, "base":"Rich_Hotel_Reception_Monica_Receptionist_AfterJail_2_Monica", "click" : "rich_hotel_reception_environment2", "actions" : "l", "zorder" : 10})
        $ add_object_to_scene("ReceptionGirl", {"type":2, "base":"Rich_Hotel_Reception_Monica_Receptionist_AfterJail_2_Reception", "click" : "rich_hotel_reception_environment2", "actions" : "lt", "zorder" : 10})


    $ add_object_to_scene("Logo", {"type":2, "base":"Rich_Hotel_Reception_Logo", "click" : "street_rich_hotel_environment2", "actions" : "l", "zorder" : 3, "tint":[1.0, 1.0, 0.3]})
    $ add_object_to_scene("Clocks", {"type":2, "base":"Rich_Hotel_Reception_Clocks", "click" : "rich_hotel_reception_environment2", "actions" : "l", "zorder" : 3})
    $ add_object_to_scene("Door", {"type":2, "base":"Rich_Hotel_Reception_Door", "click" : "rich_hotel_reception_environment2", "actions" : "l", "zorder" : 3, "b":0.15})
    $ add_object_to_scene("Flowers", {"type":2, "base":"Rich_Hotel_Reception_Flowers", "click" : "rich_hotel_reception_environment2", "actions" : "l", "zorder" : 3})
    $ add_object_to_scene("Jug1", {"type":2, "base":"Rich_Hotel_Reception_Jug1", "click" : "rich_hotel_reception_environment2", "actions" : "l", "zorder" : 3})
    $ add_object_to_scene("Jug2", {"type":2, "base":"Rich_Hotel_Reception_Jug2", "click" : "rich_hotel_reception_environment2", "actions" : "l", "zorder" : 3})
#    $ add_object_to_scene("Lamps", {"type":2, "base":"Rich_Hotel_Reception_Lamps", "click" : "rich_hotel_reception_environment", "actions" : "l", "zorder" : 3})
    $ add_object_to_scene("Tea", {"type":2, "base":"Rich_Hotel_Reception_Tea", "click" : "rich_hotel_reception_environment2", "actions" : "l", "zorder" : 15})
    $ add_object_to_scene("Desk", {"type":2, "base":"Rich_Hotel_Reception_Desk", "click" : "rich_hotel_reception_environment2", "actions" : "l", "zorder" : 3})
    $ add_object_to_scene("Chair", {"type":2, "base":"Rich_Hotel_Reception_Chair", "click" : "rich_hotel_reception_environment2", "actions" : "l", "zorder" : 3})

    $ add_object_to_scene("Teleport_Restaurant", {"type":3, "text" : _("РЕСТОРАН"), "rarrow" : "arrow_right_2", "base":"Rich_Hotel_Reception_Teleport_Restaurant", "click" : "rich_hotel_reception_teleport2", "xpos" : 1018, "ypos" : 103, "zorder":11})
    $ add_object_to_scene("Teleport_Street_Rich_Hotel", {"type":3, "text" : _("НАЗАД НА УЛИЦУ"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "rich_hotel_reception_teleport2", "xpos" : 960, "ypos" : 956, "zorder":11})

    music Groove2_85
    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label rich_hotel_reception_teleport2(obj_name, obj_data):
    if obj_name == "Teleport_Street_Rich_Hotel":
        call change_scene("street_rich_hotel")
        return
    if obj_name == "Teleport_Restaurant":
        if richHotelReceptionistMode == 1:
            mt "Сначала надо заселиться, потом пойду покушаю в ресторане..."
            return
        call change_scene("rich_hotel_restaurant_entrance", "Fade_long", "highheels_short_walk")
    return
label rich_hotel_reception_environment2(obj_name, obj_data):
    if obj_name == "Clocks":
        m "Часы..."
        "Нью-Йорк, Токио, Лондон..."
    if obj_name == "Door":
        m "Какая-то дверь за рецепшином."
    if obj_name == "Flowers":
        m "Цветы... Похоже искусственные. Но я не буду трогать их чтобы проверить."
    if obj_name == "Jug1" or obj_name == "Jug2":
        m "Кувшин. На вид недорогой."
    if obj_name == "Tea":
        m "Чайник. Как я соскучилась по горячему чаю!"
    if obj_name == "Desk":
        m "Стойка Администратора."
    if obj_name == "Chair":
        "Стул..."
    if obj_name == "Monica":
        if richHotelReceptionistMode == 1:
            mt "Этот отель вполне подойдет чтобы переночевать один раз."
            "Хоть он и не очень мне нравится."
            "Но что поделать, Моника?"
            "У тебя возникла небольшая проблема и теперь придется ночевать в этом отеле."
            "Мне приходится идти на такие жертвы!"
            "Кто-то дорого заплатит за это потом!"
        if richHotelReceptionistMode == 2:
            mt "Сучка!"
            "Тварь!"
            "НЕНАВИЖУ!!!"
            "Я УВОЛЮ ЕЕ, КЛЯНУСЬ!!!"
            return
    if obj_name == "ReceptionGirl":
        if obj_data["action"] == "l":
            if richHotelReceptionistMode == 1:
                mt "Администратор.
                Надо же, на рабочем месте!"
            if richHotelReceptionistMode == 2:
                mt "Сучка!"
                "Тварь!"
                "НЕНАВИЖУ!!!"
                "Я УВОЛЮ ЕЕ, КЛЯНУСЬ!!!"
                return
        if obj_data["action"] == "t":
            if richHotelReceptionistMode == 1:
                call after_jail_rich_hotel1()
                return
            if richHotelReceptionistMode == 2:
                mt "Я не собираюсь общаться с этой сучкой!"
                return

    return
