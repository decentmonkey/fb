label jail_day9:
    $ jailDay = 9
    $ day = day + 1
    $ jailDaySceneStage = 0
    $ jailScenePlace = 0
    $ policeCellStageName1 = "scene_Police_Cell_1_Day_9_1"
    $ policeCellStageName2 = "scene_Police_Cell_2_Day_6_2"
    $ policeCellMonica1 = "Police_Cell_1_Day_9_1"
    $ policeCellMonica2 = "Police_Cell_2_Day_6_2"
    $ policeCellMonicaLabel = "jail_day9_Monica"
    $ policeCellBedLabel = "jail_day9_Bed"
    $ policeCellCageLabel = "jail_day9_Cage"
    stop music fadeout 1.0
    call textonblack(_("ДЕНЬ 9"))
    img black_screen
    with Dissolve(1)
    music Jail_Clock

    img 2404
    with fadelong
    mt "Девятый день..."
    img 2405
    "Когда же я выберусь отсюда?"
    img 2406
    "Надеюсь этот жирный урод все сделает правильно."
    "И надеюсь эта дура в банке ничего не напортачит!"
    img 2407
    "Иначе она мне ответит за это!"
    "..."
    img 2408
    "Надо проверить вернулся этот кретин уже или нет?"
    call refresh_scene_fade()
    return

label jail_day9_Monica(obj_name, obj_data):
    if jailDaySceneStage == 0:
        mt "Надо проверить вернулся этот кретин уже или нет?"
    if jailDaySceneStage == 1:
        mt "МНЕ НАДО ЧТО-ТО ПРИДУМАТЬ!!!"
    if jailDaySceneStage == 2:
        mt "Надо позвать этого жирного слизняка..."
    if jailDaySceneStage == 3:
        mt "Надеюсь все получится... Должно получиться!!!"
    if jailDaySceneStage == 4:
        mt "Что им надо снова???"
        "Как они смеют звать меня?!?!"
        "Ублюдки!!!"
    if jailDaySceneStage == 5:
        if jailCageBlackmailEnded == True:
            mt "Как я их, а?"
            "Моника, ты умеешь поставить на место зарвавшихся мерзавцев!"
            "Ты молодец!"
            "Интересно, почему они так боятся шуметь при этом жирном слизняке?"
            "Но это и не важно!"
            "Меня это никак не касается!"
        else:
            mt "Какой ужас!"
            "Надеюсь это не зайдет слишком далеко, прежде чем я отсюда выберусь!"

    return

label jail_day9_Bed(obj_name, obj_data):
    if act == "l":
        call jail_day1_Bed(obj_name, obj_data)
        return

    if jailDaySceneStage == 0:
        mt "Некогда спать!"
    if jailDaySceneStage == 1:
        mt "МНЕ НАДО ЧТО-ТО ПРИДУМАТЬ!!!"
        menu:
            "ЛЕЧЬ И ДУМАТЬ! ДУМАТЬ!":
                pass
            "Не ложиться":
                return
        call jail_day9_2()
        return

    if jailDaySceneStage == 2:
        mt "Некогда спать!"
        return

    if jailDaySceneStage == 3:
        menu:
            "Лечь спать":
                pass
            "Не ложиться":
                return
        if jailCageBlackmailEnded == True:
            call jail_day10()
            return
        stop music fadeout 1.0
        call textonblack(_("Спустя некоторое время..."))
        music prison_yell_music
        img black_screen
        with Dissolve(1)
        img 2436
        with fadelong
        mt "Какой-то шум..."
        "..."
        prisoner1 "Эй! Шлюха!"
        "Иди сюда!"
        "Мы хотим видеть тебя!"
        $ jailDaySceneStage = 4
        return
    if jailDaySceneStage == 4:
        prisoner1 "Эй! Шлюха!"
        "Иди сюда!"
        "Мы хотим видеть тебя!"

    if jailDaySceneStage == 5:
        if jailCageBlackmailEnded == True:
            mt "Как я их, а?"
            "Моника, ты умеешь поставить на место зарвавшихся мерзавцев!"
            "Ты молодец!"
            "Интересно, почему они так боятся шуметь при этом жирном слизняке?"
            "Но это и не важно!"
            "Меня это никак не касается!"
        else:
            mt "Какой ужас!"
            "Надеюсь это не зайдет слишком далеко, прежде чем я отсюда выберусь!"
        menu:
            "Лечь спать":
                pass
            "Не ложиться":
                return
        call jail_day10()
    return

label jail_day9_Cage(obj_name, obj_data):
    if jailDaySceneStage == 4:
        call jail_day9_4()
        return
    if act == "l":
        call jail_cage_blackmail_day()
        call refresh_scene_fade()
        return
    if act == "w":
        $ cageInteractLabel = "jail_day9_Cage_Interact"
        call change_scene("police_jail_cage_scene")
        return

    return

label jail_day9_Cage_Interact:
    if jailDaySceneStage == 0:
        # приходит
        music Groove2_85
        img 2409
        with fadelong
        overseer "А!"
        "Я знаю!"
        "Небось жрать хочешь!"
        img 2410
        music Hidden_Agenda
        m "Да, Сэр."
        "Я бы очень хотела."
        "И еще я бы хотела узнать у Вас как Вы сходили в Банк?"
        if jailBoobsForFood == True:
            img 5214
            overseer "..."
            m "..."
            overseer "..."
            img 5215
            m "Что? Снова?!?!"
            m "Что ВАМ надо снова???"
            img 5214
            overseer "Сиськи..."
            img 5216
            m "Вы можете мне сказать как Вы сходили?"
            img 5217
            overseer "Нет. Сначала сиськи..."
            menu:
                "Сказать как его зовут." if monicaKnowOverseerName == True:
                    call jail_boobs_for_food_end()
                    img 2410
                    m "Сэр! Пожалуйста! Скажите, как Вы сходили?"
                "Показать грудь.":
                    # показывает грудь
                    call jail_boobs_for_food()
                    img 5228
                    m "Я думаю этого достаточно!"
                    m "Сэр! Пожалуйста! Скажите, как Вы сходили?"
                "Не показывать.":
                    m "Я не хочу показывать свою грудь..."
                    img 5173
                    overseer "Нет вежливости, нет сисек, нет еды..."
                    img 5116
                    w
                    # уходит
                    music Jail_Clock
                    call refresh_scene_fade()
                    return


        music Power_Bots_Loop
        overseer "Плохо!"
        img 2411
        m "Сэр, но что случилось?"
        "Вам не дали бумаги на подпись?"
        overseer "Сейчас принесу баланду, потом скажу!"
        "Ишь какая шустрая!"

        # уходит
        music Power_Bots_Loop
        img 2412
        with fadelong
        mt "Что там могло случиться?"
        "Этому идиоту ничего нельзя доверить!"
        "Он тупой как пробка!"
        "О Боже!"
        "За что мне все это???"

        # приходит
        music Groove2_85
        img 2413
        with fadelong
        overseer "На, жри!"
        $ jailFoodInteractLabel = "jail_day9_1a"
        call change_scene("police_jail_food_scene", "Fade", False)
        return

    if jailDaySceneStage == 1:
        img 2253
        with fadelong
        mt "Он не подходит."
        "Может быть попробовать еще раз попозже?"
#        call jail_cage_blackmail_day()
        return

    if jailDaySceneStage == 2:
        call jail_day9_3()
        return
    if jailDaySceneStage == 3:
        img 2253
        with fadelong
        mt "Он не подходит."
        "Может быть он вообще ушел?"
        "Мне не видно отсюда!"
        call jail_cage_blackmail_day()
        return
    if jailDaySceneStage == 5:
        img 2253
        with fadelong
        mt "Никого нет..."
        return
    return

label jail_day9_1a:
    music Groove2_85
    img 2414
    with fadelong
    m "Сэр."
    "Спасибо!"
    "Очень вкусно!"
    "А теперь пожалуйста!"
    "Скажите что там в Банке?"
    img 2415
    overseer "Я пришел туда значит."
    "Там сидят бабы с такими сиськами, Во!"
    img 2416
    m "Сэр, я понимаю."
    "Пожалуйста, давайте перейдем к делу."
    "Что Вам сказали там?"
    "Почему что-то не получилось?"
    img 2417
    overseer "Я значит дал ей эту бумажку."
    "Которую ты написала."
    "Она посмотрела в своем телевизоре и говорит."
    "..."
    img 2416
    m "Что говорит, Сэр?!"
    img 2417
    overseer "Говорит что счета твои все арестованы и что на них ничего нет."
    music Power_Bots_Loop
    img 2418
    with fade
    mt "НЕЕЕЕЕЕЕЕЕТ!!!"
    $ money = 0.0
    img 2419
    overseer "Так что я и ушел."
    "Ты мне надоела."
    "Пудришь мне мозги какими-то умными словечками, писульками."
    "А я хожу туда-сюда только за зря."
    img 2420
    "А у меня голова болит."

    img 2421
    m "Да, Сэр."
    "Спасибо."
    "Я поняла."
    "Простите."
    img 2422
    mt "МНЕ НАДО ЧТО-ТО ПРИДУМАТЬ!!!"
    music Jail_Clock
    $ jailDaySceneStage = 1
    $ policeCellStageName1 = "scene_Police_Cell_1_Day_9_2"
    $ policeCellStageName2 = "scene_Police_Cell_2_Day_6_2"
    $ policeCellMonica1 = "Police_Cell_1_Day_9_2"
    $ policeCellMonica2 = "Police_Cell_2_Day_6_2"
    call refresh_scene_fade()
    return

label jail_day9_2:
    music Hidden_Agenda
    img 2423
    with fadelong
    mt "Есть идея!"
    "У меня же есть дом!"
    "Арестовали наверняка только счета и деньги!"
    "Я уверена что недвижимости это еще не коснулось!"
    img 2424
    "Раньше он принадлежал мужу."
    "Но недавно я через знакомую риелтора провернула схему."
    "И переписала дом на себя."
    img 2425
    "Про это вообще никто не знает."
    "Надо отправить этого жирного урода к ней."
    "Она все сделает как надо!"

    $ jailDaySceneStage = 2
    call refresh_scene_fade()
    return

label jail_day9_3:
    #
    music Groove2_85
    img 2426
    with fadelong
    overseer "Знаешь что?"
    "Я тебя сегодня кормил!"
    "Ты все время стучишь и стучишь!"
    "Как ты появилась, так у меня голова вообще не проходит!"
    img 2427
    "Можешь ты сидеть тихо как все остальные?"
    "Они шумят лишь иногда!"
    "А ты все время!"
    music Hidden_Agenda
    img 2428
    m "..."
    "Сэр."
    "Простите."
    "Я придумала как достать деньги."

    music Groove2_85
    overseer "Ты уже придумывала сколько раз."
    "Ничего не выходит!"
    "Мне надоело ходить!"

    music Hidden_Agenda
    m "Сэр!"
    "Ну пожалуйста!"
    "Последний раз!"
    "На Вас запишут огромный дом в пригороде!"
    "Это целый дворец!"
    img 2429
    overseer "Дворец говоришь?"
    "А если не запишут?"
    img 2428
    m "Сэр!"
    "Это точно!"
    "Я Вам клянусь!"

    if jailBoobsForFood == True:
        overseer "..."
        m "..."
        overseer "..."
        img 5229
        m "Что? Снова?!?!"
        m "Почему Вы снова на меня так смотрите?"
        img 5230
        overseer "Сиськи..."
        img 5231
        m "Я вам уже показывала сегодня их!"
        overseer "Еще..."
        img 5232
        mt "О БОЖЕ!!!"
        menu:
            "Показать грудь.":
                # показывает грудь
                call jail_boobs_for_food()
            "Не показывать.":
                m "Я не хочу показывать свою грудь..."
                overseer "Нет вежливости, нет сисек, я никуда не хожу..."
                # уходит
                music Jail_Clock
                call refresh_scene_fade()
                return
#        m "Сэр!"
#        "Ну пожалуйста!"
#        "Последний раз!"

    if jailBoobsForFood == False:

        img 2429
        overseer "Ну..."
        "Ладно."
        "Но последний раз!"
        "Ежели что не так, то пиняй на себя!"
        img 2430
        m "Сэр!"
        "Все будет хорошо!"

        music Pyro_Flow
        img 2431
        with fade
        mt "Потому что зависеть будет не от тебя, а от риелтора, жирный урод!!!"
        "Ты обязательно бы все испортил!!!"

        music Hidden_Agenda
        img 2432
        with fade
        m "Сэр."
        "Пожалуйста, принесите бумагу."
        "Мне надо написать записку для риелтора."
        "Она переоформит дом на Вас!"
        overseer "Ладно..."
        "Сейчас..."
        # уходит
        stop music fadeout 1.0
        call textonblack(_("Спустя 5 минут..."))
        img black_screen
        with Dissolve(1)

        music Groove2_85
        # приходит
        img 2433
        with fadelong
        overseer "На!"
        "Пиши!"
        sound snd_pen_writing
        img black_screen
        with Dissolve(1)
        $ renpy.pause(3.0)
    else:
        img 5256
        with fadelong
        m "Теперь Вы не можете отказать мне в том что я прошу..."
        img 2429
        overseer "Ну..."
        "Ладно."
        "Но последний раз!"
        "Ежели что не так, то пиняй на себя!"
        img 5256
        m "Все будет хорошо!"

        music Pyro_Flow
        img 2431
        with fade
        mt "Потому что зависеть будет не от тебя, а от риелтора, жирный урод!!!"
        "Ты обязательно бы все испортил!!!"

#        music Hidden_Agenda
        music Groove2_85
        img 5257
        with fade
        m "Сэр."
        "Пожалуйста, принесите бумагу."
        "Мне надо написать записку для риелтора."
        "Она переоформит дом на Вас!"
        overseer "Ладно..."
        "Сейчас..."
        img 5116
        w
        # уходит
        stop music fadeout 1.0
        call textonblack(_("Спустя 5 минут..."))
        img black_screen
        with Dissolve(1)

        music Groove2_85
        img 5117
        with fadelong
        w
        # приходит
        img 2433
        overseer "На!"
        "Пиши!"
        sound snd_pen_writing
        img black_screen
        with Dissolve(1)
        $ renpy.pause(3.0)

    img 2434
    with fadelong
    m "Вот, Сэр!"
    "Вы можете придти по этому адресу и спросить этого человека."
    "В бумаге все указано!"
    overseer "Ладно. Завтра схожу."
    "А сейчас ВСЕ!"

    music Jail_Clock
    $ jailDaySceneStage = 3
    call refresh_scene_fade()
    return

label jail_day9_4:
    call jail_cage_blackmail()
    return
