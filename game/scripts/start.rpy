default dickSearch = False
default hotelVisited = False
default homeVisited = False
default gameStage = 0
default gameSubStage = 0
default afterJail = False
default rain = False
default rainIntencity = 0
default lightning = False
default sceneIsStreet = False

label start:
#    jump credits
    $ game_version1_screen_ready_to_render = True
    $ cloth_type = "Lingerie"
    $ cloth = "Lingerie1"
    $ zoom_factor = 1

    define day_time = "day"
    $ day_suffix = ""
    $ day = 1
    $ money = 100000000.0
    $ scenes_data = {"objects": {}, "substs" : {}, "autorun": {}}
    $ inventory_objects = {}
    $ inventory = []

    $ hud_preset_current = "default"
    $ bitchmeterValue = 280

    call game_init from _call_game_init
    python:
        for i in renpy.exports.get_image_load_log():
            print i

    $ map_objects = {
            "Teleport_Monica_Office" : {"text" : _("ОФИС МОНИКИ"), "xpos" : 882, "ypos" : 320, "base" : "map_marker", "state" : "visible"},
            "Teleport_Street_Corner" : {"text" : _("УГОЛ УЛИЦЫ"), "xpos" : 124, "ypos" : 476, "base" : "map_marker", "state" : "invisible"},
            "Teleport_Dick_Office" : {"text" : _("ОФИС ДИКА"), "xpos" : 1370, "ypos" : 127, "base" : "map_marker", "state" : "invisible"},
            "Teleport_Gas_Station" : {"text" : _("ЗАПРАВКА"), "xpos" : 1125, "ypos" : 910, "base" : "map_marker", "state" : "invisible"},
            "Teleport_Police" : {"text" : _("ПОЛИЦИЯ"), "xpos" : 912, "ypos" : 809, "base" : "map_marker", "state" : "invisible"},
            "Teleport_Rich_Hotel" : {"text" : _("ОТЕЛЬ ЛЯ ГРАНД"), "xpos" : 1782, "ypos" : 593, "base" : "map_marker", "state" : "invisible"},
            "Teleport_Fitness" : {"text" : _("ФИТНЕСС"), "xpos" : 356, "ypos" : 411, "base" : "map_marker", "state" : "invisible"},
            "Teleport_Steve_Office" : {"text" : _("ОФИС СТИВА"), "xpos" : 1333, "ypos" : 724, "base" : "map_marker", "state" : "invisible"},
            "Teleport_Bank" : {"text" : _("БАНК"), "xpos" : 1212, "ypos" : 439, "base" : "map_marker", "state" : "invisible"},
            "Teleport_Cloth_Shop" : {"text" : _("МАГАЗИН ОДЕЖДЫ"), "xpos" : 340, "ypos" : 901, "base" : "map_marker", "state" : "invisible"},
            "Teleport_Street_Corner" : {"text" : _("УГОЛ УЛИЦЫ"), "xpos" : 88, "ypos" : 942, "base" : "map_marker", "state" : "invisible"},
            "Teleport_House" : {"text" : _("ДОМ МОНИКИ"), "xpos" : 95, "ypos" : 798, "base" : "map_marker_house", "state" : "active"}
    }
#mousedown_3, hide_windows
#    $ print(config.keymap["game_menu"])
#    $ config.keymap["hide_windows"] = []
#    $ print(config.keymap)
#    pause

    $ scene_refresh_flag = True
    $ map_enabled = False
    call intro_scene() from _call_intro_scene

    $ add_objective("monica_wakeup", _("Разбудить Монику"), c_green, 0)

    $ scene_transition = "Fade_long"
    $ autorun_to_object("intro_scene", "intro_scene_start")
    jump show_scene

label start_new_game:
    music casualMusic
    $ map_enabled = True
    $ add_objective("dress_homecloth", _("Одеть домашнюю одежду"), c_blue, 0)
    $ add_objective("take_bath", _("Принять душ"), c_green, 1)
    $ add_objective("eat", _("Позавтракать"), c_green, 2)
    $ add_objective("go_outside", _("Одеться и идти на улицу"), c_orange, 10)

    $ miniMapDisabled = ["Basement"]

#    m "test!"
#    call bedroom1 from _call_bedroom1
#    jump show_scene
#    imgc monica_homecloth1_disgust1

#    show monica_homecloth1_отвращение1 at dialogue_image_left

#    show screen dialogue_image_center("monica_homecloth1_отвращение1", config.screen_width / 2, config.screen_height)
#    show img_1011 at dialogue_image_left
#    $ dialogue_active_flag = False
    img 1010
    with fadelong
#    music All_Stars_Loop
    m "Доброе утро! Меня зовут Моника Бакфетт! Я замужем."

    "Мы с мужем поженились 12 лет назад."

    img 1011
#    music BossaBossa
    "Мой муж очень богат.
    После свадьбы мы поселились в этом большом доме."

    "Люблю-ли я мужа?
    Можно сказать что люблю.
    Он такой мягкий и пушистый."

    img 1010
#    music All_Stars_Loop
    "Я с удовольствием им управляю."

    img 1011
    sound snd_far_hit
    mt "На улице что-то хлопнуло"

    img img_1010
    pause 0.5
    img img_1013
    with Dissolve(0.5)
#    music BossaBossa
    m "Любовь?
    Моя главная любовь - это власть и управление людьми."

    "А еще я считаю что я очень красива.
    Я люблю свою красоту, вот моя любовь :)"

    "У меня свой бизнес.
    Я владею очень популярным журналом моды.
    Многие девушки завидуют мне."

    "Мне вообще все завидуют."

    "Но я считаю что это их проблемы.
    Неудачники всегда завидуют таким успешным людям."

    "Таким как я :)"

    "Впрочем что-то я задумалась.
    Пора вставать, собираться и ехать заниматься своим любимым делом :)"

    img 1018
    "Итак, что мне надо сделать."

    "Надо одеться в домашнюю одежду.
    Надо принять душ. Надо позавтракать.
    Надо одеться на выход и идти на улицу."

    "Фред (это мой водитель) должен ждать меня на улице."

    img 1019
    "И только пусть попробует его там не оказаться когда я выйду! (злобно ухмыляется)."

    "Он старается, но у него и так уже много промахов.
    Я подумываю о том чтобы его заменить."

    img 1020
    "Людей вообще надо почаще менять.
    Независимо от того стараются они или нет."

    "Люди..."

    img 1021
    "Люди просто надоедают вот и все."

    w
    $ scene_refresh_flag = True
    $ scene_transition = "Fade"
    call change_scene("bedroom1", "Fade_long") from _call_change_scene_84

    $ add_inventory("phone", 1, True)
    return
























#
