label jail_day13:
    $ jailDay = 13
    $ day = day + 1
    $ jailDaySceneStage = 0
    $ jailScenePlace = 0
    stop music fadeout 1.0
    call textonblack(_("ДЕНЬ 13"))
    img black_screen
    with Dissolve(1)
    music Jail_Clock

    img 2505
    with fadelong
    mt "Что же мне делать?"
    "(хмык)"
    "Мне конец..."
    "(хмык)"
    "Я умру здесь, умру!"

    music Groove2_85
    img black_screen
    with Dissolve(1)
    #заключенный подходит
    sound snd_jail_lock
    img black_screen
    with Dissolve(1)
    img 2505
    with fadelong
    overseer "Заходи, Джимми!"
    sound man_steps
    img 5473
    "Ты победитель!"
    img 5474
    "Но помни!"
    "Через две недели я тебя выселю отсюда!"
    img 5475
    prisoner "Нет проблем, Боб!"
    img 5476
    "Я буду торопиться!"
    "В день по пять раз - это семьдесят раз!"
    img 5477
    overseer "А ты сможешь?"
    prisoner "Смогу, Боб!"
    img 5478
    "Я уже давно не засовывал член в женскую киску!"
    img 5479
    "И в ротик!"
    "И в попу тоже!"
    img 5480
    overseer "Удачно провести время, Джимми!"

    img black_screen
    with Dissolve(1)
    #уходит
    sound snd_jail_lock
    img 5116
    with fadelong
    w
    music Groove2_85
    img 5481
    with fadelong
    prisoner "Ну что, детка!"
    img 5482
    "Знакомься с нами!"
    img 5483
    "Меня зовут Джимми!"
    img 5484
    "А это мой друг!"
    "Жесткий Боб!"
    img 5485
    with fadelong
    sound Jump2
    "Мы теперь будем жить вместе!"
    img 5486
    w
    img 5487
    w
    img 5488
    w
    img 5489
    w
    img 5490
    w
    img 5491
    "Ты ему понравилась!"
    img 5492
    w
    img 5493
    w
    img 5494
    w
    img 5495
    w

    stop music fadeout 0.5
    img black_screen
    with Dissolve(1)
    sound man_steps

    #заходит Маркус
    music Groove2_85
    img 5496
    with fadelong
    overseer "Всем тихо!"
    "Мистер Маркус идет!"
    img 5498
    w
    img 5497
    prisoner "Упс!"
    img 5499
    overseer "Быстро назад в свою камеру!!!"
    img 5500
    w

    sound snd_jail_lock
    img black_screen
    with Dissolve(1)

    #Маркус подходит к Бобу
    music Groove2_85
    img 5501
    with fadelong
    marcus "Добрый день, Боб!"
    overseer "Добрый день, Мистер Маркус!"
    "Что я могу для Вас сделать?"

    marcus "Как там новая заключенная?"

    overseer "Немного переживает, но в целом в порядке."
    "Еще не смирилась."
    marcus "Ясно."
    img 5502
    "Я сейчас проведу процесс с Господином Судьей, а потом вызову тебя, чтобы ты привел ее ко мне."
    overseer "Так точно, Мистер Маркус!"

    #В комнате допросов
    stop music fadeout 1.0
    call textonblack(_("СПУСТЯ 15 МИНУТ..."))
    img black_screen
    with Dissolve(1)
    music Groove2_85
    img 5503
    with fadelong
    judge "Хорошо, Маркус."
    "Я оформлю решение как полагается."
    "Не забудь меня пригласить, когда она станет покладистой."
    marcus "Конечно!"
    "До встречи!"
    judge "До встречи, Маркус."

    img black_screen
    with Dissolve(1)
    img 5503
    with fadelong
    sound snd_phone1
    overseer "Да, Мистер Маркус?"
    marcus "Боб, давай веди ее сюда!"
    "Пора ей узнать что ее ждет."
    overseer "Конечно, Мистер Маркус, одну минуту!"

    img black_screen
    with Dissolve(1)
    img 2507
    with fadelong
    overseer "Эй!"
    "Давай вставай!"
    "Хватит тут отдыхать!"
    "Мистер Маркус вызывает тебя!"
    img 2508
    m "Мистер Маркус!"
    "Все-таки он согласился со мной поговорить?"
    "Пожалуйста, отведите меня к нему!"
    img 2509
    "Я все ему объясню!"
    "Это какая-то ошибка!"
    "Он должен выпустить меня отсюда!"
    img 2510
    overseer "Вот вставай и иди."
    "Я тебя не собираюсь нести к нему."

    #
    img 2511
    with fadelong
    overseer "Иди за мной!"

    if jailCageBlackmailMonicaSaidSheIsAWhore == True:
        img 5504
        with fade
        sound prison_yell
        prisoner2 "Шлюха! Шлюха!"
        img 5505
        with fade
        prisoner1 "Хорошая Шлюха!"

        sound prison_yell
        img 5506
        with fade
        prisoner3 "Хорошая Шлюха!"
        img 5507
        with fade
        prisoner4 "Да! Хорошая Шлюха!"
        img 5508
        with fade
        prisoner1 "Хорошая Шлюха!"
        sound prison_yell
        img 5509
        with fade
        prisoner6 "Шлюха! Хорошая!"
        img 5510
        with fade
        prisoner5 "Хорошая Шлюха!"
        sound prison_yell
        img 5511
        with fade
        prisoner2 "Шлюха! Шлюха!"
        img 5512
        with fade
        sound prison_yell
        prisoner1 "Хорошая Шлюха!"
        img 5513
        with fade
        w
        img 5514
        with fade
        w
        sound prison_yell
        img 5515
        with fade
        w
        img 5516
        with fade
        w
        sound prison_yell
        img 5517
        with fade
        w
    else:
        sound prison_yell
        img 5504
        with fade
        prisoner2 "Шлюха! Шлюха!"
        img 5505
        with fade
        prisoner1 "Шлюха!"

        sound prison_yell
        img 5506
        with fade
        prisoner3 "Шлюха!"
        img 5507
        with fade
        prisoner4 "Да! Шлюха!"
        sound prison_yell
        img 5508
        with fade
        prisoner1 "Шлюха!"
        img 5509
        with fade
        prisoner6 "Шлюха!"
        sound prison_yell
        img 5510
        with fade
        prisoner5 "Шлюха!"
        sound prison_yell
        img 5511
        with fade
        prisoner2 "Шлюха! Шлюха!"
        img 5512
        with fade
        prisoner1 "Шлюха!"
        img 5513
        with fade
        w
        sound prison_yell
        img 5514
        with fade
        w
        img 5515
        with fade
        w
        sound prison_yell
        img 5516
        with fade
        w
        img 5517
        with fade
        w

    img black_screen
    with Dissolve(1)
    img 2512
    with fadelong
    overseer "Мистер Маркус!"
    "Заключенная доставлена."
    img 2513
    marcus "Хорошо, Боб."
    "Можешь ступать."
    img 2514
    overseer "Мистер Маркус!"
    "Если я понадоблюсь, только позовите!"
    img 2515
    marcus "Не надоедай, Боб!"
    "Брысь отсюда."
    overseer "Так точно, Мистер Маркус!"
    $ autorun_to_object("police_jailcabinet", "jail_cabinet_dialogue1")
    call change_scene("police_jailcabinet", False, False)
    return
