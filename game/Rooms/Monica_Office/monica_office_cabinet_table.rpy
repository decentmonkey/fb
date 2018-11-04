default monicaOfficeCabinetMonkeys = False
default monicaOfficeCabinetMonkeysSuffix = "1"

default monicaOfficeWorkMonkeysPlanned = False

label monica_office_cabinet_table:
    $ print "enter_monica_office_cabinet_table"
    $ miniMapData = []

    $ scene_name = "monica_office_cabinet_table"
    $ scene_caption = _("Monica's Office")
    $ clear_scene_from_objects(scene_name)

    if monicaOfficeCabinetMonkeys == False:
        $ scene_image = "scene_Office_Monica_Cabinet_Table_Monica_" + cloth + day_suffix
    else:
        $ scene_image = "scene_Office_Monica_Cabinet_Table_Monica_Monkeys" + monicaOfficeCabinetMonkeysSuffix + "_" + cloth + day_suffix
        $ add_object_to_scene("Monkeys", {"type" : 2, "base" : "Office_Monica_Cabinet_Table_Monica_Monkeys" + monicaOfficeCabinetMonkeysSuffix + "_" + cloth, "click" : "monica_office_monkeys_interact", "actions" : "lt", "zorder":10})

    $ add_object_to_scene("Monica", {"type" : 2, "base" : "Office_Monica_Cabinet_Table_Monica_" + cloth, "click" : "monica_office_cabinet_table_environment", "actions" : "l", "zorder":10})

    if check_inventory("phone"):
        if monicaOfficeSteveCall1Planned == True:
            $ add_object_to_scene("Phone", {"type":3, "text" : _("ТЕЛЕФОН"), "larrow" : "arrow_left_2", "img_overlay":"Office_Monica_Cabinet_Table_Phone", "base":"Office_Monica_Cabinet_Table_Phone", "click" : "monkeys_monica_office1", "xpos" : 1416, "ypos" : 633, "zorder":11, "hover_overlay":True})
        else:
            $ add_object_to_scene("Phone", {"type" : 2, "base" : "Office_Monica_Cabinet_Table_Phone", "click" : "monica_office_cabinet_table_environment", "actions" : "lt", "zorder":10})
    else:
        $ add_object_to_scene("NoPhone", {"type" : 2, "base" : "empty", "click" : "monica_office_cabinet_table_environment", "img_overlay":"Office_Monica_Cabinet_Table_NoPhone" + day_suffix, "actions" : "l", "zorder":0})

    $ add_object_to_scene("Flowers", {"type" : 2, "base" : "Office_Monica_Cabinet_Table_Flowers", "click" : "monica_office_cabinet_environment", "actions" : "l", "zorder":2})
    $ add_object_to_scene("Paints", {"type" : 2, "base" : "Office_Monica_Cabinet_Table_Paints", "click" : "monica_office_cabinet_environment", "actions" : "l", "zorder":2})
    $ add_object_to_scene("Journal", {"type" : 2, "base" : "Office_Monica_Cabinet_Table_Journal" + day_suffix, "click" : "monica_office_cabinet_table_environment", "actions" : "l", "zorder":11})
    $ add_object_to_scene("Water", {"type" : 2, "base" : "Office_Monica_Cabinet_Table_Water" + day_suffix, "click" : "monica_office_cabinet_table_environment", "actions" : "l", "zorder":2})

    if check_inventory("phone"):
        $ add_object_to_scene("Table", {"type" : 2, "base" : "Office_Monica_Cabinet_Table_Table" + day_suffix, "click" : "monica_office_cabinet_table_environment", "actions" : "lh", "zorder":1})

    $ add_object_to_scene("Teleport_Monica_Office_Secretary", {"type":3, "text" : _("К СЕКРЕТАРЮ"), "larrow" : "arrow_left_2", "base":"Office_Monica_Cabinet_Table_Exit", "click" : "monica_office_cabinet_table_teleport", "xpos" : 723, "ypos" : 166, "zorder":11, "b":0.15, "tint":[1.0, 1.0, 0.85]})

    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label monica_office_cabinet_table_teleport(obj_name, obj_data):
    if obj_name == "Teleport_Monica_Office_Secretary":
        call change_scene("monica_office_secretary") from _call_change_scene_54
        return
    return
label monica_office_cabinet_table_environment(obj_name, obj_data):
    if obj_name == "Monica":
        if day_time == "evening":
            m "Уже вечер!
            Не собираюсь же я работать в самом деле?"
            return
        m "Может быть немного поработать?
        Как только станет скучно, я сразу прекращу работу!"
    if obj_name == "Journal":
        m "Я всегда держу на столе свежий номер своего журнала."
        "Другие журналы?
        Я их не читаю!"
        "Что в них может быть интересного?"
        "То-ли дело мой журнал!!!"

    if obj_name == "Water":
        m "Вода.
        Даже такая королева как я должна пить.
        И есть."
        "У меня никогда не было с этим проблем.
        И не будет никогда!"

    if obj_name == "Phone":
        if obj_data["action"] == "l":
            m "Мой любимый телефончик!"

            "Я люблю делать селфи!"

            "Отправлять их в instagram!"

            "У меня сотни тысяч подписчиков!"

            "Меня все любят и все восхищаются мной!"

            "Хи-хи!"
        if obj_data["action"] == "t":
            m "Я никому не хочу звонить!
            Мне все уже надоели!"

    if obj_name == "Table":
        if obj_data["action"] == "l":
            m "Если у меня вдруг появится желание, я могу поработать..."
            if going_to_fitness_quest == True:
                m "Но сначала я собираюсь поехать в фитнесс!"
            if day_time == "evening":
                m "Но вечером оно у меня вряд-ли появится..."
        if obj_data["action"] == "h":
            if going_to_fitness_quest == True:
                m "Я хочу поехать в фитнес зал!"
                "Я и так вчера туда не попала!"
                "Не буду работать!"
                return
            if day == 1 and monicaOfficeSteveCall1Planned == True:
                m "Мне надо позвонить Стиву."
                return
            if day_time == "evening":
                m "Я не знаю чем мне заняться по работе."
                "Потому что уже вечер и я не собираюсь работать!"
                return
            m "Я не знаю чем мне заняться по работе.
            Может быть узнать у секретаря что на повестке дня?"

    return


#
