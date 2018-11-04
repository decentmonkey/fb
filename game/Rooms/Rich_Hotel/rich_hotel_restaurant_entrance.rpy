label rich_hotel_restaurant_entrance:

    $ print "enter_rich_hotel_restaurant_entrance"
    $ miniMapData = []

    $ scene_name = "rich_hotel_restaurant_entrance"
    $ scene_caption = _("Restaurant")
    $ clear_scene_from_objects(scene_name)
    $ scene_image = "scene_Rich_Hotel_Restaurant_Entrance_Monica_" + cloth

    $ add_object_to_scene("Monica", {"type":2, "base":"rich_hotel_restaurant_entrance_Monica_" + cloth, "click" : "rich_hotel_restaurant_entrance_environment", "actions" : "l", "zorder" : 10})
    if waitressMonicaOffended1 == True:
        $ add_object_to_scene("Waitress", {"type":2, "base":"rich_hotel_restaurant_entrance_Waitress_Angry", "click" : "rich_hotel_restaurant_entrance_environment", "actions" : "lt", "zorder" : 10})
    else:
        $ add_object_to_scene("Waitress", {"type":2, "base":"rich_hotel_restaurant_entrance_Waitress_Smile", "click" : "rich_hotel_restaurant_entrance_environment", "actions" : "lt", "zorder" : 10})
    $ add_object_to_scene("Teleport_Reception", {"type":3, "text" : _("РЕЦЕПШИН"), "larrow" : "arrow_left_2", "base":"Screen_Left_Arrow_Tight", "click" : "rich_hotel_restaurant_entrance_teleport", "xpos" : 220, "ypos" : 545, "zorder":11})

    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label rich_hotel_restaurant_entrance_teleport(obj_name, obj_data):
    if obj_name == "Teleport_Reception":
        call change_scene("rich_hotel_reception", "Fade", "highheels_short_walk")
    return
label rich_hotel_restaurant_entrance_environment(obj_name, obj_data):
    if obj_name == "Monica":
        mt "Вот и ресторан.
        Куда меня приводил Дик..."
    if obj_name == "Waitress":
        if obj_data["action"] == "l":
            if gameStage == 2:
                if waitressMonicaOffended1 == True:
                    mt "А, это та дура, которая не могла принести нам еду вовремя..."
                    if waitressMonicaFired == True:
                        mt "Дик пока не уволил ее?"
                else:
                    mt "Это та официантка, которая работает без выходных..."
                return

            if waitressMonicaOffended1 == True:
                mt "А, это та дура, которая не могла принести нам еду вовремя..."
                if waitressMonicaFired == True:
                    mt "Дик пока не уволил ее?
                    Надо будет проверить через пару дней."
                    "Если она все еще будет здесь, Дику не поздоровится!"
            else:
                mt "Это та официантка, которая работает без выходных..."
                if waitressMonicaTips == True:
                    mt "Надеюсь чаевых ей хватит на то чтобы отправиться в отпуск и отдохнуть..."
        if obj_data["action"] == "t":
            if gameStage == 2:
                if waitressMonicaOffended1 == True:
                    waitress "Мэм... Хотели куда-нибудь присесть?"
                    m "Скажите, здесь есть кто-нибудь из начальства?"
                    waitress "Мэм, сейчас за старшую администратор на рецепшине."
                    "Вы можете обратиться к ней."
                    m "К этой сучке?"
                    "НИКОГДА!!!"
                    waitress "Мэм?"
                else:
                    waitress "Мэм... Хотели куда-нибудь присесть?"
                    m "Скажите, вы знаете место где можно переночевать?"
                    waitress "Вы можете переночевать здесь, Мэм!"
                    "У нас прекрасный отель!"
                    m "Скажите, вы можете меня заселить?"
                    waitress "Мэм, заселением занимается администратор."
                    m "А вы лично можете?"
                    "Не обязательно уведомлять об этом администратора."
                    waitress "Мэм, я не могу на это пойти!"
                    m "Хорошо, а у вас дома есть свободное место?"
                    "Одному знакомому человеку надо переночевать."
                    waitress "Мэм, сожалею, но нет!"
                    if waitressMonicaTips == True:
                        m "Но я же оставляла чаевые тебе!"
                        "Как ты можешь мне отказать?"
                        waitress "Мэм, большое спасибо за чаевые!"
                        "Я Вам очень благодарна!"
                    mt "СУЧКА!!!"
                return
            if waitressMonicaOffended1 == True:
                waitress "Мэм... Хотели куда-нибудь присесть?"
                m "Вот еще!
                Ноги моей не будет в вашем дурацком пустом ресторане!"
            else:
                waitress "Мэм! Здравствуйте!
                Рада видеть Вас!"
                if day_time == "evening":
                    waitress "Уже вечер, но для Вас мы будем работать сколько потребуется!"
                m "Спасибо...
                В другой раз...
                Я просто проходила мимо."


return
