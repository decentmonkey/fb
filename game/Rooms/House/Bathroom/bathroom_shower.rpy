label bathroom_shower:
    $ print "enter_bathroom_shower"
    $ miniMapData = []
    call miniMapHouseGenerate()

    $ scene_name = "bathroom_shower"
    $ scene_caption = _("Bathroom Shower")
    $ clear_scene_from_objects(scene_name)
    $ scene_image = "scene_Bathroom_Shower_Monica_" + cloth

    $ add_object_to_scene("Monica", {"type" : 2, "base" : "Bathroom_Shower_Monica_" + cloth, "click" : "bathroom_environment", "actions" : "l", "zorder":10, "tint": monica_tint})


    $ add_object_to_scene("Shower", {"type":2, "base":"Bathroom_Shower_Shower", "click" : "bathroom_environment", "actions" : "lh", "zorder" : 0})

    $ add_object_to_scene("Teleport_Floor2", {"type":3, "text" : _("НАЗАД"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "bathroom_teleport", "xpos" : 990, "ypos" : 956, "zorder":11, "high_sprite_hover": True})
    $ add_object_to_scene("Teleport_Bathroom_Bath", {"type":3, "text" : _("ВАННА"), "larrow" : "arrow_left_2", "base":"Screen_Left_Arrow_Tight", "click" : "bathroom_teleport", "xpos" : 240, "ypos" : 520, "zorder":11})

    return
