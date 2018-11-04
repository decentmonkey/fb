default whoresTalkStage = 0
default whore1Enabled = True
default whoresMonicaDisturb = False

label whores_place:
    $ print "enter_whores_place"
    $ miniMapData = []

    $ scene_name = "whores_place"
    $ sceneIsStreet = True
    $ scene_caption = _("Whores place")
    $ clear_scene_from_objects(scene_name)
    if whore1Enabled == True:
        $ scene_image = "scene_street_Whores_Place_Whores_Monica_" + cloth + day_suffix
    else:
        $ scene_image = "scene_street_Whores_Place_Whores2_Monica_" + cloth + day_suffix
    $ add_object_to_scene("Monica", {"type":2, "base":"Street_Whores_Place_Whores_Monica_" + cloth + day_suffix, "click" : "whores_place_environment", "actions" : "l", "zorder" : 10})

    $ add_object_to_scene("Mommy", {"type":2, "base":"Street_Whores_Place_Mommy" + day_suffix, "click" : "whores_place_environment", "actions" : "lt", "zorder" : 5})
    $ add_object_to_scene("GrayMouse2", {"type":2, "base":"Street_Whores_Place_GrayMouse2" + day_suffix, "click" : "whores_place_environment", "actions" : "lt", "zorder" : 5})
    if whore1Enabled == True:
        $ add_object_to_scene("Whore1", {"type":2, "base":"Street_Whores_Place_Whore1" + day_suffix, "click" : "whores_place_environment", "actions" : "lt", "zorder" : 5})


    $ add_object_to_scene("Street_Fencing1", {"type":2, "base":"Street_Whores_Place_Fencing1", "click" : "whores_place_street1_environment", "actions" : "l", "zorder" : 0, "b":0.15})
    $ add_object_to_scene("Street_Fencing2", {"type":2, "base":"Street_Whores_Place_Fencing2", "click" : "whores_place_street1_environment", "actions" : "l", "zorder" : 0, "b":0.15})
    $ add_object_to_scene("Trash_Can", {"type":2, "base":"Street_Whores_Place_Trash_Can", "click" : "whores_place_street1_environment", "actions" : "l", "zorder" : 0})
    $ add_object_to_scene("Trash1", {"type":2, "base":"Street_Whores_Place_Trash1", "click" : "whores_place_environment", "actions" : "l", "zorder" : 0})
    $ add_object_to_scene("Trash2", {"type":2, "base":"Street_Whores_Place_Trash2", "click" : "whores_place_environment", "actions" : "l", "zorder" : 0})
    $ add_object_to_scene("Trash3", {"type":2, "base":"Street_Whores_Place_Trash3", "click" : "whores_place_environment", "actions" : "l", "zorder" : 0})
    $ add_object_to_scene("Trash4", {"type":2, "base":"Street_Whores_Place_Trash4", "click" : "whores_place_environment", "actions" : "l", "zorder" : 0})
    $ add_object_to_scene("Trash5", {"type":2, "base":"Street_Whores_Place_Trash5", "click" : "whores_place_environment", "actions" : "l", "zorder" : 0})
    $ add_object_to_scene("Trash6", {"type":2, "base":"Street_Whores_Place_Trash6", "click" : "whores_place_environment", "actions" : "l", "zorder" : 0})

    $ add_object_to_scene("Teleport_Shawarma", {"type":3, "text" : _("ВНИЗ ПО УЛИЦЕ"), "larrow" : "arrow_left_2", "base":"Street_Whores_Place_Teleport_Shawarma", "click" : "whores_place_teleport", "xpos" : 195, "ypos" : 778, "zorder":15})
    $ add_object_to_scene("Teleport_Street1", {"type":3, "text" : _("ВВЕРХ ПО УЛИЦЕ"), "rarrow" : "arrow_right_2", "base":"Street_Whores_Place_Teleport_Street1", "click" : "whores_place_teleport", "xpos" : 1642, "ypos" : 218, "zorder":15})
    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label whores_place_teleport(obj_name, obj_data):
    if obj_name == "Teleport_Street1":
        call change_scene("whores_place_street1", "Fade_long", "highheels_run2")
        return
    if obj_name == "Teleport_Shawarma":
        if whoresTalkStage == 0:
            call dress_return_whores_talk1()
            return
        call change_scene("whores_place_shawarma", "Fade_long", "highheels_run2")
        return
    return
label whores_place_environment(obj_name, obj_data):
    if obj_name == "Trash1" or obj_name == "Trash2" or obj_name == "Trash3" or obj_name == "Trash4" or obj_name == "Trash5" or obj_name == "Trash6" or obj_name == "Trash7" or obj_name == "Trash8":
        mt "О Боже!!!"
        "ГДЕ Я???"
        "Это же настоящая помойка!"
        "Не в переносном смысле, а в прямом!!!"
        "Моника, как ты оказалась здесь???"

    if obj_name == "Mommy":
        if obj_data["action"] == "l":
            mt "Судя по всему, это их мамочка."
            "Помогает им продавать свои тела...
            За бесценок..."
            "Фи!"
        if obj_data["action"] == "t":
            if whoresTalkStage == 1:
                music Master_Disorder
                if cloth == "BusinessCloth2":
                    img 1896
                mt "Эта мамочка как-то странно на меня смотрит."
                "Каким-то странным взглядом."
                "..."
                "Уверена что она мне просто завидует."
                "Старуха, Фи!"
                music casualMusic
                return
            mt "Я не собираюсь разговаривать с этой отвратительной мамочкой!!"
    if obj_name == "Whore1":
        if obj_data["action"] == "l":
            mt "Обычная уличная проститутка..."
            "Самая дешевая..."
            "Они обычно все так одеваются."
            "По крайней мере, как я видела в кино."
            "Я не могу смотреть на это без отвращения!"
        if obj_data["action"] == "t":
            mt "О чем говорить МНЕ!
            Монике Бакфетт!!"
            "Одной из самых богатых леди города!"
            "Владелицей самого популярного модного журнала!"
            "С какой-то уличной проституткой!!!"
    if obj_name == "GrayMouse2":
        if obj_data["action"] == "l":
            mt "Я знаю эту проститутку."
            "О Боже! Моника!"
            "ТЫ!!!"
            "ЗНАЕШЬ!!!"
            "ПРОСТИТУТКУ!!!"
            "Я не верю в это."
            "Но эта история забавна!
            Хи-хи!"
        if obj_data["action"] == "t":
            if whoresTalkStage == 0:
                call dress_return_whores_talk1()
                return
            if whoresTalkStage == 1:
                if grayMouse2WhoreOffended == True:
                    mt "Я не собираюсь общаться с со шлюхами. Я что, ненормальная?"
                else:
                    mt "Зря я подошла к ней. Она обычная шлюха."
                    mt "Я не собираюсь общаться с со шлюхами. Я что, ненормальная?"

                return


    return
