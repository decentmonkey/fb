default fitness1_trainer_talk2_choice_rough = False

label fitness1_trainer_talk1:
    if fitnessMonicaTrained == False:
        img 1521
        fitness_instructor "Добрый день, Моника!"
        "Ты, как всегда, выглядишь неотразимо!"

        m "Спасибо."

        img 1522
        mt "Не помню как его зовут."

        img 1521
        fitness_instructor "Моника, ты можешь идти переодеваться и мы начнем заниматься."

        m "Да, хорошо."
        $ add_objective("change_cloth_to_fitness", _("Переодеться в раздевалке"), c_green, 20)
    return

label fitness1_stephanie_rebecca_talk1:
    #2 - stephanie, 1- rebecca
    music BossaBossa
    img 1524
    img 1525
    img 1523
    rebecca "Привет, Моника!"

    stephanie "Привет, подружка!"

    img 1526
    m "Привет, девочки."
    "Хорошо выглядите."

    img 1527
    rebecca "Мы девочки."
    "Мы должны хорошо выглядеть!"

    stephanie "Для этого мы сюда и ходим."

    img 1528
    stephanie "Моника, ты выглядишь тоже великолепно."

    img 1529
    rebecca "Да, Моника."
    "Ты выглядишь супер!"

    img 1530
    m "Спасибо, девочки."
    "Я знаю."

    img 1531
    rebecca "Моника."
    "Расскажи."
    "Что у тебя новенького?"
    "Нам интересно!"

    stephanie "Ты говорила у тебя уехал муж?"

    rebecca "А ты встречалась с Диком?"
    "У вас было свидание?"

    stephanie "Ну и как он в постели?"

    rebecca "А что он тебе подарил?"

    img 1532
    m "Да, мой тюфяк уехал."
    "По работе."
    "Я даже ему не звонила."
    "Не знаю что с ним и как он."
    "Да мне и неинтересно, если честно."

    img 1533
    rebecca "А Дик?"

    img 1534
    stephanie "Ты встречалась с ним?"

    img 1535
    m "Ой, девочки..."
    "Да, встречалась."
    "Он влюблен в меня без ума."

    img 1536
    rebecca "Правда?"

    stephanie "Он тебе сказал?"

    img 1537
    m "Ему не надо было этого говорить."
    "Я видела его щенячьи глаза, полные преданности."

    img 1538
    rebecca "Как прошло свидание?"

    stephanie "Расскажи скорее!"
    "Нам же интересно!"

    menu:
        "Все было потрясающе.":
            img 1539
            m "Что рассказывать..."
            "Все было потрясающе, как всегда у меня бывает."
            "Сначала мы ездили по магазинам."
            "Он покупал мне подарки."
            "Подносил мне то одно, то другое."

            img 1540
            "Смотрел на меня как на богиню."
            "Потом мы ездили по ресторанам."
            call bitch(-1, "fitness_dick1")
            "Все было на высоте."

            img 1541
            mt "Не скажу же я что свидание было дурацким."

        "Дик идиот!":
            img 1532
            m "Что рассказывать..."
            "Вы знаете мой уровень?"
            img 1533
            rebecca "Конечно, Моника, мы знаем!"
            img 1539
            m "Ну так вот, Дик ему не соответствует!"
            call bitch(1, "fitness_dick1")
            "У него не хватает интеллекта и много чего другого!"
            "Но он старался."
            "Сначала мы ездили по магазинам."
            "Он покупал мне подарки."
            "Подносил мне то одно, то другое."

            img 1540
            "Смотрел на меня как на богиню."
            "Потом мы ездили по ресторанам."

    img 1542
    rebecca "А что потом?"

    stephanie "Вы спали вместе?"

    img 1543
    m "Ой, девочки."
    "Ну что вы?"
    "Ну конечно нет."
    "Я же себя уважаю."
    "Я не стану спать с таким как он."
    "Мне нравятся мачо."
    "Но те кого я встречала полные болваны."
    "А я такого не хочу."

    img 1544
    stephanie "Такие мачо как наш инструктор?"

    img 1545
    m "Ты шутишь?"
    "Мне нравятся мачо."
    "Но чтобы они были богатые и знаменитые."
    "А наш инструктор - нищий болван."
    "Если ему кто и даст, то только какая-нибудь глупая провинциалка."

    img 1546
    stephanie "Это точно."
    "Хи-хи"
    "Ты, как всегда права."

    img 1547
    rebecca "Вот ты даешь."
    "Моника!"
    "Ты такая крутая!"

    stephanie "Да!"
    "Вертеть Диком Адвокатом!"
    "Это высший класс!"
    "Говорят у него железный характер!"

    img 1548
    m "Фи."
    "Со мной он ведет себя как плюшевый мишка."
    "Я поиграю с мишкой еще немного."
    "Потом заведу новую игрушку."

    img 1549
    m "А у вас что нового?"

    img 1550
    stephanie "Я познакомилась с одним мачо."
    "Он известен, но пока не очень богат."
    "Мы занимаемся сексом каждый день."

    img 1549
    m "И что, нравится?"

    stephanie "Для меня да, но тебе наверное не понравится."

    m "Просто уверена."

    menu:
        "Стефани, ты ведь не провинциалка?":
            img 1543
            m "Стефани, ты ведь не провинциалка?"
            img 1555
            stephanie "Конечно нет, Моника!"
            "Я бы никогда не дала такому идиоту как наш инструктор. Тот парень совсем другой!"
            "Я ведь уважаю себя, Моника!"
            "И я равняюсь на тебя!"
            img 1549
            m "То-то же, Стефани!"
            "Не красней, я разбираюсь в людях."
            "И я знаю что ты бы не опустилась до такого."
            call bitch(1, "fitness_stephanie1")

        "...":
            pass

    img 1551
    rebecca "А я развела своего тюфяка на новый бриллиант."
    "Размером с карат, представляешь?"

    img 1549
    m "Фи. Карат."
    "У меня таких несколько."

    img 1549
    m "Ладно, девочки."
    "Я пойду заниматься."
    "Поболтаем еще потом."

    img 1553
    rebecca "Конечно, Моника!"
    "Поболтаем."
    "Расскажешь что у тебя будет дальше с Диком?"

    img 1549
    m "Конечно, девочки."
    "От вас у меня секретов нет, вы знаете."

    img 1553
    stephanie "Пока, Моника!"
    "Чмок!"

    m "Пока, девочки."


    music casualMusic
    $ fitnessStephanieRebeccaTalked = True
    call refresh_scene()
    return


label fitness1_rebecca_talk2():
    img 1554
    rebecca "Моника, ты такая классная!"
    m "Ты тоже, Ребекка."
    return
label fitness1_stephanie_talk2():
    img 1555
    stephanie "Моника, как ты поддерживаешь такую хорошую форму?"
    return

label fitness1_change_cloth1():
    img 1552
    with fade
    m "Девочки, я буду переодеваться. Вы можете идти."
    img 1547
    rebecca "Конечно, Моника! Мы уже закончили, мы уходим!"

    #
    # fade
    mt "Надо быстро переодеться и идти заниматься."
    music DarxieLand
    img 4697
    w
    img 4698
    w
    img 4699
    w
    img 4700
    w
    img 4701
    w
    img 4702
    w

    # сцена переодевания to_do!!!

    sound snd_fabric1
    img 1556
    with fadelong
    w
    img 1557
    w
    $ cloth = "FitnessSuit"
    $ cloth_type = "FitnessSuit"
    $ fitnessStephanieRebeccaInLocker = False
    call refresh_scene_fade_long()


    $ remove_objective("change_cloth_to_fitness")
    $ add_objective("fitness_go_workout", _("Идти заниматься Йогой"), c_orange, 20)
#    $ remove_objective("change_cloth_to_fitness", _("Переодеться в раздевалке"), c_green, 20)
    return

label fitness1_trainer_workout():
    menu:
        "Начать заниматься Йогой.":
            pass
        "Позже...":
            return
    music living_the_daydream
    img 1558
    with fadelong
    w
    img 1559
    w
    img 1560
    w
    img 1561
    w
    img 1562
    w
    img 1563
    w
    img 1564
    w
    img 1565
    w
    img 1566
    w
    img 1567
    w
    img 1569
    w
    img 1570
    w
    img 1571
    w
    img 1572
    w
    img 1573
    w
    img 1574
    w
    img 1575
    w
    img 1576
    w
    img 1577
    w
    img 1578
    w
    img 1579
    w
    img 1580
    w
    img 1581
    w
    img 1582
    w
    img 1583
    w
    img 1584
    w
    img 1586
    w
    img 1587
    w
    img 1588
    w
    img 1589
    w
    img 1590
    w
    img 1591
    w
    img 1592
    w
    img 1593
    w
    img 1594
    w
    img 1595
    w
    img 1596
    w
    img 1597
    w
    img 1598
    w
    img 1599
    w
    img 1600
    w
    img 1601
    w
    img 1602
    w
    img 1603
    w
    img 1604
    w
    img 1605
    w
    img 1606
    w
    img 1608
    w
    img 1613
    w
    img 1614
    w
    img 1615
    w
    img 1616
    w
    img 1617
    w
    img 1618
    w
    img 1619
    w
    img 1620
    w
    img 1621
    w
    img 1622
    w
    img 1623
    w
    img 1624
    w
    img 1625
    w
    img 1626
    w
    img 1627
    w
    img 1628
    w
    img 1629
    w
    img 1630
    w
    img 1631
    w
    img 1632
    w
    img 1633
    w
    img 1634
    w
    img 1635
    w
    img 1636
    w
    img 1637
    w
    img 1638
    w
    img 1639
    w
    img 1640
    w
    img 1641
    w
    img 1642
    w
    img 1643
    w
    img 1644
    w
    $ remove_objective("fitness_go_workout")
    $ autorun_to_object("fitness_gym", "fitness1_trainer_talk2")
    $ fitnessMonicaTrained = True
    $ map_objects["Teleport_Bank"]["state"] = "visible"
    music casualMusic
    call refresh_scene_fade_long()
    return
label fitness1_trainer_talk2:
    img 1645
    with fade
    fitness_instructor "Браво, Моника!"
    "Ты в отличной форме!"
    "Хочешь я могу дать тебе частные уроки после занятий?"
    menu:
        "Отшить грубо!":
            $ fitness1_trainer_talk2_choice_rough = True
            img 1646
            m "Нет уж."
            "Спасибо."
            "Клейся к кому-нибудь другому."
            call bitch(1, "fitness_trainer1")
            "Обезъяна."
            img 1647
            fitness_instructor "..."
        "Сказать НЕТ...":
            m "Спасибо, но я и так хорошо справляюсь!"
    call refresh_scene_fade_long()
    $ add_objective("fitness_change_cloth_to_bc1", _("Переодеться в раздевалке"), c_pink, 20)

    return

label fitness1_trainer_talk2_repeat:
    img 1645
    with fade
    fitness_instructor "Браво, Моника!"
    "Ты в отличной форме!"
    "Хочешь я могу дать тебе частные уроки после занятий?"
    if fitness1_trainer_talk2_choice_rough == True:
        img 1646
        m "Нет уж."
        "Спасибо."
        "Клейся к кому-нибудь другому."
        "Обезъяна."
        img 1647
        fitness_instructor "..."
    else:
        m "Спасибо, но я и так хорошо справляюсь!"
    call refresh_scene_fade_long()
    return

label fitness1_change_cloth2:
    mt "Приятная расслабленность."
    "Можно переодеться неспеша..."
    call stephanie_fitness_looking_monica()
    sound snd_fabric1
    img 1648
    with fadelong
    mt "Я готова!!"
    "Надрать кому-нибудь задницу!"
    "..."
    "Ладно."
    "Пора заняться делами."
    "Надо заехать в Банк."
    $ going_to_fitness_quest = False
    $ cloth = "BusinessCloth2"
    $ cloth_type = "BusinessCloth"
    $ remove_objective("fitness_change_cloth_to_bc1")
    $ add_objective("goto_bank1", _("Ехать в Банк по вопросу денег от Стива"), c_red, 20)
    call refresh_scene_fade_long()

    return
