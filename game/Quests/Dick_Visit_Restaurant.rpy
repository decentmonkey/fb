default dick_meeting1_restaurant_drive_dialogue1_planned = False
default dick_meeting1_restaurant_dialogue1_completed = False
default dick_meeting1_restaurant_dialogue2_completed = False
default dick_meeting1_restaurant_dialogue3_completed = False



label dick_meeting1_restaurant_init:
    $ add_objective("dick_meeting1_goto_restaurant", _("Ехать с Диком в ресторан"), c_pink, 25)
    $ dick_meeting1_restaurant_drive_dialogue1_planned = True
    $ dickMeeting1RestaurantPlanned = True
    $ focus_map("Teleport_Rich_Hotel", "dick_meeting1_restaurant_map_disabled")
#    $ unfocus_map()
    return

label dick_meeting1_restaurant_map_disabled(obj_name, obj_data):
    dick "Моника!
    Поехали скорее в ресторан!"
    "Он и так скоро закроется!"
    m "Дик, хватит ныть!"
    "Ты мне уже надоел!"
    return

label dick_meeting1_restaurant_drive_dialogue1:
    sound snd_car_engine
    img 1400
    with fadelong
    dick "Уже стемнело..."

    menu:
        "Это ты виноват!":
            $ dickDriveRestaurantOffended1 = True
            call bitch(1, "dickDriveRestaurantOffended1")

            m "Я бы справилась быстрее, если бы ты отвез меня в нормальное место."
            "Я считаю это ты виноват, что мы так задержались."
        "Зато мы купили платье!":
            m "Зато мы купили платье, Дик!"
            "Ты разве не рад?"
            img 1402
            dick "Конечно, Моника."
            "Я очень рад."

    sound snd_car_engine
    img 1401
    with fadelong
    dick "Ресторан уже вот-вот закроется..."

    m "Дик, мы договорились что ты не будешь жаловаться."

    img 1402
    dick "Конечно, Моника."
    $ dickWaitingMonica2 = True
    $ autorun_to_object("street_rich_hotel", "dick_waiting_monica_dialogue2")
    return

label dick_waiting_monica_dialogue2:
    $ unfocus_map()
    $ remove_objective("dick_meeting1_goto_restaurant")
    $ autorun_to_object("rich_hotel_reception", "dick_meeting1_restaurant_reception_dialogue")
    imgr Dick3
    dick "Дорогая!
    Пойдем внутрь скорее!"
    "Ресторан скоро закроется!"
    imgl Dial_monicaEveningDress_2
    m "Дик, не торопи меня!"
    "Если ты будешь на меня давить, мне станет скучно."
    "Ты ведь не хочешь этого, правда Дик?"
    imgr Dick5
    dick "Нет, дорогая, конечно нет!"
    return

label dick_waiting_monica_dialogue2Short:
    imgr Dick1
    dick "Дорогая!
    Пойдем внутрь скорее!"
    return

label dick_meeting1_restaurant_reception_dialogue:
    $ dickWaitingMonica2 = False
    $ dickWaitingMonica3 = True
    dick "Дорогая, пойдем вовнутрь!
    Обещаю, тебе понравится!"
    m "Увидим, Дик!
    Не загадывай!"
    return

label dick_meeting1_restaurant_enter1:
    sound highheels_short_walk
    img 1405
    with fadelong
    waitress "Добрый вечер, господа."
    "Мы скоро закрываемся."

    img 1406
    dick "Я знаю, мадам."
    "У нас заказан столик."
    "Мы хотели бы немного посидеть."
    "До закрытия."

    img 1407
    waitress "Хорошо, сэр."
    "Пожалуйста, идите за мной."

#    img 1408
#    with fadelong
#    waitress "Пожалуйста, присаживайтесь."
    $ autorun_to_object("rich_hotel_restaurant", "dick_meeting1_restaurant_enter1_letsit")
    return

label dick_meeting1_restaurant_enter1_letsit:
    waitress "Пожалуйста, присаживайтесь."
    return

label dick_meeting1_restaurant_monica_interaction(obj_data):
    if richHotelRestaurantState == 1:
        mt "Мои ножки упираются в этот неудобный столик."
        "Что-ж, сяду поудобнее!
        Надеюсь Дик ничего не увидит.
        Но ничего, пусть попускает слюни."
        "Все-равно ему ничего не светит!
        Хи-хи."
    if richHotelRestaurantState == 2:
        mt "Стейк и лобстер?"
        "Интересно кому что?"
        "Даже не поинтересовался что я люблю.
        Может до этого он изучил мои вкусы?"
        "Не думаю что у него хватило бы ума на это!
        Хотя он хороший адвокат..."
        "У адвокатов ведь должен быть ум? Или что там еще?"
    if richHotelRestaurantState == 3:
        if bitchmeterValue > maxBitchness / 2:
            mt "Эта сучка что, издевается над нами?"
        else:
            mt "Ведь она не специально это говорит?
            Уже правда поздно."
    return

label dick_meeting1_restaurant_dick_interaction(obj_data):
    if obj_data["action"] == "l":
        if richHotelRestaurantState == 3:
            if bitchmeterValue > maxBitchness / 2:
                mt "Дик так и собирается терпеть наглость этой официантки?"
            else:
                mt "Дик уже упоминал что ресторан скоро закроется..."
            return
        if richHotelRestaurantDickOffended1ChoiceMade == False:
            $ richHotelRestaurantDickOffended1ChoiceMade = True
            mt "Дик так смешно выглядит на этом стуле!"
            "Растекся по нему как желе."
            "Может сказать ему об этом?
            Или это будет слишком?"
            menu:
                "Сказать Дику что он смешной.":
                    $ richHotelRestaurantDickOffended1 = True
                    m "..."
                    img 1413
                    dick "Моника, чему ты улыбнулась?"
                    img 4677
                    m "О Боже, Дик!"
                    "Ты такой смешной на этом стуле!"
                    "Растекся по нему словно желе!"
                    "Это очень смешно!"
                    call bitch(5, "richHotelRestaurantDickOffended1")
                    if richHotelRestaurantState == 1:
                        img 1423
                    if richHotelRestaurantState == 2:
                        img 1428
                    dick "Кхмм.. Моника..."
                    m "Ладно, Дик! Проехали! Хи-хи"

                "Промолчать, это уже будет слишком.":
                    m "..."
                    img 1413
                    dick "Моника, чему ты улыбнулась?"
                    mt "Нет, Дик, ничему, прости!"
                    call bitch(-3, "richHotelRestaurantDickOffended1")
        else:
            if richHotelRestaurantDickOffended1 == True:
                mt "Может я зря ему сказала что он так смешно выглядит на этом стуле?"
                "Но ведь это же правда."
                "Люди должны говорить друг другу правду, правда ведь?"
            else:
                mt "Не буду ему говорить как он выглядит сейчас."
                "Но я боюсь не сдержаться и засмеяться."
    if obj_data["action"] == "t":
        if richHotelRestaurantState == 1:
            call dick_meeting1_restaurant_dialogue1()
            return
        if richHotelRestaurantState == 2:
            call dick_meeting1_restaurant_dialogue2()
            return
        if richHotelRestaurantState == 3:
            dick "Моника! Я... Эээээ..."
            return
    return

label dick_meeting1_restaurant_waitress_interaction(obj_data):
    if obj_data["action"] == "l":
        if richHotelRestaurantState == 3:
            if bitchmeterValue > maxBitchness / 2:
                mt "Эта сучка меня уже достала!"
            else:
                mt "Она выглядит уставшей..."

        return

    if obj_data["action"] == "t":
        if richHotelRestaurantState == 1:
            call dick_meeting1_restaurant_dialogue1()
            return
        if richHotelRestaurantState == 3:
            call dick_meeting1_restaurant_dialogue4_waitress_b()
    return


label dick_meeting1_restaurant_dialogue1():
    img 1409
    with fade
    waitress "Что вы желаете?"

    img 1410
    dick "Пожалуйста, вино."
    "Стейк и лобстер."

    img 1411
    waitress "Хорошо, скоро подадим."
    sound highheels_run1
    $ richHotelRestaurantState = 2
    call refresh_scene_fade()
    return

label dick_meeting1_restaurant_dialogue2():
    img 1412
    with fadelong
    m "..."

    dick "..."
    "Дорогая."

    m "Да, Дик."

    img 1413
    dick "Как прошел твой день?"

    label dick_meeting1_restaurant_dialogue2_menu_loop1:
    menu:
        "Мой сосед...":
            call dick_meeting1_restaurant_dialogue2_neighbor()
            call refresh_scene_fade()
            return
        "Ферма соседа..." if dick_meeting1_restaurant_dialogue1_completed == True and neighborOffendedFarm == True and neighborOffendedSue == True:
            call dick_meeting1_restaurant_dialogue2_neighbor_d_farm()
            call refresh_scene_fade()
            return
        "Ферма соседа... (disabled)" if dick_meeting1_restaurant_dialogue1_completed == True and neighborOffendedFarm == False and neighborOffendedSue == True:
            jump dick_meeting1_restaurant_dialogue2_menu_loop1

        "Моя служанка...":
            call dick_meeting1_restaurant_dialogue2_julia()
            call refresh_scene_fade()
            return

        "Модели...":
            call dick_meeting1_restaurant_dialogue3_models()
            call refresh_scene_fade()
            return

#        "Где там наш ужин?" if dick_meeting1_restaurant_dialogue1_completed == True and dick_meeting1_restaurant_dialogue2_completed == True and dick_meeting1_restaurant_dialogue3_completed == True:
        "Где там наш ужин?" if dick_meeting1_restaurant_dialogue1_completed == True:
            img 1416
            m "Дик! Где там наш ужин? Сколько можно ждать?"
            img 1412
            dick "Официантка уже идет, Моника!
            Она прямо за тобой!"
            img 1420
            with fadelong
            waitress "Ваш заказ скоро будет готов."
            $ autorun_to_object("rich_hotel_restaurant", "dick_meeting1_restaurant_dialogue4_waitress")
            $ richHotelRestaurantState = 3
#            $ bitchmeterValue = maxBitchness #debug
            call refresh_scene_fade()

    return

label dick_meeting1_restaurant_dialogue2_neighbor():
    $ dick_meeting1_restaurant_dialogue1_completed = True
    img 1414
    m "О, Дик!
    Мой сосед..."

    img 1413
    dick "У тебя есть соседи, Моника?"

    img 1414
    m "Да, представляешь, Дик?
    Он поцарапал мой забор."

    img 1413
    dick "Он висел на нем, чтобы подглядывать за тобой?
    А потом сорвался и поцарапал его?"

    img 1414
    m "Хм, Дик..."
    "Я как-то не задумывалась над этим."

    img 1413
    dick "Ты видела его?"

#    $ houseStreetFenceLocationOpened = True #debug

    label dick_meeting1_restaurant_dialogue2_neighbor_menu_loop1:
    menu:
        "Да, я видела его, Дик!" if houseStreetFenceLocationOpened == True :
            jump dick_meeting1_restaurant_dialogue2_neighbor_a

        "Да, я видела его, Дик! (disabled)" if houseStreetFenceLocationOpened == False:
            jump dick_meeting1_restaurant_dialogue2_neighbor_menu_loop1

        "Нет, Дик! Я не видела его!" if houseStreetFenceLocationOpened == False:
            img 1418
            m "Нет, Дик! Я не видела его!"
            img 1413
            dick "Но почему, Моника?
            Я не узнаю тебя!"
            "Моника Бакфетт должна была закатить ему иск и стереть его в порошок!"
            img 1417
            "Ты ведь знаешь, я очень хорошо умею это делать и сделал бы это для тебя, с удовольствием! Хе-хе"
            img 1418
            m "Дик, я считаю что это не мое дело.
            Пусть мой муж разбирается в этом."
            img 1416
            m "Ты ведь не забыл что у меня есть муж, правда Дик?"
            img 1412
            dick "Конечно конечно, Моника. Я помню."
            if dickMonicaIdiotsAround == False:
                img 1413
                dick "Просто я помню про то что ты самостоятельная девочка. Хе-хе"
                img 1414
                m "Я самостоятельная девочка, Дик!
                Но это не значит что я должна решать все дела за вас, мужчин."
                img 1418
                m "Или ты считаешь что должна?"
                img 1419
                dick "Что ты, Моника, дорогая!"
                "Вокруг тебя полно мужчин, которые могут решить все твои проблемы!"
                img 1418
                m "Вот и пусть решают!"
                return
            else:
                img 1417
                dick "Просто я помню что ты сама говорила, что нас окружают одни идиоты."
                "И все приходится делать нам самим."
                img 1418
                m "Нам - это кому?
                Ты очень искуссно вычеркнул себя из списка идиотов, которые меня окружают, Дик!"
                img 1428
                dick "Моника, ты правда считаешь что я тоже идиот?"
                img 4678
                m "Ладно, Дик. Не обижайся. Я так не считаю."
                "Иначе ты бы не сидел здесь со мной."
                img 1413
                m "Я ценю твой уровень.
                Ведь ты бы решил эту проблему если бы я попросила?"
                img 1417
                dick "Конечно, Моника!
                Ты знаешь что я готов решить любую твою проблему!"
                "И я прекрасно умею это делать!"
                img 1418
                m "Проверю при случае, Дик!"
                dick "Конечно, дорогая! Буду рад тебе помочь всегда!"
                return

        "Нет, Дик! Я не видела его! (disabled)" if houseStreetFenceLocationOpened == True:
            jump dick_meeting1_restaurant_dialogue2_neighbor_menu_loop1


    #houseStreetFenceLocationOpened

    return

label dick_meeting1_restaurant_dialogue2_neighbor_a():

    img 1418
    m "Да, я видела его, Дик!"
    label dick_meeting1_restaurant_dialogue2_neighbor_a_menu_loop1:
    menu:
        "Это какой-то бедняк." if neighborOffended1 == True:
            m "Это какой-то бедняк. Я не понимаю как он смог стать моим соседом."
            "Я даже не стала здороваться с ним! Какое-то ничтожество!"
        "Это какой-то бедняк. (disabled)" if neighborOffended1 == False:
            jump dick_meeting1_restaurant_dialogue2_neighbor_a_menu_loop1
        "Обычный сосед." if neighborOffended1 == False:
            img 4680
            m "Обычный сосед. Вполне себе вежливый на вид!"
        "Обычный сосед. (disabled)" if neighborOffended1 == True:
            jump dick_meeting1_restaurant_dialogue2_neighbor_a_menu_loop1


    label dick_meeting1_restaurant_dialogue2_neighbor_a_menu_loop2:
    menu:
        "Этот придурок чуть не погиб!" if neighborOffended2 == True:
            img 1416
            m "Ты представляешь, Дик!
            Судя по его словам там было что-то с газонокосилкой и он чуть не погиб!"
            "То есть он думал разжалобить меня этим!"
            "Он думает что мне станет жаль такого идиота, который сам себя чуть не убил на пустом месте!"
        "Этот придурок чуть не погиб! (disabled)" if neighborOffended2 == False:
            jump dick_meeting1_restaurant_dialogue2_neighbor_a_menu_loop2
        "Он был в опасности." if neighborOffended2 == False:
            img 4681
            m "Он убедил меня в том что подвергся опасности во время инцидента."
            img 1413
            dick "А что там случилось?"
            img 4681
            m "Он косил газон и вдруг чуть не погиб!"
        "Он был в опасности. (disabled)" if neighborOffended2 == True:
            jump dick_meeting1_restaurant_dialogue2_neighbor_a_menu_loop2

    img 1413
    dick "Это если он говорит правду, Моника!
    Он ведь и просто мог подглядывать за тобой с забора."
    img 1415
    m "Не знаю, Дик, что он там делал."
    if neighborOffended3 == True:
        m "Я знаю что он к тому же решил потоптаться в моем дворе своими грязными ботинками."
    else:
        m "В общем мы прошли посмотреть что там с забором."

#    $ neighborOffended4 = True
    label dick_meeting1_restaurant_dialogue2_neighbor_a_menu_loop3:
    menu:
        "Дик! Он полностью сломал мне забор!" if neighborOffended4 == True:
            call dick_meeting1_restaurant_dialogue2_neighbor_b()
            return
        "Дик! Он полностью сломал мне забор! (disabled)" if neighborOffended4 == False:
            jump dick_meeting1_restaurant_dialogue2_neighbor_a_menu_loop3
        "Там оказалась просто царапина." if neighborOffended4 == False:
            img 4678
            m "В общем это оказалось просто царапиной, Дик!"
            "Сущая ерунда! Я только зря потратила время!"

            dick "И что было дальше?"
            m "Я сказала ему что он может идти, что еще могло быть дальше?"
            img 1413
            dick "Но почему, Моника?
            Я не узнаю тебя!"
            "Моника Бакфетт должна была закатить ему иск и стереть его в порошок!"
            img 4679
            m "Ой, Дик!
            Я знаю что многие считают меня стервой, но это на самом деле не так!"
            img 1428
            dick "Я не считаю тебя стервой, Моника!"
            img 4679
            m "Я знаю, Дик! Потому что я не стерва!
            И я доказала это в очередной раз!"
            m "Просто глупые люди часто совершают некомпетентные поступки."
            "А когда им приходит расплата за них, то они пытаются обвинить в этом других, например меня!"
            "А я ведь очень добрая, согласись Дик?"
            img 1417
            dick "Моника, я считаю ты слишком добрая. Хе-Хе"
            "Надо было закатить ему иск и стереть его в порошок!"
            "Ты ведь знаешь, я очень хорошо умею это делать и сделал бы это для тебя, с удовольствием! Хе-хе"
            img 1414
            m "Правда, Дик? Ты бы сделал это для меня?"
            img 1417
            dick "Конечно, Моника!
            Ты знаешь что я готов решить любую твою проблему!"
            "И я прекрасно умею это делать!"
            img 1418
            m "Проверю при случае, Дик!"
            dick "Конечно, дорогая! Буду рад тебе помочь всегда!"
            return

        "Там оказалась просто царапина. (disabled)" if neighborOffended4 == True:
            jump dick_meeting1_restaurant_dialogue2_neighbor_a_menu_loop3
    return

label dick_meeting1_restaurant_dialogue2_neighbor_b():
    img 1416
    m "Дик! Он полностью сломал мне забор!"
    "И посмел назвать это царапиной!
    Он пытался обдурить меня!"
    img 1413
    dick "И что было дальше?"
#    $ neighborOffended5 = False #debug

    label dick_meeting1_restaurant_dialogue2_neighbor_b_menu_loop1:
    menu:
        "Я закатила ему иск!" if neighborOffended5 == False:
            call dick_meeting1_restaurant_dialogue2_neighbor_c()
            return
        "Я закатила ему иск! (disabled)" if neighborOffended5 == True:
            jump dick_meeting1_restaurant_dialogue2_neighbor_b_menu_loop1

        "Я прогнала этого идиота!" if neighborOffended5 == True:
            img 1416
            m "Я прогнала этого идиота!
            Что еще могло быть дальше?"
            img 1413
            dick "Но почему, Моника?
            Я не узнаю тебя!"
            "Моника Бакфетт должна была закатить ему иск и стереть его в порошок!"
            img 1418
            m "Дик, у меня нет времени на каждого болвана, который болтается под ногами!"
            "Я занимаюсь большими деньгами!"
            "Между прочим, если бы я закатила иск, то мне пришлось бы обращаться к тебе, а у тебя вечно на меня нет времени!"
            img 1428
            dick "Что ты, Моника?
            Я никогда тебе ни в чем не отказывал!"
            "Если бы ты попросила, то я сделал бы это для тебя, бесплатно!"
            "Ты же знаешь как я отношусь к тебе!"
            img 1414
            m "Правда, Дик? Ты бы сделал это для меня?"
            img 1417
            dick "Конечно, Моника!
            Ты знаешь что я готов решить любую твою проблему!"
            "И я прекрасно умею это делать!"
            img 1418
            m "Проверю при случае, Дик!"
            dick "Конечно, дорогая! Буду рад тебе помочь всегда!"
            return

        "Я прогнала этого идиота! (disabled)" if neighborOffended5 == False:
            jump dick_meeting1_restaurant_dialogue2_neighbor_b_menu_loop1

    return

label dick_meeting1_restaurant_dialogue2_neighbor_c():
    # neighborOffended1 = False #не здороваться
    # neighborOffended2 = False #без разницы что он чуть не погиб
    # neighborOffended3 = False #решил потоптать во дворе?
    # neighborOffended4 = False #это не просто царапина, наехать
    # neighborOffended5 = False #прогнать идиота, грубо
    # neighborOffendedSue = False #закатить иск
    # neighborOffendedSueBig = False #иск огромный
    # neighborOffendedFarm = False #наехать на ферму
    img 1414
    m "Я закатила ему иск!"
    img 1413
    dick "Моника! Я узнаю тебя!"
    "Это очень на тебя похоже!"
    "И сколько ты решила с него взыскать?"
#    $ neighborOffendedSueBig = True #debug
    label dick_meeting1_restaurant_dialogue2_neighbor_c_menu_loop1:
    menu:
        "$100.000, Дик!" if neighborOffendedSueBig == True:
            img 4682
            m "$100.000, Дик!"
            img 1413
            dick "Ого! Видимо ты очень любила этот забор, Моника!"
            m "Я люблю вещи, которые принадлежат мне!"
            dick "А людей, которые тебе принадлежат?"
            img 1416
            m "Людей нет, Дик!"
            "Хорошие вещи не бывают такими тупыми и бесполезными, как люди!"
            "К чему эти глупые вопросы, Дик?"
            img 1428
            dick "Эгххмм... Моника, прости."
            dick "Это была неудачная шутка."
            img 1413
            dick "Ты ведь знаешь, я бываю иногда немного неповоротлив... в шутках..."
            if richHotelRestaurantDickOffended1 == True:
                img 4682
                m "Бываешь, Дик! И не только в шутках."
                "То что ты растекся как желе на этом стуле я уже говорила тебе, так что..."
                img 1428
                dick "Моника, ну что ты..."
                img 4678
                m "Ладно, Дик. Кое в чем ты даже забавный, не обижайся."
                img 1413
                dick "Я не обижаюсь, Моника! Хе-хе"
            else:
                img 4678
                mt "Я не могу сдержаться, так хочется рассмеяться."
                "Это каждый раз когда я сравниваю Дика с растекшимся желе на этом стуле."
                "Может стоит все-таки подшутить над ним?"
            img 1415
            with fade
            m "Так вот, Дик!
            У меня есть предчуствие что этот сосед не собирается отдавать мне деньги!"
            "И вообще мне он не нравится.
            Дик, убери его, пожалуйста, подальше от моего дома!"
            img 1417
            dick "Моника, я тебя понял!"
            "Не переживай, завтра же иск отправится в суд!"
            "Через месяц твоего соседа не будет."
            img 1418
            m "А можно быстрее?"
            "Завтра?"
            img 1419
            dick "К сожалению, суды работают очень долго."
            "Иначе я зарабатывал бы деньги во много раз быстрее. Хе-хе"
            $ dickHelpsMoniceSue = True

        "$100.000, Дик! (disabled)" if neighborOffendedSueBig == False:
            jump dick_meeting1_restaurant_dialogue2_neighbor_c_menu_loop1
        "$500..." if neighborOffendedSueBig == False:
            img 1415
            m "$500, Дик."
            img 1413
            dick "Сколько???
            Моника, ты шутишь?"
            m "Нет, Дик."
            dick "Моника, даже пуговица на моем костюме стоит больше чем ты с него решила взыскать!"
            img 1418
            m "Ну и что?
            Это значит что ты не возьмешься за дело, если он не отдаст эти деньги?"
            img 1428
            dick "Что ты, Моника!"
            "Просто я немного удивлен твоей щедростью!"
            img 1413
            "Тебе не жаль было времени на разговор с этим человеком?
            Ведь ты за это время заработала гораздо больше, чем сумма иска!"
            "Хе-хе"
            img 4679
            m "Ой, Дик!
            Я знаю что многие считают меня стервой, но это на самом деле не так!"
            img 1428
            dick "Я не считаю тебя стервой, Моника!"
            img 4679
            m "Я знаю, Дик! Потому что я не стерва!
            И я доказала это в очередной раз!"
            m "Просто глупые люди часто совершают некомпетентные поступки."
            "А когда им приходит расплата за них, то они пытаются обвинить в этом других, например меня!"
            "А я ведь очень добрая, согласись Дик?"
            img 1417
            dick "Моника, я считаю ты слишком добрая. Хе-Хе"
            "Надо было закатить ему иск и стереть его в порошок!"
            "Ты ведь знаешь, я очень хорошо умею это делать и сделал бы это для тебя, с удовольствием! Хе-хе"
            img 1414
            m "Правда, Дик? Ты бы сделал это для меня?"
            img 1417
            dick "Конечно, Моника!
            Ты знаешь что я готов решить любую твою проблему!"
            "И я прекрасно умею это делать!"
            img 1418
            m "Проверю при случае, Дик!"
            dick "Конечно, дорогая! Буду рад тебе помочь всегда!"


        "$500... (disabled)" if neighborOffendedSueBig == True:
            jump dick_meeting1_restaurant_dialogue2_neighbor_c_menu_loop1

    return

label dick_meeting1_restaurant_dialogue2_neighbor_d_farm():
    img 1418
    m "Да, кстати, Дик!
    Я совсем забыла!"
    img 1412
    dick "Да, Моника!
    Я тебя внимательно слушаю!"
    img 1418
    m "У этого соседа.
    Через дорогу.
    Есть ферма."
    "Вонючая ферма!"
    img 1416
    m "Я хочу чтобы этой фермы также не было, как и соседа!"
    "Ты меня понял, Дик?!"
    img 1417
    dick "Я понял, Моника!
    Нет проблем!"
    img 4679
    m "Вот и хорошо."

    return

#default juliaMonicaYell = False #Моника обращается с Юлией криком
#default juliaPunished = False #жестко наказана, убирается на втором этаже каждый день
#default juliaPunishedLow = False #наказана криком, но разрешено не убирать пятно
#default juliaPunishedVoluntarily = False #мягко, разрешено убирать в свободное время
#default juliaPunishedNone = False #пятно есть, но Юлию не наказали вообще никак
#default juliaMonicaLied = False #Моника соврала что пятно поставила не она

label dick_meeting1_restaurant_dialogue2_julia():
    $ dick_meeting1_restaurant_dialogue2_completed = True
    img 1414
    m "Знаешь, Дик, у меня все хорошо."
    dick "Не сомневаюсь, Моника."
    m "Не знаю даже что рассказать тебе.
    Могу только о какой-нибудь ерунде."
    "Но для такого человека как ты это не будет интересно."
    img 1412
    dick "Что ты, Моника!
    Мне все очень интересно!"
    "Пожалуйста, расскажи!"
    img 4679
    m "У меня испачкался ковер, Дик."
    img 1428
    dick "Да ты что?!
    Моника, как же ты это пережила?!"

    label dick_meeting1_restaurant_dialogue2_julia_menu_loop1:
    menu:
        "Я это пережила." if juliaMonicaLied == False:
            img 1415
            m "Я это пережила, Дик!
            И знаешь почему?"
            img 1413
            dick "Почему-же, Моника?
            Мне очень интересно!"
            img 1414
            m "Потому что я сама его испачкала, Дик!"
            img 1413
            dick "Как же так случилось, Моника?"
            "Наверное за этим кроется какая-то история?"
            img 1415
            m "Какая история, Дик?"
            "Я обожглась утюгом сегодня!"
            img 1428
            dick "Ты? Утюгом??"
            "Боже, Моника!"
            "Тебе нужна помощь?"
            img 1418
            m "Мне не нужна помощь, Дик!"
            img 1413
            dick "Но я уверен, что кто-то за это жестоко ответил, ведь правда, Моника?"
            img 1415
            m "Нет, Дик, ты никогда не можешь ничего угадать!"
            "Да, я сама погладила платье."
            "Из-за этого испачкала ковер."
            "Формально в этом виновата моя гувернантка."
            img 1418
            "Но я не тиран, Дик!"
            "Она хорошая девушка.
            Она доказала свой профессионализм."
            "Мой водитель, Фред.
            Он хоть и болван, но он разбирается в том кто профессионал, а кто нет."
            "И его советы мне очень кстати!"

            if juliaPunishedVoluntarily == True:
                img 4678
                m "Тем более она будет убирать это пятно на ковре в свободное время."
                "Так что инцидент исчерпан, Дик."
            img 1413
            dick "Моника, ты слишком добрая!"
            "Твоя доброта тебя погубит!"
            img 4679
            m "Но ты ведь тоже добр ко мне, Дик?"
            img 1417
            m "О, Моника! Я к тебе очень добр!"
            "И, клянусь, буду добр всегда, чего бы мне это ни стоило!"
            m "Вот и славно."

        "Я это пережила. (disabled)" if juliaMonicaLied == True:
            jump dick_meeting1_restaurant_dialogue2_julia_menu_loop1

        "Я этого не пережила." if juliaMonicaLied == True:
            img 1418
            m "Я этого не пережила, Дик!"
            "Пятно все еще на ковре.
            И я переживу это когда оно исчезнет!"

            img 1414
            with fade
            "Эта Юлия, гувернантка.
            Я обожглась сегодня утюгом из-за нее."
            "А еще она поставила пятно на ковер!"
            img 1428
            dick "Ты? Утюгом??"
            "Боже, Моника!"
            "Тебе нужна помощь?"
            img 1418
            m "Мне не нужна помощь, Дик!"
            img 1413
            dick "Но я уверен, что она жестоко ответила за это, ведь правда, Моника?"

            if juliaPunished == True:
                img 1416
                m "Да, Дик!
                А как ты думаешь?"
                "Я за меньшее увольняю безо всяких сомнений!"
                "Но я сделала исключение, проявила доброту и дала этой сучке гувернантке один день на то чтобы оттереть это пятно!"
                img 1413
                dick "О, Моника!
                Ты слишком добрая!"
                "Если она не профессионал, то ее следовало уволить."
                img 1414
                m "Она профессионал."
                "Мой водитель, Фред.
                Он хоть и болван, но он разбирается в том кто профессионал, а кто нет."
                "И его советы мне очень кстати!"
            else:
                img 1416
                m "Да, Дик!
                А как ты думаешь?"
                "Я за меньшее увольняю безо всяких сомнений!"
                img 1414
                "Но я не тиран, Дик!"
                "Она хорошая девушка.
                Она доказала свой профессионализм."
                "Мой водитель, Фред.
                Он хоть и болван, но он разбирается в том кто профессионал, а кто нет."
                "И его советы мне очень кстати!"
                m "Так что она будет убирать это пятно в свободное время, даже если это займет у нее всю оставшуюся жизнь."

            img 1428
            dick "Моника, я кажется помню.
            Это та гувернантка, которой я лично для тебя делал договор о приеме на работу?"
            img 1415
            m "Да, Дик."
            "Это она."
            img 1428
            dick "Моника, прости меня, если я посоветовал тебе непрофессионала, который создает проблемы."
            img 1418
            m "Дик, ты вечно ничего не помнишь.
            Я удивляюсь как ты вообще можешь быть хорошим адвокатом."
            m "Это не твое протеже."
            "Ее посоветовал Фред, мой водитель.
            Он профессионал и разбирается в работниках, как я тебе уже говорила."
            "..."
            "Хотя..."
            img 1416
            m "Ты прав, Дик!"
            "Ведь это его промах!"
            "Я решу как его наказать. Этого болвана.
            Но позже."


        "Я этого не пережила. (disabled)" if juliaMonicaLied == False:
            jump dick_meeting1_restaurant_dialogue2_julia_menu_loop1


    return


label dick_meeting1_restaurant_dialogue3_models():
    $ dick_meeting1_restaurant_dialogue3_completed = True

#    $ monkeysOffended3 = True #debug
    label dick_meeting1_restaurant_dialogue3_models_menu_loop1:
    menu:
        "Сегодня был забавный случай..." if monkeysOffended3 == True:
            img 4683
            m "Сегодня был забавный случай, Дик!
            Хочешь расскажу?"
            img 1413
            dick "Конечно, Моника!
            Очень хочу!"

            img 4683
            if monkeysOffended1 == True:
                m "Сегодня приходили две какие-то мартышки... Модели..."
            else:
                m "Сегодня приходили две какие-то смешные девушки... Модели..."

            if entranceTalkedWithMonkeys == True:
                m "Я их встретила внизу возле моего личного входа в Tower."
                "Они мне нагрубили."
                img 1413
                dick "И ты их испепелила, прямо там внизу возле входа?"
                img 4679
                m "Нет, Дик!
                Я тебе говорила, что я очень добрая!"
                "Я их не тронула и пошла дальше!"
                img 1428
                dick "Не могу поверить, Моника!
                Да ты просто ангел во плоти!"
                img 4679
                m "Да, Дик!
                Так и есть!"
                "А ты только сейчас это понял?"

            img 4683
            m "Так вот! Слушай дальше!"
            "Спустя 10 минут они пришли ко мне на кастинг!"
            "Угадай что я с ними сделала, Дик?"
            img 1413
            dick "Я ни за что не угадаю, Моника! Расскажи скорее!"
            img 4683
            m "Я заставила их раздеться догола и принимать разные отвратительные позы!"
            "Хорошо что моя секретарь этого не видела!"
            "Она бы упала в обморок!
            Хи-хи!"
            img 4685
            dick "Догола?"
            img 4683
            m "Да, Дик!"
            if melaniePhotoShotProcessed == True:
                "Конечно они в итоге не подошли."
                "Но я добрая, и я решила показать им как снимаются настоящие модели."
                "И я показала им фотосессию с моей топ моделью."
                "Видел-бы ты их глаза, Дик!"
                "Это было так смешно!"
                img 4685
                dick "А с какой моделью, Моника?"
                "Кто у тебя сейчас топ?"
                img 1418
                m "Мелани, Дик!
                Ты ее знаешь?"
                img 4686
                dick "Мелани?
                Это та самая?"
                dick "И ты видела ее обнаженной?"
                img 1418
                m "Дик, ты что, идиот?"
                "Она была в белье."
                "Но я видела ее обнаженной, естественно."
                "Ты ведь знаешь что я провожу немного унизительный осмотр всем моделям."
                "Это умеряет их гонор и учит дисциплине."
                img 4684
                m "Дик, ты бы себя сейчас видел!"
                "У тебя такое лицо...
                Ты что, хочешь трахнуть Мелани?"
                img 1428
                dick "Что ты, Моника?!"
                "Конечно нет!"
                "Мой идеал - это ты!"
                "Ты же знаешь!"
                $ dickWantFuckMelanie = True


        "Сегодня был забавный случай... (disabled)" if monkeysOffended3 == False:
            jump dick_meeting1_restaurant_dialogue3_models_menu_loop1

        "Все пытаются отнять мое время..." if monkeysOffended3 == False:
            img 4683
            m "Сегодня был забавный случай, Дик!
            Хочешь расскажу?"
            img 1413
            dick "Конечно, Моника!
            Очень хочу!"
            img 4683
            if monkeysOffended1 == True:
                m "Сегодня приходили две какие-то мартышки... Модели..."
            else:
                m "Сегодня приходили две какие-то смешные девушки... Модели..."

            if entranceTalkedWithMonkeys == True:
                m "Я их встретила внизу возле моего личного входа в Tower."
                "Они мне нагрубили."
                img 1413
                dick "И ты их испепелила, прямо там внизу возле входа?"
                img 4679
                m "Нет, Дик!
                Я тебе говорила, что я очень добрая!"
                "Я их не тронула и пошла дальше!"
                img 1428
                dick "Не могу поверить, Моника!
                Да ты просто ангел во плоти!"
                img 4679
                m "Да, Дик!
                Так и есть!"
                "А ты только сейчас это понял?"

            img 4683
            m "Так вот! Слушай дальше!"
            "Спустя 10 минут они пришли ко мне на кастинг!"
            "Угадай что я с ними сделала, Дик?"
            img 1413
            dick "Я ни за что не угадаю, Моника! Расскажи скорее!"
            if melaniePhotoShotProcessed == True:
                img 1418
                m "Я прогнала их, Дик!"
                "Но не сразу!"
                img 4683
                "Я решила показать им как снимаются настоящие модели."
                "И я показала им фотосессию с моей топ моделью."
                "Видел-бы ты их глаза, Дик!"
                "Это было так смешно!"
                img 4685
                dick "А с какой моделью, Моника?"
                "Кто у тебя сейчас топ?"
                img 1418
                m "Мелани, Дик!
                Ты ее знаешь?"
                img 4686
                dick "Мелани?
                Это та самая?"
                dick "И ты видела ее обнаженной?"
                img 1418
                m "Дик, ты что, идиот?"
                "Она была в белье."
                "Но я видела ее обнаженной, естественно."
                "Ты ведь знаешь что я провожу немного унизительный осмотр всем моделям."
                "Это умеряет их гонор и учит дисциплине."
                img 4684
                m "Дик, ты бы себя сейчас видел!"
                "У тебя такое лицо...
                Ты что, хочешь трахнуть Мелани?"
                img 1428
                dick "Что ты, Моника?!"
                "Конечно нет!"
                "Мой идеал - это ты!"
                "Ты же знаешь!"
                $ dickWantFuckMelanie = True
            else:
                img 1418
                m "Я прогнала их, Дик!"
                "Какой же ты тупой иногда!"
                "Конец истории."
                img 1428
                w

        "Все пытаются отнять мое время... (disabled)" if monkeysOffended3 == True:
            jump dick_meeting1_restaurant_dialogue3_models_menu_loop1


    #entranceTalkedWithMonkeys
    #monkeysOffended1 - обозвать мартышками
    #monkeysOffended3 - полностью раздеться
    #melaniePhotoShotProcessed
    return
#

label dick_meeting1_restaurant_dialogue4_waitress():
    stop music fadeout 1.0
    sound plastinka
#          img 1421
    "Но я хотела бы вам напомнить, что мы скоро закрываемся."
    return

label dick_meeting1_restaurant_dialogue4_waitress_b():
    label dick_meeting1_restaurant_dialogue4_waitress_b_menu_loop1:
    menu:
        "Меня утомила эта стерва." if bitchmeterValue > maxBitchness / 2:
            music casualMusic
            img 1422
            m "Дик."
            call bitch(3, "waitressMonicaOffended1")
            $ waitressMonicaOffended1 = True
            "Меня утомила эта стерва."
            img 1423
            dick "..."

            img 1424
            m "Девушка!"
            "То что вы скоро закрываетесь."
            "Это очень плохо."
            "Вам следовало бы работать когда приходят такие гости как мы."
            img 1425
            waitress "Мэм."
            "Прошу прощения."
            "Но это не в моей компетенции."
            img 1426
            m "Конечно не в твоей."
            "В компетенцию официантки вообще ничего не входит."
            "Только приносить еду, которую она даже не готовит."
            "Потому что не умеет."
            "А также в компетенции убирать объедки."
            "Большего от тебя никто не ждет."

            "..."
            img 1427
            m "Дик!"
            dick "Да, дорогая."
            m "Давай уйдем отсюда."
            "Мне не нравится это место."
            "Но ваш заказ уже готов."
            img 1428
            dick "Хорошо, дорогая."
            "Как скажешь."
            "Можем уйти."
            img 1429
            m "Да, и я запрещаю тебе платить."
            img 1431
            w
            menu:
                "Уволь эту дуру.":
                    img 1430
                    m "А, и еще."
                    "Дик."
                    img 1432
                    dick "Да, дорогая."
                    img 1433
                    call bitch(5, "waitressMonicaFired")
                    $ waitressMonicaFired = True
                    m "Уволь эту дуру."

                    "В следующий раз, когда мы придем."
                    "Ее здесь не должно быть."
                    img 1434
                    dick "Хорошо, дорогая."
                    "Как скажешь. (улыбается)"

                    img 1435
                    waitress "Про что это они???"
                    "Да как они смеют?"
                    img 1436
                    m "Пойдем, Дик!"
                    dick "Пойдем, дорогая."

                "Пойдем, Дик!":
                    img 4689
                    m "Пойдем, Дик!"
                    dick "Пойдем, дорогая."
        "Меня утомила эта стерва. (Моника слишком добрая) (disabled)" if bitchmeterValue < maxBitchness / 2:
            jump dick_meeting1_restaurant_dialogue4_waitress_b_menu_loop1
        "Уже правда поздно?" if bitchmeterValue < maxBitchness / 2:
            music Last_Kiss_Goodnight
            img 4672
            m "Уже правда так поздно?"
            waitress "Да, Мэм."
            img 4673
            "Если честно, ресторан давно закрыт."
            m "Значит по этой причине мы сидим здесь одни?"
            waitress "Да, Мэм.
            Гостей уже не пускают сюда.
            Для вас сделано исключение."
            "Простите что напомнила вам о времени.
            Больше такого не повторится."
            "Я сейчас же принесу Ваш заказ."
            call bitch(-3, "waitressMonicaOffended1")
            img 4671
            m "Не стоит беспокоиться.
            Мы уже уходим."
            "Я не люблю сидеть в пустых ресторанах."
            img 4675
            m "Дик, ты не против если мы пойдем?"
            dick "Аэээмм.. Нет, Моника, я не против..."
            menu:
                "Оставить чаевые...":
                    img 4670
                    m "Девушка!"
                    "Судя по вашему виду, вы, наверное, работали с самого утра?"
                    waitress "Да, Мэм.
                    У меня уже неделю не было выходных."
                    "Уже поздно и мне завтра снова на работу с самого утра."
                    img 4676
                    m "Ясно."
                    "Деточка, видишь-ли, я пытаюсь доказать всем что я добрая и что я не тиран."
                    img 4675
                    "Я ведь не тиран, Дик?"
                    dick "Нет, Моника!
                    Конечно нет!"
                    call bitch(-5, "waitressMonicaTips")
                    $ waitressMonicaTips = True
                    img 4670
                    m "Вот. Поэтому этот мужчина с радостью оставит Вам в качестве чаевых ваш месячный оклад."
                    img 4678
                    m "Дик, ты ведь сделаешь это?"
                    img 1432
                    dick "(Дик поперхнулся)
                    Эгхммм... Моника..."
                    m "..."
                    dick "Конечно, с радостью.
                    Я думаю эта девушка заслуживает поощрения."
                    img 4675
                    m "То-то же."
                    img 4691
                    m "Пойдем, Дик!"
                    dick "Пойдем, дорогая."

                "Уйти...":
                    img 4690
                    m "Пойдем, Дик!"
                    dick "Пойдем, дорогая."

            #waitressMonicaTips
        "Уже правда поздно? (Моника слишком стерва) (disabled)" if bitchmeterValue > maxBitchness / 2:
            jump dick_meeting1_restaurant_dialogue4_waitress_b_menu_loop1

    $ richHotelReceptionEntered = False
    $ dickWaitingMonica3 = False
    $ dickWaitingMonica4 = True
    music casualMusic
    $ add_objective("dick_meeting1_goto_car", _("Сесть в машину"), c_blue, 25)
    $ autorun_to_object("street_rich_hotel", "dick_meeting1_car_parting1")
    call change_scene("rich_hotel_reception", "Fade_long")
    return
