default dickOfficeHallMonicaMode = 0
default dickOfficeHallVisited = False

label dick_office_hall1:
    $ print "dick_office_hall1"
    $ miniMapData = []

    $ scene_name = "dick_office_hall1"
    $ scene_caption = _("Dick's Office Hall")
    $ clear_scene_from_objects(scene_name)
    if dickOfficeHallMonicaMode == 0:
        $ scene_image = "scene_Office_Dick_Hall1_Monica_" + cloth
        $ add_object_to_scene("Monica", {"type":2, "base":"Office_Dick_Hall1_Monica_" + cloth, "click" : "dick_office_hall1_environment", "actions" : "l", "zorder" : 10})
    if dickOfficeHallMonicaMode == 1 and cloth == "Whore":
        $ scene_image = "scene_Office_Dick_Hall1_Monica_Whore_2"
        $ add_object_to_scene("Monica", {"type":2, "base":"Office_Dick_Hall1_Monica_Whore_2", "click" : "dick_office_hall1_environment", "actions" : "l", "zorder" : 10})

    $ add_object_to_scene("Door", {"type":2, "base":"Office_Dick_Hall1_Door", "click" : "dick_office_hall1_environment", "actions" : "l", "zorder" : 0})
    $ add_object_to_scene("Exhibit1", {"type":2, "base":"Office_Dick_Hall1_Exhibit1", "click" : "dick_office_hall1_environment", "actions" : "l", "zorder" : 0})
    $ add_object_to_scene("Exhibit2", {"type":2, "base":"Office_Dick_Hall1_Exhibit2", "click" : "dick_office_hall1_environment", "actions" : "l", "zorder" : 0})
    $ add_object_to_scene("Exhibit3", {"type":2, "base":"Office_Dick_Hall1_Exhibit3", "click" : "dick_office_hall1_environment", "actions" : "l", "zorder" : 0})
    $ add_object_to_scene("Exhibit4", {"type":2, "base":"Office_Dick_Hall1_Exhibit4", "click" : "dick_office_hall1_environment", "actions" : "l", "zorder" : 0})

    $ add_object_to_scene("Teleport_Entrance", {"type":3, "text" : _("ЛИФТ ВНИЗ"), "rarrow" : "arrow_down_2", "base":"Office_Dick_Hall1_Teleport_Entrance", "click" : "dick_office_hall1_teleport", "xpos" : 1534, "ypos" : 781, "zorder":9})
    $ add_object_to_scene("Teleport_Secretary", {"type":3, "text" : _("СЕКРЕТАРЬ ДИКА"), "larrow" : "arrow_left_2", "base":"Office_Dick_Hall1_Teleport_Secretary", "click" : "dick_office_hall1_teleport", "xpos" : 273, "ypos" : 850, "zorder":9})

    $ dickOfficeHallVisited = True
    return
    #                            $ brightness_adjustment = 0.1
    #                            $ saturation_adjustment = 1.07
    #                            $ contrast_adjustment = 1.3

label dick_office_hall1_teleport(obj_name, obj_data):
    if obj_name == "Teleport_Entrance":
        if dickOfficeHallMonicaMode == 1:
            call dickAfterJail_secretary_dialogue8()
            return
        call change_scene("dick_office_entrance", "Fade_long", "snd_lift")
        return
    if obj_name == "Teleport_Secretary":
        call change_scene("dick_office_secretary")
        return
    return
label dick_office_hall1_environment(obj_name, obj_data):
    if obj_name == "Monica":
        if dickOfficeSecretaryMonicaStage == 0:
            mt "Неплохо обосновался Дик."
            "Насколько помню, на этом этаже только его кабинет."
            "Где-то в конце коридора, если я не забыла."
            return
        if dickOfficeSecretaryMonicaStage > 0 and dickOfficeSecretaryMonicaStage < 7:
            mt "Где этот чертов Дик???"
            "Я разнесу его офис к чертовой матери!!!"
            return
        if dickOfficeSecretaryMonicaStage == 7:
            mt "Завтра???"
            "Дик будет только завтра?!?!"
            return
        if dickOfficeSecretaryMonicaStage == 8:
            mt "Дик сам виноват в том что я так одета!"
            return
        if dickOfficeSecretaryMonicaStage == 9:
            mt "Галстук..."
            mt "(хмык)"
            return


    if obj_name == "Door":
        sound snd_door_locked1
        mt "Хм.. закрыто..."
        "Что это за дверь?"
        "Куда она ведет?"
    if obj_name == "Exhibit1" or obj_name == "Exhibit2" or obj_name == "Exhibit3" or obj_name == "Exhibit4":
        mt "Что это такое?"
        "Какие-то экспонаты?"
        "Это нравится Дику???"
    return

label dick_office_hall1_dialogue1:
    mt "Неплохо обосновался Дик."
    "Насколько помню, на этом этаже только его кабинет."
    "Где-то в конце коридора, если я не забыла."
    return
