label monica_office_secretary_teatable:
    $ print "enter_monica_office_secretary_teatable"
    $ miniMapData = []

    $ scene_name = "monica_office_secretary_teatable"
    $ scene_caption = _("Monica's Secretary")
    $ clear_scene_from_objects(scene_name)

    $ scene_image = "scene_Office_Monica_Secretary_Teatable_Monica_" + cloth + day_suffix
    $ add_object_to_scene("Monica", {"type" : 2, "base" : "Office_Monica_Secretary_Teatable_Monica_" + cloth, "click" : "monica_office_secretary_teatable_environment", "actions" : "l", "zorder":10})

    $ add_object_to_scene("Bakery", {"type" : 2, "base" : "Office_Monica_Secretary_Teatable_Bakery", "click" : "monica_office_secretary_teatable_environment", "actions" : "l", "zorder":0})
    $ add_object_to_scene("Books1", {"type" : 2, "base" : "Office_Monica_Secretary_Teatable_Books", "click" : "monica_office_secretary_environment", "actions" : "l", "zorder":0})
    $ add_object_to_scene("Coffee", {"type" : 2, "base" : "Office_Monica_Secretary_Teatable_Coffee", "click" : "monica_office_secretary_teatable_environment", "actions" : "l", "zorder":0})
    $ add_object_to_scene("Documents", {"type" : 2, "base" : "Office_Monica_Secretary_Teatable_Documents", "click" : "monica_office_secretary_teatable_environment", "actions" : "l", "zorder":0})
    $ add_object_to_scene("Elephant", {"type" : 2, "base" : "Office_Monica_Secretary_Teatable_Elephant", "click" : "monica_office_secretary_teatable_environment", "actions" : "l", "zorder":0})
    $ add_object_to_scene("Flower", {"type" : 2, "base" : "Office_Monica_Secretary_Teatable_Flower", "click" : "monica_office_secretary_teatable_environment", "actions" : "l", "zorder":0})
    $ add_object_to_scene("Gong", {"type" : 2, "base" : "Office_Monica_Secretary_Teatable_Gong", "click" : "monica_office_secretary_teatable_environment", "actions" : "l", "zorder":0})
    $ add_object_to_scene("Sofa", {"type" : 2, "base" : "Office_Monica_Secretary_Teatable_Sofa", "click" : "monica_office_secretary_teatable_environment", "actions" : "l", "zorder":-1})
    $ add_object_to_scene("TableBooks", {"type" : 2, "base" : "Office_Monica_Secretary_Teatable_TableBooks", "click" : "monica_office_secretary_teatable_environment", "actions" : "l", "zorder":0})

    $ add_object_to_scene("Teleport_Monica_Office_Secretary", {"type":3, "text" : _("НАЗАД"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "monica_office_secretary_teatable_teleport", "xpos" : 960, "ypos" : 956, "zorder":11})
    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label monica_office_secretary_teatable_teleport(obj_name, obj_data):
    if obj_name == "Teleport_Monica_Office_Secretary":
        call change_scene("monica_office_secretary") from _call_change_scene_81
        return
    return
label monica_office_secretary_teatable_environment(obj_name, obj_data):
    if obj_name == "Monica":
        m "Это чайный столик."
        "Моя секретарь обычно угощает чаем, либо кофе тех, кто ожидает моего приема."
    if obj_name == "Documents":
        m "Какие-то документы?"

    if obj_name == "Bakery":
        m "Моя секретарь обычно угощает чаем, либо кофе тех, кто ожидает моего приема."
        "Разумеется, я распорядилась, чтобы выпечка была невкусная."
        "Эти люди собираются отнять мое время, в конце концов!"
        "И я не собираюсь облегчать им жизнь!"
    if obj_name == "Coffee":
        m "Кофе...
        Похоже, остывший."
        "Остывший кофе для гостей - это хорошо..."
    if obj_name == "Flower":
        m "Надо же, я разглядела цветок!"
        "Какой-то один жидкий, облезлый цветок и все!"
        "Моя секретарь совсем свихнулась со своими книгами."
        "Надо будет дать ей пару полезных советов, когда у меня будет свободное время."
        "И пусть попробует не прислушаться к ним!"
    if obj_name == "Gong":
        m "Что это?"
        "Маленький Гонг?"
        "Ни разу не слышала что в него кто-то бил."
        "Может быть кто-то из ожидающих рискнет это сделать?
        Ну-ну!!"
    if obj_name == "Sofa":
        m "Дива для ожидающих приема гостей."
        "Я на нем никогда не сидела, но надеюсь он жесткий!"
    if obj_name == "TableBooks":
        m "Развлекательные книги для ожидающих гостей."
        "У них ведь много свободного времени!"
        "Это у меня его нет!"
    if obj_name == "Elephant":
        m "Ух-ты!
        Маленький слоник!"
        "Как это мило!..."
        call bitch(-3, "secretary_elephant") from _call_bitch_73
    return


#
