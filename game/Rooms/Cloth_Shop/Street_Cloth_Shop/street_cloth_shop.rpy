default bDickFollowingMonica = False
default whoresPlaceOpened = False

label street_cloth_shop:

    $ print "enter_street_cloth_shop"
    $ miniMapData = []

    $ scene_name = "street_cloth_shop"
    $ sceneIsStreet = True
    $ scene_caption = _("Clothing Shop")
    $ clear_scene_from_objects(scene_name)
    if bDickFollowingMonica == True:
        $ scene_image = "scene_Street_Cloth_Shop_Driver_Monica_DickTheLawyer_" + cloth + day_suffix
        $ add_object_to_scene("Car", {"type":2, "base":"Street_Cloth_Shop_Car", "click" : "street_house_main_yard_environment", "actions" : "l", "zorder" : 3})
        $ add_object_to_scene("Driver", {"type":2, "base":"Street_Cloth_Shop_Driver", "click" : "street_cloth_shop_environment", "actions" : "lt", "zorder" : 5, "icon_t":"/Icons/talk" + res.suffix +".png", "b":0.2, "s":1.3, "tint":[1.0, 1.0, 0.8]})
        $ add_object_to_scene("Monica", {"type":2, "base":"Street_Cloth_Shop_Driver_Monica_DickTheLawyer_Monica_" + cloth + day_suffix, "click" : "street_cloth_shop_environment", "actions" : "l", "zorder" : 12})
        $ add_object_to_scene("DickTheLawyer", {"type":2, "base":"Street_Cloth_Shop_Driver_Monica_DickTheLawyer_Dick" + day_suffix, "click" : "street_cloth_shop_environment", "actions" : "lt", "zorder" : 12, "icon_t":"/Icons/talk" + res.suffix +".png", "b":0.2, "s":1.3, "tint":[1.0, 1.0, 0.8]})

    else:
        if bFredFollowingMonica == True and map_scene == "Cloth_Shop":
            $ scene_image = "scene_Street_Cloth_Shop_Driver_Monica_" + cloth + day_suffix
            $ add_object_to_scene("Car", {"type":2, "base":"Street_Cloth_Shop_Car", "click" : "street_house_main_yard_environment", "actions" : "l", "zorder" : 3})
            $ add_object_to_scene("Driver", {"type":2, "base":"Street_Cloth_Shop_Driver", "click" : "street_cloth_shop_environment", "actions" : "lt", "zorder" : 5, "icon_t":"/Icons/talk" + res.suffix +".png", "b":0.2, "s":1.3, "tint":[1.0, 1.0, 0.8]})
            $ add_object_to_scene("Monica", {"type":2, "base":"Street_Cloth_Shop_Driver_Monica_" + cloth + day_suffix, "click" : "street_cloth_shop_environment", "actions" : "l", "zorder" : 10})
        else:
            $ scene_image = "scene_Street_Cloth_Shop_Monica_" + cloth + day_suffix
            $ add_object_to_scene("Monica", {"type":2, "base":"Street_Cloth_Shop_Monica_" + cloth + day_suffix, "click" : "street_cloth_shop_environment", "actions" : "l", "zorder" : 10})

    $ add_object_to_scene("Parking_Cash", {"type":2, "base":"Street_Cloth_Shop_Parking_Cash", "click" : "street_cloth_shop_environment", "actions" : "l", "zorder" : 0})
    $ add_object_to_scene("Trees", {"type":2, "base":"Street_Cloth_Shop_Trees", "click" : "street_cloth_shop_environment", "actions" : "l", "zorder" : 0})
#    $ add_object_to_scene("Teleport_Cloth_Shop_Entrance", {"type":3, "text" : _("Магазин Одежды"), "larrow" : "arrow_up", "base": "Street_Cloth_Shop_Teleport_Inside", "click" : "street_cloth_shop_teleport", "xpos" : 1746, "ypos" : 649, "zorder":11})
    $ add_object_to_scene("Teleport_Cloth_Shop_Entrance", {"type":3, "text" : _("Магазин Одежды"), "rarrow" : "arrow_right_2", "base": "Street_Cloth_Shop_Teleport_Inside", "click" : "street_cloth_shop_teleport", "xpos" : 835, "ypos" : 341, "zorder":11})

    if whoresPlaceOpened == True:
        $ add_object_to_scene("Teleport_Shawarma", {"type":3, "text" : _("Вверх по улице"), "rarrow" : "arrow_up_2", "base": "Street_Cloth_Shop_Teleport_Shawarma", "click" : "street_cloth_shop_teleport", "xpos" : 1705, "ypos" : 887, "zorder":11})
    return

#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label street_cloth_shop_teleport(obj_name, obj_data):
    if obj_name == "Teleport_Cloth_Shop_Entrance":
        if dickBuyDressInProgress == True and dickDressBrought == False:
            $ autorun_to_object("cloth_shop_view1", "dickBuyDressEnterShop")
        call change_scene("cloth_shop_view1", "Fade_long")
        return
    if obj_name == "Teleport_Shawarma":
        call change_scene("whores_place_shawarma", "Fade_long", "highheels_run2")
        return
    return
label street_cloth_shop_environment(obj_name, obj_data):
    if obj_name == "Parking_Cash":
        m "Парковочный автомат?"
        "Здесь что, много машин?
        В этой дыре!!!"
    if obj_name == "Trees":
        m "Милые деревья."
        "Это единственное что скрашивает ту дыру куда Дик привез меня!"
    if obj_name == "DickTheLawyer":
        if obj_data["action"] == "l":
            mt "Дик.
            Мой персональный адвокат."
            "Какой же он смешной!"
        if obj_data["action"] == "t":
            if dickWaitingMonica4 == True:
                dick "До встречи, Моника."
                "Буду ждать."
                return
            if dickMeeting1RestaurantPlanned == True:
                dick "Дорогая, нам надо торопиться."
                "Уже много времени."
                "Мы никуда не успеем."
                return
            if dickBuyDressInProgress == True:
                if dickDressBrought == False:
                    imgl Monica_HomeCloth1_Dick2
                    imgr Dick3
                    m "Дик! Куда ты привез меня?
                    Что это за дыра?"
                    dick "Дорогая, пойдем в магазин.
                    Я уверен мы что-нибудь подберем тебе!"
                    return
    if obj_name == "Monica":
        if gameStage == 3:
            if gameSubStage == 1:
                mt "Сейчас надо осторожно проникнуть в магазин, чтобы меня никто там не видел."
                return
            mt "Я не пойду в этот магазин. Это слишком опасно!"
            return
        if dickWaitingMonica4 == True:
            mt "Пусть сам добирается до дома!"
            return
        if dickMeeting1RestaurantPlanned == True:
            mt "Это лучший магазин из тех что открыт..."
            "Ну и дыра!"
            "Теперь он собирается везти меня в лучший ресторан из тех что октрыт?"
            return
        if dickBuyDressInProgress == True:
            if dickDressBrought == False:
                mt "Куда Дик привез меня?"
                "Разве я смогу что-то подобрать в этой дыре!?"
                return
        m "Дешевый магазин!
        В какой-то дыре!"

    if obj_name == "Driver":
        if obj_data["action"] == "l":
            call monica_looking_to_fred1()
            return
        if obj_data["action"] == "t":
            if dickWaitingMonica4 == True:
                $ dickWaitingMonica4 = False
                $ bDickFollowingMonica = False
                $ monicaEnterCarLookingCharacter = "Fred"
            if dickBuyDressInProgress == True:
                if dickDressBrought == False:
                    imgr Driver_Stand
                    fred "Мэм, вы готовы ехать?"
                    imgr Dick1
                    dick "Дорогая, мы еще не подобрали платье!
                    Пойдем в магазин!"
                    return
            call get_to_drive_dialogue()
            return

    return
