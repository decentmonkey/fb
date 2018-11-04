#dickMonicaIdiotsAround - True: вокруг одни идиоты, False: либо я самостоятельная
#dickMonicaOffended1 - True: Я знаю что я обещала, а ты давно ждешь. Но у меня как-то нет настроения сейчас общаться с тобой.
#dickDriveDialOffend1 - True: Я сегодня уже слышала это. И тот кто это сказал был болваном., False: Погода нелохая, Дик.

#dickClothShopOffended1 and dickClothShopOffended2 - True: ты уродливый и уродливый галстук, False: либо у тебя смешной галстук
#dickClothShopOffended3 - True: я сама могу за себя заплатить, False: Если тебе это так нужно, то плати.
#dickClothShopOffended4 - True: идем, плюшевый мишка, False: Идем, Дик. Идем, мой кавалер.
#dickDriveRestaurantOffended1 - True: ты виноват что уже поздно, не отвез меня в нормальный магазин, False: Зато мы купили платье!
#dickCarKickedOut - True: Выбросить его прямо здесь..., False: Отвезти к офису...
#dickMonicaSaidToFredOffend - True: Дик жирный урод!, False: Дик облажался, но он старался...
#richHotelRestaurantDickOffended1ChoiceMade - True: Сказать Дику что он смешной. Ресторан

default dickMonicaCabinetOffended = False
default dickIncomingCallDay1PhoneRingedAlready = False
default dickMonicaIdiotsAround = False
default dickMonicaOffended1 = False
default dickMeetingPlannedDay1 = False
default dickRefuelPlanned = False
default dickClothShopOffended1 = False
default dickClothShopOffended2 = False
default dickClothShopOffended3 = False
default dickClothShopOffended4 = False

default dickDriveRestaurantOffended1 = False

default dickMeeting1Drive1DialoguePlanned = False
default dickDriveDialOffend1 = False
default dickBuyDressInProgress = False
default dickDressBrought = False
default dickMeeting1RestaurantPlanned = False
default dickWaitingMonica2 = False
default dickWaitingMonica3 = False
default dickWaitingMonica4 = False
default dickCarKickedOut = False
default dickMonicaSaidToFredOffend = False
default richHotelDickMeetingExitClosed = True

default dickHelpsMoniceSue = False
default dickWantFuckMelanie = False

default richHotelRestaurantDickOffended1ChoiceMade = False
default richHotelRestaurantDickOffended1 = False

label dickIncomingCallDay1_subst(obj_name, obj_data):
label dickIncomingCallDay1:

    $ remove_objective("go_work")
    $ add_objective("take_phone", _("Взять трубку"), c_orange, 20)

    sound snd_phone_ring
    pause 1.5
    if dickIncomingCallDay1PhoneRingedAlready == False:
        m "Кажется это звонит мой телефон!"
        "Кто бы это мог быть?"
        "Этот номер еще не известен прессе, поэтому это может быть либо Дик, либо очень влиятельный поклонник, раз ему удалось узнать номер."
    else:
        m "Телефон все еще звонит, думаю мне надо взять трубку."
        "Этот номер еще не известен прессе, поэтому это может быть либо Дик, либо очень влиятельный поклонник, раз ему удалось узнать номер."

    $ subst_to_object("Teleport_Monica_Office_Secretary", "dickIncomingCallDay1_subst")
    $ subst_to_object("Phone", "dickIncomingCallDay1_2")
    $ dickIncomingCallDay1PhoneRingedAlready = True

    return

label dickIncomingCallDay1_2(obj_name, obj_data): #take phone
    if obj_data["action"] == "l":
        sound snd_phone_ring
        m "Телефон звонит.
        Мне надо взять трубку"
        return
    if obj_data["action"] == "t":
        sound snd_phone2
        $ remove_objective("take_phone")
        mt "Это Дик!"
        img 1321
        with fade
        m "Алло?"

        "Дик?"

        dick "Привет, Моника."

        "Привет, моя дорогая."

        "Ты помнишь про нашу встречу?"

        img 1322
        m "Да... Дик... Я помню..."

        "Знаешь, вообще-то уже поздно."

        "Я сегодня задержалась с утра."

        menu:
            "Из-за идиотов, которые меня окружают.":
                call bitch(2, "dick_phone_call1_dial1") from _call_bitch_32
                $ dickMonicaIdiotsAround = True
                "Потом был день, полный идиотов."

                "Ну ты знаешь как это бывает."

                dick "О да!"

                "Моника!"

                "Я знаю."

                "Мир вокруг нас просто кишит никчемными людьми."

                img 1323
                m "О Дик!"

                "Как ты меня хорошо понимаешь!"

                dick "Да, милая Моника."

                "Я тебя очень хорошо понимаю."

            "Из-за проблем, с которыми я справилась сама.":
                call bitch(-2, "dick_phone_call1_dial1") from _call_bitch_33
                $ dickMonicaIdiotsAround = False
                m "Из-за проблем, с которыми я справилась сама."
                dick "О, милая Моника.
                Я знаю что ты самостоятельная девочка."
                "И можешь справиться с чем угодно!"
                img 1325
                m "Да, Дик!"

                img 1322

        dick "Так что насчет нашей встречи?"

        img 1324
        m "Дик, может быть перенесем ее?"

        "Я знаю что я обещала, а ты давно ждешь."

        if dickMonicaIdiotsAround == False:
            menu:
                "Но у меня как-то нет настроения сейчас общаться с тобой.":
                    m "Но у меня как-то нет настроения сейчас общаться с тобой."
                    $ dickMonicaOffended1 = True
                    call bitch(2, "dick_phone_call1_dial2") from _call_bitch_34

                "Но устала за сегодня, потому что справлялась со всем сама.":
                    img 1323
                    m "Но устала за сегодня, потому что справлялась со всем сама."
                    $ dickMonicaOffended1 = False

        dick "Моника.
        Моя хорошая."

        "Но ты ведь обещала, а я так ждал."

        "Ты ведь не будешь так поступать со мной?
        Ты ведь не хочешь чтобы я сильно переживал?"

        "Вдруг ты вообще никогда не захочешь меня видеть..."

        img 1325
        m "Ну что ты, Дик."

        "Ну... Ладно..."

        "Так уж и быть.
        Мы встретимся."

        "Не обижайся."

        dick "Я не обижаюсь, Моника.
        Просто ты же знаешь я жду нашей встречи."

        img 1326
        mt "Конечно ждешь.
        Особенно узнав что мой муж уехал на несколько дней."

        "Так уж и быть, я с ним встречусь."

        "Но я примерно знаю чего он хочет."

        if dickMonicaIdiotsAround == True or dickMonicaOffended1 == True:
            mt "И у этого жирного толстяка нет шансов добиться желаемого."
        else:
            mt "И у него нет шансов добиться желаемого."

        img 1327
        m "Дик.
        Я собираюсь выезжать с работы."

        "Будь готов, я за тобой заеду."

        dick "Дорогая, ты не хочешь чтобы я прислал своего водителя?"

        m "У меня есть свой водитель, Дик!"

        "Я гордая и самостоятельная женщина."

        if dickMonicaIdiotsAround == True or dickMonicaOffended1 == True:
         "Мне не нужны твои услуги!"

        dick "Хорошо, хорошо."

        "Моника, я буду тебя ждать."

        "Целую."

        img 1328
        if dickMonicaIdiotsAround == True or dickMonicaOffended1 == True:
            m "Я тебя нет, Дик, до встречи."
        else:
            m "...."

        dick "До встречи, Моника, буду ждать!"

        img 1329
        with fade
        m "Итак, встреча с Диком."

        "..."

        img 1330
        m "Что это?
        Что с моим платьем?"

        img 1331
        "Оно мятое?
        Но я же его гладила!"

        m "Не может же быть чтобы я его плохо погладила!"

        img 1332
        "Это, наверное, плохой утюг."

        if juliaPunished == True or juliaPunishedLow == True:
            call bitch(1, "dick_phone_call1_dial3") from _call_bitch_35
            "Никчемная вещь!"

        if juliaPunished == True or juliaPunishedLow == True:
            call bitch(1, "dick_phone_call1_dial4") from _call_bitch_36
            m "Вообще это все из-за этой Юлии!"

        if juliaPunished == True:
            call bitch(2, "dick_phone_call1_dial4") from _call_bitch_37
            m "Наверное она сейчас все еще трет то пятно."

            img 1333
            m "Кто-то трет пятно, а кто-то встречается с богатым и влиятельным мужчиной."

            "У каждого своя жизнь.
            Хи-хи."

            m "..."
            img 1334
            "Но все-же, что мне делать с платьем?"
        else:

            img 1334
            "Что же мне делать с платьем?"

        m "Не могу же я пойти в таком виде куда-то?"

        "Я должна быть безупречная!"

        m "Я же королева!"

        "...."

        m "Что же делать?"

        m "..."

        "Хм. Заедем куда-нибудь с Диком."

        "Пусть купит мне платье."

#imgl:Monica_BusinessCloth1_Злость1
        if dickMonicaIdiotsAround == True or dickMonicaOffended1 == True:
            m "Надо же хоть что-то получить за свое согласие встретиться с ним!"
        else:
            m "Я думаю он захочет сделать мне приятно!"

        $ add_objective("go_dick_day1", _("Отправиться на встречу с Диком"), c_orange, 20)
        $ subst_to_object("Teleport_Monica_Office_Secretary", False)
        $ subst_to_object("Phone", False)
        $ monicaOfficeSteveCall1Planned = False
        $ dickMeetingPlannedDay1 = True

        $ map_objects["Teleport_Dick_Office"]["state"] = "visible"

        return
























#
