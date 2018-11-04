default police_entrance_s2_policeman1_talked = False
default police_entrance_s2_policeman2_talked = False

label police_entrance_s2:
    $ print "enter_police_entrance_s2"
    $ miniMapData = []

    $ scene_name = "police_entrance_s2"
    $ scene_caption = _("Police Station")
    $ clear_scene_from_objects(scene_name)

    if policeEntranceState == 4:
        $ scene_image = "scene_Police_Entrance_Monica_Reception_PoliceMen"
        $ add_object_to_scene("Reception", {"type":2, "base":"Police_Entrance_Monica_Reception_PoliceMen_Reception", "click" : "police_entrance_s2_environment", "actions" : "lt", "zorder" : 9})
        $ add_object_to_scene("Monica", {"type":2, "base":"Police_Entrance_Monica_Reception_PoliceMen_Monica", "click" : "police_entrance_s2_environment", "actions" : "l", "zorder" : 10})
        $ add_object_to_scene("PoliceMan1", {"type":2, "base":"Police_Entrance_Monica_Reception_PoliceMen_PoliceMan1", "click" : "police_entrance_s2_environment", "actions" : "lt", "zorder" : 9, "icon_t":"/Icons/talk" + res.suffix +".png"})
        $ add_object_to_scene("PoliceMan2", {"type":2, "base":"Police_Entrance_Monica_Reception_PoliceMen_PoliceMan2", "click" : "police_entrance_s2_environment", "actions" : "lt", "zorder" : 9, "icon_t":"/Icons/talk" + res.suffix +".png"})

    if policeEntranceState == 5:
        $ scene_image = "scene_Police_Entrance_Monica_Reception_" + cloth
        $ add_object_to_scene("Reception", {"type":2, "base":"Police_Entrance_Monica_Reception_AfterJail_Reception", "click" : "police_entrance_s2_environment", "actions" : "l", "zorder" : 9})
        $ add_object_to_scene("Monica", {"type":2, "base":"Police_Entrance_Monica_Reception_" + cloth, "click" : "police_entrance_s2_environment", "actions" : "l", "zorder" : 10})
        music Power_Bots_Loop


    $ add_object_to_scene("Table", {"type":2, "base":"police_entrance_Table", "click" : "police_entrance_s2_environment", "actions" : "l", "zorder" : 0})
    $ add_object_to_scene("Turniket", {"type":2, "base":"police_entrance_Turniket", "click" : "police_entrance_s2_environment", "actions" : "l", "zorder" : 0})
    $ add_object_to_scene("Teleport_Inside", {"type":3, "text" : _("ВХОД"), "rarrow" : "arrow_right_2", "base":"police_entrance_Teleport_Inside", "click" : "police_entrance_s2_teleport", "xpos" : 1009, "ypos" : 59, "zorder":5})
    $ add_object_to_scene("Telepost_Street_Police", {"type":3, "text" : _("НА УЛИЦУ"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "police_entrance_s2_teleport", "xpos" : 960, "ypos" : 956, "zorder":15})

    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label police_entrance_s2_teleport(obj_name, obj_data):
    if obj_name == "Teleport_Inside":
        mt "Я НИ ЗА ЧТО НЕ ПОЙДУ ТУДА!"
        "Мне надо быстрее убраться из этого страшного места!"
        return
    if obj_name == "Telepost_Street_Police":
        if policeEntranceState == 4:
            if police_entrance_s2_policeman1_talked == False:
                img 2646
                with fade
                policeman1 "До свидания, Мэм."
            if police_entrance_s2_policeman2_talked == False:
                img 2647
                with fade
                policeman2 "До скорой встречи, сучка."

            mt "Мне надо пройти этот турникет... Там дальше.. свобода!"
            img 2648
            with fadelong
            m "..."
            $ policeEntranceState = 5
            $ bFredFollowingMonica = False
            $ gameStage = 2
            $ afterJail = True
            $ rain = True
            $ rainIntencity = 3
            $ lightning = True
            $ map_enabled = True
            $ miniMapTurnedOff = True
            $ dickOfficeUnlocked = True
            $ richHotelReceptionistMode = 1
            $ cloth_type = "AfterJail"
            $ cloth = "AfterJail"
            stop music fadeout 1.0
            $ changeDayTime("evening")
            $ autorun_to_object("street_police_s2", "entrance_dialogue8")
            $ autorun_to_object("cloth_shop_view1_s2", "after_jail_cloth_shop_enter")
            call change_scene("street_police")
            return
        call change_scene("street_police")
        return

    return
label police_entrance_s2_environment(obj_name, obj_data):
    if obj_name == "Table":
        mt "Это место, где работает эта страшная женщина..."
    if obj_name == "Turniket":
        if policeEntranceState == 4:
            mt "Мне надо пройти этот турникет... Там дальше.. свобода!"
        if policeEntranceState == 5:
            mt "Я не буду приближаться к этому турникету! Мне страшно!"
    if obj_name == "Monica":
        if policeEntranceState == 4:
            mt "Эти полицейские... что они тут делают?"
            "ОНИ ЖДУТ МЕНЯ?!?!"
            "МНЕ СТРАШНО!!!"
        if policeEntranceState == 5:
            mt "Что я здесь делаю???"
            "Мне надо быстрее убраться из этого страшного места!"
    if obj_name == "Reception":
        if policeEntranceState == 4:
            img 2079
            with fade
        mt "Я не буду говорить с этой жуткой женщиной!"
        "Мне надо быстрее убраться из этого страшного места!"
    if obj_name == "PoliceMan1":
        $ police_entrance_s2_policeman1_talked = True
        img 2646
        with fade
        policeman1 "До свидания, Мэм."
    if obj_name == "PoliceMan2":
        $ police_entrance_s2_policeman2_talked = True
        img 2647
        with fade
        policeman2 "До скорой встречи, сучка."



    return
