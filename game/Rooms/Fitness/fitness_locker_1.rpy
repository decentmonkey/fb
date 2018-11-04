label fitness_locker_1:
    $ print "enter_fitness_locker_1"
    $ miniMapData = []

    $ scene_name = "fitness_locker_1"
    $ scene_caption = _("Fitness Gym")
    $ clear_scene_from_objects(scene_name)
    if fitnessStephanieRebeccaInLocker == True:
        $ scene_image = "scene_fitness_locker_1_Stephanie_Rebecca"
        $ add_object_to_scene("Stephanie", {"type":2, "base":"fitness_locker_1_Stephanie", "click" : "fitness_locker_1_environment", "actions" : "lw", "zorder" : 12})
        $ add_object_to_scene("Rebecca", {"type":2, "base":"fitness_locker_1_Rebecca", "click" : "fitness_locker_1_environment", "actions" : "lw", "zorder" : 12})
    else:
        $ scene_image = "scene_fitness_locker_1"


#    $ add_object_to_scene("Lockers", {"type":2, "base":"fitness_locker_1_Lockers", "click" : "fitness_locker_1_environment", "actions" : "lw", "zorder" : 0})
    $ add_object_to_scene("Benches", {"type":2, "base":"fitness_locker_1_Benches", "click" : "fitness_locker_1_environment", "actions" : "l", "zorder" : 0})
    $ add_object_to_scene("Teleport_Lockers", {"type":3, "text" : _("ШКАФЧИКИ ДЛЯ ПЕРЕОДЕВАНИЯ"), "larrow" : "arrow_down_2", "base":"fitness_locker_1_Lockers", "click" : "fitness_locker_1_teleport", "xpos" : 1492, "ypos" : 311, "zorder":11})
    $ add_object_to_scene("Teleport_Gym", {"type":3, "text" : _("НАЗАД В ЗАЛ"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "fitness_locker_1_teleport", "xpos" : 960, "ypos" : 956, "zorder":11})
    if driveTriggers.has_key("stephanie_return_event") == True and driveTriggers["stephanie_return_event"] == "on":
        call stephanie_fitness_return_scene()
        call refresh_scene_fade()
    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label fitness_locker_1_teleport(obj_name, obj_data):
    if obj_name == "Teleport_Gym":
        call change_scene("fitness_gym")
        return
    if obj_name == "Teleport_Lockers":
        call change_scene("fitness_locker_2")
        return

    return
label fitness_locker_1_environment(obj_name, obj_data):
    if obj_name == "Benches":
        mt "Скамейки в раздевалке.
        Не знаю, может быть на них что-то и удобно делать, но точно не переодеваться!"
    if obj_name == "Stephanie":
        if obj_data["action"] == "l":
            mt "Это Стефани.
            Моя подружка."
            "У нее очень богатые и влиятельные родители.
            Потому я резрешаю ей дружить со мной."
            "Но она слишком помешана на мужчинах, как я считаю."
        if obj_data["action"] == "w":
            call change_scene("fitness_locker_2")
            return
    if obj_name == "Rebecca":
        if obj_data["action"] == "l":
            mt "Это Ребекка.
            Они слишком любит деньги и тех кто ими обладает.
            Но она часто льстит мне, потому я держу ее рядом со мной."
        if obj_data["action"] == "w":
            call change_scene("fitness_locker_2")
            return
    if obj_name == "Lockers":
        if obj_data["action"] == "l":
            mt "Шкафчики для переодевания.
            Один из них мой."
        if obj_data["action"] == "w":
            call change_scene("fitness_locker_2")
            return
    return
