label dick_meeting1_car_parting1:
    $ dick_meeting1_restaurant_drive_dialogue1_planned = False
    $ richHotelReceptionDickEnabled = False
    $ richHotelReceptionistEnabled = True
    imgr Dick4
    imgl Dial_MonicaEveningDress_2
    dick "Дорогая! Пожалуйста, садись в машину!"
    return

label dick_meeting1_car_parting2:
    call get_to_drive_dialogue_return_result()
    if _return == False:
        return
    $ remove_objective("dick_meeting1_goto_car")
    $ richHotelClosed1 = True
    $ richHotelReceptionDickEnabled = False
    $ photostudioEmpty = True
    $ dickMeeting1RestaurantPlanned = False
    call get_into_car()
    sound snd_car_turn_on
    img 1437
    with fadelong
    m "Сначала дешевый магазин в какой-то дыре..."
    "Затем пустой ресторан..."
    m "Ну что, дорогой?"
    "Наш вечер на сегодня окончен?"

    dick "Моника."
    "Ты знаешь, по пути к тебе домой есть один бар."
    "Может быть заглянем туда на минутку?"
    "Там весело!"

    sound snd_car_engine
    img 1437
    m "Дик."
    "Я даже не знаю."
    "Может в другой раз?"

    img 1438
    dick "Ну дорогая."
    "Я с тобой даже не успел побыть."

    sound snd_car_engine
    img 1400
    m "Нет, Дик!"
    "Ты уже дважды разочаровал меня!"
    "Боюсь что третий раз уже слишком сильно скажется на наших отношениях!"
    "А ты для меня пока еще полезен."
    img 1401
    "Пока еще..."
    img 1402
    dick "Хорошо, Моника."
    "Отвезешь меня к дому?"

    menu:
        "Выбросить его прямо здесь...":
            sound snd_car_engine
            call bitch(5, "dickCarKickedOut")
            $ dickCarKickedOut = True
            img 1439
            m "Дик, ты правда думаешь что я буду тратить время чтобы отвозить тебя домой?"
            img 1438
            dick "Дорогая, я бы тебе показал где я живу и..."
            img 1437
            m "Нет, Дик!"
            "Я не куплюсь на такую уловку!"
            "Мне неинтересно где ты живешь!
            Я не хочу этого знать!"
            m "..."
            img black_screen
            imgc 1440
            m "И вообще, Дик!"
            "Это случилось!"
            dick "Что, Моника?"
            m "Ты умудрился мне надоесть, в конце концов!"
            img black_screen
            imgl 1441
            m "Фред!"
            imgr 1444
            fred "Да, Мэм?"
            imgl 1441
            m "Фред, быстро останови машину!"
            "Мистеру Дику надо срочно выйти!"
            imgr 1442
            fred "Конечно, Мэм!"
            call process_change_map_location("Cloth_Shop")
            $ autorun_to_object("street_cloth_shop", "dick_meeting1_car_parting3")
            call change_scene("street_cloth_shop", "Fade_long", "snd_car_engine")
        "Отвезти к офису...":
            sound snd_car_engine
            call bitch(-2, "dickCarKickedOut")
            img 1439
            m "Дик, ты правда думаешь что я буду тратить время чтобы отвозить тебя домой?"
            img 1438
            dick "Дорогая, я бы тебе показал где я живу и..."
            img 1437
            m "Нет, Дик!"
            "Я не куплюсь на такую уловку!"
            "Мне неинтересно где ты живешь!
            Я не хочу этого знать!"
            m "..."
            img 1439
            m "Хорошо.
            Я отвезу тебя к твоему офису."
            "Тебя устроит это?"
            img 1438
            m "Хорошо, дорогая!
            Меня это устроит!"
            $ bDickFollowingMonica = False
            $ dickWaitingMonica4 = False
            $ bDickFollowingMonica = False
            $ monicaEnterCarLookingCharacter = "Fred"
            call process_change_map_location("Dick_Office")
            $ autorun_to_object("street_dick_office", "dick_meeting1_car_parting3")
            call change_scene("street_dick_office", "Fade_long", "snd_car_engine")
    return

label dick_meeting1_car_parting3:
    imgr Dick5
    dick "Мне очень жаль что все так вышло в этот вечер..."

    imgl Dial_MonicaEveningDress_3
    m "Дик, ты испортил все с самого начала."
    if scene_name == "street_cloth_shop":
        m "Нам повезло что мы как раз проезжали мимо той дыры, куда ты привез меня!"
        "Вот и оставайся здесь!
        А я не хочу тебя видеть!"
    imgr Dick6
    dick "Дорогая, но ты должна меня понять."
    "Ведь я стараюсь."
    "Если у тебя есть какие-то желания, я все сделаю для тебя."

    imgl Dial_MonicaEveningDress_4
    m "Ладно, Дик."
    "Я подумаю о том что ты можешь для меня сделать еще."
    "Но сейчас я поеду домой."
    "А ты добирайся сам!"
    "ПОНЯЛ??"
    dick "Да, Моника."
    "Я понял."
    m "Тогда пока!"
    dick "До встречи, Моника."
    "Буду ждать."
    $ drivingPlacePlannedArray["House"] = "dick_meeting1_car_parting4_fred_dialogue"
    $ bDickFollowingMonica = False
    return

label dick_meeting1_car_parting4_fred_dialogue(target_scene):
    sound snd_car_engine
    imgl 1440
    m "Дик..."
    menu:
        "Дик жирный урод!":
            sound snd_car_engine
            $ dickMonicaSaidToFredOffend = True
            call bitch(2, "dickMonicaSaidToFredOffend")

            m "Вот ведь жирный урод!"
            "Испортил мне весь вечер своим присутствием."

            imgl 1441
            "Ты тоже так считаешь, Фред?"

            imgr 1442
            fred "Но Мэм."

            "На мой взгляд Вы ему нравитесь."

            "Он старался Вам угодить."

            imgl 1443
            m "Не спорь со мной, Фред!"

            "А лучше заткнись!"

            imgr 1444
            m "Хорошо, Мэм."
            "Конечно, Мэм."

        "Дик облажался, но он старался...":
            sound snd_car_engine
            call bitch(-2, "dickMonicaSaidToFredOffend")
            m "Дурацкий вечер!"
            "Этот Дик..."
            "Ландо, хоть он и облажался, но он, похоже, старался угодить мне."
            "Посмотрим, может с него еще будет какая-то польза..."
            "Но то что ему он может никогда не рассчитывать на секс со мной - это сто процентов!"
            imgl 1441
            m "Фред!"
            imgr 1444
            fred "Да, Мэм?"
            imgl 1441
            m "Долго ты будешь меня везти!?"
            imgr 1444
            fred "Мы уж почти приехали, Мэм!"
    $ driverMode = 1
    $ autorun_to_object("street_house_main_yard", "monica_fred_day1_evening_dialogue")
    call quest_house_monica_day1_evening_init()
    return
