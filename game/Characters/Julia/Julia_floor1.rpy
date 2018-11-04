default juliaLocation = "floor1"
#default juliaLocation = "kitchen"
default juliaMonicaYell = False #Моника обращается с Юлией криком
default juliaPunished = False #жестко наказана, убирается на втором этаже каждый день
default juliaPunishedLow = False #наказана криком, но разрешено не убирать пятно
default juliaPunishedVoluntarily = False #мягко, разрешено убирать в свободное время
default juliaPunishedNone = False #пятно есть, но Юлию не наказали вообще никак
default juliaMonicaLied = False #Моника соврала что пятно поставила не она
default juliaMonicaForgivenessAfterPunishment = False #Моника простила Юлию после строгого наказания на 2-ом этаже

default juliaSeen = False
default juliaSeen_action = False

default juliaHasSexInPool = False

default juliaNeedToCheckStreet = False
default juliaMonicaRevengeQueued = False

label julia_interact(obj_name, obj_data):
    if scene_name == "floor1":
        if day == 1 and day_time == "evening":
            call julia_day1_evening(obj_name, obj_data)
            return
        if day == 2 and day_time == "day":
            call julia_day2_day(obj_name, obj_data)
            return
        if day == 2 and day_time == "evening":
            call julia_day2_evening(obj_name, obj_data)
            return
        if day == 3 and day_time == "day":
            call julia_day3_day(obj_name, obj_data)
            return


        if julia_monica_revenge_in_progress == True:
            jump floor2_julia_monica_revenge_julia_punish2
        if juliaSeen == False:
            if obj_data["action"] == "l":
                img 1028
                img 1029
                mt "А вот и Юлия.
                Она работает у меня гувернанткой."

                img 1030
                mt "Она из бедной семьи.
                Старается работать, но немного туповата."

                img 1031
                "Постоянно что-то путает и не туда кладет.
                Ее можно научить делать все как надо, но мне лень этим заниматься"

                img 1032
                "Я считаю что если человек пришел куда-то работать, то должен уже уметь это делать."

                "Юлии повезло что я пока добрая, но это ненадолго."

                "...."

                $ juliaSeen_action = True

            if obj_data["action"] == "t":
                if juliaSeen_action == False:

                    img 1028
                    img 1029
                    mt "А вот и Юлия.
                    Она работает у меня гувернанткой."

                    img 1030
                    mt "Она из бедной семьи.
                    Старается работать, но немного туповата."

                    img 1031
                    "Постоянно что-то путает и не туда кладет.
                    Ее можно научить делать все как надо, но мне лень этим заниматься"

                    img 1032
                    "Я считаю что если человек пришел куда-то работать, то должен уже уметь это делать."

                    "Юлии повезло что я пока добрая, но это ненадолго."

                    "...."

                    $ juliaSeen_action = True

                img 1032
                menu:
                    "Позвать Юлию грубо":
                        $ juliaMonicaYell = True
                        call bitch(5, "call_julia1") from _call_bitch_29
                        img 1033
                        m "Юлия!
                        Что ты там копаешься???"

                        "Быстро подойди ко мне!!!"

                        img 1034
                        "Я сказала БЫСТРО!!!"

                        sound highheels_run2
                        wc
                        img 1035
                        julia "Да, миссис Бакфетт?
                        Чем я могу Вам помочь?"

                        img 1036
                        m "Я не должна говорить тебе чем можно мне помочь.

                        Знаешь что должно быть вместо этого??"

                        julia "Что, миссис...?"

                        m "Вместо этого ты сама должна знать чем помочь, а не спрашивать!!!"

                        m "Ясно тебе?"

                        img 1037
                        julia "Да, миссис, я поняла."

                        julia "Я стараюсь."

                        m "Приготовь мне завтрак и сходи посмотри на улицу что там случилось."

                        img 1038
                        julia "Да, миссис, я все сделаю тот час."

                        m "Ну, и?
                        Что ты стоишь???"

                        img 1039
                        "БЫСТРО!!!"
                        sound highheels_run1
                        $ juliaLocation = "kitchen"
                        $ juliaSeen = True
                        call refresh_scene() from _call_refresh_scene_9
                        show screen notify (_("Юлия убежала на кухню."))
                        $ juliaNeedToCheckStreet = True

                        menu:
                            "Ехидный комментарий в адрес Юлии.":
                                call bitch(2, "call_julia1") from _call_bitch_30
                                img 1040
                                m "Глупое никчемное создание."

                                "Я наверное очень добрая раз терплю вокруг всех этих недалеких людей."

                                "Мне, наверное, надо какую-то награду за доброту."

                                "Типа как Мать Тереза."

                                img 1041
                                "Интересно, какую шляпку я бы одела если бы меня награждали..."

                                "Впрочем, я снова замечталась."

                                if bathTaken == False:
                                    "Надо скорее принять душ и покушать."
                                else:
                                    "Надо скорее покушать."
                                return
                            "Продолжить заниматься делами.":
                                return

                    "Позвать Юлию вежливо":
                        sound highheels_run1
                        $ juliaMonicaYell = False
                        call bitch(-5, "call_julia1") from _call_bitch_31
                        img 1032
                        m "Юлия!
                        Не могла-бы ты подойти ко мне?"

                        img 1038
                        julia "Да, миссис Бакфетт."

                        "Чем могу Вам помочь?"

                        menu:
                            "Спросить у Юлии что случилось на улице.":
                                img 1038
                                m "Юлия, ты не знаешь что был за шум на улице с утра?"

                                julia "Нет, Миссис Бакфетт, не знаю."

                                m "Юлия, могла-бы ты узнать что случилось?"

                                julia "Да, Миссик Бакфетт, конечно, я узнаю."

                                "Позвольте вначале подать Вам на стол?"

                                m "Конечно, Юлия, подай на стол, затем может пойти узнать."

                                julia "Конечно, Миссис Бакфетт.
                                Одну минуту.
                                Сейчас подам Вам."

                                sound highheels_run1
                                $ juliaLocation = "kitchen"
                                $ juliaSeen = True
                                call refresh_scene() from _call_refresh_scene_10
                                show screen notify (_("Юлия убежала на кухню."))
                                $ juliaNeedToCheckStreet = True

                            "Попросить подать еду.":
                                img 1038
                                m "Юлия, можешь подавать еду на стол."

                                julia "Конечно, Миссис Бакфетт.
                                Одну минуту.
                                Сейчас подам Вам."
                                sound highheels_run1
                                $ juliaLocation = "kitchen"
                                $ juliaSeen = True
                                call refresh_scene() from _call_refresh_scene_11
                                show screen notify (_("Юлия убежала на кухню."))

        if juliaSeen == True:
            call julia_interact3(obj_name, obj_data) from _call_julia_interact3

    if scene_name == "kitchen":
        call julia_interact2(obj_name, obj_data) from _call_julia_interact2

























#
