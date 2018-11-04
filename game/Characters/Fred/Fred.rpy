default bFredFollowingMonica = True
default fredOffendedRefuel = False
default fredOffendedRefuel2 = False

default fredOffendedDriveFitness1 = False
default fredOffendedDriveFitness2 = False
default fredOffendedDriveFitness3 = False
default fredOffendedDriveFitness4 = False
default fredOffendedDriveReturnDress1 = False

label get_to_drive_dialogue:
    if bFredFollowingMonica:
        imgr Driver_Stand
        fred "Мэм, вы готовы ехать?"
        menu:
            "Да, поехали.":
                m "Да, поехали."
                call map_show(True) from _call_map_show
                return
            "Нет, жди меня здесь.
            И помалкивай.":
                m "Нет, жди меня здесь.
                И помалкивай."
                imgr Driver_Stand
                fred "Конечно, Мэм."
                "Как скажете."
                return
    return

label get_to_drive_dialogue_return_result:
    imgr Driver_Stand
    fred "Мэм, вы готовы ехать?"
    menu:
        "Да, поехали.":
            m "Да, поехали."
            return True
        "Нет, жди меня здесь.
        И помалкивай.":
            m "Нет, жди меня здесь.
            И помалкивай."
            imgr Driver_Stand
            fred "Конечно, Мэм."
            "Как скажете."
            return False
    return

label monica_looking_to_fred1:
    m "Фи...
    Это всего-лишь Фред."
    "Мой водитель."
    "Он работает недавно, но уже успел мне поднадоесть."
    "У меня вообще почти никто долго не работает."
    "В этом мире очень трудно найти действительно компетентных работников!"
    return

label monica_fred_day1_evening_dialogue:
    imgr Driver_Stand
    fred "Мы приехали, Мэм."

    "Спокойной ночи Вам!"

    imgl Dial_MonicaEveningDress_3
    m "Все, Фред."

    "Ты меня утомил за день."

    "Не хочу тебя видеть."

    "Убирайся."

    fred "Хорошо, Мэм!"

    $ miniMapEnabledOnly = ["Street_Yard", "Floor1"]

    return
label monica_fred_day1_evening_dialogue2:
    imgr Driver_Stand
    fred "Мэм."
    "До завтра."
    "Спокойной ночи!"
    return

label monica_fred_day2_morning_dialogue1:
    music Mandeville
    imgr Driver_Stand
    fred "Доброе утро, Мэм!"
    $ driverMode = 0
    call get_to_drive_dialogue()
    return
