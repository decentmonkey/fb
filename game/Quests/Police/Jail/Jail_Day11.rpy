label jail_day11:
    $ jailDay = 11
    $ day = day + 1
    $ jailDaySceneStage = 0
    $ jailScenePlace = 0
    $ policeCellStageName1 = "scene_Police_Cell_1_Day_11_1"
    $ policeCellStageName2 = "scene_Police_Cell_2_Day_11_1"
    $ policeCellMonica1 = "Police_Cell_1_Day_11_1"
    $ policeCellMonica2 = "Police_Cell_2_Day_11_1"
    $ policeCellMonicaLabel = "jail_day11_Monica"
    $ policeCellBedLabel = "jail_day11_Bed"
    $ policeCellCageLabel = "jail_day11_Cage"
    stop music fadeout 1.0
    call textonblack(_("ДЕНЬ 11"))
    img black_screen
    with Dissolve(1)
    music Jail_Clock

    img 2457
    with fadelong
    mt "Ура!"
    "Я скоро выберусь из этой мерзкой дыры!"
    img 2458
    "Конечно я не собираюсь оставлять мой дом этому ничтожеству."
    img 2459
    "Насколько я знаю эту риелторшу, она всегда оставляет запасные варианты."
    "Не может же она на самом деле оформить такой дом на какого-то бомжа!"
    "Я уверена, что я скоро снова буду жить в своем доме!"
    img 2460
    "Я клянусь себе в этом!!!"
    "Не вешать нос, Моника!"
    "Осталось всего пара дней!"
    img 2461
    "..."
    "Надо проверить, где там этот жирный урод..."
    call refresh_scene_fade()
    return

label jail_day11_Monica(obj_name, obj_data):
    if jailDaySceneStage == 0:
        mt "Где там этот жирный урод?"
    if jailDaySceneStage == 1:
        mt "Надо лечь на кровать и подождать его..."
    if jailDaySceneStage == 2:
        mt "Где там этот жирный урод?"
    if jailDaySceneStage == 3:
        mt "Я хочу лечь и поплакать. Может быть засну?"
    return

label jail_day11_Bed(obj_name, obj_data):
    if act == "l":
        call jail_day1_Bed(obj_name, obj_data)
        return

    if jailDaySceneStage == 0:
        mt "Где там этот жирный урод?"
    if jailDaySceneStage == 1:
        menu:
            "Лечь и ждать толстого урода?":
                pass
            "Не ложиться":
                return
        img black_screen
        with Dissolve(1)
        # пикча лежащей моники
        img 2436
        with fadelong

        mt "Прошло какое-то время... Может быть стоит проверить теперь?"
        $ jailDaySceneStage = 2
        return
    if jailDaySceneStage == 2:
        mt "Где там этот жирный урод?"
    if jailDaySceneStage == 3:
        mt "Я хочу лечь и поплакать. Может быть засну?"
        menu:
            "Лечь и плакать":
                pass
            "Не ложиться":
                return
        if jailCageBlackmailEnded == True:
            call jail_day12()
            return
        stop music fadeout 1.0
        call textonblack(_("Спустя некоторое время..."))
        music prison_yell_music
        img black_screen
        with Dissolve(1)
        mt "Какой-то шум..."
        "..."
        prisoner1 "Эй! Шлюха!"
        "Иди сюда!"
        "Мы хотим видеть тебя!"
        mt "..."
        mt "Я не буду вставать... я умру здесь... лучше..."
        mt "(хмык)"
        call jail_day12()
    return

label jail_day11_Cage(obj_name, obj_data):
    if jailDaySceneStage == 3:
        mt "Я не буду даже приближаться туда..."
        return

    if act == "l":
        call jail_cage_blackmail_day()
        call refresh_scene_fade()
        return
    if act == "w":
        $ cageInteractLabel = "jail_day11_Cage_Interact"
        call change_scene("police_jail_cage_scene")
        return

    return

label jail_day11_Cage_Interact:

    if jailDaySceneStage == 0:

    # выглядывает за решетку (интеракт)
        img 2462
        with fadelong
        mt "Его еще нет."
        "Это хорошо!"
        "Наверное он совершает сделку."
        "Потерпи, Моника!"
        "Потерпи!"
        $ jailDaySceneStage = 1
        return
    if jailDaySceneStage == 1:
        img 2253
        with fadelong
        mt "Никого нет..."

    if jailDaySceneStage == 2:
        img 2463
        with fadelong
        mt "Он пришел!"
        "Притащил свою жирную жопу!"
        "Надо узнать у него как дела!"
        "Я уверена что все хорошо!"
        # подходит
        music Power_Bots_Loop
        img 2464
        with fadelong
        overseer "А!!!"
        "Это снова ты!!!"
        "Можешь забыть про еду!"
        "Больше ты ничего не получишь!!!"

        img 2465
        m "Сэр!"
        "Но почему?"
        "Как Вы сходили?"
        "Вы все оформили?"

        overseer "Мы сходили плохо!"
        img 2466
        mt "БОЖЕ!"
        "ЧТО ЕЩЕ МОГ НАТВОРИТЬ ЭТОТ ТУПОЙ УРОД???"
        img 2467
        m "Сэр."
        "Простите."
        "Но что могло быть не так?"
        img 2468
        overseer "Что не так???"
        "Ты!"
        "Стерва!"
        "Ты обманывала меня с самого начала!"
        "Мы пришли перефоромлять в эту.. как его..."
        "В общем где переоформляют все."
        "Стали все делать."
        "Эта баба, которая делала."
        img 2469
        "С такими сиськами, Во!"
        img 2470
        m "Сэр!"
        "Пожалуйста!"
        "Хватит про сиськи!"
        "Что там случилось?"
        img 2471
        overseer "В общем эта баба."
        "Она и говорит что в доме этом уже кто-то живет."
        "И что он не твой."
        img 2472
        mt "НЕЕЕЕТ!"
        "КАК ТАКОЕ МОЖЕТ БЫТЬ???"
        img 2473
        m "Сэр!"
        "Я что-нибудь придумаю, обещаю!"
        img 2474
        overseer "И это еще не все."
        "В общем посмотрела эта баба свой телевизор."
        "И говорит."
        "Что такого человека вообще не существует."
        img 2475
        "..."
        "Ты!"
        "Стерва!"
        "С самого начала обманула меня!"
        "Придумала какое-то имя!"
        "И со своими подельниками хотела обхитрить меня!"
        "Но меня не так-то просто обхитрить!!!"
        img 2476
        m "Сэр!"
        "Это мое настоящее имя!"
        "Меня зовут Моника Бакфетт!!!"
        img 2477
        "Сэр!"
        "Пожалуйста!"
        img 2475
        overseer "Не ври мне тут!!!"
        "А я из-за тебя опоздал на службу!"
        "Теперь мне будет выговор!"
        "А если меня уволят, то что?"
        "Я уже не найду другой работы!"
        "Ты подставила меня!"
        "И ты за это ответишь!"
        "Да!"

        music Power_Bots_Loop
        img 2478
        with fadelong
        overseer "Ты жаловалась по поводу одежды!"
        "У тебя еще остались жалобы?"
        img 2479
        m "Сэр."
        "Конечно."
        "Мне очень неудобно все время находиться в нижнем белье."
        overseer "Я помогу тебе!"
        m "Спасибо, Сэр!"
        img 2480
        with fade
        "..."
        "Сэр?"
        img 2481
        with fadelong
        "Сэр?"
        "Сэр!!!"

        sound snd_break_dress
        sound snd_woman_scream1

        $ cloth_type = "Jail"
        $ cloth = "Nude"


        music Power_Bots_Loop
        img 2482
        with fadelong
        overseer "Так-то лучше!"
        "А то хожу по всяким местам."
        "Там у всех сиськи Во!"
        "Но никто не показывает их."
        "А так хоть буду смотреть на твои."
        "Почаще!"
        "Все какая-то радость от работы!"
        img 2483
        m "ЧТО ТЫ СДЕЛАЛ???"
        "УБЛЮДОК!!!"
        overseer "Ты больно строптивая."
        "Надо воспитать тебя."

        #
        img 5116
        with fadelong
        w
        img black_screen
        with Dissolve(1)
        img 5117
        with fadelong
        w
        sound snd_ui_connect
        img 5464
        w
        overseer "Холодная водичка пойдет тебе на пользу!"
        sound snd_water_hose
        img 5465
        w

#        sound snd_water_hose
#        $ renpy.pause(5.0)
        sound snd_woman_scream2
        img 5466
        w
#        $ renpy.pause(3.0)
        img 5467
        overseer "На! Отведай! Это тебе за то что хотела меня надуть!"
        sound snd_water_hose
        img 5465
        w
#        $ renpy.pause(5.0)
        sound snd_woman_scream2
        img 5468
        w
#        $ renpy.pause(3.0)
        img 5467
        overseer "Ишь сбежать захотела! Думала я тебя выводить буду?"
        "Отсюда нет выходов!!! Ха-ха-ха!"
        sound snd_water_hose
        img 5465
        w
#        $ renpy.pause(5.0)
        sound snd_woman_scream2
        img 5469
        w
#        $ renpy.pause(3.0)

        img black_screen
        with Dissolve(1)
        sound snd_bodyfall

        img 5470
        overseer "То-то же!"
        img 5471
        "Лежи, отдыхай здесь!"
#        img 5472
        "И про еду забудь теперь!!!"
        sound snd_jail_lock
        img black_screen
        with Dissolve(1)

        #
        music Power_Bots_Loop
        img 2484
        with fadelong
        mt "О Боже!"
        "Он сорвал с меня белье!"
        "Я абсолютно голая здесь!"
        img 2485
        mt "..."
        "У меня нет ни офиса."
        "Ни счетов."
        img 2486
        "Ни дома!"
        img 2487
        "Кто черт возьми живет в моем доме!!!"
        "Я убью его!!!"
        "Этого человека!!!"
        "..."
        img 2488
        "А этот!"
        "Жирный урод!"
        "Даже не собирался выводить меня!"
        if jailBoobsForFoodShowed == True:
            mt "Вместо этого он использовал меня, чтобы я показывала ему себя, свою грудь!"
            "Он обманывал меня!!!"
        if jailCageBlackmailBoobsShowed == True:
            mt "А эти! Ублюдки!"
            "Шантажировали меня!"
            "Заставили показывать свою грудь, кому попало!!!"
        if jailCageBlackmailMonicaSaidSheIsAWhore == True:
            mt "Заставили меня назвать себя... я даже не хочу произносить это..."
        if jailCageBlackmailAssShowed == True:
            mt "Заставили меня встать в какую-то унизительную позу!"
            "И ждут еще какого-то продолжения!"
            "Что теперь будет???"

        music Jail_Clock
        img 2489
        with fade
        mt "О Боже!"
        "Как мне отсюда выбраться!"
        "Я умру здесь!"
        $ jailDaySceneStage = 3
        $ jailScenePlace = 0
        $ policeJailObjectsEnabled = False
        $ policeCellStageName1 = "scene_Police_Cell_1_Day_11_2"
        $ policeCellStageName2 = "scene_Police_Cell_2_Day_11_1"
        $ policeCellMonica1 = "Police_Cell_1_Day_11_2"
        $ policeCellMonica2 = "Police_Cell_2_Day_11_1"
        call refresh_scene_fade()
    return

    #menu Лечь и ждать толстого урода?
    #Лечь и ждать
    #Не ложиться

    # выглядывает за решетку (интеракт)

    #

    #menu Я хочу лечь и поплакать. Может быть засну?




    return
