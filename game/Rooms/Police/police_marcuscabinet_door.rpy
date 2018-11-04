default marcusCabinetDoorState = 0

label police_marcuscabinet_door:
    $ print "enter_police_marcuscabinet_door"
    $ miniMapData = []

    $ scene_name = "police_marcuscabinet_door"
    $ scene_caption = _("Marcus Cabinet")
    $ clear_scene_from_objects(scene_name)

    if marcusCabinetDoorState == 0:
        $ scene_image = "scene_Police_MarcusCabinet2_Monica_1"
        $ add_object_to_scene("Monica", {"type":2, "base":"Police_MarcusCabinet2_Monica_1", "click" : "police_marcuscabinet_door_environment", "actions" : "l", "zorder" : 10})

    if marcusCabinetDoorState == 1:
        $ scene_image = "scene_Police_MarcusCabinet2_Monica_2"
        $ add_object_to_scene("Monica", {"type":2, "base":"Police_MarcusCabinet2_Monica_2", "click" : "police_marcuscabinet_door_environment", "actions" : "l", "zorder" : 10})

    $ add_object_to_scene("FileCabinet", {"type":2, "base":"Police_MarcusCabinet2_FileCabinet", "click" : "police_marcuscabinet_environment", "actions" : "l", "zorder" : 0})
    $ add_object_to_scene("Door", {"type":2, "base":"Police_MarcusCabinet2_Door", "click" : "police_marcuscabinet_door_teleport", "actions" : "lw", "zorder" : 0})

#    $ add_object_to_scene("Telepost_Police_Entrance", {"type":3, "text" : _("ВЫХОД"), "larrow" : "arrow_down_2", "base":"police_marcuscabinet_door_Teleport_Entrance", "click" : "police_marcuscabinet_door_teleport", "xpos" : 100, "ypos" : 716, "zorder":5})
    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label police_marcuscabinet_door_teleport(obj_name, obj_data):
    if obj_name == "Door":
        if obj_data["action"] == "l":
            if marcusCabinetDoorState == 0:
                mt "Это, по всей видимости, и есть выход."
                "Все, я ухожу!!!"
            if marcusCabinetDoorState == 1:
                mt "О БОЖЕ!!!"
                "Я НЕ ОСТАНУСЬ ЗДЕСЬ!!!"
                "ВЫПУСТИТЕ МЕНЯ!!!"
        if obj_data["action"] == "w":
            if marcusCabinetDoorState == 0:
                mt "Это, по всей видимости, и есть выход."
                "Все, я ухожу!!!"
                call marcus_cabinet_dialogue3()
                return
            if marcusCabinetDoorState == 1:
                call marcus_cabinet_dialogue8()
                return

    return
label police_marcuscabinet_door_environment(obj_name, obj_data):
    if obj_name == "Monica":
        if marcusCabinetDoorState == 0:
            mt "Я не собираюсь больше общаться с этим уродом!"
            "Я ухожу!!!"
        if marcusCabinetDoorState == 1:
            mt "О БОЖЕ!!!"
            "Я НЕ ОСТАНУСЬ ЗДЕСЬ!!!"
            "ВЫПУСТИТЕ МЕНЯ!!!"


    return
