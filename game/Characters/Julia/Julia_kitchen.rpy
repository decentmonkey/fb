label julia_interact2(obj_name, obj_data):
    if juliaFirePlanned == True:
        img 4259
        with fade
        julia "Миссис Бакфетт."
        "(хмык)"
        "Пожалуйста, присаживайтесь за стол."
        "(хмык)"
        "Я все подам Вам."
        "(хмык)"
        return

    if juliaMonicaForgivenessAfterPunishment == True:
        img 4258
        with fade
        julia "Миссис Бакфетт.
        Пожалуйста, присаживайтесь за стол.
        Я все подам Вам."
        img 4259
        "Спасибо Вам!!!
        Спасибо!!!"
        return

    if juliaMonicaYell == False and juliaPunished == False:
#        imgr Dial_Governess1
        img 4257
        with fade
        julia "Миссис Бакфетт.
        Пожалуйста, присаживайтесь за стол.
        Я все подам Вам."
        return

    if juliaMonicaYell == True and juliaPunished == False:
#        imgr Dial_Governess1
        img 4258
        with fade
        julia "Миссис Бакфетт.
        Пожалуйста, присаживайтесь за стол.
        Я все подам Вам."
        return

    if juliaPunished == True:
#        imgr Dial_Governess2
        img 4259
        with fade
        julia "Миссис Бакфетт.
        Пожалуйста, присаживайтесь за стол.
        Я все подам Вам."
    return
