default trainerInTheGym = True
default fitnessMonicaTrained = False
default fitnessMonicaTrainerTalked = False
default fitnessStephanieRebeccaInLocker = True
default fitnessStephanieRebeccaTalked = False
default fitnessStephanieSceneProcessed = False

label fitness_gym:
    $ print "enter_fitness_gym"
    $ miniMapData = []

    $ scene_name = "fitness_gym"
    $ scene_caption = _("Fitness Gym")
    $ clear_scene_from_objects(scene_name)
    if trainerInTheGym == True:
        $ scene_image = "scene_Fitness_Gym_Trainer_Monica_" + cloth
        $ add_object_to_scene("Monica", {"type":2, "base":"Fitness_Gym_Trainer_Monica_" + cloth, "click" : "fitness_gym_environment", "actions" : "l", "zorder" : 12})
        $ add_object_to_scene("Trainer", {"type":2, "base":"Fitness_Gym_Trainer", "click" : "fitness_gym_environment", "actions" : "lt", "zorder" : 10, "icon_t":"/Icons/talk" + res.suffix +".png"})

    $ add_object_to_scene("Pictures", {"type":2, "base":"Fitness_Gym_Pictures", "click" : "fitness_gym_environment", "actions" : "l", "zorder" : 0})
    $ add_object_to_scene("Fitness_Equipment", {"type":2, "base":"Fitness_Gym_Fitness_Equipment", "click" : "fitness_gym_environment", "actions" : "l", "zorder" : 0, "tint": [1.0, 1.0, 0.8]})
    $ add_object_to_scene("Yoga_Carpet", {"type":2, "base":"Fitness_Gym_Yoga_Carpet", "click" : "fitness_gym_environment", "actions" : "l", "zorder" : 0})


    $ add_object_to_scene("Teleport_Locker_1", {"type":3, "text" : _("В РАЗДЕВАЛКУ"), "rarrow" : "arrow_right_2", "base":"Fitness_Teleport_Locker_1", "click" : "fitness_gym_teleport", "xpos" : 609, "ypos" : 117, "zorder":11})
    $ add_object_to_scene("Teleport_Outside", {"type":3, "text" : _("НА УЛИЦУ"), "larrow" : "arrow_left_2", "base":"Fitness_Teleport_Outside", "click" : "fitness_gym_teleport", "xpos" : 1278, "ypos" : 91, "zorder":11})
    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label fitness_gym_teleport(obj_name, obj_data):
    if obj_name == "Teleport_Outside":
        if fitnessMonicaTrained == False:
            mt "Я пока не позанималась в зале."
            "Еще рано уезжать"
            return
        if cloth_type != "BusinessCloth":
            mt "Куда я пойду в таком виде?
            Мне надо переодеться!"
            return
        if fitnessStephanieSceneProcessed == False:
            call stephanie_fitness_scene1_1()
        call change_scene("street_fitness")
        return
    if obj_name == "Teleport_Locker_1":
        if fitnessMonicaTrainerTalked == False:
            call fitness1_trainer_talk1()
            $ fitnessMonicaTrainerTalked = True
        call change_scene("fitness_locker_1")
        return

    return
label fitness_gym_environment(obj_name, obj_data):
    if obj_name == "Pictures":
        mt "Это идеал? Не думаю.
        Идеал - это Я!"
    if obj_name == "Fitness_Equipment":
        mt "Здесь можно заниматься силовыми упражнениями, но я предпочитаю Йогу."
    if obj_name == "Yoga_Carpet":
        mt "Это коврик для Йоги.
        Не мой."
        "Мой всегда должен быть разложен к моему приходу.
        И никто не посмеет прикасаться к нему кроме меня!"
    if obj_name == "Monica":
        mt "Этот фитнесс-клуб меня пока устраивает.
        Пока..."
    if obj_name == "Trainer":
        if obj_data["action"] == "l":
            mt "Мой фитнесс-тренер.
            Он типа Мачо...
            Фи..."
            "Такой понравится только какой-нибудь глупой провинциалке..."
        if obj_data["action"] == "t":
            if fitnessMonicaTrained == False and cloth_type != "FitnessSuit":
                call fitness1_trainer_talk1()
                $ fitnessMonicaTrainerTalked = True
                return
            if fitnessMonicaTrained == False and cloth_type == "FitnessSuit":
                call fitness1_trainer_workout()
                return
            if fitnessMonicaTrained == True and  cloth_type == "FitnessSuit":
                call fitness1_trainer_talk2_repeat()
                return
            if fitnessMonicaTrained == True and  cloth_type != "FitnessSuit":
                mt "Мне не о чем сейчас разговаривать с этим болваном!"
                return

    return
