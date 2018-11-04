init python:
    obj_properties_prefix = "img"
    obj_properties_suffixes = {" ":"sprite", "_evening":"sprite", "_mask":"mask", "_overlay":"overlay", "_evening_mask":"mask", "_evening_overlay":"overlay"}

    def fill_object_properties(name, obj_data):
        obj_base = obj_data["base"]
        asset_found = False
        for suffix in obj_properties_suffixes:
            suffix_type = obj_properties_suffixes[suffix]
            if suffix == " ":
                suffix = ""
            obj_prop_name = obj_properties_prefix + suffix
            if obj_data.has_key(obj_prop_name) == False:
                obj_data[obj_prop_name] = get_image_filename(obj_base + suffix)
                canvas_base_name = obj_base + suffix
                canvas_offset = get_canvas_offset(canvas_base_name)
                if obj_data[obj_prop_name] != False: asset_found = True
            else:
                canvas_base_name = obj_data[obj_prop_name]
                canvas_offset = get_canvas_offset(canvas_base_name)
                obj_data[obj_prop_name] = get_image_filename(obj_data[obj_prop_name])
#                if name == "Spot":
#                    print "canvas_" + obj_prop_name
#                    print canvas_offset

            if canvas_offset != False:
                obj_data["canvas_" + obj_prop_name] = canvas_offset

        if asset_found == False:
            ui.text("Assets not found for " + name + "\nScene name: " + scene_name, size=40, xalign=0.5, yalign=0.5)
            renpy.pause()
        return obj_data

    def add_object_to_scene_many(data):
        for room_name in data:
            if scenes_data["objects"].has_key(room_name) == False:
                scenes_data["objects"][room_name] = {}

            for obj_name in data[room_name]:
                obj_data = fill_object_properties(obj_name, data[room_name][obj_name])
                if obj_data.has_key("actions") == False: obj_data["actions"] = "l" # по дефолту всегда есть взгляд в действиях с предметом
                if obj_data.has_key("zorder") == False: obj_data["zorder"] = 0
                if obj_data.has_key("larrow") == False:
                    obj_data["larrow"] = False
                else:
                    obj_data["larrow"] = get_image_filename(obj_data["larrow"] + res.suffix)
                    obj_data["larrow_hover"]
                if obj_data.has_key("rarrow") == False:
                    obj_data["rarrow"] = False
                else:
                    obj_data["rarrow"] = get_image_filename(obj_data["rarrow"] + res.suffix)
                obj_data["hover_overlay"] = obj_data["hover_overlay"] if obj_data.has_key("hover_overlay") else False
                obj_data["hover_enabled"] = obj_data["hover_enabled"] if obj_data.has_key("hover_enabled") else True
                scenes_data["objects"][room_name][obj_name] = obj_data
#        print scenes_data
        return

    def add_object_to_scene(obj_name, data, room_name = False): #adds to current scene
        if room_name == False: room_name = scene_name
        if scenes_data["objects"].has_key(room_name) == False:
            scenes_data["objects"][room_name] = {}

        obj_data = fill_object_properties(obj_name, data)
        obj_data["name"] = obj_name
        if obj_data.has_key("actions") == False: obj_data["actions"] = "l" # по дефолту всегда есть взгляд в действиях с предметом
        if obj_data.has_key("zorder") == False: obj_data["zorder"] = 0
        if obj_data.has_key("larrow") == False:
            obj_data["larrow"] = False
        else:
            obj_data["larrow"] = get_image_filename(obj_data["larrow"] + res.suffix)
        if obj_data.has_key("rarrow") == False:
            obj_data["rarrow"] = False
        else:
            obj_data["rarrow"] = get_image_filename(obj_data["rarrow"] + res.suffix)
        obj_data["hover_overlay"] = obj_data["hover_overlay"] if obj_data.has_key("hover_overlay") else False
        obj_data["hover_enabled"] = obj_data["hover_enabled"] if obj_data.has_key("hover_enabled") else True
        scenes_data["objects"][room_name][obj_name] = obj_data
#        print obj_data
#        print scenes_data
        return

    def remove_object_from_scene(scene, obj_name):
        if obj_name in scenes_data["objects"][scene]: del scenes_data["objects"][scene][obj_name]
        return

    def clear_scene_from_objects(scene):
        scenes_data["objects"][scene] = {}
        return


    def subst_to_object(obj_name, subst_func):
        if subst_func != False:
            scenes_data["substs"][obj_name] = subst_func
        else:
            if obj_name in scenes_data["substs"]:
                del scenes_data["substs"][obj_name]
        return

    def autorun_to_object(obj_name, autorun_func):
        if autorun_func != False:
            scenes_data["autorun"][obj_name] = autorun_func
        else:
            if obj_name in scenes_data["autorun"]:
                del scenes_data["autorun"][obj_name]
        return

    def get_object_actions(actions_str):
        actions = []
        for idx in range(0, len(actions_str)):
            if actions_objects.has_key(actions_str[idx]):
                objects_to_append = actions_objects[actions_str[idx]]
                objects_to_append["action"] = actions_str[idx]
                actions.append(objects_to_append)

        return actions


label process_object_click(func_name, obj_name, obj_data):
    if clickHoldMode == True and clickHoldFlag == True:
        $ x,y = renpy.get_mouse_pos()
        if time.time() - clickHoldLastTime < 1 and abs(x - clickHoldLastMouseX) < 3 and abs(y - clickHoldLastMouseY) < 3:
#            $ clickHoldFlag = False
#            show screen notify ("click holded!!!")
            return

    if interface_blocked_flag == True:
        return
#    $ print renpy.get_screen("say")
    if renpy.get_screen("say") != None or renpy.get_screen("choice") != None:
        return
    if scenes_data["substs"].has_key(obj_name):
        if scenes_data["substs"][obj_name] != False:
            $ func_name = scenes_data["substs"][obj_name]
    hide screen action_menu_screen
    show screen sprites_hover_dummy_screen()
    $ obj_data["action"] = obj_data["actions"]
    $ interface_blocked_flag = True
    $ screenActionHappened = False
    $ act = obj_data["action"]
    call expression func_name pass (obj_name, obj_data) from _call_expression
    if screenActionHappened == True:
        $ clickHoldFlag = True
        $ clickHoldLastTime = time.time()
        $ clickHoldLastMouseX,clickHoldLastMouseY = renpy.get_mouse_pos()

    $ interface_blocked_flag = False
    if _return != False:
        $ scene_refresh_flag = True
    else:
        $ scene_refresh_flag = False
#        $ dialogue_active_flag = False
    $ show_scene_loop_flag = True
    $ parse_transition_flag = False
    return
#    jump show_scene

#    return

label process_object_click_alternate_action(idx, actions_list, click_label, name, data):
    if interface_blocked_flag == True:
        return
    if renpy.get_screen("say") != None or renpy.get_screen("choice") != None:
        return
    if idx == 0:
        $ func_name = click_label
    else:
        if renpy.has_label(name + actions_list[idx]["label_suffix"]) == False:
            $ func_name = click_label
        else:
            $ func_name = name + actions_list[idx]["label_suffix"]

#    call showLog("alternate action click!") from _call_showLog
    hide screen action_menu_screen
    #проверяем подстановку
    if func_name == click_label:
        if scenes_data["substs"].has_key(name):
            if scenes_data["substs"][name] != False:
                $ func_name = scenes_data["substs"][name]

    $ data["action"] = actions_list[idx]["action"]
    show screen sprites_hover_dummy_screen()
    $ interface_blocked_flag = True
    $ act = data["action"]
    call expression func_name pass (name, data) from _call_expression_1
    $ interface_blocked_flag = False
    if _return != False:
        $ scene_refresh_flag = True
    else:
        $ scene_refresh_flag = False
#        $ dialogue_active_flag = False
    $ show_scene_loop_flag = True
    $ parse_transition_flag = False
    return
#    jump show_scene
#    return

label process_object_click_alternate_inventory(idx, inventory_data, click_label, name, data):
    if interface_blocked_flag == True:
        return
    if renpy.get_screen("say") != None or renpy.get_screen("choice") != None:
        return
    $ func_name = name + inventory_data["label_suffix"]
    $ shortFunction = True
    if renpy.has_label(func_name) == False:
        $ func_name = inventory_data["default_nolabel"]
        $ shortFunction = False

#    call showLog("alternate inventory click!") from _call_showLog_1
    hide screen action_menu_screen
    show screen sprites_hover_dummy_screen()

    $ data["action"] = "inv"
    $ interface_blocked_flag = True
    $ act = data["action"]
    if shortFunction == False:
        call expression func_name pass (name, inventory[idx], inventory_data, data) from _call_expression_2
    else:
        call expression func_name from _call_expression_6
    $ interface_blocked_flag = False
    if _return != False:
        $ scene_refresh_flag = True
    else:
        $ scene_refresh_flag = False
#        $ dialogue_active_flag = False
#        jump show_scene
    $ show_scene_loop_flag = True
    $ parse_transition_flag = False
    return
#    jump show_scene
