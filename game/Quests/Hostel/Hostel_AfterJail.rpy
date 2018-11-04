label hostelAfterJail_dialogue1:
    mt "Фу! Что за место?"
    "Хорошо что мне здесь нужно провести всего одну ночь!"
    "Но даже на это у меня едва хватит сил!"
    return

label hostelAfterJail_dialogue2:
    $ hostelReceptionStage = 0
    mt "Может стоило все-таки остаться там?"
    "Мне больше некуда идти..."
    "А на улице такой ливень!!!"
    return

label hostelAfterJail_Perry_dialogue1:
#                $ cloth_type = "AfterJail"
#                $ cloth = "AfterJail"
#    music Groove2_85
    sound highheels_short_walk
    if cloth_type == "AfterJail":
        img 2930
        with fade
    perry "Девушка!"
    "Вы куда собрались?!"
    "Сначала надо оформиться и заплатить!"
    "А потом уже идти спать!"
    sound highheels_short_walk
    call refresh_scene_fade()
    return


label hostelAfterJail_Perry_dialogue2:
    img 2931
    with fadelong
#    music:_rich_hotel_casual_dialogue
    perry "Здравствуйте, девушка."
    img 2932
    "Как вас зовут?"
    img 2933
    m "Меня зовут Моника Бакфетт."
    img 2934
    perry "Значит Моника."
    img 2935
    m "Не Моника, а Моника Бакфетт!"
    img 2936
    "Миссис Моника Бакфетт!"
    img 2937
    music Power_Bots_Loop
    perry "Слушай, дорогуша."
    "Миссис здесь у нас не останавливаются."
    "Похоже ты ошиблась адресом?"
    img 2938
    "Проваливай отсюда!"

    $ hostelReceptionStage = 1
    call refresh_scene_fade()
    return


label hostelAfterJail_Perry_dialogue3:
    menu:
        "Нем, Мэм. Я не ошиблась...":
            pass
        "Уйти...":
            call refresh_scene_fade()
            return
    img 2939
    with fadelong
    m "Нет, Мэм..."
    img 2940
    perry "Меня зовут Перри!"
    "И не надо мне тут Мэм'кать!"
    music Groove2_85
    img 2941
    m "Хорошо, мэ.. Перри."
    "Я не ошиблась адресом."
    "Мне правда надо остановиться здесь."
    img 2942
    perry "Хорошо, у тебя есть документы?"
    img 2943
    m "Если честно, то есть, но они..."
    img 2944
    perry "Ладно, мне они не нужны."
    img 2945
    "Мне нужны деньги."
    "За ночь с тебя $10."
    img 2946
    music Stealth_Groover
    mt "Ну и дыра!"
    "$10 за ночь!"
    "Моника!"
    "До чего ты докатилась???"
    "Ты же не рассматривала гостиницы дешевле $10.000 за день проживания!"
    "А здесь?"
    "Это во сколько раз дешевле и хуже??"
    "В тысячу раз дешевле..."
    "Но хуже, кажется, в миллион!!!"
    music Groove2_85
    img 2947
    with fadelong
    m "Мэ.. Прошу прощения."
    img 2948
    "Перри. А нельзя получить какую-то скидку?"
    img 2949
    perry "Скидок нет!"
    "Или плати или выметайся!"
    menu:
        "Перри, давай договоримся!":
            pass
        "У меня нет денег...":
            img 2942
            with fadelong
            m "Перри, у меня нет с собой $10."
            "Можно я переночую бесплатно?"
            music Pyro_Flow
            img 2938
            perry "Ну раз у тебя нет денег, тогда проваливай отсюда!"
            call refresh_scene_fade()
            return

    music Stealth_Groover
    img 2950
    with fadelong
    m "Перри."
    "Деньги будут завтра."
    "Завтра я дам тебе $10.000."
    img 2951
    mt "Не откажет же мне Дик в такой мелочи..."
    m "Но сегодня я должна переночевать бесплатно..."
    img 2952
    perry "$10.000?"
    "И какие гарантии?"
    img 2953
    m "Я не знаю."
    "Какие гарантии тебя устроят?"
    music Groove2_85
    img 2954
    perry "Хм..."
    "Что бы с тебя взять-то?"
    "Есть телефон?"
    img 2955
    m "Нет."
    img 2956
    perry "А что есть?"
    img 2957
    m "Ничего нет."
    img 2958
    perry "Ну как ничего?"
    "Смотри какое красивое у тебя платье."
    "Давай его в залог."
    img 2959
    music Power_Bots_Loop
    m "В смысле в залог?"
    "Что ты имеешь ввиду, Перри?"
    img 2960
    perry "Снимай платье и клади в ящик."
    img 2961
    "Как будут деньги завтра, я тебе его отдам."
    img 2962
    m "Но мне будет не выйти на улицу без платья."
    "Как я принесу деньги?"
    img 2963
    perry "Я дам тебе позвонить."
    "Тебя устроит?"
    music Groove2_85
    img 2964
    with fade
    mt "Куда я буду звонить?"
    "Дику?"
    "У меня нет его номера!"
    img 2965
    "Хотя..."
    "Я же могу узнать в справочной его номер."
    "Скорее всего я наткнусь на эту секретаршу, сучку."
    "Но у меня нет другого выхода."
    "Тем более она обещала что предупредит Дика."
    "Я поговорю с ним."
    "Скажу в какую неприятность я попала."
    "Он сразу приедет и решит все проблемы."
    mt "..."
    img 2966
    m "Хорошо."
    "Но мне надо два звонка."
    img 2967
    perry "Хоть три!"
    "Но ты будешь здесь сидеть пока не будет денег, поняла?"
    "И ты в любом случае отдашь эти $10.000."
    "Если не сможешь деньгами, то будешь отрабатывать."
    img 2968
    "Тебе ясно?"
    "Ты согласна?"
    menu:
        "Да. Я согласна...":
            pass
        "Я не собираюсь раздеваться здесь!":
            img 2966
            with fadelong
            m "Я не собираюсь раздеваться здесь, Перри!"
            img 2938
            perry "Ну раз у тебя нет денег, тогда проваливай отсюда!"
            call refresh_scene_fade()
            return

    img 2969
    with fadelong
    m "Да..."
    "Я согласна."
    img 2970
    perry "Тогда снимай платье и клади в ящик."
    img 2971
    with fadelong
    mt "Черт!"
    "У меня же нет трусиков и лифчика!"
    "..."
    music Hidden_Agenda
    img 2972
    with fadelong
    m "Перри."
    "Дело в том что у меня нет белья."
    "Может быть у тебя есть какой-нибудь халат?"
    img 2973
    music Power_Bots_Loop
    perry "Это в La Grand тебе выдают халаты и тапочки."
    "У нас ничего такого нет!"
    "Не нравится - иди ночуй туда!"
    img 2974
    music Hidden_Agenda
    m "Но Перри."
    "Я же буду абсолютно голой..."
    img 2975
    perry "Моника."
    "Здесь всем абсолютно наплевать на это."
    "Здесь люди ходят голые, пьяные, под травкой.. любые."
    "Тем более сейчас никого нет."
    "Только одна посетительница спит."
    img 2976
    "Снимай свое платье и клади в ящик."
    "Или убирайся за дверь."
    img 2977
    m "Хорошо, Перри..."
    img 2978
    mt "У меня нет выхода."
    "Перри сказала там только одна посетительница..."
    "Может быть надо это преодолеть."
    "Последний трудный шаг."
    "Справиться с этим."
    img 2979
    mt "А завтра все наладится и будет как прежде."
    "Я встречусь с Диком."
    "Он мне поможет!"

    img 2980
    "Давай, Моника!"
    "Сделай это!"

    $ remove_objective("go_hostel")
    $ add_objective("put_cloth_to_box", _("Положить платье в коробку"), c_blue, 10)
    call question_helper_enable("question_hostel_perry_dress")
    $ autorun_to_object("hostel_reception", "hostelAfterJail_Perry_dialogue4")
    $ hostelReceptionStage = 2

    $ subst_to_object("Teleport_Hostel_Street", "hostelAfterJail_Perry_dialogue5")
    $ subst_to_object("Teleport_Hostel_Bedroom", "hostelAfterJail_Perry_dialogue6")

    call refresh_scene_fade()
    return

label hostelAfterJail_Perry_dialogue4:
    perry "Положи платье в верхнюю коробку справа от меня."
    return

label hostelAfterJail_Perry_dialogue5(n,d):
    sound highheels_short_walk
    img 2976
    with fade
    perry "Эй! Куда собралась!?"
    "Мы договорились! Быстро клади платье в коробку!!!"
    sound highheels_short_walk
    call refresh_scene_fade()
    return

label hostelAfterJail_Perry_dialogue6(n,d):
    sound highheels_short_walk
    if cloth_type == "AfterJail":
        img 2930
        with fade
    perry "Эй! Куда собралась!?"
    "Мы договорились! Быстро клади платье в коробку!!!"
    sound highheels_short_walk
    call refresh_scene_fade()
    return

label hostelAfterJail_Perry_dialogue7:
    menu:
        "Положить платье в коробку.":
            pass
        "Не класть платье.":
            return
    music Hidden_Agenda
    sound snd_fabric1
    img black_screen
    with fadelong
    $ renpy.pause(2.0)
    img 2981
    with fadelong
    mt "Мне надо очень осторожно передвигаться, чтобы никто не увидел!"
    "Я в таком виде..."
    "Я очень смущаюсь..."

    call question_helper_disable()

    $ cloth = "Nude"
    $ cloth_type = "Nude"

    $ hostelReceptionStage = 3
    $ subst_to_object("Teleport_Hostel_Street", "hostelAfterJail_Perry_dialogue7a")
    $ subst_to_object("Teleport_Hostel_Bedroom", False)

    call refresh_scene_fade()

    return

label hostelAfterJail_Perry_dialogue7a(n,d):
    mt "Я не выйду на улицу в таком виде! Я еще не сошла с ума!"
    return

label hostelAfterJail_Perry_dialogue7b:
    mt "Мне надо очень осторожно передвигаться, чтобы никто не увидел!"
    "Я в таком виде..."
    "Я очень смущаюсь..."
    return

label hostelAfterJail_Perry_dialogue8:
    music Hidden_Agenda
    img 2982
    with fadelong
    perry "Ха, Моника!"
    img 2983
    "Ты выглядишь очень возбуждающе!"
    img 2984
    "У меня даже начинает становиться влажно между ножек!"

    img 2985
    with fadelong
    w
    img 2986
    with fade
    "Не хочешь полизать мою волосатую киску за $30?"
    img 2987
    "В счет твоего долга $10.000?"
    img 2988
    "Останется $9.970."
    img 2989
    "Хорошая экономия!"

    img 2990
    with fade
    w
    img 2991
    with fade
    w
    img 2990
    with fade
    w
    img 2992
    with fade
    w

    $ hostelReceptionStage = 4
    call refresh_scene_fade()
    return

label hostelAfterJail_Perry_dialogue8a:
    menu:
        "Согласиться...":
            mt "Я никогда не соглашусь на такое!!!"
            "НИ-КОГ-ДА!!!"
            return
        "Мэм, Вы в своем уме??":
            pass
    music Power_Bots_Loop
    img 2993
    with fade
    m "Мэм, Вы в своем уме??"
    "Я надеюсь Вы пошутили?"
    img 2994
    "Как Вы можете предлагать мне такие мерзости???"
    "Я порядочная леди!"
    img 2995
    "Я в жизни ничего подобного не делала и, клянусь! не буду делать никогда!!"
    img 2996
    music Hidden_Agenda
    perry "Хорошо."
    img 2997
    "$30..."
    img 2998
    "И плюс еще день бесплатного проживания."
    img 2999
    "Да, и называй меня Перри, а не Мэм!"
    img 3000
    music Pyro_Flow
    m "Иди ты в жопу, Перри!!"
    img 3001
    "Куда тут идти чтобы поспать???"
    img 3002
    perry "Ха-ха!"
    "Иди по коридору, Моника!"
    "И повиляй покрасивее попой!"
    img 3003
    mt "!!!!!!!"

    $ remove_objective("put_cloth_to_box")
    $ add_objective("go_sleep", _("Принять душ и лечь спать"), c_orange, 10)

    $ hostelReceptionStage = 5
    $ autorun_to_object("hostel_bedroom", "hostelAfterJail_bedroom_dialogue1")
    $ autorun_to_object("hostel_bedroom2", "hostelAfterJail_bedroom_dialogue2")
    music Groover2_85
    call refresh_scene_fade()
    return

label hostelAfterJail_Perry_dialogue8b:
    img 2989
    with fadelong
    perry "Моника, подожди!"
    img 2991
    m "Я жду ответа!"
    img 2992
    w
    call refresh_scene_fade()
    return

label hostelAfterJail_Perry_dialogue9:
    music Hidden_Agenda
    img 3004
    with fadelong
    perry "Мне нравится как ты виляешь попой!"
    "Я же вижу ты стараешься понравиться мне!"
    img 3005
    "Может быть ты передумала?"
    img 3006
    m "По поводу чего я передумала??"
    img 3007
    perry "По поводу того чтобы полизать мне киску."

    img 3008
    w
    img 3009
    with fade
    w
    music Pyro_Flow
    img 3010
    m "Иди в жопу!!!"
    return

label hostelAfterJail_bedroom_dialogue1:
    $ hostelReceptionStage = 6
    mt "ГОСПОДИ! ЧТО ЭТО???"
    "И ЭТО НАЗЫВАЕТСЯ ОТЕЛЬ?!?!?"
    "Это какое-то место для бездомных!!!"
    "..."
    "Но, по крайней мере, это крыша над головой."
    "Я слышу как на улице идет дождь."
    "Не представляю как бы я была сейчас там!!!"

    $ autorun_to_object("hostel_bathroom", "hostelAfterJail_bathroom_dialogue1")
    return

label hostelAfterJail_bedroom_dialogue2:
    img 5629
    with fadelong
    mt "Что это?"
    "Это какие-то тряпки."
    "Похожи на те что носят те шлюхи, мимо которых я проходила."
    img 5628
    "А в кровати, похоже, одна из них."
    "Фу!"
    "Как противно!"
    "Не понимаю, как можно в таком ходить!"
    "Никакого уважения к себе!"
    "И мне придется спать рядом с этим животным!"
    mt "Ой, Моника! Забудь это слово!"
    call refresh_scene_fade()
    return

label hostelAfterJail_bathroom_dialogue1:
    mt "Какое жуткое место!"
    "Мне неуютно чувствовать себя без одежды."
    "Но эта ненормальная Перри была права."
    "В этом вонючем хостеле почти никого нет."
    return

label hostelAfterJail_bathroom_dialogue2:
    if hostelBathroomStage == 0:
        if hostelBathTaken == True:
            mt "Я уже принимала душ."
            "Если я сделаю это еще раз, боюсь, он сломается!"
            return
        img 5633
        with fadelong
        mt "А вот и душ."
        sound snd_water_hose
        img 5634
        with fadelong
        mt "Как же хорошо!"
        "Я даже на минуту забыла про свои проблемы..."
        "Осталось лечь спать."
        "До следующего дня осталось несколько минут..."
        "Завтра я встану и все станет как прежде..."

        $ hostelBathTaken = True
        call refresh_scene_fade()

    if hostelBathroomStage == 1:
        img 3013
        with fadelong
        mt "А вот и душ."

        sound snd_walk_barefoot
        img 3015
        with fadelong
        mt "Душ...."
        sound snd_walk_barefoot
        img 3014
        with fadelong
        "Как же хорошо..."
        "Теплая вода..."
        "А не ледяная с дождем..."
        "Мммм..."
        "Я королева..."
        "Королева..."
        "..."
        "...."
        img black_screen
        with Dissolve(1)
        $ renpy.pause(2.0)
        img 3014
        with fadelong
        mt "Мне кажется я так замечталась что даже на минуту уснула под душем!"
        img 3016
        with fade
        mt "Надо скорее выходить и звонить Дику!"
        img 3017
        with fade
        mt "Пора заканчивать это Цирк, который последнее время меня окружает!"
        img 3018
        music Gearhead
        mt "!!!!!!!!!"
        img 3019
        "О БОЖЕ!!!"
        img 3020
        "КТО ВЫ????"
        sound snd_woman_scream1
        mt "АААААААААААААААА!!!!"
        $ autorun_to_object("hostel_bedroom", "hostelAfterJail_bedroom_dialogue4")
        $ hostelBedroomStage = 2
        call change_scene("hostel_bedroom", "Fade", "snd_walk_barefoot")

    return

label hostelAfterJail_bedroom_sleep1:
    menu:
        "Лечь спать":
            pass
        "Не ложиться":
            call refresh_scene_fade()
            return
    img 5630
    with fadelong
    mt "Какой ужас!"
    "Но я не могу уже ни о чем думать..."
    mt "Я хочу спать!"
    "Поскорее бы завтра!"

    call clothShopTraderScene1()

    scene black_screen
    with Dissolve(1)
    stop music fadeout 1.0
    call textonblack_long("УТРО")
    scene black_screen
    with Dissolve(1)
    $ changeDayTime("day")

    music Cheery_Monday
    $ hostelBathroomPissed = False
    $ hostelBathroomStage = 1
    $ hostelBedroomStage = 1
    $ hostelBathTaken = False
    $ remove_objective("go_sleep")
    $ remove_objective("dick_tomorrow1")
    $ add_objective("go_dick", _("Идти к Дику!"), c_blue, 6)
    $ add_objective("go_bath_call_dick", _("Принять душ и позвонить Дику"), c_green, 10)

    $ autorun_to_object("hostel_bedroom", "hostelAfterJail_bedroom_dialogue3")

    call refresh_scene_fade()

    return

label hostelAfterJail_bedroom_dialogue3:
    mt "Ура! Утро!!!"
    #render+
    #Моника рассуждает с утра в хостеле
#    imgl Dial_begin34_1
    img 5660
    with fadelong
    mt "Я смотрю эта шлюха все так и спит."
    "Бесполезное создание..."
    "Я надеялась что она встанет раньше меня и исчезнет, чтобы не смущать мой взгляд своим жутким видом."
    "И своими жуткими лохмотьями."
    "..."
    img 5661
#    imgl Dial_begin34_4
    mt "Моника!"
    "Выше нос!"
    "Все!"
    "Ты отмучалась!"
    "Сейчас ты позвонишь Дику и все закончится!"
    img 5662
#    imgl Dial_begin34_5
    mt "Надо идти принять душ."
    "Все-таки перед Диком надо выглядеть на все 100!"
    "Хоть он и хомячок, тюфяк, но вокруг него вьются разные давалки."
    "Такие как та секретарша."
    img 5663
#    imgl Dial_begin34_6
    mt "Ей, конечно, не сравниться со мной, но все-же."

    call refresh_scene_fade()

    return

label hostelAfterJail_bedroom_dialogue4:
    sound snd_woman_scream1
    mt "АААААААААААААААА!!!!"
    return

label hostelAfterJail_bedroom_dialogue5:
    sound snd_bodyfall
    img 5626
    with fade
    $ autorun_to_object("hostel_bedroom3", "hostelAfterJail_bedroom_dialogue6")
    call change_scene("hostel_bedroom3", "Fade", False)
    return

label hostelAfterJail_bedroom_dialogue6:
    mt "Что это???"
    "Тряпки?"
    "Надо схватить хоть что-нибудь!!!"
    return

label hostelAfterJail_bedroom_dialogue7:
    img 5635
    w
    sound snd_fabric1
    img 5636
    with fadelong
    w
    img 5637
    with fade
    sound snd_woman_scream1
    mt "АААААААААААААААА!!!!"
    img 3021
    perry "СТОЯТЬ!!!"
    "КУДА СОБРАЛАСЬ!!!"
    img 3022
    "ГОНИ $10.000!!!"
    "ИЛИ Я ВЫЗОВУ БАНДИТОВ!!!"

    $ rain = True
    $ rainIntencity = 3
    $ lightning = False

    $ gameStage = 3
    $ gameSubStage = 0

    $ subst_to_object("Teleport_Hostel_Street", False)
    $ autorun_to_object("hostel_street", "hostelAfterJail_street_dialogue1")
    call change_scene("hostel_street", "Fade", "snd_walk_barefoot")
    return

label hostelAfterJail_street_dialogue0:
    mt "Я абсолютно голая!"
    "На улице!"
    mt "О НЕТ!"
    return

label hostelAfterJail_street_dialogue1:
    #render+
    #Моника на улице возле хостела
    music Power_Bots_Loop
    img 5664
#    imgl Dial_begin34_7
    mt "О БОЖЕ!!!"
    "СКОЛЬКО ИХ БЫЛО???"
    "ЧТО БЫ ОНИ СО МНОЙ СДЕЛАЛИ???"
    "..."
    "..."
    img 5665
#    imgl Dial_begin34_8
    mt "Я абсолютно голая!"
    "На улице!"
    "..."

    img 5666
#    imgl Dial_begin34_9
#    mt "Что это у меня в руках?"
    mt "Что это выпало у меня из рук?"
    "Это тряпки той шлюхи?"
#    imgl Dial_begin34_10
    mt "О НЕТ!"
    "НО ЧТО МНЕ ДЕЛАТЬ???"
    "У МЕНЯ ВЫБОР!"
    "БЕЖАТЬ ПО УЛИЦЕ ГОЛОЙ ИЛИ НАДЕТЬ ЭТО!!!"
    img 5667
#    imgl Dial_begin34_11
    mt "Я одену это, буквально на 10 минут, пока не найду что-то другое!"
    "..."
    img 5668
#    imgl Dial_begin34_12
    if hostel_edge_1_a_visited == True:
        mt "Здесь за углом был переулок тупик."
        "Там никого нет!"
        "Надо бежать туда!"
    else:
        mt "Надо где-то укрыться!"
        "Здесь за дом ведет какая-то дорога!"
        "Надо бежать туда!"

    $ remove_objective("go_bath_call_dick")
    $ subst_to_object("Teleport_Shawarma", "hostelAfterJail_street_dialogue2")
    $ add_objective("find_place_to_take_cloth", _("Найти место где можно одеться!"), c_red, 10)
    call refresh_scene_fade()
    return

label hostelAfterJail_street_dialogue2(o, d):

    menu:
        "Переодеться за углом шавермы.":
            pass
        "Найти другое место...":
            return

#    /Все, я на месте. Мне надо переодеться
    img 3023
    with fadelong
    mt "Надо как-то надеть эти тряпки!"
    "Где тут верх? Где низ?"
    "Моника, быстрее!"
    "Тебя могут увидеть!"
    img 3024
    "ГОЛОЙ!!!"
    sound snd_fabric1
    img black_screen
    with Dissolve(1)
    $ renpy.pause(1.0)

    img 3025
    with fadelong
    "Моника!"
    "Что это за наряд!"
    "Я почти голая!"
    "Это так вульгарно!"
    img 3026
    "Как так получилось что ты одета в это?"
    "Как все могло докатиться до такого?"
    img 3027
    "Моника!"
    "Что с тобой!"
    "Ты же умная!"
    img 3028
    "Не может это все так долго продолжаться!"
    "..."
    "..."
    img 3029
    "Успокойся."
    "Дыши ровно..."
    "Сейчас ты быстренько пробежишь мимо всех."
    "Так, чтобы тебя не заметили."
    img 3030
    "Затем ты пойдешь в магазин одежды и украдешь себе нормальное платье!"
    img 3028
    "НОРМАЛЬНОЕ!!!"
    "А НЕ ЭТО НЕПОТРЕБСТВО!!!"
    img 3031
    "Сколько туда идти?"
    "Он находится буквально за углом."
    "Всего-лишь пару сотен метров..."
    "Пару сотен метров такого позора..."
    img 3032
    "Одетой в ЭТО..."
    "О БОЖЕ!"
    "..."
    img 3033
    "Моника!"
    "Ты справишься!"
    "Ты умная, сильная, красивая и независимая женщина!"
    "Тебе по плечу любые трудности!"
    img 3034
    "Вспомни!"
    "Чем ты отличаешься от той же Юлии?"
    "Она - это низы, которые ничего не умеют."
    img 3035
    "А я - Леди!"
    img 3036
    "Я Леди!"
    "Я справлюсь со всем!"
    $ splay("snd_light_rain", "rain", loop=True)
    "Я достойна лучшего!"

    $ rainIntencity = 1
    hide screen rain
#    $ renpy.music.stop("rain")
    $ remove_objective("find_place_to_take_cloth")
    $ subst_to_object("Teleport_Shawarma", "hostelAfterJail_street_dialogue2")
    $ autorun_to_object("whores_place_shawarma_s2", "hostelAfterJail_street_dialogue5")
    $ autorun_to_object("hostel_street", "hostelAfterJail_street_dialogue4a")
    $ add_objective("steal_cloth", _("Украсть в магазине одежды новое платье!"), c_blue, 10)
    $ map_enabled = False

    $ subst_to_object("Teleport_Shawarma", False)
    $ gameSubStage = 1
    $ cloth = "Whore"
    $ cloth_type = "Whore"
    call refresh_scene_fade()
    return

label hostelAfterJail_street_dialogue3:
    imgc inv_monica_whore
    "Мне..."
    "Очень стыдно..."
    "Носить это..."
    imgc inv_monica_whore2
    "Надо скорее что-то придумать..."
    "Я сгораю от стыда!!"

    return

label hostelAfterJail_street_dialogue4:

    menu:
        "Одеть наряд шлюхи.":
            pass
        "Уйти.":
            return

#    /Все, я на месте. Мне надо переодеться

    #render+
    #Моника одевается в Hostel_Edge_a
    img 5669
#    img 3023
    with fadelong
    mt "Надо как-то надеть эти тряпки!"
    "Где тут верх? Где низ?"
    "Моника, быстрее!"
    "Тебя могут увидеть!"
    img 5670
#    img 3024
    "ГОЛОЙ!!!"
    sound snd_fabric1
    img black_screen
    with Dissolve(1)
    $ renpy.pause(1.0)

    img 5671
#    img 3025
    with fadelong
    "Моника!"
    "Что это за наряд!"
    "Я почти голая!"
    "Это так вульгарно!"
    img 5672
#    img 3026
    "Как так получилось что ты одета в это?"
    "Как все могло докатиться до такого?"
    img 5673
#    img 3027
    "Моника!"
    "Что с тобой!"
    "Ты же умная!"
    #до этого переделать
    img 5674
#    img 3028
    "Не может это все так долго продолжаться!"
    "..."
    "..."
    img 5675
#    img 3029
    "Успокойся."
    "Дыши ровно..."
    "Сейчас ты быстренько пробежишь мимо всех."
    "Так, чтобы тебя не заметили."
    img 5676
#    img 3030
    "Затем ты пойдешь в магазин одежды и украдешь себе нормальное платье!"
    img 5674
#    img 3028
    "НОРМАЛЬНОЕ!!!"
    "А НЕ ЭТО НЕПОТРЕБСТВО!!!"
    img 5677
#    img 3031
    "Сколько туда идти?"
    "Он находится буквально за углом."
    "Всего-лишь пару сотен метров..."
    "Пару сотен метров такого позора..."
    img 5678
#    img 3032
    "Одетой в ЭТО..."
    "О БОЖЕ!"
    "..."
    img 5679
#    img 3033
    "Моника!"
    "Ты справишься!"
    "Ты умная, сильная, красивая и независимая женщина!"
    "Тебе по плечу любые трудности!"
    img 5680
#    img 3034
    "Вспомни!"
    "Чем ты отличаешься от той же Юлии?"
    "Она - это низы, которые ничего не умеют."
    img 5681
#    img 3035
    "А я - Леди!"
    img 5682
#    img 3036
    "Я Леди!"
    "Я справлюсь со всем!"
    $ splay("snd_light_rain", "rain", loop=True)
    "Я достойна лучшего!"

    $ rainIntencity = 1
    hide screen rain
#    $ renpy.music.stop("rain")
    $ remove_objective("find_place_to_take_cloth")
    $ subst_to_object("Teleport_Shawarma", "hostelAfterJail_street_dialogue2")
    $ autorun_to_object("whores_place_shawarma_s2", "hostelAfterJail_street_dialogue5")
    $ autorun_to_object("hostel_edge_1_a", "hostelAfterJail_street_dialogue4a")
    $ add_objective("steal_cloth", _("Украсть в магазине одежды новое платье!"), c_blue, 10)
    $ map_enabled = False

    $ subst_to_object("Teleport_Shawarma", False)
    $ gameSubStage = 1
    $ cloth = "Whore"
    $ cloth_type = "Whore"
    call change_scene("hostel_edge_1_a", "Fade_long", False)
    return

label hostelAfterJail_street_dialogue4a:
    mt "Кажется дождь немного стих..."
    return

label hostelAfterJail_street_dialogue5:
#    hide screen Rain
#    $ renpy.music.stop("rain")
    $ renpy.music.set_pause(True, "rain")
    music DarxieLand
    img 3037
    with fadelong
    shawarma "О!"
    "Мадаме!"
    "Вы все-таки решили расстаться с Вашим платьем?"
    "А мне оно так нравилось!"
    img 3038
    m "Иди в жопу!!!"
    img 3039
    shawarma "Мадаме!"
    "Все еще смею робко надеяться на Ваш поцелуй!"
    "По Французски...!"
    img 3040
    m "!!!!!!!!!!"
    $ renpy.music.set_pause(False, "rain")
    $ autorun_to_object("whores_place_s2", "hostelAfterJail_street_dialogue6")
    $ autorun_to_object("street_cloth_shop_s2", "hostelAfterJail_street_dialogue7")
    call change_scene("whores_place")
    return

label hostelAfterJail_street_dialogue6:
    mt "Дьявол!"
    "Я побежала не в ту сторону!"
    "Мне надо идти назад!"
    if shawarmaTraderOffended1 == True:
        mt "И я не собираюсь разговаривать с этим животным!"
    else:
        mt "И я не собираюсь разговаривать с этим продавцом!"

    return

label hostelAfterJail_street_dialogue7:
    #render+
    #Моника рассуждает у магазина
    $ renpy.music.set_pause(True, "rain")
    music Groove2_85
    img 5683
#    imgl Dial_begin35_1
    mt "..."
    "Я почти добралась!"
    img 5684
#    imgl Dial_begin35_2
    mt "Сейчас надо осторожно проникнуть в магазин, чтобы меня никто там не видел."
    "Даже покупатели не поверят что девушка в такой одежде как я собирается что-то покупать."
    "А не украсть..."
    $ renpy.music.set_pause(False, "rain")
    call refresh_scene_fade()
    return

label hostelAfterJail_street_dialogue8:
    hide screen Rain
    sound highheels_short_walk
    music Power_Bots_Loop
    img 3041
    with fadelong
    mt "О Боже!"
    img 3042
    "Сколько здесь посетителей!!!"
    "Мне никогда отсюда ничего не взять!"
    img 3043
    "Мне надо скорее убираться отсюда, пока меня не заметили!"
    "Они сразу позовут эту продавщицу."
    "Увидев меня в таком виде, она сразу вызовет полицию."
    img 3044
    "Моника! Беги!!"

    #render+
    #рассуждает у магазина на выходе
    sound highheels_short_walk
    show screen Rain
    $ renpy.music.set_pause(True, "rain")

    img 5685
#    imgl Dial_begin35_3
    with fadelong
    music Groove2_85
    mt "Я не знаю что мне делать..."
    "Это единственное место где я могла взять одежду..."

    img 5686
#    imgl Dial_begin35_4
    "Может пойти в хостел, попросить Перри дать мне мое платье?"
    "Что-нибудь придумать для нее?"
    "..."

    img 5687
#    imgl Dial_begin35_5
    "Нет. Эта извращенка наверняка что-нибудь потребует от меня взамен."
    "Еще она угрожала мне бандитами."
    "И я ей должна $10.000."
    img 5688
#    imgl Dial_begin35_6
    mt "Мне кажется она меня уже не выпустит."
    "Так что не стоит туда идти."
    "..."
    img 5689
#    imgl Dial_begin35_7
    mt "Дик."
    "Мне не хочется появляться перед ним в таком виде, но..."
    music Pyro_Flow
    mt "Вообще-то это его вина, что я оказалась в таком положении."
    "Это ему не найти время на меня!"

    img 5690
#    imgl Dial_begin35_8
    mt "Жалкий тюфяк!"
    "Я ему устрою за все!"
    "Я пойду к нему в таком виде."
    img 5691
#    imgl Dial_begin35_9
    mt "И пусть видит к чему привело то что он не нашел вчера на меня время!"
    "Совсем не заботится обо мне!"
    "И на что он еще смеет рассчитывать при этом?"
    img 5692
#    imgl Dial_begin35_10
    mt "Фи!"

    $ autorun_to_object("gas_station_view1_s2", False)

    $ remove_objective("steal_cloth")
#    $ add_objective("steal_cloth", _("Украсть в магазине одежды новое платье!"), c_blue, 10)
    $ autorun_to_object("street_dick_office", "hostelAfterJail_street_dialogue10")
    $ dickReceptionStage = 5
    $ teleportDickOfficeHeavyRainFlag = True
    $ teleportDickOfficeEveningFlag = False
    $ gameSubStage = 2
    $ map_enabled = True
    $ renpy.music.set_pause(False, "rain")
    call refresh_scene_fade()
    return

label hostelAfterJail_street_dialogue9:
    mt "Я не пойду в этот магазин. Там слишком опасно!"
    return

label hostelAfterJail_street_dialogue10:
    mt "Дождь снова усилился."
    "Надо быстрее идти к Дику и закончить с этим!"
    "Сколько уже можно мокнуть!!!"
    "Я - Моника Бакфетт!!!"
    "И я по определению не могу мокнуть под дождем!!! И точка!!!"
    return
