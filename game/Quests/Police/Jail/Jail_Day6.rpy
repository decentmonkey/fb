label jail_day6:
    $ jailDay = 6
    $ day = day + 1
    $ jailDaySceneStage = 0
    $ jailScenePlace = 0
    $ policeCellStageName1 = "scene_Police_Cell_1_Day_6_1"
    $ policeCellStageName2 = "scene_Police_Cell_2_Day_6_1"
    $ policeCellMonica1 = "Police_Cell_1_Day_6_1"
    $ policeCellMonica2 = "Police_Cell_2_Day_6_1"
    $ policeCellMonicaLabel = "jail_day6_Monica"
    $ policeCellBedLabel = "jail_day6_Bed"
    $ policeCellCageLabel = "jail_day6_Cage"
    stop music fadeout 1.0
    call textonblack(_("ДЕНЬ 6"))
    img black_screen
    with Dissolve(1)
    music Jail_Clock

    img 2334
    with fadelong
    mt "День."
    "Шесть."
    "О Боже!"
    "Мне надо что-то придумать!"
    "Все что у меня есть - это общение с этим жирным ублюдком!"
    "Еще и тупым!"
    "Надо как-то использовать его глупость чтобы вырваться отсюда."
    if jailBoobsForFood == True:
        mt "Если чтобы поесть мне приходится показывать грудь такому идиоту, значит я тупее его?"
        "Но ведь это не так!"
    img 2335
    mt "Моника!"
    "Ты же самая умная!"
    "Думай!"
    call refresh_scene_fade()
    return

label jail_day6_Monica(obj_name, obj_data):
    if jailDaySceneStage == 0:
        mt "Мне надо что-то придумать!"
    if jailDaySceneStage == 1:
        mt "Мне надо что-то придумать!"
        "Но сейчас я уже хочу спать..."
    return

label jail_day6_Bed(obj_name, obj_data):
    if act == "l":
        call jail_day1_Bed(obj_name, obj_data)
        return

    if jailDaySceneStage == 0:
        mt "Мне надо что-то придумать!"
    if jailDaySceneStage == 1:
        mt "Мне надо что-то придумать!"
        "Но сейчас я уже хочу спать..."
        menu:
            "Лечь спать":
                pass
            "Не ложиться":
                return
        call jail_day7()
    return

label jail_day6_Cage(obj_name, obj_data):
    if act == "l":
        call jail_cage()
        call refresh_scene_fade()
        return
    if act == "w":
        $ cageInteractLabel = "jail_day6_Cage_Interact"
        call change_scene("police_jail_cage_scene")
        return

    return

label jail_day6_Cage_Interact:
    if jailDaySceneStage == 0:
        music Groove2_85
        # подходит
        img 2336
        with fadelong
        overseer "Что стучишь?"
        "Жрать хочешь?"
        img 2337
        music Hidden_Agenda
        m "Сэр."
        "Вы так проницательны..."
        music Groove2_85
        img 2338
        overseer "Если будешь меня снова путать своими словечками, я перестану тебя кормить!"
        if jailBoobsForFood == True:
            img 5180
            with fadelong
            overseer "..."
            m "..."
            overseer "..."
            img 5181
            m "Что? Снова?!?!"
            img 5182
            m "Что ВАМ надо снова???"
            img 5183
            overseer "Сиськи..."
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
        # уходит за едой
        img 5116
        with fadelong
        w
        img black_screen
        with Dissolve(1)
        img 5118
        with fadelong
        w

        $ jailFoodInteractLabel = "jail_day6_1a"
        call change_scene("police_jail_food_scene", "Fade", False)

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

label jail_day6_1a:
    sound snd_eating
    music Groove2_85
    img 2339
    m "Очень вкусно, Спасибо!"
    overseer "Еще бы!"
    music Hidden_Agenda
    m "Сэр."
    "У меня есть к Вам предложение."
    img 2340
    overseer "Какое еще пред..ложение?"
    img 2339
    m "Мы бы могли придумать с Вами где взять деньги."
    "Вы знаете, у меня на свободе есть возможности."

    img 2340
    overseer "И зачем?"
    img 2341
    m "Чтобы купить мне одежду, Сэр!"

    img 2342
    overseer "Вот еще!"
    "Буду я из-за каких-то тряпок бегать что-то искать!"
    "Опять из-за тебя голова начинает болеть!"
    "Разговор закончен!"

    $ jailDaySceneStage = 1
    $ policeCellStageName1 = "scene_Police_Cell_1_Day_6_1"
    $ policeCellStageName2 = "scene_Police_Cell_2_Day_6_2"
    $ policeCellMonica1 = "Police_Cell_1_Day_6_1"
    $ policeCellMonica2 = "Police_Cell_2_Day_6_2"
    music Jail_Clock
    call refresh_scene_fade()
    return
