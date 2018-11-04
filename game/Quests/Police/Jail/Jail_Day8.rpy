label jail_day8:
    $ jailDay = 8
    $ day = day + 1
    $ jailDaySceneStage = 0
    $ jailScenePlace = 0
    $ policeCellStageName1 = "scene_Police_Cell_1_Day_8_1"
    $ policeCellStageName2 = "scene_Police_Cell_2_Day_6_2"
    $ policeCellMonica1 = "Police_Cell_1_Day_8_1"
    $ policeCellMonica2 = "Police_Cell_2_Day_6_2"
    $ policeCellMonicaLabel = "jail_day8_Monica"
    $ policeCellBedLabel = "jail_day8_Bed"
    $ policeCellCageLabel = "jail_day8_Cage"
    stop music fadeout 1.0
    call textonblack(_("ДЕНЬ 8"))
    img black_screen
    with Dissolve(1)
    music Jail_Clock

    img 2379
    with fadelong
    mt "Итак."
    img 2380
    mt "Кажется у меня что-то наклевывается."
    "Надеюсь этот жирный урод уже сходил ко мне на работу."
    img 2381
    "Надо проверить."
    call refresh_scene_fade()
    return

label jail_day8_Monica(obj_name, obj_data):
    if jailDaySceneStage == 0:
        mt "Надеюсь этот жирный урод уже сходил ко мне на работу."
        "Надо проверить."
    if jailDaySceneStage == 1:
        mt "Мне надо придумать еще что-то!"
    if jailDaySceneStage == 2:
        mt "Надо отправить его в банк!"
    if jailDaySceneStage == 3:
        mt "Пора спать..."
    if jailDaySceneStage == 4:
        mt "Что им надо???"
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

label jail_day8_Bed(obj_name, obj_data):
    if act == "l":
        call jail_day1_Bed(obj_name, obj_data)
        return

    if jailDaySceneStage == 0:
        mt "Некогда спать!"
    if jailDaySceneStage == 1:
        mt "Мне надо придумать еще что-то!"
        menu:
            "Лечь и думать":
                pass
            "Не ложиться":
                return
        $ jailScenePlace = 0
        call jail_day8_2()

        return
    if jailDaySceneStage == 2:
        mt "Некогда спать!"

    if jailDaySceneStage == 3:
        menu:
            "Лечь спать":
                pass
            "Не ложиться":
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
        call jail_day9()
    return

label jail_day8_Cage(obj_name, obj_data):
    if jailDaySceneStage == 4:
        call jail_day8_4()
        return
    if act == "l":
        if jailDaySceneStage == 5:
            call jail_cage_blackmail_day()
            call refresh_scene_fade()
            return
        call jail_cage()
        call refresh_scene_fade()
        return
    if act == "w":
        if jailDaySceneStage == 1:
            mt "Мне надо сначала что-то придумать!"
            return
        $ cageInteractLabel = "jail_day8_Cage_Interact"
        call change_scene("police_jail_cage_scene")
        return

    return

label jail_day8_Cage_Interact:
    if jailDaySceneStage == 0:
        #
        music Groove2_85
        # подходит
        img 2382
        with fadelong
        overseer "Чего тебе?"
        "Жрать?"
        img 2383
        music Hidden_Agenda
        m "Сэр."
        "Это, конечно, было бы хорошо."
        "Но я бы хотела также узнать по поводу того как Вы сходили?"
        if jailBoobsForFood == True:
            overseer "..."
            m "..."
            overseer "..."
            img 5200
            m "Что? Снова?!?!"
            img 5201
            m "Что ВАМ надо снова???"
            overseer "Сиськи..."
            img 5202
            m "Вы можете мне сказать как Вы сходили?"
            img 5201
            overseer "Нет. Сначала сиськи..."
            menu:
                "Сказать как его зовут." if monicaKnowOverseerName == True:
                    call jail_boobs_for_food_end()
                "Показать грудь.":
                    # показывает грудь
                    call jail_boobs_for_food()
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
            img 2383
            m "Сэр! Пожалуйста! Скажите, как Вы сходили?"

        music Groove2_85
        overseer "Плохо!"

        m "Почему?"
        overseer "Сейчас принесу еду скажу!"
        # уходит
        img 5116
        with fade
        w
        img black_screen
        with Dissolve(1)
        img 5118
        with fadelong
        w
        # приходит
        $ jailFoodInteractLabel = "jail_day8_1a"
        call change_scene("police_jail_food_scene", "Fade", False)
    if jailDaySceneStage == 1 or jailDaySceneStage == 3 or jailDaySceneStage == 5:
        img 2253
        with fadelong
        mt "Никого нет..."

    if jailDaySceneStage == 2:
        call jail_day8_3()
        return
    return

label jail_day8_1a:

    music Groove2_85
    img 2384
    with fadelong
    m "Сэр!"
    "Я поела. Очень вкусно!"
    "Спасибо!"
    "Расскажите, пожалуйста, почему Вы плохо сходили?"
    overseer "Я пришел сказал что от Босса."
    "Мне сказали что у них есть Босс."
    "Вышел какой-то мужик."
    "Меня оттуда выгнали."

    img 2385
    music Power_Bots_Loop
    m "КАК???"
    "КАКОЙ МУЖИК???"

    img 2386
    overseer "Я откуда знаю какой?"
    "Потом меня внизу догнала какая-то баба."
    "Сказала она твой секретарь."
    "Я ей рассказал что с тобой."
    "Она заплакала."
    "Я сказал что ты просила дать много денег."
    "Она сказала что от нее это теперь не зависит."
    "Я и ушел!"
    "Так что я тебя вытаскивать не буду!"
    img 2387
    m "Ясно, Сэр."
    "Я придумаю что-нибудь еще!"

    img 2388
    overseer "Вот тогда и поговорим!"
    "А сейчас все!"

    # уходит
    img 2389
    with fadelong
    mt "Мне надо придумать еще что-то!"

    music Jail_Clock
    $ jailDaySceneStage = 1
    $ policeCellStageName1 = "scene_Police_Cell_1_Day_8_1"
    $ policeCellStageName2 = "scene_Police_Cell_2_Day_8_2"
    $ policeCellMonica1 = "Police_Cell_1_Day_8_1"
    $ policeCellMonica2 = "Police_Cell_2_Day_8_2"
    call refresh_scene_fade()
    return

label jail_day8_2:
    #menu Лечь и думать
    #Не ложиться

    music Hidden_Agenda
    img 2390
    with fadelong
    mt "Идея!"
    img 2391
    "Надо отправить его в банк!"
    $ jailDaySceneStage = 2
    call refresh_scene_fade()
    return

label jail_day8_3:
    # подходит
    music Groove2_85
    img 2392
    with fadelong
    overseer "Чего тебе снова?"
    "Что ты все шумишь?"
    "Я тебе уже давал сегодня жрать!"
    "Больше не положено!"
    img 2393
    music Hidden_Agenda
    m "Сэр."
    "Я по поводу нашего договора."
    overseer "И что?"
    m "Сэр."
    "Я знаю как достать деньги."
    overseer "Говори."
    img 2394
    m "Вы можете сходить в Банк."
    "Я могу написать заявление на снятие денег со счета."
    "Вы туда сходите."
    "Вам дадут бумажку."
    "Я ее подпишу и Вы сможете снять деньги!"
    img 2395
    overseer "Ну давай."
    img 2396
    m "Принесите мне, пожалуйста, бумагу и ручку."
    img 2395
    overseer "?"
    img 2397
    m "Сэр!"
    overseer "Хорошо, сейчас."

    stop music fadeout 1.0
    call textonblack(_("Спустя 5 минут..."))
    img black_screen
    with Dissolve(1)
    music Groove2_85

    img 2395
    with fadelong
    overseer "На, пиши там."
    sound snd_pen_writing
    img black_screen
    with Dissolve(1)
    $ renpy.pause(3.0)

    img 2398
    with fadelong
    m "Вот, Сэр."
    "Вы сможете снять деньги."
    img 2399
    overseer "И сколько там?"
    img 2400
    m "Там заявление на сумму 10 миллионов долларов, Сэр."
    img 2401
    overseer "Ух ё!.."
    "И что мне сказать там?"

    img 2402
    m "Просто скажите что Вы мой представитель."
    img 2403
    overseer "Ладно, схожу завтра."
    m "Буду ждать, Сэр!"
    overseer "А сейчас все!"
    $ jailDaySceneStage = 3
    call refresh_scene_fade()
    return

label jail_day8_4:
    call jail_cage_blackmail()
    return
