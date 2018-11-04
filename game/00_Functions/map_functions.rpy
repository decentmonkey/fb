init python:

    def focus_map(place_to_focus, disabled_label):
        global map_objects, mapFocusedObjects
        for place_name in map_objects:
            if place_name != place_to_focus and place_name != "Teleport_" + place_to_focus:
                #disabling place
                if map_objects[place_name]["state"] != "invisible":
                    mapFocusedObjects.append([place_name, map_objects[place_name]["state"], scenes_data["substs"][place_name] if scenes_data["substs"].has_key(place_name) else False])
                    map_objects[place_name]["state"] = "disabled"
                    subst_to_object(place_name, disabled_label)



        map_objects[place_to_focus]["state"] = "visible"
        hud_preset_current = "map_locked"
        return

    def unfocus_map():
        global map_objects, mapFocusedObjects
        for place_arr in mapFocusedObjects:
            place_name = place_arr[0]
            map_state = place_arr[1]
            object_subst = place_arr[2]
            if map_state == "active":
                map_state = "visible"
            map_objects[place_name]["state"] = map_state
            subst_to_object(place_name, object_subst)
        mapFocusedObjects = []
        hud_preset_current = "default"
        return
