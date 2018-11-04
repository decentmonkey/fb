default juliaPunishedChecked = False

label quest_house_monica_day1_evening_init:
    $ autorun_to_object("floor1", "quest_house_monica_day1_evening1")
    return

label quest_house_monica_day1_evening1:
    $ add_objective("dress_homecloth", _("Одеть домашнюю одежду"), c_blue, 0)
    $ add_objective("take_bath", _("Принять душ"), c_green, 1)
    $ add_objective("eat", _("Поужинать"), c_orange, 2)
    $ add_objective("sleep", _("Лечь спать"), c_orange, 4)
    $ subst_to_object("Wardrobe", False)
    $ houseOutMode = "evening"
    $ bathTakenJust = False
    $ bathTaken = False
    $ monicaEated = False
#    $ juliaPunished = False #debug
#    $ juliaPunishedLow = True #debug
#    $ juliaMonicaLied = False #debug
#    $ juliaPunishedVoluntarily = True #debug
#    $ juliaMonicaYell = False #debug
#    $ juliaPunishedNone = True #debug
#    $ juliaLocation = "floor1" #debug
    m "Мне надо переодеться."
    "Поесть."
    "Принять ванну и ложиться спать."

    $ miniMapEnabledOnly = []

    if juliaPunished == True:
        m "Да, и еще надо проверить эту гувернантку!"
        "Как там поживает пятно на ковре?!"
        $ juliaPunishedChecked = False
        $ add_objective("julia_check_spot", _("Проверить Юлию"), c_red, 3)
    return
