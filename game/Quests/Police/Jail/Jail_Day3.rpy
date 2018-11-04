label jail_day3:
    $ jailDay = 3
    $ day = day + 1
    $ jailDaySceneStage = 0
    $ jailScenePlace = 0
    $ policeCellStageName1 = "scene_Police_Cell_1_Day_3_1"
    $ policeCellStageName2 = "scene_Police_Cell_2_Day_3_1"
    $ policeCellMonica1 = "Police_Cell_1_Day_3_1"
    $ policeCellMonica2 = "Police_Cell_2_Day_3_1"
    $ policeCellMonicaLabel = "jail_day3_Monica"
    $ policeCellBedLabel = "jail_day3_Bed"
    $ policeCellCageLabel = "jail_day3_Cage"
    stop music fadeout 1.0
    call textonblack(_("ДЕНЬ 3"))
    img black_screen
    with Dissolve(1)
    music Jail_Clock

    img 2255
    with fadelong
    mt "Уже третий день я здесь."
    "Кажется третий?"
    img 2256
    mt "Не могу же я здесь находиться вечно!"
    "Кто-то должен меня вытащить!"
    img 2257
    mt "Я ведь такая крупная фигура!"
    img 2258
    "Не может все быть вот так!"
    "..."
    "Тем не менее сейчас самое главное поесть."
    img 2259
    "Я безумно хочу есть!!!"
    call refresh_scene_fade()
    return

label jail_day3_Monica(obj_name, obj_data):
    if jailDaySceneStage == 0 or jailDaySceneStage == 1:
        mt "Я безумно хочу есть!!!"
    if jailDaySceneStage == 2:
        "Какое же имя у этого урода???"
    if jailDaySceneStage == 3:
        if monicaKnowOverseerName == True:
            mt "Ублюдок Боб с коротким членом!"
            "Гребаный жирный импотент!!!"
        if jailBoobsForFoodShowed == True:
            mt "Гребаный ублюдок!"
            "Как же его зовут???"
            "Я не могу поверить что мне пришлось ТАК УНИЗИТЬСЯ перед ним!!!"
            "Я! Моника Бакфетт!!!"
            "О БОЖЕ!"
            "Но что мне делать? Я чуть не умерла с голода!!!"
            "О БОЖЕ!"

    return

label jail_day3_Bed(obj_name, obj_data):
    if act == "l":
        call jail_day1_Bed(obj_name, obj_data)
        return
    if jailDaySceneStage == 0:
        mt "Я безумно хочу есть!!!"
    if jailDaySceneStage == 1:
        call jail_day3_1()
        return
    if jailDaySceneStage == 2:
        mt "Я безумно хочу есть!!!"
    if jailDaySceneStage == 3:
        menu:
            "Лечь спать":
                pass
            "Не ложиться":
                return
        call jail_day4()
        return


    return

label jail_day3_Cage(obj_name, obj_data):
    if act == "l":
        call jail_cage()
        call refresh_scene_fade()
        return
    if act == "w":
        $ cageInteractLabel = "jail_day3_Cage_Interact"
        call change_scene("police_jail_cage_scene")
        return

    return

label jail_day3_Cage_Interact:
    if jailDaySceneStage == 0:
        music Groove2_85
        # подходит
        img 5117
        with fadelong
        w
        img 2260
        overseer "Что тебе снова надо?"
        img 2261
        m "Я хочу есть!"
        "Ты не можешь просто не кормить меня!"
        img 2262
        overseer "Очень даже могу."
        "Хочешь пожалуйся куда-нибудь."
        "Позвони какому-нибудь боссу или что ты еще умеешь делать?"
        img 2263
        m "..."
        img 2264
        overseer "Мне бесполезно угрожать."
        "Ниже меня уже не понизят."
        img 2265
        m "Позовите Маркуса!"
        img 2266
        overseer "Мистер Маркус слишком занят чтобы общаться с вами."
        img 2267
        m "Но передайте что я хочу его видеть!"
        img 2268
        overseer "Не буду."
        img 2269
        m "Мне нужна еда!"
        "Я же живая!"
        img 2270
        overseer "Это временно..."
        img 2271
        music Power_Bots_Loop
        m "??????"
        img 2272
        "!!!!!!"
        "..."
        img 2273
        "..."

        menu:
            "Стой!":
                pass
            "...":
                music Jail_Clock
                return

        music Groove2_85
        img 2274
        with fade
        m "Стой!"
        img 2275
        "Слушай!"
        "Я понимаю."
        "Еда у тебя есть."
        "Я тебе нагрубила."
        "Скажи, что тебе надо чтобы ты меня покормил?"
        img 2276
        overseer "Во-первых, называй меня по имени!"
        "Во-вторых, будь со мной очень вежлива."
        "Я для тебя здесь самый главный Босс!"
        img 2277
        m "Я поняла."
        img 2278
        mt "Ненавижу этого урода!"
        "Но сейчас надо как-то подыграть."
        img 2279
        mt "Я же не могу ничего не есть третий день!"
        img 2280
        m "..."
        "Пожалуйста, дай мне еду."
        img 2281
        overseer "Я считаю недостаточно вежливо."
        img 2283
        m "..."
        img 2282
        m "..."
        img 2284
        with fade
        m "Пожалуйста, Сэр."
        "Я была бы очень благодарна Вам если бы Вы дали мне немного Вашей вкусной пищи."
        img 2285
        overseer "Я не знаю к кому ты обращаешься."
        img 2286
        m "Я обращаюсь к Вам, Сэр."
        img 2287
        overseer "У меня есть имя."
        "Разговор закончен."
        $ jailDaySceneStage = 1
        music Jail_Clock
        return

    if jailDaySceneStage == 1:
        img 2253
        with fadelong
        mt "Он не подходит."
        "Может быть попробовать еще раз попозже?"
        return

    if jailDaySceneStage == 2:
        music Groove2_85
        img 2291
        with fadelong
        overseer "Что тебе надо снова?"
        "Что ты все не угомонишься?"
#        $ bitchmeterValue = 1000 #debug
        label day3_menu_loop1:
            menu:
                "Обмануть надзирателя, чтобы узнать его имя..." if bitchmeterValue > maxBitchness / 2:
                    $ jailBoobsForFood = False
                    call jail_day3_2()
                "Обмануть надзирателя, чтобы узнать его имя... - Моника слишком добрая (disabled)" if bitchmeterValue <= maxBitchness / 2:
                    jump day3_menu_loop1
                "Пожалуйста! Дайте поесть! Я готова на все!!! - Моника слишком сучка (disabled)" if bitchmeterValue > maxBitchness / 2:
                    jump day3_menu_loop1
                "Пожалуйста! Дайте поесть! Я готова на все!!!" if bitchmeterValue <= maxBitchness / 2:
                    $ jailBoobsForFood = True
                    call jail_day3_3()
            $ policeCellStageName1 = "scene_Police_Cell_1_Day_3_2"
            $ policeCellStageName2 = "scene_Police_Cell_2_Day_3_2"
            $ policeCellMonica1 = "Police_Cell_1_Day_3_2"
            $ policeCellMonica2 = "Police_Cell_2_Day_3_2"
            call refresh_scene_fade()
            return


    if jailDaySceneStage == 3:
        img 2253
        with fadelong
        mt "Он не подходит."
        "Может быть он вообще ушел?"
        "Мне не видно отсюда!"
        if jailBoobsForFoodShowed == True:
            call jail_cage()
            return

    return



label jail_day3_1:
    img 2288
    with fadelong
    mt "Я не могу лечь спать"
    "Я безумно хочу есть!"
    img 2289
    music Hidden_Agenda
    "Как он сказал?"
    "Имя?"
    img 2290
    "Черт!"
    "Какое же имя у этого урода???"
    $ jailDaySceneStage = 2
    $ jailScenePlace = 0
    call refresh_scene_fade()
    return
    #


    #

label jail_day3_2:
    img 2292
    with fade
    w
    music Hidden_Agenda
    img 2293
    with fade
    m "Сэр."
    img 2294
    "Я бы хотела с Вами познакомиться."
    img 2295
    "Вы такой элегантный и симпатичный."
    img 2296
    "Меня зовут Моника."
    "А Вас?"
    img 2297
    overseer "Меня Боб."
    $ monicaKnowOverseerName = True

    music Groove2_85
    img 2298
    overseer "Тьфу!"
    "Ты меня развела!"
    "Вот хитрая сучка!"

    music Hidden_Agenda
    img 2299
    with fade
    m "..."
    "Боб."
    "Пожалуйста."
    "Вы такой заметный кавалер!"
    "Не угостите-ли Вы даму чем-нибудь?"
    overseer "Ладно."
    "Уговорила."
    "Сейчас принесу."
    img 2300
    m "Большое спасибо, Боб!"

    music Pyro_Flow
    img 2301
    mt "Ублюдок Боб с коротким членом!"
    "Гребаный жирный импотент!!!"

    # подходит
    img 5118
    music Groove2_85
    img 2302
    with fadelong
    overseer "На, ешь!"
    "И только попробуй сказать что это невкусная баланда!"

    $ jailFoodInteractLabel = "jail_day3_2a"
    call change_scene("police_jail_food_scene", "Fade", False)
    return

label jail_day3_2a:

    # подходит
    music Groove2_85
#    img 2303
#    with fadelong
    img 2304
    with fadelong
    mt "Просто жуть!"
    "Но почему так мало?"
    if monicaKnowOverseerName == True:
        m "Боб."
    m "Скажите, можно добавки?"
    overseer "Нет."
    "Порции рассчитаны."
    "Разговор закончен."
    $ jailDaySceneStage = 3
    call refresh_scene_fade()
    return

label jail_day3_3:
    #jail_boobs_for_food
    music Groove2_85
    img 5119
    with fadelong
    m "Сэр!"
    "Прошу ВАС!!!"
    "Я УМИРАЮ С ГОЛОДА!!!"
    "Пожалуйста!!!"
    "Дайте мне что-нибудь поесть!"
    img 5120
    "Скажите что мне сделать для этого? Я готова на все!"
    img 2249
    overseer "Я не знаю."
    "А что у тебя есть?"
    img 5120
    m "У меня..."
    "Ничего нет..."
    "(хмык)"
    img 5121
    overseer "Ну как же нет, а это?"
    img 5122
    m "Что?"
    overseer "Ну это!"
    img 5123
    m "Что это? Что ВЫ имеете ввиду сэр?"
    img 5124
    overseer "Твои сиськи! Что еще?"
    img 5125
    m "В смысле мои... си..???"
    img 5126
    overseer "Покажи сиськи, тогда покормлю!"
    "У меня здесь все просто!"
    "Или вежливость или сиськи!"
    img 5127
    "Вежливости у тебя нет!"
    "Но сиськи есть! Да!"
    img 5128
    mt "О БОЖЕ!!!"
    m "Сэр..."
    img 5129
    "А можно как-то... как-то по другому..."
    img 5116
    overseer "Нельзя! Разговор закончен!"
    menu:
        "Стойте! Я покажу Вам сиськи!":
            pass
        "...":
            return
    img 2373
    with fade
    m "Стойте! Я покажу Вам сиськи!"
    img 5130
    overseer "Хе-хе. Давай показывай..."
    img 5131
    mt "БОЖЕ, Моника!"
    "Как ты здесь очутилась???"
    "Как ты вообще могла согласиться на это???"
    img 5132
    "Но у меня нет выбора!!!"
    "У МЕНЯ НЕТ ВЫБОРА!!!"
    "Я умру здесь! И всем плевать!!!"
    img 5133
    "Но ничего! Я придумаю! Я выберусь отсюда!"
    "Этот мерзавец заплатит за все!!!"
    img 5134
    "Он будет первым в моем списке мести!!!"
    img 5135
    w
    img 5136
    overseer "Ну? Так где сиськи? Я ухожу!"
    img 5137
    m "Стойте!"
    img 5138
    "..."
    img 5139
    overseer "Ну?"
    img black_screen
    with Dissolve(1)
    $ jailBoobsForFoodShowed = True
    #показывает в лифчике
    music Loved_up2
    img 5141
    with fadelong
    w
    img 5142
    w
    img 5143
    w
    img 5144
    w
    img 5145
    w
    img 5146
    overseer "Я это и так вижу! Сними этот, как его..."
    music Groove2_85
    img 5147
    with fade
    m "Сэр! Я думаю этого достаточно!"
    img 5148
    overseer "Ладно, ладно, не злись."
    "Снимешь в следующий раз..."
    img 5149
    m "!!!"
    img 5116
    with fadelong
    overseer "Сейчас принесу."

    img 5150
    m "Большое спасибо, Сэр!"

    music Pyro_Flow
    img 2301
    mt "Ублюдок с коротким членом!"
    "Гребаный жирный импотент!!!"

    # подходит
    img 5118
    music Groove2_85
    img 2302
    with fadelong
    overseer "На, ешь!"
    "И только попробуй сказать что это невкусная баланда!"

    $ jailFoodInteractLabel = "jail_day3_2a"
    call change_scene("police_jail_food_scene", "Fade", False)

    return
