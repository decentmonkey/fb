label street_bank_s2:

    $ print "enter_street_bank"
    $ miniMapData = []

    $ scene_name = "street_bank_s2"
    $ sceneIsStreet = True
    $ scene_caption = _("BANK")
    $ clear_scene_from_objects(scene_name)
    $ scene_image = "scene_Bank_Street_Monica_" + cloth + day_suffix
    $ add_object_to_scene("Monica", {"type":2, "base":"Bank_Street_Monica_" + cloth + day_suffix, "click" : "street_bank_environment_s2", "actions" : "l", "zorder" : 10})

    $ add_object_to_scene("Traffic_Light", {"type":2, "base":"Bank_Street_Traffic_Light", "click" : "street_bank_environment_s2", "actions" : "l", "zorder" : 0, "b":0.15})
    $ add_object_to_scene("Bank_Green", {"type":2, "base":"Bank_Street_Bank_Green", "click" : "street_bank_environment_s2", "actions" : "l", "zorder" : 0, "b":0.2})
    $ add_object_to_scene("Building", {"type":2, "base":"Bank_Street_Building", "click" : "street_bank_environment_s2", "actions" : "l", "zorder" : 0})
    $ add_object_to_scene("Teleport_Inside", {"type":2, "base":"Bank_Street_Teleport_Inside", "click" : "street_bank_teleport_s2", "actions" : "lw", "zorder" : 1, "b":0.12})
    $ scene_sound = "streets_sound"
    return

#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label street_bank_teleport_s2(obj_name, obj_data):
    if obj_name == "Teleport_Inside":
        if obj_data["action"] == "l":
            m "Это мой банк!"
        if obj_data["action"] == "w":
            if day_time == "evening":
                mt "Сейчас вечер. Банк уже закрыт."
                return
            mt "Что мне там делать?"
            "У меня нет никаких документов!"
            "(хмык)"
#            call change_scene("bank_office", "Fade_long")
            return
    return
label street_bank_environment_s2(obj_name, obj_data):
    if obj_name == "Traffic_Light":
        m "Светофор?"
    if obj_name == "Bank_Green":
        m "Bank Green..."
    if obj_name == "Building":
        m "Это зеленое здание.
        В нем должен быть мой банк."
    if obj_name == "Monica":
        mt "На этой оживленной улице находится мой банк..."
        "Но мне он сейчас ни к чему..."
        "У меня нет никаких документов!"
        "(хмык)"
        return

    return
