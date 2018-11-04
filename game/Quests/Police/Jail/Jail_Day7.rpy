label jail_day7:
    $ jailDay = 7
    $ day = day + 1
    $ jailDaySceneStage = 0
    $ jailScenePlace = 0
    $ policeCellStageName1 = "scene_Police_Cell_1_Day_7_1"
    $ policeCellStageName2 = "scene_Police_Cell_2_Day_6_2"
    $ policeCellMonica1 = "Police_Cell_1_Day_7_1"
    $ policeCellMonica2 = "Police_Cell_2_Day_6_2"
    $ policeCellMonicaLabel = "jail_day7_Monica"
    $ policeCellBedLabel = "jail_day7_Bed"
    $ policeCellCageLabel = "jail_day7_Cage"
    stop music fadeout 1.0
    call textonblack(_("ДЕНЬ 7"))
    img black_screen
    with Dissolve(1)
    music Jail_Clock

    img 2343
    with fadelong
    mt "Значит этот урод не хочет бегать из-за каких-то тряпок..."
    img 2344
    mt "Он тупой, это понятно."
    mt "Но он говорил про то что ниже его не понизят..."
    img 2345
    mt "Значит он понимает что находится на дне карьеры."
    "Если он об этом сказал, значит его это не устраивает..."
    img 2346
    mt "Может быть я могла бы сделать ему предложение..."
    "Изменить его жизнь..."
    "Надо попробовать!"
    img 2347
    mt "Главное как-то выбраться отсюда!"
    "На свободе я быстро решу все свои проблемы!"
    img 2348
    mt "И вскоре снова начну сниматься для журнала!"
    "Я уверена!"
    "Итак..."
    call refresh_scene_fade()
    return

label jail_day7_Monica(obj_name, obj_data):
    if jailDaySceneStage == 0:
        mt "У меня есть идея! Надо позвать этого урода!"
    if jailDaySceneStage == 1:
        mt "Кажется у меня что-то наклевывается."
    return

label jail_day7_Bed(obj_name, obj_data):
    if act == "l":
        call jail_day1_Bed(obj_name, obj_data)
        return

    if jailDaySceneStage == 0:
        mt "Некогда спать!"


    if jailDaySceneStage == 1:
        menu:
            "Лечь спать":
                pass
            "Не ложиться":
                return
        call jail_day8()
    return

label jail_day7_Cage(obj_name, obj_data):
    if act == "l":
        call jail_cage()
        call refresh_scene_fade()
        return
    if act == "w":
        $ cageInteractLabel = "jail_day7_Cage_Interact"
        call change_scene("police_jail_cage_scene")
        return

    return

label jail_day7_Cage_Interact:
    if jailDaySceneStage == 0:

        music Groove2_85
        # подходит
        img 2349
        with fadelong
        overseer "Жрать?"
        m "Да, Сэр."
        if jailBoobsForFood == True:
            overseer "..."
            m "..."
            overseer "..."
            img 5190
            m "Что? Снова?!?!"
            img 5191
            m "Что ВАМ надо снова???"
            img 5192
            overseer "Сиськи..."
            menu:
                "Сказать как его зовут." if monicaKnowOverseerName == True:
                    call jail_boobs_for_food_end()
                "Показать грудь.":
                    # показывает грудь
                    call jail_boobs_for_food()
                "Не показывать.":
                    m "Я не хочу показывать свою грудь..."
                    img 5173
                    overseer "Нет вежливости, нет сисек, нет еды..."
                    img 5116
                    w
                    # уходит
                    music Jail_Clock
                    call refresh_scene_fade()
                    return
        # уходит за едой
        img 5116
        with fade
        w
        img black_screen
        with Dissolve(1)
        img 5118
        with fadelong
        w
        img 2349
        overseer "На."
        $ jailFoodInteractLabel = "jail_day7_1a"
        call change_scene("police_jail_food_scene", "Fade", False)

    if jailDaySceneStage == 1:
        img 2253
        with fadelong
        mt "Он не подходит."
        "Может быть он вообще ушел?"
        "Мне не видно отсюда!"
        if jailBoobsForFoodShowed == True:
            call jail_cage()
            return
        return

    return

label jail_day7_1a:

    music Groove2_85
    img 2350
    m "Спасибо, Сэр!"
    overseer "..."

    music Hidden_Agenda
    m "Сэр?"
    overseer "Ну что тебе?"

    m "Я бы хотела с Вами поговорить о Вашей карьере."
    overseer "О чем?"
    m "Сэр."
    "Вы такой красивый, умный!"
    img 2351
    overseer "Да, я хорош!"
    img 2352
    mt "Урод!!!"
    "Ненавижу!!!"
    img 2353
    with fade
    m "Сэр."
    "Я считаю что Вы заслуживаете гораздо большего, нежели работа здесь."
    img 2354
    overseer "Я тоже так думаю."
    "Я всем и говорил, а они..."
    img 2355
    m "Сэр."
    "Хотели бы Вы иметь свой огромный дом."
    "Отдыхать на Бора-Бора."
    "Иметь красивую машину."

    img 2356
    m "И никогда не ходить на работу?"
    img 2354
    overseer "Конечно хотел бы."
    "Да кто же мне это даст."
    m "Сэр."

    img 2356
    "Я могу помочь Вам с этим?"

    img 2357
    music Groove2_85
    overseer "Ты?"
    "Да чем ты можешь мне помочь?"
    "Ты сидишь здесь в клетке."
    "Ишь чего мне тут лепечет!"
    music Hidden_Agenda
    img 2358
    with fade
    m "Сэр."
    "Знаете."
    "На свободе я очень, ОЧЕНЬ большой человек!"
    img 2359
    "У меня ОЧЕНЬ ОЧЕНЬ много денег!"
    "И Вы знаете."
    img 2360
    "Если бы Вы поспособствовали тому чтобы я отсюда выбралась, я бы могла помочь Вам начать другую жизнь!"
    img 2361
    overseer "Ну.. Я не знаю."
    img 2362
    m "Сэр."
    "Вы подумайте!"
    "Дорогие отели..."
    img 2363
    "Красивые женщины..."
    img 2364
    overseer "И что ты предлагаешь?"
    img 2365
    m "Я предлагаю Вам вывести меня отсюда."
    "Ведь Вы такой умный."
    "Вы знаете как это сделать?"
    img 2366
    overseer "Конечно."
    "Здесь есть много ходов."
    "Начальство-то сюда не ходит."
    "А мне и канализацию почистить и вентиляцию..."
    img 2367
    m "Сэр!"
    "Это прекрасно!"
    "Вы мой герой!"
    "Помогите мне выбраться отсюда и, клянусь, я сделаю из Вас богача!"
    img 2368
    music Groove2_85
    overseer "Ну..."
    "Что-то я не верю тебе."
    "Я тебе помогу, а что потом будет со мной?"
    img 2369
    music Hidden_Agenda
    m "Сэр."
    "Вас это уже не будет волновать."
    "У Вас будет столько денег, что Вам не страшны никакие проблемы!"
    overseer "А ежели ты обманешь?"
    m "Я не обману Вас, Сэр!"
    overseer "Нет. Так не пойдет."
    img 2370
    music Pyro_Flow
    mt "????"
    "!!!!!"
    "УРОД!!!"
    "ВСЕ ЛОМАЕТСЯ!!!"
    img 2371
    "НУ ЖЕ!!!!"
    img 2372
    music Hidden_Agenda
    m "Сэр."
    "Почему?"

    music Groove2_85
    overseer "А ты сначала сделай то что обещала, а потом я тебя вытащу."
    m "А вдруг Вы меня обманете?"
    img 2373
    with fadelong
    overseer "Тогда забудем об этом."
    "Я пошел."
    m "Нет!"
    "Стойте!"
    "Я согласна!"
    img 2374
    m "Сэр!"
    "Вы можете пойти к моему секретарю."
    "Это в здании журнала моды, в центре."
    img 2375
    "Поднимитесь на 57-ой этаж."
    img 2376
    "Скажите что Вас прислала Моника Бакфетт, их Босс."
    "Расскажите секретарю где я и скажите ей что вы хотите взамен."
    img 2378
    overseer "Хорошо, завтра с утра я схожу."
    m "Сэр!"
    "Буду ждать!"
    img 2377
    overseer "А сейчас все."
    m "Голова?"
    overseer "Да, как ты догадалась?"
    $ jailDaySceneStage = 1
    $ policeCellStageName1 = "scene_Police_Cell_1_Day_7_2"
    $ policeCellStageName2 = "scene_Police_Cell_2_Day_7_2"
    $ policeCellMonica1 = "Police_Cell_1_Day_7_2"
    $ policeCellMonica2 = "Police_Cell_2_Day_7_2"
    music Jail_Clock
    call refresh_scene_fade()
    return
