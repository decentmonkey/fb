label afterJailHouse_dialogue1:
    music RnB4_100
    img 3336
    with fadelong
    mt "Моника!"
    "Моника!"
    "Ты дома!"
    "Да!"
    "Пусть все совсем не так как ты хотела!"
    "Но ты снова под этой крышей!"
    img 3337
    "Жизнь, кажется, начинает налаживаться."
    "Ну хоть чуть-чуть!"
    img 3338
    "Мне сейчас надо переодеться."
    "Принять ванну."
    "Плотно покушать."
    "Как я хочу нормально наесться наконец!"
    "И идти ложиться спать."

    img 3339
    "Наверняка хозяева заняли мою спальню."
    "Еще какую-то комнату занял мальчик."

    img 3340
    "Остается еще спальня для гостей!"
    "Я наконец-то нормально высплюсь!"
    "В мягкой постели, приятно пахнущей ароматом лаванды!"
    "Моника!"
    "Я так за себя рада!"

    music Groove2_85

    $ add_objective("take_governess_cloth", _("Одеть униформу"), c_blue, 10)
    $ add_objective("take_bath", _("Принять душ"), c_green, 11)
    $ add_objective("to_eat", _("Поесть"), c_orange, 12)

    $ monicaEated = False
    $ bathTaken = False

    $ autorun_to_object("bedroom_second", "afterJailHouse_dialogue2")
    $ autorun_to_object("bedroom_bardie", "afterJailHouse_dialogue3")
    $ autorun_to_object("living_room", "afterJailHouse_dialogue4")
    $ autorun_to_object("bedroom1", "afterJailHouse_dialogue5")
#    $ autorun_to_object("kitchen", "afterJailHouse_dialogue6")
#    $ autorun_to_object("kitchen2", "afterJailHouse_dialogue6")
    $ autorun_to_object("bathroom_bath", "afterJailHouse_dialogue7")

    $ subst_to_object("Teleport_Kitchen", "afterJailHouse_dialogue1a")
    $ subst_to_object("Teleport_Bedroom", "afterJailHouse_dialogue1a")

    $ miniMapEnabledOnly = ["Bathroom", "Floor1", "Floor2", "Basement", "Street_Yard"]

    $ autorun_to_object("floor1", "afterJailHouse_dialogue1b")

    call refresh_scene_fade()
    return

label afterJailHouse_dialogue1a(o,d): #
    mt "Мне надо сначала переодеться, а то хозяева будут ругаться!"
    return
label afterJailHouse_dialogue1b: #
    help "В доме стали доступны новые локации! Гостиная, спальня для гостей и комната Барди."
    return


label afterJailHouse_dialogue2: #bedroomsecond
    mt "Я сюда очень давно не заходила."
    "Эта спальня, конечно, не сравнится с моей, но меня она сейчас вполне устроит..."
    return
label afterJailHouse_dialogue3: #bedroombardie
    mt "Раньше здесь была моя гардеробная."
    "Они переделали мою гардеробную под комнату этого оболтуса!!!"
    return
label afterJailHouse_dialogue4: #livingroom
    mt "Не помню когда я здесь была в последний раз."
    "Кажется когда запретила мужу приводить гостей."
    return
label afterJailHouse_dialogue5: #bedroom_betty
    return
label afterJailHouse_dialogue6: #kitchen
    return
label afterJailHouse_dialogue7: #bathroom
    music Groove2_85
    img 3341
    with fadelong
    mt "Кажется это униформа Юлии?"
    if juliaFirePlanned == True and juliaFireCancelled == True:
        "Как хорошо что я уволила эту дуру!"
        "Что бы я делала сейчас, если бы она была здесь?"
    else:
        "Как хорошо что ее здесь нет!"
        "Интересно, а куда она делась?"
        "Ладно, мне сейчас не до нее!"

    menu:
        "Одеть униформу горничной.":
            pass
        "Уйти.":
            $ autorun_to_object("bathroom_bath", "afterJailHouse_dialogue7")
            call change_scene("floor2")
            return

    $ cloth_type = "Governess"
    $ cloth = "Governess"

    img 3342
    with fade
    mt "..."
    img 3343
    with fade
    w
    img 3344
    with fade
    mt "Теперь надо принять ванну, поесть и ложиться спать."
    "Наконец-то, Моника!"
    img 3345
    "Наконец-то!"

    $ remove_objective("take_governess_cloth")
    $ subst_to_object("Teleport_Kitchen", False)
    $ subst_to_object("Teleport_Bedroom", False)

    $ miniMapEnabledOnly = []

    $ autorun_to_object("kitchen", "afterJailHouse_dialogue13")
    $ autorun_to_object("kitchen2", "afterJailHouse_dialogue13")

    call refresh_scene_fade()
    return

label afterJailHouse_dialogue8: #bed
    if cloth != "Governess":
        mt "Мне надо переодеться сначала."
        return
    $ print "HERER!!!!!"
    if monicaEated == False:
        mt "Перед сном надо что-то поесть."
        "Я уже нормально не ела целую вечность!!!"
        return
    if bathTaken == False:
        mt "Хоть меня дождь хорошенько помыл, я хотела бы освежиться перед сном!"
        return
    call afterJailHouse_dialogue17()
    return

label afterJailHouse_dialogue9: #bathroom forbid
    sound highheels_run2
    music Pyro_Flow
    img 3344
    with fadelong
    betty "Это что это ты собралась делать, дорогуша??"
    img 3346
    music Hidden_Agenda
    m "Миссис Робертс, я хотела принять ванну."
    mt "СВОЮ ВАННУ В СВОЕМ ДОМЕ!!!"
    "И Я НЕ ХОЧУ СПРАШИВАТЬ КАКИХ-ТО ЛЕВЫХ БАБ РАЗРЕШЕНИЯ НА ЭТО!!!"
    img 3347
    m "Простите, мне надо было спросить разрешения у Вас?"
    "Я заранее прошу прощения, Миссис Робертс."

    music Pyro_Flow
    img 3348
    betty "!!!"
    "Какое разрешение, детка???"
    "Ты что, собираешься мыть свое тело с такой жуткой фигурой в моей ванне?"
    "Или в моем душе?"
    "Твое дело - это убирать дом!"
    "А пользоваться удобствами - это привилегия хозяев!"
    img 3349
    "Скажи, ты здесь хозяйка?"
    mt "ДА ДА ДА, СУЧКА!!!"
    "Я ЗДЕСЬ ХОЗЯЙКА, А ТЫ НИКТО!!!"
    music Hidden_Agenda
    img 3350
    m "Нет, Миссис Робертс."
    "Здесь хозяйка Вы..."
    music Pyro_Flow
    betty "Тогда выйди отсюда и чтобы я тебя больше здесь не видела!"
    m "Да, Миссис Робертс. Прошу прощения."

    $ monicaBathroomForbidden = True
    $ remove_objective("take_bath")
    $ bathTaken = True

    music casualMusic

    $ autorun_to_object("floor2", "afterJailHouse_dialogue11")

    call change_scene("floor2")
    return

label afterJailHouse_dialogue10: #бетти запретила
    mt "Бетти запретила мне заходить сюда."
    return

label afterJailHouse_dialogue11:
    mt "Ладно, душ - это сейчас не самое главное."
    "Я очень хочу скорее поспать на мягкой кроватке!"
    call afterJailHouse_dialogue16()
    return

label afterJailHouse_dialogue12:
    sound highheels_run2
    music Pyro_Flow
    img 3354
    with fadelong
    betty "Я не поняла!"
    "Что ты здесь делаешь???"
    music Hidden_Agenda
    img 3355
    with fade
    m "Мэм..."
    "Я зашла просто покушать..."
    img 3356
    "Вернее, простите, Мэм, я не так сказала."
    "Я хотела начать готовить ужин, чтобы Вы и Ваш муж и ребенок могли покушать перед сном."
    img 3358
    music Pyro_Flow
    betty "Детка!"
    "Запомни правило!"
    "В этом доме готовлю Я!"
    "Для своего мужа!"
    img 3359
    "И мне не нужно, чтобы в мою семью влезала какая-то проститутка!"
    "ЯСНО ТЕБЕ!!!"
    music Hidden_Agenda
    img 3360
    with fade
    m "Миссис Робертс.."
    "Я не имела ввиду.. Я просто..."
    music Pyro_Flow
    img 3361
    betty "Если я еще раз увижу тебя на кухне."
    "Или увижу что пропали хоть какие-то продукты..."
    img 3362
    with hpunch
    "Я тебя сразу уволю!"
    "Ты поняла?"
    img 3363
    m "Да, Миссис Робертс..."
    "Я поняла..."
    betty "Я буду проверять холодильник!"
    "И другие вещи в доме!"
    "Мебель, одежду, все!"
    "Я подозреваю что такая проститутка, как ты, может что-то украсть!"
    img 3364
    "А сейчас, пожалуйста, покинь кухню!"

    $ remove_objective("to_eat")
    $ monicaEated = True

    $ monicaKitchenForbidden = True

    $ autorun_to_object("floor1", "afterJailHouse_dialogue14")

    music casualMusic

    call change_scene("floor1")
    return

label afterJailHouse_dialogue13:
    $ autorun_to_object("kitchen", False)
    $ autorun_to_object("kitchen2", False)

    music RnB4_100
    img 3353
    with fadelong
    mt "Боже! Наконец-то я поем!"
    call refresh_scene_fade()
    return

label afterJailHouse_dialogue14:
    mt "Вот тебе и покушала..."
    call afterJailHouse_dialogue16()
    return

label afterJailHouse_dialogue15:
    mt "Бетти запретила мне появляться на кухне... Так что в этом доме я остаюсь без еды..."
    return

label afterJailHouse_dialogue16:
    if monicaEated == False or bathTaken == False:
        return

    music Power_Bots_Loop
    imgc Dial_begin37_3
    with Dissolve(0.5)
    mt "Просто замечательно!"
    "Мне не принять душ!"
    "Мне не поесть!"
    "Что в этом доме мне делать МОЖНО?"
    "Похоже ничего!"
    imgc Dial_begin37_4
    mt "НЕНАВИЖУ!"
    "НЕНАВИЖУ!!!"

    imgc Dial_begin37_5
    mt "(хмык)"
    "Пойду спать."
    "У меня нет больше сил..."
    $ add_objective("to_sleep", _("Лечь спать"), c_green, 12)

    music casualMusic

    call refresh_scene_fade()
    return

label afterJailHouse_dialogue16a:
    mt "Эту спальню заняли новые хозяева. Мне нежелательно сюда заходить..."
    return

label afterJailHouse_dialogue17:
    #render+
    #Диалог Моники с Бетти в спальне для гостей
    music Hidden_Agenda
    img 5766
#    imgl Dial_begin37_6
    with fadelong
#    /Кажется эта комната свободна.
    mt "Постель!"
    "Наконец-то я нормально высплюсь!"
    "Я придумаю завтра как мне помыться и где покушать!"
    "В конце концов, мне надо худеть!"
    "Все девушки легко переносят голод!"
    "Но я так давно нормально не спала!"
    "Я так хочу просто уснуть, на теплой кроватке!"
    "Наконец-то!"

    img black_screen
    with Dissolve(0.5)
    sound highheels_run2
    $ renpy.pause(1.0)

    music Pyro_Flow
    img 5767
#    imgr Dial_Betty_2
    with fadelong
    betty "Моника!"
    "Нерадивая служанка!"
    music Hidden_Agenda
    img 5768
#    imgl Dial_begin37_7
    m "Да, Миссис Робертс?"
    "Что Вы хотели?"
    music Pyro_Flow
    img 5769
    betty "Что ты делаешь здесь?"
    music Hidden_Agenda
    img 5770
    m "Миссис Робертс, я собиралась лечь спать. Мистер Робертс сказал что я могу..."
    music Pyro_Flow
    img 5771
#    imgr Dial_Betty_3
    betty "Во-первых, ты должна запомнить что в этом доме командую я, а не Ральф!"
    img 5774
#    imgl Dial_begin37_8
    m "Да, Мэм, я запомнила..."
    img 5772
    betty "Во-вторых, это наш дом."
    "И ты не можешь здесь спать."
    music Power_Bots_Loop
    img 5773
    with fade
#    imgl Dial_begin37_9
    mt "КАК Я НЕ МОГУ ЗДЕСЬ СПАТЬ!!!"
    "ДА Я СЮДА УСТРОИЛАСЬ ТОЛЬКО ИЗ-ЗА ЭТОГО!!!"
    "ЗА БЕСПЛАТНО!!!"
    "ТОЛЬКО ЗА ЭТУ!!!"
    "ЭТУ ГРЕБАНУЮ ПОСТЕЛЬ!!!"
    "И МНЕ НЕЛЬЗЯ СПАТЬ НА НЕЙ????"
    music Hidden_Agenda
    img 5775
#    imgl Dial_begin37_8
    m "Миссис Робертс, что Вы имеете ввиду?"
    "А где мне спать?"
    music Pyro_Flow
    img 5776
#    imgr Dial_Betty_4
    betty "Вы должны спать в специальном помещении для прислуги."
    music Hidden_Agenda
    img 5777
#    imgl Dial_begin37_10
    m "Миссис Робертс, а где это помещение?"
    mt "А где спала Юлия?"
    "Я даже никогда не задумывалась..."
    music Pyro_Flow
    img 5778
    betty "Я не знаю где это, но где-то внизу."
    "В любом случае, мне ночью не нужна прислуга в доме!"
    img 5779
    "Тебе все ясно, Моника?"
    music Hidden_Agenda
    img 5780
    m "Да, Миссис Робертс."
    "Я поняла, я пойду поищу..."
    mt "(хмык)"
    img 5781
#    imgr Dial_Betty_5
    music Groove2_85
    betty "..."
    "Да, и вообще..."
    m "Что, Миссис Робертс?"
    img 5782
    betty "Мне надоело за тобой ходить и указывать что тебе делать и как."
    "Ты, Моника, очень недешево стоишь и я думаю что не должна тебя учить что и как делать."
    img 5783
    "Что можно, а чего нельзя."
    "Ты должна сама уметь все соблюдать."
    img 5784
#    imgl Dial_begin37_11
    with hpunch
    m "..."
    "Миссис Робертс..."
    "Что Вы имеете ввиду под словом Недешево?"
    img 5785
    betty "Я считаю что мы не можем себе такого позволить!"
    "И я не знаю зачем Ральф решил нанять гувернантку за так много денег."
    img 5786
    mt "???????"
    img 5787
    betty "Но за $90 в час гувернантка должна уметь вообще все."
    "И не должно быть необходимости ничему учить ее!"
    music Power_Bots_Loop
    img 5788
#    imgl Dial_begin37_12
    with hpunch
    mt "90... ДЕВЯНОСТО!!!"
    "ДОЛЛАРОВ В ЧАС!!!"
    "НА ЭТИ ДЕНЬГИ МОЖНО ЖИТЬ В ХОСТЕЛЕ БОЛЬШЕ НЕДЕЛИ!!!"
    img 5789
    "ПОЧЕМУ ЖЕ МНЕ СКАЗАЛИ ЧТО Я РАБОТАЮ БЕСПЛАТНО???"
    img 5790
    "Надо узнать у Ральфа насчет моей оплаты..."
    music Hidden_Agenda
    img 5791
#    imgl Dial_begin37_11
    m "..."
    "Да, Миссис Робертс."
    "Я все поняла."
    "Простите меня."
    "Я работаю первый день."
    "Только осваиваюсь."
    "У Вас такой большой дом, что в нем можно заблудиться!"
    music Groove2_85
    img 5792
#    imgr Dial_Betty_6
    betty "Да, мне нравится этот домик."
    "Вполне ничего себе..."
    img 5793
    mt "ЕЩЕ БЫ!!!"
    "НЕ ТЫ СУЧКА ДЕЛАЛА ЕГО ДИЗАЙН"
    "НЕ-НА-ВИ-ЖУ!!!"
    img 5794
    with fade
    m "Я могу идти, Миссис Робертс?"
    betty "Да, иди."
    m "Спасибо, Миссис Робертс..."

    $ ralphStage = 1
    $ add_objective("ask_ralph", _("Узнать у Ральфа по поводу оплаты"), c_orange, 13)

    $ autorun_to_object("bedroom_second", "afterJailHouse_dialogue17a")

    $ autorun_to_object("basement_hole", "afterJailHouse_dialogue18")

    $ bedroomSecondStage = 1
    $ basementHoleRefuseFlag = False


    call refresh_scene_fade()
    return

label afterJailHouse_dialogue17a:
    mt "Надо узнать у Ральфа по поводу моей оплаты."
    "И надо найти место где мне спать."
    "Мне уже неважно где это будет! Я хочу отдохнуть от этого кошмара!!!"

    return

label afterJailHouse_dialogue18:
    #render+
    #Моника в подвале
    music Power_Bots_Loop
    img 5795
#    imgl Dial_begin37_18
    with fadelong
    mt "Снова этот вонючий подвал..."
    "Я поклялась себе что никогда сюда не спущусь..."
    "Но что мне делать???"
    "Идти на улицу?"

    music As_long_as_a_word_remains_unspoken
    img 5796
#    imgl Dial_begin37_19
    mt "Моника!"
    "Как же тебя угораздило так влипнуть?"
    "Ты бродишь по подвалу в собственном доме..."
    "В поисках постели..."

    call refresh_scene_fade()

#    mt "Какой страшный корридор..."
#    "Мне нигде не найти спальню для прислуги."
#    "Там в конце есть какой-то свет."
#    "Может быть сходить проверить?"
    return

label afterJailHouse_dialogue19:
    img 3365
    with fadelong
    mt "Я не знаю куда ведет этот коридор."
#    img 3366
    img 5797
    mt "Он темный."
    "Я никогда по нему не ходила."
    "Может быть где-то там ночевала Юлия?"

#    $ autorun_to_object("basement_bedroom2", "afterJailHouse_dialogue20")
    call afterJailHouse_dialogue20()
    return

label afterJailHouse_dialogue20:
    img black_screen
    with Dissolve(1.0)
    help "Вы можете безопасно сохраниться в этой локации для того, чтобы использовать сохранение в Эпизоде 2."
    img 3374
    with fadelong
    mt "Вот где жила Юлия..."
    img 3375
    with fade
    mt "Узкая темная каморка, без окон."
    mt "В то время пока я нежилась в постели из шелка..."
    img 3376
    with fade
    mt "..."
    "Там на столике что-то лежит..."

    $ miniMapEnabledOnly = ["none"]


    $ add_objective("take_journal", _("Там на столике что-то лежит..."), c_white, 15)

#    call refresh_scene_fade()
    return

label afterJailHouse_dialogue21:
    $ basementBedroomJournal = False

#    sound snd_take_paper
    img 3378
    with fadelong
    mt "Это мой журнал."
    "Я на обложке."
    "Зачем он Юлии?"
    img 3377
    with fade
    mt "Наверное она смотрела на него и думала про меня."
    "Про ту кто живет наверху..."
    "..."
    img 3379
    with fade
    mt "Моника."
    "Что с тобой стало?"
    "..."
    "Не могу сейчас ни о чем думать."
    "Главное что я под крышей над головой, а не в ледяной камере или еще где похуже."
    "..."
    "Надо раздеться и ложиться спать..."

    $ remove_objective("take_journal")
    $ add_inventory("journal", 1, True)
    $ basementBedroomStage = 1
    $ autorun_to_object("basement_bedroom1", "afterJailHouse_dialogue22")

    call change_scene("basement_bedroom2", "Fade", False)
    return

label afterJailHouse_dialogue22:
    mt "В этот старый шкаф можно повесить одежду..."
    "Если это можно назвать одеждой..."
    return
