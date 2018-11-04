default steveOfficeSteveState = 0
default steveOfficeSteveInOffice = True

label steve_office_office:

    $ print "enter_steve_office_office"
    $ miniMapData = []

    $ scene_name = "steve_office_office"
    $ scene_caption = _("STEVE'S CABINET")
    $ clear_scene_from_objects(scene_name)
    $ scene_image = "scene_steve_office_office_Monica_" + cloth
    if steveOfficeSteveInOffice == True:
        if steveOfficeSteveState == 0:
            $ scene_image = "scene_steve_office_office_Monica_Steve"
            $ add_object_to_scene("Steve", {"type":2, "base":"Steve_Office_Office_Steve", "click" : "steve_office_office_environment", "actions" : "lt", "zorder" : 10, "icon_t":"/Icons/talk" + res.suffix +".png"})
        if steveOfficeSteveState == 1:
            $ scene_image = "scene_steve_office_office_Monica_Steve2"
            $ add_object_to_scene("Steve", {"type":2, "base":"Steve_Office_Office_Steve2", "click" : "steve_office_office_environment", "actions" : "lt", "zorder" : 10, "icon_t":"/Icons/talk" + res.suffix +".png"})
        if steveOfficeSteveState == 2:
            $ scene_image = "scene_steve_office_office_Monica_Steve3"
            $ add_object_to_scene("Steve", {"type":2, "base":"Steve_Office_Office_Steve3", "click" : "steve_office_office_environment", "actions" : "lt", "zorder" : 10, "icon_t":"/Icons/talk" + res.suffix +".png"})
        $ add_object_to_scene("Monica", {"type":2, "base":"Steve_Office_Office_Monica_" + cloth, "click" : "steve_office_office_environment", "actions" : "l", "zorder" : 1})

    else:
        $ scene_image = "scene_steve_office_office_Monica"
        $ add_object_to_scene("Monica", {"type":2, "base":"Steve_Office_Office_Monica_" + cloth, "click" : "steve_office_office_environment", "actions" : "l", "zorder" : 1})

    $ add_object_to_scene("Bar", {"type":2, "base":"steve_office_office_Bar", "click" : "steve_office_office_environment", "actions" : "l", "zorder" : 0})
    $ add_object_to_scene("Chair1", {"type":2, "base":"steve_office_office_Chair1", "click" : "steve_office_office_environment", "actions" : "l", "zorder" : 0})
    $ add_object_to_scene("Chair2", {"type":2, "base":"steve_office_office_Chair2", "click" : "steve_office_office_environment", "actions" : "l", "zorder" : 0})
    $ add_object_to_scene("Chair3", {"type":2, "base":"steve_office_office_Chair3", "click" : "steve_office_office_environment", "actions" : "l", "zorder" : 0})
    $ add_object_to_scene("Chair4", {"type":2, "base":"steve_office_office_Chair4", "click" : "steve_office_office_environment", "actions" : "l", "zorder" : 0})
    $ add_object_to_scene("Chair5", {"type":2, "base":"steve_office_office_Chair5", "click" : "steve_office_office_environment", "actions" : "l", "zorder" : 0})
    $ add_object_to_scene("Sofa", {"type":2, "base":"steve_office_office_Sofa", "click" : "steve_office_office_environment", "actions" : "l", "zorder" : 0})
    $ add_object_to_scene("Table", {"type":2, "base":"steve_office_office_Table_Object", "click" : "steve_office_office_environment", "actions" : "lw", "zorder" : 0})

    $ add_object_to_scene("Teleport_Steve_Office_Secretary", {"type":3, "text" : _("НАЗАД К СЕКРЕТАРШЕ"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "steve_office_office_teleport", "xpos" : 960, "ypos" : 956, "zorder":15})
    return

#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label steve_office_office_teleport(obj_name, obj_data):
    if obj_name == "Teleport_Steve_Office_Secretary":
        call change_scene("steve_office_secretary")
        return
    return
label steve_office_office_environment(obj_name, obj_data):
    if obj_name == "Chair1" or obj_name == "Chair2" or obj_name == "Chair3" or obj_name == "Chair4" or obj_name == "Chair5" or obj_name == "Chair6" or obj_name == "Chair7" or obj_name == "Chair8" or obj_name == "Chair9" or obj_name == "Chair10":
        mt "Много стульев..."
        "Стив любит делать собрания."
        if bitchmeterValue > maxBitchness / 2:
            "Тщеславный ублюдок..."
    if obj_name == "Table":
        if obj_data["action"] == "l":
            mt "Большой стол..."
            "Стив любит делать собрания."
            if bitchmeterValue > maxBitchness / 2:
                "Тщеславный ублюдок..."
        if obj_data["action"] == "w":
            if steveOfficeSteveState == 0:
                call steve1_steve_talk1()
                call refresh_scene_fade()
                return
            if catchSteveInProgress == False and steveOfficeSteveInOffice == True:
                call steve1_steve_talk6()
                call refresh_scene_fade()
                return
            call change_scene("steve_office_office_table")
            return


    if obj_name == "Sofa":
        mt "Диван в кабинете?"
        "Это, наверное, здесь происходит ПРОДВИЖЕНИЕ по карьерной лестнице?"
    if obj_name == "Bar":
        mt "Милый бар..."
        "Книжки, цветочки."
        "Пускает пыль в глаза."
        "Я уверена что, если порыться, то в каждой книжке окажется спрятана бутылка алкоголя!"
    if obj_name == "Steve":
        if obj_data["action"] == "l":
            mt "Стив..."
            "Мой младший партнер..."
            if bitchmeterValue > maxBitchness / 2:
                mt "Скользкий мешок с дерьмом..."
            return
        if obj_data["action"] == "t":
            if steveOfficeSteveState == 0:
                call steve1_steve_talk1()
                call refresh_scene_fade()
                return
            if catchSteveInProgress == False and steveOfficeSteveInOffice == True:
                call steve1_steve_talk6()
                call refresh_scene_fade()
                return
    return
