label jail_day12:
    $ jailDay = 12
    $ day = day + 1
    $ jailDaySceneStage = 0
    $ jailScenePlace = 0
    $ policeJailObjectsEnabled = True
    $ policeCellStageName1 = "scene_Police_Cell_1_Day_12_1"
    $ policeCellStageName2 = "scene_Police_Cell_2_Day_12_1"
    $ policeCellMonica1 = "Police_Cell_1_Day_12_1"
    $ policeCellMonica2 = "Police_Cell_2_Day_12_1"
    $ policeCellMonicaLabel = "jail_day12_Monica"
    $ policeCellBedLabel = "jail_day12_Bed"
    $ policeCellCageLabel = "jail_day12_Cage"
    stop music fadeout 1.0
    call textonblack(_("ДЕНЬ 12"))
    img black_screen
    with Dissolve(1)
    music Jail_Clock

    img 2490
    with fadelong
    mt "О Боже!"
    "О Боже!!"
    "О Боже!!!"
    img 2491
    "Я совершенно голая!"

    img 2492
    mt "Мне вообще нечем прикрыться!!!"
    img 2493
    mt "И я уже хочу есть!"
    "Он сказал что снова перестанет меня кормить!"
    img 2494
    mt "О Боже!"
    "Как мне выжить???"
    call refresh_scene_fade()
    return

label jail_day12_Monica(obj_name, obj_data):
    if jailDaySceneStage == 0:
        mt "Я совершенно голая!"
        mt "Мне вообще нечем прикрыться!!!"

    if jailDaySceneStage == 1:
        call jail_day13()
        return
    return

label jail_day12_Bed(obj_name, obj_data):
    if act == "l":
        call jail_day1_Bed(obj_name, obj_data)
        return

    if jailDaySceneStage == 0:
        mt "Я не могу спать!"
        mt "Я совершенно голая!"
        mt "Мне вообще нечем прикрыться!!!"
        return
    return

label jail_day12_Cage(obj_name, obj_data):
    if act == "l":
        mt "Я не буду смотреть на этих... у меня даже нет слов..."
        return
    if act == "w":
        $ cageInteractLabel = "jail_day12_Cage_Interact"
        call change_scene("police_jail_cage_scene")
        return

    return

label jail_day12_Cage_Interact:
    music Groove2_85
    img 2495
    with fadelong
    overseer "Что стучишь?"
    "Жрать не дам!!!"
    img 2496
    m "Сэр!"
    "Пожалуйста!"
    "Дайте мне хоть что-нибудь чтобы прикрыться!"
    overseer "Тебе больше незачем прикрываться."
    "Привыкай."
    img 2497
    m "Сэр!"
    "Но почему?"
    "К чему я должна привыкать?"
    overseer "К тому что тебя каждый день будут трахать."
    music Power_Bots_Loop
    img 2498
    with fade
    m "О Боже!!!"
    "КТО???"
    img 2499
    overseer "А ты не знала?"
    "Ах да, я же тебе не говорил."
    "Понимаешь. У меня часто болит голова."
    "А заключенные ведут себя шумно."
    "Недавно мне кто-то из них сказал идею."
    "Как раз тогда поступила заключенная, которая до тебя."
    "В общем это что-то вроде конкурса."
    "Все ведут себя тихо."
    "Кто отличится и вообще не проронит ни звука, тот будет победителем."
    "И того я награждаю."
    img 2498
    m "Ссссэр..."
    "И в чем награда?"
    img 2499
    overseer "Я его переселяю к заключенной."
    "У нас правила это не разрешают, но никому особо нет дела."
    "А у меня голова зато не болит!"
    "Потому что никто не шумит!"
    img 2498
    m "И что, вы подселите его ко мне?"
    "И что будет?"
    img 2499
    overseer "Как что?"
    "Я думаю тебя будут трахать целыми днями, ведь ему надо торопиться."
    img 2500
    m "Ккккуда? Торопиться."

    img 2499
    overseer "Как куда?"
    "Через две недели будет другой победитель, а тот кто уже выиграл, тот не участвует в конкурсе."
    img 2500
    m "То есть потом вы подселите кого-то другого?"
    img 2499
    overseer "Конечно!"
    "Такого же голодного!"
    "Ведь все должны получить желаемое, так ведь?"
    "Это же справедливо?"
    "Я думаю ты за справедливость, правда?"
    img 2501
    "Вот."
    "А в прошлый раз победитель пришел и стал рвать одежду на заключенной."
    "А она давай сопротивляться."
    "Он стянул с нее колготки, а они запутались в ногах."
    "Она и упала на пол."
    "И потеряла товарный вид."
    "Ее и увезли."
    "Так ее и нет."
    "Это было как раз до тебя."
    "Она была в твоей камере."
    "Потому я и решил что без одежды тебе безопаснее."
    img 2502
    "Я же о тебе переживаю!"
    "Ты этого не ценишь!"
    img 2503
    m "ССсссэр..."
    "И когда будет победитель?"
    img 2499
    overseer "Так завтра!"
    "Как раз пройдет две недели!"

    #падает
    sound snd_bodyfall
    img black_screen
    with Dissolve(1)

    music Groove2_85
    img 2504
    with fadelong
    overseer "Не хочешь больше ничего узнать?"
    "А много чего еще есть интересного."
    "Ну как хочешь."
    "Лежи тут отдыхай."
    music Jail_Clock
    $ policeCellStageName1 = "scene_Police_Cell_1_Day_12_2"
    $ policeCellStageName2 = "scene_Police_Cell_2_Day_12_2"
    $ policeCellMonica1 = "Police_Cell_1_Day_12_2"
    $ policeCellMonica2 = "Police_Cell_2_Day_12_2"
    $ policeJailObjectsEnabled = False
    $ policeJailObjectsBed1Enabled = False
    $ policeJailObjectsTeleportForced = True
    $ jailDaySceneStage = 1
    call refresh_scene_fade()

    return
