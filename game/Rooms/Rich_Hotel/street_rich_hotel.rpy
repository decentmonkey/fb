default richHotelClosed1 = False

label street_rich_hotel:

    $ print "enter_street_rich_hotel"
    $ miniMapData = []

    $ scene_name = "street_rich_hotel"
    $ sceneIsStreet = True
    $ scene_caption = _("Hotel La Grand")
    $ clear_scene_from_objects(scene_name)
    if bFredFollowingMonica == True:
        $ scene_image = "scene_Street_Rich_Hotel_Driver" + day_suffix
        $ add_object_to_scene("Car", {"type":2, "base":"Street_Rich_Hotel_Car", "click" : "street_house_main_yard_environment", "actions" : "l", "zorder" : 3, "b":0.14})
        $ add_object_to_scene("Driver", {"type":2, "base":"Street_Rich_Hotel_Driver", "click" : "street_rich_hotel_environment", "actions" : "lt", "zorder" : 2, "icon_t":"/Icons/talk" + res.suffix +".png", "b":0.2, "s":1.3, "tint":[1.0, 1.0, 0.8]})
    else:
        $ scene_image = "scene_Street_Rich_Hotel" + day_suffix

    $ add_object_to_scene("Logo", {"type":2, "base":"Street_Rich_Hotel_Logo", "click" : "street_rich_hotel_environment", "actions" : "l", "zorder" : 3, "tint":[1.0, 1.0, 0.3]})
    $ add_object_to_scene("Building", {"type":2, "base":"Street_Rich_Hotel_Building", "click" : "street_rich_hotel_environment", "actions" : "l", "zorder" : 3})
    $ add_object_to_scene("Teleport_Rich_Hotel_Reception", {"type":2, "base":"Street_Rich_Hotel_Teleport_Inside", "click" : "street_rich_hotel_teleport", "actions" : "lw", "zorder" : 3, "b":0.17, "c":1.5})

    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label street_rich_hotel_teleport(obj_name, obj_data):
    if obj_name == "Teleport_Rich_Hotel_Reception":
        if obj_data["action"] == "l":
            if gameStage == 2:
                mt "Вход в отель..."
                return
            m "А это, видимо, вход в якобы роскошный ресторан..."
        if obj_data["action"] == "w":
            if gameStage == 3:
                mt "Я еще не сошла с ума, чтобы идти в такой дорогой отель одетой в ЭТО!!!"
                return
#            if dickWaitingMonica4 == True:
#                m "Я не пойду туда. Ресторан уже закрыт."
#                return
#            if richHotelClosed1 == True:
#                m "Мне нечего сейчас там делать, Фи!"
#                return
            call change_scene("rich_hotel_reception")
        return
    return
label street_rich_hotel_environment(obj_name, obj_data):
    if obj_name == "Building":
        m "Это и есть Hotel La Grand?"
        if day_time == "evening":
            m "Вечером он выглядит довольно эффектно."
        else:
            m "Днем он тоже выглядит неплохо."
        m "Это не небоскреб, в нем нет какого-то величия."
        "Но смотрится он очень мило."
        "По крайней мере это не дыра!...
        На вид..."
        if dickWaitingMonica2 == True:
            call dick_waiting_monica_dialogue2Short()
    if obj_name == "Logo":
        m "La Grand?"
        "Как банально..."
        if dickWaitingMonica2 == True:
            call dick_waiting_monica_dialogue2Short()
    if obj_name == "Driver":
        if obj_data["action"] == "l":
            call monica_looking_to_fred1()
            if dickWaitingMonica2 == True:
                call dick_waiting_monica_dialogue2Short()
                return
        if obj_data["action"] == "t":
            if dickWaitingMonica4 == True:
                call dick_meeting1_car_parting2()
                return
            if dickWaitingMonica2 == True:
                call dick_waiting_monica_dialogue2()
                return
            call get_to_drive_dialogue()
            return

    return
