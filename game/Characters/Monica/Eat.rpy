default monicaEated = False
default juliaPraiseOnOccasion = False

label eat:
    if juliaLocation != "kitchen":
        m "Мне надо распорядиться гувернантке подать еду на стол."

        "Я не собираюсь заниматься этим сама!"

        return
    if day == 3:
        if day_time == "day":
            jump eat_day3
    if day == 2:
        if day_time == "day":
            jump eat_day2
        if day_time == "evening":
            jump eat_day2_evening
    if day == 1:
        if day_time == "day":
            img 1051
            "Юлия! Можешь подавать еду!"
            img 1052
            julia "Да, Миссис Бакфетт, одну секунду!"
            wc
            sound highheels_run2
            img 1053
            with fade
            julia "Пожалуйста, Миссис Бакфетт."

            "Приятного аппетита!"

            menu:
                "Спасибо и брысь отсюда!":
                    img 1054
                    m "Спасибо..."

                    "И..."

                    m "Брысь отсюда!"
                    call bitch(2, "julia_eat_1_morning") from _call_bitch_25

                    julia "Да, Миссис Бакфетт.
                    Не смею Вам мешать."

                "Спасибо!":
                    img 1054
                    m "Спасибо..."

                    "Можешь идти."

                    call bitch(-2, "julia_eat_1_morning") from _call_bitch_26

                    julia "Да, Миссис Бакфетт.
                    Не смею Вам мешать."

            sound highheels_run1
            wc
            img 1055
            with fade
            m "Юлия готовит довольно вкусно."

            "Мда, определенно вкусно."

            "Может стоит ее похвалить?"

            menu:
                "Что за вздор, кого еще хвалить?":
                    img 1056
                    m "Что за вздор."
                    "Кого хвалить?"
                    "Какую-то служанку?"
                    call bitch(2, "julia_eat_2_morning") from _call_bitch_27

                "Похвалить при случае":
                    img 1055
                    m "Похвалю ее при случае."
                    call bitch(-2, "julia_eat_2_morning") from _call_bitch_28
                    $ juliaPraiseOnOccasion = True

            $ monicaEated = True
            $ remove_objective("eat")
            $ juliaLocation = "none"

            wc
            img 1055
            with fade
            imgc Monica_HomeCloth1_Thinking1
            m "Ну что-ж."

            "Я Поела."
            if bathTaken == True:
                "Помылась."

                "Теперь пора одеваться и идти на улицу."
            else:
                "Осталось принять душ, одеваться и идти на улицу"

            "К Фреду."
            "Пока этот никчемный болван куда-нибудь не подевался."

            "Я собираюсь одеть новое платье.
            Надеюсь Юлия его подготовила и повесила в шкаф.
            Надо пойти в спальню проверить."

            $ businessClothNotFoundDay1 = True
        if day_time == "evening":
            if juliaPunished == True:
                img 1458
                with fade
                w
                img 1459
                m "Юлия! Можешь подавать еду!"
                julia "Да, Миссис Бакфетт, одну секунду!"
                sound highheels_run1
                img 1460
                with fadelong
                julia "Пожалуйста, Миссис Бакфетт."
                "Приятного аппетита!"
                m "..."
                m "Юлия?"
                m "Да, миссис Бакфетт?"
                img 1461
                m "Что там с пятном?"
                img 1462
                julia "Слушаюсь, миссис Бакфетт!"
                $ monicaEated = True
                $ remove_objective("eat")
                $ juliaLocation = "floor2"
                sound highheels_run1
                show screen notify (_("Юлия убежала тереть пятно."))
                call refresh_scene_fade()
                return
#default juliaPunishedLow = False #наказана криком, но разрешено не убирать пятно
#default juliaPunishedVoluntarily = False #мягко, разрешено убирать в свободное время
#default juliaPunishedNone = False #пятно есть, но Юлию не наказали вообще никак
#default juliaMonicaLied = False #Моника соврала что пятно поставила не она
            img 1458
            with fade
            m "Юлия!"
            img 1459
            "Можешь подавать еду!"
            julia "Да, Миссис Бакфетт, одну секунду!"
            sound highheels_run1
            img 1460
            with fadelong
            julia "Пожалуйста, Миссис Бакфетт."
            "Приятного аппетита!"
            m "..."
            m "Юлия?"
            m "Да, миссис Бакфетт?"
            img 1461
            if juliaPunishedLow == True:
                m "Если я не заставила тебя убирать пятно, то это не значит что у тебя нет других обязанностей!"
                "Ты уже все сделала по дому?"
                img 1462
                julia "Еще нет..."
                "..."
                julia "Слушаюсь, миссис Бакфетт!"
                $ monicaEated = True
                $ remove_objective("eat")
                $ juliaLocation = "floor1"
                sound highheels_run1
                show screen notify (_("Юлия убежала выполнять обязанности."))
                call refresh_scene_fade()
                return
            if juliaPunishedVoluntarily == True:
                m "Спасибо.
                Ты свободна."
                "И не забывай про уборку пятна в свободное время!"
                img 4692
                julia "Конечно, Миссис Бакфетт!"
                "Я занимаюсь им в любую свободную минуту.
                Спасибо Вам!"
                $ monicaEated = True
                $ remove_objective("eat")
                $ juliaLocation = "floor1"
                sound highheels_run1
                call refresh_scene_fade()
                return
            m "Спасибо за еду.
            Ты свободна."
            img 4692
            julia "Миссис Бакфетт, рада служить Вам!"
            $ monicaEated = True
            $ remove_objective("eat")
            $ juliaLocation = "floor1"
            sound highheels_run1
            call refresh_scene_fade()
            return

    return

label eat_day2:
    if day_time == "day":
        img 1506
        m "Юлия."
        "Можешь подавать на стол."
        julia "Один момент, миссис Бакфетт!"
        if juliaPunished == True:
            julia "хмык..."

        img 1507
        with fadelong
        julia "Пожалуйста, миссис Бакфетт."
        "Приятного аппетита!"
        m "Спасибо."
        julia "Миссис Бакфетт?"
        m "Да?"
        if juliaPunished == True and juliaMonicaForgivenessAfterPunishment == False:
            julia "Я могу идти заниматься пятном?"
            img 1508
            m "Ты не можешь идти."

            img 1509
            julia "?"
            img 1510
            m "Ты можешь и ты должна БЕЖАТЬ им заниматься."
            img 1511
            julia "Хорошо, миссис Бакфетт!"
            "Спасибо Вам!"
            $ monicaEated = True
            $ remove_objective("eat")
            $ juliaLocation = "floor2"
            sound highheels_run1
            show screen notify (_("Юлия убежала тереть пятно."))
            call refresh_scene_fade()
            return
        if juliaPunishedLow == True:
            julia "Я могу идти заниматься своими обязанностями?"
            m "Иди и занимайся, пока я не заставила тебя убирать пятно!"
            julia "Хорошо, миссис Бакфетт!"
            "Спасибо Вам!"
            $ monicaEated = True
            $ remove_objective("eat")
            $ juliaLocation = "floor1"
            sound highheels_run1
            show screen notify (_("Юлия убежала выполнять обязанности."))
            call refresh_scene_fade()
            return
        if juliaPunishedVoluntarily == True:
            julia "Я могу идти заниматься своими обязанностями?"
            m "Спасибо.
            Ты свободна."
            "И не забывай про уборку пятна в свободное время!"
            julia "Конечно, Миссис Бакфетт!"
            img 4693
            "Я занимаюсь им в любую свободную минуту.
            Спасибо Вам!"
            $ monicaEated = True
            $ remove_objective("eat")
            $ juliaLocation = "floor1"
            sound highheels_run1
            show screen notify (_("Юлия убежала выполнять обязанности."))
            call refresh_scene_fade()
            return
        if juliaMonicaForgivenessAfterPunishment == True:
            julia "Я могу идти заниматься своими обязанностями?"
            m "Иди и занимайся, пока я не передумала насчет пятна!"
            img 4693
            julia "Хорошо, миссис Бакфетт!"
            "Спасибо Вам!"
            "Спасибо!"
            "Спасибо!!!"

            $ monicaEated = True
            $ remove_objective("eat")
            $ juliaLocation = "floor1"
            sound highheels_run1
            show screen notify (_("Юлия убежала выполнять обязанности."))
            call refresh_scene_fade()
            return


#        if juliaPunishedNone == True:
    img 4693
    julia "Я могу идти заниматься своими обязанностями?"
    m "Да, Юлия. Иди."
    "Спасибо за завтрак."
    julia "Хорошо, миссис Бакфетт!"
    "Спасибо Вам!"
    $ monicaEated = True
    $ remove_objective("eat")
    $ juliaLocation = "floor1"
    sound highheels_run1
    show screen notify (_("Юлия убежала выполнять обязанности."))
    call refresh_scene_fade()
    return

    return

label eat_day2_evening:
    if juliaPunished == True and juliaMonicaForgivenessAfterPunishment == False:
        img 1959
        with fadelong
        m "Юлия! Можешь подавать еду!"
        julia "Да, Миссис Бакфетт, одну секунду!"
        if juliaPunished == True:
            julia "хмык..."
        img 1960
        with fadelong
        julia "Пожалуйста, Миссис Бакфетт."
        "Приятного аппетита!"

        m "Ты свободна."
        julia "Спасибо, Миссис Бакфетт!"

        $ monicaEated = True
        $ remove_objective("eat")
        $ juliaLocation = "floor2"
        $ autorun_to_object("floor1", "eat_day2_evening_after")
        sound highheels_run1
        show screen notify (_("Юлия убежала выполнять обязанности."))
        call refresh_scene_fade()
        return
    if juliaPunished == True and juliaMonicaForgivenessAfterPunishment == True:
        img 1959
        with fadelong
        m "Юлия! Можешь подавать еду!"
        julia "Да, Миссис Бакфетт, одну секунду!"
        img 1960
        with fadelong
        julia "Пожалуйста, Миссис Бакфетт."
        "Приятного аппетита!"

        m "Ты свободна."
        m "Иди и занимайся своими обязанностями, пока я не передумала насчет пятна!"
        julia "Спасибо, Миссис Бакфетт!"
        $ monicaEated = True
        $ remove_objective("eat")
        $ juliaLocation = "floor1"
        $ autorun_to_object("floor1", "eat_day2_evening_after")
        sound highheels_run1
        show screen notify (_("Юлия убежала выполнять обязанности."))
        call refresh_scene_fade()
        return
    if juliaPunishedLow == True:
        img 1959
        with fadelong
        m "Юлия! Можешь подавать еду!"
        julia "Да, Миссис Бакфетт, одну секунду!"
        img 1960
        with fadelong
        julia "Пожалуйста, Миссис Бакфетт."
        "Приятного аппетита!"

        m "Ты свободна."
        m "Не забудь заботиться о пятне."
        julia "Спасибо, Миссис Бакфетт!"
        "Конечно!"
        $ monicaEated = True
        $ remove_objective("eat")
        $ juliaLocation = "floor1"
        $ autorun_to_object("floor1", "eat_day2_evening_after")
        sound highheels_run1
        show screen notify (_("Юлия убежала выполнять обязанности."))
        call refresh_scene_fade()
        return
    if juliaPunishedVoluntarily == True:
        m "Юлия! Можешь подавать еду!"
        julia "Да, Миссис Бакфетт, одну секунду!"
        img 1960
        with fadelong
        julia "Пожалуйста, Миссис Бакфетт."
        "Приятного аппетита!"

        m "Ты свободна."
        "Да, кстати, тебя не напрягает убирать то пятно на ковре?"
        img 4693
        julia "Нет, Миссис Бакфетт!"
        "Я рада служить Вам!"
        m "Хорошо, можешь идти."
        $ monicaEated = True
        $ remove_objective("eat")
        $ juliaLocation = "floor1"
        $ autorun_to_object("floor1", "eat_day2_evening_after")
        sound highheels_run1
        show screen notify (_("Юлия убежала выполнять обязанности."))
        call refresh_scene_fade()

        return
    m "Юлия! Можешь подавать еду!"
    julia "Да, Миссис Бакфетт, одну секунду!"
    img 1960
    with fadelong
    julia "Пожалуйста, Миссис Бакфетт."
    "Приятного аппетита!"

    m "Ты свободна."
    "И спасибо за еду. Я вижу что на этот раз очень вкусно."
    img 4693
    "Спасибо, Миссис Бакфетт!"
    "Я рада служить Вам!"
    $ monicaEated = True
    $ remove_objective("eat")
    $ juliaLocation = "floor1"
    $ autorun_to_object("floor1", "eat_day2_evening_after")
    sound highheels_run1

    show screen notify (_("Юлия убежала выполнять обязанности."))

    call refresh_scene_fade()
    return

label eat_day2_evening_after:
    imgc Monica_HomeCloth2_Thinking
    mt "Я поела."
    "Что там у нас дальше?"
    return

label eat_day3:
    if juliaFirePlanned == True:
        img 2021
        with fadelong
        m "Юлия! Можешь подавать еду!"
        img 2022
        "В последний раз."

        img 2023
        julia "Я все несу..."
        "(хмык)"
        sound highheels_run1
        img 2024
        with fade
        julia "Пожалуйста, Миссис Бакфетт."
        "(хмык)"

        img 2025
        "Приятного аппетита!"
        "(хмык)"

        img 2026
        m "Ты свободна."

        julia "Миссис Бакфетт..."

        "Может быть Вы передумаете?"

        menu:
            "Вон отсюда, малявка!":
                music Pyro_Flow
                img 2027
                with fade
                m "НЕТ!"
                call bitch(5, "julia_firing")
                "Вон отсюда, малявка!"

                img 2028
                w
                sound highheels_run1
                $ juliaLocation = "none"
                $ remove_objective("fire_julia")

                img 2029
                with fadelong
                show screen notify (_("Юлия расплакалась и убежала."))
                music Cheery_Monday
                mt "Я поела."
                "Вечером мне уже будет готовить другая служанка."
                "Уверена что будет гораздо вкуснее."
                "Предвкушаю вечерний ужин."
                "Мммммм..."
            "Пожалеть Юлию...":
                $ juliaFirePlanned = False
                $ juliaFireCancelled = True
                img 2029
                with fade
                m "Хорошо, Юлия."
                "Так уж и быть."
                call bitch(-3, "julia_firing")
                "Я разрешаю тебе тереть пятно еще до завтрашнего утра."
                img 2026
                "А сейчас брысь отсюда, пока я не передумала!"
                img 2025
                julia "Спасибо, Миссис Бакфетт!"
                "Спасибо ВАМ!!!"
                $ juliaLocation = "floor2"
                sound highheels_run1
                show screen notify (_("Юлия убежала тереть пятно."))

        $ monicaEated = True
        $ remove_objective("eat")
        call refresh_scene_fade()
        return

    img 2021
    with fadelong
    m "Юлия!"
    "Можешь подавать на стол!"
    img 2029
    with fadelong
    julia "Пожалуйста, Миссис Бакфетт."
    m "Ты свободна, можешь идти!"
    if fredFirePlanned == True:
        m "Да, и передай привет Фреду!"
        "У меня сегодня на него планы."
        julia "Простите, Миссис Бакфетт, что мне ему передать?"
        m "Ничего, Юлия. Можешь идти."
        julia "Спасибо, Миссис Бакфетт!"

    else:
        julia "Спасибо, Миссис Бакфетт!"
    $ monicaEated = True
    $ remove_objective("eat")
    $ juliaLocation = "none"
    sound highheels_run1
    show screen notify (_("Юлия убежала выполнять обязанности."))
    call refresh_scene_fade()
    return
