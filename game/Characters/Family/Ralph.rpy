default ralphLocation = "none"
default ralphStage = 0
default ralphAskedAboutPayment = False

label ralphInteract1(obj_name, obj_data):
    if act == "l":
        mt "Это Ральф."
        "Подкаблучник."
        "Бетти неплохо выдрессировала его, надо отдать должное ей."
        "Но мужчины такими и должны быть."
        "Мы, женщины, выше мужчин и они должны это понимать!"
    if act == "t":
        if ralphLocation == "LivingRoom":
            if ralphStage == 1:
                call ralphDialogue2()
                return
            if ralphStage == 0:
                call ralphDialogue1()
                return
        call refresh_scene_fade()
        return
    return
