default laundryVisited = False
default clothesPinsSeen = False

default businessClothSearchDressInProgressLaundryVisited = False

default laundrySearchingForDress = False
default laundryDressFound = False
default laundrySearchingForIron = False
default laundryIronFound = False
default landryIroningActive = False

default laundryBoxesActive = True

default laundryIroningBoardState = "Default"

label basement_laundry:
    $ print "enter_basement_laundry"
    $ miniMapData = []
    call miniMapHouseGenerate()

    $ scene_name = "basement_laundry"
    $ scene_caption = _("Laundry")
    $ clear_scene_from_objects(scene_name)
    $ scene_image = "scene_Laundry1_" + laundryIroningBoardState
#    $ scene_image = "scene_Basement_Pool_Monica_BusinessCloth1"

#    $ add_object_to_scene("Monica", {"type" : 2, "base" : "Basement_Pool_Monica_" + cloth, "click" : "basement_pool_environment", "actions" : "l", "zorder":10, "tint": monica_tint})

#    $ add_object_to_scene("Bidet", {"type":2, "base":"Basement_Pool_Bidet", "click" : "basement_pool_environment", "actions" : "l", "zorder" : 0})
#    $ add_object_to_scene("Teleport_Floor1_Stairs", {"type":3, "text" : _("ЛЕСТНИЦА"), "rarrow" : "arrow_down_2", "base":"Basement_Pool_Door1", "click" : "basement_pool_teleport", "xpos" : 1043, "ypos" : 173, "zorder":0, "tint": [1.0, 1.0, 0.6]})
#    $ add_object_to_scene("Teleport_Basement_Laundry", {"type":3, "text" : _("ПРАЧЕЧНАЯ"), "larrow" : "arrow_left_2", "base":"Basement_Pool_Door2", "click" : "basement_pool_teleport", "xpos" : 1561, "ypos" : 408, "zorder":0, "tint": [1.0, 1.0, 0.6]})

    if businessClothSearchDressInProgress == True:
        $ add_object_to_scene("Accessories1", {"type":2, "base":"Basement_Laundry_Accessories1", "click" : "basement_laundry_environment", "actions" : "l", "zorder" : 0})
        $ add_object_to_scene("Accessories2", {"type":2, "base":"Basement_Laundry_Accessories2", "click" : "basement_laundry_environment", "actions" : "l", "zorder" : 0})
        $ add_object_to_scene("Basket1", {"type":2, "base":"Basement_Laundry_Basket1", "click" : "basement_laundry_environment", "actions" : "l", "zorder" : 0})
        $ add_object_to_scene("Basket2", {"type":2, "base":"Basement_Laundry_Basket2", "click" : "basement_laundry_environment", "actions" : "l", "zorder" : 0})
        $ add_object_to_scene("Cloth1", {"type":2, "base":"Basement_Laundry_Cloth1", "click" : "basement_laundry_environment", "actions" : "l", "zorder" : 0})
        $ add_object_to_scene("Drying_Machine", {"type":2, "base":"Basement_Laundry_Drying_Machine", "click" : "basement_laundry_environment", "actions" : "l", "zorder" : 0})
        $ add_object_to_scene("Rags1", {"type":2, "base":"Basement_Laundry_Rags1", "click" : "basement_laundry_environment", "actions" : "l", "zorder" : 0})
        $ add_object_to_scene("Toilet_Paper", {"type":2, "base":"Basement_Laundry_Toilet_Paper", "click" : "basement_laundry_environment", "actions" : "l", "zorder" : 0})
        $ add_object_to_scene("Towels1", {"type":2, "base":"Basement_Laundry_Towels1", "click" : "basement_laundry_environment", "actions" : "l", "zorder" : 0})
        $ add_object_to_scene("Washer", {"type":2, "base":"Basement_Laundry_Washer", "click" : "basement_laundry_environment", "actions" : "l", "zorder" : 0})
        $ add_object_to_scene("Clothes_Pin", {"type":2, "base":"Basement_Laundry_Clothes_Pin", "click" : "basement_laundry_environment", "actions" : "l", "zorder" : 0})



        $ add_object_to_scene("Teleport_Box1", {"type":2, "base":"Basement_Laundry_Box1", "click" : "basement_laundry_teleport", "actions" : "l", "zorder" : 0})
        $ add_object_to_scene("Teleport_Box2", {"type":2, "base":"Basement_Laundry_Box2", "click" : "basement_laundry_teleport", "actions" : "l", "zorder" : 0})
        $ add_object_to_scene("Teleport_Box3", {"type":2, "base":"Basement_Laundry_Box3", "click" : "basement_laundry_teleport", "actions" : "l", "zorder" : 0})
        $ add_object_to_scene("Teleport_Box4", {"type":2, "base":"Basement_Laundry_Box4", "click" : "basement_laundry_teleport", "actions" : "l", "zorder" : 0})
        $ add_object_to_scene("Teleport_Box5", {"type":2, "base":"Basement_Laundry_Box5", "click" : "basement_laundry_teleport", "actions" : "l", "zorder" : 0})
        $ add_object_to_scene("Teleport_Box6", {"type":2, "base":"Basement_Laundry_Box6", "click" : "basement_laundry_teleport", "actions" : "l", "zorder" : 0})

    if laundryVisited == False and businessClothSearchDressInProgress == False:
        $ autorun_to_object("basement_laundry", "basement_laundry_first_visit")

    if businessClothSearchDressInProgress == True:
        $ laundryVisited = True
        if businessClothSearchDressInProgressLaundryVisited == False:
            $ businessClothSearchDressInProgressLaundryVisited = True
            $ autorun_to_object("basement_laundry", "basement_laundry_dress_visit")
            $ laundrySearchingForDress = True
        $ add_object_to_scene("Teleport_Basement_Ironing_Board", {"type":3, "text" : _("ГЛАДИЛЬНАЯ ДОСКА"), "rarrow" : "arrow_down_2", "base": "Basement_Laundry_Teleport_Ironing_Board_" + laundryIroningBoardState, "click" : "basement_laundry_teleport", "xpos" : 1652, "ypos" : 555, "zorder":11})


    $ add_object_to_scene("Teleport_Basement_Hole", {"type":3, "text" : _("В ПОДВАЛ"), "larrow" : "arrow_dl", "base":"empty", "click" : "basement_laundry_teleport", "xpos" : 183, "ypos" : 873, "zorder":11})
    $ add_object_to_scene("Teleport_Basement_Pool", {"type":3, "text" : _("НАЗАД К БАССЕЙНУ"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "basement_laundry_teleport", "xpos" : 960, "ypos" : 956, "zorder":11})

    return

label basement_laundry_teleport(obj_name, obj_data):
    if obj_name == "Teleport_Basement_Pool":
        call change_scene("basement_pool") from _call_change_scene_39
        return
    if obj_name == "Teleport_Basement_Hole":
        if basementHoleRefuseFlag == True:
            call basement_hole_check()
            return
        $ basementHoleIncomingDirection = "Laundry"
        call change_scene("basement_hole")
        return
    if obj_name == "Teleport_Basement_Ironing_Board":
        call change_scene("basement_laundry2") from _call_change_scene_40
        return
    if laundryBoxesActive == False:
        m "Мне ничего не надо в этом ящике."
        return
    if obj_name == "Teleport_Box1":
        call change_scene("basement_laundry_box1", "Fade", "desk_open") from _call_change_scene_41
        return
    if obj_name == "Teleport_Box2":
        call change_scene("basement_laundry_box2", "Fade", "desk_open") from _call_change_scene_42
        return
    if obj_name == "Teleport_Box3":
        call change_scene("basement_laundry_box3", "Fade", "desk_open") from _call_change_scene_43
        return
    if obj_name == "Teleport_Box4":
        call change_scene("basement_laundry_box4", "Fade", "desk_open") from _call_change_scene_44
        return
    if obj_name == "Teleport_Box5":
        call change_scene("basement_laundry_box5", "Fade", "desk_open") from _call_change_scene_45
        return
    if obj_name == "Teleport_Box6":
        call change_scene("basement_laundry_box6", "Fade", "desk_open") from _call_change_scene_46
        return
    return

label basement_laundry_environment(obj_name, obj_data):
    if obj_name == "Accessories1":
        m "Какие-то щетки и моющие средства."
    if obj_name == "Accessories2":
        m "Какие-то гели и губки."
    if obj_name == "Clothes_Pin":
        m "ЧТО??"
        "Прищепки для белья?
        Деревянные???"

        "Юлия этим пользуется???"

        if clothesPinsSeen == False:
            menu:
                "Юлия деревенщина":
                    call bitch(5, "julia_basement_pins") from _call_bitch_23
                    m "Из какой провинциальной дыры вылезла эта нерадивая служанка?"
                    "Нужны-ли мне такие работники?
                    Большой вопрос!"

                "Юлия пользуется раритетными вещами":
                    call bitch(-5, "julia_basement_pins") from _call_bitch_24
                    m "Хм.. У Юлии есть определенный вкус к раритетным вещам.
                    Я тоже люблю все раритетное, но только роскошное."

                    "А эти прищепки...
                    Ну, не знаю..."

            $ clothesPinsSeen = True

    if obj_name == "Basket1":
        m "Эта корзина пустая."
    if obj_name == "Basket2":
        m "Мне не дотянуться до этих корзин.
        Что там в них?"
    if obj_name == "Washer":
        m "Машина для сушки белья..."
        "Пустая..."
    if obj_name == "Cloth1":
        m "Какие-то тряпки.
        Я не могу назвать это одеждой."
        "Наверное это что-то из одежды Юлии.
        Фи!"
    if obj_name == "Rags1":
        m "Какие-то тряпки.
        Это явно не мое платье!"
    if obj_name == "Toilet_Paper":
        m "Туалетная бумага?!
        И я тянулась туда чтобы об этом узнать?!"
    if obj_name == "Towels1":
        m "Какие-то полотенца, но мне толком не разглядеть отсюда."
    if obj_name == "Drying_Machine":
        m "Судя по всему это стиральная машина..."
        "Пустая..."

    return

label basement_laundry_first_visit:
    m "Это прачечная."
    m "Здесь гувернантка занимается своей работой."
    m"Я не понимаю что Я здесь забыла???"
    $ laundryVisited = True
    return

label basement_laundry_dress_visit:
    m "Хммм.. прачечная."

    "Возможно где-то здесь я найду свое платье..."

    call question_helper_enable("question_helper_laundry")


    return
