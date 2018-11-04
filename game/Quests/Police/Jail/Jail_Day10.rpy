label jail_day10:
    $ jailDay = 10
    $ day = day + 1
    $ jailDaySceneStage = 0
    $ jailScenePlace = 0
    $ policeCellStageName1 = "scene_Police_Cell_1_Day_10_1"
    $ policeCellStageName2 = "scene_Police_Cell_2_Day_6_2"
    $ policeCellMonica1 = "Police_Cell_1_Day_10_1"
    $ policeCellMonica2 = "Police_Cell_2_Day_6_2"
    $ policeCellMonicaLabel = "jail_day10_Monica"
    $ policeCellBedLabel = "jail_day10_Bed"
    $ policeCellCageLabel = "jail_day10_Cage"
    stop music fadeout 1.0
    call textonblack(_("ДЕНЬ 10"))
    img black_screen
    with Dissolve(1)
    music Jail_Clock

    img 2435
    with fadelong
    mt "Десятый день!"
    "О Боже!"
    "Моника!"
    "Как ты могла оказаться в таком месте?"
    "..."
    img 2436
    mt "Не ныть."
    "У нас есть план."
    img 2437
    "Где там этот жирный урод?"
    "Надеюсь хоть придти к риелтору он смог!"
    call refresh_scene_fade()
    return

label jail_day10_Monica(obj_name, obj_data):
    if jailDaySceneStage == 0:
        mt "Где там этот жирный урод?"
    if jailDaySceneStage == 1:
        mt "Два дня!"
        "Два дня!"
        "Бесконечных два дня!"
    if jailDaySceneStage == 2:
        mt "Что им надо снова???"
        "Ублюдки!!!"
    if jailDaySceneStage == 3:
        mt "Я хочу спать... Не могу ни о чем думать..."

    return

label jail_day10_Bed(obj_name, obj_data):
    if act == "l":
        call jail_day1_Bed(obj_name, obj_data)
        return

    if jailDaySceneStage == 0:
        mt "Некогда спать!"

    if jailDaySceneStage == 1:
        menu:
            "Лечь спать":
                pass
            "Не ложиться":
                return
        if jailCageBlackmailEnded == True:
            call jail_day11()
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
        $ jailDaySceneStage = 2
        return
    if jailDaySceneStage == 2:
        prisoner1 "Эй! Шлюха!"
        "Иди сюда!"
        "Мы хотим видеть тебя!"
    if jailDaySceneStage == 3:
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
        call jail_day11()
    return

label jail_day10_Cage(obj_name, obj_data):
    if jailDaySceneStage == 2:
        call jail_day10_2()
        return
    if act == "l":
        call jail_cage_blackmail_day()
        call refresh_scene_fade()
        return
    if act == "w":
        $ cageInteractLabel = "jail_day10_Cage_Interact"
        call change_scene("police_jail_cage_scene")
        return

    return

label jail_day10_Cage_Interact:
    if jailDaySceneStage == 0:
        # подходит
        img 5117
        with fadelong
        w
        music Groove2_85
        img 2438
        overseer "Сейчас жрать принесу!"
        "Не стучи!"
        "Голова!"
        m "Сэр?"
        "Пожалуйста?"
        "Как Вы сходили?"

        music Power_Bots_Loop
        overseer "Плохо."

        img 2439
        mt "О НЕТ!!!!"

        music Groove2_85
        img 2438
        overseer "Ой."
        "Вернее хорошо."
        "Это то что голова болит плохо."
        "Что ты меня путаешь все???"
        "Надоела уже!!!"
        music Hidden_Agenda
        img 2440
        m "ДА!!!"
        "Сэр."
        "Хорошо."
        "Я с удовольствием жду Вашу самую вкусную еду!"
        overseer "То-то же..."
        img 5116
        w
        img black_screen
        with Dissolve(1)
        img 5118
        with fade
        w
        # уходит
        # приходит
        music Groove2_85
        img 2441
#        with fadelong
        overseer "На, жри!"

        music Hidden_Agenda
        m "Спасибо, Сэр!"
        "Спасибо!"

        mt "УРА УРА УРА"
        "ОН ХОРОШО СХОДИЛ!!!"

        $ jailFoodInteractLabel = "jail_day10_1a"
        call change_scene("police_jail_food_scene", "Fade", False)
    if jailDaySceneStage == 1:
        img 2253
        with fadelong
        mt "Никого нет..."
    if jailDaySceneStage == 3:
        img 2253
        with fadelong
        mt "Никого нет..."

    return

label jail_day10_1a:
    music Hidden_Agenda
    img 2443
    with fadelong
    m "Сэр!"
    "Спасибо!"
    "Очень!"
    "Очень вкусно!"
    "А теперь пожалуйста!"
    "Расскажите что Вам сказала риелтор."

    if jailBoobsForFood == True:
        img 5258
        overseer "..."
        m "..."
        overseer "..."
        overseer "Сиськи..."
        img 5259
        m "Сэр, вы правда хорошо сходили?"
        img 5260
        w
        img 5261
        overseer "Да, правда. Сначала сиськи..."
        img 5262
        w
        menu:
            "Показать грудь.":
                # показывает грудь
                call jail_boobs_for_food()
#        m "Сэр! Пожалуйста! Расскажите скорее!"
        img 5289
        m "Расскажите как Вы сходили!"
        img 5290
        overseer "Ну..."
        "Я пришел."
        "Дал твою бумажку ей."
        "Она посмотрела."
        "Сказала чтобы завтра приходил."
        "Что она все оформит."
        img 5291
        m "УРА!!!"
        img 5292
        "Сэр?"
        "Вы помните свою часть уговора?"

        overseer "Да помню я, помню!"
        img 5293
        m "Сэр."
        "Когда Вы сможете меня вывести отсюда?"
        sound snd_jail_door
        img black_screen
        with Dissolve(1)
        img 5294
        with fadelong
        w
        img 5295
        w
        img 5296
        overseer "Ну ежели все оформится хорошо."
        "То через два дня тебя выведу."
        img 2448
        mt "Два дня!"
        "Два дня!"
        "Бесконечных два дня!"

        music Pyro_Flow
        img 2449
        with fade
        mt "Но я потерплю!"
        "Ради всей мести, которая во мне накопилась, я потерплю!"
        img 2450
        "И когда я выберусь отсюда, я всем устрою АД!"

        music Jail_Clock
        img 2451
        mt "СТОП!"
        "Маркус говорил что мой вопрос решится через две недели. Может быть даже меньше!"
        "А вдруг я не успею выбраться?"
#        music Hidden_Agenda
        img 5297
        with fade
        m "Сэр!"
        "А можно завтра?"
        "Пожалуйста!"
        img 2454
        overseer "Нет."
        "Как сказал, так и будет."
#        m "Ну пожалуйста, Сэр!"

        music Groove2_85
        img 2454
        overseer "У меня начинает болеть голова от тебя."
        "Если будешь мне надоедать, я откажусь от твоей ерунды!"
        img 5298
        m "Нет нет, Сэр!"
        "Хорошо, я подожду!"
        img 2456
        mt "Очень надеюсь что успею!"
        "Я должна успеть!"
    else:

        img 2444
        with fadelong
        overseer "Ну..."
        "Я пришел."
        "Дал твою бумажку ей."
        "Она посмотрела."
        "Сказала чтобы завтра приходил."
        "Что она все оформит."
        img 2445
        m "УРА!!!"
        img 2446
        "Сэр?"
        "Вы помните свою часть уговора?"

        overseer "Да помню я, помню!"
        img 2447
        m "Сэр."
        "Когда Вы сможете меня вывести отсюда?"
        overseer "Ну ежели все оформится хорошо."
        "То через два дня тебя выведу."
        img 2448
        mt "Два дня!"
        "Два дня!"
        "Бесконечных два дня!"

        music Pyro_Flow
        img 2449
        with fade
        mt "Но я потерплю!"
        "Ради всей мести, которая во мне накопилась, я потерплю!"
        img 2450
        "И когда я выберусь отсюда, я всем устрою АД!"

        music Jail_Clock
        img 2451
        mt "СТОП!"
        "Маркус говорил что мой вопрос решится через две недели. Может быть даже меньше!"
        "А вдруг я не успею выбраться?"
        music Hidden_Agenda
        img 2452
        with fade
        m "Сэр!"
        "А можно завтра?"
        "Пожалуйста!"
        img 2453
        overseer "Нет."
        "Как сказал, так и будет."
        m "Ну пожалуйста, Сэр!"

        music Groove2_85
        img 2454
        overseer "У меня начинает болеть голова от тебя."
        "Если будешь мне надоедать, я откажусь от твоей ерунды!"
        img 2455
        m "Нет нет, Сэр!"
        "Хорошо, я подожду!"
        img 2456
        mt "Очень надеюсь что успею!"
        "Я должна успеть!"

    $ jailDaySceneStage = 1
    $ policeCellStageName1 = "scene_Police_Cell_1_Day_10_2"
    $ policeCellStageName2 = "scene_Police_Cell_2_Day_10_2"
    $ policeCellMonica1 = "Police_Cell_1_Day_10_2"
    $ policeCellMonica2 = "Police_Cell_2_Day_10_2"
    call refresh_scene_fade()
    return

    #menu Лечь спать?
    #Лечь спать
    #Не ложиться

    return

label jail_day10_2:
    call jail_cage_blackmail()
    return
