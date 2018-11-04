label jail_day4:
    $ jailDay = 4
    $ day = day + 1
    $ jailDaySceneStage = 0
    $ jailScenePlace = 0
    $ policeCellStageName1 = "scene_Police_Cell_1_Day_4_1"
    $ policeCellStageName2 = "scene_Police_Cell_2_Day_4_1"
    $ policeCellMonica1 = "Police_Cell_1_Day_4_1"
    $ policeCellMonica2 = "Police_Cell_2_Day_4_1"
    $ policeCellMonicaLabel = "jail_day4_Monica"
    $ policeCellBedLabel = "jail_day4_Bed"
    $ policeCellCageLabel = "jail_day4_Cage"
    stop music fadeout 1.0
    call textonblack(_("ДЕНЬ 4"))
    img black_screen
    with Dissolve(1)
    music Jail_Clock

    img 2305
    with fadelong
    mt "Какой это уже день?"
    "Кажется четвертый?"
    "Я до сих пор как-будто во сне."
    "Мне надо как-то выбраться отсюда."
    "Позвать друзей."
    "..."
    "Хотя у меня нет друзей."
    img 2306
    mt "Но есть Дик!"
    "Кстати!"
    "Дик должен что-то придумать!"
    "Надо выбраться отсюда и придти к нему!"
    img 2307
    "Он меня спасет!"
    "..."
    "А сейчас..."

    img 2308
    mt "Я не могу находиться без одежды."
    "Мимо меня постоянно водят заключенных."
    "Все пялятся на меня как-будто я какая-то шлюха."
    img 2309
    mt "А я не шлюха!"
    "Я королева!"
    "Мое лицо на обложке самого модного журнала!"
    "Все эти люди вокруг какие-то недоноски!"
    if monicaKnowOverseerName == True:
        "Особенно этот жирный Боб!"
    else:
        "Особенно этот жирный урод!"
        "Как, черт побери, его зовут?!?!"
    img 2310
    mt "Он вообще не человек, он просто насекомое!"
    if jailBoobsForFoodShowed == True:
        mt "Я не могу поверить на что мне пришлось пойти чтобы добиться от него элементарной еды!!!"
    "Они даже не понимают кого тут держат!"
    img 2311
    mt "..."
    "!!!!!!!"
    call refresh_scene_fade()
    return

label jail_day4_Monica(obj_name, obj_data):
    if jailDaySceneStage == 0:
        mt "Черт побери! Я снова хочу есть!"
    if jailDaySceneStage == 1:
        mt "Этот урод ушел!"
        "Но, по крайней мере, я поела хоть какую-то еду..."
        "Если эти помои вообще можно назвать едой!"
        "О БОЖЕ!!!"

    return

label jail_day4_Bed(obj_name, obj_data):
    if act == "l":
        call jail_day1_Bed(obj_name, obj_data)
        return
    if jailDaySceneStage == 0:
        mt "Черт побери! Я снова хочу есть!"
    if jailDaySceneStage == 1:
        menu:
            "Лечь спать":
                pass
            "Не ложиться":
                return
        call jail_day5()
        return

    return

label jail_day4_Cage(obj_name, obj_data):
    if act == "l":
        call jail_cage()
        call refresh_scene_fade()
        return
    if act == "w":
        $ cageInteractLabel = "jail_day4_Cage_Interact"
        call change_scene("police_jail_cage_scene")
        return

    return

label jail_day4_Cage_Interact:
    if jailDaySceneStage == 0:
        call jail_day4_1()
        return
    if jailDaySceneStage == 1:
        img 2253
        with fadelong
        mt "Он не подходит."
        "Может быть он вообще ушел?"
        "Мне не видно отсюда!"
        if jailBoobsForFoodShowed == True:
            call jail_cage()
            return
        return

    return

    #
label jail_day4_1:
    sound snd_jail_door_locked
    if jailBoobsForFood == False:
        music Groove2_85
        img 2312
        with fadelong
        overseer "Чего тебе?"
        img 2313
        m "Сэр."
        "Могли-бы Вы меня чем-нибудь угостить..."
        "Какой-нибудь едой..."
        overseer "Сейчас принесу."
        "Так уж и быть."
        img 2314
        m "Мерси..."
        img 2315
        mt "Урод!!!"

        # подходит
        img 2316
        with fadelong
        overseer "На, ешь!"
        m "Спасибо, Сэр!"
        img 2317
        mt "Спасибо, жирный урод!"
        $ jailFoodInteractLabel = "jail_day4_1a"
        call change_scene("police_jail_food_scene", "Fade", False)
        return

    if jailBoobsForFood == True:
        music Groove2_85
        img 2312
        with fadelong
        overseer "Чего тебе?"
        img 5151
        m "Сэр."
        "Могли-бы Вы меня чем-нибудь угостить..."
        "Какой-нибудь едой..."
        img 5152
        overseer "Сиськи..."
        m "Сэр, я Вам уже показывала."
        "Может быть обойдемся без этого?"
        overseer "Ты не показывала."
        m "Сэр, но я показывала и я..."
        img 5116
        with fade
        overseer "У меня голова болит от тебя!"
        overseer "Все, я ухожу. Ты надоела мне."
        menu:
            "Стойте! Я покажу Вам!":
                pass
            "...":
                call refresh_scene_fade()
                return
        img 2373
        m "Стойте! Я покажу Вам!"
        img 5153
        overseer "Давай, показывай! Без этого, как это его..."
        img 5154
        m "Лифчика?"
        overseer "Да! Лиф.. Так! Не путай меня!"
        "Давай показывай!"
        img 5155
        m "Сэр! Может быть показать в лифчике, как вчера?"
        img 5156
        overseer "Все! Я ухожу!"
        img 5157
        m "Стойте!"
        img 5158
        with fadelong
        mt "..."
        "..."
        # показывает
        call jail_boobs_for_food()

        img 5168
        with fadelong
        overseer "То-то же!"
        overseer "Сейчас принесу."
        "Так уж и быть."
        "И в следующий раз проси улыбаясь!"
        "Иначе больше еды не дам!!!"
        m "Мерси..."
        img 2315
        mt "Урод!!!"

        # подходит
        img 5116
        with fadelong
        w
        img 5118
        with fadelong
        w
        if jailBoobsForFood == False:
            img 2316
            with fadelong
        else:
            img 2317
            with fadelong
        overseer "На, ешь!"
        m "Спасибо, Сэр!"
        img 2317
        mt "Спасибо, жирный урод!"
        $ jailFoodInteractLabel = "jail_day4_1a"
        call change_scene("police_jail_food_scene", "Fade", False)
        return

label jail_day4_1a:
    #

    music Groove2_85
    if jailBoobsForFood == True:
        img 2320
        with fadelong
        overseer "Ну как?"
        m "Сэр. Спасибо."
        "Очень вкусно!"
        mt "Для такого урода как ты может быть и вкусно!"
        overseer "То-то же."
        m "Сэр?"
        overseer "Что еще?"
        m "Сэр, могу я Вас попросить принести мне одежду?"
    else:
        img 2318
        with fadelong
        overseer "Ну как?"
        m "Сэр. Спасибо."
        "Очень вкусно!"
        img 2319
        mt "Для такого урода как ты может быть и вкусно!"
        img 2318
        overseer "То-то же."
        m "Сэр?"
        overseer "Что еще?"
        m "Сэр, могу я Вас попросить принести мне одежду?"
        img 2320
    overseer "В той одежде нельзя здесь находиться."
    "Здесь нужна тюремная одежда."
    "У нас все строго."

    music Pyro_Flow
    img 2321
    with fade
    m "Так принеси тюремную!"
    img 2322
    overseer "Что?"
    "Как ты со мной говоришь?"
    music Hidden_Agenda
    img 2323
    m "Простите, Сэр."
    "Это просто вырвалось."
    "Такого больше не повторится."
    mt "УРОД!"
    music Groove2_85
    overseer "То-то же."
    img 2324
    m "Сэр."
    "Могли-бы Вы принести мне тюремную одежду, если Вас не затруднит?"

    img 2325
    overseer "У нас не осталось женской тюремной одежды."
    "Последнюю разорвали когда насиловали в камере заключенную."
    "Мы ее выкинули."
    "Больше поставок не было."
    img 2326
    music Power_Bots_Loop
    m "Насиловали заключенную???"
    "Это нормально?"
    img 2325
    overseer "Мне без разницы."
    "Если нет шума, значит не болит голова."
    "Для меня это главное."
    img 2327
    mt "!?!?!?!?!"
    img 2325
    overseer "Все, у меня начинает она болеть."
    "Разговор закончен."
    music Jail_Clock
    $ jailDaySceneStage = 1
    $ policeCellStageName1 = "scene_Police_Cell_1_Day_4_2"
    $ policeCellStageName2 = "scene_Police_Cell_2_Day_4_2"
    $ policeCellMonica1 = "Police_Cell_1_Day_4_2"
    $ policeCellMonica2 = "Police_Cell_2_Day_4_2"
    call refresh_scene_fade()


    return
