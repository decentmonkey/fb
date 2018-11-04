
label street_police_s2:
    $ print "enter_street_police"
    $ miniMapData = []

    $ scene_name = "street_police_s2"
    $ sceneIsStreet = True
    $ scene_caption = _("Police Station")
    $ clear_scene_from_objects(scene_name)

    $ scene_image = "scene_street_Police_Monica_" + cloth + day_suffix
    $ add_object_to_scene("Monica", {"type":2, "base":"Street_Police_Monica_" + cloth + day_suffix, "click" : "street_police_environment2", "actions" : "l", "zorder" : 10})

    $ add_object_to_scene("Bench1", {"type":2, "base":"Street_Police_Bench1", "click" : "street_police_environment2", "actions" : "l", "zorder" : 0})
    $ add_object_to_scene("Bench2", {"type":2, "base":"Street_Police_Bench2", "click" : "street_police_environment2", "actions" : "l", "zorder" : 0})
    $ add_object_to_scene("Building", {"type":2, "base":"Street_Police_Building", "click" : "street_police_environment2", "actions" : "lw", "zorder" : 0})
    $ add_object_to_scene("Poster", {"type":2, "base":"Street_Police_Poster", "click" : "street_police_environment2", "actions" : "l", "zorder" : 1})
    $ add_object_to_scene("Car1", {"type":2, "base":"Street_Police_Car1", "click" : "street_police_environment2", "actions" : "l", "zorder" : 0})
    $ add_object_to_scene("Car2", {"type":2, "base":"Street_Police_Car2", "click" : "street_police_environment2", "actions" : "l", "zorder" : 0})
    $ add_object_to_scene("Car3", {"type":2, "base":"Street_Police_Car3", "click" : "street_police_environment2", "actions" : "l", "zorder" : 0})
    $ add_object_to_scene("Car4", {"type":2, "base":"Street_Police_Car4", "click" : "street_police_environment2", "actions" : "l", "zorder" : 0})
    $ add_object_to_scene("Car5", {"type":2, "base":"Street_Police_Car5", "click" : "street_police_environment2", "actions" : "l", "zorder" : 0})

    $ add_object_to_scene("Teleport_Map", {"type":3, "text" : _("БЕЖАТЬ ОТСЮДА!"), "rarrow" : "arrow_right_2", "base":"empty", "click" : "street_police_teleport2", "xpos" : 1713, "ypos" : 828, "zorder":15})

    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label street_police_teleport2(obj_name, obj_data):
    call map_show()
    return
label street_police_environment2(obj_name, obj_data):
    if obj_name == "Monica":
        mt "Это страшное здание..."
        "Страшное место..."
        "Мне лучше уйти отсюда, скорее!!!"
    if obj_name == "Building":
        if act == "l":
            mt "Это страшное здание..."
            "Страшное место..."
            "Мне лучше уйти отсюда, скорее!!!"
        if act == "w":
            call change_scene("police_entrance")

    if obj_name == "Bench1" or obj_name == "Bench2":
        mt "Я не буду сидеть на скамейке около этого страшного места!"
    if obj_name == "Car1" or obj_name == "Car2" or obj_name == "Car3" or obj_name == "Car4" or obj_name == "Car5":
        mt "Полицейская машина!"
        "Маркус сказал что любая проверка документов - и я попадаю назад к нему!"
        "Я боюсь этих машин!"
    if obj_name == "Poster":
        mt "TO PROTECT AND SERVE THE RICH"
        "JAIL THE HOMELESS"
        "О БОЖЕ!!!"

    return
