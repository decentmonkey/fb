default juliaFloor2Looked2 = False
label floor1_monica_julia_revenge_interact:
    if obj_data["action"] == "l":
        call floor1_monica_julia_revenge_interact_look() from _call_floor1_monica_julia_revenge_interact_look
        $ juliaFloor2Looked2 = True
        return
    if obj_data["action"] == "t":
        if juliaFloor2Looked2 == False:
            call floor1_monica_julia_revenge_interact_look() from _call_floor1_monica_julia_revenge_interact_look_1

        if monicaEated == True:

            if juliaPunishedLow == True:
                m "Юлия!
                Быстро ко мне!"
                sound highheels_run1
                #imgr Dial_Governess1
                $ imageName = "4255" + day_suffix
                img imageName
                julia "Да, конечно, Миссис Бакфетт!"


            if juliaPunishedNone == True or juliaPunishedVoluntarily == True:
                m "Юлия, можно к тебе обратиться?"
                sound highheels_run1
                #imgr Dial_Governess1
                $ imageName = "4254" + day_suffix
                img imageName
                julia "Да, конечно, Миссис Бакфетт!"

            julia "Миссис Бакфетт.
            Вы уже кушали недавно."

            "Вам подать снова?"

            menu:
                "Не надо, продолжай работу.":
                    julia "Конечно, Миссис Бакфетт."

                "Похвалить Юлию за вкусную еду." if juliaPraiseOnOccasion == True:
                    if juliaPunishedLow != True:
                        m "Ты готовишь довольно вкусно, Юлия."
                        julia "Спасибо, Миссис Бакфетт!"
                        call bitch(-5, "juliaPraiseOnOccasion") from _call_bitch_12
                    else:
                        mt "Не собираюсь я ее хвалить!"
                        "Хотела, но передумала!"
                        if juliaMonicaLied == True:
                            "Особенно после того пятна, которое она сама же и поставила!"
                            "И не стала убирать!!!"
                            "..."

            if juliaPunishedLow == True:
                julia "Миссис Бакфетт, спасибо что не заставили убирать меня это жуткое пятно!"
                "Я бы умерла, но не смогла оттереть его!"
                m "Радуйся пока я добрая.
                Если будешь себя хорошо вести, то тебе не придется убирать его."
                "В противном случае, ты понимаешь..."
                julia "Да, Миссис Бакфетт!
                Я буду делать все что Вы скажете!!!"
                "Только пожалуйста!!!"

            if juliaPunishedNone == True:
                julia "Миссис Бакфетт, спасибо что не заставили меня убирать это пятно."
                "Мне немного неудобно перед Вами."
                "Ведь это моя обязанность..."
                m "Ничего страшного, Юлия."
                "Я же не садист..."
                julia "Спасибо!!!"

            if juliaPunishedVoluntarily == True:
                julia "Миссис Бакфетт, я занимаюсь пятном в свободное время."
                "Но оно все еще есть."
                m "Я вижу, Юлия.
                Продолжай заниматься."
                julia "Спасибо, Миссис Бакфетт!"
    return


label floor1_monica_julia_revenge_interact_look:
    img 1029
    mt "А вот и Юлия.
    Она работает у меня гувернанткой."

    if juliaPunishedLow == True:
        img 1030
        mt "Она из бедной семьи.
        Старается работать, но немного туповата."
        img 1031
        if juliaMonicaLied == True:
            mt "Сделала мне пятно на ковре.
            Но, каким-то чудом избежала наказания."
            "Не знаю как это случилось, но это явно моя недоработка!"
        else:
            mt "Я сделала пятно на ковре.
            Юлия каким-то чудом избежала необходимости оттирать его."
            "Не знаю как это случилось, но это явно моя недоработка!"

    if juliaPunishedNone == True:
        img 1030
        mt "Я сделала пятно на ковре, но не заставила ее убирать его."
        "Все-равно ковер скоро менять."
        img 1031
        mt "Я считаю что она и так много работает, бедняжка."

    if juliaPunishedVoluntarily == True:
        img 1030
        mt "Я сделала пятно на ковре, но не заставила ее убирать его."
        img 1031
        mt "Однако Юлия сама вызвалась это сделать в свободное время."
        "Это стоит похвалы..."

    if juliaMonicaForgivenessAfterPunishment == True:
        mt "Я собиралась уволить из-за ковра..."
        mt "Но несмотря на все я простила ей это пятно...
        Пока..."
        "Я ведь не тиран, в конце концов!"
    return
