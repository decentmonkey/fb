default police_marcuscabinet_s2_chair_seen = False

label police_marcuscabinet_s2:
    $ print "enter_police_marcuscabinet_s2"
    $ miniMapData = []

    $ scene_name = "police_marcuscabinet_s2"
    $ scene_caption = _("Marcus Cabinet")
    $ clear_scene_from_objects(scene_name)

    if marcusCabinetState == 4:
        $ scene_image = "scene_Police_MarcusCabinet_Monica_Marcus_AfterJail_1"
        $ add_object_to_scene("Marcus", {"type":2, "base":"Police_MarcusCabinet_Monica_Marcus_AfterJail_1_Marcus", "click" : "police_marcuscabinet_s2_environment", "actions" : "lt", "zorder" : 9, "icon_t":"/Icons/talk" + res.suffix +".png"})
        $ add_object_to_scene("Monica", {"type":2, "base":"Police_MarcusCabinet_Monica_Marcus_AfterJail_1_Monica", "click" : "police_marcuscabinet_s2_environment", "actions" : "l", "zorder" : 10})
        $ add_object_to_scene("Chair", {"type":2, "base":"Police_MarcusCabinet_Chair", "click" : "police_marcuscabinet_s2_environment", "actions" : "lh", "zorder" : 0})

    if marcusCabinetState == 5 or marcusCabinetState == 6 or marcusCabinetState == 7:
        $ scene_image = "scene_Police_MarcusCabinet4_Monica_Marcus_AfterJail_1"
        $ add_object_to_scene("Marcus", {"type":2, "base":"Police_MarcusCabinet4_Monica_Marcus_AfterJail_1_Marcus", "click" : "police_marcuscabinet_s2_environment", "actions" : "lt", "zorder" : 9, "icon_t":"/Icons/talk" + res.suffix +".png"})
        $ add_object_to_scene("Monica", {"type":2, "base":"Police_MarcusCabinet4_Monica_Marcus_AfterJail_1_Monica", "click" : "police_marcuscabinet_s2_environment", "actions" : "l", "zorder" : 10})

    if marcusCabinetState == 8:
        $ scene_image = "scene_Police_MarcusCabinet3_Monica_Marcus_AfterJail_1"
        $ add_object_to_scene("Marcus", {"type":2, "base":"Police_MarcusCabinet3_Monica_Marcus_AfterJail_1_Marcus", "click" : "police_marcuscabinet_s2_environment", "actions" : "lt", "zorder" : 9, "icon_t":"/Icons/talk" + res.suffix +".png"})
        $ add_object_to_scene("Monica", {"type":2, "base":"Police_MarcusCabinet3_Monica_Marcus_AfterJail_1_Monica", "click" : "police_marcuscabinet_s2_environment", "actions" : "l", "zorder" : 10})


    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label police_marcuscabinet_s2_teleport(obj_name, obj_data):
    return
label police_marcuscabinet_s2_environment(obj_name, obj_data):
    if obj_name == "Monica":
        if marcusCabinetState < 7:
            mt "О БОЖЕ!!!"
            "ОНИ ХОТЯТ МЕНЯ ОТПРАВИТЬ НА ЭТУ ЖУТКУЮ ФЕРМУ!!!"
            "ПРЯМО СЕЙЧАС!!!"
        if marcusCabinetState == 7:
            mt "ДИК!! ДИК!!"
            mt "ТЫ СДЕЛАЛ ЭТО!"
            "ТЫ НЕ ОСТАВИЛ МЕНЯ!"
        if marcusCabinetState == 8:
            mt "КАКОЙ СТРАШНЫЙ ВЫБОР!!!"
            "О БОЖЕ!!!"
            "КАК ЖЕ МНЕ ДАЛЬШЕ БЫТЬ???"

    if obj_name == "Marcus":
        if act == "l":
            mt "Это страшный человек!"
            "У меня начинают дрожать коленки, когда я смотрю на него!!!"
            return
        if marcusCabinetState == 4:
            marcus "Здравствуйте, Миссис Бакфетт."
            "Присаживайтесь."
            return
        if marcusCabinetState == 6:
            call marcus_cabinet_dialogue11()
            return
        if marcusCabinetState == 7:
            call marcus_cabinet_dialogue12()
            return
        if marcusCabinetState == 8:
            call marcus_cabinet_dialogue13()
            return

    if obj_name == "Chair":
        if act == "l":
            $ police_marcuscabinet_s2_chair_seen = True
            mt "Снова стул... Что же со мной будет на этот раз?"
            "О БОЖЕ!!!"
            "МНЕ СТРАШНО!!!"
        if act == "h":
            if police_marcuscabinet_s2_chair_seen == False:
                mt "Снова стул... Что же со мной будет на этот раз?"
                "О БОЖЕ!!!"
                "МНЕ СТРАШНО!!!"
            $ marcusCabinetState = 5
            $ autorun_to_object("police_marcuscabinet_s2", "marcus_cabinet_dialogue10")
            call refresh_scene_fade()
            return

    return
