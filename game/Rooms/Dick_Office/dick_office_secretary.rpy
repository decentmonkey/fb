default dickOfficeSecretaryMonicaStage = 0
default dickOfficeSecretaryMonicaStageGfx = 0
default dickOfficeSecretaryTalkedFlag1 = False
default dickOfficeSecretaryTalkedFlag2 = False

label dick_office_secretary:
    $ print "dick_office_secretary"
    $ miniMapData = []

    $ scene_name = "dick_office_secretary"
    $ scene_caption = _("Dick's Secretary")
    $ clear_scene_from_objects(scene_name)
    if dickOfficeSecretaryMonicaStageGfx == 0:
        $ scene_image = "scene_Office_Dick_Secretary_Monica_Secretary1_" + cloth
        $ add_object_to_scene("Monica", {"type":2, "base":"Office_Dick_Secretary_Monica_Secretary1_" + cloth + "_Monica", "click" : "dick_office_secretary_environment", "actions" : "l", "zorder" : 10})
        $ add_object_to_scene("Secretary", {"type":2, "base":"Office_Dick_Secretary_Monica_Secretary1_" + cloth + "_Secretary", "click" : "dick_office_secretary_environment", "actions" : "lt", "zorder" : 0})
    if dickOfficeSecretaryMonicaStageGfx == 1:
        $ scene_image = "scene_Office_Dick_Secretary_Monica_Secretary2_" + cloth
        $ add_object_to_scene("Monica", {"type":2, "base":"Office_Dick_Secretary_Monica_Secretary2_" + cloth + "_Monica", "click" : "dick_office_secretary_environment", "actions" : "l", "zorder" : 10})
        $ add_object_to_scene("Secretary", {"type":2, "base":"Office_Dick_Secretary_Monica_Secretary2_" + cloth + "_Secretary", "click" : "dick_office_secretary_environment", "actions" : "lt", "zorder" : 0})

    if dickOfficeSecretaryMonicaStageGfx == 0:
        $ add_object_to_scene("Computer", {"type":2, "base":"Office_Dick_Secretary_Computer", "click" : "dick_office_secretary_environment", "actions" : "l", "zorder" : 1})
        $ add_object_to_scene("Papers", {"type":2, "base":"Office_Dick_Secretary_Papers", "click" : "dick_office_secretary_environment", "actions" : "l", "zorder" : 1})
        $ add_object_to_scene("Phone", {"type":2, "base":"Office_Dick_Secretary_Phone", "click" : "dick_office_secretary_environment", "actions" : "l", "zorder" : 1})
        $ add_object_to_scene("Printer", {"type":2, "base":"Office_Dick_Secretary_Printer", "click" : "dick_office_secretary_environment", "actions" : "l", "zorder" : 1})
        $ add_object_to_scene("Terminal", {"type":2, "base":"Office_Dick_Secretary_Terminal", "click" : "dick_office_secretary_environment", "actions" : "l", "zorder" : 1})

    $ add_object_to_scene("Door", {"type":2, "base":"Office_Dick_Secretary_Door", "click" : "dick_office_secretary_teleport", "actions" : "lw", "zorder" : 0})

    $ add_object_to_scene("Teleport_Hall", {"type":3, "text" : _("НАЗАД В ХОЛЛ"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "dick_office_secretary_teleport", "xpos" : 960, "ypos" : 956, "zorder":11})
    return
    #                            $ brightness_adjustment = 0.1
    #                            $ saturation_adjustment = 1.07
    #                            $ contrast_adjustment = 1.3

label dick_office_secretary_teleport(obj_name, obj_data):
    if obj_name == "Teleport_Hall":
        if dickOfficeSecretaryMonicaStage == 9 and dickOfficeSecretaryTalkedFlag2 == False:
            call dickAfterJail_secretary_dialogue7a()
#            return
        call change_scene("dick_office_hall1")
        return
    if obj_name == "Door":
        if act == "l":
            if dickOfficeSecretaryMonicaStage == 0:
                mt "Дверь... за ней должен быть Дик..."
                return
            if dickOfficeSecretaryMonicaStage == 7:
                mt "Завтра???"
                "Дик будет только завтра?!?!"
                return
            if dickOfficeSecretaryMonicaStage == 8:
                mt "Мне плевать что эта сучка говорит."
                "Я силой ворвусь к нему!"
                return
            if dickOfficeSecretaryMonicaStage == 9:
                mt "Галстук..."
                mt "(хмык)"
                return
            mt "Дверь... мне надо дождаться Дика!"
#            mt "Дверь... Может быть Дик все-таки там?"

        if act == "w":
            if dickOfficeSecretaryMonicaStage == 0:
                call afterJail_Day2_DickOffice_Secretary_dialogue1()
                return
            if dickOfficeSecretaryMonicaStage == 3:
                img 2881
                with fade
                dick_secretary "Мэм. Вам надо придти попозже."
                return
            if dickOfficeSecretaryMonicaStage == 7:
                mt "Завтра???"
                "Дик будет только завтра?!?!"
                return

            if dickOfficeSecretaryMonicaStage == 8:
                call dickAfterJail_secretary_dialogue2()
                return

            if dickOfficeSecretaryMonicaStage == 9:
                mt "Галстук..."
                mt "(хмык)"
                return
            mt "Мне не пройти туда. Эта сучка секретарша сразу кричит и начинает куда-то звонить...");
            return
            call change_scene("dick_office_cabinet")
        return
    return
label dick_office_secretary_environment(obj_name, obj_data):
    if obj_name == "Monica":
        if dickOfficeSecretaryMonicaStage == 0:
            mt "Вот где сидит Дик!"
            "А это что за новая соска завелась здесь???"
            "Я ее впервые вижу!"
            return
        if dickOfficeSecretaryMonicaStage == 1:
            mt "Эта сучка много на себя берет!"
        if dickOfficeSecretaryMonicaStage == 2:
            mt "Тут негде ждать! Она издевается???"
            return
        if dickOfficeSecretaryMonicaStage == 3 or dickOfficeSecretaryMonicaStage == 5 or dickOfficeSecretaryMonicaStage == 6:
            mt "Я ВСЕ ВЫСКАЖУ ДИКУ ПО ПОВОДУ ЭТОЙ СУЧКИ!!!"
            "Я ДОБЬЮСЬ ЧТОБЫ ОН ЕЕ УВОЛИЛ!!!"
            return
        if dickOfficeSecretaryMonicaStage == 4:
            mt "Где там этот Дик???"
            return
        if dickOfficeSecretaryMonicaStage == 7:
            mt "Завтра???"
            "Дик будет только завтра?!?!"
            return
        if dickOfficeSecretaryMonicaStage == 8:
            mt "Я ВСЕ ВЫСКАЖУ ДИКУ ПО ПОВОДУ ЭТОЙ СУЧКИ!!!"
            "Я ДОБЬЮСЬ ЧТОБЫ ОН ЕЕ УВОЛИЛ!!!"
        if dickOfficeSecretaryMonicaStage == 9:
            mt "(хмык)"
            return

    if obj_name == "Secretary":
        if act == "l":
            if dickOfficeSecretaryMonicaStage == 0:
                "А это что за новая соска завелась здесь???"
                "Я ее впервые вижу!"
                return
            if dickOfficeSecretaryMonicaStage == 1:
                mt "Эта сучка много на себя берет!"
                return
            if dickOfficeSecretaryMonicaStage == 2:
                mt "Тут негде ждать! Она издевается???"
                return
            if dickOfficeSecretaryMonicaStage == 3 or dickOfficeSecretaryMonicaStage == 4 or dickOfficeSecretaryMonicaStage == 5 or dickOfficeSecretaryMonicaStage == 6 or dickOfficeSecretaryMonicaStage == 7 or dickOfficeSecretaryMonicaStage == 8:
                mt "Я ВСЕ ВЫСКАЖУ ДИКУ ПО ПОВОДУ ЭТОЙ СУЧКИ!!!"
                "Я ДОБЬЮСЬ ЧТОБЫ ОН ЕЕ УВОЛИЛ!!!"
                return
            if dickOfficeSecretaryMonicaStage == 9:
                mt "(хмык)"
                return
        if act == "t":
            if dickOfficeSecretaryMonicaStage == 0:
                call afterJail_Day2_DickOffice_Secretary_dialogue2()
                return
            if dickOfficeSecretaryMonicaStage == 1:
                mt "Мне надо устроиться удобно и подождать Дика..."
                return
            if dickOfficeSecretaryMonicaStage == 2:
                call afterJail_Day2_DickOffice_Secretary_dialogue4()
                return
            if dickOfficeSecretaryMonicaStage == 3:
                img 2881
                with fade
                dick_secretary "Мэм. Вам надо придти попозже."
                return
            if dickOfficeSecretaryMonicaStage == 4:
                call afterJail_Day2_DickOffice_Secretary_dialogue7()
                return
            if dickOfficeSecretaryMonicaStage == 5:
                img 2886
                with fade
                dick_secretary "Мэм."
                "Вам надо придти попозже."
                return
            if dickOfficeSecretaryMonicaStage == 6:
                call afterJail_Day2_DickOffice_Secretary_dialogue11()
                return

            if dickOfficeSecretaryMonicaStage == 7:
                img 2901
                with fade
                dick_secretary "Приходите завтра, Мэм."
                return

            if  dickOfficeSecretaryMonicaStage == 8:
                img 3074
                with fade
                dick_secretary "Прошу прощения, но я вынуждена отказать в посещении Мистера Дика."
                "Он доверяет мне первоначальную фильтрацию посетителей."
                img 3075
                "И я считаю вам не следует его беспокоить."
                return
            if dickOfficeSecretaryMonicaStage == 9:
                $ dickOfficeSecretaryTalkedFlag2 = True
                call dickAfterJail_secretary_dialogue7a()
                return

    if obj_name == "Computer":
        mt "Когда эта дура пялится в компьютер, выражение ее лица особенно глупое..."
    if obj_name == "Papers":
        if dickOfficeSecretaryMonicaStage == 0:
            mt "Какие-то никчемные бумажки!"
            return
        mt "Бумаги... может быть там есть телефон Дика?"
        "Но эта сучка не даст мне посмотреть!"
    if obj_name == "Phone":
        if dickOfficeSecretaryMonicaStage == 0:
            mt "Какой смешной старый телефон!"
            return
        mt "Телефон..."
        "Может быть там есть номер Дика?"
        "Но эта сучка не даст мне посмотреть!"
    if obj_name == "Printer":
        if dickOfficeSecretaryMonicaStage == 0:
            mt "Принтер..."
            return
        mt "Похоже здесь эта сучка печатает документы Дику на подпись."
    if obj_name == "Terminal":
        if dickOfficeSecretaryMonicaStage == 0:
            mt "Терминал?"
            return
        mt "Терминал?"
        "Для записи на прием?"
        "Эта сучка совсем не собирается работать сама???"
        "У меня нет времени на записи! Мне нужен Дик!"
        "СЕЙЧАС ЖЕ!!!"
    return
