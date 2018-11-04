default julia_monica_revenge_in_progress = False
default julia_monica_revenge_undo_in_progress = False

label floor2_julia_monica_revenge_start:
    $ miniMapEnabledOnly = ["Floor2"]

    call question_helper_enable("question_helper_hairdye")

    m "Хм...
    Я обожглась когда гладила платье."

    $ juliaLocation = "floor1"
    wc
    img 1061
    "Это случилось из-за того что Юлия не приготовила его."
    "Неужели я это просто так оставлю?"

    menu:
        "Я это так не оставлю, эту сучку Юлию надо наказать!":
            $ julia_monica_revenge_in_progress = True
            call bitch(5, "monica_julia_revenge_begin") from _call_bitch_13
            img 1061
            "Как бы наказать Юлию?"

            "То что я заберу половину зарплаты за это и все премиальные - это само собой."

            "Надо что-то еще..."

            "Может что-нибудь разлить?
            Чтобы эта сучка замучалась убирать!"

            "Надо поискать что-нибудь у зеркал, на столике для косметики!"

        "Юлия и так много работает. Возможно она просто не успела погладить платье.":
            $ julia_monica_revenge_undo_in_progress = True
            $ julia_monica_revenge_in_progress = True
            call bitch(-5, "monica_julia_revenge_begin") from _call_bitch_14
            m "Юлия и так много работает.
            Она очень устает и, возможно, просто забыла приготовить платье."

            "Но это не изменяет того что я должна ее проучить!"
            "Может что-нибудь разлить?
            Чтобы Юлии пришлось убирать?"

            "Не знаю правильно это или нет, но я, пожалуй, сделаю это."

            "Надо поискать что-нибудь у зеркал, на столике для косметики!"

    $ add_objective("find_hair_dye", _("Найти что-нибудь что можно разлить и напакостить Юлии"), c_pink, 20)
    $ subst_to_object("Teleport_Floor2_Stairs", "floor2_julia_monica_revenge_block_exits")
    $ subst_to_object("Teleport_Bedroom", "floor2_julia_monica_revenge_block_exits")
    $ subst_to_object("Teleport_Bathroom", "floor2_julia_monica_revenge_block_exits")
    $ hairDyeSearchMode = True

    return

label floor2_julia_monica_revenge_hair_dye_taken:
    $ remove_objective("find_hair_dye")
    $ add_objective("spill_hair_dye", _("Разлить куда-нибудь краску для волос"), c_red, 20)
    $ autorun_to_object("floor2", "floor2_julia_monica_revenge_look_for_spill_hair_dye")
    return

label floor2_julia_monica_revenge_look_for_spill_hair_dye:
    img 1063
    with fade
    m "Хорошо!"

    img 1064
    m "Теперь надо разлить ее куда-то."
    "Например вот туда, на ковер."
    return

label floor2_julia_monica_revenge_block_exits(obj_name, obj_data):
    if julia_monica_revenge_undo_in_progress == False:
        m "Я никуда не уйду пока не сделаю что-нибудь, чтобы наказать эту сучку Юлию!
        Как она смеет?!"
    else:
        m "Я не хочу уходить пока не сделаю что задумала."
    return


label floor2_julia_monica_revenge_spill_hairdye_confirm:
    menu:
        "Разлить краску на ковер.":
            jump Carpet_use_hairdye
        "Не разливать красу.":
            return

label Carpet_use_hairdye:
    #разливаем краску на ковер
    $ remove_objective("spill_hair_dye")
    img 1064
    $ renpy.pause(1.5, hard=True)
    sound snd_wet_dirt
    img black_screen
    with dissolve
    $ remove_inventory("hairdye", 1, True)
    $ renpy.pause(4.0, hard=True)
    img 1065
    with dissolve
    if julia_monica_revenge_undo_in_progress == False:
        m "Отлично!
        Так-то лучше!"

        "Все.
        Теперь я себя чувствую отлично."

        "Можно ехать по делам."
    else:
        m "Не знаю правильно-ли я сделала.
        Но теперь ничего не изменишь."

        "Хотя, все-равно я хотела менять этот ковер."
        "Ладно, поеду по делам."

    $ floor2SpotJustMade = True
    $ floor2SpotEnabled = True

    $ miniMapEnabledOnly = []
#    call miniMapAddDisabled("Street_Yard")
    $ miniMapSubst["Street_Yard"] = "miniMapJuliaRevengeFloor1Catch"


    call question_helper_disable()

    $ subst_to_object("Teleport_Floor2_Stairs", False)
    $ subst_to_object("Teleport_Bedroom", False)
    $ subst_to_object("Teleport_Bathroom", False)
    $ subst_to_object("Teleport_Street", "floor2_julia_monica_revenge_julia_need_catch")
    $ scene_transition = "Fade"
    call refresh_scene() from _call_refresh_scene_1

    $ autorun_to_object("floor1", "floor2_julia_monica_revenge_julia_catch")

    return

label miniMapJuliaRevengeFloor1Catch:
    call change_scene("floor1")
    $ miniMapSubst["Street_Yard"] = False
    return False

label floor2_julia_monica_revenge_julia_need_catch(obj_name, obj_data):
    m "Надо сначала поговорить с Юлией, потом уже идти на улицу."
    return
label floor2_julia_monica_revenge_julia_catch:
    if julia_monica_revenge_in_progress == True:
        jump floor2_julia_monica_revenge_julia_punish
#    if julia_monica_revenge_undo_in_progress == True:
#        jump floor2_julia_monica_revenge_julia_punish_undo

    return

label floor2_julia_monica_revenge_julia_punish:
    mt "Ага!"
    "А вот и Юлия!"
    if julia_monica_revenge_undo_in_progress == False:
        "Попалась, мелкая сучка!"
    $ miniMapSubst["Street_Yard"] = False
    call miniMapAddDisabled("Street_Yard")

    return
label floor2_julia_monica_revenge_julia_punish2:

    if obj_data["action"] == "l":
        mt "Ага!"
        "А вот и Юлия!"
        if julia_monica_revenge_undo_in_progress == False:
            "Попалась, мелкая сучка!"
        return
    img 1066

    call miniMapRemoveDisabled("Street_Yard")
    if julia_monica_revenge_undo_in_progress == False:
        m "ЮЛИЯ!
        БЫСТРО КО МНЕ!!!"
    else:
        m "Юлия!
        Можешь, пожалуйста, подойти ко мне?"
    wc
    sound highheels_run1
    img 1067
    with fade
    julia "Да, Миссис Бакфетт?
    Я Вас слушаю"

    if julia_monica_revenge_undo_in_progress == False:
        img 1068
        m "У меня к тебе два вопроса.
        Но ты должна хорошо подумать что ответишь на них."

        "От этого зависит выйдешь-ли ты завтра на работу или нет."

        if juliaPraiseOnOccasion == True:
            m "И я не посмотрю на то что ты вкусно готовишь."

        "Тебе понято???"
    else:
        img 1070
        if juliaPraiseOnOccasion == True:
            m "Хотела сказать тебе, что ты вкусно готовишь, Юлия"
            "Но это еще не все."
            m "У меня есть пара вопросов к тебе."
        else:
            m "У меня есть пара вопросов к тебе, Юлия.
        Я бы хотела задать их тебе."

    julia "Да, Миссис Бакфетт."
    if julia_monica_revenge_undo_in_progress == False:
        img 1069
        "Задавайте.
        Только пожалуйста, не увольняйте меня."
    else:
        img 1071
        "Задавайте."

    img 1070
    m "Первый вопрос."
    if julia_monica_revenge_undo_in_progress == False:
        "ГДЕ ТЫ БЫЛА??
        Я ИСКАЛА ТЕБЯ!!!"
    else:
        "Я не могла тебя нигде найти."


    if julia_monica_revenge_undo_in_progress == False:
        img 1071
        if juliaNeedToCheckStreet == True:
            julia "Но Миссис Бакфетт."
            "Вы сами приказали мне идти на улицу посмотреть что случилось."

            julia "Там человек из соседнего дома поцарапал газонокосилкой наш забор."
            "Из-за этого был шум с утра."

            img 1072
            mt "Хм.
            Я правда приказывала ей."

            "Но где она так долго шлялась?
            Почему столько времени?"

            img 1073
            m "Почему ты так долго ходила?
            Неужели не выйти и не вернуться через минуту?"
        else:
            if juliaHasSexInPool == True:
                julia "Миссис Бакфетт...."
                "Я.. мммм...."
                "Я просто выходила вынести мусор!!
                Да!"
            else:
                julia "Миссис Бакфетт..."
                "В это время регулярно подъезжает служба забора мусора."
                "Я следовала инструкциям и передала весь мусор им."
    else:
        img 1074
        if juliaNeedToCheckStreet == True:
            julia "Но Миссис Бакфетт."
            "Вы сами приказали мне идти на улицу посмотреть что случилось."

            julia "Там человек из соседнего дома поцарапал газонокосилкой наш забор."
            "Из-за этого был шум с утра."

            m "Ах, да, точно.
            Я совсем забыла."
            "Извини."
        else:
            if juliaHasSexInPool == True:
                julia "Миссис Бакфетт...."
                "Я.. мммм...."
                "Я просто выходила вынести мусор!!
                Да!"
            else:
                julia "Миссис Бакфетт..."
                "В это время регулярно подъезжает служба забора мусора."
                "Я следовала инструкциям и передала весь мусор им."



    if julia_monica_revenge_undo_in_progress == False:
        m "ТЫ БЫЛА НУЖНА МНЕ!"

        m "ЗДЕСЬ!!!"
        img 1074
        julia "Миссис Бакфетт.
        Пожалуйста, простите меня."

        if juliaNeedToCheckStreet == True:

            "Дело в том что я не видела что произошло на улице."

            "Но там был Фред.
            Ваш водитель."

            "Он рассказал мне в подробностях как все случилось."

            "Я подумала что очень важно донести до Вас все в мельчайших деталях."

            "Разговор занял у меня буквально 5 минут.
            Ведь времени прошло совсем немного.
            Взгляните на часы."
        else:
            "Я старалась управиться как можно быстрее."
            "Все заняло не более 5 минут."
            "Ведь времени прошло совсем немного.
            Взгляните на часы."

    else:
        m "Мне была нужна твоя помощь, Юлия."
        julia "Миссис Бакфетт.
        Ведь времени прошло совсем немного.
        Взгляните на часы."


    img 1075
    mt "Хм.
    Времени и правда прошло мало."

    "Видимо для меня поход в подвал был стрессом.
    И время шло очень медленно."

    if julia_monica_revenge_undo_in_progress == False:
        img 1076
        m "Второй вопрос!"

        m "ПОЧЕМУ НЕ ГОТОВО МОЕ ПЛАТЬЕ???"

        m "Оно оказалось не только не принесенным!
        Но и не поглаженным!"

        img 1077
        julia "Но Миссис Бакфетт!"

        "Вы говорили мне приготовить его завтра!"

        "Я собиралась гладить и приводить в порядок весь оставшийся вечер!"

        julia "Я бы легла посреди ночи, если бы понадобилось.
        Но я сделала бы это платье неотразимым!"
    else:
        img 1075
        m "Второй вопрос, Юлия."
        "Я не смогла найти своего платья."
        "Ты забыла его погладить?"

        img 1077
        julia "Миссис Бакфетт."
        "Я никогда ничего не забываю из своих обязанностей."
        "Вы говорили приготовить платье завтра.
        И я это помню..."

    img 1078
    mt "Хм.
    Мне действительно вчера позвонил Дик и уговорил меня встретиться сегодня."

    mt "Я совсем забыла сказать об этом Юлии."

    if julia_monica_revenge_undo_in_progress == False:
        mt "Нет, но вы посмотрите какая сучка.
        На все у нее есть ответ!"

        mt "Вот такие они все.
        Эти никчемные работники!"

        "Все у них хорошо, а крайняя остаюсь как-будто Я!"

        "Ну посмотрим что ты скажешь теперь..."
    else:
        mt "Получается Юлия не виновата?
        И я зря сделала это пятно?"

    if julia_monica_revenge_undo_in_progress == False:
        img 1079
        m "ЮЛИЯ!!!"

        julia "Да, Миссис Бакфетт?"

        m "ИДИ ЗА МНОЙ, НАВЕРХ!"
    else:
        img 1075
        m "Юлия.
        Наверху случился небольшой несчастный случай."
        "Пойдем я тебе покажу."
        julia "Да, Миссис Бакфетт, пойдемте."

label skip11:

    $ autorun_to_object("floor2", "floor2_julia_monica_revenge_go_to_floor2")
    call change_scene("floor2") from _call_change_scene_35

    return

label floor2_julia_monica_revenge_go_to_floor2:
    $ floor2SpotJustMade = False
    if julia_monica_revenge_undo_in_progress == False:
        img 1080
        with fade
        m "ВОТ!"
        menu:
            "Обвинить во всем Юлию":
                m "ВОТ!"
                m "ПОСМОТРИ ЧТО ТЫ НАДЕЛАЛА!!!"
                call bitch(5, "monica_julia_revenge_lie") from _call_bitch_15
                $ juliaMonicaLied = True
                img 1092
                julia "Аххххх!!!"

                img 1081
                julia "Но Миссис Бакфетт!
                Когда я проходила здесь в последний раз, этого пятна не было!"

                img 1082
                m "И?"

                "ЧТО ТЫ ХОЧЕШЬ СКАЗАТЬ?"

                "ЧТО ЭТО Я ПОСТАВИЛА ЭТО ПЯТНО???"

                img 1083
                julia "Нет, конечно, Миссис Бакфетт!"

                "Я ни в коем случае не говорила этого!"

                img 1082
                m "А ОТКУДА ТОГДА ЭТО ПЯТНО?"

                m "И ГЛАВНОЕ!
                ЧТО ТЕПЕРЬ С ЭТИМ ДЕЛАТЬ???"


            "Признаться что сама поставила пятно":
                $ juliaMonicaLied = False
                call bitch(-5, "monica_julia_revenge_lie") from _call_bitch_16
                m "Посмотри что из-за тебя случилось!"
                "Пока я носилась сама с этим платьем, я поставила пятно на ковер!"
                julia "Аххххх!!!"

        img 1083
        julia "Миссис Бакфетт, пожалуйста!"

        "Это пятно так просто не оттереть."

        "Этому ковру нужна химчистка!"

        menu:
            "Ты что, серьезно? Ты сама ототрешь это пятно!!!":
                call bitch(10, "monica_julia_revenge_punished") from _call_bitch_17
                $ juliaPunished = True
                $ juliaPunishedLow = False
                $ juliaPunishedVoluntarily = False
                $ juliaLocation = "floor2"
                img 1084
                m "Правда?"

                "Да ты что, серьезно??"

                "У меня как раз есть партнер у которого сеть элитных химчисток!"

                "И исправить этот ковер будет совсем недорого!"

                "Всего около $10.000."

                "И я думаю вычту это с твоей зарплаты."

                if juliaMonicaLied == False:
                    "Хоть это пятно сделала и не ты, но в твои обязанности входит следить за порядком в доме."
                    "Так что отвечать за это придется тебе!"

                "Даже не знаю сколько тебе придется работать."

                "Но это в любом случае будет дешевле для тебя, чем увольняться и платить неустойку за 3 года работы."

                "Согласно нашему трудовому договору."

                mt "Дик молодец."

                "Всегда делает договора какие надо."

                img 1086
                julia "О Боже!!!"

                "Миссис Бакфетт!"

                "Умоляю!"

                img 1085
                "Пожалуйста!"

                "Не надо!"

                "(плачет)"

                img 1087
                m "..."

                "Моя бедная девочка."

                "Не думай что я такой же злой работодатель как и все."

                "Напротив, я очень добрая."

                "Я оказываю тебе безмерное доверие."

                "Я разрешаю тебе оттереть это пятно до завтрашнего дня."

                "Если ты этого не сделаешь, то я уволю тебя с неустойкой."

                "Тебе понято?"

                img 1088
                julia "Да, Миссис Бакфетт."

                "Мне понятно."

                "(хмык)"

                img 1089
                m "Вот и славно."

                "Не подведи мое доверие, девочка."

                julia "(хмык)"

                "Я не подведу Вас, Миссис Бакфетт."

                m "Надеюсь ты ценишь мою доброту, Юлия."

                img 1090
                julia "Я очень ценю Вашу доброту, Миссис Бакфетт."

                "Спасибо Вам."

            "Я знаю что его не оттереть, я не буду заставлять тебя это делать.":
                call bitch(-10, "monica_julia_revenge_punished") from _call_bitch_18
                $ juliaPunished = False
                $ juliaPunishedLow = True
                $ juliaPunishedVoluntarily = False
                $ juliaLocation = "floor1"
                img 1089
                m "Деточка, я знаю что это пятно не оттереть."
                "Я могла бы заставить тебя и ты бы стала пытаться это делать, верно?"

                img 1083
                julia "Конечно, Миссис Бакфетт!"
                "Если бы Вы приказали, я бы сделала все что в моих силах!"

                img 1089
                m "Но я не буду заставлять тебя это делать, хотя ты и заслуживаешь хорошего наказания."
                m "Надеюсь ты ценишь мою доброту, Юлия."
                img 1090
                julia "Я очень ценю Вашу доброту, Миссис Бакфетт."
                "Спасибо Вам."
    if julia_monica_revenge_undo_in_progress == True:
        img 1080
        with fade
        call bitch(-15, "monica_julia_revenge_punished") from _call_bitch_19
        m "Вот!"
        "Посмотри что я нечаянно сделала."

        julia "Аххххх!!!"
        img 1083
        julia "Миссис Бакфетт, пожалуйста!"

        "Это пятно так просто не оттереть."

        "Этому ковру нужна химчистка!"

        img 1089
        m "Я знаю, Юлия."
        "Это моя вина."

        "Я все-равно собиралась выкидывать этот ковер, так что не стоит переживать."

        img 1083
        julia "Миссис Бакфетт!"
        "Я бы могла попытаться оттереть это пятно."
        "Это может занять много времени, но вы так добры ко мне, что я хотела бы вам помочь."
        "Я могу заниматься этим пятном по утрам, пока Вы спите."
        "Я могу это делать тихо, чтобы не беспокоить Вас."

        menu:
            "Да, Юлия, попытайся его оттереть в свободное время.":
                call bitch(5, "monica_julia_revenge_punished_voluntarily") from _call_bitch_20
                $ juliaPunished = False
                $ juliaPunishedLow = False
                $ juliaPunishedVoluntarily = True
                $ juliaLocation = "floor1"
                img 1089
                m "Да, Юлия, попытайся его оттереть в свободное время."
                "Но не слишком усердствуй, ты и так очень устаешь."
                img 1083
                julia "Хорошо, Миссис Бакфетт."
                "Я займусь им в свободное время."

            "Нет, Юлия. Не стоит пытаться сделать невозможную работу.":
                call bitch(-5, "monica_julia_revenge_punished_voluntarily") from _call_bitch_21
                $ juliaPunished = False
                $ juliaPunishedLow = False
                $ juliaPunishedVoluntarily = False
                $ juliaPunishedNone = True
                $ juliaLocation = "floor1"
                img 1089
                m "Нет, Юлия. Не стоит пытаться сделать невозможную работу."
                "Я не садист."
                img 1083
                julia "Как скажете, Миссис Бакфетт."

    $ julia_monica_revenge_in_progress = False
    $ julia_monica_revenge_undo_in_progress = False
    $ subst_to_object("Teleport_Street", False)
    $ scene_transition = "Fade"
    call refresh_scene() from _call_refresh_scene_2
    return

#label floor2_washing_accessories(obj_name, obj_data):

#    return

label floor2_julia_punished_autorun:
    sound snd_scrub
    return
label julia_interact_punished(obj_name, obj_data):
    if obj_data["action"] == "l":
        $ img_num = renpy.random.randint(1,4)
        if img_num == 1:
            img 1446
        if img_num == 2:
            img 1483
        if img_num == 3:
            img 1940
        if img_num == 4:
            img 3395
            img 3396
        mt "Я считаю что эта гувернантка недостаточно старается."
        mt "Бесполезное создание...
        Фи..."

    if obj_data["action"] == "t":
        if day ==1 and day_time == "evening":
            jump julia_punished_talk_day1_evening
        if day == 2 and day_time == "day":
            jump julia_punished_talk_day2_day
        if day == 2 and day_time == "evening":
            jump julia_punished_talk_day2_evening
        if day == 3 and day_time == "day":
            jump julia_punished_talk_day3_day


        img 3395
        w
        img 3396
        w
        img 1446
        w
        stop sound

        img 1450
        julia "Миссис Бакфетт!"

        "Я ототру это пятно."

        "Я не подведу Ваше доверие."

        "Обещаю!"

        "Пожалуйста!"



        sound snd_scrub
    return

label julia_punished_talk_day1_evening:
    if monicaEated == False:
        if cloth_type != "HomeCloth":
            m "Мне надо переодеться сначала."
            "Юлия там моет, я поскользнусь на каблуках!"
            "На своих красивых каблуках!!!"
            return
        img 1445
        with fadelong
        m "О!"
        img 1446
        img 1447
        m "Юлия?"
        img 1448
        m "Я смотрю пятно все еще есть?"
        "Ты решила меня подвести?"
        stop sound fadeout 1.0
        img 1449
        julia "Нет, Миссис Бакфетт!"
        "Еще не следующий день."
        "Вы сказали что я должна оттереть его до завтра."
        img 1450
        julia "У меня впереди еще есть целая ночь!"
        "Пожалуйста!"
        img 1451
        m "Хорошо, детка."
        "Я помню что я обещала."
        "Сейчас отвлекись и подай мне поесть."
        "Затем можешь продолжить."
        "Завтра я одену свой бизнес наряд."
        "Пусть он будет готов."
        img 1452
        julia "Слушаюсь, Миссис Бакфетт!"
        $ juliaPunishedChecked = True
        $ juliaLocation = "kitchen"
        $ remove_objective("julia_check_spot")
        sound highheels_run1
        call refresh_scene_fade()
        show screen notify (_("Юлия убежала на кухню."))
        return
    img 1464
    img 1463
    img 1465
    img 1466
    julia "Миссис Бакфетт!"
    "Я ототру это пятно."
    "Я не подведу Ваше доверие."
    "Обещаю!"
    "Пожалуйста!"

    return

label julia_punished_talk_day2_day:
    if monicaEated == True:
        if businessCloth2NotFoundDay2 == True:
            music Groove2_85
            img 1496
            m "Деточка."
            stop sound fadeout 1.0
            img 1497
            julia "Да, миссис Бакфетт?"
            img 1498
            m "Где мой бизнес наряд?"
            "Отвечай очень осторожно."
            "А не то ты вылетишь прямо сейчас!"
            img 1497
            julia "Миссис Бакфетт!"
            "Он готов!"
            "Я в 4 утра занималась им!"
            "Он постиран."
            "Поглажен."
            "Надушен всеми освежителями для гардероба!"
            "Он благоухает и готов для того чтобы Вы его одели."
            img 1499
            "На свое восхитительное тело!"
            img 1500
            m "Я и так знаю что у меня красивое тело."
            img 1501
            "Нет нужды постоянно подчеркивать это."
            julia "Да, миссис Бакфетт."
            "Я поняла."
            m "Принеси мне его в шкаф."
            julia "Одну секунду, миссис Бакфетт!"
            sound highheels_run1
            img black_screen
            with fadelong
            img 1502
            with fade
            julia "Миссис Бакфетт."
            "Ваш наряд в шкафу."
            img 1503
            m "Хорошо, деточка."
            "Продолжай работать."
            img 1504
            julia "Хорошо, миссис Бакфетт."
            "Спасибо!"

            $ remove_objective("ask_julia_businesscloth2")
            music Mandeville
            $ businessCloth2NotFoundDay2 = False
            $ businessCloth2FoundedDay2 = True
            call refresh_scene_fade()
            return
        img 1505
        with fade
        julia "Миссис Бакфетт!"

        "Я ототру это пятно."

        "Я не подведу Ваше доверие."

        "Обещаю!"

        "Пожалуйста!"
        return
    music Stealth_Groover
    img 1483
    w
    img 1484
    m "ЮЛИЯ!!"
    julia "Да, Миссис Бакфетт?"
    "хмык..."
    img 1485
    m "ЧТО С ПЯТНОМ?"
    img 1486
    julia "Миссис Бакфетт!"
    "Я терла его всю ночь!"
    "Оно стало меньше."
    "Пожалуйста!"
    "хмык..."
    "Миссис Бакфетт!"
    "Умоляю!"
    "Дайте мне еще один день!"
    "хмык..."
    img 1487
    "Я все сделаю!"
    "Я оправдаю Ваше доверие, Миссис Бакфетт!"
    "хмык..."
    label julia_punished_talk_day2_day_menu_loop1:
    menu:
        "Уволить эту сучку прямо сейчас! (disabled)":
            jump julia_punished_talk_day2_day_menu_loop1
        "Помучать эту сучку еще один день...":
            img 1488
            mt "Хммм..."
            "Я решила уволить ее завтра."
            "Почему-бы и не дать ей этот день."
            "Ну раз уж она так хочет оттереть это пятно."
            "Это у нее сейчас прямо цель в жизни."
            img 1489
            "Какие-то глупые люди."
            "С глупыми целями."
            img 1490
            "Эх."
            "Как тяжело с ними таким как Я."

            img 1491
            m "Хорошо, деточка."
            "Я разрешаю тебе тереть до завтрашнего утра."
            call bitch(5, "day2dayMonicaJuliaPunishment")
            "Если завтра с утра будет хоть что-то заметно, то ты уволена максимально жестко."
            img 1492
            "Ты поняла меня?"
            img 1493
            julia "Да, Миссис Бакфетт!"
            "Я поняла!"
            "Спасибо Вам!"
            "Спасибо большое!"
            "хмык..."
            img 1494
            m "А сейчас деточка."
            "Я хочу видеть еду на столе."
            "Ты ведь не забыла про свои обязанности?"
            "Правда?"

            img 1495
            julia "Одну минуту, Миссис Бакфетт."
            "Все готово!"
        "Простить ее...":
            $ juliaMonicaForgivenessAfterPunishment = True
            img 1488
            mt "Хммм..."
            "Может мне простить ее?"
            img 1489
            mt "Она действительно старается стереть это пятно..."
            if juliaMonicaLied == True:
                mt "Пятно, которое я же и поставила, но обвинила ее в этом..."
            img 1490
            mt "Но я ведь ни какая-нибудь сучка и ни тиран!"
            img 1491
            m "Юлия, я считаю что ты не справишься с этим пятном..."
            img 1493
            julia "Миссис Бакфетт! Я справлюсь!"
            "Не увольняйте меня, пожалуйста!!!"
            img 1494
            m "Деточка, я не буду увольнять тебя.
            Пока..."
            "А сейчас быстро встань."
            img 1503
            julia "Миссис... Бакфетт..."
            "хмык..."
            "Вы правда не будете меня увольнять?"
            "хмык..."
            if bitchmeterValue > maxBitchness / 2:
                bitchmeterValue = maxBitchness / 2
            call bitch(-20, "juliaMonicaForgivenessAfterPunishment")
            $ juliaMonicaForgivenessAfterPunishment = True
            m "Нет..."
            julia "А как-же пятно?"
            m "Можешь убирать его... В свободное время..."
            "Если оно у тебя бывает..."
            "..."
            m "А сейчас деточка."
            "Пока я не передумала"
            "Я хочу видеть еду на столе."
            "Ты ведь не забыла про свои обязанности?"
            "Правда?"
            img 1504
            julia "Одну минуту, Миссис Бакфетт."
            "Все готово!"


    music Mandeville
    $ juliaPunishedChecked = True
    $ juliaLocation = "kitchen"
    $ remove_objective("julia_check_spot")
    sound highheels_run1
    call refresh_scene_fade()
    show screen notify (_("Юлия убежала на кухню."))
    return
#juliaPunishedVoluntarily

label julia_punished_talk_day2_evening:
    if cloth_type == "BusinessCloth":
        imgc Dial_Monica_BusinessCloth2_Thinking
        mt "Я только с улицы."
        "Сначала надо переодеться."
        return

    if monicaEated == True:
        stop sound fadeout 1.0
        img 1958
        with fade
        julia "Миссис Бакфетт!"
        "Я ототру это пятно."
        "Я не подведу Ваше доверие."
        "Обещаю!"
        "Пожалуйста!"
        call refresh_scene_fade()
        return

    music Stealth_Groover
    img 1937
    with fadelong
    w
    img 1938
    with fade
    w
    img 1939
    with fade
    w
    img 1940
    with fade
    w
    img 1941
    with fade
    w
    stop sound fadeout 1.0
    julia "Добрый вечер, Миссис Бакфетт!"
    "Пятно уже стало меньше!"
    m "Ах, оно все еще есть?"
    "Как жаль."
    "У тебя же было время только до вечера, детка?"
    "Значит все?"
    img 1942
    julia "Миссис Бакфетт!"
    "Вы же обещали что у меня время до завтра!"
    "У меня есть еще одна ночь впереди!"
    "Пожалуйста!"
    "(хмык)"
    img 1943
    m "Я помню, детка."
    "Я пошутила."
    "У тебя совершенно нет чувства юмора."
    "..."
    img 1944
    "Или ты считаешь что это у меня нет чувства юмора, Юлия?"
    img 1945
    julia "Что Вы, Миссис Бакфетт!"
    "У Вас очень хорошее чувство юмора!"
    "Оно очень тонкое и изысканное!"
    img 1946
    "Как Вы сама!"

    img 1947
    m "Вот."
    "То-то же."
    "..."
    img 1948
    "Юлия?"
    julia "Да, Миссис Бакфетт?"
    img 1949
    m "Юлия."
    "Может быть ты устала?"
    "Все-таки ты не спала больше суток."
    img 1950
    "И собираешься не спать еще ночь?"
    "Может быть передохнешь?"

    img 1951
    julia "Миссис Бакфетт!"
    "Спасибо за заботу."

    img 1952
    "Но мне очень нужно оттереть это пятно до завтра!"

    img 1953
    m "Хорошо, детка."
    "Я стараюсь о тебе заботиться, но я не буду препятствовать твоим желаниям."

    img 1954
    "Я же хорошая?"

    img 1955
    julia "Вы очень хорошая, Миссис Бакфетт!"
    img 1956
    m "Хорошо."
    "А сейчас приготовь ужин."
    "Потом можешь продолжать."

    img 1957
    julia "Одну минуту, Миссис Бакфетт!"
    $ juliaLocation = "kitchen"
    sound highheels_run1
    call refresh_scene_fade()
    show screen notify (_("Юлия убежала на кухню."))
    music Mandeville
    return

label julia_punished_talk_day3_day:
    if monicaEated == True:
        stop sound fadeout 1.0
        img 1958
        with fade
        julia "Миссис Бакфетт!"
        "Я ототру это пятно."
        "Я не подведу Ваше доверие."
        "Обещаю!"
        "Пожалуйста!"
        call refresh_scene_fade()
        return
    if juliaFirePlanned == False:
        img 1994
        with fade
        w
        img 1995
        w
        img 1996
        m "Юлия!"
        img 2006
        with fade
        julia "Ой!"
        "Миссис Бакфетт!"
        "Это Вы?"

        "Я ототру это пятно до утра, обещаю!"
        img 2007
        m "Уже утро, деточка!"
        img 2008
        julia "Как?"

        "Как же так?"

        "Этого не может быть!"

        "(хмык)"
        img 2009
        julia "Миссис Бакфетт!!! Умоляю ВАС!!!"
        "Дайте мне еще немного времени!"
        "Еще чуть-чуть!!!"
        "(хмык)"
        img 2010
        with fade
        m "Тебе повезло, Юлия!"
        "У меня сегодня хорошее настроение. Поэтому я решила пожалеть тебя."
        img 2008
        m "До завтрашнего дня, не более!"
        if fredFirePlanned == True:
            m "А вот Фреду сегодня не повезло, так что цени свое везение, деточка!"
        img 2010
        m "А теперь беги с сделай мне завтрак, пока я не передумала!"
        julia "Да, Миссис Бакфетт! Я уже бегу!!!"

        $ juliaLocation = "kitchen"
        sound highheels_run1
        call refresh_scene_fade()
        show screen notify (_("Юлия убежала на кухню."))
        music Cheery_Monday
        return
    music Pyro_Flow
    img 1994
    with fade
    w
    img 1995
    w
    img 1996
    w
    img 1998
    w
    img 1999
    w
    stop sound fadeout 1.0
    img 2000
    with fade
    w
    stop music fadeout 1.0
    img 2001
    with fade
    w
    img 2002
    with fade
    sound snd_bodyfall
    w
    img 2003
    w
    img 2004
    music Pyro_Flow
    m "Привет, дорогуша."

    img 2005
    with fade
    julia "Ой!"
    "Миссис Бакфетт!"
    "Это Вы?"

    img 2006
    "Я ототру это пятно до утра, обещаю!"

    img 2007
    m "Уже утро, деточка!"

    img 2008
    julia "Как?"

    "Как же так?"

    img 2009
    "Этого не может быть!"

    "(хмык)"

    img 2010
    m "Ты уволена, детка."
    "Тебе по почте придет уведомление о сумме неустойки."

    img 2011
    "Собирай свои вещи и чтобы через 15 минут тебя не было."

    "ЯСНО??"

    img 2012
    julia "Миссис Бакфетт!"

    "(хмык)"

    "Пожалуйста!"

    "(хмык)"

    "Не делайте этого!"

    "У моей семьи много долгов!"

    "Если вы меня уволите, то моей семье будет нечего есть!"

    "Пожалуйста!"

    "(хмык)"

    img 2013
    m "Ой."

    "Еще одна зануда про еду и долги."

    "Мне скучно."

    "Я все сказала тебе."

    "Если я тебя увижу через 15 минут, то вызову полицию."

    "Ты меня хорошо слышишь, деточка?"

    img 2014
    julia "Да, Миссис Бакфетт..."

    "(хмык)"

    "Я пошла..."

    img 2015
    m "Стой."

    "Я совсем забыла."

    "Ты пойдешь после того как приготовишь мне завтрак."

    img 2016
    "То что ты уволена, не освобождает тебя от обязанности прислуживать мне."

    img 2017
    "Быстро приготовь мне и проваливай отсюда."

    img 2018
    julia "Хорошо, Миссис Бакфетт..."
    $ juliaLocation = "kitchen"
    sound highheels_run1

    img 2019
    with fadelong
    show screen notify (_("Юлия убежала на кухню."))
    mt "Пятно так и осталось."
    "Нерадивые сотрудники вечно оставляют за собой недоделанную работу."

    "Пятно придется оттирать следующей гувернантке."

    img 2020
    "С удовольствием поиграю с ней как с Юлией."

    "Это пятно - отличная идея."

    "С помощью него я поднимаю настроение каждое утро!"

    "Хи-хи"

    call refresh_scene_fade()
    music Cheery_Monday
    return


























#
