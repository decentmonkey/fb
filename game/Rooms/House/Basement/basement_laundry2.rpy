
#default laundryIroningBoardState = "Default"
#Clean, Dress, Dress_Ironed, Empty_Garbage, Iron

default laundry2_ironOnBoard = False
default laundry2_dressOnBoard = False
default laundry2_dressIroned = False
default laundry2_garbageOnBoard = True

default Iron_Board_Full_looked = False
default Dress_Ironed_looked = False

label basement_laundry2:
    $ print "enter_basement_laundry2"
    $ miniMapData = []
    call miniMapHouseGenerate()

    $ scene_name = "basement_laundry2"
    $ scene_caption = _("Laundry")
    $ clear_scene_from_objects(scene_name)

    if landryIroningActive == False:
        if laundry2_garbageOnBoard == True:
            $ add_object_to_scene("Rags1", {"type":2, "base":"Basement_Laundry2_Rags1", "click" : "basement_laundry2_environment", "actions" : "l", "zorder" : 0})
            $ add_object_to_scene("Iron_Board", {"type":2, "base":"Basement_Laundry2_Ironing_Board_Default", "click" : "basement_laundry2_environment", "actions" : "l", "zorder" : 0})
            $ laundryIroningBoardState = "Default"
        else:
            $ add_object_to_scene("Iron_Board_After_Iron", {"type":2, "base":"Basement_Laundry2_Ironing_Board_Clean", "click" : "basement_laundry2_environment", "actions" : "lh", "zorder" : 0})
            $ add_object_to_scene("Garbage", {"type":2, "base":"Basement_Laundry2_Garbage_Empty_Garbage", "click" : "basement_laundry2_environment", "actions" : "l", "zorder" : 0})
            $ add_object_to_scene("Garbage_Iron", {"type":2, "base":"Basement_Laundry2_Garbage_Empty_Garbage_Iron", "click" : "basement_laundry2_environment", "actions" : "l", "zorder" : 0})
            $ laundryIroningBoardState = "Empty_Garbage"
    else:
        if laundry2_garbageOnBoard == True:
            $ laundryIroningBoardState = "Default"
            $ add_object_to_scene("Rags1", {"type":2, "base":"Basement_Laundry2_Rags1", "click" : "basement_laundry2_environment", "actions" : "lh", "zorder" : 0})
            $ add_object_to_scene("Iron_Board", {"type":2, "base":"Basement_Laundry2_Ironing_Board_Default", "click" : "basement_laundry2_environment", "actions" : "lh", "zorder" : 0})
        else:
            if laundry2_dressIroned == False:
                if laundry2_ironOnBoard == False and laundry2_dressOnBoard == False:
                    $ laundryIroningBoardState = "Clean"
                    $ add_object_to_scene("Iron_Board", {"type":2, "base":"Basement_Laundry2_Ironing_Board_Clean", "click" : "basement_laundry2_environment", "actions" : "lh", "zorder" : 0})
                    $ add_object_to_scene("Garbage", {"type":2, "base":"Basement_Laundry2_Garbage_Clean", "click" : "basement_laundry2_environment", "actions" : "l", "zorder" : 0})
                if laundry2_ironOnBoard == False and laundry2_dressOnBoard == True:
                    $ laundryIroningBoardState = "Dress"
                    $ add_object_to_scene("Dress", {"type":2, "base":"Basement_Laundry2_Item_Dress", "click" : "basement_laundry2_environment", "actions" : "l", "zorder" : 0})
                    $ add_object_to_scene("Iron_Board", {"type":2, "base":"Basement_Laundry2_Ironing_Board_Dress", "click" : "basement_laundry2_environment", "actions" : "lh", "zorder" : 0})
                    $ add_object_to_scene("Garbage", {"type":2, "base":"Basement_Laundry2_Garbage_Clean", "click" : "basement_laundry2_environment", "actions" : "l", "zorder" : 0})
                if laundry2_ironOnBoard == True and laundry2_dressOnBoard == False:
                    $ laundryIroningBoardState = "Iron"
                    $ add_object_to_scene("Iron", {"type":2, "base":"Basement_Laundry2_Item_Iron", "click" : "basement_laundry2_environment", "actions" : "l", "zorder" : 0})
                    $ add_object_to_scene("Iron_Board", {"type":2, "base":"Basement_Laundry2_Ironing_Board_Iron", "click" : "basement_laundry2_environment", "actions" : "lh", "zorder" : 0})
                    $ add_object_to_scene("Garbage", {"type":2, "base":"Basement_Laundry2_Garbage_Clean", "click" : "basement_laundry2_environment", "actions" : "l", "zorder" : 0})
                if laundry2_ironOnBoard == True and laundry2_dressOnBoard == True:
                    $ laundryIroningBoardState = "Dress_and_Iron"
                    $ subst_to_object("Teleport_Basement_Laundry", "basement_laundry2_noexit")
                    $ add_object_to_scene("Iron_Board_Full", {"type":2, "base":"Basement_Laundry2_Ironing_Board_Full", "click" : "basement_laundry2_environment", "actions" : "lh", "zorder" : 0})
                    $ add_object_to_scene("Garbage", {"type":2, "base":"Basement_Laundry2_Garbage_Clean", "click" : "basement_laundry2_environment", "actions" : "l", "zorder" : 0})
            else:
                $ subst_to_object("Teleport_Basement_Laundry", False)
                $ laundryIroningBoardState = "Dress_Ironed"
                $ add_object_to_scene("Dress_Ironed", {"type":2, "base":"Basement_Laundry2_Item_Dress_Ironed", "click" : "basement_laundry2_environment", "actions" : "lh", "zorder" : 0})
                $ add_object_to_scene("Iron_Board_After_Iron", {"type":2, "base":"Basement_Laundry2_Ironing_Board_Dress_Ironed", "click" : "basement_laundry2_environment", "actions" : "lh", "zorder" : 0})
                $ add_object_to_scene("Garbage", {"type":2, "base":"Basement_Laundry2_Garbage_Empty_Garbage", "click" : "basement_laundry2_environment", "actions" : "l", "zorder" : 0})
                $ add_object_to_scene("Garbage_Iron", {"type":2, "base":"Basement_Laundry2_Garbage_Empty_Garbage_Iron", "click" : "basement_laundry2_environment", "actions" : "l", "zorder" : 0})


    $ scene_image = "scene_Laundry2_" + laundryIroningBoardState

#    $ add_object_to_scene("Accessories1", {"type":2, "base":"Basement_Laundry_Accessories1", "click" : "basement_laundry_environment", "actions" : "l", "zorder" : 0})
#    $ add_object_to_scene("Accessories2", {"type":2, "base":"Basement_Laundry_Accessories2", "click" : "basement_laundry_environment", "actions" : "l", "zorder" : 0})
#    $ add_object_to_scene("Basket1", {"type":2, "base":"Basement_Laundry_Basket1", "click" : "basement_laundry_environment", "actions" : "l", "zorder" : 0})
#    $ add_object_to_scene("Basket2", {"type":2, "base":"Basement_Laundry_Basket2", "click" : "basement_laundry_environment", "actions" : "l", "zorder" : 0})
#    $ add_object_to_scene("Cloth1", {"type":2, "base":"Basement_Laundry_Cloth1", "click" : "basement_laundry_environment", "actions" : "l", "zorder" : 0})
#    $ add_object_to_scene("Drying_Machine", {"type":2, "base":"Basement_Laundry_Drying_Machine", "click" : "basement_laundry_environment", "actions" : "l", "zorder" : 0})
#    $ add_object_to_scene("Rags1", {"type":2, "base":"Basement_Laundry_Rags1", "click" : "basement_laundry_environment", "actions" : "l", "zorder" : 0})
#    $ add_object_to_scene("Toilet_Paper", {"type":2, "base":"Basement_Laundry_Toilet_Paper", "click" : "basement_laundry_environment", "actions" : "l", "zorder" : 0})
#    $ add_object_to_scene("Towels1", {"type":2, "base":"Basement_Laundry_Towels1", "click" : "basement_laundry_environment", "actions" : "l", "zorder" : 0})
#    $ add_object_to_scene("Washer", {"type":2, "base":"Basement_Laundry_Washer", "click" : "basement_laundry_environment", "actions" : "l", "zorder" : 0})
#    $ add_object_to_scene("Clothes_Pin", {"type":2, "base":"Basement_Laundry_Clothes_Pin", "click" : "basement_laundry_environment", "actions" : "l", "zorder" : 0})

    $ add_object_to_scene("Clothes_Pin", {"type":2, "base":"Basement_Laundry2_Clothes_Pin", "click" : "basement_laundry_environment", "actions" : "l", "zorder" : 2})
    $ add_object_to_scene("Accessories1", {"type":2, "base":"Basement_Laundry2_Accessories1", "click" : "basement_laundry2_environment", "actions" : "l", "zorder" : 0})
    $ add_object_to_scene("Detergents", {"type":2, "base":"Basement_Laundry2_Detergents", "click" : "basement_laundry2_environment", "actions" : "l", "zorder" : 0})
    $ add_object_to_scene("Towels", {"type":2, "base":"Basement_Laundry2_Towels", "click" : "basement_laundry2_environment", "actions" : "l", "zorder" : 0})
    $ add_object_to_scene("Small_Boxes", {"type":2, "base":"Basement_Laundry2_Small_Boxes", "click" : "basement_laundry2_environment", "actions" : "l", "zorder" : 1})


    $ add_object_to_scene("Teleport_Box1", {"type":2, "base":"Basement_Laundry2_Box1", "click" : "basement_laundry2_teleport", "actions" : "l", "zorder" : 0})
    $ add_object_to_scene("Teleport_Box2", {"type":2, "base":"Basement_Laundry2_Box2", "click" : "basement_laundry2_teleport", "actions" : "l", "zorder" : 0})

    $ add_object_to_scene("Teleport_Basement_Laundry", {"type":3, "text" : _("НАЗАД"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "basement_laundry2_teleport", "xpos" : 510, "ypos" : 956, "zorder":11})

    return


label basement_laundry2_teleport(obj_name, obj_data):
    if obj_name == "Teleport_Basement_Laundry":
        call change_scene("basement_laundry") from _call_change_scene_36
        return
    if laundryBoxesActive == False:
        m "Мне ничего не надо в этом ящике."
        return
    if obj_name == "Teleport_Box1":
        call change_scene("basement_laundry2_box1", "Fade", "desk_open") from _call_change_scene_37
        return
    if obj_name == "Teleport_Box2":
        call change_scene("basement_laundry2_box2", "Fade", "desk_open") from _call_change_scene_38
        return
    return

label basement_laundry2_environment(obj_name, obj_data):
    if obj_name == "Garbage_Iron":
        m "Этот утюг какой-то плохой!"
        "Я обожглась из-за него!"

    if obj_name == "Iron_Board_After_Iron":
        m "Эта доска какая-то неровная!"
        "Я обожглась из-за нее!"
    if landryIroningActive == True:
        if obj_name == "Rags1":
            if obj_data["action"] == "l":
                m "Мне надо убрать этот хлам с гладильной доски."
                "Я не могу гладить когда на доске это!"
            if obj_data["action"] == "h":
                m "Сейчас я аккуратно уберу все что мне мешает..."
                $ laundry2_garbageOnBoard = False
                sound snd_iron_garbage
                $ scene_transition = "Fade"
                call refresh_scene() from _call_refresh_scene_3
                return

        if obj_name == "Garbage":
            m "Я постаралась убрать аккуратно как могла.
            Оно же мне мешало, в конце концов!"
            "Только попробуйте сказать мне что я неаккуратная!!!"

        if obj_name == "Iron_Board":
            if laundry2_ironOnBoard == False or laundry2_dressOnBoard == False or laundry2_dressIroned == False:
                if laundry2_garbageOnBoard == False:
                    m "Мне надо воспользоваться платьем и утюгом на этой доске, чтобы погладить платье."
                else:
                    m "Мне надо убрать этот хлам с гладильной доски."
                    "Я не могу гладить когда на доске что-то лежит!"
            return
        if obj_name == "Iron":
            m "Этим утюгом я собираюсь погладить платье."
            "САМА!!
            Представляете?"
        if obj_name == "Dress" and laundry2_dressIroned == False:
            m "Мятое платье.
            Надо его погладить."
        if obj_name == "Iron_Board_Full":
            if obj_data["action"] == "l":
                m "Ура!
                Я все нашла!
                Я молодец!"
                "Теперь осталось погладить платье."
                $ Iron_Board_Full_looked = True
            if obj_data["action"] == "h":
                if Iron_Board_Full_looked == False:
                    m "Ура!
                    Я все нашла!
                    Я молодец!"
                    "Теперь осталось погладить платье."
                m "Итак, гладим...."
                sound snd_ironing_1
                $ renpy.pause(4.0, hard=True)
                sound snd_ironing_2
                $ renpy.pause(3.0, hard=True)
                sound snd_woman_pain
                $ renpy.pause(1.0, hard=True)
                sound snd_iron_garbage
                $ autorun_to_object("basement_laundry2", "basement_laundry2_dress_ironed")
                $ laundry2_dressIroned = True
                $ scene_transition = "Fade"
                call refresh_scene() from _call_refresh_scene_4
                return

        if obj_name == "Dress_Ironed":
            if obj_data["action"] == "l":
                m "В конце концов получилось погладить платье."
                $ Dress_Ironed_looked = True
            if obj_data["action"] == "h":
                if Dress_Ironed_looked == False:
                    m "В конце концов получилось погладить платье."
                sound put_dress
                $ define_inventory_object("businesscloth1", {"description" : _("Красивое платье"), "label_suffix" : "_use_businesscloth", "default_label" : False, "default_nolabel" : "cant_use", "icon" : "Inventory/inv_businesscloth1" + res.suffix + ".png"})
                $ add_inventory("businesscloth1", 1, True)
                $ remove_objective("take_ironed_dress")
                $ add_objective("dress_businesscloth", _("Одеть платье у гардероба в спальне."), c_pink, 20)
                $ scene_transition = "Fade"
                $ autorun_to_object("basement_laundry2", "basement_laundry2_iron_taked")
                $ landryIroningActive = False
                $ businessClothNotFoundDay1 = False
                $ businessClothEnabled = True
                $ businessClothSearchDressInProgress = False
                call question_helper_disable()
                call refresh_scene() from _call_refresh_scene_5

#        return
    if obj_name == "Iron_Board":
        m "Гладильная доска."

    if obj_name == "Rags1":
        m "Какой-то хлам на гладильной доске."

    if obj_name == "Accessories1":
        m "Это различные хозяйственные приспособления."

    if obj_name == "Detergents":
        m "Кондиционеры и ароматизаторы для белья."
    if obj_name == "Towels":
        m "Просто полотенца..."
        "Лежат, здесь."
        "И мне плевать на них!!!"
    if obj_name == "Small_Boxes":
        m "Эти коробки слишком маленькие."
    return

label Iron_Board_use_crumpled_dress:
    if laundry2_garbageOnBoard != False:
        m "Мне надо убрать этот хлам с гладильной доски."
        "Я не могу гладить когда на доске что-то лежит!"
        return

    sound put_dress
    $ laundry2_dressOnBoard = True
    $ remove_inventory("crumpled_dress", 1, True)
    $ scene_transition = "Fade"
    call refresh_scene() from _call_refresh_scene_6
    return

label Iron_Board_use_iron:
    if laundry2_garbageOnBoard != False:
        m "Мне надо убрать этот хлам с гладильной доски."
        "Я не могу гладить когда на доске что-то лежит!"
        return

    sound snd_ui_connect
    $ laundry2_ironOnBoard = True
    $ remove_inventory("iron", 1, True)
    $ scene_transition = "Fade"
    call refresh_scene() from _call_refresh_scene_7
    return

label basement_laundry2_noexit(obj_name, obj_data):
    m "Я не уйду пока не поглажу это платье!!"
    return



label basement_laundry2_dress_ironed:
    m "Ай!!
    Я обожглась!!!"
    if juliaMonicaYell == True:
        m "Ну эта Юлия заплатит мне за это!!!"
    else:
        m "Почему Юлия его не погладила?"
    $ remove_objective("iron_dress")
    $ add_objective("take_ironed_dress", _("Забрать платье с гладильной доски"), c_white, 20)
return


label basement_laundry2_iron_taked:
    m "Теперь пойду в свою спальню.
    Одену платье."
    return

















    #
