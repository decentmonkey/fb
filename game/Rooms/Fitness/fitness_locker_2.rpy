label fitness_locker_2:
    $ print "enter_fitness_locker_2"
    $ miniMapData = []

    $ scene_name = "fitness_locker_2"
    $ scene_caption = _("Fitness Gym")
    $ clear_scene_from_objects(scene_name)
    if fitnessStephanieRebeccaInLocker == True:
        if fitnessStephanieRebeccaTalked == False:
            $ scene_image = "scene_fitness_locker_2_Stephanie_Rebecca_Monica_" + cloth
            $ add_object_to_scene("Monica", {"type":2, "base":"Fitness_Locker_2_Stephanie_Rebecca_Monica_" + cloth, "click" : "fitness_locker_2_environment", "actions" : "l", "zorder" : 12})
        else:
            $ scene_image = "scene_fitness_locker_2_Stephanie_Rebecca_Monica2_" + cloth
            $ add_object_to_scene("Monica", {"type":2, "base":"Fitness_Locker_2_Stephanie_Rebecca_Monica2_" + cloth, "click" : "fitness_locker_2_environment", "actions" : "l", "zorder" : 12})
        $ add_object_to_scene("Stephanie", {"type":2, "base":"fitness_locker_2_Stephanie", "click" : "fitness_locker_2_environment", "actions" : "lt", "zorder" : 12})
        $ add_object_to_scene("Rebecca", {"type":2, "base":"fitness_locker_2_Rebecca", "click" : "fitness_locker_2_environment", "actions" : "lt", "zorder" : 12})

    else:
        if cloth_type == "BusinessCloth":
            $ scene_image = "scene_fitness_locker_2_Monica_" + cloth
            $ add_object_to_scene("Monica", {"type":2, "base":"Fitness_Locker_2_Monica_" + cloth, "click" : "fitness_locker_2_environment", "actions" : "l", "zorder" : 12})
        if cloth == "FitnessSuit":
            if fitnessMonicaTrained == False:
                $ scene_image = "scene_fitness_locker_2_Monica_" + cloth
                $ add_object_to_scene("Monica", {"type":2, "base":"Fitness_Locker_2_Monica_" + cloth, "click" : "fitness_locker_2_environment", "actions" : "l", "zorder" : 12})
            else:
                $ scene_image = "scene_fitness_locker_2_Monica2_" + cloth
                $ add_object_to_scene("Monica", {"type":2, "base":"Fitness_Locker_2_Monica2_" + cloth, "click" : "fitness_locker_2_environment", "actions" : "l", "zorder" : 12})




    $ add_object_to_scene("Monica_Locker", {"type":2, "base":"fitness_locker_2_Monica_Locker", "click" : "fitness_locker_2_environment", "actions" : "lh", "zorder" : 0})
    $ add_object_to_scene("Benches", {"type":2, "base":"fitness_locker_2_Benches", "click" : "fitness_locker_1_environment", "actions" : "l", "zorder" : 0})
    $ add_object_to_scene("Teleport_Gym", {"type":3, "text" : _("НАЗАД В ЗАЛ"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "fitness_locker_2_teleport", "xpos" : 960, "ypos" : 956, "zorder":15})
    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label fitness_locker_2_teleport(obj_name, obj_data):
    if obj_name == "Teleport_Gym":
        call change_scene("fitness_gym")
        return

    return
label fitness_locker_2_environment(obj_name, obj_data):
    if obj_name == "Stephanie":
        if obj_data["action"] == "l":
            mt "Это Стефани.
            Моя подружка."
            "У нее очень богатые и влиятельные родители.
            Потому я резрешаю ей дружить со мной."
            "Но она слишком помешана на мужчинах, как я считаю."
        if obj_data["action"] == "t":
            if fitnessStephanieRebeccaTalked == False:
                call fitness1_stephanie_rebecca_talk1()
                return
            call fitness1_stephanie_talk2()
            return
    if obj_name == "Rebecca":
        if obj_data["action"] == "l":
            mt "Это Ребекка.
            Они слишком любит деньги и тех кто ими обладает.
            Но она часто льстит мне, потому я держу ее рядом со мной."
        if obj_data["action"] == "t":
            if fitnessStephanieRebeccaTalked == False:
                call fitness1_stephanie_rebecca_talk1()
                return
            call fitness1_rebecca_talk2()
            return
    if obj_name == "Monica":
        if fitnessStephanieRebeccaTalked == False:
            mt "А вот и мои подружки!"
            return
        if fitnessMonicaTrained == False and cloth_type == "BusinessCloth":
            mt "Мне надо переодеться в мою спортивную форму."
            return
        if fitnessMonicaTrained == False and cloth_type == "FitnessSuit":
            mt "В нем так удобно!!"

        if fitnessMonicaTrained == True and cloth_type != "BusinessCloth":
            mt "Я позанималась."
            "Обожаю это состояние легкости в теле."
            "Мне надо почаще приходить сюда..."
            "А теперь надо переодеться."
            return
        if fitnessMonicaTrained == True and cloth_type == "BusinessCloth":
            mt "Я позанималась."
            "Обожаю это состояние легкости в теле."
            "Мне надо почаще приходить сюда..."
            "А теперь надо ехать в Банк."
            "У меня подозрения насчет Стива..."

    if obj_name == "Monica_Locker":
        if obj_data["action"] == "l":
            mt "Мой шкафчик.
            Здесь я могу переодеться."
        if obj_data["action"] == "h":
            if fitnessStephanieRebeccaTalked == False:
                call fitness1_stephanie_rebecca_talk1()
                return
            if fitnessStephanieRebeccaInLocker == True:
                menu:
                    "Переодеться...":
                        call fitness1_change_cloth1()
                        return
                    "Отойти.":
                        return
            if fitnessMonicaTrained == True and cloth_type == "FitnessSuit":
                menu:
                    "Переодеться...":
                        call fitness1_change_cloth2()
                        return
                    "Отойти.":
                        return
            if fitnessMonicaTrained == True and cloth_type == "BusinessCloth":
                mt "Мне не к чему переодеваться, пора ехать по делам!"
                return

#                    $ add_objective("change_cloth_to_fitness", _("Переодеться в раздевалке"), c_green, 20)


    return
