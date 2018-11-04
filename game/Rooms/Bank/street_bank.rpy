label street_bank:

    $ print "enter_street_bank"
    $ miniMapData = []

    $ scene_name = "street_bank"
    $ sceneIsStreet = True
    $ scene_caption = _("BANK")
    $ clear_scene_from_objects(scene_name)
    if bFredFollowingMonica == True:
        $ scene_image = "scene_Bank_Street_Driver_Monica_" + cloth + day_suffix
        $ add_object_to_scene("Car", {"type":2, "base":"Bank_Street_Car", "click" : "street_house_main_yard_environment", "actions" : "l", "zorder" : 3})
        $ add_object_to_scene("Driver", {"type":2, "base":"Bank_Street_Driver", "click" : "street_bank_environment", "actions" : "lt", "zorder" : 5, "icon_t":"/Icons/talk" + res.suffix +".png", "b":0.2, "s":1.3, "tint":[1.0, 1.0, 0.8]})
        $ add_object_to_scene("Monica", {"type":2, "base":"Bank_Street_Driver_Monica_" + cloth + day_suffix, "click" : "street_bank_environment", "actions" : "l", "zorder" : 10})
    else:
        $ scene_image = "scene_Bank_Street_Monica_" + cloth + day_suffix
        $ add_object_to_scene("Monica", {"type":2, "base":"Bank_Street_Monica_" + cloth + day_suffix, "click" : "street_bank_environment", "actions" : "l", "zorder" : 10})

    $ add_object_to_scene("Traffic_Light", {"type":2, "base":"Bank_Street_Traffic_Light", "click" : "street_bank_environment", "actions" : "l", "zorder" : 0, "b":0.15})
    $ add_object_to_scene("Bank_Green", {"type":2, "base":"Bank_Street_Bank_Green", "click" : "street_bank_environment", "actions" : "l", "zorder" : 0, "b":0.2})
    $ add_object_to_scene("Building", {"type":2, "base":"Bank_Street_Building", "click" : "street_bank_environment", "actions" : "l", "zorder" : 0})
    $ add_object_to_scene("Teleport_Inside", {"type":2, "base":"Bank_Street_Teleport_Inside", "click" : "street_bank_teleport", "actions" : "lw", "zorder" : 1, "b":0.12})
    $ scene_sound = "streets_sound"
    return

#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label street_bank_teleport(obj_name, obj_data):
    if obj_name == "Teleport_Inside":
        if obj_data["action"] == "l":
            m "Это мой банк!"
        if obj_data["action"] == "w":
            if day_time == "evening":
                mt "Сейчас вечер. Банк уже закрыт."
                return
            call change_scene("bank_office", "Fade_long")
            return
    return
label street_bank_environment(obj_name, obj_data):
    if obj_name == "Traffic_Light":
        m "Светофор?
        Это такая штука, которая мешает мне ездить из-за пешеходов?
        Фи!"
    if obj_name == "Bank_Green":
        m "Bank Green..."
        "Нет, мне нужен другой банк."
    if obj_name == "Building":
        m "Это зеленое здание.
        В нем должен быть мой банк.
        Но я чувствую что мне придется сменить его!"
    if obj_name == "Driver":
        if obj_data["action"] == "l":
            call monica_looking_to_fred1()
            return
        if obj_data["action"] == "t":
            call get_to_drive_dialogue()
            return
    if obj_name == "Monica":
        m "На этой оживленной улице находится мой банк..."
        return

    return
