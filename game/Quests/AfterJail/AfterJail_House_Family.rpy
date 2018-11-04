label afterJailHouseFamily_dialogue0():
    music Groove2_85
    img 3292
    with fadelong
    fred "Миссис Бакфетт."
    "Вернее теперь просто Моника."
    "Пожалуйста, пройдите к Вашим хозяевам, Вас ждут."
    call refresh_scene_fade()
    return
label afterJailHouseFamily_dialogue1(o,d):
    call afterJailHouseFamily_dialogue0()
    return

label afterJailHouseFamily_dialogue2:
    img 3293
    with fade
    if monicaFredWasForcedBlowjob == True:
        fred "Моника."
        "Ваш ротик бесподобен!"
    else:
        fred "Моника."
        "Ваша ручка просто бесподобна!"

    m "!!!!!!!!!!"
    call refresh_scene_fade()
    return

label afterJailHouseFamily_dialogue2a:
    music Groove2_85
    img 3292
    with fadelong
    fred "Беги скорее, Моника!"
    "Твои новые хозяева не станут ждать!"

    return

label afterJailHouseFamily_dialogue3:
    $ remove_objective("come_to_family")
    music Groove2_85
    img 3294
    with fadelong
    w
    img 3295
    with fade
    w
    img 3296
    with fade
    ralph "Здравствуй."
    "Как тебя зовут?"
    img 3297
    m "Меня зовут Моника, Мистер Робертс."
    img 3298
    ralph "Приятно познакомиться, Моника."
    "Мы тебя как раз ждали."
    img 3299
    m "Мне тоже приятно познакомиться, Мистер Робертс и .."
    img 3300
    "...Миссис Робертс."
    img 3301
    "У Вас такой забавный мальчик!"
    img 3302
    bardie "Я не мальчик!"
    "Я уже взрослый!"
    "Меня зовут Барди!"
    "Мне 18!"
    img 3303
    m "Конечно, Барди."
    "Я и с тобой рада познакомиться."
    img 3304
    music Pyro_Flow
    betty "Фи!"
    "Ральф!"
    "Зачем нам такая гувернантка?"
    "Неужели она что-то умеет?"
    "Да и вообще! Посмотри на нее!"
    img 3305
    "Она же некрасивая!"
    "Посмотри на ее фигуру! Какие у нее толстые неровные бедра!"
    "И какая нелепая грудь!"
    img 3306
    "Да и одета она как шлюха."
    "Посмотри на нее, Ральф."
    "Посмотри на ее одежду!"
    "Я не удивлюсь если она еще час назад ублажала мужчину!"
    img 3307
    with fade
    w
    img 3308
    w
    img 3309
    "Ральф? Тебе нужны шлюхи в доме?"
    "Мне нет!"
    img 3310
    mt "ССССССУЧКА!!!!"
    music Hidden_Agenda
    img 3311
    bardie_t "Я считаю что шлюх много не бывает..."
    "Надо рассмотреть эту MILF'у поближе"

    music Groove2_85
    img 3312
    ralph "Итак, Моника."
    "Что ты умеешь?"
    "Нам надо делать уборку в доме."
    img 3313
    m "Да, Мистер Робертс."
    "Я имею большой опыт в деле уборки."
    "Я уже занималась уборкой в богатых домах."
    img 3314
    mt "Да! Я вру!"
    "Но мне же надо устроиться сюда!"
    img 3315
    ralph "Видишь, Бетти?"
    "Она умеет делать уб..."
    img 3316
    music Pyro_Flow
    betty "Помолчи, Ральф!"
    "Я не разрешала тебе говорить!"
    ralph "Прости, дорогая..."

    img 3311
    sound man_steps
    img black_screen
    with Dissolve(0.5)
    $ renpy.pause(1.0)
    img 3317
    with fade
    sound wow
    w
    music Power_Bots_Loop
    img 3318
    with fade
    mt "МНЕ НАДО КАК-ТО УБЕДИТЬ ЭТУ СУЧКУ ВЗЯТЬ МЕНЯ!"
    "ААААААААРГХХ"
    "МОНИКА!"
    "КАК ЭТО ВСЕ МОГЛО СЛУЧИТЬСЯ????"
    music Hidden_Agenda
    img 3319
    m "Миссис Робертс."
    "Пожалуйста, возьмите меня."
    img 3320
    "Я Вас очень прошу!"
    "Я буду делать всю работу по дому и буду выполнять все Ваши приказы."
    img 3321
    "..."
    "Пожалуйста, не обращайте внимание на мой внешний вид."
    "Дело в том что мое платье испачкалось и мне пришлось одеть что попалось, так как я торопилась к Вам!"
    music Pyro_Flow
    img 3322
    betty "Нет, я не думаю."
    "Твоя прическа мне тоже не нравится."
    music Hidden_Agenda
    img 3323
    bardie_t "Хм..."
    "Неплохо было бы переубедить мачеху..."
    "Эта гувернантка весьма горяча..."
    img 3324
    "Еще такая послушная кукла может пригодиться для моих планов относительно мачехи..."

    sound man_steps
    img black_screen
    with Dissolve(0.5)
    $ renpy.pause(1.0)

    music Hidden_Agenda
    img 3325
    bardie "Бетти!"
    "Послушай."
    "Давай возьмем эту гувернантку."
    betty "С чего бы вдруг?"
    bardie "Я думаю она может хорошо работать."
    img 3326
    bardie_t "Своей киской, хе-хе"
    img 3326
    bardie "А я начну тебя слушаться."
    "И перестану донимать."
    "Стану хорошо учиться и не буду лезть в то что ты тратишь много денег на одежду!"
    betty "Хм..."
    "Обещаешь?"
    bardie "Обещаю, Бетти!"
    bardie_t "Ты мне потом заплатишь за мои лишения, сполна! Хе-хе"
    img 3327
    betty "Ой, ну ладно..."
    "Раз уж так..."
    "Но Барди!"
    "Я запомню твое обещание!"
    bardie "Конечно, Бетти!"
    img 3328
    betty "Хорошо."
    music Groove2_85
    "Ральф, пусть она работает у нас."
    "Может быть буду брать ее иногда в фитнес-зал."
    "Поправлю ее ужасную фигуру."
    img 3329
    music Power_Bots_Loop
    mt "!!!!!!!!"
    "ТВАРЬ!!!!"
    "НЕНАВИЖУ!!!"
    music Hidden_Agenda
    img 3330
    bardie "Добро пожаловать, Моника!"
    bardie_t "Хе-хе"

    music Groove2_85
    img 3331
    ralph "..."
    "Моника."
    "Ты можешь проходить в дом."
    "Мы сегодня не выспались, так как у нас были гости."
    "Но Бетти уже все убрала, поэтому на сегодня у тебя работы нет."
    "Мы сегодня пораньше ляжем спать."
    "Так что ты можешь отдыхать."
    "Завтра с утра ты можешь приступать к работе."

    m "Хорошо, Сэр."
    "Спасибо Вам."
    img 3332
    "..."
    "Спасибо, Миссис Робертс."
    img 3333
    betty "Фи..."
    mt "!!!!!!!"
    "СУЧКА!!!!!!"

    stop music fadeout 1.0
    sound man_steps
    img black_screen
    with Dissolve(0.5)
    sound highheels_short_walk
    $ renpy.pause(1.0)
    music Groove2_85
    img 3334
    with fadelong
    betty "Твоя униформа находится в ванной комнате."
    "Иди переоденься."
    "Мне не нравится что по дому кто-то гуляет в таком виде!"
    img 3335
    with fade
    "И да!"
    "Я буду присматривать за тобой!"

    $ streetHouseMainYardStage = 2

    $ miniMapEnabledOnly = ["Floor1", "Street_Yard"]
    $ casualMusic = "Groove2_85"

    $ bettyLocation = "Bedroom1"
    $ bardieLocation = "BedroomBardie"
    $ ralphLocation = "LivingRoom"

    $ subst_to_object("Teleport_House_Outside_Outside", "afterJailHouseFamily_dialogue4")
    $ subst_to_object("Teleport_Gate", False)
    $ subst_to_object("Teleport_House", False)
    $ subst_to_object("Teleport_Fence", False)
    $ autorun_to_object("basement_pool", False)
    $ autorun_to_object("floor1", "afterJailHouse_dialogue1")
    call refresh_scene_fade()
    return

label afterJailHouseFamily_dialogue4(o,d):
    mt "Я никуда не пойду! Я так устала!"
    return
