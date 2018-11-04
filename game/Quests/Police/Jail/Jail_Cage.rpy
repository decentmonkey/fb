default jailCageStatus = 0
default jailCageShowedBoobsForBobName = False
default jailCageBlackmailInProgress = False
default jailCageBlackmailStage = 0
default jailCageBlackmailEnded = False
default jailCageBlackmailBoobsShowed = False
default jailCageBlackmailAssShowed = False
default jailCageBlackmailMonicaSaidSheIsAWhore = False

label jail_cage:
    if jailCageShowedBoobsForBobName == True:
        sound prison_yell
        img 5113
        prisoner1 "Я же говорил?!"
        "Видели???"
        "Она показала их!"
        img 5112
        "Показала свои сиськи!!!"
        img 5101
        prisoner4 "Покажи нам их еще раз!"
        "Покажи!"
        prisoner3 "Шлюха!"
        img 5111
        prisoner1 "Еще раз! Покажи!"
        img 5100
        prisoner2 "Шлюха!"
        img 5305
        mt "О БОЖЕ!!!"
        return
    if jailBoobsForFoodShowed == True:
        if jailCageStatus == 0:
            sound prison_yell
            img 5113
            prisoner1 "Я же говорил?!"
            "Видели???"
            "Она показала их!"
            img 5112
            "Показала свои сиськи!!!"
            img 5101
            prisoner4 "Покажи нам их!"
            "Покажи!"
            prisoner3 "Шлюха!"
            img 5100
            prisoner2 "Шлюха!"
            img 5306
            mt "О БОЖЕ!!!"
            "Эти отбросы видели это..."
            img 5307
            "Но у меня не было выбора!"
            img 5308
            "Что же мне делать теперь???"
            "..."
            img 2315
            "Ничего, Моника!"
            "Скоро ты выйдешь отсюда!"
            "Выйдешь и позаботишься чтобы никто из этих отбросов не увидел белый свет и никому не рассказал!"
            img 5309
            "Это для тебя совсем нетрудно, Моника!"
            "А пока не обращай внимания на них."
            "Тебе ведь даже немного жаль их, правда?"
            img 5310
            "Жалкие людишки! Бесполезные!"
            "Никчемные!"

            if jailDay >= 5:
                img 5311
                mt "..."
                mt "Может быть спросить у них имя этого жирного ублюдка?"
                "Будет с них хоть какая-то польза!"
                menu:
                    "Спросить у них имя.":
                        pass
                    "Не спрашивать.":
                        return
                music Stealth_Groover
                img 5312
                m "Эй вы!"
                img 5110
                prisoner1 "???"
                img 5102
                prisoner5 "???"
                img 5313
                m "Да, вы!"
                "Как зовут этого жир..."
                img 5314
                mt "Черт! Он же может услышать!"
                img 5313
                m "Как зовут нашего надзирателя?"
#                sound prison_yell
                stop music fadeout 1.0
                music prison_yell_music
                img 5112
                prisoner1 "Ребята! Шлюха нас о чем-то спрашивает!"
                "Шлюхе нужна наша помощь!"
                img 5102
                prisoner5 "Да! Поможем ей!"
                img 5101
                prisoner3 "Да! Вгоним свои члены прямо в нее! Да!"
                "Поможем шлюхе!"
                img 5315
                mt "Сволочи!!! НЕНАВИЖУ!!!"
                img 5316
                mt "Моника! Терпение! Это самое большое испытание в твоей жизни!"
                "Справишься - и дальше будет проще!"
                img 5312
                m "Как зовут надзирателя?!?!?!"
                img 5112
                prisoner1 "Шлюхе нужна наша помощь!"
                img 5113
                "Что у шлюх требуют взамен помощи?"
                img 5102
                prisoner5 "Сиськи!"
                img 5100
                prisoner2 "Да! Сиськи!"
                img 5103
                prisoner6 "Сиськи! Сиськи!"
                "Покажи сиськи!"
                img 5099
                prisoner1 "Детка! Покажи сиськи! И мы тебе скажем!"
                img 5101
                prisoner3 "Давай! Ты все-равно их показываешь налево-направо!"
                "Мы же видим!"
                img 5317
                mt "О БОЖЕ!!!"
                "У меня есть выбор."
                "Жуткий выбор, Моника!"
                img 5318
                mt "О БОЖЕ!!!"
                "Показать им свою грудь. Один раз."
                img 5319
                "Или делать это каждый день тому жирному ублюдку."
                "Что же мне делать?"
                menu:
                    "Показать грудь в обмен на имя надзирателя.":
                        img 5321
                        m "Только один раз!"
                        img 5322
                        "И имя вперед!"
#                        sound prison_yell
                        img 5102
                        prisoner5 "Сиськи!"
                        img 5103
                        prisoner6 "Сиськи! Сиськи!"
                        img 5114
                        prisoner1 "Нет, шлюха! Сначала сиськи! Голые!"
                        "Мы шлюхам не верим, да ребята?"
                        img 5101
                        prisoner3 "Не верим!"
                        prisoner4 "Мы не верим шлюхам!"
                        img 5102
                        prisoner5 "Сиськи!"
                        img 5103
                        prisoner6 "Сиськи! Сиськи!"
                        menu:
                            "Показать грудь в обмен на имя надзирателя.":
                                music prison_yell_music
                                img 5108
                                prisoner5 "Сиськи!"
                                prisoner6 "Сиськи! Сиськи!"
                                #сиськи выглядывают из-за решетки
                                img black_screen
                                with fadelong
                                img 5625
                                with fadelong
                                prisoner5 "Сиськи!"
                                prisoner6 "Сиськи! Сиськи!"
                                music Loved_up2
                                img 5323
                                with Dissolve(0.5)
                                w
                                img 5324
                                w
                                img 5325
                                w
                                sound prison_yell
                                img 5106
                                prisoner2 "Да! Сиськи!"
                                img 5326
                                w
                                img 5327
                                w
                                img 5108
                                sound prison_yell
                                prisoner5 "Сиськи!"
                                prisoner6 "Сиськи! Сиськи!"
                                img 5328
                                w
                                img 5329
                                w
                                img 5108
                                sound prison_yell
                                prisoner6 "Сиськи! Сиськи!"
                                img 5330
                                w
                                img 5331
                                w
                                img 5332
                                w
                                #еще картинки с сиськами
                                music prison_yell_music
                                img 5113
                                prisoner1 "Хорошо, шлюшка!"
                                "Его имя Боб!"
                                "Если бы ты не была тупой шлюхой, то ты бы запомнила это имя тогда когда тебя привели сюда!"
                                "Ха-ха"
                                music Jail_Clock
                                img 5333
                                with fadelong
                                mt "Сволочи!!!"
                                "(хмык)"
                                $ jailCageShowedBoobsForBobName = True
                                $ monicaKnowOverseerName = True
                                return

                            "Не показывать.":
                                music Pyro_Flow
                                img 5320
                                m "Я не собираюсь вам ничего показывать! Я не шлюха!"
                                sound prison_yell
                                img 5108
                                prisoner5 "Сиськи!"
                                prisoner6 "Сиськи! Сиськи!"
                                img 5113
                                prisoner1 "Детка! Подумай! У тебя много времени впереди!"
                                "Хе-хе!"
                                music Jail_Clock
                                return


                    "Не показывать.":
                        music Pyro_Flow
                        img 5320
                        m "Я не собираюсь вам ничего показывать! Я не шлюха!"
                        sound prison_yell
                        img 5108
                        prisoner5 "Сиськи!"
                        prisoner6 "Сиськи! Сиськи!"
                        img 5113
                        prisoner1 "Детка! Подумай! У тебя много времени впереди!"
                        "Хе-хе!"
                        music Jail_Clock
                        return


            return
    if jailCageStatus == 0:
        sound prison_yell
        img 5099
        with fadelong
        prisoner1 "Смотрите какую сучку к нам подселили!"
        img 5100
        prisoner2 "Да! Посмотрите на нее!"
        img 5102
        prisoner5 "Горячая штучка!"
        img 5101
        prisoner3 "Покажи сиськи, девочка!!!"
        prisoner4 "Она не покажет тебе их, Пит!"
        "Смотри как она стесняется!"
        img 5112
        prisoner1 "Она шлюха, вот увидите!"
        "Она нам еще все покажет и всех обслужит!"
        img 5113
        "Ставлю свой доллар!"
        img 5299
        mt "О БОЖЕ!!!"
        "ЧТО ЗА ЖИВОТНЫЕ!!!"
        "КАКАЯ МЕРЗОСТЬ!!!"
        img 5300
        menu:
            "Послать их...":
                music Pyro_Flow
                img 5302
                m "Вы перепутали адрес, мальчики!"
                "Вы знаете с кем вообще разговариваете!"
                img 5303
                "Сидите там и не высовывайтесь, а то вам будет хуже!!!"
                img 5101
                prisoner4 "Смотри какой нее ротик!"
                "Может ты и прав, она точно шлюха!"
                music Jail_Clock
                img 5304
                m "Фу! Что за мерзость!!!"
            "Игнорировать...":
                img 5301
                w
                pass
    return


label jail_cage_blackmail_day:
    if jailCageBlackmailEnded == True:
        # заключенные молчат...
        img 5455
        with fade
        w
        img 5456
        w
        img 5457
        mt "То-то же..."
        "Так гораздо спокойнее"
    else:
        sound prison_yell
        img 5099
        prisoner1 "Шлюха! До вечера!"
        "Хорошая шлюха!"
        "Мы ждем тебя!"
        "Сегодня вечером!!!"
        img 5458
        mt "Вот ублюдки!!!"
        "..."
        "Откуда только они знают день здесь или вечер..."
        "Скорее всего они просто сумасшедшие..."
        img 5459
        "О БОЖЕ!!!"
        "Моника, тебе надо что-то делать со всем этим!!!"
        "Мне не лезет в голову все что сейчас происходит!"
        "Это как сон!"
        "Страшный сон!"
    return
label jail_cage_blackmail:
    $ jailCageBlackmailInProgress = True
    if jailCageBlackmailStage == 0:
        music Pyro_Flow
        img 5334
        with fadelong
        m "Что вам надо???"
        "Как вы смеете мешать мне спать???"
        img 5335
        "Вы-никто!!! Запомните это!!!"
        "Вы даже не представляете себе КТО Я!!!"
        img 5099
        prisoner1 "Эй! Шлюха!"
        img 5336
        m "Я не шлюха!!!"
        img 5112
        if jailBoobsForFoodShowed == True:
            prisoner1 "Мы видели как ты показывала сиськи надзирателю!!!"
        if jailCageShowedBoobsForBobName == True:
            prisoner1 "Ты показывала сиськи нам!"
        if jailBoobsForFoodShowed == True and jailCageShowedBoobsForBobName == True:
            prisoner1 "Ты показываешь свои сиськи направо и налево!"
        if jailBoobsForFoodShowed == True or jailCageShowedBoobsForBobName == True:
            prisoner1 "Так что ты шлюха!"
        else:
            prisoner1 "Мы знаем что ты шлюха! Просто ты еще не доказала это!"
        img 5100
        prisoner2 "Шлюха!"
        img 5103
        prisoner6 "Шлюха!"
        img 5101
        prisoner4 "Шлюха!"
        prisoner3 "Шлюха!"
        img 5337
        m "Что вам от меня надо?!?!"
        img 5113
        prisoner1 "Эй! Детка!"
        "Мы слышали твой разговор с надзирателем!"
        "Решила покинуть нас? Да?"
        img 5338
        m "Что вы слышали? Вам показалось!"
        music Power_Bots_Loop
        img 5339
        with fade
        mt "ЧЕРТ!!! ЭТО ПЛОХО!!!"
        img 5105
        prisoner1 "Детка, тебе придется взять нас с собой!"
        "ВСЕХ!!!"
        img 5106
        prisoner2 "Да!"
        img 5108
        prisoner6 "Да!"
        img 5107
        prisoner4 "С собой!"
        prisoner3 "Да!"
        img 5112
        prisoner1 "Или у тебя есть еще один вариант!"
        "Чтобы мы молчали!"
        img 5340
        m "Какой вариант?"
        img 5341
        mt "Мерзавцы! Ненавижу!!!"
        img 5114
        prisoner1 "Ты будешь показывать нам все что мы захотим!"
        "Докажи что ты шлюха! Хорошая шлюха!"
        "Мы любим хороших шлюх, да ребята?"
        img 5100
        prisoner2 "Да!"
        img 5103
        prisoner6 "Да!"
        img 5101
        prisoner4 "Хорошая шлюха!"
        prisoner3 "Да!"
        img 5342
        m "Один день?"
        img 5112
        prisoner1 "Каждый день!"
        "Нам нужна шлюха каждый день! Не один день! Каждый день!"
        "Да, ребята?"
        img 5100
        prisoner2 "Да!"
        img 5103
        prisoner6 "Да!"
        img 5101
        prisoner4 "Каждый день!"
        prisoner3 "Да!"
        img 5343
        m "Я не собираюсь ничего вам показывать!!!"
        img 5344
        "Вы мерзавцы! И даже не знаете с кем разговариваете!"
        "Я уничтожу вас!!!"
        img 5115
        prisoner1 "Если ты не покажешь нам сиськи прямо сейчас же, то мы все расскажем мистеру Маркусу!!!"
        "Да!"
        "Я уверен, он увеличит нам за это паёк!"
        img 5100
        prisoner2 "Да!"
        img 5103
        prisoner6 "Да!"
        img 5101
        prisoner4 "Увеличит!"
        prisoner3 "Да!"
        img 5114
        prisoner1 "У тебя минута, шлюха!"
        "Докажи что ты хорошая шлюха!"
        "Тогда мы будем молчать!"
        "У тебя минута!"
        img 5345
        m "..."
        img 5346
        mt "О БОЖЕ!!!"
        "ЧТО МНЕ ДЕЛАТЬ???"
        "У МЕНЯ ПОЧТИ ВСЕ ПОЛУЧИЛОСЬ!!!"
        "И ТЕПЕРЬ ВОТ ЭТО!!!"
        img 5347
        mt "О БОЖЕ!!!"
        "КАК МНЕ ВЫЖИТЬ???"
        "Если Маркус узнает, то мне конец!"
        "Да даже если этот жирный ублюдок узнает о том что заключенные в курсе, то не станет мне помогать!"
        "Он жалкое ничтожество, трусливое!!!"
        img 5348
        "Как ты поступишь, Моника?"
        menu:
            "Я знаю как заткнуть рот этим мерзавцам...":
                call jail_cage_blackmail_stop()
                $ jailCageBlackmailEnded = True
                $ jailDaySceneStage = 5
                call refresh_scene_fade()
                return
            "У меня нет выбора...":
                $ jailCageBlackmailBoobsShowed = True
                img 5349
                with fadelong
                m "..."
                "...."
                "....."
                music Loved_up2
                # вылазят сиськи
                img 5350
                with Dissolve(0.5)
                w
                img 5351
                w
                img 5352
                w
                sound prison_yell
                img 5108
                prisoner5 "Сиськи!"
                prisoner6 "Сиськи! Сиськи!"
                img 5353
                w
                img 5354
                w
                img 5106
                sound prison_yell
                prisoner2 "Да! Сиськи!"
                img 5355
                w
                img 5356
                w
                img 5357
                w
                sound prison_yell
                img 5107
                prisoner3 "Сиськи!"
                img 5109
                prisoner4 "Сиськи! Сиськи!"
                img 5358
                w
                img 5359
                w
                img 5360
                w
                img 5361
                w
                img 5362
                w
                img 5099
                prisoner1 "Ребята, все кончили?"
                img 5114
                prisoner1 "Хорошая шлюха! Завтра в это же время!"
                music Jail_Clock
                img 5363
                with fadelong
                mt "О БОЖЕ!!!"
                img 5364
                with fade
                "КАКАЯ МЕРЗОСТЬ!!!"
                $ jailCageBlackmailStage = 1
                $ jailDaySceneStage = 5
                call refresh_scene_fade()
                return
    if jailCageBlackmailStage == 1:

        music Power_Bots_Loop
        img 5365
        with fadelong
        m "Что вам надо снова???"
        img 5366
        prisoner1 "Шлюха! Что значит что нам надо?"
        img 5115
        "Нам нужны твои сиськи, ты забыла?!"
        img 5102
        prisoner5 "Сиськи!"
        img 5103
        prisoner6 "Сиськи! Сиськи!"
        img 5100
        prisoner2 "Да! Сиськи!"
        img 5367
        mt "О БОЖЕ!!!"
        img 5114
        prisoner1 "Или нам позвать мистера Маркуса?"
        prisoner1 "А, шлюха?"
        prisoner1 "Показывай нам свои булочки и поиграй ими как следует!"
        img 5102
        prisoner5 "Сиськи!"
        img 5103
        prisoner6 "Сиськи! Сиськи!"
        img 5100
        prisoner2 "Да! Сиськи!"
        img 5102
        prisoner5 "Да!"
        img 5103
        prisoner6 "Поиграй!"
        img 5368
        menu:
            "Я знаю как заткнуть рот этим мерзавцам...":
                call jail_cage_blackmail_stop()
                $ jailCageBlackmailEnded = True
                $ jailDaySceneStage = 5
                call refresh_scene_fade()
                return
            "У меня нет выбора...":
                music prison_yell_music
                img 5369
                with fadelong
                m "..."
                "...."
                "....."
                img 5370
                music Loved_up2
                with Dissolve(0.5)
                w
                # вылазят сиськи и Моника ими играет
                img 5108
                prisoner5 "Сиськи!"
                prisoner6 "Сиськи! Сиськи!"
                img 5371
                w
                img 5106
                prisoner2 "Да! Сиськи!"
                img 5372
                w
                scene black
                image videoPolice_Jail_Monica_Tits_1_1 = Movie(play="video/Police_Jail_Monica_Tits_1_1.mp4", fps=30)
                show videoPolice_Jail_Monica_Tits_1_1
                wclean
                img 5373
                w
                #video
                img 5108
                prisoner5 "Сиськи!"
                prisoner6 "Сиськи! Сиськи!"
                scene black
                image videoPolice_Jail_Monica_Tits_1_2 = Movie(play="video/Police_Jail_Monica_Tits_1_2.mp4", fps=30)
                show videoPolice_Jail_Monica_Tits_1_2
                wclean
                img 5374
                w
                scene black
                image videoPolice_Jail_Monica_Tits_1_3 = Movie(play="video/Police_Jail_Monica_Tits_1_3.mp4", fps=30)
                show videoPolice_Jail_Monica_Tits_1_3
                wclean
                img 5374
                w
                scene black
                image videoPolice_Jail_Monica_Tits_1_4 = Movie(play="video/Police_Jail_Monica_Tits_1_4.mp4", fps=30)
                show videoPolice_Jail_Monica_Tits_1_4
                wclean
                img 5113
                with fadelong
                prisoner1 "Ребята, все кончили?"
                img 5114
                prisoner1 "Хорошая шлюха! Завтра в это же время!"
                music Jail_Clock
                img 5376
                mt "О БОЖЕ!!!"
                img 5377
                "КАКАЯ МЕРЗОСТЬ!!!"
                $ jailCageBlackmailStage = 2
                $ jailDaySceneStage = 5
                call refresh_scene_fade()
                return

    if jailCageBlackmailStage == 2:
        music Power_Bots_Loop
        img 5378
        m "Что вам надо снова???"
        img 5115
        prisoner1 "Шлюха, ты знаешь что нам надо!"
        "Давай быстрее, не испытывай наше терпение!!!"
        img 5379
        menu:
            "Я знаю как заткнуть рот этим мерзавцам...":
                call jail_cage_blackmail_stop()
                $ jailCageBlackmailEnded = True
                $ jailDaySceneStage = 3
                call refresh_scene_fade()
                return
            "У меня нет выбора...":
                music prison_yell_music
                img 5369
                with fadelong
                m "..."
                "..."
                "..."
                # вылазят сиськи
                music Loved_up2
                img 5370
                with Dissolve(0.5)
                w
                music Power_Bots_Loop
                img 5114
                prisoner1 "Нет, мы уже их видели!"
                prisoner1 "Шлюха! Никому уже не нужны твои сиськи!"
                "Нам нужно больше!"
                img 5100
                prisoner2 "Да!"
                img 5103
                prisoner6 "Да!"
                img 5101
                prisoner4 "Надо больше!"
                prisoner3 "Да!"
                img 5380
                m "Что вам надо, ублюдки??!?!"
                img 5113
                prisoner1 "Нам нужна твоя попка!"
                img 5100
                prisoner2 "Да!"
                img 5103
                prisoner6 "Да!"
                img 5101
                prisoner4 "Ее попка!"
                prisoner3 "Да!"
                img 5381
                m "Я не буду вам показывать ничего такого!"
                img 5382
                "Это уже слишком!!!"
                img 5114
                prisoner1 "Ты шлюха! Ты хорошая шлюха!"
                "Ты должна слушаться нас!"
                "Плохая шлюха будет наказана!"
                "Плохая шлюха хочет убежать отсюда!"
                img 5100
                prisoner2 "Да!"
                img 5103
                prisoner6 "Да!"
                img 5101
                prisoner4 "Плохая шлюха!"
                prisoner3 "Да!"
                img 5383
                mt "О БОЖЕ!!!"
                "Это заходит слишком далеко!"
                img 5384
                "Я хотела просто потянуть время, но они требуют невозможного!"
                "Я хочу отсюда выбраться, но моя честь дороже всего для меня!"
                img 5385
                "Я ЛЕДИ, а не какая-то потаскуха!"
                img 5386
                menu:
                    "Я не буду вам ничего показывать! Ни за что!!!":
                        music Pyro_Flow
                        img 5387
                        m "Делайте что хотите!"
                        "Это для меня уже слишком!"
                        music Jail_Clock
                        img 5388
                        mt "О БОЖЕ!!!"
                        "КАКАЯ МЕРЗОСТЬ!!!"
                        $ jailCageBlackmailStage = 3
                        $ jailDaySceneStage = 3
                        call refresh_scene_fade()

                    "Может быть как-то потянуть время?":
                        music Hidden_Agenda
                        $ jailCageBlackmailAssShowed = True
                        img 5389
                        mt "Я вот-вот выберусь отсюда!"
                        "Мне надо совсем-совсем еще немного времени!"
                        img 5390
                        "Нельзя вот так все испортить, когда я уже почти у цели!"
                        img black_screen
                        with Dissolve(1)
                        img 5391
                        m "Эй вы!"
                        img 5392
                        "Хорошо! Я покажу вам!"
                        img 5393
                        "Но я не буду раздеваться сейчас!"
                        img 5394
                        "Я буду делать это постепенно, каждый день!"
                        img 5393
                        "Вы ведь хотите растянуть удовольствие!"
                        img 5112
                        prisoner1 "Да! Хотим!"
                        img 5111
                        "Хорошо, шлюха! Вставай скорее к нам задом! Нагибайся! Скорее!"
                        img 5395
                        mt "УБЛЮДКИ!!!"
                        img 5396
                        w
                        music Loved_up2
                        img black_screen
                        with Dissolve(1)
                        img 5397
                        with fadelong
                        w
                        img 5398
                        w
                        img 5399
                        w
                        img 5400
                        w
                        img 5401
                        w
                        img 5402
                        w
                        img 5403
                        w
                        "НЕНАВИЖУ!!!"
                        img 5404
                        w
                        img 5405
                        w
                        img 5406
                        w
                        img 5407
                        w
                        img 5408
                        "НЕНАВИЖУУУУУ!!!"
                        # моника встает задом
                        img 5115
                        prisoner1 "Ниже! Наклонись ниже!"
                        "Неопытная шлюха!"
                        # моника наклоняется сильнее
                        img 5409
                        with fadelong
                        w
                        img 5410
                        w
                        img 5411
                        w
                        img 5412
                        mt "ТВАРИ!!!"
                        img 5413
                        w
                        img 5414
                        w
                        img 5415
                        w
                        img 5416
                        "УБЛЮДКИ!!!"
                        img 5417
                        w
                        img 5418
                        w
                        img 5419
                        "ВАМ ВСЕМ КОНЕЦ!!!"
                        img 5420
                        w
                        img 5421
                        "КЛЯНУСЬ!!!"
                        img 5105
                        prisoner1 "Давай! Больше действий! Повиляй бедрами, шлюха!"
                        "Давай!"
                        img 5422
                        w
                        scene black
                        image videoPolice_Jail_Monica_Butt_1_1 = Movie(play="video/Police_Jail_Monica_Butt_1_1.mp4", fps=30)
                        show videoPolice_Jail_Monica_Butt_1_1
                        wclean
                        scene black
                        image videoPolice_Jail_Monica_Butt_1_2 = Movie(play="video/Police_Jail_Monica_Butt_1_2.mp4", fps=30)
                        show videoPolice_Jail_Monica_Butt_1_2
                        wclean
                        scene black
                        image videoPolice_Jail_Monica_Butt_1_3 = Movie(play="video/Police_Jail_Monica_Butt_1_3.mp4", fps=30)
                        show videoPolice_Jail_Monica_Butt_1_3
                        wclean
                        scene black
                        image videoPolice_Jail_Monica_Butt_1_4 = Movie(play="video/Police_Jail_Monica_Butt_1_4.mp4", fps=30)
                        show videoPolice_Jail_Monica_Butt_1_4
                        wclean
#                        scene black
#                        image videoPolice_Jail_Monica_Butt_1_5 = Movie(play="video/Police_Jail_Monica_Butt_1_5.mp4", fps=30)
#                        show videoPolice_Jail_Monica_Butt_1_5
#                        wclean
                        scene black
                        image videoPolice_Jail_Monica_Butt_1_6 = Movie(play="video/Police_Jail_Monica_Butt_1_6.mp4", fps=30)
                        show videoPolice_Jail_Monica_Butt_1_6
                        wclean
                        scene black
                        image videoPolice_Jail_Monica_Butt_1_7 = Movie(play="video/Police_Jail_Monica_Butt_1_7.mp4", fps=30)
                        show videoPolice_Jail_Monica_Butt_1_7
                        wclean
                        scene black
                        image videoPolice_Jail_Monica_Butt_1_8 = Movie(play="video/Police_Jail_Monica_Butt_1_8.mp4", fps=30)
                        show videoPolice_Jail_Monica_Butt_1_8
                        wclean
                        scene black
                        image videoPolice_Jail_Monica_Butt_1_9 = Movie(play="video/Police_Jail_Monica_Butt_1_9.mp4", fps=30)
                        show videoPolice_Jail_Monica_Butt_1_9
                        wclean
                        scene black
                        image videoPolice_Jail_Monica_Butt_1_10 = Movie(play="video/Police_Jail_Monica_Butt_1_10.mp4", fps=30)
                        show videoPolice_Jail_Monica_Butt_1_10
                        wclean

                        # моника морщится и виляет бедрами
                        img 5423
                        w

                        music Power_Bots_Loop
                        img 5105
                        prisoner1 "Да! Вот так!"
                        "И последнее условие!"
                        img 5424
                        m "Какие еще условия??? Вам что, мало???"
                        img 5115
                        prisoner1 "Мы разрешили тебе раздеваться медленно, шлюха!"
                        "Поэтому мы здесь ставим условия! А ты не пререкаешься!"
                        img 5425
                        m "Какое условие?"
                        img 5112
                        prisoner1 "Скажи что ты хорошая шлюха!"
                        img 5426
                        m "ЧТО СКАЗАТЬ?!?!"
                        img 5114
                        prisoner1 "Скажи что ты хорошая шлюха!"
                        img 5427
                        m "Я НЕ БУДУ ЭТОГО ГОВОРИТЬ!!!"
                        img 5115
                        prisoner1 "Скажи или ты станешь плохой шлюхой! А ты знаешь что грозит плохой шлюхе здесь!!!"
                        img 5428
                        mt "О БОЖЕ!!!"
                        "КАК УНИЗИТЕЛЬНО!"
                        "НЕУЖЕЛИ Я ЭТО СДЕЛАЮ???"
                        menu:
                            "Я НЕ СДЕЛАЮ ЭТО НИ ЗА ЧТО!!!":
                                # моника встает
                                music Pyro_Flow
                                img 5439
                                m "Я никогда этого не скажу!"
                                "Я - леди!"
                                img 5440
                                "А вы - ублюдки!"
                                music Jail_Clock

                            "У меня нет выбора...":
                                # моника почти плачет
                                img 5429
                                with fadelong
                                w
                                img 5430
                                with fade
                                m "Я хорошая шлюха..."
                                img 5115
                                prisoner1 "Громче! Мы не слышим!"
                                img 5431
                                w
                                img 5432
                                w
                                img 5433
                                w
                                img 5434
                                w
                                img 5435
                                m "Я хорошая шлюха!"
                                img 5115
                                prisoner1 "Громче! Громко и ясно!"
                                img 5436
                                m "Я ХОРОШАЯ ШЛЮХА!!!"
                                $ jailCageBlackmailMonicaSaidSheIsAWhore = True
                                img 5099
                                prisoner1 "Хорошая шлюха! Завтра в это же время!"
                                # моника плачет в углу
                                img black_screen
                                with Dissolve(1)
                                img 5437
                                with fadelong
                                mt "Мне надо скорее убираться отсюда..."
                                img 5438
                                "Я не знаю как мне жить с тем что я сейчас сделала..."
                                "Но больше моя гордость не выдержит - это точно..."


                $ jailCageBlackmailStage = 3
                $ jailDaySceneStage = 3
                call refresh_scene_fade()
                return
    return

label jail_cage_blackmail_stop:
    music Pyro_Flow
    img 5441
    with fadelong
    m "Знаете что?"
    "Вы что-то расшумелись сегодня и мешаете мне спать!"
    "Мне без разницы что вы там напридумывали себе!"
    img 5442
    "Вы гниете тут заживо и стали сходить с ума, похоже!"
    "Но я вам скажу одну вещь!"
    img 5443
    "Если вы с этой же минуты не заткнетесь и пророните хоть один звук..."
    "То я скажу надзирателю что вы шумите, когда его нет!"
    img 5444
    "И особенно шумишь ты, жирдяй!"
    img 5445
    prisoner1 "(сглатывает)"
    img 5446
    m "Не знаю почему вы так боитесь шуметь при нем."
    "Но я предупреждаю вас!"
    img 5447
    "Еще хоть один звук и я все ему расскажу!"
    "И не сомневайтесь что он мне поверит!"
    img 5448
    "ЯСНО ВАМ?!?!"
    img 5449
    prisoner1 "Все... все... Не кипятись!"
    "Мы все поняли, мы больше не шумим!"
    "Не надо ему говорить про это!"
    music Jail_Clock
    img 5450
    m "То-то же!!!"
    img 5451
    mt "..."
    "Как я их, а?"
    img 5452
    "Моника, ты умеешь поставить на место зарвавшихся мерзавцев!"
    "Ты молодец!"
    img 5453
    "Интересно, почему они так боятся шуметь при этом жирном слизняке?"
    img 5454
    "Но это и не важно!"
    "Меня это никак не касается!"
    return
