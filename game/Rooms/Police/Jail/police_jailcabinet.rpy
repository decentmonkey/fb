default jailCabinetState = 0
default jailCabinetMonicaStanding = True
default jailCabinetMonicaPunished = False

label police_jailcabinet:
    $ print "enter_police_jailcabinet"
    $ miniMapData = []

    $ scene_name = "police_jailcabinet"
    $ scene_caption = _("Interrogation Room")
    $ clear_scene_from_objects(scene_name)

    if jailCabinetState == 0 or jailCabinetState == 1 or jailCabinetState == 2 or jailCabinetState == 3 or jailCabinetMonicaStanding == False:
        if jailCabinetMonicaStanding == True:
            $ scene_image = "scene_Police_JailCabinet_Monica_Marcus_1"
            $ add_object_to_scene("Marcus", {"type":2, "base":"Police_JailCabinet_Monica_Marcus_1_Marcus", "click" : "police_jailcabinet_environment", "actions" : "lt", "zorder" : 9, "icon_t":"/Icons/talk" + res.suffix +".png"})
            $ add_object_to_scene("Monica", {"type":2, "base":"Police_JailCabinet_Monica_Marcus_1_Monica", "click" : "police_jailcabinet_environment", "actions" : "l", "zorder" : 10})
        else:
            $ scene_image = "scene_Police_JailCabinet_Monica_Marcus_2"
            $ add_object_to_scene("Marcus", {"type":2, "base":"Police_JailCabinet_Monica_Marcus_1_Marcus", "click" : "police_jailcabinet_environment", "actions" : "lt", "zorder" : 9, "icon_t":"/Icons/talk" + res.suffix +".png"})
            $ add_object_to_scene("Monica", {"type":2, "base":"Police_JailCabinet_Monica_Marcus_2", "click" : "police_jailcabinet_environment", "actions" : "l", "zorder" : 10})

    if (jailCabinetState == 4 or jailCabinetState == 5) and jailCabinetMonicaStanding == True:
        $ scene_image = "scene_Police_JailCabinet_Monica_Marcus_3"
        $ add_object_to_scene("Marcus", {"type":2, "base":"Police_JailCabinet_Monica_Marcus_3_Marcus", "click" : "police_jailcabinet_environment", "actions" : "lt", "zorder" : 9, "icon_t":"/Icons/talk" + res.suffix +".png"})
        $ add_object_to_scene("Monica", {"type":2, "base":"Police_JailCabinet_Monica_Marcus_3_Monica", "click" : "police_jailcabinet_environment", "actions" : "l", "zorder" : 10})


    if jailCabinetMonicaStanding == True and jailCabinetState != 4:
        $ add_object_to_scene("Chair", {"type":2, "base":"Police_JailCabinet_Chair", "click" : "police_jailcabinet_environment", "actions" : "lh", "zorder" : 0, "b":0.13, "s":1.3, "tint":[1.0, 1.0, 0.8]})
    else:
        $ add_object_to_scene("Chair", {"type":2, "base":"Police_JailCabinet_Chair", "click" : "police_jailcabinet_environment", "actions" : "l", "zorder" : 0, "b":0.13, "s":1.3, "tint":[1.0, 1.0, 0.8]})
    $ add_object_to_scene("Lamp", {"type":2, "base":"Police_JailCabinet_Lamp", "click" : "police_jailcabinet_environment", "actions" : "l", "zorder" : 0, "b":0.13, "s":1.3, "tint":[1.0, 1.0, 0.8]})
    $ add_object_to_scene("Table", {"type":2, "base":"Police_JailCabinet_Table", "click" : "police_jailcabinet_environment", "actions" : "l", "zorder" : 0, "b":0.13, "s":1.3, "tint":[1.0, 1.0, 0.8]})
    $ add_object_to_scene("Teleport_Jail_Cabinet2", {"type":3, "text" : _("ДВЕРЬ"), "larrow" : "arrow_down_2", "base":"empty", "click" : "police_jailcabinet_teleport", "xpos" : 1523, "ypos" : 969, "zorder":5})

    return

label police_jailcabinet2:
    $ print "enter_police_jailcabinet2"
    $ miniMapData = []

    $ scene_name = "police_jailcabinet2"
    $ scene_caption = _("Interrogation Room")
    $ clear_scene_from_objects(scene_name)

    $ scene_image = "scene_Police_JailCabinet2_Monica_Marcus_1"

    $ add_object_to_scene("Marcus", {"type":2, "base":"Police_JailCabinet2_Monica_Marcus_1_Marcus", "click" : "police_jailcabinet2_environment", "actions" : "l", "zorder" : 9, "icon_t":"/Icons/talk" + res.suffix +".png"})
    $ add_object_to_scene("Monica", {"type":2, "base":"Police_JailCabinet2_Monica_Marcus_1_Monica", "click" : "police_jailcabinet2_environment", "actions" : "l", "zorder" : 10})

    $ add_object_to_scene("Chair", {"type":2, "base":"Police_JailCabinet2_Chair", "click" : "police_jailcabinet_environment", "actions" : "lh", "zorder" : 0, "b":0.13, "s":1.3, "tint":[1.0, 1.0, 0.8]})
    $ add_object_to_scene("Door", {"type":2, "base":"Police_JailCabinet2_Door", "click" : "police_jailcabinet2_environment", "actions" : "lh", "zorder" : 0, "b":0.13, "s":1.3, "tint":[1.0, 1.0, 0.8]})
    $ add_object_to_scene("Teleport_Jail_Cabinet", {"type":3, "text" : _("СТОЛ"), "larrow" : "arrow_down_2", "base":"empty", "click" : "police_jailcabinet_teleport", "xpos" : 326, "ypos" : 986, "zorder":5})

    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label police_jailcabinet_teleport(obj_name, obj_data):
    if obj_name == "Teleport_Jail_Cabinet2":
        call change_scene("police_jailcabinet2")
        return
    if obj_name == "Teleport_Jail_Cabinet":
        $ jailCabinetMonicaStanding = True
        call change_scene("police_jailcabinet")
        return


    return
label police_jailcabinet_environment(obj_name, obj_data):
    if obj_name == "Monica":
        mt "О БОЖЕ!!!"
        "Мне очень страшно!!!"
#        "Как мне выбраться отсюда???"
    if obj_name == "Chair":
        if act == "l":
            if jailCabinetMonicaStanding == True:
                img 2517
                with fade
                mt "Жуткий ржавый стул!..."
                "Маркус сказал чтобы я села на него..."
            else:
                mt "Этот стул просто ледяной."
                "И мне больно сидеть на нем..."
        if act == "h":
            $ jailCabinetMonicaStanding = False
            call change_scene("police_jailcabinet", "Fade", False)
            return
    if obj_name == "Lamp":
        mt "Какая ядовитая лампа..."
        "Почему здесь так темно?"
    if obj_name == "Table":
        mt "Какой жуткий ржавый стол..."
        "Неужели Мистер Маркус работает за ним?..."

    if obj_name == "Marcus":
        if act == "l":
            mt "Этот Маркус... Это очень страшный человек..."
            "Я его очень боюсь! Что он еще может со мной сделать?"
            "Я даже не представляю! Мне страшно!"
        if act == "t":
            if jailCabinetState == 5:
#                $ bitchmeterValue = 1000 #debug
                label police_jailcabinet_menu_loop1:
                    menu:
                        "Ты мерзкий ублюдок! Жалкое существо!!! (наказание)" if bitchmeterValue > maxBitchness / 2:
                            call jail_cabinet_punishment()
                            return
                        "Ты мерзкий ублюдок! Жалкое существо!!! (наказание) (Моника слишком добрая) (disabled)" if bitchmeterValue <= maxBitchness / 2:
                            jump police_jailcabinet_menu_loop1
                        "...":
                            pass
            if jailCabinetMonicaStanding == True and jailCabinetState != 4:
                marcus "Миссис Бакфетт."
                "Не отвлекайтесь."
                "Присаживайтесь и продолжим."
                return
            if jailCabinetState == 0:
                call jail_cabinet_dialogue2()
                return
            if jailCabinetState == 1:
                call jail_cabinet_dialogue3()
                return
            if jailCabinetState == 2:
                call jail_cabinet_dialogue4()
                return
            if jailCabinetState == 3:
                call jail_cabinet_dialogue5()
                return
            if jailCabinetState == 4:
                call jail_cabinet_dialogue6()
                return
            if jailCabinetState == 5:
                call jail_cabinet_dialogue7()
                return

            return


    return
label police_jailcabinet2_environment(obj_name, obj_data):
    if obj_name == "Marcus":
        mt "Этот Маркус... Это очень страшный человек..."
        "Я его очень боюсь! Что он еще может со мной сделать?"
        "Я даже не представляю! Мне страшно!"
    if obj_name == "Monica":
        mt "Как мне выбраться отсюда?"
        mt "О БОЖЕ!!!"
        "(хмык)"
    if obj_name == "Door":
        if act == "l":
            mt "Эта дверь... Может быть я могу выбраться через нее?"
        if act == "h":
            sound snd_jail_door_locked
            $ renpy.pause(1.0)
            sound snd_jail_door_locked
            $ renpy.pause(1.0)
            sound snd_jail_door_locked
            $ renpy.pause(1.0)
            marcus "Миссис Бакфетт. Дверь заперта."
            "Не отвлекайтесь."
            "Присаживайтесь и продолжим."


    return
