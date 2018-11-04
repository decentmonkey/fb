default basementHoleRefuseFlag = True
default basementHoleStage = 0
default basementHoleIncomingDirection = ""

label basement_hole_check:
    if basementHoleRefuseFlag == True:
        sound highheels_run2
        $ img1_name = "Basement_Hole_Refuse_Monica_" + cloth + "_1"
        $ img2_name = "Basement_Hole_Refuse_Monica_" + cloth + "_2"
    #    if day == 1:
    #        if cloth_type == "HomeCloth":
    #            img Basement_Hole_Refuse_Monica_HomeCloth1_1
    #            with fade
    #        if cloth_type == "BusinessCloth":
    #            img Basement_Hole_Refuse_Monica_BusinessCloth1_1
    #            with fade
        img img1_name
        m "Не, я не собираюсь туда идти.
        Там темно и какая-то вонь."

    #    if day == 1:
    #        if cloth_type == "HomeCloth":
    #            img Basement_Hole_Refuse_Monica_HomeCloth1_2
    #        if cloth_type == "BusinessCloth":
    #            img Basement_Hole_Refuse_Monica_BusinessCloth1_1
        img img2_name
        m "Более того, я не собираюсь не только сейчас туда идти.

        Но и вообще никогда!!!"

        "Не для моего статуса ползать по всяким подвалам!!!"
        sound highheels_run2
        return

label basement_hole:
    $ print "enter_basement_hole"
    $ miniMapData = []
    call miniMapHouseGenerate()

    $ scene_name = "basement_hole"
    $ scene_caption = _("Basement")
    $ clear_scene_from_objects(scene_name)

    $ monica_tint = [1.0, 1.0, 0.9]

    if cloth == "Whore":
        if basementHoleIncomingDirection == "Laundry":
            $ scene_image = "scene_Basement_Hole_Monica_Whore_1"
            $ add_object_to_scene("Monica", {"type" : 2, "base" : "Basement_Hole_Monica_Whore_1", "click" : "basement_hole_environment", "actions" : "l", "zorder":10, "tint": monica_tint})
        if basementHoleIncomingDirection == "Bedroom":
            $ scene_image = "scene_Basement_Hole_Monica_Whore_2"
            $ add_object_to_scene("Monica", {"type" : 2, "base" : "Basement_Hole_Monica_Whore_2", "click" : "basement_hole_environment", "actions" : "l", "zorder":10, "tint": monica_tint})

    if cloth == "Governess":
        if basementHoleStage == 0:
            $ scene_image = "scene_Basement_Hole_Monica_Governess"
            $ add_object_to_scene("Monica", {"type" : 2, "base" : "Basement_Hole_Monica_Governess", "click" : "basement_hole_environment", "actions" : "l", "zorder":10, "tint": monica_tint})
        if basementHoleStage == 1:
            if basementHoleIncomingDirection == "Laundry":
                $ scene_image = "scene_Basement_Hole_Monica_Governess_2"
                $ add_object_to_scene("Monica", {"type" : 2, "base" : "Basement_Hole_Monica_Governess_2", "click" : "basement_hole_environment", "actions" : "l", "zorder":10, "tint": monica_tint})
            if basementHoleIncomingDirection == "Bedroom":
                $ scene_image = "scene_Basement_Hole_Monica_Governess_3"
                $ add_object_to_scene("Monica", {"type" : 2, "base" : "Basement_Hole_Monica_Governess_3", "click" : "basement_hole_environment", "actions" : "l", "zorder":10, "tint": monica_tint})


    $ add_object_to_scene("Lamp", {"type":2, "base":"Basement_Hole_Lamp", "click" : "basement_hole_environment", "actions" : "l", "zorder" : 0})
    $ add_object_to_scene("Trash1", {"type":2, "base":"Basement_Hole_Trash1", "click" : "basement_hole_environment", "actions" : "l", "zorder" : 0})
    $ add_object_to_scene("Trash2", {"type":2, "base":"Basement_Hole_Trash2", "click" : "basement_hole_environment", "actions" : "l", "zorder" : 0})
    $ add_object_to_scene("Trash3", {"type":2, "base":"Basement_Hole_Trash3", "click" : "basement_hole_environment", "actions" : "l", "zorder" : 0})
    $ add_object_to_scene("Trash4", {"type":2, "base":"Basement_Hole_Trash4", "click" : "basement_hole_environment", "actions" : "l", "zorder" : 0})
    $ add_object_to_scene("Trash5", {"type":2, "base":"Basement_Hole_Trash5", "click" : "basement_hole_environment", "actions" : "l", "zorder" : 0})

    if basementBedroomFound == False:
        $ add_object_to_scene("Teleport_Basement_Bedroom", {"type":3, "text" : _("ДАЛЬНИЙ КОРИДОР"), "rarrow" : "arrow_right_2", "base":"Basement_Hole_Teleport_Bedroom", "click" : "basement_hole_teleport", "xpos" : 1334, "ypos" : 232, "zorder":15, "high_sprite_hover": True})
    else:
        $ add_object_to_scene("Teleport_Basement_Bedroom", {"type":3, "text" : _("СПАЛЬНЯ ДЛЯ ПРИСЛУГИ"), "rarrow" : "arrow_right_2", "base":"Basement_Hole_Teleport_Bedroom", "click" : "basement_hole_teleport", "xpos" : 1334, "ypos" : 232, "zorder":15, "high_sprite_hover": True})
    $ add_object_to_scene("Teleport_Basement_Laundry", {"type":3, "text" : _("ПРАЧЕЧНАЯ"), "larrow" : "arrow_down_2", "base":"Basement_Hole_Teleport_Laundry", "click" : "basement_hole_teleport", "xpos" : 960, "ypos" : 956, "zorder":15, "high_sprite_hover": True})
    $ add_object_to_scene("Teleport_Basement_Side", {"type":3, "text" : _("ТЕМНЫЙ ПРОХОД"), "rarrow" : "arrow_right_2", "base":"Basement_Hole_Teleport_Side", "click" : "basement_hole_teleport", "xpos" : 693, "ypos" : 184, "zorder":15, "high_sprite_hover": True})
    return

#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label basement_hole_teleport(obj_name, obj_data):
    if obj_name == "Teleport_Basement_Laundry":
        call change_scene("basement_laundry")
        return
    if obj_name == "Teleport_Basement_Bedroom":
        if basementBedroomFound == False:
            call afterJailHouse_dialogue19()
            call change_scene("basement_bedroom2", "Fade_long")
            return
        call change_scene("basement_bedroom1")
        return
    if obj_name == "Teleport_Basement_Side":
        mt "В том коридоре нет света. Я туда не пойду!"
    return

label basement_hole_environment(obj_name, obj_data):
    if obj_name == "Monica":
        mt "Какой жуткий коридор..."

    if obj_name == "Lamp":
        mt "Я не знала что в моем доме есть такие древние лампы..."

    if obj_name == "Trash1" or obj_name == "Trash2" or obj_name == "Trash3" or obj_name == "Trash4" or obj_name == "Trash5":
        mt "Какой-то бесполезный хлам..."
    return
