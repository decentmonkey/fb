default journalTaken = False
default journalViewed = False
default hairDyeTaken = False
default hairDyeSearchMode = False
default Hairdye_looked = False

label floor2_mirrors:
    $ print "enter_floor2_mirrors"
    $ miniMapData = []
    call miniMapHouseGenerate()

    $ scene_name = "floor2_mirrors"
    $ scene_caption = _("Mirrors")
    $ clear_scene_from_objects(scene_name)
    $ scene_image = "scene_Floor2_Mirrors"
    if hairDyeTaken == True:
        $ scene_image = "scene_Floor2_Mirrors_no_hair_dye" + day_suffix

    $ add_object_to_scene("Ink1", {"type":2, "base":"Floor2_Mirrors_Ink1", "click" : "floor2_mirrors_environment2", "actions" : "l", "zorder" : 0})
    $ add_object_to_scene("Bottle1", {"type":2, "base":"Floor2_Mirrors_Bottle1", "click" : "floor2_mirrors_environment2", "actions" : "l", "zorder" : 0})
    $ add_object_to_scene("Pomade1", {"type":2, "base":"Floor2_Mirrors_Pomade1", "click" : "floor2_mirrors_environment2", "actions" : "l", "zorder" : 0})
    $ add_object_to_scene("Perfume1", {"type":2, "base":"Floor2_Mirrors_Perfume1", "click" : "floor2_mirrors_environment2", "actions" : "l", "zorder" : 0})
    $ add_object_to_scene("Shadows1", {"type":2, "base":"Floor2_Mirrors_Shadows1", "click" : "floor2_mirrors_environment2", "actions" : "l", "zorder" : 0})
    $ add_object_to_scene("Shadows2", {"type":2, "base":"Floor2_Mirrors_Shadows2", "click" : "floor2_mirrors_environment2", "actions" : "l", "zorder" : 0})
    $ add_object_to_scene("Cosmetics", {"type":2, "base":"Floor2_Mirrors_Cosmetics", "click" : "floor2_mirrors_environment2", "actions" : "l", "zorder" : 0})
    $ add_object_to_scene("Perfume2", {"type":2, "base":"Floor2_Mirrors_Perfume2", "click" : "floor2_mirrors_environment2", "actions" : "l", "zorder" : 0})
    $ add_object_to_scene("Perfume2", {"type":2, "base":"Floor2_Mirrors_Perfume2", "click" : "floor2_mirrors_environment2", "actions" : "l", "zorder" : 0})
    $ add_object_to_scene("Mirror2", {"type":2, "base":"Floor2_Mirrors_Mirror2", "click" : "floor2_mirrors_environment2", "actions" : "l", "zorder" : 0})
    if hairDyeTaken == False:
        if hairDyeSearchMode == False:
            $ add_object_to_scene("Hairdye", {"type":2, "base":"Floor2_Mirrors_HairDye", "click" : "floor2_mirrors_environment2", "actions" : "l", "zorder" : 0})
        else:
            $ add_object_to_scene("Hairdye", {"type":2, "base":"Floor2_Mirrors_HairDye", "click" : "floor2_mirrors_environment2", "actions" : "lh", "zorder" : 0})


    if journalTaken == False:
        $ add_object_to_scene("Journal", {"type":2, "base":"Floor2_Mirrors_Journal", "click" : "floor2_mirrors_environment", "actions" : "lh", "zorder" : 0})


    $ add_object_to_scene("Teleport_Floor2", {"type":3, "text" : _("НАЗАД"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "floor2_mirrors_teleport", "xpos" : 960, "ypos" : 956, "zorder":11})
    return

#    $ add_object_to_scene("Mirrors", {"type":2, "base":"Floor2_Mirrors", "click" : "floor2_environment", "actions" : "l", "zorder" : 0})
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label floor2_mirrors_teleport(obj_name, obj_data):
    if obj_name == "Teleport_Floor2":
        call change_scene("floor2") from _call_change_scene_25
        return

label floor2_mirrors_environment2(obj_name, obj_data):
#ink1, bottle1, pomade1, perfume1, shadows1, shadows2, cosmetics, perfume2, hairdye
    if obj_name == "Mirror2":
        m "Как же я люблю любоваться собой!

        Я - совершенство!"

    if obj_name == "Ink1":
        m "Это тушь для ресниц."

        "Я нечасто пользуюсь ей.
        Мои ресницы и так очень длинные и изящные."

    if obj_name == "Bottle1":
        m "Это увлажняющий спрей для лица."

    if obj_name == "Pomade1":
        m "Помада."

        "Я люблю яркие тона, но не очень вызывающие."

    if obj_name == "Perfume1":
        m "Мои любимые духи."

        "Их шлейф сводит с ума любого мужчину."

        "Хи-хи."


    if obj_name == "Shadows1":
        m "Это тени."

    if obj_name == "Shadows2":
        m "Это тени."

    if obj_name == "Cosmetics":
        m "Одна из моих многочисленных косметичек."

        m "Я нечасто пользуюсь косметикой.
        Я и так отлично выгляжу."

        "Мне не надо рисовать лицо.
        Посмотрите на меня.
        Я сегодня не красилась, но выгляжу прекрасно!"

    if obj_name == "Perfume2":
        m "Эти духи я использую для массовых мероприятий.

        Они очень нейтральные, чтобы не привлекать излишнее внимание мужчин."

        "Которое мне совершенно не нужно!"

    if obj_name == "Hairdye":
        if obj_data["action"] == "l" or obj_data["action"] == "":
            m "Краска для волос."

            "Не понимаю зачем она здесь."

            "Я не крашу волосы."

            "Эта вещь здесь определенно лишняя!"

            $ Hairdye_looked = True

            if julia_monica_revenge_in_progress == True:
                "Ее как раз можно использовать для того чтобы куда-нибудь разлить!"

        if obj_data["action"] == "h":
            m "Краска для волос."
            if Hairdye_looked == False:
                "Не понимаю зачем она здесь."

                "Я не крашу волосы."

                "Эта вещь здесь определенно лишняя!"

            m "Если ее разлить, то ее просто невозможно будет оттереть!"

            "Как раз то что мне надо."

            "Возьму-ка я ее.
            Хи-хи."

            $ add_inventory("hairdye", 1, True)
            $ hairDyeTaken = True
            $ hairDyeSearchMode = False
            call floor2_julia_monica_revenge_hair_dye_taken() from _call_floor2_julia_monica_revenge_hair_dye_taken
            call change_scene("floor2_mirrors", "Fade", "glass_click") from _call_change_scene_26
            return
    return


label floor2_mirrors_environment(obj_name, obj_data):
    if obj_name == "Journal":
        if obj_data["action"] == "l":
            m "А что это лежит сбоку от зеркала?"

            m "Да это же выпуск моего журнала!"

            $ journalViewed = True

        if obj_data["action"] == "h":
            imgc fashion2
            $ add_inventory("journal", 1, True)
            $ journalTaken = True

            if journalViewed == False:
                m "А что это лежит сбоку от зеркала?"

                "Да это же выпуск моего журнала!"

            m "Этот выпуск особенный."

            "Его украшает мой образ."

            "Как я смотрюсь на ней?"

            "По-моему, потрясающе!"

            "Как владелец журнала, я могу позволить себе такие мелочи."

            "Такие как быть на обложке самого модного журнала."

            "Хи-хи."
            w
            call change_scene("floor2_mirrors", "Fade", "snd_take_paper") from _call_change_scene_27
            return

    return
