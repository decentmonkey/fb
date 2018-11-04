label jail_day2:
    $ jailDay = 2
    $ day = day + 1
    $ jailDaySceneStage = 0
    $ jailScenePlace = 0
    $ policeCellStageName1 = "scene_Police_Cell_1_Day_2_1"
    $ policeCellStageName2 = "scene_Police_Cell_2_Day_2_1"
    $ policeCellMonica1 = "Police_Cell_1_Day_2_1"
    $ policeCellMonica2 = "Police_Cell_2_Day_2_1"
    $ policeCellMonicaLabel = "jail_day2_Monica"
    $ policeCellBedLabel = "jail_day2_Bed"
    $ policeCellCageLabel = "jail_day2_Cage"
    call refresh_scene_fade()
    stop music fadeout 1.0
    call textonblack(_("ДЕНЬ 2"))
    img black_screen
    with Dissolve(1)
    music Cheery_Monday

    img 2232
    with fadelong
    mt "Утро...."
    img 2233
    "Новый прекрасный день..."
    "А где Юлия?"
    img 2234
    if juliaPunishedNone == True or juliaPunishedLow == True:
        mt "Что-то не слышно как она убирается в доме с утра..."
    else:
        mt "Что-то не слышно как она трет пятно..."
    if juliaPunished == True and juliaFirePlanned == True and juliaFireCancelled == False:
        "А, я же уволила ее!"
        "Точно. Я и забыла!"
    img 2235
    "Вчера был интересный день."
    if juliaFirePlanned == True and janeTiffanyFirePlanned == True:
        "Я уволила Юлию, потом поехала увольнять Тиффани и Джейн."
    if juliaFirePlanned == True and janeTiffanyFirePlanned == False:
        "Я уволила Юлию"
    if fredFirePlanned == True:
        if juliaFirePlanned == True or janeTiffanyFirePlanned == True:
            "Потом Фреда."
        else:
            "Я уволила Фреда."
    if fireAmount > 1:
        "А я уволила их или нет?"
        "Что-то не помню."
        "Так. Что вчера было?"
    else:
        "А что вчера еще было?"
    "Помню я заехала в полицию на 5 минут."

    img 2236
    mt "Маркус..."

    music Jail_Clock
    img 2237
    with fade
    mt "СТОП!!!!!"
    "ГДЕ Я???????"
    img 2238
    "СНОВА ЭТО МЕСТО!!!"
    img 2239
    "ЭТО ЖЕ БЫЛ СОН!!!"
    "Я ЕЩЕ НЕ ПРОСНУЛАСЬ????"

    return

label jail_day2_Monica(obj_name, obj_data):
    if jailDaySceneStage == 0:
        mt "Я ЕЩЕ НЕ ПРОСНУЛАСЬ????"
    if jailDaySceneStage == 1:
        mt "Может стоит лечь поспать?"
    if jailDaySceneStage == 2 or jailDaySceneStage == 3:
        mt "Я не могу заснуть."
        "Я хочу есть!"
    if jailDaySceneStage == 4:
        mt "Похоже придется ложиться голодной."

    return

label jail_day2_Bed(obj_name, obj_data):
    if act == "l":
        call jail_day1_Bed(obj_name, obj_data)
        return
    if jailDaySceneStage == 0:
        mt "Я только проснулась, я не могу больше лежать НА ЭТОМ!!!"
    if jailDaySceneStage == 1:
        mt "Может стоит лечь поспать?"
        menu:
            "Лечь спать":
                pass
            "Не ложиться":
                return
        img black_screen
        with Dissolve(1)
        img 2248
        with fadelong
        mt "Наверное уже вечер."
        "Я не могу заснуть."
        "Я хочу есть!"
        $ jailDaySceneStage = 2
        $ jailScenePlace = 0
        $ policeCellStageName1 = "scene_Police_Cell_1_Day_2_2"
        $ policeCellStageName2 = "scene_Police_Cell_2_Day_2_2"
        $ policeCellMonica1 = "Police_Cell_1_Day_2_2"
        $ policeCellMonica2 = "Police_Cell_2_Day_2_2"
        call refresh_scene_fade()
        return
    if jailDaySceneStage == 2 or jailDaySceneStage == 3:
        mt "Я не могу заснуть."
        "Я хочу есть!"

    if jailDaySceneStage == 4:
        menu:
            "Лечь спать голодной":
                pass
            "Не ложиться":
                return
        call jail_day3()
        return
    return

label jail_day2_Cage(obj_name, obj_data):
    if jailCageViewed == False:
        mt "Возможно стоит подойти к решетке?"
        "Мне надо кого-то позвать!"
        "Я уже провела здесь ночь! И я не собираюсь оставаться еще хоть сколько-то времени здесь!!!"
        call jail_cage()
        $ jailCageViewed = True
        call refresh_scene_fade()
        return
    if act == "l":
        call jail_cage()
        call refresh_scene_fade()
        return
    if act == "w":
        if jailDaySceneStage == 1:
            mt "Я не собираюсь туда подходить! Это ничтожество не заслуживает общения со мной!"
            return
        $ cageInteractLabel = "jail_day2_Cage_Interact"
        call change_scene("police_jail_cage_scene")
        return

    return

label jail_day2_Cage_Interact:
    if jailDaySceneStage == 2:
        music Groove2_85
        # подходит
        img 5117
        with fadelong
        w
        img 2249
        overseer "Что ты снова шумишь?"
        "Ты не поняла с первого раза?"
        "Не шуметь!!!"
        img 2250
        m "Слушай, как там тебя зовут?"
        "Я хочу есть!"
        img 2251
        overseer "А мне какое дело?"
        "Ты даже не помнишь как меня зовут!"
        "Я не собираюсь кормить тебя."
        img 2252
        "Научись вежливо общаться для начала!"
        $ jailDaySceneStage = 3
        music Jail_Clock
        call refresh_scene_fade()
        return
    if jailDaySceneStage == 3 or jailDaySceneStage == 4:
        img 2253
        with fadelong
        mt "Он не подходит."
        "Он специально игнорирует меня."
        img 2254
        "Похоже придется ложиться голодной."
        $ jailDaySceneStage = 4
        return

    music Groove2_85
    # подходит
    img 5117
    with fadelong
    w
    img 2240
    overseer "Ты чего шумишь?"
    "Ты знаешь что у меня болит голова?"
    "Будешь шуметь, я устрою неприятности тебе!"

    img 2241
    music Pyro_Flow
    m "Слышишь, болван!"
    "Скажи где я?"
    img 2242
    overseer "Ты ненормальная?"
    "Ты находишься в подвале полиции."
    img 2243
    m "А долго я здесь буду?"
    img 2244
    overseer "Этого я не знаю!"
    "Кто-то сидит здесь уже долго."
    "Кого-то через некоторое время направляют в другие учреждения."
    img 2245
    "По мне чем меньше заключенных, тем лучше!"
    img 2246
    m "Ясно, свободен."
    img 2247
    overseer "Как ты со мной разговариваешь, стерва???"

    music Jail_Clock
    $ jailDaySceneStage = 1
    $ policeCellStageName1 = "scene_Police_Cell_1_Day_2_2"
    $ policeCellMonica1 = "Police_Cell_1_Day_2_2"
    call refresh_scene_fade()
    return
