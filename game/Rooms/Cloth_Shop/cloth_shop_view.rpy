default clothShopCashierOffended1 = False
default clothShopCashierOffended2 = False
default clothShopCashierOffended3ReturnDress = False
default clothShopCashierFirstNightOffended = False

default dressFitInProgress = False
default dressFitInProgressEnded = False
default dressFitOwnDressDressedOut = False
default eveningDressFitted = False
default clothShopInited = False
default dressMonicaPaid = False

default shopDressFit1Begin = False
default shopDressFit1End = False
default shopDressFit2Begin = False
default shopDressFit2End = False
default shopDressFit3Begin = False
default shopDressFit3End = False

default clothShopClothViewedV1C2 = False
default clothShopClothViewedV1C4 = False
default clothShopClothViewedV1C6 = False
default clothShopClothViewedV2C1 = False
default clothShopClothViewedV2C3 = False
default clothShopClothViewedV2C4 = False
default clothShopClothViewedV2C5 = False

default clothShopFittingCount = 0
default clothShopCashierTalkStage = 0
default clothShopCashierAtCashDesk = True

label cloth_shop_view1:
    $ print "enter_cloth_shop_view1"
    $ miniMapData = []

    $ scene_name = "cloth_shop_view1"
    $ scene_caption = _("Clothing Shop")
    $ clear_scene_from_objects(scene_name)

    $ scene_image = "scene_Cloth_Shop_View1"

    if dickBuyDressInProgress == True and dickDressBrought == False:
        $ add_object_to_scene("Cloth1", {"type":2, "base":"Cloth_Shop_View1_Cloth1", "click" : "cloth_shop_view1_environment", "actions" : "l", "zorder" : 1})
        $ add_object_to_scene("Cloth2", {"type":2, "base":"Cloth_Shop_View1_Cloth2", "click" : "cloth_shop_view1_environment", "actions" : "lw", "zorder" : 3})
        $ add_object_to_scene("Cloth3", {"type":2, "base":"Cloth_Shop_View1_Cloth3", "click" : "cloth_shop_view1_environment", "actions" : "l", "zorder" : 1})
        $ add_object_to_scene("Cloth4", {"type":2, "base":"Cloth_Shop_View1_Cloth4", "click" : "cloth_shop_view1_environment", "actions" : "lw", "zorder" : 0})
        $ add_object_to_scene("Cloth5", {"type":2, "base":"Cloth_Shop_View1_Cloth5", "click" : "cloth_shop_view1_environment", "actions" : "l", "zorder" : 0})
        $ add_object_to_scene("Cloth6", {"type":2, "base":"Cloth_Shop_View1_Cloth6", "click" : "cloth_shop_view1_environment", "actions" : "lw", "zorder" : 0})
        $ add_object_to_scene("Cloth7", {"type":2, "base":"Cloth_Shop_View1_Cloth7", "click" : "cloth_shop_view1_environment", "actions" : "l", "zorder" : 0})
        $ add_object_to_scene("Cloth8", {"type":2, "base":"Cloth_Shop_View1_Cloth8", "click" : "cloth_shop_view1_environment", "actions" : "l", "zorder" : 0})

        $ add_object_to_scene("Mannequin", {"type":2, "base":"Cloth_Shop_View1_Mannequin", "click" : "cloth_shop_view1_environment", "actions" : "l", "zorder" : 0})
        $ add_object_to_scene("Pouf1", {"type":2, "base":"Cloth_Shop_View1_Pouf1", "click" : "cloth_shop_view1_environment", "actions" : "l", "zorder" : 0})
        $ add_object_to_scene("Pouf2", {"type":2, "base":"Cloth_Shop_View1_Pouf2", "click" : "cloth_shop_view1_environment", "actions" : "l", "zorder" : 1})
        $ add_object_to_scene("Rack1", {"type":2, "base":"Cloth_Shop_View1_Rack1", "click" : "cloth_shop_view1_environment", "actions" : "l", "zorder" : 0})
        $ add_object_to_scene("Rack2", {"type":2, "base":"Cloth_Shop_View1_Rack2", "click" : "cloth_shop_view1_environment", "actions" : "l", "zorder" : 0})

    $ add_object_to_scene("Teleport_Cashier", {"type":2, "base":"Cloth_Shop_View1_Cashier", "click" : "cloth_shop_view1_teleport", "actions" : "lw", "zorder" : 0})
    $ add_object_to_scene("Teleport_Dressing_Room", {"type":2, "base":"Cloth_Shop_View1_DressingRoom", "click" : "cloth_shop_view1_teleport", "actions" : "lw", "zorder" : 0})
    $ add_object_to_scene("Teleport_View2", {"type":3, "text" : _("ИДТИ ДАЛЬШЕ"), "rarrow" : "arrow_up_2", "base":"Cloth_Shop_View1_Teleport_View2", "click" : "cloth_shop_view1_teleport", "xpos" : 183, "ypos" : 929, "zorder":11})
    $ add_object_to_scene("Teleport_Street_Cloth_Shop", {"type":3, "text" : _("НАЗАД НА УЛИЦУ"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "cloth_shop_view1_teleport", "xpos" : 960, "ypos" : 956, "zorder":11})

    if clothShopInited == False:
        call cloth_shop_init()

    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label cloth_shop_view1_teleport(obj_name, obj_data):
    if obj_name == "Teleport_View2":
        call change_scene("cloth_shop_view2")
        return
    if obj_name == "Teleport_Dressing_Room":
        if obj_data["action"] == "l":
            m "Там примерочная."
            "На вид какая-то убогая!"
            return
        if obj_data["action"] == "w":
            call change_scene("cloth_shop_dressing_room")
            return
    if obj_name == "Teleport_Cashier":
        if obj_data["action"] == "l":
            m "Насколько мне видно отсюда, там касса."
            "Не думаю что она понадобится мне в этом магазине!
            Если его можно так назвать вообще!"
            return
        if obj_data["action"] == "w":
            call change_scene("cloth_shop_cashier")
    if obj_name == "Teleport_Street_Cloth_Shop":
        if eveningDressFitted == True:
            if dressFitOwnDressDressedOut == True:
                mt "Я забыла забрать свое платье из примерочной.
                Оно стоит дороже всего этого магазина вместе взятого!"
                if dickDressBrought == False:
                    dick "Дорогая! Пойдем к кассе!
                    Нам надо заплатить за платье!"
                return
            if dickDressBrought == False:
                dick "Дорогая! Пойдем к кассе!
                Нам надо заплатить за платье!"
                return
        if dickBuyDressInProgress == True and dickDressBrought == False:
            if dressFitInProgress == True:
                mt "Я что, уйду отсюда с платьем на руках, не заплатив?"
                "Я никогда не опущусь до такого, клянусь!"
                "Этим занимаются только жалкие и никчемные неудачники! Я никогда не была и не буду одной из них!!!"
                return
            dick "Дорогая!
            Мы еще не все посмотрели!
            Может быть что-то подойдет?"
            return
        call change_scene("street_cloth_shop", "Fade_long")
        return
    return

label cloth_shop_view1_environment(obj_name, obj_data):

    if obj_name == "Mannequin":
        m "Какой-то менекен..."
        "Что на нем надето? Даже отсюда видно что какая-то ерунда!"
        return
    if obj_name == "Pouf1" or obj_name == "Pouf2":
        m "Цвет этого пуфика не гармонирует с цветом штор в примерочной."
        "Какая безвкусица!"
        return
    if obj_name == "Rack1":
        m "На том прилавке что-то лежит.
        Мне не видно отсюда."
        "Но не думаю что там что-то подходящее."
        return
    if obj_name == "Rack2":
        m "На том прилавке что-то лежит.
        Мне не видно отсюда."
        "Но не думаю что там что-то подходящее."
        return
    if obj_name == "Cloth1":
        m "Здесь нечего даже смотреть."
        return
    if obj_name == "Cloth2":
        #1361 view1 cloth2
        if clothShopClothViewedV1C2 == True:
            m "Я уже смотрела там..."
            return
        if obj_data["action"] == "l":
            m "Там сбоку, кажется, есть что посмотреть."
            return
        if obj_data["action"] == "w":
            if dressFitInProgress == True:
                m "Мне надо померять одно платье, прежде чем начинать мерять другое!"
                return
            sound highheels_short_walk
            img 1361
            with fade
            m "Давай попробую это, хотя я не уверена."
            img 4266
            dick "Да, дорогая!"
            img 4267
            dick "Пожалуйста, попробуй это!"
            sound highheels_short_walk
            $ scene_transition = "Fade"
            $ clothShopClothViewedV1C2 = True
            call clothShopCheckFinalFitting()
            return
        return
    if obj_name == "Cloth3":
        m "Мне прекрасно видно отсюда. Там нет ничего такого что бы я одела..."
        return
    if obj_name == "Cloth4":
        #1362 view1 cloth4
        if clothShopClothViewedV1C4 == True:
            m "Я уже смотрела там..."
            return
        if obj_data["action"] == "l":
            m "Кажется там сбоку еще стеллаж, на котором что-то интересное..."
            return
        if obj_data["action"] == "w":
            if dressFitInProgress == True:
                m "Мне надо померять одно платье, прежде чем начинать мерять другое!"
                return
            sound highheels_short_walk
            img 1362
            with fade
            m "Дик, ну что это такое?"
            "Это же вообще не модно!"
            img 4268
            dick "Эм, дорогая? Про что ты говоришь?"
            img 4269
            dick "Прости, я отвлекся..."

            sound highheels_short_walk
            $ scene_transition = "Fade"
            $ clothShopClothViewedV1C4 = True
            return
        return
    if obj_name == "Cloth5":
        m "Какие-то юбки для девочек..."
        return
    if obj_name == "Cloth6":
        #1363 view1 cloth6
        if clothShopClothViewedV1C6 == True:
            m "Я уже смотрела там..."
            return
        if obj_data["action"] == "l":
            m "Мне плохо видно отсюда, может быть там есть что-то стоящее?"
            return
        if obj_data["action"] == "w":
            if dressFitInProgress == True:
                m "Мне надо померять одно платье, прежде чем начинать мерять другое!"
                return
            sound highheels_short_walk
            img 1363
            with fade
            m "В этом магазине продается одежда для рабочих!"
            "И не более!"

            img 1364
            cashier "Нормальная у нас одежда."
            cashier "Ненавижу эту посетительницу."
            "Сучка."

            img 4270
            dick "Дорогая!"
            img 4271
            dick "Давай еще походим по магазину!"
            img 4272
            dick "Вдруг что-то найдем..?"

            sound highheels_short_walk
            $ scene_transition = "Fade"
            $ clothShopClothViewedV1C6 = True
            return
        return
    if obj_name == "Cloth7":
        m "Я отсюда вижу что там ерунда. Даже не собираюсь подходить смотреть..."
        return
    if obj_name == "Cloth8":
        m "Еще какие-то тряпки, Фи!..."
        return

    return

label cloth_shop_view2:
    $ print "enter_cloth_shop_view2"
    $ miniMapData = []

    $ scene_name = "cloth_shop_view2"
    $ scene_caption = _("Clothing Shop")
    $ clear_scene_from_objects(scene_name)

    $ scene_image = "scene_Cloth_Shop_View2"

    if dickBuyDressInProgress == True and dickDressBrought == False:
        $ add_object_to_scene("Cloth1", {"type":2, "base":"Cloth_Shop_View2_Cloth1", "click" : "cloth_shop_view2_environment", "actions" : "lw", "zorder" : 0})
        $ add_object_to_scene("Cloth2", {"type":2, "base":"Cloth_Shop_View2_Cloth2", "click" : "cloth_shop_view2_environment", "actions" : "l", "zorder" : 1})
        $ add_object_to_scene("Cloth3", {"type":2, "base":"Cloth_Shop_View2_Cloth3", "click" : "cloth_shop_view2_environment", "actions" : "lw", "zorder" : 0})
        $ add_object_to_scene("Cloth4", {"type":2, "base":"Cloth_Shop_View2_Cloth4", "click" : "cloth_shop_view2_environment", "actions" : "lw", "zorder" : 0})
        $ add_object_to_scene("Cloth5", {"type":2, "base":"Cloth_Shop_View2_Cloth5", "click" : "cloth_shop_view2_environment", "actions" : "lw", "zorder" : 0})
        $ add_object_to_scene("Cloth6", {"type":2, "base":"Cloth_Shop_View2_Cloth6", "click" : "cloth_shop_view2_environment", "actions" : "l", "zorder" : 0})

        $ add_object_to_scene("Pouf1", {"type":2, "base":"Cloth_Shop_View2_Pouf1", "click" : "cloth_shop_view2_environment", "actions" : "l", "zorder" : 0})

    $ add_object_to_scene("Teleport_Cashier", {"type":3, "text" : _("К КАССЕ"), "rarrow" : "arrow_right_2", "base":"Cloth_Shop_View2_Teleport_Cashier", "click" : "cloth_shop_view2_teleport", "xpos" : 1602, "ypos" : 917, "zorder":11})
    $ add_object_to_scene("Teleport_Cloth_Shop_View1", {"type":3, "text" : _("НАЗАД"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "cloth_shop_view2_teleport", "xpos" : 960, "ypos" : 956, "zorder":11})

    return
label cloth_shop_view2_teleport(obj_name, obj_data):
    if obj_name == "Teleport_Cloth_Shop_View1":
        call change_scene("cloth_shop_view1")
        return
    if obj_name == "Teleport_Cashier":
        call change_scene("cloth_shop_cashier")
        return
    return
label cloth_shop_view2_environment(obj_name, obj_data):
    if obj_name == "Pouf1":
        m "Зачем этот пуф здесь?
        Кто здесь будет сидеть посреди зала?"
        "Полная безвкусица!"
        return
    if obj_name == "Cloth1":
        #1356 view2 cloth1
        if clothShopClothViewedV2C1 == True:
            m "Я уже смотрела там..."
            return
        if obj_data["action"] == "l":
            m "Здесь висит какая-то ерунда, но за этим есть еще какой-то прилавок..."
            return
        if obj_data["action"] == "w":
            if dressFitInProgress == True:
                m "Мне надо померять одно платье, прежде чем начинать мерять другое!"
                return
            sound highheels_short_walk
            img 1356
            with fade
            m "О Боже!"
            "Дик!"
            "Что это за убожество?"
            "Куда ты меня привез?"
            img 4273
            dick "Дорогая!"
            img 4274
            dick "Пойдем посмотрим еще где-нибудь?"
            img 4275
            dick "Мне нравится ходить с тобой по магазину..."

            sound highheels_short_walk
            $ scene_transition = "Fade"
            $ clothShopClothViewedV2C1 = True
            return
        return
    if obj_name == "Cloth2":
        m "Фи! Какие-то тряпки!"
        return
    if obj_name == "Cloth3":
        #1357 view2 cloth3
        if clothShopClothViewedV2C3 == True:
            m "Я уже смотрела там..."
            return
        if obj_data["action"] == "l":
            m "Мне отсюда плохо видно, заслоняет другая одежда. Может стоит сходить посмотреть что там?"
            return
        if obj_data["action"] == "w":
            if dressFitInProgress == True:
                m "Мне надо померять одно платье, прежде чем начинать мерять другое!"
                return
            sound highheels_short_walk
            img 1357
            with fade
            m "Фи, здесь все не модно."
            "Что это вообще за лавочка?"
            img 4276
            dick "Дорогая, посмотри еще."
            img 4277
            "Вдруг что-то подойдет."
            img 4278
            w

            sound highheels_short_walk
            $ scene_transition = "Fade"
            $ clothShopClothViewedV2C3 = True
            return
        return
    if obj_name == "Cloth4":
        #1358 view2 cloth4
        if clothShopClothViewedV2C4 == True:
            m "Я уже смотрела там..."
            return
        if obj_data["action"] == "l":
            m "Отсюда плохо видно, может быть там есть что-то стоящее?"
            return
        if obj_data["action"] == "w":
            if dressFitInProgress == True:
                m "Мне надо померять одно платье, прежде чем начинать мерять другое!"
                return

            sound highheels_short_walk
            img 1358
            with fade
            m "Давай попробую."
            img 4279
            "Хотя бы вот это платье."
            img 4280
            w
            img 4281
            "Из жалости к тебе."

            sound highheels_short_walk
            $ scene_transition = "Fade"
            $ clothShopClothViewedV2C4 = True
            call clothShopCheckFinalFitting()
            return
        return
    if obj_name == "Cloth5":
        #1365 view2 cloth5
        if clothShopClothViewedV2C5 == True:
            m "Я уже смотрела там..."
            return
        if obj_data["action"] == "l":
            m "Это какая-то одежда для бедняков, но мне отсюда не видно что с обратной стороны..."
            return
        if obj_data["action"] == "w":
            if dressFitInProgress == True:
                m "Мне надо померять одно платье, прежде чем начинать мерять другое!"
                return
            sound highheels_short_walk
            img 1365
            with fade
            m "Давай попробую это."
            img 4282
            dick "Что, дорогая? А! Конечно, давай попробуем это платье!"
            img 4283
            dick "Прости, я отвлекся... чуть-чуть..."
            $ clothShopClothViewedV2C5 = True
            call clothShopCheckFinalFitting()
            return
        return
    if obj_name == "Cloth6":
        m "Одежда для бабушек...
        Фи!"
        return
    return


label cloth_shop_cashier:
    $ print "enter_cloth_shop_cashier"
    $ miniMapData = []

    $ scene_name = "cloth_shop_cashier"
    $ scene_caption = _("Cashier")
    $ clear_scene_from_objects(scene_name)

    $ scene_image = "scene_Cloth_Shop_Cashier"

    if clothShopCashierAtCashDesk == True:
        $ add_object_to_scene("Cashier", {"type":2, "base":"Cloth_Shop_Cashier_Character", "click" : "cloth_shop_cashier_environment", "actions" : "lt", "zorder" : 5})

    if s2ClothShopStage == 2:
        $ add_object_to_scene("Chocolate", {"type":2, "base":"Cloth_Shop_Cashier_Chocolate", "click" : "cloth_shop_view1_environment2", "actions" : "lh", "zorder" : 0})


    if dickBuyDressInProgress == True and dickDressBrought == False:
        $ add_object_to_scene("Computer", {"type":2, "base":"Cloth_Shop_Cashier_Computer", "click" : "cloth_shop_cashier_environment", "actions" : "l", "zorder" : 0})
        $ add_object_to_scene("Mannequins", {"type":2, "base":"Cloth_Shop_Cashier_Mannequins", "click" : "cloth_shop_cashier_environment", "actions" : "l", "zorder" : 0})
        $ add_object_to_scene("OtherDress", {"type":2, "base":"Cloth_Shop_Cashier_OtherDress", "click" : "cloth_shop_cashier_environment", "actions" : "l", "zorder" : 0})
        $ add_object_to_scene("Rack1", {"type":2, "base":"Cloth_Shop_Cashier_Rack1", "click" : "cloth_shop_cashier_environment", "actions" : "l", "zorder" : 0})
        $ add_object_to_scene("Rack2", {"type":2, "base":"Cloth_Shop_Cashier_Rack2", "click" : "cloth_shop_cashier_environment", "actions" : "l", "zorder" : 0})


    $ add_object_to_scene("Teleport_Dressing_Room", {"type":3, "text" : _("К ПРИМЕРОЧНОЙ"), "rarrow" : "arrow_right_2", "base":"empty", "click" : "cloth_shop_cashier_teleport", "xpos" : 1640, "ypos" : 152, "zorder":11})
    $ add_object_to_scene("Teleport_Cloth_Shop_View1", {"type":3, "text" : _("НАЗАД"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "cloth_shop_view2_teleport", "xpos" : 960, "ypos" : 956, "zorder":11})

    return
label cloth_shop_cashier_teleport(obj_name, obj_data):
    if obj_name == "Teleport_Cloth_Shop_View1":
        call change_scene("cloth_shop_view1")
        return
    if obj_name == "Teleport_Dressing_Room":
        call change_scene("cloth_shop_dressing_room")
        return


    return
label cloth_shop_cashier_environment(obj_name, obj_data):
    if obj_name == "Computer":
        m "Ха, компьютер!
        Надеюсь хоть этот работает?"
        "Но если нет, то знаю как заставить его заработать!"
        "Оказывается, я умею чинить компьютеры!
        Хи-хи"
        return
    if obj_name == "Mannequins":
        m "На этих манекенах висит нечто, что я даже не могу назвать одеждой, ни то что примерить это!"
        return
    if obj_name == "OtherDress":
        m "Что это за тряпка тут валяется?
        Эта продавец совершенно не умеет следить за порядком!"
        return
    if obj_name == "Rack1":
        m "Какие-то рубашки, мужские?"
        "О Боже!
        Как можно в одном магазине продавать товар и для этих жалких мужчин!"
        return
    if obj_name == "Rack2":
        m "Какие-то тряпки, я даже боюсь сказать что это.
        Это не магазин, это дыра!"
        return
    if obj_name == "Cashier":
        if obj_data["action"] == "l":
            img Cloth_Shop_Cashier2
            w
            img Cloth_Shop_Cashier3
            mt "Фу! Какая-то лесбиянка!"
            return
        if obj_data["action"] == "t":
            if clothShopCashierTalkStage == 2:
                call cashier_afterjail_day2_talk1()
                return
            if clothShopCashierTalkStage == 1:
                call dress_return_cashier_talk2()
                return
            if returnDressInProgress == True:
                call dress_return_cashier_talk1()
                return
            if eveningDressFitted == True:
                if dickDressBrought == True:
                    if clothShopCashierOffended2 == True:
                        img 1913
                        with fade
                        cashier "Добрый вечер, Мэм!"
                        "Вы решили еще что-нибудь подобрать?"
                        "Рады видеть Вас!"
                        m "Сомневаюсь что я еще что-то найду в вашей дыре!"
                        img 1398
                        cashier "Сучка!!!"
                        call refresh_scene_fade()
                        return
                    else:
                        img 1913
                        with fade
                        cashier "Добрый вечер, Мэм!"
                        "Вы решили еще что-нибудь подобрать?"
                        "Рады видеть Вас!"
                        m "Спасибо, я просто осматриваюсь."
                        call refresh_scene_fade()
                        return
                else:
                    call clothShopCheckFinalBuyDress()
                    return
                return
            img 1354
            with fade
            cashier "Вы что-то насмотрели, Мэм?"

            m "Сомневаюсь что я здесь что-то найду!"
            call refresh_scene_fade()
            return
    return

label cloth_shop_dressing_room:
    $ print "enter_cloth_shop_dressing_room"
    $ miniMapData = []

    $ scene_name = "cloth_shop_dressing_room"
    $ scene_caption = _("Dressing Room")
    $ clear_scene_from_objects(scene_name)

    $ scene_image = "scene_Cloth_Shop_Dressing_Room"
    if dickBuyDressInProgress == True and dickDressBrought == False:
        call cloth_shop_dressing_room_spawn1()

    $ add_object_to_scene("Teleport_Dressing_Room2", {"type":2, "base":"Cloth_Shop_Dressing_Room_Teleport_Dressing_Room2", "click" : "cloth_shop_dressing_room_teleport", "actions" : "lw", "zorder" : 0})

    if eveningDressFitted == False and dressFitOwnDressDressedOut == True:
        $ add_object_to_scene("Teleport_Cloth_Shop_View1", {"type":3, "text" : _("НАЗАД"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "cloth_shop_dressing_room_teleport", "xpos" : 960, "ypos" : 956, "zorder":11})
    else:
        $ add_object_to_scene("Teleport_Cloth_Shop_View1", {"type":3, "text" : _("НАЗАД"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "cloth_shop_view2_teleport", "xpos" : 960, "ypos" : 956, "zorder":11})

    return
label cloth_shop_dressing_room_spawn1:
    if shopDressFit1End == True:
        $ add_object_to_scene("DickTheLawyer", {"type":2, "base":"Cloth_Shop_Dressing_Room_Monica_Dick_Dress1_Dick", "click" : "cloth_shop_dressing_room_environment", "actions" : "lt", "zorder" : 5, "icon_t":"/Icons/talk" + res.suffix +".png"})
        $ add_object_to_scene("Monica", {"type":2, "base":"Cloth_Shop_Dressing_Room_Monica_Dick_Dress1_Monica", "click" : "cloth_shop_dressing_room_environment", "actions" : "l", "zorder" : 5})
        return
    if shopDressFit2End == True:
        $ add_object_to_scene("DickTheLawyer", {"type":2, "base":"Cloth_Shop_Dressing_Room_Monica_Dick_Dress2_Dick", "click" : "cloth_shop_dressing_room_environment", "actions" : "lt", "zorder" : 5, "icon_t":"/Icons/talk" + res.suffix +".png"})
        $ add_object_to_scene("Monica", {"type":2, "base":"Cloth_Shop_Dressing_Room_Monica_Dick_Dress2_Monica", "click" : "cloth_shop_dressing_room_environment", "actions" : "l", "zorder" : 5})
        return
    if shopDressFit3End == True:
        $ add_object_to_scene("DickTheLawyer", {"type":2, "base":"Cloth_Shop_Dressing_Room_Monica_Dick_Dress1_Dick", "click" : "cloth_shop_dressing_room_environment", "actions" : "lt", "zorder" : 5, "icon_t":"/Icons/talk" + res.suffix +".png"})
        $ add_object_to_scene("Monica", {"type":2, "base":"Cloth_Shop_Dressing_Room_Monica_Dick_Dress3", "click" : "cloth_shop_dressing_room_environment", "actions" : "l", "zorder" : 5})
        return
    $ add_object_to_scene("DickTheLawyer", {"type":2, "base":"Cloth_Shop_Dressing_Room_Dick", "click" : "cloth_shop_dressing_room_environment", "actions" : "lt", "zorder" : 5, "icon_t":"/Icons/talk" + res.suffix +".png"})
    return
label cloth_shop_dressing_room_teleport(obj_name, obj_data):
    if obj_name == "Teleport_Cloth_Shop_View1":
        if eveningDressFitted == False and dressFitOwnDressDressedOut == True:
            m "Мне надо переодеться в свое платье!"
            "Я не буду разгуливать по магазину в этом!"
            return
        return
    if obj_name == "Teleport_Dressing_Room2":
        if obj_data["action"] == "l":
            m "Мне как-то неприятно переодеваться в такой дыре.
            Я обнажаю свое тело только в роскошных местах, таких как мой дом!"
            return
        if obj_data["action"] == "w":
            if dressFitInProgress == True:
                img 4284
                m "Хорошо, Дик, я померяю это."
                img 4285
                dick "Дорогая, я очень рад!
                Пожалуйста, проходи!"
                img 4286
                m "..."
                img 4287
                dick "хе-хе..."
            call change_scene("cloth_shop_dressing_room2")
        return


    return
label cloth_shop_dressing_room_environment(obj_name, obj_data):
    if obj_name == "Monica":
        if eveningDressFitted == True:
            mt "Надо же!
            Я что-то смогла подобрать в этой дыре!"
            "Я теперь что, должна Дика похвалить?"
            "Еще чего!"
            return
        mt "Мне не нравится это место!"
        "Надо или что-то быстрее найти здесь или убираться!"
        "Дик все наставивает чтобы что-то найти...
        Он мне уже успел сегодня надоесть..."
        return
    if obj_name == "DickTheLawyer":
        if obj_data["action"] == "l":
            mt "Дик... Пытается угодить мне.
            Никчемное создание..."
            return
        if obj_data["action"] == "t":
            if eveningDressFitted == True:
                dick "Дорогая!
                Ты просто неотразима в этом платье!"
                "Пойдем к кассе! Я подарю тебе его!"
                m "Дик!
                Хватит подлизываться!
                Это бесполезно со мной!"
                return
            if dressFitInProgress == True:
                label DickTheLawyer_use_shop_dress:
                dick "Дорогая!
                Примерь это платье!"
                "Я уверен что оно подойдет тебе!"
                return
            dick "Дорогая! Давай посмотрим еще! Может быть что-то подойдет?"

            return
    return


label cloth_shop_dressing_room2:
    $ print "enter_cloth_shop_dressing_room2"
    $ miniMapData = []

    $ scene_name = "cloth_shop_dressing_room2"
    $ scene_caption = _("Dressing Room")
    $ clear_scene_from_objects(scene_name)

    if dressFitOwnDressDressedOut == True:
        $ scene_image = "scene_Cloth_Shop_Dressing_Room2_Dress"
        if s2ClothShopStage == 0:
            $ add_object_to_scene("Dress", {"type":2, "base":"Cloth_Shop_Dressing_Room2_Dress", "click" : "cloth_shop_dressing_room2_environment", "actions" : "lh", "zorder" : 0, "b":0.14})
    else:
        $ scene_image = "scene_Cloth_Shop_Dressing_Room2"
        if s2ClothShopStage == 0:
            $ add_object_to_scene("Hanger", {"type":2, "base":"Cloth_Shop_Dressing_Room2_Hanger", "click" : "cloth_shop_dressing_room2_environment", "actions" : "lh", "zorder" : 0})

    if dickBuyDressInProgress == True:
        pass

    if s2ClothShopStage == 0:
        $ add_object_to_scene("Mirror1", {"type":2, "base":"Cloth_Shop_Dressing_Room2_Mirror1", "click" : "cloth_shop_dressing_room2_environment", "actions" : "lh", "zorder" : 0})
        $ add_object_to_scene("Mirror2", {"type":2, "base":"Cloth_Shop_Dressing_Room2_Mirror2", "click" : "cloth_shop_dressing_room2_environment", "actions" : "lh", "zorder" : 0})
        $ add_object_to_scene("Pouf1", {"type":2, "base":"Cloth_Shop_Dressing_Room2_Pouf1", "click" : "cloth_shop_dressing_room2_environment", "actions" : "l", "zorder" : 0})
        $ add_object_to_scene("Pouf2", {"type":2, "base":"Cloth_Shop_Dressing_Room2_Pouf2", "click" : "cloth_shop_dressing_room2_environment", "actions" : "l", "zorder" : 0})
        $ add_object_to_scene("Pouf3", {"type":2, "base":"Cloth_Shop_Dressing_Room2_Pouf3", "click" : "cloth_shop_dressing_room2_environment", "actions" : "l", "zorder" : 0})
        $ add_object_to_scene("Sofa", {"type":2, "base":"Cloth_Shop_Dressing_Room2_Sofa", "click" : "cloth_shop_dressing_room2_environment", "actions" : "lh", "zorder" : 0})

    if s2ClothShopStage == 3:
        $ add_object_to_scene("Sofa", {"type":2, "base":"Cloth_Shop_Dressing_Room2_Sofa", "click" : "cloth_shop_view1_environment2", "actions" : "lh", "zorder" : 0})


    $ add_object_to_scene("Teleport_Dressing_Room", {"type":3, "text" : _("НАЗАД"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "cloth_shop_dressing_room2_teleport", "xpos" : 960, "ypos" : 956, "zorder":11})

    return
label cloth_shop_dressing_room2_teleport(obj_name, obj_data):
    if obj_name == "Teleport_Dressing_Room":
        if dressFitInProgress == True and dressFitInProgressEnded == False and dressFitOwnDressDressedOut == True:
            m "Я не пойду к Дику в таком виде!"
            "И вообще!"
            "Я никогда не разрешу ему увидеть меня в нижнем белье!"
            return
        if dressFitInProgress == True and dressFitInProgressEnded == False:
            m "Наверное мне надо померять это платье."
            "В конце концов, не зря же я пересилила себя и зашла в эту грязную вонючую примерочную!"
            "Вдруг платье подойдет мне?"
            return
        call change_scene("cloth_shop_dressing_room")
        return
    return
label cloth_shop_dressing_room2_environment(obj_name, obj_data):
    if obj_name == "Dress":
        if obj_data["action"] == "l":
            m "Хм... Мое платье."
            "Надеюсь оно не помнется и не испачкается на этом ржавом крючке?"
            return
        if obj_data["action"] == "h":
            if eveningDressFitted == True:
                m "Хорошо что я не забыла забрать свое сегодняшнее платье!"
                "Оно столько стоит, что я уверена, любой бы покупатель этой дыры продал бы душу дъяволу за то чтобы обладать им!"
                "Но меня не волнует не цена платья, а то что его бы присвоил кто-то не достойный его!"
                "Ничего себе! Носить платье самой Моники Бакфетт!"
                "Такое представить просто невозможно!"
                "Хи-хи."
                $ remove_objective("cloth_shop_forgot_own_dress")
                $ dressFitOwnDressDressedOut = False
                $ scene_transition = "Fade_long"
                $ scene_sound = "snd_fabric1"
                $ add_inventory("businesscloth1", 1, True)
                call refresh_scene()
                return
            if dressFitInProgressEnded == False:
                m "Надо померять это дурацкое платье."
                "Зря я что-ли сняла свое изысканное и дорогое и повесила на этот ржавый крючок?"
                return
            call clothShopCheckFinalFittingDressInOwnDress()
            return

    if obj_name == "Hanger":
        if obj_data["action"] == "l":
            m "Вешалка для одежды. Хорошо что не ржавая..."
        if obj_data["action"] == "h":
            if dressFitInProgress == True and dressFitOwnDressDressedOut == False:
                call clothShopCheckFinalFittingOwnDressOut()
                return
            m "Зачем мне вешать туда свое платье?
            Просто так?!!"
            return
        return
    if obj_name == "Mirror1":
        if obj_data["action"] == "l":
            m "Наверное туда надо смотреть если я буду что-то примерять.
            ЕСЛИ..."
            return
        if obj_data["action"] == "h":
            if dressFitInProgress == False:
                m "Мне нечего мерять здесь... Что я вообще здесь делаю?"
                return
            call clothShopCheckFinalFitting2()
            return
        return
    if obj_name == "Mirror2":
        if obj_data["action"] == "l":
            m "Наверное туда надо смотреть если я буду что-то примерять.
            ЕСЛИ..."
            return
        if obj_data["action"] == "h":
            if dressFitInProgress == False:
                m "Мне нечего мерять здесь... Что я вообще здесь делаю?"
                return
            call Mirror1_use_shop_dress()
            return
        return
    if obj_name == "Pouf1":
        m "Серый пуф...
        Или он должен быть белым?
        Не удивлюсь если в этой дыре он посерел!"
        return
    if obj_name == "Pouf2":
        m "Черный пуф."
        "Безвкусица..."
        return
    if obj_name == "Pouf3":
        m "Красный пуф..."
        "Кто собрал вместе эти пуфы?
        Это полное отсутствие цветовой гармонии!"
        return
    if obj_name == "Sofa":
        if obj_data["action"] == "l":
            m "Какой-то жуткий диван!"
            "Потертый на вид. Уверена что он скрипит!"
            "Буду держаться от него подальше, чтобы не испачкаться!"
            return
        if obj_data["action"] == "h":
            m "Я не притронусь к нему!"
            return
        return
    return

label Mirror1_use_shop_dress:
label Mirror2_use_shop_dress:
    if dressFitOwnDressDressedOut == False:
        m "Мне надо сначала раздеться прежде чем одевать что-то другое!"
        return
    call clothShopCheckFinalFitting2()
    return


label cloth_shop_dressing_room3:
    $ print "enter_cloth_shop_dressing_room3"
    $ miniMapData = []

    $ scene_name = "cloth_shop_dressing_room3"
    $ scene_caption = _("Dressing Room")
    $ clear_scene_from_objects(scene_name)

    if shopDressFit1End == True:
        $ scene_image = "scene_Cloth_Shop_Dressing_Room3_1"
        $ add_object_to_scene("Monica", {"type":2, "base":"Cloth_Shop_Dressing_Room3_Monica1", "click" : "cloth_shop_dressing_room3_environment", "actions" : "l", "zorder" : 5})
    if shopDressFit2End == True:
        $ scene_image = "scene_Cloth_Shop_Dressing_Room3_2"
        $ add_object_to_scene("Monica", {"type":2, "base":"Cloth_Shop_Dressing_Room3_Monica2", "click" : "cloth_shop_dressing_room3_environment", "actions" : "l", "zorder" : 5})

    $ add_object_to_scene("Teleport_Dressing_Room", {"type":3, "text" : _("ПОКАЗАТЬСЯ ДИКУ"), "rarrow" : "arrow_down_2", "base":"Cloth_Shop_Dressing_Room3_Teleport_Dressing_Room", "click" : "cloth_shop_dressing_room3_teleport", "xpos" : 1213, "ypos" : 88, "zorder":11})

    $ add_object_to_scene("Pouf1", {"type":2, "base":"Cloth_Shop_Dressing_Room3_Pouf1", "click" : "cloth_shop_dressing_room2_environment", "actions" : "l", "zorder" : 12})
    $ add_object_to_scene("Sofa", {"type":2, "base":"Cloth_Shop_Dressing_Room3_Sofa", "click" : "cloth_shop_dressing_room2_environment", "actions" : "lh", "zorder" : 0})


    return
label cloth_shop_dressing_room3_teleport(obj_name, obj_data):
    if obj_name == "Teleport_Dressing_Room":
        call clothShopCheckFinalFitting3()
        call change_scene("cloth_shop_dressing_room", "Fade", False)
        return
    return
label cloth_shop_dressing_room3_environment(obj_name, obj_data):
    if obj_name == "Monica":
        m "Не уверена насчет этого платья."
        "Ладно, посмотрим что скажет Дик."
        "Хотя какой у него вкус..?
        У него нет его."
    return


label clothShopCheckFinalFitting:
    $ clothShopFittingCount += 1
    if clothShopFittingCount == 1:
        $ add_inventory("shop_dress1", 1, True)
        $ shopDressFit1Begin = True
    if clothShopFittingCount == 2:
        $ add_inventory("shop_dress2", 1, True)
        $ shopDressFit2Begin = True
    if clothShopFittingCount == 3:
        $ add_inventory("shop_dress_eveningdress", 1, True)
        $ shopDressFit3Begin = True
    $ dressFitInProgress = True
    $ dressFitInProgressEnded = False
    $ add_objective("cloth_shop_fit_dress", _("Померять платье в примерочной"), c_green, 25)
    return

label clothShopCheckFinalFittingOwnDressOut:
    if shopDressFit1Begin == True:
        music Loved_up
        img 4288
        w
        img 4289
        w
        img 4304
        dick "Вау!!!"
        img 4290
        w
        img 4291
        w
        img 4292
        w
        img 4293
        w
        img 4294
        w
        img 4295
        w
        sound snd_fabric1
        img 4296
        w
        img 4297
        w
        $ dressFitOwnDressDressedOut = True
        menu:
            "Полюбоваться собой в зеркало.":
                img 4298
                w
                img 4299
                w
                img 4300
                w
                img 4301
                w
                img 4302
                w
                img 4303
                w
                img 4304
                w
                img 4305
                w
                img 4306
                w
                img 4307
                w
                img 4308
                w
                img 4309
                w
            "Не заниматься ерундой":
                img 4309
                w
        music casualMusic
        $ scene_transition = "Fade"
        call refresh_scene()
        return
    if shopDressFit2Begin == True:
        music Loved_up
        img 4288
        w
        img 4289
        w
        img 4304
        dick "Вау!!!"
        img 4290
        w
        img 4291
        w
        img 4292
        w
        img 4293
        w
        img 4294
        w
        img 4295
        w
        img 4320
        w
        $ dressFitOwnDressDressedOut = True
        menu:
            "Полюбоваться собой в зеркало.":
                img 4321
                w
                img 4322
                w
                img 4323
                w
                img 4324
                w
                img 4304
                dick "Вау!!!"
                img 4325
                w
                img 4326
                w
                img 4327
                w
                img 4328
                w
                img 4329
                w
            "Не заниматься ерундой":
                img 4321
                w
        music casualMusic
        $ scene_transition = "Fade"
        call refresh_scene()
        return
    if shopDressFit3Begin == True:
        music Loved_up
        img 4288
        w
        img 4289
        w
        img 4290
        w
        img 4291
        w
        img 4292
        w
        img 4293
        w
        img 4294
        w
        img 4295
        w
        img 4343
        w
        $ dressFitOwnDressDressedOut = True
        menu:
            "Полюбоваться собой в зеркало.":
                img 4344
                w
                img 4345
                dick "Вау!!!"
                img 4346
                w
                img 4347
                w
                img 4348
                w
            "Не заниматься ерундой":
                pass
        music casualMusic
        $ scene_transition = "Fade"
        call refresh_scene()
        return
    return

label clothShopCheckFinalFitting2:
    if shopDressFit1Begin == True:
        menu:
            "Надеть платье быстро.":
                sound snd_fabric1
                img 1359
                w
            "Надевать платье неспеша, чтобы не помять и ничего не зацепить на нем.":
                music Loved_up
                img 4310
                w
                img 4311
                w
                img 1359
                w
                music casualMusic

        $ remove_inventory("shop_dress1", 1)
        $ shopDressFit1Begin = False
        $ shopDressFit1End = True
        $ dressFitInProgressEnded = True
    if shopDressFit2Begin == True:
        menu:
            "Надеть платье быстро.":
                sound snd_fabric1
                img 1366
                w
            "Надевать платье неспеша, чтобы не помять и ничего не зацепить на нем.":
                music Loved_up
                img 4330
                w
                img 4332
                w
                img 4333
                w
                img 4334
                w
                img 4335
                w
                img 4336
                w
                img 4337
                w
                img 4338
                w
                img 1366
                w
                music casualMusic
        $ remove_inventory("shop_dress2", 1)
        $ shopDressFit2Begin = False
        $ shopDressFit2End = True
        $ dressFitInProgressEnded = True
    if shopDressFit3Begin == True:
        menu:
            "Надеть платье быстро.":
                music Loved_up
                img 4349
                with fadelong
                w
                img 4350
                w
                sound snd_fabric1
                stop music fadeout 1.0
                img 4351
                m "Упс!!!"
                img 4352
                music Molten_Alloy
                m "Что там?"
                img 4353
                with dissolve
                m "Мои трусики!
                Дьявол!"
                m "Я поспешила надеть это дурацкое платье и зацепила им за трусики!!!"
                img 4355
                w
                img 4356
                w
                img 4304
                dick "ОГО!!!"
                img 4357
                w
                img 4358
                m "Дьявол!
                Я запуталась в этом платье!"
                "Ничего! Сейчас я дотянусь!"
                menu:
                    "Дотянуться аккуратно.":
                        img 4359
                        with fadelong
                        w
                        img 4360
                        w
                        music casualMusic
                        img 4368
                        m "Все, инцидент исчерпан!"

                    "Дотянуться резко. Я что, собираюсь тут вечно стоять без трусиков???":
                        img 4361
                        with fadelong
                        m "Дурацкое платье! Я запуталась!"
                        img 4362
                        m "Надо потянуться еще посильнее..."
                        img 4304
                        dick "Вот это да!!! У нее грудь и правда на миллиард долларов!"

                        img 4359
                        w
                        img 4360
                        w
                        img 4363
                        m "Так-то лучше."
                        m "Все, инцидент исчерпан!"
                        img 4364
                        m "ЧТООООО????"
                        m "Дьявол!
                        Из-за того что я сильно потянулась, это дурацкое платье сползло с моей груди!"
                        img 4365
                        w
                        img 4366
                        w
                        music casualMusic
                        img 4367
                        w
                        img 4368
                        w

            "Надевать платье неспеша, чтобы не помять и ничего не зацепить на нем.":
                music Loved_up
                img 4349
                with fadelong
                w
                img 4350
                w
                img 4368
                w

        music casualMusic
        $ remove_inventory("shop_dress_eveningdress", 1)
        img 4369
        call question_helper_disable()

        m "Дурацкое платье!"
        "Хотя... оно довольно красиво..."
        "Надо застегнуть застежку..."
        sound snd_fabric1
        img 1369
        with fadelong
        mt "Черт, где же тут эта застежка."
        img 1370
        mt "Ну же, давай, застегивайся."
        img 1371
        w
        img 1372
        mt "..."
        sound highheels_short_walk
        img 1373
        with fadelong
        m "О!"
        "Дик!"
        "Ты что это делаешь?"
        "Подглядываешь за мной?"
        dick "Нет, дорогая."
        "Я просто хотел проверить что у тебя все в порядке."
        m "Что у меня может быть не в порядке в какой-то примерочной?"
        "Я же здесь не собираюсь жить!"
        "Зашла на минуту, а ты уже собрался проверять меня!"

        img 1374
        "..."
        "Смотри, нравится тебе это платье?"
        dick "Да, дорогая."
        "Тебе оно очень идет."
        "Может быть мы возьмем его и поедем."
        "Уже много времени."
        "Скоро начнет закрываться ресторан."
        m "Хорошо, я возьму это платье."
        "..."
        img 1375
        m "Ты возьмешь."
        dick "Конечно, Моника."
        $ changeDayTime("evening")
        $ cloth = "EveningDress"
        $ shopDressFit3Begin = False
        $ shopDressFit3End = True
        $ remove_objective("dick_cloth_shop_buy_dress")
        $ remove_objective("cloth_shop_fit_dress")
        $ add_objective("cloth_shop_buy_dress_cashier", _("Купить вечернее платье"), c_pink, 25)
        $ eveningDressFitted = True
        $ dressFitInProgress = False
        $ autorun_to_object("cloth_shop_cashier", "clothShopCheckFinalBeforeBuyDress")
        call change_scene("cloth_shop_dressing_room", "Fade", False)
        return
    $ remove_objective("cloth_shop_fit_dress")
    $ dressFitInProgress = False
    $ add_objective("cloth_shop_fit_dress_show_dick", _("Показаться Дику"), c_white, 25)
    $ remove_objective("cloth_shop_fit_dress")
    call change_scene("cloth_shop_dressing_room3", "Fade_long", "snd_fabric1")
    return

label clothShopCheckFinalFitting3:
    sound highheels_short_walk
    if shopDressFit1End == True:
        img 1360
        with fadelong
        m "Как тебе это платье?"
        img 4314
        dick "Вау!"
        img 4315
        dick "По-моему замечательно!"
        img 4316
        m "Не подлизывайся, Дик!"
        "Я же вижу что оно мне не идет."
        menu:
            "Дик! Если это лучшее что мы здесь найдем, то нам лучше уйти!":
                call bitch(1, "dick_cloth_shop_dress1")
                img 4317
                m "Дик! Если это лучшее что мы здесь найдем, то нам лучше уйти!"
                img 4318
                dick "Дорогая! Это платье прекрасно подходит тебе!"
                m "Нет, Дик!"
                img 4319
                m "..."
                "Ладно, Дик!
                Уговорил!"
                "Давай посмотрим еще."
            "Давай посмотрим еще.":
                call bitch(-1, "dick_cloth_shop_dress1")
                m "Давай посмотрим еще."
        $ remove_objective("cloth_shop_fit_dress_show_dick");
    if shopDressFit2End == True:
        img 1367
        with fadelong
        m "Как тебе это платье?"
        dick "Это платье определенно лучше чем предыдущее."
        m "Думаешь?"

        menu:
            "Мне ничего здесь не нравится!":
                call bitch(1, "dick_cloth_shop_dress2")
                img 4340
                m "Дик!
                Мне не нравится это платье!"
                "Это уже вторая вещь, которую я здесь меряю!"
                "И она такая же уродливая как и все здесь вокруг."
                img 4341
                m "Ты не ошибся, дорогой?"
                "Может у тебя есть другие идеи?"
                img 4340
                dick "Моника, дорогая!
                Пожалуйста!"
                "Давай еще посмотрим!"
                "Ну... еще один разок, последний!"
                img 4342
                m "Хорошо, Дик!"
                "Но только последний..."
                dick "Конечно, дорогая!
                Как ты скажешь!"
            "Посмотрю еще.":
                call bitch(-1, "dick_cloth_shop_dress2")
                img 1368
                m "Ну..."
                "Не знаю...."
                "Посмотрю еще."
        $ remove_objective("cloth_shop_fit_dress_show_dick");
    if shopDressFit3End == True:
        pass
    return

label clothShopCheckFinalFittingDressInOwnDress:
    if shopDressFit3End == True:
        pass
#        add_inventory("businesscloth1", 1, True)
#        $ dressFitOwnDressDressedOut = False
#        $ shopDressFit3Begin = False
#        $ shopDressFit3End = False
    else:
        if shopDressFit2End == True:
            m "Одену свое платье.
            В нем гораздо удобнее!"
            sound snd_fabric1
            $ dressFitOwnDressDressedOut = False
            $ shopDressFit2Begin = False
            $ shopDressFit2End = False
        else:
            if shopDressFit1End == True:
                img 4313
                with fade
                m "Одену свое платье.
                В нем гораздо удобнее!"
                sound snd_fabric1
                $ dressFitOwnDressDressedOut = False
                $ shopDressFit1Begin = False
                $ shopDressFit1End = False
    $ scene_transition = "Fade"
    sound snd_fabric1
    call refresh_scene()
    return

label clothShopCheckFinalBeforeBuyDress:
    music Marty_Gots_a_Plan
    img 1376
    with fadelong
    m "Дик."
    dick "Да, дорогая."

    menu:
        "Дик. Зачем ты подглядывал за мной?":
            $ dickClothShopOffended1 = True
            call bitch(5, "dick_cloth_shop_peeping_dialogue1")
            m "Дик.
            Скажи."

            m "Зачем ты подглядывал за мной?"

            img 1377
            dick "Дорогая, я уже говорил."
            "Я хотел проверить все-ли у тебя в порядке."
            img 1378
            m "Дик, не ври мне."
            "Я прекрасно понимаю что у тебя на уме."
            "Можно задать вопрос, а ты честно ответишь на него."

            img 1377
            dick "Конечно..."

            img 1379
            m "Ты ведь хочешь переспать со мной?"
            "Верно?"
            img 1377
            dick "Моника... Я..."
            img 1379
            m "Не увиливай, скажи прямо да или нет."

            img 1380
            dick "Ну, вообще-то, да."

            music casualMusic
            menu:
                "Дик, ты же уродливый. Посмотри на себя.":
                    $ dickClothShopOffended2 = True
                    call bitch(5, "dick_cloth_shop_peeping_dialogue2")
                    img 1381
                    m "О Боже, Дик, Дик."
                    "Ну посмотри на себя."
                    "Ты жирный и уродливый."
                    "Как вообще ты себе представляешь что такая девушка как я будет заниматься с тобой этим?"

                    img 1382
                    m "Посмотри на свой уродливый галстук!"

                    img 1383
                    m "Где твой вкус?"
                    "Мы общаемся только потому что ты решаешь мои дела."

                "Дик, это невозможно.":
                    img 1389
                    m "Ты считаешь что я буду спать с мужчиной у которго такой смешной галстук?"
                    "Да, Дик?"

            img 1384
            dick "Моника.. Я..."

            img 1385
            m "Ты знаешь, Дик, что вообще-то я замужем."
            "Ты ведь знаешь это?"

            img 1380
            dick "Да..."
            img 1385
            m "И это тебя не смущает?"

            img 1386
            m "А ты знаешь что я вообще не люблю секс?"
            "Я не понимаю что в нем вообще такого."
            "Это любят только мужчины."

            img 1387
            m "Мы с мужем занимались этим всего пару раз за все время."

            img 1388
            m "И то только тогда, когда мне что-то было от него нужно."
            "..."
            "..."

            img 1389
            m "Что молчишь?"

            img 1390
            dick "Моника, дорогая."
            "Скажи, мой вес это правда проблема?"
            "Я могу пойти заниматься в спортзал и ...."

            img 1391
            m "Да, Дик!"
            "Это проблема!"
            "И, пока ты это не решишь, в любом случае это будет оставаться проблемой."

            img 1389
            m "А ты ведь знаешь что мне не нужны люди с проблемами."
            "..."

            img 1392
            m "И вообще, как я уже сказала."
            "Мне секс неинтересен."
            "Ни с тобой, ни с кем-либо еще."
            "И на этом закроем эту тему раз и навсегда."

            img 1393
            dick "Хорошо, Моника."
            "Как скажешь."
            "Давай я заплачу за платье?"

            menu:
                "Я сама могу о себе позаботиться.":
                    $ dickClothShopOffended3 = True
                    call bitch(1, "dick_cloth_shop_peeping_dialogue3")
                    $ dressMonicaPaid = True
                    img 1392
                    m "Я сама могу о себе позаботиться."
                "Если тебе это так нужно, то плати.":
                    img 1391
                    m "Если тебе это так нужно, то плати."
                    "Но учти что твои деньги мне не нужны.
                    У меня их гораздо больше чем у тебя!"
                    img 1393
                    dick "Да, Моника, я знаю..."


        "У тебя смешной галстук, Дик!":
            img 1389
            m "У тебя смешной галстук, Дик!"
            img 1383
            dick "Моника.. Я..."
            img 1384
            dick "Ты так правда считаешь? Он смешной?"
            m "Да, Дик! Определенно!"
            img 1391
            "Тебе нужен кто-то кто купит тебе новый галстук!"
            music casualMusic
            img 1385
            "И это определнно буду не я!"
            dick "Да, Моника, я понимаю..."
            "Конечно."
            "Пойдем я оплачу тебе платье?"

            menu:
                "Я сама могу о себе позаботиться.":
                    $ dickClothShopOffended3 = True
                    call bitch(1, "dick_cloth_shop_peeping_dialogue3")
                    $ dressMonicaPaid = True
                    img 1392
                    m "Я сама могу о себе позаботиться."
                "Если тебе это так нужно, то плати.":
                    img 1391
                    m "Если тебе это так нужно, то плати."
                    "Но учти что твои деньги мне не нужны.
                    У меня их гораздо больше чем у тебя!"
                    img 1393
                    dick "Да, Моника, я знаю..."


    return

label clothShopCheckFinalBuyDress:
    $ shopDressFit3End = False
    menu:
        "Общаться с продавцом грубо.":
            $ clothShopCashierOffended2 = True
            call bitch(2, "clothShopCashierOffended2")
            img 1394
            with fadelong
            if dressMonicaPaid == True:
                m "Я беру это платье."
                "Возьмите деньги."
            else:
                m "Я беру это платье."
                m "Этот мужчина заплатит за него."
                "Возьмите деньги."

            img 1395
            cashier "Да, Мэм."
            "Спасибо за покупку."

            img 1396
            m "Я знаю.
            Я заслужила ваше спасибо."

            "Небось я единственный покупатель в этой дыре."
            "Не представляю кто тут может что-то покупать."
            "Да и думаю вы своим видом распугали даже тех покупателей которые могли бы придти."

            img 1397
            cashier "Мэм, еще раз спасибо за покупку (улыбается)"

            img 1398
            cashier "Сучка!!!"

        "Общаться с продавцом более вежливо (насколько Моника вообще умеет).":
            call bitch(-2, "clothShopCashierOffended2")
            img 4371
            with fadelong
            if dressMonicaPaid == True:
                m "Добрый вечер еще раз."
                m "Я беру это платье."
                "Возьмите деньги."
            else:
                m "Добрый вечер еще раз."
                m "Я беру это платье."
                m "Этот мужчина заплатит за него."
                "Возьмите деньги."
            img 1395
            cashier "Да, Мэм."
            "Спасибо за покупку."

            img 4371
            m "Хоть это и дыра, но я смогла найти что-то что мне понравилось."
            "Так что вы молодец."
            img 1397
            cashier "Мэм, еще раз спасибо за покупку (улыбается)"
    $ remove_objective("cloth_shop_buy_dress_cashier")

    menu:
        "Подшутить над Диком.":
            music Poppers_and_Prosecco
            $ dickClothShopOffended4 = True
            call bitch(1, "dickClothShopOffended4")
            img 1399
            m "Идем, Дик."
            "Идем, мой плюшевый мишка."

        "Взять Дика за руку и пойти.":
            music Poppers_and_Prosecco
            call bitch(-1, "dickClothShopOffended4")
            img 4372
            m "Идем, Дик."
            m "Идем, мой кавалер."
            mt "Хи-хи."

    $ dickBuyDressInProgress = False
    $ dickDressBrought = True
    call dick_meeting1_after_cloth_shop_init()
    if dressFitOwnDressDressedOut == False:
        call change_scene("street_cloth_shop", "Fade_long")
    else:
        $ add_objective("cloth_shop_forgot_own_dress", _("Забрать свое платье из примерочной"), c_green, 25)
        $ autorun_to_object("cloth_shop_view1", "clothShopForgotOwnDress")
        call change_scene("cloth_shop_view1", "Fade_long")
    return

label clothShopForgotOwnDress:
    m "Дьявол!
    Я забыла свое платье в примерочной!"
    "Дик!
    Иди на улицу, я догоню тебя!"
    dick "Но Моника, давай я пойду с тобой!"
    m "Дик, не мешайся под ногами!
    Делай что я сказала!"
    return

label cloth_shop_init:
    $ define_inventory_object("shop_dress1", {"description" : _("Платье для примерки"), "label_suffix" : "_use_shop_dress", "default_label" : False, "default_nolabel" : "cant_use", "icon" : "Inventory/shop_dress1" + res.suffix + ".png"})
    $ define_inventory_object("shop_dress2", {"description" : _("Платье для примерки"), "label_suffix" : "_use_shop_dress", "default_label" : False, "default_nolabel" : "cant_use", "icon" : "Inventory/shop_dress2" + res.suffix + ".png"})
    $ define_inventory_object("shop_dress_eveningdress", {"description" : _("Вечернее платье"), "label_suffix" : "_use_shop_dress", "default_label" : False, "default_nolabel" : "cant_use", "icon" : "Inventory/shop_dress_eveningdress" + res.suffix + ".png"})
    # $ add_inventory("phone", 1, True)
    return
