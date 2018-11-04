default returnDressInProgress = False

label dress_return_drive1(target_scene):
    sound snd_car_engine
    music Walking_Sax2
    imgl 1904
    with fadelong
    m "Едем в тот дурацкий магазин одежды."
    "Где мы были вчера."
    "Но сначала заедем домой за платьем"

    imgr 1905
    fred "Хорошо, Мэм!"

    call textonblack(_("СПУСТЯ ЧАС..."))
    img scene_Map_Evening
    imgl 1904
    with Dissolve(1)
    $ add_inventory("shop_dress_eveningdress", 1, True)

    menu:
        "Задирать Фреда.":
            sound snd_car_engine
            imgl 1904
            m "Фрэд!"
            imgr 1905
            fred "Да, Мэм!"
            m "Ты так и не ответил тогда на вопрос про керосин?"
            fred "Мэм, я ответил."
            "Что в машину заливают бензин, а не керосин."
            imgl 1906
            m "Я имела ввиду все-ли у тебя есть?"
            "Вдруг снова чего-то нет и надо куда-то заехать?"
            "Сорвать мои планы."
            "Или что-то еще."
            imgr 1907
            fred "Нет, Мэм."
            "Бак заправлен!"

            m "Я к тому, Фред."
            "Что я не забыла твой промах."
            call bitch(1, "dress_return_drive1_1")

            fred "Мэм, простите еще раз..."

            menu:
                "Продолжить задирать Фреда":
                    sound snd_car_engine
                    imgl 1908
                    with fadelong
                    m "Не прощу, Фред."
                    "Ты реально кретин, понимаешь?"
                    "Полный идиот."
                    imgr 1907
                    fred "Мэм..."
                    m "Ну, скажи что-нибудь?"
                    "Попробуй!"
                    fred "Мэм..."
                    imgl 1909
                    m "Давай, урод, скажи!"
                    "Ты так держишь в руках себя!"
                    "Ну скажи что-нибудь в ответ."
                    call bitch(1, "dress_return_drive1_2")
                    "Дай мне повод уволить тебя."
                    imgr 1910
                    fred "Мэм."
                    "Вы не сможете вывести меня из равновесия."
                    imgl 1911
                    m "Почему это?"
                    fred "Мэм."
                    "Я проходил психологическую подготовку."
                    "Я профессионал."
                    "Мне не страшны любые стрессовые ситуации."
                    "Я могу держать себя в руках в любом случае."
                    imgl 1912
                    m "Ах вот оно что..."

                "Молча ехать и смотреть инстаграм.":
                    pass

        "Молча ехать и смотреть инстаграм.":
            pass

    $ autorun_to_object("street_corner", "dress_return_drive2")

    return

label dress_return_drive2:
    music Stealth_Groover
    imgl Dial_Monica_BusinessCloth2_1
    with fade
    m "Фред."

    imgr Driver_Stand
    fred "Да, Мэм."

    m "Фред.
    Куда ты меня привез?"

    "Я просила привезти меня в магазин."

    "Ты забыл?"

    fred "Нет, Мэм."

    "Но там не было парковочных мест."

    m "Там были места, Фред."

    fred "Нет, Мэм."

    "Сожалею, но их там не было."

    imgl Dial_Monica_BusinessCloth2_Angry1
    m "Ты специально сделал это, Фред?"

    "Ты специально нарываешься???"

    fred "Простите, Мэм!"

    "Я делал все что в моих силах!"

    "Там не было мест."

    "Хотите, я провожу Вас до магазина?"

    "Тут близко."

    imgl Dial_Monica_BusinessCloth2_Thinking
    m "Нет уж, спасибо!"

    "Кто-нибудь подумает что ты мой муж или что-нибудь еще."

    "А я не хочу чтобы кто-то подумал что я связалась с таким кретином как ты, Фред."

    fred "..."

    m "Жди меня здесь."

    "Я скоро вернусь."

    fred "Да, Мэм."

    "Конечно."

    $ whoresPlaceOpened = True
    $ returnDressInProgress = True
    $ autorun_to_object("whores_place", "dress_return_whores1")
    call refresh_scene_fade()
    return

label dress_return_whores1:
    img 1868
    with fadelong
    w
    img 1869
    with fade
    w
    img 1870
    with fade
    music All_Stars_Loop
    mt "Ого!"

    "А это у нас что?"

    "Шлюхи?"

    "Да уж..."

    "Самое дно."

    img 1871
    "Как раз место для Джейн или Тиффани."

    "..."

    img 1872
    "..."

    "Кого я вижу?"

    "Знакомая девушка."

    "Откуда?"

    "А, так это одна из моделей, которая приходила вчера на кастинг."

    "Уже вышла на панель?"

    img 1873
    "Ха-ха-ха."

    "Достойная карьера для такой модели!"

    "Надо подойти спросить..."
    music Stealth_Groover
    return

label dress_return_whores_talk1:
    menu:
        "Издеваться над проституткой!":
            $ grayMouse2WhoreOffended = True
            music Stealth_Groover
            img 1874
            with fadelong
            m "Я вижу ты быстро сделала карьеру, деточка?"

            img 1875
            w
            img 1876
            model2 "..."

            call bitch(8, "dress_return_whore1")
            img 1877
            m "Достойный финал для супермодели!"

            img 1878
            "Девочка, вот твое место."

            img 1879
            "Я пыталась тебе это объяснить, но не знала как."

            img 1880
            "Стой тут и наслаждайся карьерой."

            "Ха-ха."

            img 1881
            model2 "...."

            "(хмык)"

            img 1882
            w
            img 1883
            w
            img 1884
            with fadelong
            $ renpy.pause(0.5)
            img 1885
            with fadelong
            $ renpy.pause(0.5)
            img 1886
            with fadelong
            m "А эта старая шлюха - твоя мамочка?"
            "Помогает продавать свое тело?"
            "Фи!"
            img 1887
            mommy "..."

            img 1888
            m "Что смотришь?"

            img 1889
            music Master_Disorder
            mommy "Мэм."
            "Я хоть и старая, но у моих девочек всегда есть работа."
            "..."
            img 1890
            "Если будет желание, можете придти, я помогу вам устроиться."

            img 1891
            m "..."
            "Это я могу помочь тебе устроиться."

            "Поудобнее."

            img 1892
            "В полицейском участке!"

            img 1893
            mommy "Я прожила побольше вашего, Мэм."
            "Поверьте.
            Жизнь непредсказуемая штука."
            "И полицейский участок изнутри я знаю наизусть."

            img 1894
            "А вы бы сумели там удобно устроиться?"
            img 1895
            m "Ты меня утомляешь, старая карга."
            "Фи!"

        "Пожалеть ее...":
            music RnB4_100
            img 1875
            with fadelong
            m "Я тебя знаю."
            img 1876
            m "Ты та модель, которая приходила ко мне на кастинг."
            img 1879
            m "Если честно, то я недооценила твои проблемы."
            "Я не думала что у тебя все так плохо."
            call bitch(-8, "dress_return_whore1")
            "Возможно, тебе стоит снова придти ко мне."
            "Моделью работать ты не сможешь, но я не позволю чтобы люди, которые общались со мной, работали проститутками впоследствии."
            img 1880
            "Так что подумай..."

            img 1882
            music Master_Disorder
            with fadelong
            $ renpy.pause(0.5)
            img 1883
            with fadelong
            $ renpy.pause(0.5)
            img 1886
            with fadelong
            mommy "Мэээм..."
            "Обещания таких богатых и знаменитых как вы - они ничтожны."
            "Вы забудете эту девочку через 5 минут."
            "Не вселяйте напрасных надежд, не вы решаете ее судьбу."
            img 1888
            m "Что это за старая шлюха, которая меня прервала?"
            "Какое твое дело до всего этого?"
            img 1889
            mommy "Я забочусь о вашей душе, мадам."
            "Вы не только отвлекаете моих девушек от работы, но и вселяете в них ненужные надежды."
            "Уходите..."
            img 1890
            with fadelong
            "Если будет желание, можете придти, я помогу вам устроиться."
            img 1891
            m "..."
            "Это я могу помочь тебе устроиться."

            "Поудобнее."

            img 1892
            "В полицейском участке!"

            img 1893
            mommy "Я прожила побольше вашего, Мэм."
            "Поверьте.
            Жизнь непредсказуемая штука."
            "И полицейский участок изнутри я знаю наизусть."

            img 1894
            "А вы бы сумели там удобно устроиться?"
            img 1895
            m "Ты меня утомляешь, старая карга."
            "Фи!"
    $ whoresTalkStage = 1
    $ autorun_to_object("whores_place", "dress_return_whores_thinking1")
    $ autorun_to_object("whores_place_shawarma", "dress_return_shawarma_talk1")
    call refresh_scene_fade()
    return

label dress_return_whores_thinking1:
    mt "Ненормальная старая шлюха."
    "Будет еще меня учить жить."
    return

label dress_return_shawarma_talk1:
    music DarxieLand
    shawarma "Мадаме!"
    "Да!"
    "Вы!"
    "Мадаме!"
    "Подойдите сюда, скорее!"

    imgl Dial_Monica_BusinessCloth2_Angry1
    mt "Это он мне?"
    "Что ему надо?"
    music Stealth_Groover
    $ shawarmaTraderStage = 1
    return

label dress_return_shawarma_talk2:
    #shawarmaTraderOffended1
    music DarxieLand
    img 1897
    m "Что тебе надо?"
    "Как ты посмел ко мне обратиться?"

    shawarma "Мадаме!"
    "Не пропустите!"

    m "Что я не должна пропустить?"

    img 1898
    shawarma "Только у меня!"
    "Лучшая шаверма в округе!"
    "Даже лучшие рестораны завидуют мне!"
    "Весь район ее покупает!"
    "С удовольтвием!"
    "Ко мне даже приходят из других районов!"
    "Специально чтобы отведать мою шаверму!"
    "Из вкуснейших кусочков мяса, лаваша и сыра!"

    img 1899
    shawarma "Мадаме!"
    "Не проходите мимо!"

    menu:
        "О Боже! Что это за животное?!":
            $ shawarmaTraderOffended1 = True
            img 1900
            m "О Боже!"
            "Знаешь что??"
            "Такую еду едят только ЖИВОТНЫЕ!"
            "Ты ее ешь?"

            img 1898
            shawarma "Конечно, Мадаме!"

            img 1901
            call bitch(1, "shawarmaTraderOffended1")
            m "Вот значит и ты животное."
            "Удивительно что ты умеешь разговаривать."
            "Кто тебя дрессировал?"

        "Отказать мягче...":
            call bitch(-1, "shawarmaTraderOffended1")
            img 1899
            m "Простите, Мистер, но я не ем такую еду!"
            img 1897
            m "Я питаюсь в дорогих ресторанах!
            Так что Вы зря обратились ко мне!"

    img 1898
    shawarma "Мадаме!"
    "Если вы передумаете, я всегда к вашим услугам!"
    "Мадаме!"

    img 1902
    mt "Фу, что за место?"
    if shawarmaTraderOffended1 == True:
        "Шлюхи, животные."
    else:
        "Шлюхи, какие-то уличные продавцы..."
    "Кого я еще повстречаю по пути в этот магазин?"
    "Сам магазин тоже соответствует месту, кстати."

    img 1903
    "Не могу поверить что Дик привез меня сюда."
    "А Фред виноват в том что мне приходится идти мимо всего ЭТОГО!"
    "Надо поторопиться!"
    music Stealth_Groover
    $ shawarmaTraderStage = 2
    return

label dress_return_shawarma_talk3:
    imgr Dial_ShawarmaTrader1
    shawarma "Мадаме!"

    if cloth == "BusinessCloth2":
        imgl Dial_Monica_BusinessCloth2_Angry2
    if shawarmaTraderOffended1 == True:
        m "Кыш!!"
        "Животное!"
    else:
        m "Пожалуйста, оставьте меня в покое!"
    return

label dress_return_cashier_talk1:
    img 1913
    with fadelong
    cashier "Добрый вечер, Мэм!"
    "Вы решили еще что-нибудь подобрать?"
    "Рады видеть Вас!"

    img 1914
    music Pyro_Flow
    m "Я не собираюсь подбирать что-то еще в вашей дыре."

    img 1915
    "Я возвращаю вчерашнее платье."
    "Оно жуткое."

    img 1916
    cashier "Но Мэм."

    "Оно Вам прекрасно подходит."

    "На нем нет никаких дефектов."

    "Его нет нужды возвращать назад."

    img 1917
    m "Я не ношу такие дешевые платья."
    "Пусть оно дальше висит в вашем дешевом магазине."
    "И его купит какая-нибудь дура, у которой нет денег на нормальные вещи."

    img 1918
    "Так что возьмите его по хорошему и не тратьте мое время."
    "Иначе пожалеете."

    img 1919
    cashier "Мэм."
    "Как хотите, но..."

    menu:
        "Никаких НО, сучка!!":
            $ clothShopCashierOffended3ReturnDress = True
            img 1920
            m "Никаких НО!!"

            call bitch(3, "clothShopCashierOffended3ReturnDress")
            img 1921
            "Если ты сучка еще раз мне скажешь НО или будешь возражать мне, то я тебя засужу и закрою твой магазин к чертовой матери!"

            img 1922
            "ПОНЯТНО??"

            img 1923
            cashier "Хорошо, Мэм."

            img 1924
            w
        "Просто вернуть платье вежливо...":
            $ clothShopCashierOffended3ReturnDress = False
            music Stealth_Groover
            img 1917
            m "Девушка, я знаю свои права как потребителя."
            call bitch(-3, "clothShopCashierOffended3ReturnDress")
            "Просто возьмите это платье, мне не нужны деньги за него."
            "Это мои принципы, вы понимаете?"
            img 1919
            cashier "Да, я понимаю, конечно."
            "Спасибо, Мэм!"

    $ remove_inventory("shop_dress_eveningdress", 1, True)
    $ clothShopCashierTalkStage = 1
    call refresh_scene_fade()
    music Stealth_Groover
    $ remove_objective("return_dress")
    $ add_objective("return_to_home", _("Ехать домой"), c_green, 20)
    #$ drivingPlacePlannedArray["House"] = "dress_return_drive3"
    $ dressReturnDialoguePlanned = True
    $ returnDressInProgress = False
    return

label dress_return_cashier_talk2:
    if clothShopCashierOffended3ReturnDress == True:
        img 1923
        with fade
    else:
        img 1913
        with fade
    cashier "Мэм."
    "Если передумаете, платье будет ждать Вас!"
    "Я не передумаю!"
    call refresh_scene_fade()
    return

label dress_return_drive3:
    sound snd_car_engine
    imgl 1925
    with fadelong
    m "Фрэд!!!"

    imgr 1910
    fred "Да, Мэм?"

    m "Ты куда меня привез, я спрашиваю еще раз!!!"

    imgl 1926
    m "Тут полно каких-то животных и шлюх!"
    "Знал бы ты через что я прошла, чтобы добраться до магазина!!!"
    fred "Мэм, к сожалению, это наш мир."
    "Он нас окружает."
    "Такого полно вокруг."
    "Сложно где-то остановиться и избежать подобного."

    imgl 1927
    m "Я живу в другом мире, Фрэд!"

    imgl 1928
    "И в этом другом мире нет всех этих нищих!"

    menu:
        "Продолжить ругаться на Фреда.":
            $ fredOffendedDriveReturnDress1 = True
            sound snd_car_engine
            imgl 1929
            with fadelong
            "Это в твоем они есть, Фрэд!"
            call bitch(2, "fredOffendedDriveReturnDress1a")
            "Это ты жалкий болван!"
            imgr 1910
            fred "..."
            imgl 1930
            m "Молчишь."
            "Ах, ты же натренирован в своей психологии."
            "Профессионал..."
            "Ну посмотрим как ты выдержишь!"
            "..."
            m "..."
            imgl 1931
            call bitch(2, "fredOffendedDriveReturnDress1b")
            m "Ты огурец!"
            fred "..."
            imgl 1932
            m "Ты зеленый помидор, раздавленный на дороге!"
            fred "..."
            m "Ты кривая картофелина!"
            fred "..."
            m "У тебя тыква вместо головы!"
            fred "..."

            sound snd_car_engine
            imgl 1933
            with fadelong
            call bitch(2, "fredOffendedDriveReturnDress1c")
            m "У тебя член размером с корнюшон!"
            imgr 1910
            m "..."
            fred "..."
            imgl 1934
            m "Что?"
            "И даже это тебе все-равно?"
            fred "..."
            m "..."
            imgl 1935
            m "Нет, Фрэд."
            "Я думаю мне не нужен такой водитель."
            "Мне с тобой скучно."
            "Давай вези меня быстрее."
            imgr 1936
            w
        "Молча ехать и смотреть инстаграм.":
            pass

    $ miniMapEnabledOnly = ["Street_Yard", "Floor1"]

    $ autorun_to_object("floor1", "quest_house_monica_day2_evening_init")

    return
