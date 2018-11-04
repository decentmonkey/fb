default christineFuckedByFred = False
default christineFuckedByFredBlowjob = False
default christineFuckedByFredAnal = False


default gas_saleswoman_dialogue2_flag1_viewed = False

label gas_saleswoman_dialogue2:
    if gasStationSaleswomanMischiefed == False:
        call gas_saleswoman_dialogue2_alternative()
        return
    music Hidden_Agenda
    call textonblack(_("ТЕМ ВРЕМЕНЕМ..."))
    img black_screen
    with Dissolve(1)
#    music Groove2_85
    img 4687
    with fadelong
    sound snd_car_door
    $ renpy.pause(1)
    sound snd_car_turn_on
    img 4688
    with fade
    $ renpy.pause(3)
    sound snd_car_engine
    img scene_Street_Gas_Station_Driver_Monica_EveningDress_Evening
    with fadelong
    $ renpy.pause(1)
    sound man_steps
    img scene_Street_Gas_Station_Car_NoDriver_Evening
    with Dissolve(1)
    $ renpy.pause(1)

    img 4373
    with fadelong
    saleswoman "Здравствуйте, Мистер."
    "Прошу прощения, но компьютер так и не работает, так что если вы хотели заправиться, то..."

    img 4374
    fred "Здравствуйте, юная леди.
    Я приехал по другому вопросу."

    img 4375
    saleswoman "По какому?"

    img 4376
    fred "Вы, наверное, очень устали за сегодня.
    Вы работали весь день без отдыха."

    "Ваша смена, должно быть, уже давно закончена.
    Почему вы на работе?"

    img 4377
    saleswoman "Почему вас это интересует?
    Какое вам дело до этого?"

    img 4378
    fred "Ну как же, такая красивая и очаровательная девушка."
    "Вы не созданы для такой тяжелой и долгой работы..."

    menu:
        "Красивая?...":
            jump gas_saleswoman_dialogue2_l1
        "Мне не нужны ваши комплименты!":
            call gas_saleswoman_dialogue2_getout1()
            return
    label gas_saleswoman_dialogue2_l1:
    img 4379
    saleswoman "Красивая?..."

    img 4380
    saleswoman "Да, если честно, то я не должна была работать сейчас."

    img 4381
    "Но мой Босс очень зол на меня."
    "И теперь мне, наверное, придется работать целыми сутками и без выходных..."

    img 4382
    fred "Что же привело его в ярость?"

    ###
    if gasStationMonicaLied == True:
        img 4383
        saleswoman "То что я неправильно поставила бутылку самого дорогого вина."
        "Тут была одна су.. ой простите, женщина, которая случайно разбила его и чуть не поранилась."
        "Босс посчитал что это моя вина и теперь мне придется долго расплачиваться за эту оплошность."

        img 4384
        fred "Значит это была Ваша вина?"

        img 4385
        saleswoman "Если честно, то... я не знаю стоит-ли Вам говорить."
        "В общем... Эта бутылка стояла также как и все."

        img 4386
        "Я думаю что она сама ее разбила, специально."

        img 4387
        fred "Но зачем?"

        img 4388
        "Затем что она долго ждала меня."


        fred "Это было очень долго?"

        img 4389
        saleswoman "Сказать по правде, это было не более 10 минут."

        img 4390
        fred "Тогда почему Вас так строго наказали?"

        img 4391
        saleswoman "Эта женщина оказалась очень влиятельна."
        "Когда мой Босс узнал кто она, то у него прямо изменился голос."
        "Он даже не стал меня слушать!!!"
        "А ведь я не виновата!!!"

    else:
        saleswoman "Тут была одна су.. ой простите, женщина, которая случайно разбила его и чуть не поранилась."
        "Она призналась в том что это ее вина, но при этом настояла на том чтобы меня наказали."
        fred "За что наказали? Ведь это ее вина?"

        saleswoman "За то что она долго ждала меня."

        fred "Это было очень долго?"

        saleswoman "Сказать по правде, это было не более 10 минут."

        fred "Тогда почему Вас так строго наказали?"

        saleswoman "Эта женщина оказалась очень влиятельна."
        "Когда мой Босс узнал кто она, то у него прямо изменился голос."
        "Он даже не стал меня слушать!!!"
        "А ведь я не виновата!!!"

    ###---

    img 4392
    fred "Бедная девушка.
    Как я Вас понимаю."

    img 4393
    fred "Как вас зовут?"

    img 4394
    saleswoman "Кристина."

    fred "Приятно познакомиться, Кристина.
    Меня зовут Фред. Мистер Фред."

    img 4395
    saleswoman "Приятно познакомиться, Мистер Фред."

    img 4396
    fred "Скажите, как вы хотели назвать эту женщину?"

    img 4397
    saleswoman "В смысле? Я назвала ее... женщиной."

    fred "Нет, вы хотели назвать ее по другому."

    img 4398
    saleswoman "Вы, наверное, ошиблись.
    Я... ничего не хотела сказать... такого..."

    img 4399
    fred "Вы не хотели назвать ее сучкой?"

    img 4400
    saleswoman "Что? Нет, Мистер, ни в коем случае, я просто..."

    img 4401
    fred "Кристина, расслабьтесь.
    Я знаю что она сучка.
    Вы можете говорить об этом открыто."

    img 4402
    saleswoman "Вы знаете эту женщину?"

    img 4403
    fred "Очень хорошо ее знаю."
    "Она умеет быть сучкой, но я умею делать так что она становится очень покладистой."

    img 4404
    saleswoman "Что вы имеете ввиду?
    А кто она вообще такая?
    Почему ее все так боятся?"

    img 4405
    fred "Моника Бакфетт, одна из самых богатых леди этого города.
    Также она владелица журнала моды."

    img 4406
    saleswoman "Ах, это та самая Моника Бакфетт?? Я вспомнила это имя!"
    "Теперь мне все понятно."
    img 4407
    "А что вы имели ввиду когда сказали что умеете влиять на нее?
    Кем Вы приходитесь ей?"

    img 4408
    "Если вы ее знаете, значит вы, наверное, тоже большой человек..."

    img 4409
    fred "Видите-ли, Кристина, величина человека - это очень относительное понятие."
    "Я не привык преподносить себя как большой человек именно из-за относительности этого определения."
    "Но, по правде говоря, если отбросить скромность, то я не самый последний человек."

    img 4410
    saleswoman "?"

    img 4411
    fred "Я ее личный помощник, правая рука."
    "Я профессионал, и она во всем слушается меня."

    img 4412
    saleswoman "Правда?"

    img 4413
    fred "..."

    #
    if gasStationMonicaLied == True:
        img 4414
        saleswoman "Мистер Фред.
        Скажите, а вы можете как-то повлиять на Миссис Бакфетт?"
        "Понимаете, я и так мало зарабатываю.
        У меня нет большого образования, чтобы найти другую работу."
        "Я как раз собиралась его получать, но..."
        img 4415
        "..."

        img 4416
        "Эта бутылка очень дорого стоит и теперь, когда Босс так зол, он удержит у меня все премии и..."

    #
    else:
        saleswoman "Мистер Фред.
        Скажите, а вы можете как-то повлиять на Миссис Бакфетт?"
        "Понимаете, я и так мало зарабатываю.
        У меня нет большого образования, чтобы найти другую работу."
        "Я как раз собиралась его получать, но..."
        "..."
        "Теперь Босс очень зол на меня, но ведь я не виновата!"
        "Однако он удержит у меня все премии и заставит работать сверхурочно! И..."

    #---

    img 4417
    w
    img 4418
    w
    img 4419
    fred "Кристина.
    Я все понимаю.
    Я здесь чтобы помочь Вам!"

    img 4420
    saleswoman "Правда? Вы мне поможете?"

    img 4421
    "Ведь все это несправедливо!"

    img 4422
    fred "Конечно, Кристина!"
    "Это несправедливо!
    Несправедливо что Вас наказали ни за что."

    img 4423
    "Также несправедливо то что такая красивая девушка как Вы работает в этом месте, да еще и сверхурочно."

    img 4424
    saleswoman "Что вы имеет ввиду?"

    img 4425
    fred "Я имею ввиду что Вам, Кристина, стоит работать кое-где получше, учитывая Ваши внешние данные."

    img 4426
    saleswoman "Вы знаете какое-то место?"

    img 4427
    fred "Конечно! Не забывайте, что я личный помощник самой Моники Бакфетт!"
    "Владелицы модного журнала."

    "Я считаю что мы просто обязаны заключить контракт с такой непревзойденной моделью как Вы, Кристина."

    img 4428
    saleswoman "Вы... Правда считаете что я достойна этого? Вы считаете что я настолько красивая?"

    img 4429
    fred "Да, Кристина. Посмотрите на себя в зеркало, Вы очарование!"

    menu:
        "Я просто обожаю фотографироваться.":
            jump gas_saleswoman_dialogue2_l2
        "Предложение работы от первого встречного?":
            call gas_saleswoman_dialogue2_getout2()
            return
    saleswoman "Спасибо..."
    label gas_saleswoman_dialogue2_l2:
    img 4430
    "Я просто обожаю фотографироваться."
    "Я даже не могла мечтать о таком предложении! Журнал моды!"

    img 4431
    "..."

    img 4432
    "Мистер Фред, но... разве Моника Бакфетт не зла на меня?
    Она на меня так смотрела, я думаю она никогда не согласится на то чтобы заключить контракт со мной!"

    img 4433
    fred "Миссис Бакфетт очень вспыльчива, но быстро отходит."
    "Между прочим, она говорила мне о Вас сегодня."

    img 4434
    saleswoman "Правда?"

    img 4433
    fred "Да, это именно она обратила внимание на Вас, Кристина."
    "Мы заезжали с ней вместе сегодня и, если честно, я вас не заметил."
    "Я думаю что все дело в вашем рабочем пиджаке."
    "Он скрывает Вашу благородную фигуру, но Моника Бакфетт очень опытна и заметила Вас."

    "Может быть даже она была так зла из-за того что завидует Вам..."

    img 4435
    saleswoman "Правда? Завидует?"

    fred "Конечно, Кристина."

    img 4436
    "Но Моника Бакфетт, в первую очередь профессионал.
    И она не поддается эмоциям."
    "Думаю, если бы я захотел, то мог бы уговорить ее не сердиться на Вас.
    И взять Вас на работу."
    img 4437
    "В качестве Топ модели нашего журнала..."

    img 4438
    saleswoman "Топ модели??? Правда?!"

    img 4439
    fred "Да, Кристина. Топ модели."
    "А еще я бы мог попросить ее позвонить вашему Боссу, чтобы он принес извинения перед Вами за то что наказал Вас."

    img 4440
    saleswoman "Правда? Это возможно?
    Я бы с удовольствием посмотрела на его лицо в этот момент!!!"
    "Он никогда ни за что не извиняется!"

    img 4441
    fred "Вот увидите, ему придется..."

    #
    if gasStationMonicaLied == True:
        "Также Миссис Бакфетт попросит его предоставить счет за разбитую бутылку."
    #---

    "Я считаю что так будет справедливо, поэтому я скажу ей сделать это."
    "Как и то чтобы заключить контракт."

    img 4442
    saleswoman "Вы правда можете сделать все это? Вы думаете я подхожу Вам?"

    img 4443
    fred "Конечно, Кристина.
    Мне кажется что вы подходите."
    "Хотя у меня есть кое-какие сомнения...насчет того стоит-ли мне делать все это..."

    img 4444
    saleswoman "Какие?"

    img 4445
    fred "Видите-ли, Кристина. Я профессионал."
    "Говоря Миссис Бакфетт свое мнение о Вас, мне придется ставить на кон свою репутацию как профессионала."

    img 4446
    "Я вижу что красотой вашего личика вы затмеваете все вокруг..."

    img 4447
    saleswoman "..."

    img 4448
    fred "Я уверен что ваше тело такое же красивое как и ваше лицо..."

    img 4449
    saleswoman "Оно такое же красивое..."

    img 4450
    fred "Но, как профессионал, я не могу оценить его, потому что на Вас много одежды."

    img 4451
    "Например Ваш пиджак."
    "Он очень красивый, но..."

    img 4452
    menu:
        "Вам нравится мой пиджак?":
            jump gas_saleswoman_dialogue2_l3
        "Мне он тоже нравится, но я вам не верю!":
            call gas_saleswoman_dialogue2_getout3()
            return
    label gas_saleswoman_dialogue2_l3:
    saleswoman "Вам нравится мой пиджак?"

    img 4453
    fred "Да, Кристина, мне он нравится, но..."

    img 4454
    saleswoman "Вы хотите чтобы я сняла его?"

    img 4455
    fred "Да, Кристина, для начала сделайте это..."

    img 4456
    saleswoman "Хорошо, Мистер Фред."

    sound snd_fabric1
    img 4457
    with fadelong
    saleswoman "Вам нравится?"

    img 4458
    fred "Да, Кристина, я не разочарован!"

    "Но, чтобы быть уверенным, я бы хотел увидеть больше."

    img 4459
    saleswoman "Что же вы хотите?"

    img 4460
    fred "Мне очень нравится Ваша юбочка, Кристина!"

    img 4461
    saleswoman "Вам нравится моя юбочка?"

    #
    if gasStationSaleswomanAlmostCummed == True:
        img 4462
        saleswoman "(как же я возбуждаюсь! эта стерва не дала мне кончить!)"
        "(мне оставалось от силы 10 секунд!)"
        img 4463
        "(у меня до сих пор дрожь в ногах!)"
        img 4464
        saleswoman "(и этот босс! ничего, ему придется извиниться передо мной!)"
        img 4465
        saleswoman "Я только недавно закончила оттирать следы разбитой бутылки!"
#        "пятно на полу"

    #
    else:
        saleswoman "(как же я возбуждаюсь! эта стерва не дала мне поиграть сегодня!)"
        saleswoman "(и этот босс! ничего, ему придется извиниться передо мной!)"
    #--

    img 4466
    saleswoman "Вы хотите чтобы я сняла ее?"

    img 4467
    fred "Да, Кристина!
    Я бы хотел оценить Вас прежде чем рисковать своей репутацией!"

    img 4468
    saleswoman "Вы думаете что я могу быть некрасивой где-то?"

    img 4469
    fred "Не знаю, Кристина.
    Но я знаю что если у вас красивое тело, то вы бы хотели показать его!"
    "Но если у вас где-то что-то не так, то вы можете не показывать мне."
    "Мы просто забудем этот разговор."

    img 4470
    with fadelong
    saleswoman "..."

    img 4471
    fred "Так мне идти?"

    img 4472
    w

    img 4473
    saleswoman "Не надо, Мистер Фред.
    Я красивая везде и могу это доказать!"

    img 4474
    fred "Отлично, Кристина, прошу вас!"

    img 4475
    saleswoman "Мистер Фред, но мне неудобно делать это здесь, на работе."
    "Может быть мы встретимся с Вами в одной из Ваших студий и..."

    img 4476
    fred "Кристина, у меня плотный график!
    Завтра я улетаю."
    "У меня будет время поговорить с Моникой Бакфетт только с утра!"
    "Я и так потратил время чтобы приехать сюда к Вам!"
    "Здесь есть какое-то уединенное место?"

    img 4477
    saleswoman "Здесь есть туалет..."

    img 4478
    fred "Хорошо, Кристина, пройдите, пожалуйста, в него и разденьтесь полностью!"

    img 4479
    saleswoman "Полностью??? И даже трусики?"

    img 4480
    fred "У Вас красивые трусики, Кристина?"

    menu:
        "Да...":
            jump gas_saleswoman_dialogue2_l4
        "У меня красивые трусики и они нравятся моему парню!":
            call gas_saleswoman_dialogue2_getout4()
            return
    label gas_saleswoman_dialogue2_l4:


    img 4481
    saleswoman "Да..."

    img 4480
    fred "Тогда снимите их!"

    img 4482
    saleswoman "Мистер Фред, вы знаете, у меня есть парень и... "
    img 4483
    "я немного стесняюсь и..."

    img 4484
    fred "Кристина! Если Вы хотите эту работу, то Вам придется быть смелой!"
    "Вы ведь хотите ее?"

    img 4485
    saleswoman "Да..."

    saleswoman "А Вы обещаете что возьмете меня?"
    saleswoman "И сделаете другое о чем говорили..."

    img 4486
    fred "Да, Кристина!"
    #
    if gasStationMonicaLied == True:
        "Три пункта!"
        "Ваш Босс позвонит Вам и извинится за то что несправедливо наказал Вас!"
        "Моника Бакфетт запросит реквизиты на оплату за разбитую бутылку!"
    #
    else:
        "Два пункта!"
        "Ваш Босс позвонит Вам и извинится за то что несправедливо наказал Вас!"

    "И Вы будете приняты на работу в качестве Топ Модели!"

    img 4487
    "Я не обещаю что Вы сможете стать самой высокооплачиваемой моделью в первый же день."
    "Но, если я прав и вы правда везде также красивы, то я уверен что Вы станете ей очень быстро!"

    img 4486
    fred "Взамен я хочу оценить Вас, чтобы я знал что я не рискую своей репутацией."
    "Вы должны понимать меня, Кристина."
    "Вы ведь умная девушка? Правда?"

    menu:
        "Да, я умная. И красивая...":
            jump gas_saleswoman_dialogue2_l5
        "Я умная и не поведусь на этот блеф!":
            call gas_saleswoman_dialogue2_getout5()
            return
    label gas_saleswoman_dialogue2_l5:

    img 4488
    saleswoman "Да, я умная."
    img 4489
    "И красивая."
    img 4490
    saleswoman "(кристина, ты умная, ты правда пойдешь показывать свое тело полузнакомому человеку прямо в туалете на работе?)"
    img 4491
    saleswoman "(но он обещает такие вещи...)"
    img 4492
    "(хотя это не будет правильным по отношению к моему любимому...)"
    img 4493
    "(правда он ведь не узнает...)"
    img 4494
    "(и я так возбуждена, я не могу устоять от соблазна показать свое восхитительно тело кому-то...)"
    img 4495
    "(в конце концов, мой любимый не устроит меня на такую работу!)"
    img 4496
    "(этот мистер фред может это! и он заслуживает того чтобы насладиться зрелищем моего обнаженного тела)"
    img 4497
    "(я и так хотела пойти на перерыв, чтобы закончить то что начала сегодня днем)"
    "(это будет маленьким приключением, вполне безобидным!)"
    "(а когда он уйдет, я закончу то что начала)"
    img 4498
    "(я достану своего любимого огромного друга и... ммммм.....)"
    img 4499
    fred "Хорошо, тогда мы заключили сделку?"

    img 4500
    saleswoman "Да, Мистер Фред.
    Пожалуйста, закройте дверь, чтобы посетители не побеспокоили нас."
    "И подождите пару минут, мне надо раздеться и приготовиться к кастингу."

    img 4501
    fred "Кристина, конечно!
    Вам предстоит очень ответственный кастинг!"
    img 4502
    "Так что готовьтесь к нему как следует!"
    call change_scene("gas_station_view_door_scene1", "Fade_long", "snd_door_close1")
    return


label gas_station_view_door_scene1:
    $ print "enter_gas_station_view_door_scene1"

    $ scene_name = "gas_station_view_door_scene1"
    $ scene_caption = _("Gas Station")
    $ clear_scene_from_objects(scene_name)

    $ scene_image = "scene_Gas_Station_View_Door"

    $ add_object_to_scene("Door", {"type":2, "base":"Gas_Station_View_Door_Door", "click" : "gas_station_view_door_scene1_environment", "actions" : "lh", "zorder" : 0})


    return
label gas_station_view_door_scene1_environment(obj_name, obj_data):
    if obj_name == "Door":
        if obj_data["action"] == "l":
            $ gas_saleswoman_dialogue2_flag1_viewed = True
            fred "Юная модель ушла туда..."
            "Мне кажется она уже готова к кастингу!"
        if obj_data["action"] == "h":
            if gas_saleswoman_dialogue2_flag1_viewed == False:
                fred "Юная модель ушла туда..."
                "Мне кажется она уже готова к кастингу!"
            call gas_saleswoman_dialogue2_2()

    return


label gas_saleswoman_dialogue2_2:
    #.... в туалете
    music Loved_up2
    img 4575
    with fadelong
    w
    img 4576
    saleswoman "Надо раздеться..."
    img 4577
    saleswoman "Моя грудь..."
    img 4578
    "О Боже!
    Как же я возбуждена!"

    img 4579
    saleswoman "Снять... скорее..."
    img 4580
    w
    img 4581
    w
    img 4582
    saleswoman "Я не могу удержаться... не могу..."
    img 4583
    w
    img 4584
    saleswoman "Ахххххх..."
    img 4585
    w
    img 4586
    "Если честно, я не могу справиться с собой!
    Наверное мне не следовало соглашаться."
    img 4587
    "Ведь я не хочу кончить прямо посреди кастинга перед таким влиятельным человеком!?"

    img 4588
    "О Боже!
    Я не могу... не могу сосредоточиться..."
    img 4589
    "Нет!
    Я передумала!"

    img 4590
    "Я откажусь!"

    img 4591
    "Пусть он уйдет, скорее!"

    img 4592
    "Где мой большой мужчина?"
    img 4593
    "Самый большой! Я соврала, он больше чем у моего любимого!"
    "Мне так понравилось какой он большой! Аххххх!"
    img 4594
    "Где он???"
    "Аххххххх!!!"
    img 4595
    "Ну где же он? Где???"
    img 4596
    "Куда я его спрятала??? Ааааааа!!!"
    music Hidden_Agenda
    img 4597
    "Ахххх!! Кто это??"
    img 4598
    "Мистер Фред??"

    img 4599
    "Мистер Фред! Я..."
    "Я решила отказаться, я сегодня не могу!!!"
    img 4600
    "У меня вдруг очень заболела голова и...."
    img 4601
    fred "Кристина, смотрите что я нашел у Вас за прилавком!"
    music Turbo_Tornado
    img 4602
    "Это не ваше?"
    img 4603
    saleswoman "О БОЖЕ!!! ЧТО ЭТО????"

    fred "Где?"

    img 4604
    saleswoman "ВОТ ЭТО!!!"
    img 4605
    "ЧТО ЭТО ЗА МОНСТР!!!"
    img 4606
    fred "Кристина! Это инструмент оценки!"
    "Ему предстоит оценить все Ваши достоинства и вынести вердикт о профессиональной принадлежности!"

    img 4607
    saleswoman "Я не могу смотреть на это!"
    img 4608
    fred "О! Кристина!"
    img 4609
    "Мы уже приступаем?"
    "Отличная киска!"
    img 4610
    "Давайте начнем собеседование с нее!"
    img 4611
    saleswoman "НЕТ!!!"
    img 4612
    "ОН НЕ ВЛЕЗЕТ!!!"
    img 4613
    saleswoman "ААААААА!!!!"
    img 4614
    saleswoman "ААААААААА!!!!"
    img 4615
    saleswoman "ААААААААА!!!!"

    img 4616
    w
    img 4617
    saleswoman "ААААААААА!!!!"

    scene black
    image videoGas_Girl_Fred_Sex1_1 = Movie(play="video/Gas_Girl_Fred_Sex1_1.mp4", fps=30)
    show videoGas_Girl_Fred_Sex1_1
    wclean
    scene black
    image videoGas_Girl_Fred_Sex1_2 = Movie(play="video/Gas_Girl_Fred_Sex1_2.mp4", fps=30)
    show videoGas_Girl_Fred_Sex1_2
    wclean
    scene black
    image videoGas_Girl_Fred_Sex1_3 = Movie(play="video/Gas_Girl_Fred_Sex1_3.mp4", fps=30)
    show videoGas_Girl_Fred_Sex1_3
    wclean
    scene black
    image videoGas_Girl_Fred_Sex1_4 = Movie(play="video/Gas_Girl_Fred_Sex1_4.mp4", fps=30)
    show videoGas_Girl_Fred_Sex1_4
    wclean
    scene black
    image videoGas_Girl_Fred_Sex1_5 = Movie(play="video/Gas_Girl_Fred_Sex1_5.mp4", fps=30)
    show videoGas_Girl_Fred_Sex1_5
    wclean
    scene black
    image videoGas_Girl_Fred_Sex1_6 = Movie(play="video/Gas_Girl_Fred_Sex1_6.mp4", fps=30)
    show videoGas_Girl_Fred_Sex1_6
    wclean
    scene black
    image videoGas_Girl_Fred_Sex1_7 = Movie(play="video/Gas_Girl_Fred_Sex1_7.mp4", fps=30)
    show videoGas_Girl_Fred_Sex1_7
    wclean
    scene black
    image videoGas_Girl_Fred_Sex1_8 = Movie(play="video/Gas_Girl_Fred_Sex1_8.mp4", fps=30)
    show videoGas_Girl_Fred_Sex1_8
    wclean
    scene black
    image videoGas_Girl_Fred_Sex1_9 = Movie(play="video/Gas_Girl_Fred_Sex1_9.mp4", fps=30)
    show videoGas_Girl_Fred_Sex1_9
    wclean
    scene black
    image videoGas_Girl_Fred_Sex1_10 = Movie(play="video/Gas_Girl_Fred_Sex1_10.mp4", fps=30)
    show videoGas_Girl_Fred_Sex1_10
    wclean
    scene black
    image videoGas_Girl_Fred_Sex1_11 = Movie(play="video/Gas_Girl_Fred_Sex1_11.mp4", fps=30)
    show videoGas_Girl_Fred_Sex1_11
    wclean
    scene black
    image videoGas_Girl_Fred_Sex1_12 = Movie(play="video/Gas_Girl_Fred_Sex1_12.mp4", fps=30)
    show videoGas_Girl_Fred_Sex1_12
    wclean
    scene black
    image videoGas_Girl_Fred_Sex1_13 = Movie(play="video/Gas_Girl_Fred_Sex1_13.mp4", fps=30)
    show videoGas_Girl_Fred_Sex1_13
    wclean
    scene black
    image videoGas_Girl_Fred_Sex1_14 = Movie(play="video/Gas_Girl_Fred_Sex1_14.mp4", fps=30)
    show videoGas_Girl_Fred_Sex1_14
    wclean

    img 4618
    fred "Расслабьтесь, Кристина! Это всего-лишь собеседование!"

    scene black
    image videoGas_Girl_Fred_Sex2_1 = Movie(play="video/Gas_Girl_Fred_Sex2_1.mp4", fps=30)
    show videoGas_Girl_Fred_Sex2_1
    wclean
    scene black
    image videoGas_Girl_Fred_Sex2_2 = Movie(play="video/Gas_Girl_Fred_Sex2_2.mp4", fps=30)
    show videoGas_Girl_Fred_Sex2_2
    wclean
    scene black
    image videoGas_Girl_Fred_Sex2_3 = Movie(play="video/Gas_Girl_Fred_Sex2_3.mp4", fps=30)
    show videoGas_Girl_Fred_Sex2_3
    wclean
    scene black
    image videoGas_Girl_Fred_Sex2_4 = Movie(play="video/Gas_Girl_Fred_Sex2_4.mp4", fps=30)
    show videoGas_Girl_Fred_Sex2_4
    wclean
    scene black
    image videoGas_Girl_Fred_Sex2_5 = Movie(play="video/Gas_Girl_Fred_Sex2_5.mp4", fps=30)
    show videoGas_Girl_Fred_Sex2_5
    wclean
    scene black
    image videoGas_Girl_Fred_Sex2_6 = Movie(play="video/Gas_Girl_Fred_Sex2_6.mp4", fps=30)
    show videoGas_Girl_Fred_Sex2_6
    wclean
    scene black
    image videoGas_Girl_Fred_Sex2_7 = Movie(play="video/Gas_Girl_Fred_Sex2_7.mp4", fps=30)
    show videoGas_Girl_Fred_Sex2_7
    wclean
    scene black
    image videoGas_Girl_Fred_Sex2_9 = Movie(play="video/Gas_Girl_Fred_Sex2_9.mp4", fps=30)
    show videoGas_Girl_Fred_Sex2_9
    wclean
    scene black
    image videoGas_Girl_Fred_Sex2_10 = Movie(play="video/Gas_Girl_Fred_Sex2_10.mp4", fps=30)
    show videoGas_Girl_Fred_Sex2_10
    wclean
    scene black
    image videoGas_Girl_Fred_Sex2_11 = Movie(play="video/Gas_Girl_Fred_Sex2_11.mp4", fps=30)
    show videoGas_Girl_Fred_Sex2_11
    wclean
    scene black
    image videoGas_Girl_Fred_Sex2_12 = Movie(play="video/Gas_Girl_Fred_Sex2_12.mp4", fps=30)
    show videoGas_Girl_Fred_Sex2_12
    wclean
    scene black
    image videoGas_Girl_Fred_Sex2_13 = Movie(play="video/Gas_Girl_Fred_Sex2_13.mp4", fps=30)
    show videoGas_Girl_Fred_Sex2_13
    wclean
    scene black
    image videoGas_Girl_Fred_Sex2_14 = Movie(play="video/Gas_Girl_Fred_Sex2_14.mp4", fps=30)
    show videoGas_Girl_Fred_Sex2_14
    wclean
    scene black
    image videoGas_Girl_Fred_Sex2_15 = Movie(play="video/Gas_Girl_Fred_Sex2_15.mp4", fps=30)
    show videoGas_Girl_Fred_Sex2_15
    wclean
    scene black
    image videoGas_Girl_Fred_Sex2_16 = Movie(play="video/Gas_Girl_Fred_Sex2_16.mp4", fps=30)
    show videoGas_Girl_Fred_Sex2_16
    wclean
    scene black
    image videoGas_Girl_Fred_Sex2_17 = Movie(play="video/Gas_Girl_Fred_Sex2_17.mp4", fps=30)
    show videoGas_Girl_Fred_Sex2_17
    wclean

    $ christineFuckedByFred = True
    #video
    #video

    img 4619
    fred "ААААГГГХХХ!"
    img 4620
    saleswoman "Вы кончили в меня?????!!!"
    img 4621
    fred "ААААГГГХХХ!"
    img 4622
    fred "Начало неплохое, Кристина.
    Давайте продолжим!"
    img 4623
    saleswoman "Мистер Фффред...
    Я...."
    img 4624
    saleswoman "Я ничего не чувствую там..."
    "У меня дрожат ноги..."
    img 4625
    saleswoman "Они подгибаются..."
    sound snd_bodyfall
    img 4626
    w
    img 4627
    saleswoman "Я...."
    img 4628
    saleswoman "Я не могу встать..."
    img 4631
    fred "Всего-лишь небольшая зарядка для ног."
    fred "Кристина, вы готовы продолжить собеседование?"
    saleswoman "Я... я не могу, мне никак!"
    img 4632
    fred "Кристина, вы хотите стать топ моделью? Или нет?"
    menu:
        "Да, хочу...":
            jump gas_saleswoman_dialogue2_2_l1
        "Только не так!":
            call gas_saleswoman_dialogue2_2_out()
            return
    label gas_saleswoman_dialogue2_2_l1:
    saleswoman "Да, хочу..."
    img 4633
    fred "Кристина, вы ОЧЕНЬ хотите стать топ моделью??!"
    menu:
        "Да, я очень хочу...":
            pass
    saleswoman "Да, я очень хочу..."
    fred "Я помогу вам, Кристина! Идите сюда!"
    "Я оценю ваше красноречие."
    img 4634
    saleswoman "ААААААААА!!!!"
    "Мммпфффххххх..."
    $ christineFuckedByFredBlowjob = True
#    call GasStation_Saleswoman2_Video_Blowjob()
    #video
    scene black
    image videoGas_Girl_Fred_Blowjob1_1 = Movie(play="video/Gas_Girl_Fred_Blowjob1_1.mp4", fps=30)
    show videoGas_Girl_Fred_Blowjob1_1
    wclean
    scene black
    image videoGas_Girl_Fred_Blowjob1_2 = Movie(play="video/Gas_Girl_Fred_Blowjob1_2.mp4", fps=30)
    show videoGas_Girl_Fred_Blowjob1_2
    wclean
    scene black
    image videoGas_Girl_Fred_Blowjob1_3 = Movie(play="video/Gas_Girl_Fred_Blowjob1_3.mp4", fps=30)
    show videoGas_Girl_Fred_Blowjob1_3
    wclean
    scene black
    image videoGas_Girl_Fred_Blowjob1_4 = Movie(play="video/Gas_Girl_Fred_Blowjob1_4.mp4", fps=30)
    show videoGas_Girl_Fred_Blowjob1_4
    wclean
    scene black
    image videoGas_Girl_Fred_Blowjob1_5 = Movie(play="video/Gas_Girl_Fred_Blowjob1_5.mp4", fps=30)
    show videoGas_Girl_Fred_Blowjob1_5
    wclean
    img 4635
    fred "К вершине каръеры лежит непростой путь..."
    img 4636
    fred "Я помогаю вам пройти его!"
    img 4637
    w
    scene black
    image videoGas_Girl_Fred_Blowjob1_6 = Movie(play="video/Gas_Girl_Fred_Blowjob1_6.mp4", fps=30)
    show videoGas_Girl_Fred_Blowjob1_6
    wclean
    scene black
    image videoGas_Girl_Fred_Blowjob1_7 = Movie(play="video/Gas_Girl_Fred_Blowjob1_7.mp4", fps=30)
    show videoGas_Girl_Fred_Blowjob1_7
    wclean
    scene black
    image videoGas_Girl_Fred_Blowjob1_8 = Movie(play="video/Gas_Girl_Fred_Blowjob1_8.mp4", fps=30)
    show videoGas_Girl_Fred_Blowjob1_8
    wclean
    scene black
    image videoGas_Girl_Fred_Blowjob1_9 = Movie(play="video/Gas_Girl_Fred_Blowjob1_9.mp4", fps=30)
    show videoGas_Girl_Fred_Blowjob1_9
    wclean
    scene black
    image videoGas_Girl_Fred_Blowjob1_10 = Movie(play="video/Gas_Girl_Fred_Blowjob1_10.mp4", fps=30)
    show videoGas_Girl_Fred_Blowjob1_10
    wclean
    scene black
    image videoGas_Girl_Fred_Blowjob1_11 = Movie(play="video/Gas_Girl_Fred_Blowjob1_11.mp4", fps=30)
    show videoGas_Girl_Fred_Blowjob1_11
    wclean
    scene black
    image videoGas_Girl_Fred_Blowjob1_12 = Movie(play="video/Gas_Girl_Fred_Blowjob1_12.mp4", fps=30)
    show videoGas_Girl_Fred_Blowjob1_12
    wclean
    scene black
    image videoGas_Girl_Fred_Blowjob1_13 = Movie(play="video/Gas_Girl_Fred_Blowjob1_13.mp4", fps=30)
    show videoGas_Girl_Fred_Blowjob1_13
    wclean
    scene black
    image videoGas_Girl_Fred_Blowjob1_15 = Movie(play="video/Gas_Girl_Fred_Blowjob1_15.mp4", fps=30)
    show videoGas_Girl_Fred_Blowjob1_15
    wclean
    scene black
    image videoGas_Girl_Fred_Blowjob1_16 = Movie(play="video/Gas_Girl_Fred_Blowjob1_16.mp4", fps=30)
    show videoGas_Girl_Fred_Blowjob1_16
    wclean
    scene black
    image videoGas_Girl_Fred_Blowjob1_17 = Movie(play="video/Gas_Girl_Fred_Blowjob1_17.mp4", fps=30)
    show videoGas_Girl_Fred_Blowjob1_17
    wclean
    scene black
    image videoGas_Girl_Fred_Blowjob1_18 = Movie(play="video/Gas_Girl_Fred_Blowjob1_18.mp4", fps=30)
    show videoGas_Girl_Fred_Blowjob1_18
    wclean


    img 4638
    fred "ААААГГГХХХ!"
    saleswoman "ААААААААА!!!!"
    img 4639
    saleswoman "Говорит неразборчиво"
    "Мой... рот..."
    img 4640
    "У меня свело... не закрыть..."
    img 4641
    saleswoman "Ноги... не держат..."
    sound snd_bodyfall
    img 4642
    w
    fred "Кристина, вы точно очень хотите стать топ моделью?"

    img 4643
    menu:
        "Очччень.. ххооочу...":
            jump gas_saleswoman_dialogue2_2_l2
        "Без сознания...":
            call gas_saleswoman_dialogue2_2_out2()
            return
    label gas_saleswoman_dialogue2_2_l2:
    saleswoman "Очччень.. ххооочу..."
    img 4644
    fred "Кристина! Я хочу помочь вам!"
    img 4645
    fred "Но пока собеседование не показало каких-то выдающихся талантов."
    img 4646
    fred "Может быть у вас есть еще какие-то достоинства о которых вы не упоминали?"
    img 4647
    with fade
    fred "Точно!
    Кристина!"
    "Вы излишне скромны!"
    "Вам надо было сразу упомянуть о самом главном!"
    img 4648
    fred "Я помогу вам раскрыть таланты!"
    img 4649
    fred "Достичь вершины каръеры топ модели!"
    img 4650
    fred "Сейчас я поделюсь еще немного своим опытом!"
    img 4651
    saleswoman "ААААААААА!!!!"
    saleswoman "НЕЕЕЕЕЕТ!!!!"
    "ТОЛЬКО НЕ ТУДА!!!!"
    img 4652
    saleswoman "ААААААААА!!!!"

    $ christineFuckedByFredAnal = True
    #video
    scene black
    image videoGas_Girl_Fred_Anal1_1 = Movie(play="video/Gas_Girl_Fred_Anal1_1.mp4", fps=30)
    show videoGas_Girl_Fred_Anal1_1
    wclean
    scene black
    image videoGas_Girl_Fred_Anal1_2 = Movie(play="video/Gas_Girl_Fred_Anal1_2.mp4", fps=30)
    show videoGas_Girl_Fred_Anal1_2
    wclean
    scene black
    image videoGas_Girl_Fred_Anal1_4 = Movie(play="video/Gas_Girl_Fred_Anal1_4.mp4", fps=30)
    show videoGas_Girl_Fred_Anal1_4
    wclean
    scene black
    image videoGas_Girl_Fred_Anal1_7 = Movie(play="video/Gas_Girl_Fred_Anal1_7.mp4", fps=30)
    show videoGas_Girl_Fred_Anal1_7
    wclean
    scene black
    image videoGas_Girl_Fred_Anal1_11 = Movie(play="video/Gas_Girl_Fred_Anal1_11.mp4", fps=30)
    show videoGas_Girl_Fred_Anal1_11
    wclean
    scene black
    image videoGas_Girl_Fred_Anal1_14 = Movie(play="video/Gas_Girl_Fred_Anal1_14.mp4", fps=30)
    show videoGas_Girl_Fred_Anal1_14
    wclean
    scene black
    image videoGas_Girl_Fred_Anal1_15 = Movie(play="video/Gas_Girl_Fred_Anal1_15.mp4", fps=30)
    show videoGas_Girl_Fred_Anal1_15
    wclean


    call GasStation_Saleswoman2_Video_Anal()
    w
    img 4653
    fred "Оооо! Кристина!"
    "Чувствуете мой опыт?"
    "Я передаю его вам, щедро!"
    img 4654
    w
    img 4655
    fred "У меня осталось еще немного чем поделиться с вами, Кристина!"
    img 4656
    fred "Вот так! Собеседование прошло отлично!"
    "У вас есть вопросы ко мне?"
    saleswoman "Яяяя... пппррринята?"
    img 4658
    fred "О! Кристина!"
    "Не стоит торопиться. Мы с вами прошли только предварительное собеседование!"
    img 4659
    fred "Спасибо за уделенное время!"
    "Мы свяжемся с вами!"

    img 4660
    with fadelong
    w
    img 4661
    with fade
    w
    img 4662
    with fade
    w
    img 4663
    with fade
    w
    img 4664
    with fade
    w
    img 4665
    with fade
    w
    img 4666
    with fade
    w
    img 4667
    with fade
    w
    img 4668
    with fade
    w
    img 4669
    with fade
    w
    call gas_saleswoman_dialogue2_end()
    return

label gas_saleswoman_dialogue2_alternative():
    music Hidden_Agenda
    call textonblack(_("ТЕМ ВРЕМЕНЕМ..."))
    img black_screen
    with Dissolve(1)
#    music Groove2_85
    img 4687
    with fadelong
    sound snd_car_door
    $ renpy.pause(1)
    sound snd_car_turn_on
    img 4688
    with fade
    $ renpy.pause(3)
    sound snd_car_engine
    img scene_Street_Gas_Station_Driver_Monica_EveningDress_Evening
    with fadelong
    $ renpy.pause(1)
    sound man_steps
    img scene_Street_Gas_Station_Car_NoDriver_Evening
    with Dissolve(1)
    $ renpy.pause(1)

    img 4373
    with fadelong
    saleswoman "Здравствуйте, Мистер."
    "Прошу прощения, но компьютер так и не работает, так что если вы хотели заправиться, то..."

    img 4374
    fred "Здравствуйте, юная леди.
    Я приехал по другому вопросу."

    img 4375
    saleswoman "По какому?"

    img 4376
    fred "Вы, наверное, очень устали за сегодня.
    Вы работали весь день без отдыха."

    "Ваша смена, должно быть, уже давно закончена.
    Почему вы на работе?"

    img 4377
    saleswoman "Почему вас это интересует?
    Какое вам дело до этого?"

    img 4378
    fred "Ну как же, такая красивая и очаровательная девушка."
    "Вы не созданы для такой тяжелой и долгой работы..."

    img 4504
    saleswoman "Я нахожусь на рабочем месте!"
    saleswoman "Мне не нужны ваши комплименты!"
    "У меня есть парень!"
    "Если вы ничего не будете покупать, то прошу не отвлекать меня!"
    img 4505
    fred "Хорошо, юная леди.
    Мы скоро увидимся!"
    img 4504
    saleswoman "Очередной прилипала!"
    img 4506
    saleswoman "Он назвал меня красивой?"
    img 4507
    saleswoman "Да, я красивая..."
    saleswoman "Я так и не успела расслабиться в прошлый раз..."
    img 4508
    saleswoman "Может стоит сделать перерыв?"
    img 4509
    saleswoman "Всего пару минут!"
    img 4510
    saleswoman "Хммм... На чем мы остановились?"
    img 4511
    saleswoman "Где там наш огромный мужчина?"
    img 4512
    w
    img 4513
    saleswoman "Ага! Вот он!"
    music Loved_up2
    img 4514
    saleswoman "ММммммммнн..."
    img 4515
    saleswoman "ММммммммнн..."
    img 4516
    w
    img 4517 #
    saleswoman "Ахххххх..."
    img 4518
    w
    img 4519
    w
    img 4520
    saleswoman "Ахххххх..."
    img 4521
    saleswoman "Ааааа..."
    img 4522
    w
    img 4523
    saleswoman "ММммннннн..."
    img 4524
    w
    img 4525
    w
    img 4526
    w
    img 4527
    w
    img 4528
    w
    img 4529
    saleswoman "ММммннннн..."
    img 4530
    w
    img 4531
    saleswoman "Ааааа..."
    img 4532
    w
    sound snd_fabric1
    img 4533
    with fadelong
    saleswoman "Ахххххх..."
    img 4534
    w
    img 4535
    saleswoman "Ахххххх..."
    img 4536
    w
    img 4537
    w
    img 4538
    saleswoman "Ааааа..."
    img 4539
    w
    sound snd_fabric1
    img 4540
    with fadelong
    saleswoman "Ахххххх..."
    img 4541
    w
    img 4542
    w
    img 4543
    w
    img 4544
    w
    img 4545
    w
    img 4546
    w
    img 4547
    w
    img 4548
    saleswoman "Ааааа..."
    img 4549
    w
    img 4550
    w
    img 4551
    w
    img 4552
    saleswoman "Ааааа..."
    img 4553
    w
    sound snd_fabric1
    img 4554
    with fadelong
    saleswoman "ММммннннн..."
    img 4555
    w
    img 4556
    w
    img 4557
    w
    img 4558
    w
    img 4559
    saleswoman "Ааааа..."
    img 4560
    w
    img 4561
    w
    img 4562
    w
    img 4563
    saleswoman "Еще..."
    img 4564
    w
    img 4565
    saleswoman "Вот так..."
    img 4566
    w
    img 4567
    with fade
    saleswoman "Ахххххх..."
    scene black
    image videoGas_Girl_Masturbation2_1 = Movie(play="video/Gas_Girl_Masturbation2_1.mp4", fps=30)
    show videoGas_Girl_Masturbation2_1
    wclean
    scene black
    image videoGas_Girl_Masturbation2_2 = Movie(play="video/Gas_Girl_Masturbation2_2.mp4", fps=30)
    show videoGas_Girl_Masturbation2_2
    wclean
    scene black
    image videoGas_Girl_Masturbation2_3 = Movie(play="video/Gas_Girl_Masturbation2_3.mp4", fps=30)
    show videoGas_Girl_Masturbation2_3
    wclean
    scene black
    image videoGas_Girl_Masturbation2_4 = Movie(play="video/Gas_Girl_Masturbation2_4.mp4", fps=30)
    show videoGas_Girl_Masturbation2_4
    wclean
    scene black
    image videoGas_Girl_Masturbation2_5 = Movie(play="video/Gas_Girl_Masturbation2_5.mp4", fps=30)
    show videoGas_Girl_Masturbation2_5
    wclean
    scene black
    image videoGas_Girl_Masturbation2_6 = Movie(play="video/Gas_Girl_Masturbation2_6.mp4", fps=30)
    show videoGas_Girl_Masturbation2_6
    wclean
    scene black
    image videoGas_Girl_Masturbation2_7 = Movie(play="video/Gas_Girl_Masturbation2_7.mp4", fps=30)
    show videoGas_Girl_Masturbation2_7
    wclean
    scene black
    image videoGas_Girl_Masturbation2_8 = Movie(play="video/Gas_Girl_Masturbation2_8.mp4", fps=30)
    show videoGas_Girl_Masturbation2_8
    wclean
    scene black
    image videoGas_Girl_Masturbation2_9 = Movie(play="video/Gas_Girl_Masturbation2_9.mp4", fps=30)
    show videoGas_Girl_Masturbation2_9
    wclean
    scene black
    image videoGas_Girl_Masturbation2_10 = Movie(play="video/Gas_Girl_Masturbation2_10.mp4", fps=30)
    show videoGas_Girl_Masturbation2_10
    wclean
    scene black
    image videoGas_Girl_Masturbation2_11 = Movie(play="video/Gas_Girl_Masturbation2_11.mp4", fps=30)
    show videoGas_Girl_Masturbation2_11
    wclean
    scene black
    image videoGas_Girl_Masturbation2_12 = Movie(play="video/Gas_Girl_Masturbation2_12.mp4", fps=30)
    show videoGas_Girl_Masturbation2_12
    wclean
    scene black
    image videoGas_Girl_Masturbation2_13 = Movie(play="video/Gas_Girl_Masturbation2_13.mp4", fps=30)
    show videoGas_Girl_Masturbation2_13
    wclean
    scene black
    image videoGas_Girl_Masturbation2_14 = Movie(play="video/Gas_Girl_Masturbation2_14.mp4", fps=30)
    show videoGas_Girl_Masturbation2_14
    wclean
    scene black
    image videoGas_Girl_Masturbation2_15 = Movie(play="video/Gas_Girl_Masturbation2_15.mp4", fps=30)
    show videoGas_Girl_Masturbation2_15
    wclean
    img 4568
    saleswoman "О Боже! Как хорошо!"
    saleswoman "Я кончаю!"
    img 4569
    w
    img 4570
    with fade
    w
    img 4571
    with fade
    w
    img 4572
    with fade
    w
    img 4573
    with fade
    w
    img 4574
    with fade
    w
    call gas_saleswoman_dialogue2_end()
    return

label gas_saleswoman_dialogue2_getout1:
    #отшивает вначале
    img 4504
    saleswoman "Мне не нужны ваши комплименты!"
    "У меня есть парень!"
    "Если вы ничего не будете покупать, то прошу не отвлекать меня!"
    img 4505
    fred "Хорошо, юная леди.
    Мы скоро увидимся!"
    call gas_saleswoman_dialogue2_end()
    return

label gas_saleswoman_dialogue2_getout2:
    img 4504
    saleswoman "Предложение работы от первого встречного?"
    "Это все очень подозрительно."
    "Вообще-то..."
    "У меня есть парень!"
    "И он бы не одобрил это!"
    "Если вы ничего не будете покупать, то прошу не отвлекать меня!"
    img 4505
    fred "Хорошо, юная леди.
    Мы скоро увидимся!"
    call gas_saleswoman_dialogue2_end()
    return


label gas_saleswoman_dialogue2_getout3:
    img 4504
    saleswoman "Мне он тоже нравится, но я вам не верю!":
    "Если вы ничего не будете покупать, то прошу не отвлекать меня!"
    img 4505
    fred "Хорошо, юная леди.
    Мы скоро увидимся!"
    call gas_saleswoman_dialogue2_end()
    return

label gas_saleswoman_dialogue2_getout4:
    img 4503
    saleswoman "У меня красивые трусики и они нравятся моему парню!"
    "Если вы ничего не будете покупать, то прошу не отвлекать меня!"
    img 4505
    fred "Хорошо, юная леди.
    Мы скоро увидимся!"
    call gas_saleswoman_dialogue2_end()
    return
label gas_saleswoman_dialogue2_getout5:
    img 4503
    saleswoman "Я умная и не поведусь на этот блеф!"
    "Если вы ничего не будете покупать, то прошу не отвлекать меня!"
    img 4505
    fred "Хорошо, юная леди.
    Мы скоро увидимся!"
    call gas_saleswoman_dialogue2_end()
    return


label gas_saleswoman_dialogue2_2_out:
    stop music fadeout 3.0
    scene black_screen
    with Dissolve(2)
    call gas_saleswoman_dialogue2_end()
    return
label gas_saleswoman_dialogue2_2_out2:
    stop music fadeout 3.0
    scene black_screen
    with Dissolve(2)
    call gas_saleswoman_dialogue2_end()
    return
label gas_saleswoman_dialogue2_end:
    stop music fadeout 3.0
    call quest_house_monica_day2_day_init()
    return

label GasStation_Saleswoman2_Video_Blowjob():
    return
label GasStation_Saleswoman2_Video_Anal():
    return
