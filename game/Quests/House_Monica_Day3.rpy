default monicaFiringDecision = False
default juliaFirePlanned = False
default juliaFireCancelled = False
default janeTiffanyFirePlanned = False
default fredFirePlanned = False

default fireAmount = 0

label quest_house_monica_day3_day_init:
#    $ juliaPunished = False #debug
#    $ juliaPunishedLow = True #debug
#    $ juliaMonicaLied = False #debug
#    $ juliaPunishedVoluntarily = True #debug
#    $ juliaMonicaYell = False #debug
#    $ juliaPunishedNone = True #debug
#    $ juliaLocation = "floor1" #debug
    $ autorun_to_object("floor1", False)
    if juliaPunished == True:
        call textonblack(_("ЭТИМ ВЕЧЕРОМ..."))
        img black_screen
        with Dissolve(1)
        call julia_scene_floor2_evening1_1()


    call textonblack(_("ДЕНЬ 3..."))
    img black_screen
    with Dissolve(1)
    $ changeDayTime("day")
    music Cheery_Monday


    $ fireAmount = 0

    img 1010
    with fadelong
    w
    img 1011
    with fade
    w
    img 1013
    with fade
    w
    img 1961
    with fade
    mt "Еще одно чудесное утро!"

    img 1962
    "..."

    img 1963
    "Что у нас на сегодня?"

    img 1964
    mt "Сегодняшний день будет очень интересным!"
    menu:
        "Уволить кого-нибудь!":
            mt "Сегодня я собираюсь уволить несколько человек."

            img 1965
            "Я обожаю это делать!"

            if juliaPunished == True and juliaMonicaForgivenessAfterPunishment == False:
                img 1966
                "Начнем с Юлии."

                "Я сегодня ночью снова слышала ее шум."

                menu:
                    "Уволить Юлию.":
                        $ add_objective("fire_julia", _("Уволить Юлию"), c_white, 21)
                        $ juliaFirePlanned = True
                        $ fireAmount = fireAmount + 1
                        img 1967
                        mt "Бедняжка."

                        "Она совсем замучалась."

                        call bitch(5, "juliaFirePlanned")
                        "Я не могу так мучать людей."

                        img 1968
                        "Ведь я же хорошая!"

                        img 1969
                        "..."
                    "Не увольнять Юлию.":
                        $ juliaFirePlanned = False
                        img 1967
                        "Бедняжка."

                        "Она совсем замучалась."

                        "Я не могу так мучать людей."

                        call bitch(-5, "juliaFirePlanned")
                        "Но пусть она еще поработает."
                        "Хотя я чувствую себя плохой после такого решения."
                        "Еще подумаю потом надо этим..."

                img 1970
                "Затем надо съездить в офис."
            else:
                img 1967
                "Юлию я пока не буду трогать."
                img 1970
                "Вместо этого надо съездить в офис."

            img 1971
            "Затем проведать Стива."

            menu:
                "Уволить Джейн и Тиффани.":
                    $ add_objective("fire_jane", _("Уволить Джейн"), c_white, 22)
                    $ add_objective("fire_tiffany", _("Уволить Тиффани"), c_white, 23)
                    $ janeTiffanyFirePlanned = True
                    $ fireAmount = fireAmount + 1
                    img 1972
                    "Надо заняться его сотрудницами."
                    call bitch(5, "janeTiffanyFirePlanned")
                    img 1973
                    "Я бы очень хотела увидеть их у той старой мамочки."

                    img 1974
                    "Также как ту недо-модель."

                    img 1975
                    "Хи-хи."

                    img 1976
                    "Я, наверное, даже специально туда съезжу потом."

                    "Вдруг меня ждет сюрприз."

                    img 1977
                    "Хи-хи."

                "Дать им шанс.":
                    $ janeTiffanyFirePlanned = False
                    img 1972
                    "По хорошему бы надо заняться его сотрудницами."
                    "Но сдается мне что все это происки Стива."
                    "Взбучку от меня они, конечно, заслужили."
                    img 1973
                    call bitch(-5, "janeTiffanyFirePlanned")
                    "В общем посмотрим. Если они невиноваты, то если Стив их уволит, я прикажу взять их назад."
                    "А вот Стиву непоздоровится."
                    img 1974
                    "Хи-хи."

            img 1978
            "..."

            "Такс."

            "Кто еще на очереди?"

            img 1979
            "А. Фрэд!"

            menu:
                "Уволить Фреда.":
                    $ add_objective("fire_fred", _("Уволить Фреда"), c_white, 24)
                    $ fredFirePlanned = True
                    $ fireAmount = fireAmount + 1
                    img 1980
                    "Он слишком много со мной спорит."

                    call bitch(5, "fredFirePlanned")
                    img 1981
                    "Он недостаточно профессионален."
                    if juliaFirePlanned == True:
                        "К тому же он привел эту растяпу Юлию, которую мне теперь придется увольнять."
                        "Тратить на это свое время!"

                "Дать ему шанс.":
                    $ fredFirePlanned = False
                    call bitch(-5, "fredFirePlanned")
                    if juliaFirePlanned == True:
                        img 1964
                        "Фред слишком много со мной спорит, но я дам ему шанс."
                        "В конце концов, мне не так уж скучно с ним."
                        "Несмотря на то что он привел эту растяпу Юлию, которую мне теперь придется увольнять."
                    else:
                        img 1964
                        "Фред слишком много со мной спорит, но я дам ему шанс."
                        "В конце концов, мне не так уж скучно с ним."
            if fireAmount == 0:
                img 1961
                mt "Хм... странно..."
                "Я собиралась кого-нибудь уволить, но так и не решилась этого сделать."
                "Эх... Верно говорит Дик - моя доброта меня погубит!"
                "А кто-то еще говорит что я сучка! Да вы только посмотрите какая я добрая!"
            if fireAmount == 1:
                img 1982
                "Уверена, что моя дорогая секретарь уже к вечеру организует замену."
                img 1983
                with dissolve
                "Ведь на рынке труда стоят очереди к таким как Я."
                "Мечта любого - прислуживать мне."

                img 1984
                "..."
            if fireAmount > 1:
                img 1982
                "Уверена, что моя дорогая секретарь уже к вечеру организует замену всем этим людям."


        "Просто хороший день...":
            img 1966
            call bitch(-15, "noFiring")
            mt "По крайней мере у меня есть настроение для этого!"

    img 1985
    with fade
    "Итак."

    if juliaFirePlanned == True:
        "Сначала займемся Юлией."

        "Затем перекусим."
    else:
        "Сначала перекусим."

    "Примем душ."

    "И поедем в офис."

    if fireAmount == 0:
        img 1987
        "У меня классное настроение!"
        "Уииии!"
    if fireAmount == 1:
        img 1986
        "Кое-кто сегодня будет плакать!"
        img 1987
        "Уииии!"
    if fireAmount > 1:
        img 1986
        "Сегодня вечером многие будут плакать!"
        img 1987
        "Уииии!"

    $ houseOutMode = "usual"
    $ bathTakenJust = False
    $ bathTaken = False
    $ monicaEated = False

    $ casualMusic = "Cheery_Monday"

#    $ map_objects["Teleport_Fitness"]["state"] = "visible"
    $ add_objective("dress_homecloth", _("Одеть домашнюю одежду"), c_blue, 0)
    $ add_objective("take_bath", _("Принять душ"), c_green, 1)
    $ add_objective("eat", _("Позавтракать"), c_orange, 2)
    $ add_objective("drive_to_office", _("Ехать в свой офис"), c_pink, 26)

    #go_to_steve_after

#    $ beforePolicaPhoneDialoguePlanned = True
    $ drivingPlacePlannedArray["Police"] = "police_phone_dialogue1"
    $ steveOfficeSteveInOffice = False
    $ mapSubstMonicaOfficeToPolice = True
#    $ add_objective("go_outside_fitness", _("Одеться и ехать в фитнес зал"), c_orange, 10)
#    $ drivingPlacePlannedArray["Fitness"] = "drive_speak_monica_fred_fitness"
#    if juliaPunished == True:
#        $ add_objective("julia_check_spot", _("Проверить Юлию"), c_red, 3)

#    music Mandeville
#    $ casualMusic = "Mandeville"
    call change_scene("bedroom1", "Fade_long")
#    call refresh_scene_fade_long()
    return
