label bedroom2:
    $ print "enter_bedroom2"
    $ miniMapData = []
    call miniMapHouseGenerate()
    $ miniMapSubst["all"] = "miniMapBedroomCheckCloth"

    $ scene_name = "bedroom2"
    $ scene_caption = _("Bedroom")
    $ scene_image = "scene_Bedroom2_Monica_" + cloth + day_suffix

    $ monica_tint = [1.0, 1.0, 1.0]
    if gameStage <= 2:
        if (cloth_type == "Lingerie" or cloth_type == "HomeCloth"):
            $ add_object_to_scene("Monica", {"type" : 2, "base" : "Bedroom2_Monica_" + cloth, "click" : "monica_show_cloth", "actions" : "l", "zorder":10, "tint": [0.9, 0.9, 1.0]})
        else:
            $ add_object_to_scene("Monica", {"type" : 2, "base" : "Bedroom2_Monica_" + cloth, "click" : "monica_show_cloth", "actions" : "l", "zorder":10})
    if gameStage > 2:
        $ add_object_to_scene("Monica", {"type" : 2, "base" : "Bedroom2_Monica_" + cloth, "click" : "bedroom2_environment", "actions" : "l", "zorder":10})

    $ add_object_to_scene("Mess", {"type":2, "base":"Bedroom2_Mess", "click" : "bedroom1_environment", "actions" : "l"})
    $ add_object_to_scene("Chair2", {"type":2, "base":"Bedroom2_Chair", "click" : "bedroom1_environment", "actions" : "l", "zorder" : 0})
    $ add_object_to_scene("Table", {"type":2, "base":"Bedroom2_Table", "click" : "bedroom1_environment", "actions" : "l", "zorder" : 0})
    $ add_object_to_scene("Table2", {"type":2, "base":"Bedroom2_Table2", "click" : "bedroom2_environment", "actions" : "l", "zorder" : 0})
    $ add_object_to_scene("Picture", {"type":2, "base":"Bedroom2_Picture", "click" : "bedroom2_environment", "actions" : "l", "zorder" : 0})
    $ add_object_to_scene("Windows", {"type":2, "base":"Bedroom2_Windows", "click" : "bedroom1_environment", "actions" : "l", "zorder" : 0, "c":1.0, "b":0.1})
    $ add_object_to_scene("Curtains", {"type":2, "base":"Bedroom2_Curtains", "click" : "bedroom1_environment", "actions" : "l", "zorder" : -1})
    $ add_object_to_scene("Carpet", {"type":2, "base":"Bedroom2_Carpet", "click" : "bedroom1_environment", "actions" : "l", "zorder" : 0})

    if gameStage <= 2:
        $ add_object_to_scene("Wardrobe", {"type":2, "base":"Bedroom2_Wardrobe", "click" : "wardrobe", "actions" : "lh", "zorder" : 0})
    if gameStage > 2:
        $ add_object_to_scene("Wardrobe", {"type":2, "base":"Bedroom2_Wardrobe", "click" : "bedroom2_environment", "actions" : "l", "zorder" : 0})

#    $ add_object_to_scene("Chair", {"type":2, "base":"Bedroom2_Chair", "click" : "bedroom2_environment", "actions" : "l", "zorder" : 0})
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3
    $ add_object_to_scene("Teleport_Bedroom1", {"type":3, "text" : _("КРОВАТЬ"), "larrow" : "arrow_left_2", "base":"Screen_Left_Arrow_Tight", "click" : "bedroom2_teleport", "xpos" : 220, "ypos" : 545, "zorder":11})
    $ add_object_to_scene("Teleport_Floor2", {"type":3, "text" : _("ХОЛЛ"), "rarrow" : "arrow_right_2", "base":"Bedroom2_Teleport_Floor2", "click" : "bedroom2_teleport", "xpos" : 1330, "ypos" : 1005, "zorder":11})


    if gameStage > 2:
        if scene_name != lastSceneName and lastSceneName != "bedroom1":
            $ autorun_to_object(scene_name, "afterJailHouse_dialogue16a")

#    $ add_object_to_scene("Teleport_Floor2", {"type":3, "text" : _("HALL"), "rarrow" : "arrow_right_2", "base":"Bedroom2_Teleport_Floor2", "click" : "bedroom2_teleport", "xpos" : 1310, "ypos" : 1005, "zorder":11, "b":0.4, "s":0.0, "c":1.0, "tint":[0.90625, 0.69140625, 0.19140625]})
#    $ renpy.pause(10.0, hard=True)

    return
#    jump show_scene

label bedroom2_teleport(obj_name, obj_data):
    if obj_name == "Teleport_Bedroom1":
        call change_scene("bedroom1") from _call_change_scene
    if obj_name == "Teleport_Floor2":
        if cloth_type == "Lingerie":
            call monica_show_lingerie_image from _call_monica_show_lingerie_image
            m "В доме прислуга. Я не хотела бы появляться на виду в нижнем белье."
            w
            return
        $ miniMapSubst["all"] = False
        call change_scene("floor2") from _call_change_scene_1

    return

label bedroom2_environment(name, obj_data):
    if obj_name == "Monica":
        if gameStage > 2:
            mt "Моя спальня..."
            "Я скучаю по ней!"
            "ОНА МОЯ!!!"
            "НЕНАВИЖУ!!!"
            "Как такое могло случиться???"

    if obj_name == "Table2":
        if gameStage > 2:
            mt "Мой любимый маленький столик..."
            return
        m "Этот маленький столик я использую для фотографий и разной другой ерунды."

        "Использовать косметику я предпочитаю в холле около спальни."

    if obj_name == "Picture":
        if gameStage > 2:
            mt "Масляная живопись."
            "Так и висит..."
            return

        "Я люблю картины.
        Я ценитель."

        "Хотя в последнее время я предпочитаю пастельные тона."

    if obj_name == "Wardrobe":
        mt "Мой любимый гардеробный шкаф..."
        "Сейчас там висят тряпки ненавистной Бетти!"
        "НЕНАВИЖУ!!!"
    return

label miniMapBedroomCheckCloth:
    if cloth_type == "Lingerie":
        call monica_show_lingerie_image
        m "В доме прислуга. Я не хотела бы появляться на виду в нижнем белье."
        w
        return False
    $ miniMapSubst["all"] = False
    return True
#вестибюль, холл, фойе
