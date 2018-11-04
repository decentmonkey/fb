default marcusCabinetState = 0
default marcusCabinetState2 = 0

label police_marcuscabinet:
    $ print "enter_police_marcuscabinet"
    $ miniMapData = []

    $ scene_name = "police_marcuscabinet"
    $ scene_caption = _("Marcus Cabinet")
    $ clear_scene_from_objects(scene_name)

    if marcusCabinetState == 0:
        $ scene_image = "scene_Police_MarcusCabinet_Monica_Marcus_Detective_1"
        $ add_object_to_scene("Marcus", {"type":2, "base":"Police_MarcusCabinet_Monica_Marcus_Detective_1_Marcus", "click" : "police_marcuscabinet_environment", "actions" : "lt", "zorder" : 9, "icon_t":"/Icons/talk" + res.suffix +".png"})
        $ add_object_to_scene("Monica", {"type":2, "base":"Police_MarcusCabinet_Monica_Marcus_Detective_1_Monica", "click" : "police_marcuscabinet_environment", "actions" : "l", "zorder" : 10})
        $ add_object_to_scene("Detective", {"type":2, "base":"Police_MarcusCabinet_Monica_Marcus_Detective_1_Detective", "click" : "police_marcuscabinet_environment", "actions" : "lt", "zorder" : 9, "icon_t":"/Icons/talk" + res.suffix +".png" })

    if marcusCabinetState == 1:
        $ scene_image = "scene_Police_MarcusCabinet_Monica_Marcus_Detective_2"
        $ add_object_to_scene("Marcus", {"type":2, "base":"Police_MarcusCabinet_Monica_Marcus_Detective_2_Marcus", "click" : "police_marcuscabinet_environment", "actions" : "lt", "zorder" : 9, "icon_t":"/Icons/talk" + res.suffix +".png"})
        $ add_object_to_scene("Monica", {"type":2, "base":"Police_MarcusCabinet_Monica_Marcus_Detective_2_Monica", "click" : "police_marcuscabinet_environment", "actions" : "l", "zorder" : 10})
        $ add_object_to_scene("Detective", {"type":2, "base":"Police_MarcusCabinet_Monica_Marcus_Detective_2_Detective", "click" : "police_marcuscabinet_environment", "actions" : "lt", "zorder" : 9, "icon_t":"/Icons/talk" + res.suffix +".png" })

    if marcusCabinetState == 0 or marcusCabinetState == 1:
        $ add_object_to_scene("Chair", {"type":2, "base":"Police_MarcusCabinet_Chair", "click" : "police_marcuscabinet_environment", "actions" : "l", "zorder" : 0})
        $ add_object_to_scene("FileCabinet", {"type":2, "base":"Police_MarcusCabinet_FileCabinet", "click" : "police_marcuscabinet_environment", "actions" : "l", "zorder" : 0})
        $ add_object_to_scene("Folders1", {"type":2, "base":"Police_MarcusCabinet_Folders1", "click" : "police_marcuscabinet_environment", "actions" : "l", "zorder" : 0})
        $ add_object_to_scene("Folders2", {"type":2, "base":"Police_MarcusCabinet_Folders2", "click" : "police_marcuscabinet_environment", "actions" : "l", "zorder" : 0})
        $ add_object_to_scene("Folders3", {"type":2, "base":"Police_MarcusCabinet_Folders3", "click" : "police_marcuscabinet_environment", "actions" : "l", "zorder" : 0})
        $ add_object_to_scene("Safe", {"type":2, "base":"Police_MarcusCabinet_Safe", "click" : "police_marcuscabinet_environment", "actions" : "l", "zorder" : 0})
        $ add_object_to_scene("Table", {"type":2, "base":"Police_MarcusCabinet_Table", "click" : "police_marcuscabinet_environment", "actions" : "l", "zorder" : 0})
        $ add_object_to_scene("TableItems", {"type":2, "base":"Police_MarcusCabinet_TableItems", "click" : "police_marcuscabinet_environment", "actions" : "l", "zorder" : 0})
        $ add_object_to_scene("Water", {"type":2, "base":"Police_MarcusCabinet_Water", "click" : "police_marcuscabinet_environment", "actions" : "l", "zorder" : 0})

        $ add_object_to_scene("Teleport_Police_Entrance", {"type":3, "text" : _("ВЫХОД"), "larrow" : "arrow_down_2", "base":"Police_MarcusCabinet_Teleport_Entrance", "click" : "police_marcuscabinet_teleport", "xpos" : 100, "ypos" : 716, "zorder":5})


    if marcusCabinetState == 2:
        $ scene_image = "scene_Police_MarcusCabinet3_Monica_Marcus_1"
        $ add_object_to_scene("Marcus", {"type":2, "base":"Police_MarcusCabinet3_Monica_Marcus_1_Marcus", "click" : "police_marcuscabinet_environment", "actions" : "lt", "zorder" : 9, "icon_t":"/Icons/talk" + res.suffix +".png"})
        $ add_object_to_scene("Monica", {"type":2, "base":"Police_MarcusCabinet3_Monica_Marcus_1_Monica", "click" : "police_marcuscabinet_environment", "actions" : "l", "zorder" : 10})

        $ add_object_to_scene("Calendar", {"type":2, "base":"Police_MarcusCabinet3_Calendar", "click" : "police_marcuscabinet_environment", "actions" : "l", "zorder" : 0})
        $ add_object_to_scene("Door", {"type":2, "base":"Police_MarcusCabinet3_Door", "click" : "police_marcuscabinet_environment", "actions" : "l", "zorder" : 0})
        $ add_object_to_scene("Files1", {"type":2, "base":"Police_MarcusCabinet3_Files1", "click" : "police_marcuscabinet_environment", "actions" : "l", "zorder" : 0})
        $ add_object_to_scene("Files2", {"type":2, "base":"Police_MarcusCabinet3_Files2", "click" : "police_marcuscabinet_environment", "actions" : "l", "zorder" : 0})
        $ add_object_to_scene("Monitor", {"type":2, "base":"Police_MarcusCabinet3_Monitor", "click" : "police_marcuscabinet_environment", "actions" : "l", "zorder" : 0})
        $ add_object_to_scene("Notepad1", {"type":2, "base":"Police_MarcusCabinet3_Notepad1", "click" : "police_marcuscabinet_environment", "actions" : "l", "zorder" : 0})
        $ add_object_to_scene("Notepad2", {"type":2, "base":"Police_MarcusCabinet3_Notepad2", "click" : "police_marcuscabinet_environment", "actions" : "l", "zorder" : 0})
        $ add_object_to_scene("Phone", {"type":2, "base":"Police_MarcusCabinet3_Phone", "click" : "police_marcuscabinet_environment", "actions" : "l", "zorder" : 0})
        $ add_object_to_scene("Phone2", {"type":2, "base":"Police_MarcusCabinet3_Phone2", "click" : "police_marcuscabinet_environment", "actions" : "l", "zorder" : 0})
        $ add_object_to_scene("Printer", {"type":2, "base":"Police_MarcusCabinet3_Printer", "click" : "police_marcuscabinet_environment", "actions" : "l", "zorder" : 0})


    if marcusCabinetState == 3:
        $ scene_image = "scene_Police_MarcusCabinet4_Monica_Marcus_1"
        $ add_object_to_scene("Marcus", {"type":2, "base":"Police_MarcusCabinet4_Monica_Marcus_1_Marcus", "click" : "police_marcuscabinet_environment", "actions" : "lt", "zorder" : 9, "icon_t":"/Icons/talk" + res.suffix +".png"})
        $ add_object_to_scene("Monica", {"type":2, "base":"Police_MarcusCabinet4_Monica_Marcus_1_Monica", "click" : "police_marcuscabinet_environment", "actions" : "l", "zorder" : 10})

        $ add_object_to_scene("Calendar", {"type":2, "base":"Police_MarcusCabinet4_Calendar", "click" : "police_marcuscabinet_environment", "actions" : "l", "zorder" : 0})
        $ add_object_to_scene("FileCabinetA1", {"type":2, "base":"Police_MarcusCabinet4_FileCabinet", "click" : "police_marcuscabinet_environment", "actions" : "l", "zorder" : 0})
        $ add_object_to_scene("Files1", {"type":2, "base":"Police_MarcusCabinet4_Files1", "click" : "police_marcuscabinet_environment", "actions" : "l", "zorder" : 0})
        $ add_object_to_scene("Files2", {"type":2, "base":"Police_MarcusCabinet4_Files2", "click" : "police_marcuscabinet_environment", "actions" : "l", "zorder" : 0})
        $ add_object_to_scene("Monitor", {"type":2, "base":"Police_MarcusCabinet4_Monitor", "click" : "police_marcuscabinet_environment", "actions" : "l", "zorder" : 0})
        $ add_object_to_scene("Phone", {"type":2, "base":"Police_MarcusCabinet4_Phone", "click" : "police_marcuscabinet_environment", "actions" : "l", "zorder" : 0})
        $ add_object_to_scene("WaterA1", {"type":2, "base":"Police_MarcusCabinet4_Water", "click" : "police_marcuscabinet_environment", "actions" : "l", "zorder" : 0})

    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label police_marcuscabinet_teleport(obj_name, obj_data):
    if obj_name == "Teleport_Police_Entrance":
        if marcusCabinetState == 0:
            mt "Я еще не разобралась с этим Маркусом!"
            "Уйти я могу в любой момент!"
            return
        if marcusCabinetState == 1:
            call change_scene("police_marcuscabinet_door")
            return

    return
label police_marcuscabinet_environment(obj_name, obj_data):
    if obj_name == "Calendar":
        mt "Календарь..."
        "Не знаю что у этого мерзавца там отмечено..."

    if obj_name == "Door":
        if marcusCabinetState == 2:
            mt "За этой дверью какие-то мерзавцы!!!"
            "Они одели на меня наручники!!!"
    if obj_name == "Files1" or obj_name == "Files2":
        mt "Какие-то документы этого мерзавца."
        "Я не имею представления... Я..."
        "У меня кружится голова!"
    if obj_name == "Monitor":
        mt "Мне отсюда не видно что у него на экране."
    if obj_name == "Notepad1" or obj_name == "Notepad2":
        mt "Мне неинтересны записи этого подонка!"
        "Скоро они ему не понадобятся!!!"
    if obj_name == "Phone" or obj_name == "Phone2":
        mt "Мне надо как-то позвонить!"
        "Я не могу здесь находиться!!!"
    if obj_name == "Printer":
        mt "Какой-то... принтер?"
        "Зачем он мне???"
        "Мне надо отсюда выйти!!!"
    if obj_name == "FileCabinetA1":
        mt "Шкаф с документами..."
        "Зачем??? Что мне делать?"
        "Что происходит???"

    if obj_name == "WaterA1":
        mt "Вода... КАКАЯ К ЧЕРТУ ВОДА!!!"
        "Моника! На тебя надели наручники!!! Какие-то мерзавцы!!!"

    if obj_name == "Chair":
        mt "Если кто-то думает что я сяду на это ПОДОБИЕ стула, то он ошибается..."
    if obj_name == "FileCabinet":
        mt "Целый шкаф бесполезного хлама..."
    if obj_name == "Folders1" or obj_name == "Folders2" or obj_name == "Folders3":
        mt "Какие-то документы..."
        "Бесполезный хлам!"
    if obj_name == "Safe":
        mt "Что может быть ценного в этом сейфе? Фи!"
    if obj_name == "Table":
        mt "Дешевый... нет...."
        "ДЕШЕВЫЙ СТОЛ!!!"
        "И я приехала САМА к человеку, который работает за ЭТИМ столом???"
    if obj_name == "TableItems":
        mt "Весь стол завален каким-то хламом!"
        "Никакой организации труда!"
        "Никчемные люди! Бесполезные!"
    if obj_name == "Water":
        mt "Подобную водопроводную воду я уже где-то видела."
        "Никогда бы не стала пить ЭТО!"

    if obj_name == "Detective":
        if obj_data["action"] == "l":
            mt "Что это за жалкий человек?"
            "Сколько стоит этот плащь?"
            "Меньше $5000?"
            "Я принципиально не хочу общаться с людьми, которые одеваются так дешево!"
        if obj_data["action"] == "t":
            detective "Мэм, пожалуйста, обращайтесь к мистеру Маркусу..."
            return
    if obj_name == "Marcus":
        if obj_data["action"] == "l":
            if marcusCabinetState == 0:
                mt "Этот красавчик значит и есть мистер Маркус?"
                "Что он делает в этой дыре?"
                "Однако, я прождала его слишком долго, так что ему теперь не поздоровится в любом случае!"
                "Да и вживую голос у него не так уж и хорош!"
            if marcusCabinetState == 1:
                mt "Я не собираюсь больше общаться с этим уродом!"
                "Я ухожу!!!"
            if marcusCabinetState == 2:
                mt "Что этот подонок о себе возомнил???"
                "Он вообще представляет с кем имеет дело?!?!"
            if marcusCabinetState == 3:
                mt "Этот мерзавец... Что он говорит???"
                "Я не могу поверить! Это неправда!"
                "Я должна выйти отсюда, сейчас-же!"
        if obj_data["action"] == "t":
            if marcusCabinetState == 0:
                call marcus_cabinet_dialogue2()
                return
            if marcusCabinetState == 1:
                mt "Я не собираюсь больше общаться с этим уродом!"
                "Я ухожу!!!"
                return
            if marcusCabinetState == 2:
                call marcus_cabinet_dialogue4()
                return
            if marcusCabinetState == 3:
                if marcusCabinetState2 == 0:
                    call marcus_cabinet_dialogue5()
                    return
                if marcusCabinetState2 == 1:
                    call marcus_cabinet_dialogue6()
                    return
                if marcusCabinetState2 == 2:
                    call marcus_cabinet_dialogue7()
                    return
    if obj_name == "Monica":
        if marcusCabinetState == 0:
            mt "Этот красавчик значит и есть мистер Маркус?"
            "Что он делает в этой дыре?"
            "Однако, я прождала его слишком долго, так что ему теперь не поздоровится в любом случае!"
            "Да и вживую голос у него не так уж и хорош!"
        if marcusCabinetState == 1:
            mt "Я не собираюсь больше общаться с этим уродом!"
            "Я ухожу!!!"
        if marcusCabinetState == 2:
            mt "Что этот подонок о себе возомнил???"
            "Он вообще представляет с кем имеет дело?!?!"

        if marcusCabinetState == 3:
            mt "Что происходит? Моника?"
            "У меня в голове туман!"
            "Это все реально???"
            "Я не верю!"

    return
