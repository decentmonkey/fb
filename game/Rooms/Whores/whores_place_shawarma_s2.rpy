
label whores_place_shawarma_s2:
    $ print "enter_whores_place_shawarma_s2"
    $ miniMapData = []

    $ scene_name = "whores_place_shawarma_s2"
    $ sceneIsStreet = True
    $ scene_caption = _("Shawarma")
    $ clear_scene_from_objects(scene_name)
    $ scene_image = "scene_street_whores_place_shawarma_Monica" + day_suffix
    $ add_object_to_scene("Monica", {"type":2, "base":"Street_whores_place_shawarma_Monica_" + cloth + day_suffix, "click" : "whores_place_shawarma_environment2", "actions" : "l", "zorder" : 10})
    $ add_object_to_scene("Shawarma_Trader", {"type":2, "base":"Street_whores_place_shawarma_Trader" + day_suffix, "click" : "whores_place_shawarma_environment2", "actions" : "lt", "zorder" : 5})

    $ add_object_to_scene("Shawarma_Stall", {"type":2, "base":"Street_whores_place_shawarma_Stall", "click" : "whores_place_shawarma_environment2", "actions" : "l", "zorder" : 0})
    $ add_object_to_scene("Street_Fencing1", {"type":2, "base":"Street_whores_place_shawarma_Street_Fencing1", "click" : "whores_place_street1_environment", "actions" : "l", "zorder" : 0, "b":0.15})
    $ add_object_to_scene("Street_Fencing2", {"type":2, "base":"Street_whores_place_shawarma_Street_Fencing2", "click" : "whores_place_street1_environment", "actions" : "l", "zorder" : 0, "b":0.15})
    $ add_object_to_scene("Trash_Can", {"type":2, "base":"Street_whores_place_shawarma_Trash_Can", "click" : "whores_place_street1_environment", "actions" : "l", "zorder" : 0})
    $ add_object_to_scene("Fire_Valve", {"type":2, "base":"Street_whores_place_shawarma_Fire_Valve", "click" : "whores_place_street1_environment", "actions" : "l", "zorder" : 0})
    $ add_object_to_scene("Trash1", {"type":2, "base":"Street_whores_place_shawarma_Trash1", "click" : "whores_place_environment", "actions" : "l", "zorder" : 0})
    $ add_object_to_scene("Trash2", {"type":2, "base":"Street_whores_place_shawarma_Trash2", "click" : "whores_place_environment", "actions" : "l", "zorder" : 0})
    $ add_object_to_scene("Trash3", {"type":2, "base":"Street_whores_place_shawarma_Trash3", "click" : "whores_place_environment", "actions" : "l", "zorder" : 0})
    $ add_object_to_scene("Trash4", {"type":2, "base":"Street_whores_place_shawarma_Trash4", "click" : "whores_place_environment", "actions" : "l", "zorder" : 0})
    $ add_object_to_scene("Trash5", {"type":2, "base":"Street_whores_place_shawarma_Trash5", "click" : "whores_place_environment", "actions" : "l", "zorder" : 0})
    $ add_object_to_scene("Trash6", {"type":2, "base":"Street_whores_place_shawarma_Trash6", "click" : "whores_place_environment", "actions" : "l", "zorder" : 0})
    $ add_object_to_scene("Trash7", {"type":2, "base":"Street_whores_place_shawarma_Trash7", "click" : "whores_place_environment", "actions" : "l", "zorder" : 0})
    $ add_object_to_scene("Trash8", {"type":2, "base":"Street_whores_place_shawarma_Trash8", "click" : "whores_place_environment", "actions" : "l", "zorder" : 0})

    $ add_object_to_scene("Teleport_Clothing_Shop", {"type":3, "text" : _("К МАГАЗИНУ ОДЕЖДЫ"), "larrow" : "arrow_down_2", "base":"Street_whores_place_shawarma_Teleport_Clothing_Shop", "click" : "whores_place_shawarma_teleport2", "xpos" : 304, "ypos" : 856, "zorder":15})
    $ add_object_to_scene("Teleport_Street_Hostel", {"type":3, "text" : _("ПОДВОРОТНЯ"), "larrow" : "arrow_left_2", "base":"Street_whores_place_shawarma_Teleport_Street_Hostel", "click" : "whores_place_shawarma_teleport2", "xpos" : 182, "ypos" : 376, "zorder":15})
    $ add_object_to_scene("Teleport_Whores_Place", {"type":3, "text" : _("К ПЕРЕКРЕСТКУ"), "rarrow" : "arrow_right_2", "base":"Street_whores_place_shawarma_Teleport_Whores_Place", "click" : "whores_place_shawarma_teleport2", "xpos" : 1375, "ypos" : 1022, "zorder":15})

    if whoresMonicaDisturb == True:
        $ autorun_to_object("whores_place_s2", "afterjail_whores_disturb_dialogue1")

    $ whoresPlacePreviousLocation = "shawarma"

    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label whores_place_shawarma_teleport2(obj_name, obj_data):
    if obj_name == "Teleport_Clothing_Shop":
        if shawarmaTraderStage == 1:
            call dress_return_shawarma_talk2()
            return
        call change_scene("street_cloth_shop", "Fade_long", "highheels_run2")
        return
    if obj_name == "Teleport_Street_Hostel":
        if streetHostelPathEnabled == False:
            mt "Я не пойду в эту вонючую подворотню!"
            "Что там забыла такая девушка как Я!??"
            return
        call change_scene("hostel_street", "Fade_long", "highheels_run2")
        return
    if obj_name == "Teleport_Whores_Place":
        call change_scene("whores_place", "Fade_long", "highheels_run2")
        return

    return
label whores_place_shawarma_environment2(obj_name, obj_data):
    if obj_name == "Monica":
        if gameStage == 3 and gameSubStage == 1:
            call hostelAfterJail_street_dialogue3()
            return
        return
    if obj_name == "Shawarma_Stall":
        mt "Какой-то грязный ларек, который продает помои!"
        "Кто может это есть?"
    if obj_name == "Shawarma_Trader":
        if obj_data["action"] == "l":
            mt "Грязный продавец. Я не выношу даже его вида! Фу!"
        if obj_data["action"] == "t":
            if gameStage == 3 and gameSubStage == 1:
                mt "Мне не о чем разговаривать с ним!"
                return
            if gameStage == 2 and gameSubStage == 1:
                mt "Мне не о чем разговаривать с ним!"
                return
            if gameStage == 2 and gameSubStage == 2:
                if hostelReceptionVisited == True:
                    call afterJail_Day2_Shawarma_dialogue2()
                    return
                call afterJail_Day2_Shawarma_dialogue1()
                return
            hide screen Rain
            music DarxieLand
            img 2653
            with fadelong
            shawarma "Мадаме!"
            img 2654
            "Вы передумали?"
            "Попробуете мою шаверму?"
            img 2655
            if shawarmaTraderOffended1 == True:
                m "Отстань, животное!"
            else:
                m "Оставьте меня в покое!"
            img 2656
            mt "Может стоило у него спросить про ночлег?"
            img 2657
            mt "..."
            if shawarmaTraderOffended1 == True:
                "Нет, не у этого животного точно!"
            else:
                "Нет, не у этого человека точно!"
            stop music fadeout 1.0
            call refresh_scene_fade()
        return
