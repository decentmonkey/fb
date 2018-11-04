define cageInteractAmount = 5
default cageInteractLabel = ""
default jailCageLastScene = ""

label police_jail_cage_scene:
    $ print "enter_police_jail_cage_scene"
    $ miniMapData = []

    $ jailCageLastScene = scene_name
    $ scene_name = "police_jail_cage_scene"
    $ scene_caption = _("JAIL")
    $ clear_scene_from_objects(scene_name)

    $ scene_image = "scene_Police_Cell_3"
    $ add_object_to_scene("Cage", {"type":2, "base": "Police_Cell_3_Cage", "click" : "police_jail_cage_scene_environment", "actions" : "l", "zorder" : 1})
    if cloth == "Nude":
        $ add_object_to_scene("Monica", {"type":2, "base": "Police_Cell_3_Nude", "click" : "police_jail_cage_scene_environment", "actions" : "l", "zorder" : 10})
    else:
        $ add_object_to_scene("Monica", {"type":2, "base": "Police_Cell_3", "click" : "police_jail_cage_scene_environment", "actions" : "l", "zorder" : 10})

    $ cageInteractCnt = cageInteractAmount
    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label police_jail_cage_scene_teleport(obj_name, obj_data):
    return
label police_jail_cage_scene_environment(obj_name, obj_data):
    if obj_name == "Cage":
        $ cageInteractCnt = cageInteractCnt - 1
        if cageInteractCnt > 0:
            sound snd_jail_door_locked
            return
        call change_scene(jailCageLastScene, "Fade", False)
        call expression cageInteractLabel
        return
    if obj_name == "Monica":
        mt "Надо дергать эту проклятую решетку!"
        "Иначе меня никто не услышит!"

    return
