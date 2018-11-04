#default juliaMonicaYell = False #Моника обращается с Юлией криком
#default juliaPunished = False #жестко наказана, убирается на втором этаже каждый день
#default juliaPunishedLow = False #наказана криком, но разрешено не убирать пятно
#default juliaPunishedVoluntarily = False #мягко, разрешено убирать в свободное время
#default juliaPunishedNone = False #пятно есть, но Юлию не наказали вообще никак
#default juliaMonicaLied = False #Моника соврала что пятно поставила не она
default going_to_fitness_quest = False

label quest_house_monica_day2_day_init:
#    $ juliaPunished = False #debug
#    $ juliaPunishedLow = True #debug
#    $ juliaMonicaLied = False #debug
#    $ juliaPunishedVoluntarily = True #debug
#    $ juliaMonicaYell = False #debug
#    $ juliaPunishedNone = True #debug
#    $ juliaLocation = "floor1" #debug

    call textonblack(_("ДЕНЬ 2..."))
    img black_screen
    with Dissolve(1)
    $ changeDayTime("day")
    music BossaBossa

    img 1010
    with fadelong
    w
    img 1011
    w
    img 1013
    w
    img 1467
    mt "Новый чудесный день."
    if juliaPunished == True or juliaPunishedVoluntarily == True:
        "Если честно, мне немного мешал шум, который издавала Юлия."
    if juliaPunished == True:
        "Я даже сейчас его слышу."
    if juliaPunishedVoluntarily == True:
        "Сейчас этого шума уже нет.
        Видимо Юлия занята чем-то другим."

    if juliaPunished == True:
        img 1468
        mt "Но мне доставляет удовольствие то как она мучается."
        "Прямо приятно."

        img 1469
        "По всей видимости она так и не оттерла пятно."
        "Придется её уволить."
        "Мне не нужны люди, которые не могут справиться с задачей."
        "Или дать ей еще один день?"
        "Но ведь она не сможет оттереть это пятно."
        "Как бы ни старалась."

        img 1470
        "..."

        img 1471
        "Решено."
        "Завтра уволю её."
        "А сегодня пусть помучается."
        "Мне приятно."
        img 1472
        "В конце концов, я же правда добрая."
        "Я дам поработать человеку подольше."
        "Ведь ей нужна работа."
        "Ей очень нужно подметать тут все, убирать."
        "Готовить мне."
        "Стирать, гладить."
        img 1473
        "Ей это очень нужно."
        "Пусть еще один день она будет делать это."
        "..."

        img 1474
        "У меня был выбор."
        "Уволить ее сегодня."
        "Или уволить ее завтра."
        "Я выбрала добрый вариант."
        img 1475
        "Кто скажет что я не добрая?"
    else:
        img 1468
        if juliaMonicaLied == True:
            mt "Юлия поставила пятно на ковер.
            Ну с кем ни бывает, правда?"
            if juliaPunishedLow == True:
                img 1472
                mt "Эта сучка заслужила то чтобы убирать его, но я разрешила ей не делать этого."
        else:
            mt "Я случайно поставила пятно на ковер."
            if juliaPunishedLow == True:
                img 1472
                mt "Юлия, эта сучка, она обязана была убирать его, но я разрешила ей не делать этого."
        if juliaPunishedNone == True:
            mt "Но я не заставила Юлию убирать его вовсе!"

        if juliaPunishedVoluntarily == True:
            mt "Юлия вызвалась сама убирать его в свободное время."
            "Это она сама вызвалась, я не заставляла ее это делать!"
        img 1475
        "Кто скажет что я не добрая?"
        img 1474
        mt "Почему все считают меня сучкой?"
        img 1473
        mt "Посмотрите какая я на самом деле!"

    img 1476
    "..."
    "Итак."
    "Надо собираться."
    "Покушать, принять ванну."

    "И ехать по делам."

    "Я решительно собираюсь поехать в фитнес зал."

    "Там меня как раз ждут две подружки."

    "Стефани и Ребекка."

    img 1477
    "Мы любим друг перед другом хвастаться."

    "Я обычно побеждаю :)"

    img 1478
    "Еще мне надо заехать в Банк."
    "Проверить платеж от Стива."
    "Я чувствую что этот слизняк мне врет."
    "Да, и еще надо бы вернуть то платье."
    "Которое мы вчера купили с Диком."
    "Вечер был не очень."
    if dickMonicaSaidToFredOffend == True:
        "Дик испортил его.
        Жирный слизняк..."
        "Так что платье я принципиально верну."
    else:
        "У Дика не получается ухаживать, хотя он и старался..."
        "Однако платье я верну, принципиально."

    $ houseOutMode = "usual"
    $ bathTakenJust = False
    $ bathTaken = False
    $ monicaEated = False

    $ going_to_fitness_quest = True
    $ map_objects["Teleport_Fitness"]["state"] = "visible"
    $ add_objective("dress_homecloth", _("Одеть домашнюю одежду"), c_blue, 0)
    $ add_objective("take_bath", _("Принять душ"), c_green, 1)
    $ add_objective("eat", _("Позавтракать"), c_orange, 2)
    $ add_objective("go_outside_fitness", _("Одеться и ехать в фитнес зал"), c_orange, 10)
    $ drivingPlacePlannedArray["Fitness"] = "drive_speak_monica_fred_fitness"
    if juliaPunished == True:
        $ add_objective("julia_check_spot", _("Проверить Юлию"), c_red, 3)

    music Mandeville
    $ casualMusic = "Mandeville"
    call change_scene("bedroom1", "Fade_long")
#    call refresh_scene_fade_long()
    return

label quest_house_monica_day2_evening_init:
    imgc Dial_Monica_BusinessCloth2_Thinking
    mt "Мне надо переодеться."
    "Поесть."
    "Принять ванну и ложиться спать."
    $ remove_objective("return_to_home")
    $ add_objective("dress_homecloth", _("Одеть домашнюю одежду"), c_blue, 0)
    $ add_objective("take_bath", _("Принять душ"), c_green, 1)
    $ add_objective("eat", _("Поужинать"), c_orange, 2)
    $ add_objective("sleep", _("Лечь спать"), c_orange, 4)
    $ bathTakenJust = False
    $ bathTaken = False
    $ monicaEated = False
    $ houseOutMode = "evening2"
    $ wardrobeDay2EveningBlocked = False

    $ miniMapEnabledOnly = []

#    $ juliaMonicaForgivenessAfterPunishment = True #debug
#    $ juliaPunished = False #debug
#    $ juliaPunishedLow = True #debug
#    $ juliaMonicaLied = False #debug
#    $ juliaPunishedVoluntarily = True #debug
#    $ juliaMonicaYell = False #debug
#    $ juliaPunishedNone = True #debug
#    $ juliaLocation = "floor1" #debug
    return










#
