
label dick_meeting1:
    $ dickWaitingMonica1 = True
    $ remove_objective("go_dick_day1")
    $ bDickFollowingMonica = True

    music Poppers_and_Prosecco

    imgr Dick1
    dick "Привет, дорогая!"

    imgl Monica_HomeCloth1_Dick1
    m "Привет, Дик!"

    dick "Я заждался тебя!"

    imgl Monica_HomeCloth1_Dick2
    m "Дик, ну я же сама предлагала перенести нашу встречу."

    m "Это ты настаивал."

    "Теперь не жалуйся."

    imgr Dick2
    dick "Что ты, Моника."

    "Я не жалуюсь."

    "Я очень рад тебя видеть!"

    m "Куда поедем, Дик?"

    dick "Я предлагаю поехать в роскошный отель с рестораном La Grand."

    m "А просто ресторана без отеля нет?"

    dick "Там самый лучший ресторан в городе!"

    "Вот увидишь!"

    m "Хорошо, Дик."

    imgl Monica_HomeCloth1_Dick3
    "Но тогда мы поедем и ты купишь мне новое платье."

    dick "Конечно, Моника."

    "Буду рад сделать тебе приятно."

    "Правда сейчас уже почти все магазины закрыты."

    "Уже вечереет."

    "Но я знаю один магазин, который еще должен работать."

    "Поехали туда."

    m "Поехали, Дик!"

    "Садись в машину."

    $ monicaEnterCarLookingCharacter = "Dick"
    $ add_objective("drive_to_cloth_shop", _("Ехать с Диком в магазин одежды"), c_orange, 25)
    $ dickMeeting1Drive1DialoguePlanned = True
    $ focus_map("Teleport_Cloth_Shop", "dick_meeting1_map_disabled")

#    music casualMusic
    return


label dick_meeting1_map_disabled(obj_name, obj_data):
    dick "Моника! Мы же собирались ехать в магазин!"
    "Ты передумала?"
    m "Нет, Дик!
    Я не передумала!"
    "А где он?"
    dick "Моника, садись!
    Я покажу твоему водителю куда ехать!"
    return

label dick_waiting_monica_dialogue1:
    imgr Dick1
    dick "Дорогая, мы едем?"
    return

label drive_speak_monica_dick_day1_drive1():
    sound snd_car_engine
    img 1343
    with fadehold
    $ dickWaitingMonica1 = False
    dick "Сегодня отличная погода, правда, Моника?"

    menu:
        "Я сегодня уже слышала это. И тот кто это сказал был болваном.":

            $ dickDriveDialOffend1 = True
            img 1344
            m "Я сегодня уже слышала это."

            img 1345
            "И тот кто это сказал был болваном."
            call bitch(1, "dickDriveDialOffend1")

            img 1347
            w
            img 1346
            fred "Гхм..."

            m "Дик, будь оригинальнее."

            dick "Ты не рада погоде, дорогая?"

            m "Я рада когда люди себя ведут не как идиоты, Дик."

        "Погода нелохая, Дик.":
            m "Да, Дик.
            Погода сегодня и впрямь неплохая."

            img 1346
            dick "Я рад, дорогая."

    sound snd_car_engine
    img 1348
    with fadehold
    m "Мы уже довольно далеко отъехали от центра, Дик."

    "Все хорошие магазины, которые я знаю, находятся в центре."

    dick "Дорогая, я везу тебя в самый лучший магазин."

    "Из тех что открыт."

    $ unfocus_map()

    $ autorun_to_object("street_cloth_shop", "drive_speak_monica_dick_day1_drive2")

    $ dickBuyDressInProgress = True
    $ remove_objective("drive_to_cloth_shop")
    $ add_objective("dick_cloth_shop_buy_dress", _("Подобрать подходящее платье в магазине"), c_orange, 25)

    return

label drive_speak_monica_dick_day1_drive2():
    imgr Driver_Stand
    fred "Мы приехали, Мэм!"

    menu:
        "Не разговаривай со мной в присутствии других людей, пока я к тебе не обращусь.":
            imgl Monica_BusinessCloth1_Angry2
            m "Не разговаривай со мной в присутствии других людей, пока я к тебе не обращусь."

            "ЯСНО ТЕБЕ?!"
            call bitch(1, "fred_monica_cloth_shop1")

            fred "Да, Мэм."

            "Конечно."

            "Я понял."

        "Хорошо, Фред. Я вижу.":
            imgl Monica_BusinessCloth1_Angry3
            m "Хорошо, Фред. Я вижу."
    return

label dickBuyDressEnterShop():
    music casualMusic
    pause 1
    img 1349
    with fade
    w
    img 1350
    m "Надо же, в этой дыре даже есть покупатели..."

    sound highheels_run1
    img 1351
    with fade
    cashier "Добрый вечер, Сэр!"

    "Добрый вечер, Мэм!"

    "Чем могу Вам помочь?"

    "Могу предложить помощь в выборе гардероба."

    img 1352
    m "Спасибо."

    "Я сама разбираюсь в одежде и в моде."

    "Мы справимся без вас."

    "Пожалуйста, исчезните."

    cashier "Хорошо, мэм."

    "Как скажете."
    img 1353
    w
    sound highheels_run1

    img 1355
    with fade
    m "Ладно, Дик."

    "Давай посмотрим что тут есть."

    dick "Конечно, дорогая."

    "Выбирай все что тебе понравится."

    call question_helper_enable("question_cloth_shop_dick_buy_dress")

    $ scene_transition = "Fade_long"
    call refresh_scene()
    return

label dick_meeting1_after_cloth_shop_init:
    call dick_meeting1_restaurant_init()
    return
