label street_fitness:

    $ print "enter_street_fitness"
    $ miniMapData = []

    $ scene_name = "street_fitness"
    $ sceneIsStreet = True
    $ scene_caption = _("Fitness")
    $ clear_scene_from_objects(scene_name)

    if bFredFollowingMonica == True:
        $ scene_image = "scene_fitness_street_Driver_Monica_" + cloth + day_suffix
        $ add_object_to_scene("Monica", {"type":2, "base":"Fitness_Street_Driver_Monica_" + cloth + day_suffix, "click" : "street_fitness_environment", "actions" : "l", "zorder" : 10})
        $ add_object_to_scene("Car", {"type":2, "base":"Street_Fitness_Car", "click" : "street_house_main_yard_environment", "actions" : "l", "zorder" : 3})
        $ add_object_to_scene("Driver", {"type":2, "base":"Street_Fitness_Driver", "click" : "street_cloth_shop_environment", "actions" : "lt", "zorder" : 5, "icon_t":"/Icons/talk" + res.suffix +".png", "b":0.2, "s":1.3, "tint":[1.0, 1.0, 0.8]})
    else:
        $ scene_image = "scene_fitness_street_Monica_" + cloth + day_suffix
        $ add_object_to_scene("Monica", {"type":2, "base":"Fitness_Street_Monica_" + cloth + day_suffix, "click" : "street_fitness_environment", "actions" : "l", "zorder" : 10})

    $ add_object_to_scene("Teleport_Inside", {"type":2, "base":"Street_Fitness_Teleport_Inside", "click" : "street_fitness_teleport", "actions" : "lw", "zorder" : 1})

    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label street_fitness_teleport(obj_name, obj_data):
    if obj_name == "Teleport_Inside":
        if obj_data["action"] == "l":
            m "Фитнес зал."
            "Не особо большой, но, по крайней мере, сюда не ходят разные нищеброды."
            "Которые любят пялиться на девушек, не имея при этом банковского счета..."
            "У меня свои правила здесь.
            Когда я занимаюсь, никто больше в зал не допущен!"
        if obj_data["action"] == "w":
            if day_time == "evening":
                mt "Уже вечер. Фитнесс зал закрыт."
                return
            $ remove_objective("go_fitness")
            call change_scene("fitness_gym")
            return
            stop music fadeout 4.0
            scene black_screen
            with Dissolve(1)
            call textonblack_long("The End of V0.2\nTo be continued very soon...\nCheck for updates!")
            scene black_screen
            with Dissolve(1)
            $ renpy.full_restart(transition=Fade(1.0, 1.0, 1.0))

    return
label street_fitness_environment(obj_name, obj_data):
    if obj_name == "Driver":
        if obj_data["action"] == "l":
            call monica_looking_to_fred1()
            return
        if obj_data["action"] == "t":
            call get_to_drive_dialogue()
            return
    if obj_name == "Monica":
        m "Наконец-то я добралась до фитнеса!"

    return
