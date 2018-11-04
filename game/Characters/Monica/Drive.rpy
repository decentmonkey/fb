#target_scene
#target_map_scene
default enterCarScene = True

default driveCanceled = False

default monicaEnterCarLookingCharacter = "Fred"
default drivingPlacePlannedArray = {}
default dressReturnDialoguePlanned = False
default driveTriggers = {}
#default beforePolicaPhoneDialoguePlanned = False

label start_drive():
    $ driveTriggers = {}
    $ driveCanceled = False
    if enterCarScene == False:
        jump start_drive_1
    call get_into_car() from _call_get_into_car
#    $ scene_transition = "Fade"
    $ autorun_to_object(scene_name, "start_drive_1")
    call refresh_scene()
    return

label start_drive_1:
    $ driveTriggers = {}
    sound snd_car_turn_on
    call startDriving() from _call_startDriving
    if driveCanceled == True:
        return
    $ visitedPlaces[target_map_scene] = True
    $ map_scene = target_map_scene
    call change_scene(target_scene, "Fade_long", "snd_car_engine") from _call_change_scene_75
    $ visitedPlaces[target_map_scene] = True
    return

label start_drive_direct():
    call change_scene(target_scene, "Fade_long", "snd_car_engine") from _call_change_scene_76
    return
label start_walk_direct():
    call change_scene(target_scene, "Fade_long", "highheels_run2")
    return

label startDriving:
    $ print scene_name
    if drivingPlacePlannedArray.has_key(target_map_scene) and drivingPlacePlannedArray[target_map_scene] != False:
        $ driveSceneToCall = drivingPlacePlannedArray[target_map_scene]
        $ drivingPlacePlannedArray[target_map_scene] = False
        call expression driveSceneToCall pass (target_scene)
#    if beforePolicaPhoneDialoguePlanned == True:
#        $ beforePolicaPhoneDialoguePlanned = False
#        call police_phone_dialogue1()
#        return
    if dressReturnDialoguePlanned == True:
        $ dressReturnDialoguePlanned = False
        call dress_return_drive3()
        return
    if dick_meeting1_restaurant_drive_dialogue1_planned == True:
        call dick_meeting1_restaurant_drive_dialogue1()
        return
    if checkMapVisited("Monica_Office") == False:
        call drive_speak_monica_office() from _call_drive_speak_monica_office
        return
    if dickMeetingPlannedDay1 == True and dickRefuelPlanned == False and target_map_scene == "Dick_Office": #едем к Дику, нужна заправка
        call drive_speak_monica_dick_day1_need_refuel1() from _call_drive_speak_monica_dick_day1_need_refuel1
        return
    if dickMeeting1Drive1DialoguePlanned == True:
        $ dickMeeting1Drive1DialoguePlanned = False
        call drive_speak_monica_dick_day1_drive1()
        return
    return

label get_into_car:
#    if day_time == "day":
    if 1==1:
        if monicaEnterCarLookingCharacter == "Fred":
            $ img_name = "Car_Enter_Fred_1" + day_suffix
            img img_name
            with fade
            fred "Мэм, пожалуйста, садитесь."
        if monicaEnterCarLookingCharacter == "Dick":
            $ img_name = "Car_Enter_Dick_1" + day_suffix
            img img_name
            with fade
            dick "Моника, садись."
        if cloth == "BusinessCloth1":
            if day_time == "evening":
                img Car_Enter_Monica_BusinessCloth1_1_Evening
                w
                img Car_Enter_Monica_BusinessCloth1_2_Evening
                w
                img Car_Enter_Monica_BusinessCloth1_3_Evening
            else:
                $ rand1 = renpy.random.randint(1,2)
                if rand1 == 1:
                    img Car_Enter_Monica_14
                    w
                    img Car_Enter_Monica_17
                    w
                    img Car_Enter_Monica_18
                    w
                    img Car_Enter_Monica_19
                    w
                    img Car_Enter_Monica_3
                    w
                    img Car_Enter_Monica_2
                    w
                if rand1 == 2:
                    img Car_Enter_Monica_15
                    w
                    img Car_Enter_Monica_17
                    w
                    img Car_Enter_Monica_18
                    w
                    img Car_Enter_Monica_19
                    w
                    img Car_Enter_Monica_3
                    w
                    img Car_Enter_Monica_2
                    w
        if cloth == "BusinessCloth2":
            if day_time == "day":
                img Car_Enter_Monica_BusinessCloth2_1
                w
                img Car_Enter_Monica_BusinessCloth2_2
                w
                img Car_Enter_Monica_BusinessCloth2_3
            else:
                img Car_Enter_Monica_BusinessCloth2_1_Evening
                w
                img Car_Enter_Monica_BusinessCloth2_2_Evening
                w
                img Car_Enter_Monica_BusinessCloth2_3_Evening

        if cloth == "BusinessCloth3":
            if day_time == "day":
                img Car_Enter_Monica_BusinessCloth3_1
                w
                img Car_Enter_Monica_BusinessCloth3_2
                w
                img Car_Enter_Monica_BusinessCloth3_3
            else:
                img Car_Enter_Monica_BusinessCloth3_1_Evening
                w
                img Car_Enter_Monica_BusinessCloth3_2_Evening
                w
                img Car_Enter_Monica_BusinessCloth3_3_Evening

        if cloth == "EveningDress":
            if day_time == "day":
                img Car_Enter_Monica_EveningDress_1
                w
                img Car_Enter_Monica_EveningDress_2
                w
                img Car_Enter_Monica_EveningDress_3
            else:
                img Car_Enter_Monica_EveningDress_1_Evening
                w
                img Car_Enter_Monica_EveningDress_2_Evening
                w
                img Car_Enter_Monica_EveningDress_3_Evening

        if monicaEnterCarLookingCharacter == "Fred":
            fred "Я Вам помогу."
        if monicaEnterCarLookingCharacter == "Dick":
            dick "Я помогу тебе :)"
    return


label drive_speak_monica_office:
    imgr 1126
    menu:
        "Задирать Фреда.":
            jump drive_speak_monica_office_1
        "Молча ехать и смотреть инстаграм.":
            return

label look_at_car(look_at_car_stage):
    if look_at_car_stage == 0:
        m "Моя машинка.
        Я на ней езжу."
        "Это внедорожник. Я купила его, потому что осенью подмывало дорогу по пути от дома в город."
        "Сейчас эта проблема решена.
        Умолчу о том как.. Хи-хи."
        "Но я все-равно к нему привыкла.
        И, мне кажется, он меня тоже любит!"
    return

label drive_speak_monica_office_1:
    call bitch(1, "fred_monica_office1") from _call_bitch_65
    sound snd_car_engine
    imgr 1126
    fred "Хорошая сегодня погода, Мэм!
    Не правда-ли?"

    imgl 1127
    m "У тебя все всегда хорошо, кроме вождения, Фред!"

    fred "Простите, Мэм?"

    m "И пунктуальности."

    fred "Простите, Мэм?
    Я не расслышал."

    m "Смотри на дорогу."

    fred "Конечно, Мэм!"

    menu:
        "Продолжить задирать Фреда":
            jump drive_speak_monica_office_2
        "Молча ехать и смотреть инстаграм.":
            return
label drive_speak_monica_office_2:
    call bitch(1, "fred_monica_office2") from _call_bitch_66
    sound snd_car_engine
    imgr 1128
    with fade
    fred "Куда мы направляемся, Мэм?"

    imgl 1129
    m "Надо же, удосужился спросить."

    "Едешь куда глаза глядят, как всегда."

    "Даже не знаешь куда."

    fred "Я еду и ожидаю Ваших распоряжений, Мэм."

    fred "Как я могу предположить, мы едем, как обычно, в фитнесс зал?"

    imgl 1130
    m "Ты не угадал на этот раз, Фред!"

    m "Мы не едем в фитнесс зал!"

    fred "Куда же мы едем, Мэм?"

    imgl 1131
    m "Мы едем в Офис."

    m "Из-за таких растяп как ты, я сегодня потратила много времени и уже опаздываю."

    m "Так что едь быстрее."

    imgr 1133
    fred "Я еду по правилам, Мэм!"

    imgl 1132
    m "Правила задаю Я!"

    "Запомни!"

    menu:
        "Продолжить задирать Фреда":
            jump drive_speak_monica_office_3
        "Молча ехать и смотреть инстаграм.":
            return

label drive_speak_monica_office_3:
    call bitch(1, "fred_monica_office3") from _call_bitch_67
    sound snd_car_engine
    imgl 1131
    with fade
    m "Да, кстати, Фред!"

    imgr 1133
    fred "Слушаю, Мэм."

    m "У меня сегодня встреча вечером."

    "Так что будь вовремя у моего офиса, ты понял??"

    fred "Мэм, я буду вовремя, как всегда!"

    imgl 1129
    m "Ты не всегда бываешь вовремя, Фрэд!"

    fred "Мэм, я ни разу не опаздывал к Вам."

    "Если Вы про тот случай, то я просто стоял чуть подальше чем обычно."

    "Так как рядом не было парковочных мест!"

    imgl 1131
    m "Я вышла.
    Тебя на месте не было."

    "Все просто!"

    imgr 1133
    fred "Я стараюсь, Мэм!"

    menu:
        "Продолжить задирать Фреда":
            jump drive_speak_monica_office_4
        "Молча ехать и смотреть инстаграм.":
            return

label drive_speak_monica_office_4:
    call bitch(1, "fred_monica_office4") from _call_bitch_68
    sound snd_car_engine
    imgr 1133
    with fadelong
    fred "Уже почти приехали, Мэм!"

    imgl 1127
    m "Помолчи.

    Ты меня уже утомил."

    imgr 1128
    with fadelong
    fred "Мэм, мы приехали."

    imgl 1130
    m "Мог бы ехать и побыстрее!"

    fred "Я старался, Мэм!"

    imgl 1132
    m "Плохо старался, Фред!"

    fred "Простите, Мэм."

    m "Жди меня здесь."

    fred "Конечно, Мэм!"

    return


label drive_speak_monica_dick_day1_need_refuel1:
    imgl 1335
    m "Поехали к офису Дика.
    Ты знаешь где он находится?"

    imgr 1336
    fred "Да, Мэм."

    "Я знаю где он."

    "..."

    "Мэм, у нас небольшая проблема."

    music Groove2_85
    imgl 1337
    m "Что???"

    "Проблема?"

    menu:

        "Проблемы могут быть только у тебя!":
            call bitch(1, "fred_monica_fuel1") from _call_bitch_69
            $ fredOffendedRefuel = True
            m "Что за проблема?"

            "У нас не может быть проблем, Фрэд."

            "Проблемы могут быть только у тебя!"

            "..."

            "Рассказывай, что у тебя за проблема?"

            "Хотя я сомневаюсь что мне это будет интересно."

        "Что за проблема?":
            music casualMusic
            m "Что за проблема?"
            $ fredOffendedRefuel = False

    fred "Нам надо заехать на заправку, Мэм."

    if fredOffendedRefuel == True:
        imgl 1338
        m "Что???"

        "На какую еще заправку, Фрэд?"

        "Мы едем за Диком."

        fred "Да, Мэм.
        Я понимаю."

        "Но мы не доедем до места назначения, если не заправимся."

    $ map_objects["Teleport_Monica_Office"]["state"] = "disabled"
    $ subst_to_object("Teleport_Monica_Office", "drive_speak_monica_dick_day1_need_refuel1_map_refuse")
    $ map_objects["Teleport_Dick_Office"]["state"] = "disabled"
    $ subst_to_object("Teleport_Dick_Office", "drive_speak_monica_dick_day1_need_refuel1_map_refuse")
    $ map_objects["Teleport_House"]["state"] = "disabled"
    $ subst_to_object("Teleport_House", "drive_speak_monica_dick_day1_need_refuel1_map_refuse")

    $ map_objects["Teleport_Gas_Station"]["state"] = "visible"
    $ subst_to_object("Teleport_Gas_Station", "drive_speak_monica_dick_day1_need_refuel2")

    $ autorun_to_object("street_gas_station", "drive_speak_monica_dick_day1_need_refuel3")
    $ add_objective("fuel_car", _("Заправить машину топливом"), c_green, 25)
    $ driveCanceled = True
    $ scene_transition = "Fade"
    $ hud_preset_current = "map_locked"
    call refresh_scene() from _call_refresh_scene_19
    return

label drive_speak_monica_dick_day1_need_refuel1_map_refuse(obj_name, obj_data):
    fred "Мэм, мы не доедем до места назначения, если не заправимся."
    return

label drive_speak_monica_dick_day1_need_refuel2(obj_name, obj_data):
    sound snd_car_engine
    if fredOffendedRefuel == True:
        imgl 1339
        with fadelong
        m "Фрэд!
        Ты вообще нормальный или как??"

        "Ты водитель!
        Ты должен заботиться о керосине."

        "Колесах."

        "Не знаю что там еще."

        imgr 1336
        fred "О бензине, Мэм.
        Не о керосине."

        imgl 1340
        m "Да хоть о воздухе, Фрэд!"

        "Это не мои проблемы!"

        "Я из-за тебя вынуждена опаздывать на встречу с человеком."

        "Ты вообще понимаешь что тебе за это грозит?"

    else:
        imgl 1337
        with fadelong
        m "Фред!
        Вообще-то я опаздываю на встречу!"

    imgr 1341
    fred "Я понимаю, Мэм.
    Простите меня."

    "Компьютер показывал неверные значения запаса хода."

    if fredOffendedRefuel == True:
        imgl 1342
        m "Я нереально зла на тебя, Фрэд."


    $ hud_preset_current = "default"
    call process_drive_teleport_direct("Gas_Station", "street_gas_station") from _call_process_drive_teleport_direct
    return


label drive_speak_monica_dick_day1_need_refuel3: #разговор на заправке
    if fredOffendedRefuel == True:
        imgr Driver_Stand
        imgl Monica_BusinessCloth1_Arrogance1
        m "Фред!"
        "Мне показалось что заправка находится дальше чем мы ехали бы до Дика!"
        fred "Да, Мэм!
        Но это не конечная точка нашего маршрута, как я полагаю?"
        "Мы бы доехали только туда.
        У нас не осталось бы топлива на движение дальше."

        m "...!!!
        Фред!"
        "Давай быстро заправляйся.
        Я потом разберусь с тобой."
    else:
        m "Ладно, Фред.
        Давай быстро заправляйся."

#    imgr 1336
    fred "Да, Мэм.
    Это займет минуту."

    img black_screen
    with Dissolve(1)
    pause 1
    $ autorun_to_object("street_gas_station", "drive_speak_monica_dick_day1_need_refuel4")
    $ scene_transition = "Fade"
    call refresh_scene() from _call_refresh_scene_20
    return

label drive_speak_monica_dick_day1_need_refuel4:
    imgr Driver_Stand
    fred "Мэм, простите."

    "У них сломался компьютер и они не принимают наш предоплаченный документ."

    imgl Monica_BusinessCloth1_Arrogance1
    m "И?"

    fred "Нам не получается заправиться, Мэм."

    m "Заплати картой."

    fred "Мэм, у них не работает компьютер и терминал."

    m "Заплати наличными."

    fred "Они не принимают наличные, Мэм."

    menu:
        "Ты глупый никчемный человек, Фрэд.":
            $ fredOffendedRefuel2 = True
            call bitch(2, "fred_monica_fuel2") from _call_bitch_70

            imgl Monica_BusinessCloth1_Exclamation1
            m "О, Фрэд.
            Я все понимаю."

            fred "Спасибо, Мэм."

            m "Я все понимаю."

            m "Я понимаю что если что-то надо сделать, то надо делать это самой."

            m "Ты, как и все остальные работники, ни на что не способен."

            imgl Monica_BusinessCloth1_Angry2
            m "Ты глупый никчемный человек, Фрэд."

            "..."

            "Я пойду и разберусь сама."

            "А ты жди здесь.
            Больше от тебя толка нет."

            fred "Да, Мэм."

        "Ты сделал что мог.":
            $ fredOffendedRefuel2 = False
            call bitch(-2, "fred_monica_fuel2") from _call_bitch_71
            imgl Monica_BusinessCloth1_Angry3

            m "Это плохие новости, Фрэд!"
            fred "Мэм, простите."
            m "Но я понимаю, что ты испробовал все варианты.
            Это не твоя вина."
            fred "Спасибо, Мэм."

            m "Я пойду и попробую разобраться сама."
            fred "Да, Мэм."
            if dickMonicaOffended1 == False:
                imgl Monica_BusinessCloth1_Thinking2
                mt "В конце концов я даже Дику сказала что я самостоятельная и со всем могу справиться сама..."
                "Пришла пора это доказать!"

    $ gasStationFindingFuelQuest = True
    music casualMusic

    $ subst_to_object("Teleport_Monica_Office", False)
    $ subst_to_object("Teleport_Dick_Office", False)
    $ subst_to_object("Teleport_House", False)
    $ subst_to_object("Teleport_Gas_Station", False)

    $ autorun_to_object("gas_station_view1", "gas_station_no_saleswoman_caption")

    $ scene_transition = "Fade"
    $ map_enabled = False
    $ gasStationFindingFuelQuest = True
    call refresh_scene() from _call_refresh_scene_21
    return


label drive_speak_monica_fred_fitness(target_scene):
    sound snd_car_engine
    imgl 1514
    with fadelong
    m "Едем в фитнес-зал."

    imgr 1515
    fred "Принято, Мэм."
    menu:
        "Задирать Фреда.":
            $ fredOffendedDriveFitness1 = True
            m "Куда принято?"
            fred "Принято к исполнению, Мэм."
            imgl 1516
            call bitch(1, "fredOffendedDriveFitness1")
            m "Фред, ты говоришь как болван."
            imgr 1517
            fred "..."

            sound snd_car_engine
            imgr empty
            imgl 1518
            with fadelong
            m "Фрэд."
            imgr 1515
            fred "Да, Мэм?"
            menu:
                "Продолжить задирать Фреда":
                    $ fredOffendedDriveFitness2 = True
                    m "У тебя есть в машине керосин?"
                    fred "Не в машине, Мэм."
                    "В баке."
                    "И бензин, а не керосин."

                    m "Фред!"
                    "Ты прекрасно понимаешь что я имеюю ввиду!"
                    "Меня не интересует устройство машин."
                    fred "Вам не интересно, Мэм?"
                    imgl 1519
                    m "Вообще ни капли, Фрэд!"
                    "Это удел грязных механиков."
                    call bitch(1, "fredOffendedDriveFitness2")
                    "Таких как ты."
                    "Все обслуживать, готовить к работе и тд."
                    "А дело таких как я вами командовать."
                    imgr 1517
                    fred "Да, Мэм."
                    "Конечно Мэм."

                    sound snd_car_engine
                    imgl empty
                    imgr 1515
                    with fadelong
                    fred "Сегодня снова на удивление мало машин, Мэм."
                    "Мы доедем быстро."
                    menu:

                        "Продолжить задирать Фреда":
                            $ fredOffendedDriveFitness4 = True
                            call bitch(1, "fredOffendedDriveFitness4")
                            imgl 1518
                            m "Быстро - это не про тебя, Фред."
                            "Ты всегда едешь как черепаха."
                            fred "Но я соблюдаю правила, Мэм."
                            m "Я тебе уже говорила по поводу правил, забыл?"
                            fred "Да, Мэм."
                            "Я помню."

                            sound snd_car_engine
                            imgl empty
                            imgr 1515
                            with fadelong
                            fred "Почти приехали, Мэм."
                            menu:
                                "Продолжить задирать Фреда":
                                    $ fredOffendedDriveFitness3 = True
                                    imgl 1518
                                    call bitch(1, "fredOffendedDriveFitness3")
                                    m "Почти мне не интересно."
                                    "Когда приедем, тогда скажи."
                                    "А пока не отвлекай меня."
                                    "Я думаю о работе."
                                    imgr 1517
                                    fred "Конечно, Мэм."
                                    "Извините Мэм."
                                    imgl 1520
                                    mt "А мне понравилось как я выгляжу на обложке."
                                    "Надо будет снова сняться для журнала в ближайшее время."
                                    "Это будет чудесно."
                                    "Мммммм...."
                                    pass
                        "Молча ехать и смотреть инстаграм.":
                            pass
                "Молча ехать и смотреть инстаграм.":
                    m "Ничего!"
        "Молча ехать и смотреть инстаграм.":
            pass
    return












#
