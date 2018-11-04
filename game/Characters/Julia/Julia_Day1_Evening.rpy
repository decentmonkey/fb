label julia_day1_evening(obj_name, obj_data):
    if obj_data["action"] == "l":
        call floor1_monica_julia_revenge_interact_look()
        return
    if obj_data["action"] == "t":
        if monicaEated == True:
            call julia_monica_eated()
            return
        if cloth_type != "HomeCloth":
            m "Мне надо сначала переодеться, а потом уже приказывать Юлии подавать еду!"
            return
        if juliaMonicaYell == False and juliaPunished == False:
            $ imageName = "4254" + day_suffix
            img imageName

        if juliaMonicaYell == True and juliaPunished == False:
            $ imageName = "4255" + day_suffix
            img imageName

        if juliaPunished == True:
            $ imageName = "4256" + day_suffix
            img imageName
        with fade

        julia "Миссис Бакфетт.
        Вам подать еду?"
        m "Да, Юлия.
        Можешь подавать."
        julia "Слушаюсь, Миссис Бакфетт!"
        $ juliaLocation = "kitchen"
        sound highheels_run1
        call refresh_scene_fade()
        show screen notify (_("Юлия убежала на кухню."))
        return

    return

label julia_monica_eated:
    if juliaMonicaYell == False and juliaPunished == False:
        $ imageName = "4254" + day_suffix
        img imageName

    if juliaMonicaYell == True and juliaPunished == False:
        $ imageName = "4255" + day_suffix
        img imageName

    if juliaPunished == True:
        $ imageName = "4256" + day_suffix
        img imageName
    with fade
    julia "Миссис Бакфетт.
    Вы уже кушали недавно."
    "Вам подать снова?"

    menu:
        "Не надо, продолжай работу.":
            m "Не надо, продолжай работу."
            if juliaPunishedVoluntarily == True:
                m "Не забудь про уборку пятна в свободное время..."
            if juliaPunishedLow == True:
                m "Я не заставила тебя убирать пятно, но у тебя есть другие обязанности."
                "Не забывай про них."
            julia "Конечно, Миссис Бакфетт."

        "Похвалить Юлию за вкусную еду." if juliaPraiseOnOccasion == True:
            m "Ты готовишь довольно вкусно, Юлия."
            julia "Спасибо, Миссис Бакфетт!"
            call bitch(-5, "juliaPraiseOnOccasion")

    return
