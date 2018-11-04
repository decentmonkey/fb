label street_fitness_s2:

    $ print "enter_street_fitness_s2"
    $ miniMapData = []

    $ scene_name = "street_fitness_s2"
    $ sceneIsStreet = True
    $ scene_caption = _("Fitness")
    $ clear_scene_from_objects(scene_name)

    $ scene_image = "scene_fitness_street_Monica_" + cloth + day_suffix
    $ add_object_to_scene("Monica", {"type":2, "base":"Fitness_Street_Monica_" + cloth + day_suffix, "click" : "street_fitness_environment2", "actions" : "l", "zorder" : 10})

    $ add_object_to_scene("Teleport_Inside", {"type":2, "base":"Street_Fitness_Teleport_Inside", "click" : "street_fitness_teleport2", "actions" : "lw", "zorder" : 1})

    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label street_fitness_teleport2(obj_name, obj_data):
    if obj_name == "Teleport_Inside":
        if obj_data["action"] == "l":
            mt "Фитнес зал."
            "Я не хочу туда идти."
            "Меньше всего мне хотелось бы наткнуться на Стефани или Ребекку!"
            "Надо сначала решить мою небольшую проблему, а уже затем идти дальше заниматься своим телом!"
        if obj_data["action"] == "w":
            if day_time == "evening":
                mt "Уже вечер. Фитнесс зал закрыт."
                return
            "Я не хочу туда идти."
            "Меньше всего мне хотелось бы наткнуться на Стефани или Ребекку!"
            "Надо сначала решить мою небольшую проблему, а уже затем идти дальше заниматься своим телом!"
    return
label street_fitness_environment2(obj_name, obj_data):
    if obj_name == "Monica":
        if gameStage == 2 or gameStage == 3:
            "Я не пойду туда в таком виде!"
            "Меньше всего мне хотелось бы наткнуться на Стефани или Ребекку!"
            return
        "Я не хочу туда идти."
        "Меньше всего мне хотелось бы наткнуться на Стефани или Ребекку!"
        "Надо сначала решить мою небольшую проблему, а уже затем идти дальше заниматься своим телом!"

    return
