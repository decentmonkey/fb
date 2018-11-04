label floor1:
    $ print "enter_floor1"
    $ miniMapData = []
    call miniMapHouseGenerate()

    $ scene_name = "floor1"
    $ scene_caption = _("Hall Ground Floor")
    $ clear_scene_from_objects(scene_name)
    $ monica_tint = [1.0, 1.0, 1.0]
    if (cloth_type == "Lingerie" or cloth_type == "HomeCloth"):
        $ monica_tint = [0.9, 0.9, 1.0]

    $ scene_image = "scene_Floor1_Monica_" + cloth + day_suffix

    $ add_object_to_scene("Monica", {"type" : 2, "base" : "Floor1_Monica_" + cloth, "click" : "floor1_environment", "actions" : "l", "zorder":10, "tint": monica_tint})


    $ add_object_to_scene("Chandelier", {"type":2, "base":"Floor1_Chandelier", "click" : "floor1_environment", "actions" : "l", "zorder" : 1})
    $ add_object_to_scene("Curtains", {"type":2, "base":"Floor1_Curtains", "click" : "floor1_environment", "actions" : "l", "zorder" : 0, "b":0.15})
    $ add_object_to_scene("Lamps", {"type":2, "base":"Floor1_Lamps", "click" : "floor1_environment", "actions" : "l", "zorder" : 0})
    $ add_object_to_scene("Windows", {"type":2, "base":"Floor1_Windows", "click" : "floor1_environment", "actions" : "l", "zorder" : 0})
    $ add_object_to_scene("Picture", {"type":2, "base":"Floor1_Picture", "click" : "floor1_environment", "actions" : "l", "zorder" : 0})
    $ add_object_to_scene("Fountain", {"type":2, "base":"Floor1_Fountain_Object", "click" : "floor1_environment", "actions" : "lw", "zorder" : 1, "b":0.03})

    $ add_object_to_scene("Furniture", {"type":2, "base":"Floor1_Furniture", "click" : "floor1_environment", "actions" : "l", "zorder" : 0})


    if (juliaPunished == False or juliaMonicaForgivenessAfterPunishment == True) and juliaLocation == "floor1":
        $ add_object_to_scene("Julia", {"type" : 2, "base" : "Floor1_Julia1", "click" : "julia_interact", "actions" : "lt", "zorder":10})
        $ add_object_to_scene("Furniture", {"type":2, "base":"Floor1_Furniture_Julia1", "click" : "floor1_environment", "actions" : "l", "zorder" : 0})
#        $ add_object_to_scene("Furniture2", {"type":2, "base":"Floor1_Furniture2_Julia1", "click" : "floor1_environment", "actions" : "l", "zorder" : 11})


    if gameStage >= 3:
        $ add_object_to_scene("Teleport_LivingRoom", {"type":3, "text" : _("ГОСТИНАЯ"), "rarrow" : "arrow_right_2", "base":"empty", "click" : "floor1_teleport", "xpos" : 1594, "ypos" : 306, "zorder":9, "b":0.15, "tint":[1.0, 1.0, 0.9]})
        if bardieLocation == "Floor1":
            $ add_object_to_scene("Bardie", {"type" : 2, "base" : "Floor1_Bardie" + day_suffix, "click" : "bardieInteract1", "actions" : "lw", "zorder":10})
        if ralphLocation == "Floor1":
            $ add_object_to_scene("Ralph", {"type" : 2, "base" : "Floor1_Ralph" + day_suffix, "click" : "ralphInteract1", "actions" : "lt", "zorder":10, "icon_t":"/Icons/talk" + res.suffix +".png"})

    $ add_object_to_scene("Teleport_Floor1_Stairs", {"type":3, "text" : _("ЛЕСТНИЦА"), "larrow" : "arrow_left_2", "base":"Floor1_Stairs_Object", "click" : "floor1_teleport", "xpos" : 367, "ypos" : 219, "zorder":9, "b":0.15, "tint":[1.0, 1.0, 0.9]})
    $ add_object_to_scene("Teleport_Kitchen", {"type":3, "text" : _("КУХНЯ"), "larrow" : "arrow_left_2", "base":"Floor1_Teleport_Kitchen", "click" : "floor1_teleport", "xpos" : 130, "ypos" : 758, "zorder":9, "b":0.2})
    $ add_object_to_scene("Teleport_Street", {"type":3, "text" : _("НА УЛИЦУ"), "rarrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "floor1_teleport", "xpos" : 960, "ypos" : 956, "zorder":11, "high_sprite_hover": True})

#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

    return


label floor1_teleport(obj_name, obj_data):
    if obj_name == "Teleport_Floor1_Stairs":
        call change_scene("floor1_stairs") from _call_change_scene_9
    if obj_name == "Teleport_Kitchen":
        call change_scene("kitchen") from _call_change_scene_10
    if obj_name == "Teleport_LivingRoom":
        call change_scene("living_room")
        return
    if obj_name == "Teleport_Street":
        jump house_out

    return


label floor1_environment(obj_name, obj_data):
    if obj_name == "Monica":
        if gameStage > 2:
            m "Они захватили мой дом, но я верну его!"
            return
        m "Этот этаж выполнен в других цветах нежели верхний.
        Однообразие - это... скучно."

    if obj_name == "Furniture" or obj_name == "Furniture2":
        m "Эту мебель изготавливал один итальянский мастер.

        Очень известный."

        "Бедняга так влюбился в меня, а я разбила ему сердце."

        if gameStage > 2:
            m "Интересно где он сейчас?"
            "Он бы мне очень пригодился..."
            return

        "А на что еще он мог рассчитывать?
        Хи-хи."

    if obj_name == "Chandelier":
        m "Эта люстра стоит целое состояние."

        "И я боюсь ходить под ней."

        if gameStage > 2:
            m "Когда я верну себе дом, я перевешу эту люстру..."
            return

        "Я, почему-то, с детства боюсь таких больших люстр.
        Мне кажется что она может упасть."

        "Глупости, конечно, но я решила повесить ее над фонтаном."

    if obj_name == "Curtains":
        if gameStage > 2:
            m "Мои шторы..."
            "(хмык)"
            return
        m "Эти шторы плотнее чем те что висят в моей спальне."

        "Если их занавесить, солнца не будет совсем."

        "Но я не собираюсь их занавешивать."

        "Мне нечего скрывать, я живу публичной жизню."

        "И веду себя очень прилично."

    if obj_name == "Lamps":
        if gameStage > 2:
            "Когда я верну свой дом, я сделаю здесь еще больше света!"
            return

        m "Эти светильники горят, ну, вы знаете почему."

        "Повторять я не собираюсь.
        Фи!"

    if obj_name == "Windows":
        if day_time == "day":
            m "Снаружи солнечный двор."
            if gameStage > 2:
                m "Пока что не мой, но только ПОКА!"
                return

            "За моим окном всегда хорошая погода!
            Потому что я сама выбирала место где купить дом!"

        if day_time == "evening":
            m "За окнами темно."

            "Уже вечер!"
    if obj_name == "Picture":
        m "Эту картину кто-то подарил моему мужу."
        if gameStage > 2:
            m "Интересно, где мой муж?"
            return

        "Видимо это что-то важное для него."

        "Думаю надо поменять ее на что-то более подходящее под фон для фонтана."

    if obj_name == "Fountain":
        if obj_data["action"] == "l":
            if gameStage > 2:
                m "Мой фонтан..."
                "Эххххх..."
                return
            m "Этот фонтанчик замечательно вписывается в интерьер!"

            "Это была моя идея."

            "И мне без разницы сколько стоило установить его здесь."

            "Ведь строение дома это не предусматривало."

            "Но причем тут предусматривало или нет.
            Какие-то деньги, суммы и тд...
            ЕСЛИ Я ХОЧУ!"

        if obj_data["action"] == "w":
            call change_scene("floor1_fountain", "Fade", "snd_fountain") from _call_change_scene_12
            return

    return
