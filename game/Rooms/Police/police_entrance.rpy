default policeEntranceVisited = False
default policeEntranceReceptionTalked = False
default policeEntranceState = 0

label police_entrance:
    $ print "enter_police_entrance"
    $ miniMapData = []

    $ scene_name = "police_entrance"
    $ scene_caption = _("Police Station")
    $ clear_scene_from_objects(scene_name)

    if policeEntranceState == 0:
        $ scene_image = "scene_Police_Entrance_Monica_Reception_1"
        $ add_object_to_scene("Reception", {"type":2, "base":"Police_Entrance_Monica_Reception_1_Reception", "click" : "police_entrance_environment", "actions" : "lt", "zorder" : 9})
        $ add_object_to_scene("Monica", {"type":2, "base":"Police_Entrance_Monica_Reception_1_Monica", "click" : "police_entrance_environment", "actions" : "l", "zorder" : 10})
    if policeEntranceState == 1:
        $ scene_image = "scene_Police_Entrance_Monica_Reception_2"
        $ add_object_to_scene("Reception", {"type":2, "base":"Police_Entrance_Monica_Reception_2_Reception", "click" : "police_entrance_environment", "actions" : "lt", "zorder" : 9})
        $ add_object_to_scene("Monica", {"type":2, "base":"Police_Entrance_Monica_Reception_2_Monica", "click" : "police_entrance_environment", "actions" : "l", "zorder" : 10})
    if policeEntranceState == 2 or policeEntranceState == 3:
        $ scene_image = "scene_Police_Entrance_Monica_Reception_Detective"
        $ add_object_to_scene("Reception", {"type":2, "base":"Police_Entrance_Monica_Reception_Detective_Reception", "click" : "police_entrance_environment", "actions" : "lt", "zorder" : 9})
        $ add_object_to_scene("Monica", {"type":2, "base":"Police_Entrance_Monica_Reception_Detective_Monica", "click" : "police_entrance_environment", "actions" : "l", "zorder" : 10})
        $ add_object_to_scene("Detective", {"type":2, "base":"Police_Entrance_Monica_Reception_Detective_Detective", "click" : "police_entrance_environment", "actions" : "lt", "zorder" : 9, "icon_t":"/Icons/talk" + res.suffix +".png" })


    $ add_object_to_scene("Table", {"type":2, "base":"Police_Entrance_Table", "click" : "police_entrance_environment", "actions" : "l", "zorder" : 0})
    $ add_object_to_scene("Turniket", {"type":2, "base":"Police_Entrance_Turniket", "click" : "police_entrance_environment", "actions" : "l", "zorder" : 0})
    $ add_object_to_scene("Teleport_Inside", {"type":3, "text" : _("ВХОД"), "rarrow" : "arrow_right_2", "base":"Police_Entrance_Teleport_Inside", "click" : "police_entrance_teleport", "xpos" : 1009, "ypos" : 59, "zorder":5})
    $ add_object_to_scene("Telepost_Street_Police", {"type":3, "text" : _("НАЗАД НА УЛИЦУ"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "police_entrance_teleport", "xpos" : 960, "ypos" : 956, "zorder":15})
    #Police_Entrance_Teleport_Inside

    if policeEntranceVisited == False:
        $ map_enabled = False
        $ policeEntranceVisited = True
        $ autorun_to_object("police_entrance", "entrance_dialogue_enter")
    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label police_entrance_teleport(obj_name, obj_data):
    if obj_name == "Telepost_Street_Police":
        if policeEntranceState == 0 or policeEntranceState == 1 or policeEntranceState == 2 or policeEntranceState == 3:
            mt "Мне рано уходить. Я еще не встретилась с этим... как его... Маркусом."
            "Где он??? Черт бы его побрал!!!"
            return
    if obj_name == "Teleport_Inside":
        if policeEntranceState == 0:
            $ policeEntranceState = 1
            music Stealth_Groover
            call entrance_dialogue1()
            call refresh_scene_fade()
            return
        if policeEntranceState == 1:
            call entrance_dialogue1()
            return
        if policeEntranceState == 2:
            call entrance_dialogue1()
            return
        if policeEntranceState == 3:
            music Stealth_Groover
            $ autorun_to_object("police_marcuscabinet", "marcus_cabinet_dialogue1")
            call change_scene("police_marcuscabinet")
            return
    return
label police_entrance_environment(obj_name, obj_data):
    if obj_name == "Table":
        mt "Фи! Какое жуткое рабочее место!"
        "Но... у каждого свое.. место..."
        "Хи-хи..."
    if obj_name == "Turniket":
        if policeEntranceState == 0:
            mt "Что это за палки? Это какой-то турникет?"
            "Зачем он?"
        if policeEntranceState == 1:
            mt "Они что, собираются остановить меня этим турникетом?!!"
            "Меня, Монику Бакфетт!!!"
            "Они сильно ошибаются..."
            "Хи-хи..."
        if policeEntranceState == 2 or policeEntranceState == 3:
            mt "Я принципиально попаду туда!"
            "А потом уволю всех этих недотяп!!!"

    if obj_name == "Monica":
        if policeEntranceState == 0 or policeEntranceState == 1:
            mt "Какое неприятное место!"
            "Моника! 5 минут! Не более!!!"
        if policeEntranceState == 2 or policeEntranceState == 3:
            mt "Я принципиально попаду туда!"
            "А потом уволю всех этих недотяп!!!"
    if obj_name == "Reception":
        if obj_data["action"] == "l":
            if policeEntranceState == 0:
                mt "Что это там сидит? Это вообще мужчина или женщина?"
            if policeEntranceState == 1:
                mt "Это... существо... Оно что, пытается остановить МЕНЯ???"
            if policeEntranceState == 2 or policeEntranceState == 3:
                mt "Я уволю эту сучку..."
                if bitchmeterValue < maxBitchness / 2:
                    mt "Даже несмотря на то что я стараюсь быть терпимой к людям..."
        if obj_data["action"] == "t":
            if policeEntranceState == 0:
                $ policeEntranceState = 1
                if policeEntranceReceptionTalked == False:
                    $ policeEntranceReceptionTalked = True
                    music Stealth_Groover
                    call entrance_dialogue1()
                    call refresh_scene_fade()
                    return
                return
            if policeEntranceState == 1:
                call entrance_dialogue2()
                return
            if policeEntranceState == 2 or policeEntranceState == 3:
                policewoman "Пожалуйста, обращайтесь к Детективу!"
    if obj_name == "Detective":
        if obj_data["action"] == "l":
            mt "Что это за жалкий человек?"
            "Сколько стоит этот плащь?"
            "Меньше $5000?"
            "Я принципиально не хочу общаться с людьми, которые одеваются так дешево!"
        if obj_data["action"] == "t":
            if policeEntranceState == 2:
                call entrance_dialogue5()
                return
            if policeEntranceState == 3:
                call entrance_dialogue6()
                return
    return
