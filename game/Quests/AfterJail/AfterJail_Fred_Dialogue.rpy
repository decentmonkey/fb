label afterJailFredDialogue:
    $ renpy.pause(2.0)

    imgl Dial_Begin35_11
    with Dissolve(0.5)
    mt "Мне конец..."
    #debug
#    jump test_label1
    "Где я буду сегодня ночевать?"
    "(хмык)"
    "Что я буду есть?"
    "(хмык)"
    "Все места, которые я знаю, уже невозможны."
    "(хмык)"
    imgl Dial_Begin35_12
    mt "Снова спрашивать людей?"
    "(хмык)"
    "В таком виде?"
    "(хмык)"
    "Девушке в таком виде сразу подскажут где ей ночевать и как зарабатывать..."
    "(хмык)"
    imgl Dial_Begin35_11
    mt "Сегодня вечером или завтра с утра я уже буду в руках у Маркуса."
    "У меня нет никаких шансов, как он и говорил..."
    "..."
    "...."

    $ renpy.music.set_pause(True, "rain")
    music Hidden_Agenda
    imgl Dial_Begin35_13
    mt "Кто это?"
    "Это Фред?"
    "Этот никчемный водитель..."
    imgl Dial_Begin35_14
    mt "Фред!!!"
    "ФРЕД!!!"
    $ renpy.music.set_pause(False, "rain")

    $ add_objective("come_to_fred", _("Подойти к Фреду"), c_blue, 10)


    return

label afterJailFredDialogue2:
    $ renpy.music.set_pause(True, "rain")
    $ rain = False
    music Groove2_85
    imgr Driver_Stand
    fred "Добрый день, Миссис Бакфетт!"
    imgl Dial_Begin35_15
    m "Добрый день... Фред."
    "Хорошо что ты здесь."
    "Быстрее открывай дверь и поехали!"
    "Мне надо торопиться в одно место!"
    fred "Миссис Бакфетт."
    "Сожалею."
    "Но у меня сейчас другой Босс."
    "И мне запрещено общаться с Вами."
    imgl Dial_Begin35_16
    m "Я знаю это, Фред!"
    "..."
    "Фред!"
    "У меня все хорошо."
    "Есть небольшие проблемы, но я их быстро улажу."
    "Как ты думаешь, кто будет твоим Боссом после этого?"
    "А, Фред?"
    if fredFirePlanned == True:
        fred "Но Мэм."
        "Вы собирались уволить меня."
        imgl Dial_Begin35_17
        m "Я собиралась кинуть монетку!"
        fred "..."
        m "..."
        imgl Dial_Begin35_18
        m "Я бы не уволила тебя, Фред."
        "Я же просто играла..."
    fred "Мэм."
    "Я в курсе Ваших проблем."
    "Конечно же Вы скоро их решите."
    "И Вам не помешает то что у Вас нет денег."
    "И нет больше никаких документов."
    "Вы ведь, наверняка, даже не знаете где сегодня ночевать."
    "Так ведь, Мэм?"
    "Я могу помочь Вам."
    imgl Dial_Begin35_19
    m "Фред."
    "Это все неправда."
    "Кто тебе наговорил таких глупостей?"
    mt "(хмык)"
    fred "Ну раз неправда, то желаю Вам удачи, Мэм!"
    "Когда-нибудь еще увидимся!"
    "До свидания!"
    imgl Dial_Begin35_20
    m "Стой, Фред!"
    "Погоди."
    "Это, конечно, неправда, про мои проблемы."
    "Но мне интересно как же ты собирался мне помочь?"
    fred "Садитесь в машину, Мэм."
    "Можем там поговорить."
    m "Хорошо, Фред."
    imgl Dial_Begin35_21
    "..."
    "...."
    fred "..."
    m "..."
    fred "..."
    imgl Dial_Begin35_22
    m "Ты собираешься открывать дверь для меня, Фред?"
    fred "Мэм, это не входит в мои обязанности."
    "И садитесь, пожалуйста, вперед."
    "Вы можете испачкать своей одеждой салон сзади."
    "И у меня будут неприятности с Боссом."
    imgl Dial_Begin35_23
    m "...."
    mt "!!!!!!!!"
    imgl Dial_Begin35_24
    mt "Сволочь!!!"
    img black_screen
    with Dissolve(0.5)
    $ rain = False
    $ rainIntencity = 0
    hide screen rain
    sound snd_car_door
    $ renpy.pause(1.0)
    music snd_moderate_rain_music

    img 3219
    with fadelong
    hide screen rain
    fred "Мэм."
    "Я перейду сразу к делу."
    "Вы знаете что у Вашего дома теперь новые хозяева?"
    img 3221
    m "Я знаю..."
    img 3220
    fred "Я общался с новым хозяином."
    "Дом большой."
    "Поэтому они ищут домработницу."
    if juliaFirePlanned == True and juliaFireCancelled == False:
        "До этого там работала какая-то девушка, но ее кто-то уволил."
    else:
        "До этого там работала какая-то девушка, но она перешла в другое место работы."

    "Так вот."
    "Я общался с хозяином и договорился о том что девушка без документов будет у них жить и убирать дом."
    "..."
    "Но за бесплатно."
    music Pyro_Flow
    img 3222
    with hpunch
    m "Как это за бесплатно???"
    img 3223
    music snd_moderate_rain_music
    fred "Я договорился только на таких условиях."
    "По другому никак."
    "Если Вам интересно, то мы можем поехать туда, так как мне пора."
    "По дороге я Вам все расскажу."
    img 3224
    m "А если меня не устроит?"
    img 3225
    fred "Тогда считайте что я Вас бесплатно прокатил."
    "Но мне правда пора ехать."
    "Если не хотите, мы можем закончить этот разговор."
    img 3226
    m "..."
    img 3227
    "Хорошо, давай поедем."
    "Мне интересно от тебя услышать что там за новый хозяин."
    fred "Хорошо, Мэм."

    label test_label1:

    $ focus_map("Teleport_House", "afterJailFredDialogue_discardlocation")
    $ streetDickOfficeStage = 2
    $ teleportHomeFredBlowjobFlag = True
    $ bFredFollowingMonica = True
    $ enterCarScene = False
    $ map_enabled = True
    $ map_hud_preset_current = "map_locked"

    call map_show(True)
    return

label afterJailFredDialogue_discardlocation(o,d):
    fred "Мы едем к дому или Вы можете быть свободны."
    return

label afterJailFredDialogue3:
    img black_screen
    with Dissolve(0.5)
    sound snd_car_turn_on
    $ renpy.pause(2)
    sound snd_car_engine
    $ renpy.pause(0.5)

    $ renpy.music.stop("rain")
    music snd_moderate_rain_music
    img scene_Map
    show screen Rain_overlay
    imgr 3230
    $ rain = False
    $ rainIntencity = 3
    with fadelong
    m "Фрэд, так что там за урод, который теперь живет в моем доме?"

    imgl 3229
    fred "Там теперь живет Мистер Робертс, Мэм."
    "Возможно Вы его заочно знаете."
    "Он работал младшим менеджером в дочерней компании Стива, в другом городе, провинциальном."
    "Его повысили после Вашего ухода."
    "И теперь он живет здесь."
    "Он только переехал."
    "Со своей семьей."
    imgr 3231
    music Pyro_Flow
    m "Я помню его."
    "Я видела его отчеты."
    "Ни на что неспособное мелкое ничтожество."
    "!!!!!!!!!!!"
    imgr 3232
    music snd_moderate_rain_music
    imgl 3228
    fred "Он Вас лично не знает, Мэм."
    "Поэтому не советую называть свою фамилию."
    "Если новые хозяева узнают кто Вы, то они не дадут Вам работы."
    imgr 3231
    music Pyro_Flow
    m "За бесплатно???"
    "Я еще должна к этому сремиться???"
    "Стремиться работать у какого-то мелкого менеджера, такого муравья, которого я даже не замечала!"
    "Да еще и без денег!"

    music snd_moderate_rain_music
    fred "Мэм."
    "Вы получите самое главное."
    m "Что это?"
    fred "Вы получите крышу над головой, Мэм."
    "И Вам не придется спать на улице."
    "А Вы знаете, это опасно."
    imgl 3229
    w
    imgr 3232
    mt "!!!!!!!!!!!!!!!!"
    "(хмык)"
    "...."
    m "И что мне там придется делать?"
    fred "Я не знаю, Мэм."
    "У меня никогда не было гувернантки."
    "Наверное убирать дом и делать что скажут."
    "В Ваших интересах во всем выполнять приказы хозяев."
    "Иначе Вы можете лишиться крыши над головой."
    mt "!!!!!!!!!!!!"
    fred "Вы слышите меня, Мэм?"
    m "Да, я слышу, Фред..."

    stop music fadeout 1.0
    img black_screen
    hide screen Rain_overlay
    with Dissolve(0.5)
    sound snd_car_engine
    $ renpy.pause(2.0)
    music snd_moderate_rain_music
    img scene_Map
    show screen Rain_overlay
    imgl 3229
    with fadelong
    fred "Мистер Робертс живет со своей супругой. Миссис Робертс."
    imgr 3232
    m "А имя есть у супруги?"
    fred "Ее зовут Бетти, Мэм."
    "Но я советую обращаться к ней соответствующим образом."
    mt "!!!!!!!!!!!!"
    imgl 3228
    fred "Так же с ними живет сын Мистера Робертса."
    "Барди."
    "Он не в ладах с Миссис Робертс, потому что это не его родная мать."
    "Вам надо учитывать это."
    "Вам надо вписаться в их семью, принять их правила."
    "Чтобы остаться там жить."
    music Power_Bots_Loop
    hide screen Rain_overlay
    img 3233
    with hpunch
    mt "СОБЛЮДАТЬ ПРАВИЛА, ЧТОБЫ ОСТАТЬСЯ ЖИТЬ!"
    "В СВОЕМ ЖЕ ДОМЕ!!!"
    "О БОЖЕ!!!"


    stop music fadeout 1.0
    img black_screen
    hide screen Rain_overlay
    with Dissolve(0.5)
    sound snd_car_engine
    $ renpy.pause(2.0)
#    music snd_moderate_rain_music
    img 3234
    music Groove2_85
    m "Фред."
    "Куда ты меня привез?"
    "Я думала мы едем к дому?"
    "Ты же торопился."
    img 3235
    fred "Да, Миссис Бакфетт."
    "Мы правда туда едем."
    "Мы остановились всего на несколько минут."
    img 3236
    m "Зачем, Фред?.."
    fred "Понимаете, Миссис Бакфетт..."
    "Я потратил много усилий и времени чтобы помочь Вам."
    m "И что?"
    fred "И мне надо что-то взамен."
    img 3237
    m "Я позднее распоряжусь выдать тебе чаевые, Фред."
    fred "Большое спасибо заранее, Миссис Бакфетт."
    "Но мне нужно что-то сейчас..."
    img 3238
    m "Что же ты хочешь сейчас?"
    fred "Ничего особенного, Миссис Бакфетт."
    "Никто никого ни к чему не принуждает."
    "Вы вольны делать все что захотите."
    img 3239
    "..."
    "Просто поцелуйте мой член."
    music Pyro_Flow
    img 3240
    with hpunch
    m "ЧТООО!?!?!?"
    "КАК ТЫ ТАКОЕ МОЖЕШЬ ГОВОРИТЬ, ФРЕД????"
    img 3241
    fred "Мэм."
    "Если Вы не хотите, то можете этого не делать."
    "Как я говорил, никто никого не заставляет."
    img 3242
    m "Конечно же я не хочу, Фред!"
    "И не буду!!!"

    stop music fadeout 1.0
    img black_screen
    hide screen Rain_overlay
    with Dissolve(0.5)
    sound snd_car_door
    $ renpy.pause(1.0)

    img 3243
    with fadelong
    music Power_Bots_Loop
    m "Зачем ты смотришь на дверь, Фред?"
    fred "Мэм."
    "Наша встреча закончена."
    img 3244
    m "Как же так, Фред?"
    "А как же дом?"
    "Как же работа, которую ты предлагаешь?"
    img 3245
    fred "Никто никого не заставляет, Мэм."
    "Я не заставляю Вас."
    "Вы не заставляете меня Вам помогать."
    m "Это шантаж, Фред?!"
    fred "Нет, Мэм."
    "При шантаже Ваши условия ухудшаются если Вы не выполните требование."
    "Здесь-же, все остаются при своих."
    "Я без поцелуя на члене."
    "Вы без крыши над головой."
    "Все просто."
    "..."
    img 3246
    with fade
    fred "Мэм."
    "Попрошу Вас выйти, я тороплюсь!"
    img 3247
    mt "ЧТО ЖЕ МНЕ ДЕЛАТЬ???"
    "НА УЛИЦЕ СНОВА ДОЖДЬ!!!"
    "МНЕ ПРИДЕТСЯ ВЕСЬ ДЕНЬ ХОДИТЬ ПОД НИМ."
    "ИСКАТЬ КУДА ПРИЮТИТЬСЯ НА НОЧЬ!"
    img 3248
    mt "БОЛЬШЕ ВСЕГО Я БОЮСЬ ЧТО НЕ НАЙДУ ГДЕ ПЕРЕНОЧЕВАТЬ!"
    "У МЕНЯ ПРЕДЧУВСТВИЕ ЧТО ТАК И БУДЕТ!"
    img 3249
    mt "Этот Фред."
    "Извращенец."
    "Он хочет чтобы я поцеловала его грязный вонючий отросток..."
    img 3250
    mt "А Я НЕ ХОЧУ!!!"
    "..."
    music Groove2_85
    img 3253
    fred "Мэм."
    "Пожалуйста, выходите скорее."

    m "Фред.."
    "Это твое окончательное решение?"
    fred "Если Вы измение свое, то и я тоже."
    label afterJailFredDialogue3_menu_loop1:
        img 3250
        menu:
            "Я не хочу и не буду делать этого, Фред!":
                m "Я не хочу и не буду делать этого, Фред!"
                img 3246
                fred "Мэм."
                "Попрошу Вас выйти, я тороплюсь!"
                mt "О БОЖЕ!!!"
                jump afterJailFredDialogue3_menu_loop1
            "Фред, я никогда не делала этого...":
                pass

    img 3254
    m "Фред, я никогда не делала этого..."
    fred "Вы никогда не целовали член мужчины???"
    "А муж??"
    img 3255
    m "Мы..."
    "Мы с ним занимались этим всего пару раз."
    "И это было без таких извращений..."
    img 3256
    fred "Вам это не нравится, Миссис Бакфетт?"
    img 3257
    m "Я не люблю секс, Фред."
    "Я не понимаю что в нем такого."
    "Это вы мужчины любите его."
    img 3258
    fred "Хорошо, я Вам покажу."
    "Это просто, Миссис Бакфетт."
    "Расстегните мне ширинку."
    img 3259
    m "..."
    img 3260
    fred "..."
    img 3261
    w
    img 3262
    "Вот так."

    img 3263
    mt "БОЖЕ!!!"
    img 5895
#    img 3264
    "КАК ПРОТИВНО!!!"
    img 5896
#    img 3265
    m "Что дальше?"
    img 5897
#    img 3266
    fred "Возьмите его в вашу ручку, Миссис Бакфетт."
    img 5898
#    img 3267
    with fade
    w
    img 5899
#    img 3268
    w
    img 5900
#    img 3269
    m "Что дальше, Фред?"
    img 5901
#    img 3270
    fred "Теперь водите своей ручкой вверх и вниз, Миссис Бакфетт."

    stop music fadeout 1.0
    scene black
    image videoFred_Monica_Car_Blowjob_1_1 = Movie(play="video/Fred_Monica_Blowjob_1_1.mp4", fps=30)
    show videoFred_Monica_Car_Blowjob_1_1
    wclean
    scene black
    image videoFred_Monica_Car_Blowjob_1_2 = Movie(play="video/Fred_Monica_Blowjob_1_2.mp4", fps=30)
    show videoFred_Monica_Car_Blowjob_1_2
    wclean
    scene black
    image videoFred_Monica_Car_Blowjob_1_3 = Movie(play="video/Fred_Monica_Blowjob_1_3.mp4", fps=30)
    show videoFred_Monica_Car_Blowjob_1_3
    wclean
    scene black
    image videoFred_Monica_Car_Blowjob_1_4 = Movie(play="video/Fred_Monica_Blowjob_1_4.mp4", fps=30)
    show videoFred_Monica_Car_Blowjob_1_4
    wclean

    music Loved_up2
    menu:
        "Ускорить движения...":
            $ monicaFredWasForcedBlowjob = False
            #video быстрого минета
            stop music fadeout 1.0
            scene black
            image videoFred_Monica_Car_Blowjob_1_4_fast = Movie(play="video/Fred_Monica_Blowjob_1_4_fast.mp4", fps=30)
            show videoFred_Monica_Car_Blowjob_1_4_fast
            wclean
            #render
            img 5902
            fred "Ааааааааахх!"
            img 5903
            with fadelong
            w

            music Power_Bots_Loop
            img 3281
            with fadelong
            fred "Вы оказались на высоте, Миссис Бакфетт!"
            "Ваша часть договора выполнена."
            "Теперь мы можем ехать."

        "Фред, может быть хватит?":
            $ monicaFredWasForcedBlowjob = True
            img 3272
            m "Фред, может быть хватит?"
            "Пожалуйста!"
            img 3273
            fred "Миссис Бакфетт! Сядьте, пожалуйста, ровно на кресло!"
            img 3274
            m "Уфффф... Наконец-то!.."
            fred "Миссис Бакфетт. Я попросил Вас сесть ровно."
            img 3275
            m "Хорошо, Фред."
            "Но я не понимаю зачем."
            "Может быть уже поедем?"
            music Gearhead
            img 3276
            fred "Вот зачем!"
            img 3277
            m "О БОЖЕ!!!"

            scene black
            image videoFred_Monica_Car_Sex_1_1 = Movie(play="video/Fred_Monica_Car_Sex_1_1.mp4", fps=30)
            show videoFred_Monica_Car_Sex_1_1
            wclean
            scene black
            image videoFred_Monica_Car_Sex_1_2 = Movie(play="video/Fred_Monica_Car_Sex_1_2.mp4", fps=30)
            show videoFred_Monica_Car_Sex_1_2
            wclean
            scene black
            image videoFred_Monica_Car_Sex_1_3 = Movie(play="video/Fred_Monica_Car_Sex_1_3.mp4", fps=30)
            show videoFred_Monica_Car_Sex_1_3
            wclean
        #    video:3381_1
        #    video:3382
        #    video:3381_1
        #    video:3385
        #    video:3382

            img black_screen
            with Dissolve(0.5)
            "..."
            "..."
            fred "Ааааааааахх!"
            "..."
            "ЕЩЕ!!!"

            scene black
            image videoFred_Monica_Car_Sex_1_4 = Movie(play="video/Fred_Monica_Car_Sex_1_4.mp4", fps=30)
            show videoFred_Monica_Car_Sex_1_4
            wclean
            scene black
            image videoFred_Monica_Car_Sex_1_5 = Movie(play="video/Fred_Monica_Car_Sex_1_5.mp4", fps=30)
            show videoFred_Monica_Car_Sex_1_5
            wclean
            scene black
            image videoFred_Monica_Car_Sex_1_6 = Movie(play="video/Fred_Monica_Car_Sex_1_6.mp4", fps=30)
            show videoFred_Monica_Car_Sex_1_6
            wclean
            scene black
            image videoFred_Monica_Car_Sex_1_7 = Movie(play="video/Fred_Monica_Car_Sex_1_7.mp4", fps=30)
            show videoFred_Monica_Car_Sex_1_7
            wclean
            scene black
            image videoFred_Monica_Car_Sex_1_8 = Movie(play="video/Fred_Monica_Car_Sex_1_8.mp4", fps=30)
            show videoFred_Monica_Car_Sex_1_8
            wclean
            scene black
            image videoFred_Monica_Car_Sex_1_9 = Movie(play="video/Fred_Monica_Car_Sex_1_9.mp4", fps=30)
            show videoFred_Monica_Car_Sex_1_9
            wclean
        #    video:3387
        #    video:3388
        #    video:3389
        #    video:3390
        #    video:3393
        #    video:3394

            music Power_Bots_Loop
            img 3383
            with fadelong
            m "Ф... Ф...."
            "Ф... ФРЕД!!!"
            img 3279
            "ЧТО ТЫ СДЕЛАЛ?!?!?!"
            fred "Миссис Бакфетт."
            "Даже не вздумайте выплевывать."
            "Если Вы выплюнете, это разорвет наш договор!"
            "И Вы можете уходить!"
            img 3280
            m "..."
            "...."
            "..."
            stop music fadeout 1.0
            fred "НУ?!?!"
            "ГЛОТАЙТЕ!"
            menu:
                "Проглотить...":
                    $ monicaFredWasSpermEat = True
                    m "..."

                    sound snd_gulp
                    "Глоток"
                "Выплюнуть...":
                    img 5904
                    with fade
                    mt "(Сплевывание)"
                    fred "Понимаю, Вам еще предстоит это освоить..."
                    "Итак..."

            music Power_Bots_Loop
            fred "Вы оказались на высоте, Миссис Бакфетт!"
            img 3281
            "Ваша часть договора выполнена."
            "Теперь мы можем ехать."


    img black_screen
    with Dissolve(0.5)
    sound snd_car_turn_on
    $ renpy.pause(2)
    sound snd_car_engine
    $ renpy.pause(0.5)

    music snd_moderate_rain_music
#    img scene_Map
#    show screen Rain_overlay
#    $ rain = False
#    $ rainIntencity = 3

    img 3282
    with fadelong
    m "Чччасть... договора..."
    "...??????????..."
    "...!!!!!!!!!!!!!!!!"
    music Pyro_Flow
    img 3283
    "Ах ты ублюдок!!!"
    img 3284
    "СВОЛОЧЬ!!!"
    img 3285
    "Я УБЬЮ ТЕБЯ, СЛЫШИШЬ?!?!?!"
    img 3286
    fred "Мэм!"
    "Если Вы будете препятствовать водителю вести транспортное средство, то я вынужден буду высадить Вас!"
    "По инструкции безопасности!"
    img 3287
    "ВЫ МЕНЯ СЛЫШИТЕ, МЭМ?!?!"


    stop music fadeout 1.0
    img black_screen
    with Dissolve(0.5)
    sound snd_car_engine
    $ renpy.pause(2.0)

    music Groove2_85
    img 3288
    fred "Миссис Бакфетт!"
    "Не забудьте, что Вы гувернантка."
    "С солидным опытом."
    "Вы все умеете делать очень хорошо."
    "Ведите себя скромно."
    "Называйте всех Сэр и Мэм."
    "А также Мистер и Миссис."
    "От того какое впечатление вы произведете, зависит возьмут-ли Вас на работу."
    img 3289
    m "Но Фред."
    "Я думала ты уже договорился?"
    fred "Я договорился только с Мистером Робертсом."
    "С его супругой я не общался."
    "Вам надо произвести на нее впечатление."
    img 3290
    m "......"
    img 3291
    fred "Дождь закончился, Миссис Бакфетт."
    img 3290
    m "......"

    $ miniMapEnabledOnly = ["Street_Yard"]
    $ map_enabled = False
    $ hud_preset_current = "default"
    $ map_hud_preset_current = "map"
    $ unfocus_map()
    $ subst_to_object("Teleport_Gate", "afterJailHouseFamily_dialogue1")
    $ subst_to_object("Teleport_House", "afterJailHouseFamily_dialogue1")
    $ subst_to_object("Teleport_Fence", "afterJailHouseFamily_dialogue1")

    $ remove_objective("come_to_fred")
    $ add_objective("come_to_family", _("Идти к новым хозяевам"), c_orange, 10)
    $ autorun_to_object("street_house_main_yard", "afterJailHouseFamily_dialogue0")

    $ rain = False
    $ renpy.music.stop("rain")

    $ streetHouseMainYardStage = 1

    return
