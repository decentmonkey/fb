default hostelReceptionStage = 0
default hostelReceptionVisited = False
default hostelReceptionFlag1 = False

label hostel_reception:
    $ print "enter_hostel_reception"
    $ miniMapData = []

    $ scene_name = "hostel_reception"
    $ scene_caption = _("HOSTEL RECEPTION")
    $ clear_scene_from_objects(scene_name)

    if hostelReceptionStage == 0:
        $ scene_image = "scene_Hostel_Reception_Perry_Monica_AfterJail"
        $ add_object_to_scene("Monica", {"type":2, "base":"Hostel_Reception_Perry_Monica_AfterJail_Monica", "click" : "hostel_reception_environment", "actions" : "l", "zorder" : 10})
        $ add_object_to_scene("Perry", {"type":2, "base":"Hostel_Reception_Perry_Monica_AfterJail_Perry", "click" : "hostel_reception_environment", "actions" : "lt", "zorder" : 10})
    if hostelReceptionStage == 1 or hostelReceptionStage == 2:
        $ scene_image = "scene_Hostel_Reception_Perry_Monica2_AfterJail"
        $ add_object_to_scene("Monica", {"type":2, "base":"Hostel_Reception_Perry_Monica2_AfterJail_Monica", "click" : "hostel_reception_environment", "actions" : "l", "zorder" : 10})
        $ add_object_to_scene("Perry", {"type":2, "base":"Hostel_Reception_Perry_Monica2_AfterJail_Perry", "click" : "hostel_reception_environment", "actions" : "lt", "zorder" : 10})
    if hostelReceptionStage == 3:
        $ scene_image = "scene_Hostel_Reception_Perry_Monica3_AfterJail"
        $ add_object_to_scene("Monica", {"type":2, "base":"Hostel_Reception_Perry_Monica3_AfterJail_Monica", "click" : "hostel_reception_environment", "actions" : "l", "zorder" : 10})
        $ add_object_to_scene("Perry", {"type":2, "base":"Hostel_Reception_Perry_Monica3_AfterJail_Perry", "click" : "hostel_reception_environment", "actions" : "lt", "zorder" : 10})
    if hostelReceptionStage == 4:
        $ scene_image = "scene_Hostel_Reception_Perry_Monica4_AfterJail"
        $ add_object_to_scene("Monica", {"type":2, "base":"Hostel_Reception_Perry_Monica4_AfterJail_Monica", "click" : "hostel_reception_environment", "actions" : "l", "zorder" : 10})
        $ add_object_to_scene("Perry", {"type":2, "base":"Hostel_Reception_Perry_Monica4_AfterJail_Perry", "click" : "hostel_reception_environment", "actions" : "lt", "zorder" : 10})
    if hostelReceptionStage == 5:
        $ scene_image = "scene_Hostel_Reception_Perry_Monica5_AfterJail"
        $ add_object_to_scene("Monica", {"type":2, "base":"Hostel_Reception_Perry_Monica5_AfterJail_Monica", "click" : "hostel_reception_environment", "actions" : "l", "zorder" : 10})
        $ add_object_to_scene("Perry", {"type":2, "base":"Hostel_Reception_Perry_Monica5_AfterJail_Perry", "click" : "hostel_reception_environment", "actions" : "lt", "zorder" : 10})
    if hostelReceptionStage == 6:
        $ scene_image = "scene_Hostel_Reception_Perry_Monica3_AfterJail"
        $ add_object_to_scene("Monica", {"type":2, "base":"Hostel_Reception_Perry_Monica3_AfterJail_Monica", "click" : "hostel_reception_environment", "actions" : "l", "zorder" : 10})
        $ add_object_to_scene("Perry", {"type":2, "base":"Hostel_Reception_Perry_Monica3_AfterJail_Perry", "click" : "hostel_reception_environment", "actions" : "lt", "zorder" : 10})

    $ add_object_to_scene("Carpet", {"type":2, "base":"Hostel_Reception_Carpet", "click" : "hostel_reception_environment", "actions" : "l", "zorder" : 0})
    $ add_object_to_scene("Clock", {"type":2, "base":"Hostel_Reception_Clock", "click" : "hostel_reception_environment", "actions" : "l", "zorder" : 0, "b":0.13})
    $ add_object_to_scene("Door", {"type":2, "base":"Hostel_Reception_Door", "click" : "hostel_reception_environment", "actions" : "l", "zorder" : 0, "b":0.2})
    $ add_object_to_scene("Picture", {"type":2, "base":"Hostel_Reception_Picture", "click" : "hostel_reception_environment", "actions" : "l", "zorder" : 0, "b":0.13})
    $ add_object_to_scene("TV", {"type":2, "base":"Hostel_Reception_TV", "click" : "hostel_reception_environment", "actions" : "l", "zorder" : 0, "b":0.13})

    $ add_object_to_scene("Box1", {"type":2, "base":"Hostel_Reception_Box1", "click" : "hostel_reception_environment", "actions" : "lh", "zorder" : 0, "b":0.13})
    $ add_object_to_scene("Box2", {"type":2, "base":"Hostel_Reception_Box2", "click" : "hostel_reception_environment", "actions" : "lh", "zorder" : 0, "b":0.13})
    $ add_object_to_scene("Box3", {"type":2, "base":"Hostel_Reception_Box3", "click" : "hostel_reception_environment", "actions" : "lh", "zorder" : 0, "b":0.13})
    $ add_object_to_scene("Box4", {"type":2, "base":"Hostel_Reception_Box4", "click" : "hostel_reception_environment", "actions" : "lh", "zorder" : 0, "b":0.13})
    $ add_object_to_scene("Box5", {"type":2, "base":"Hostel_Reception_Box5", "click" : "hostel_reception_environment", "actions" : "lh", "zorder" : 0, "b":0.13})
    $ add_object_to_scene("Box6", {"type":2, "base":"Hostel_Reception_Box6", "click" : "hostel_reception_environment", "actions" : "lh", "zorder" : 0, "b":0.13})
    $ add_object_to_scene("Box7", {"type":2, "base":"Hostel_Reception_Box7", "click" : "hostel_reception_environment", "actions" : "lh", "zorder" : 0, "b":0.13})
    $ add_object_to_scene("Box8", {"type":2, "base":"Hostel_Reception_Box8", "click" : "hostel_reception_environment", "actions" : "lh", "zorder" : 0, "b":0.13})
    $ add_object_to_scene("Box9", {"type":2, "base":"Hostel_Reception_Box9", "click" : "hostel_reception_environment", "actions" : "lh", "zorder" : 0, "b":0.13})
    $ add_object_to_scene("Box10", {"type":2, "base":"Hostel_Reception_Box10", "click" : "hostel_reception_environment", "actions" : "lh", "zorder" : 0, "b":0.13})
    $ add_object_to_scene("Box11", {"type":2, "base":"Hostel_Reception_Box11", "click" : "hostel_reception_environment", "actions" : "lh", "zorder" : 0, "b":0.13})
#    $ add_object_to_scene("Box12", {"type":2, "base":"Hostel_Reception_Box12", "click" : "hostel_reception_environment", "actions" : "lh", "zorder" : 0, "b":0.13})
    $ add_object_to_scene("Box13", {"type":2, "base":"Hostel_Reception_Box13", "click" : "hostel_reception_environment", "actions" : "lh", "zorder" : 0, "b":0.13})
    $ add_object_to_scene("Box14", {"type":2, "base":"Hostel_Reception_Box14", "click" : "hostel_reception_environment", "actions" : "lh", "zorder" : 0, "b":0.13})
    $ add_object_to_scene("Box15", {"type":2, "base":"Hostel_Reception_Box15", "click" : "hostel_reception_environment", "actions" : "lh", "zorder" : 0, "b":0.13})
    $ add_object_to_scene("Box16", {"type":2, "base":"Hostel_Reception_Box16", "click" : "hostel_reception_environment", "actions" : "lh", "zorder" : 0, "b":0.13})
    $ add_object_to_scene("Box17", {"type":2, "base":"Hostel_Reception_Box17", "click" : "hostel_reception_environment", "actions" : "lh", "zorder" : 0, "b":0.13})

    $ add_object_to_scene("Computer", {"type":2, "base":"Hostel_Reception_Computer", "click" : "hostel_reception_environment", "actions" : "l", "zorder" : 0, "b":0.13})
    $ add_object_to_scene("Papers", {"type":2, "base":"Hostel_Reception_Papers", "click" : "hostel_reception_environment", "actions" : "l", "zorder" : 0, "b":0.13})
#    $ add_object_to_scene("Teleport_Hostel_1_a", {"type":2, "base":"hostel_reception_Teleport_Hostel_Edge_a", "click" : "hostel_reception_teleport", "actions" : "lw", "zorder" : 11, "b":0.13, "tint":[1.0, 1.0, 0.8]})

    $ add_object_to_scene("Teleport_Hostel_Street", {"type":3, "text" : _("НАЗАД НА УЛИЦУ"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "hostel_reception_teleport", "xpos" : 960, "ypos" : 956, "zorder":11})

    $ add_object_to_scene("Teleport_Hostel_Bedroom", {"type":3, "text" : _("ОБЩАЯ СПАЛЬНЯ"), "rarrow" : "arrow_right_2", "base":"Hostel_Reception_Teleport_Bedroom", "click" : "hostel_reception_teleport", "xpos" : 1500, "ypos" : 200, "zorder":15})


    $ hostelReceptionVisited = True
    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label hostel_reception_teleport(obj_name, obj_data):
    if obj_name == "Teleport_Hostel_Street":
        if hostelReceptionStage == 1:
            $ autorun_to_object("hostel_street", "hostelAfterJail_dialogue2")
        call change_scene("hostel_street", "Fade", "snd_jail_door")
        return
    if obj_name == "Teleport_Hostel_Bedroom":
        if hostelReceptionStage == 3:
            call hostelAfterJail_Perry_dialogue8()
            return

        if hostelReceptionStage < 4:
            call hostelAfterJail_Perry_dialogue1()
            return
        if hostelReceptionStage == 4:
            call hostelAfterJail_Perry_dialogue8b()
            return

        music snd_moderate_rain_music
        call change_scene("hostel_bedroom", "Fade", "snd_walk_barefoot")
        return
    return
label hostel_reception_environment(obj_name, obj_data):
    if obj_name == "Monica":
        if hostelReceptionStage == 0:
            mt "Фу! Что за место?"
            "Хорошо что мне здесь нужно провести всего одну ночь!"
            "Но даже на это у меня едва хватит сил!"
            return

        if hostelReceptionStage == 1:
            mt "Что эта рецепшионист себе позволяет?"
            "Я ведь могу уйти!"
            return
        if hostelReceptionStage == 2:
            mt "Эта Перри... Она хочет чтобы я сняла свое платье..."
            "Но у меня под ним ничего нет!"
            "Неужели я это сделаю?"
            "Но у меня нет выхода! Абсолютно нет выхода!!!"
            return
        if hostelReceptionStage == 3:
            call hostelAfterJail_Perry_dialogue7b()
            return
        if hostelReceptionStage == 4:
            mt "Я НЕ МОГУ ПОВЕРИТЬ!!!"
            "Я СТОЮ ЗДЕСЬ ГОЛАЯ И НА МЕНЯ СМОТРИТ ЭТО ВОЛОСАТОЕ..."
            "У МЕНЯ НЕТ СЛОВ!!!"
            "МОНИКА, Я ХОЧУ КОГО-НИБУДЬ УБИТЬ СЕЙЧАС!"
        if hostelReceptionStage == 5 or hostelReceptionStage == 6:
            mt "Мне надо переночевать и убираться из этой дыры!"
            "Здесь одни ненормальные, никчемные люди!!!"
            return

    if obj_name == "Perry":
        if act == "l":
            if hostelReceptionStage == 0:
                mt "Это кто? Такой рецепционист?"
                "Фи!"
            if hostelReceptionStage == 1:
                mt "Что эта рецепшионист себе позволяет?"
                "Я ведь могу уйти!"
            if hostelReceptionStage == 2:
                mt "Эта Перри... Она хочет чтобы я сняла свое платье..."
                "Но у меня под ним ничего нет!"
                "Неужели я это сделаю?"
                "Но у меня нет выхода! Абсолютно нет выхода!!!"
            if hostelReceptionStage == 3:
                mt "Эта Перри... Что она заставила меня сделать???"
                "Я отнюдь не уверена что поступила правильно!"
                "Но у меня нет выхода!"
                "Завтра все будет хорошо!"
                return
            if hostelReceptionStage == 4:
                mt "ОНА В СВОЕМ УМЕ???"
                "Я В ШОКЕ!!!"
            if hostelReceptionStage == 5 or hostelReceptionStage == 6:
                mt "Как эта Перри посмела мне предложить такое???"
                "Она ненормальная!!!"
                "НЕНОРМАЛЬНАЯ!!!"
        if act == "t":
            if hostelReceptionStage == 0:
                call hostelAfterJail_Perry_dialogue2()
                return
            if hostelReceptionStage == 1:
                call hostelAfterJail_Perry_dialogue3()
                return
            if hostelReceptionStage == 2:
                call hostelAfterJail_Perry_dialogue4()
                return
            if hostelReceptionStage == 3:
                call hostelAfterJail_Perry_dialogue8()
                return
            if hostelReceptionStage == 4:
                call hostelAfterJail_Perry_dialogue8a()
                return
            if hostelReceptionStage == 5 or hostelReceptionStage == 6:
                call hostelAfterJail_Perry_dialogue9()
                return



    if obj_name == "Fence":
        mt "Железный забор..."
        "Нет, я преодолею все заборы в моей жизни!!!"
        "Я не сдамся!!!"

    if obj_name == "Carpet":
        mt "Что за грязный ковер здесь?"
        "Фу!!!"
    if obj_name == "Clock":
        mt "Эти грязные часы, похоже, показывают правильно время только дважды раз в день..."
    if obj_name == "Door":
        mt "Что это там за дверь?"
        "Не похоже что это дверь ведет в спальни."
        "Там еще какие-то помещения?"
    if obj_name == "Picture":
        mt "Дешевая копия..."
    if obj_name == "Computer" or obj_name == "Papers":
        mt "Компьютеры, бумаги..."
        "Неужели в этой дыре есть бухгалтерский учет?"

    if obj_name == "TV":
        mt "Здесь есть работающий телевизор?"
        "Ах да, он не работает, все в порядке..."
    if obj_name == "Box1" or obj_name == "Box2" or obj_name == "Box3" or obj_name == "Box4" or obj_name == "Box5" or obj_name == "Box6" or obj_name == "Box7" or obj_name == "Box8" or obj_name == "Box9" or obj_name == "Box10" or obj_name == "Box11" or obj_name == "Box12":
        if act == "l":
            mt "Какая-то коробка..."
        if act == "h":
            if hostelReceptionStage == 2:
                perry "Не сюда! Справа от меня!"
                "Ты что, дура? Неудивительно что у тебя нет $10!!!"
                m "Но Перри, ты показала в ту сторону!"
                perry "Ты глухая? Я сказала справа от меня!"
                return
            perry "Эй! Не трогай мои коробки!"
    if obj_name == "Box13" or obj_name == "Box14" or obj_name == "Box15" or obj_name == "Box16":
        if act == "l":
            mt "Какая-то коробка..."
        if act == "h":
            if hostelReceptionStage == 2:
                perry "Не в эту коробку!"
                "В верхнюю!"
                return
            perry "Эй! Не трогай мои коробки!"
    if obj_name == "Box17":
        if act == "l":
            mt "Какая-то коробка..."
        if act == "h":
            if hostelReceptionStage == 2:
                call hostelAfterJail_Perry_dialogue7()
                return

            perry "Эй! Не трогай мои коробки!"

    return
