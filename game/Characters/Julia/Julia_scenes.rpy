default juliaBasementWarningActive = False

default juliaBasementSceneStage = 0
default juliaBasementSexLiked = False

label julia_scene_basement1:
    call textonblack(_("ТЕМ ВРЕМЕНЕМ...")) from _call_textonblack_1
    img black_screen
    with Dissolve(1)
    #juliaNeedToCheckStreet
    #juliaHasSexInPool
#    $ scene_transition = "Fade"
#    call refresh_scene()
#    return
    music Groove2_85

    if juliaNeedToCheckStreet == True:
        img 4001
        julia "Мистер Фрэд!
        Наконец-то я нашла Вас!"
        img 4002
        "Что вы здесь делаете?
        Вы же должны быть на улице, ждать Миссис Бакфетт!"

        img 4003
        fred "Юлия, ты знаешь, я профессионал.
        Я всегда буду вовремя."
    else:
        img 4004
        julia "Мистер Фрэд!
        Что вы здесь делаете?"
        img 4003
        fred "Привет, Юлия...
        А что ты здесь делаешь?"
        img 4005
        julia "Я пришла чтобы заняться вещами Миссис Бакфетт.
        Я иду в прачечную."

    img 4006
    fred "Юлия...
    Ты помнишь про условия сделки?"

    img 4007
    julia "Ккккакой сделки...
    Ммииситер Фред..."

    img 4008
    fred "О сделке, которую мы заключили, когда я устроил вас на работу сюда."
    "Это ведь я порекомендовал вас Миссис Бакфетт.
    Вы бы никогда не попали сюда."
    "Ведь у вас нет хорошоего резюме и..."

    music Hidden_Agenda
    img 4009
    julia "Мистер Фред... Вы про это..."

    img 4010
    fred "Да, Юлия.
    И я пришел сюда получить то о чем мы договорились тогда."

    img 4011
    julia "Мистер Фред, я была в таком состоянии..."
    "Мне так нужна была эта работа...
    Я была готова на все, лишь бы попасть сюда."
    img 4012
    "И я согласилась на то что вы предложили, но...
    если честно, я думала что это какая-то шутка."
    img 4013
    "Ведь вы не будете требовать этого от меня, правда?"

    img 4014
    fred "Юлия, я устроил вас сюда, потому что вы представились как профессионал."
    "У вас нет резюме и я поверил вам на слово. Я поверил вам что вы профессионал."

    img 4015
    "Несоблюдение сделки - это непрофессионально."
    "Миссис Бакфетт не нужны непрофессионалы на работе!"

    img 4016
    julia "Мистер Фред, но ведь Миссис Бакфетт не в курсе этого!
    А если она узнает?"
    img 4017
    fred "Миссис Бакфетт вообще нет дела до этого!"
    "Она не вдается в проблемы таких как вы, Юлия.
    Ей достаточно мнения профессионала о вас, такого как я."

    music Power_Bots_loop
    img 4018
    "И этого хватит чтобы вас уволить.
    Вы ведь этого хотите?"

    img 4019
    w
    img 4018
    w
    img 4020
    julia "Мистер Фред, нет!
    Пожалуйста!"
    img 4021
    "Для меня потеря этой работы - это как конец света!!"

    img 4022
    fred "Я рад, Юлия, что ты понимаешь это."

    music Hidden_Agenda
    img 4023
    julia "Что мне надо сделать, Мистер Фред?"

    img 4024
    fred "Снимай одежду и иди ко мне..."

    img 4025
    menu:
        "Подчиниться Мистеру Фреду, у меня нет выхода.":
            img 4029
            julia "Хорошо, Мистер Фред."
            img 4030
            julia "Хмык"

            fred "..."
            fred "Ну?"
            img 4031
            music Groove2_85
            with fadelong
            sound snd_fabric1
            w
            img 4033
            jump julia_scene_basement1_1

        "Отказать ему, он требует невозможного.":
            music Groove2_85
            img 4026
            julia "Мистер Фред!"
            img 4027
            "Вы требуете невозможного, мне надо подумать."
#            julia "Мистер Фред, вы требуете невозможного, мне надо подумать."

            img 4028
            fred "Думайте, Юлия, у вас есть немного времени."
            "Но потом не жалуйтесь на проблемы, которые у вас могут возникнуть."
            "А сейчас идемте со мной, мне надо кое-что показать вам."
            sound highheels_run1
    $ scene_transition = "Fade"
    $ autorun_to_object("bedroom2", "julia_scene_monica_thinking1")
    music casualMusic
    call refresh_scene() from _call_refresh_scene_24
    return


label julia_scene_basement1_1:
    $ juliaBasementSceneStage = 1
    $ juliaBasementWarningActive = True
    $ juliaHasSexInPool = True
    img 4034
    w
    julia "Что дальше, Мистер Фред?"

    img 4033
    sound snd_fabric1
    fred "Дальше?"

    img 4035
    fred "Вот что дальше!"
    img 4036
    sound snd_julia_scream1
    julia "АХХХХХ!!"
    img 4037
    julia "О БОЖЕ!!!"
    img 4036
    fred "Садись на колени и возьми мой член в ротик."
    menu:
        "У меня нет выхода...":
            jump julia_scene_basement1_2
        "Я не буду делать этого! (убежать)":
            img 4038
            julia "Я не буду этого делать!"
            sound highheels_run1
            $ juliaBasementWarningActive = False
            $ scene_transition = "Fade"
            $ autorun_to_object("bedroom2", "julia_scene_monica_thinking1")
            music casualMusic
            call refresh_scene()
            return

    #секс в бассейне в подвале
label julia_scene_basement1_2:
    $ juliaBasementSceneStage = 2
    img 4039
    with fadelong
    w
    img 4040
    julia "Какой он огромный..."
    img 4041
    julia "Мистер Фред!
    Я не могу его взять его, он слишком большой... наверное..."
    fred "Юлия!
    Не испытывай моего терпения!
    Быстро возьми его, иначе наша сделка разорвана!"
    sound snd_gulp
    julia "..."
    "Хорошо, Мистер Фред..."
    img 4042
    with fade
#    sound snd_gag10
    w
    stop music fadeout 1.0
#    $ renpy.movie_cutscene("video/Basement_Fred_Julia_Blowjob1.mp4", loops=-1)
#    $ renpy.scene()
    scene black
#    show black_screen
    image videoBasement_Fred_Julia_Blowjob1 = Movie(play="video/Basement_Fred_Julia_Blowjob1.mp4", fps=30)
#    pause 0.5
    show videoBasement_Fred_Julia_Blowjob1
#    hide black_screen
    wclean
#    sound snd_gag9
    img 4043
    with fade
    w
    img 4044
    music Groove2_85
    julia "Мммхмммпфффф...."
    fred "Продолжай, Юлия..."
    stop music fadeout 1.0
    scene black
    image videoBasement_Fred_Julia_Blowjob2 = Movie(play="video/Basement_Fred_Julia_Blowjob2.mp4", fps=30)
    show videoBasement_Fred_Julia_Blowjob2
    wclean
#    $ renpy.movie_cutscene("video/Basement_Fred_Julia_Blowjob2.mp4", loops=-1)
#    sound snd_gag9
    img 4045
    with fade
    music Groove2_85
    w
    img 4046
    julia "Мммхмммпфффф...."
    img 4047
    fred "Продолжай..."
    stop music fadeout 1.0
    scene black
    image videoBasement_Fred_Julia_Blowjob3 = Movie(play="video/Basement_Fred_Julia_Blowjob3.mp4", fps=30)
    show videoBasement_Fred_Julia_Blowjob3
    wclean
#    $ renpy.movie_cutscene("video/Basement_Fred_Julia_Blowjob3.mp4", loops=-1)
    img 4048
    with fade
    music Groove2_85
    w
    img 4049
    fred "Продолжай..."
    img 4050
    w
    stop music fadeout 1.0
    scene black
    image videoBasement_Fred_Julia_Blowjob5 = Movie(play="video/Basement_Fred_Julia_Blowjob5.mp4", fps=30)
    show videoBasement_Fred_Julia_Blowjob5
    wclean
    img 4051
    w
    stop music fadeout 1.0
    scene black
    image videoBasement_Fred_Julia_Blowjob4 = Movie(play="video/Basement_Fred_Julia_Blowjob4.mp4", fps=30)
    show videoBasement_Fred_Julia_Blowjob4
    wclean
#    $ renpy.movie_cutscene("video/Basement_Fred_Julia_Blowjob4.mp4", loops=-1)
#    sound snd_fred_argh
    img 4052
    music Groove2_85
    fred "ААААРГХХХХ!!!"
    julia "О БОЖЕ!!!"
    img 4053
    fred "ХА-ХААА!!!"
#    sound snd_fred_argh
    img 4054
    fred "ААААРГХХХХ!!!"
    img 4055
    with fade
    fred "Не переживай, Юлия..."
    img 4056
    fred "Это полезно для кожи лица!"
    img 4057
    with fade
    fred "Можешь вставать, Юлия."
    img 4058
    fred "Как ты себя чувствуешь?"
    img 4059
    menu:
        "Я даже не знаю, Мистер Фред. Вы сделали со мной такие вещи...":
            img 4060
            julia "Я даже не знаю, Мистер Фред. Вы сделали со мной такие вещи..."
            "Я могу идти?"
            jump julia_scene_basement1_3
        "Это отвратительно!!!":
            img 4061
            julia "Это отвратительно!!!"
            "Вы кажетесь приличным человеком!
            Я не думала что вы на такое способны!!!"
            sound highheels_run1
            $ juliaBasementWarningActive = False

    $ scene_transition = "Fade"
    $ autorun_to_object("bedroom2", "julia_scene_monica_thinking1")
    music casualMusic
    call refresh_scene() from _call_refresh_scene_25
    return

label julia_scene_basement1_3:
    $ juliaBasementSceneStage = 3
    img 4063
    fred "Юлия, задержись еще на минутку..."
    julia "Мистер Фред, но зачем?"
    img 4064
    sound snd_julia_scream1
    fred "Вот зачем!!!"
    img 4065
    julia "АХХХХХ!!"
    img 4066
    julia "Что вы делаете???"
    fred "Снимаю с вас трусики, Юлия!
    Могли бы помочь мне!"
    img 4067
    julia "Но зачем?
    Вы же уже кончили!"
    "У Вас же уже не стоит!"
    img 4068
    fred "Как это не стоит?
    А это что??!"
    img 4069
    julia "АХХХХХ!!"
    img 4070
    fred "Видишь?
    Он уже снова готов!"
    img 4071
    julia "Как он так быстро?
    Не могу поверить!"
    img 4072
    julia "Что вы хотите, Мистер Фред?
    Чтобы я снова глотала его?"
    img 4073
    fred "Юлия, у меня идея получше!
    Я ведь вижу что он понравился вам!"
    julia "Но Мистер Фред!"
    img 4074
    fred "Юлия! Иди ко мне моя девочка..."
    img 4075
    julia "АХХХХХ!!"
    stop music fadeout 1.0
    scene black
    image videoBasement_Fred_Julia_Teasing1_1 = Movie(play="video/Basement_Fred_Julia_Teasing1_1.mp4", fps=30)
    show videoBasement_Fred_Julia_Teasing1_1
    w
    img 4076
    music Groove2_85
    julia "Мистер Фред...
    ну хватит, пожалуйста..."
    stop music fadeout 1.0
    scene black
    image videoBasement_Fred_Julia_Teasing1_2 = Movie(play="video/Basement_Fred_Julia_Teasing1_2.mp4", fps=30)
    show videoBasement_Fred_Julia_Teasing1_2
    julia "АХХХХХ!!"
    w
    img 4077
    w
    stop music fadeout 1.0
    scene black
    image videoBasement_Fred_Julia_Teasing1_3 = Movie(play="video/Basement_Fred_Julia_Teasing1_3.mp4", fps=30)
    show videoBasement_Fred_Julia_Teasing1_3
    w
    img 4078
    w
    stop music fadeout 1.0
    scene black
    image videoBasement_Fred_Julia_Teasing2_1 = Movie(play="video/Basement_Fred_Julia_Teasing2_1.mp4", fps=30)
    show videoBasement_Fred_Julia_Teasing2_1
    w
    img 4079
    w
    stop music fadeout 1.0
    scene black
    image videoBasement_Fred_Julia_Teasing2_2 = Movie(play="video/Basement_Fred_Julia_Teasing2_2.mp4", fps=30)
    show videoBasement_Fred_Julia_Teasing2_2
    w
    img 4080
    w
    stop music fadeout 1.0
    scene black
    image videoBasement_Fred_Julia_Teasing2_3 = Movie(play="video/Basement_Fred_Julia_Teasing2_3.mp4", fps=30)
    show videoBasement_Fred_Julia_Teasing2_3
    w
    img 4081
    music Groove2_85
    fred "Юлия, развернись-ка!"
    img 4082
    julia "Мистер Фред, но зачем?"
    img 4083
    fred "Вот зачем, Юлия!
    Ха-ха!"
    img 4084
    sound snd_julia_scream1
    w
    img 4085
    julia "АХХХХХ!!"
    img 4086
    julia "Что Вы сделали, Мистер Фред?"
    img 4087
    "И что Вы собираетесь делать?"
    img 4088
    fred "Вот что, Юлия!
    Ха-ха!"
    w
    stop music fadeout 1.0
    scene black
    image videoBasement_Fred_Julia_Sex1_1 = Movie(play="video/Basement_Fred_Julia_Sex_1_1.mp4", fps=30)
    show videoBasement_Fred_Julia_Sex1_1
    julia "АХХХХХ!!"
    wclean
    img 4089
    w
    stop music fadeout 1.0
    scene black
    image videoBasement_Fred_Julia_Sex1_2 = Movie(play="video/Basement_Fred_Julia_Sex_1_2.mp4", fps=30)
    show videoBasement_Fred_Julia_Sex1_2
    wclean
    img 4090
    music Groove2_85
    julia "Мистер Фред, что вы делаете?.."
    w
    img 4091
    julia "АХХХХХ!!"
    stop music fadeout 1.0
    scene black
    image videoBasement_Fred_Julia_Sex1_3 = Movie(play="video/Basement_Fred_Julia_Sex_1_3.mp4", fps=30)
    show videoBasement_Fred_Julia_Sex1_3
    wclean
    hide videoBasement_Fred_Julia_Sex1_3
    stop music fadeout 1.0
    scene black
    image videoBasement_Fred_Julia_Sex1_4 = Movie(play="video/Basement_Fred_Julia_Sex_1_4.mp4", fps=30)
    show videoBasement_Fred_Julia_Sex1_4
    wclean
    hide videoBasement_Fred_Julia_Sex1_4
    stop music fadeout 1.0
    scene black
    image videoBasement_Fred_Julia_Sex1_5 = Movie(play="video/Basement_Fred_Julia_Sex_1_5.mp4", fps=30)
    show videoBasement_Fred_Julia_Sex1_5
    wclean
    hide videoBasement_Fred_Julia_Sex1_5
    stop music fadeout 1.0
    scene black
    image videoBasement_Fred_Julia_Sex1_6 = Movie(play="video/Basement_Fred_Julia_Sex_1_6.mp4", fps=30)
    show videoBasement_Fred_Julia_Sex1_6
    wclean
    hide videoBasement_Fred_Julia_Sex1_6
    stop music fadeout 1.0
    scene black
    image videoBasement_Fred_Julia_Sex1_7 = Movie(play="video/Basement_Fred_Julia_Sex_1_7.mp4", fps=30)
    show videoBasement_Fred_Julia_Sex1_7
    wclean
    hide videoBasement_Fred_Julia_Sex1_7
    stop music fadeout 1.0
    scene black
    image videoBasement_Fred_Julia_Sex1_8 = Movie(play="video/Basement_Fred_Julia_Sex_1_8.mp4", fps=30)
    show videoBasement_Fred_Julia_Sex1_8
    wclean
    hide videoBasement_Fred_Julia_Sex1_8
    stop music fadeout 1.0
    scene black
    image videoBasement_Fred_Julia_Sex1_9 = Movie(play="video/Basement_Fred_Julia_Sex_1_9.mp4", fps=30)
    show videoBasement_Fred_Julia_Sex1_9
    wclean
    hide videoBasement_Fred_Julia_Sex1_9
    stop music fadeout 1.0
    scene black
    image videoBasement_Fred_Julia_Sex1_10 = Movie(play="video/Basement_Fred_Julia_Sex_1_10.mp4", fps=30)
    show videoBasement_Fred_Julia_Sex1_10
    wclean
    img 4092
    w
    img 4093
    fred "ХА-ХА!"
    img 4094
    julia "АХХХХХ!!"
    img 4095
    w
    img 4096
    w
    img 4097
    w
    img 4098
    w

    $ scene_transition = "Fade"
    $ autorun_to_object("bedroom2", "julia_scene_monica_thinking1")
    music casualMusic
    call refresh_scene()

    return

label julia_scene_basement1_monica_warning:
    sound highheels_short_walk

    img 4099
    music Indo_Rock
    with fadelong
    w
    img 4100
    julia "АХХХХХ!!"
    img 4101
    fred "Еще немного, Юлия!
    Я почти закончил!"
    img 4102
    julia "АХХХХХ!!"
    img 4103
    w
    img 4104
    julia "Очень глубоко, Фред!"
    img 4105
    fred "Мистер Фред!"
    img 4106
    julia "Мистер Фред!"
    img 4107
    julia "АХХХХХ!!"
    img 4108
    julia "ААААА.. АААААААААА..."
    img 4109
    julia "МММММММММФФФФФФ...."
    img 4110
    julia "АХХХХХ!!"
    img 4111
#    sound snd_fred_argh
    fred "ААААРГХХХХ!!!"
    img 4112
    w
    img 4113
    julia "АХХХХХ!!"
    img 4114
    music Groove2_85
    fred "Поздравляю, Юлия.
    Наша сделка закрыта."
    img 4115
    w
    img 4116
    fred "Вы проявили себя как профессионал, поздравляю вас."
    img 4117
    fred "Вы отлично умеете справляться с профессиональными обязанностями!"
    img 4118
    fred "Можете вставать."
    img 4119
    with fade
    w
    img 4120
    fred "А у вас красивая фигура!"
    img 4121
    fred "Юлия, я уверен что вам понравилось!"
    img 4122
    fred "Ведь это так?"
    img 4123
    julia "Мистер Фред, Я..."
    "Я..."
    menu:
        "Мистер Фред, я не знаю что вам ответить...":
            $ juliaBasementSexLiked = True
            julia "Мистер Фред, я не знаю что вам ответить..."
            img 4124
            fred "Юлия, вы в порядке?"
            img 4125
            julia "Да, Мистер Фред.
            Я в порядке..."
            img 4129
            julia "Мистер Фред...
            Что это он делает?
            Снова встает??!?!?"
            img 4130
            fred "Да, Юлия.
            Вы ему очень понравились.
            Пожалуй, он хочет еще разок, ложитесь на пол."

        "Да как вы посмели!!!":
            img 4126
            julia "МНЕ??? ПОНРАВИЛОСЬ???
            Да как вы посмели!!!"
            img 4127
            julia "Я - бедная девушка!
            Поверила ВАМ!!"
            img 4128
            julia "Посмотрите что теперь со мной!"
            img 4129
            julia "Постойте!"
            "Что это он делает?
            Снова встает??!?!?"
            img 4130
            fred "Да, Юлия.
            Его очень возбуждает когда вы ругаетесь."
            "Он вас сразу начинает хотеть.
            Ложитесь на пол, скорее!"


    $ juliaBasementSceneStage = 4
    sound highheels_short_walk
    $ juliaBasementWarningActive = False
    img black_screen
    with fadelong
    img 4131
    julia "О БОЖЕ!!!"
    "Там кто-то идет!"
    "Наверное это Миссис Бакфетт!"
    img 4132
    fred "Идем, Юлия.
    Здесь есть другой выход на улицу."
    img 4133
    w
    sound highheels_run1
    music casualMusic
    $ scene_sound = False
    $ scene_transition = "Fade_long"
    call refresh_scene()

    return

label julia_scene_monica_thinking1:
    m "Интересно, где сейчас Юлия?"
    "Надо поискать ее..."
    return

label julia_scene_floor2_evening1_1:
    music Loved_up2
    img 5059
    with fadelong
    w
    img 5060
    with fade
    w
    img 5061
    w
    img 5062
    w
    img 5063
    fred "О! Какой вид!"
    img 5064
    with fade
    w
    sound snd_fabric1
    img 5065
    with fadelong
    w
    img 5067
    with fade
    w
    sound snd_fabric1
    img 5068
    julia "Мистер Фред, это ВЫ???"
    img 5069
    w
    #юлия трет пятно
    #фред снимает штаны
    #фред спускает трусы юлии
    #юлия в шоке смотрит вперед стоя на четвереньках
    img 5070
    "Что вы делаете???"
    img 5071
    w
    img 5072
    w
#    sound snd_fabric1
    sound Jump2
    img 5073
    with fadelong
    fred "Я помогаю вам справиться с пятном, Юлия!"
    img 5074
    julia "Таким образом???"
    img 5075
    fred "Да, Юлия! Вы, как профессионал, должны понимать связь между моими действиями."
    img 5076
    "Вы проявляете себя как профессионал, а я сообщаю об этом Миссис Бакфетт!"
    menu:
        "Вы правда попросите ее не увольнять меня?":
            img 5077
            with fade
            julia "Вы правда попросите ее не увольнять меня?"
            #начинается секс
            img 5078
            fred "Я считаю что не стоит увольнять профессиональных сотрудников!"
#            stop music fadeout 1.0
            scene black
            image videovJulia_Fred_Sex_1_1 = Movie(play="video/vJulia_Fred_Sex_1_1.mp4", fps=30)
            show videovJulia_Fred_Sex_1_1
            wclean
            #секс
            img vJulia_Fred_Sex_1_2_00
            fred "По тому как вы стараетесь, я могу сделать вывод о вашей настойчивости в достижении целей."
            scene black
            image videovJulia_Fred_Sex_1_2 = Movie(play="video/vJulia_Fred_Sex_1_2.mp4", fps=30)
            show videovJulia_Fred_Sex_1_2
            wclean
            #секс
            img vJulia_Fred_Sex_1_3_00
            fred "Это хорошее качество. И оно должно быть оценено по достоинству вашим начальством."
            scene black
            image videovJulia_Fred_Sex_1_3 = Movie(play="video/vJulia_Fred_Sex_1_3.mp4", fps=30)
            show videovJulia_Fred_Sex_1_3
            wclean
            scene black
            image videovJulia_Fred_Sex_1_4 = Movie(play="video/vJulia_Fred_Sex_1_4.mp4", fps=30)
            show videovJulia_Fred_Sex_1_4
            wclean
            #секс
            img 5079
            fred "Я также являюсь вашим начальством, поэтому и надо доказывать свой профессионализм мне."
            scene black
            image videovJulia_Fred_Sex_1_5 = Movie(play="video/vJulia_Fred_Sex_1_5.mp4", fps=30)
            show videovJulia_Fred_Sex_1_5
            wclean
            scene black
            image videovJulia_Fred_Sex_1_6 = Movie(play="video/vJulia_Fred_Sex_1_6.mp4", fps=30)
            show videovJulia_Fred_Sex_1_6
            wclean
            #секс
            img 5080
            fred "Ааааррргххххх...."
            music Groove2_85
            img 5081
            julia "Мистер Фред! Вы кончили прямо на пятно на ковре!"

            img 5082
            with fadelong
            fred "Вы убедили меня в том что не стоит мешать вам достигать своей цели."
            img 5083
            "Вы можете рассчитывать что я не буду настаивать на вашем увольнении при разговоре с Миссис Бакфетт."
            #юлия испуганно косится на фреда
            img 5084
            julia "Не будете настаивать чтобы меня увольнять? А как же помощь???"
            img 5085
            fred "К сожалению, я пока еще не все решаю здесь."
            img 5086
            "Но поверьте, вы уже добились очень многого в моих глазах."
            img 5085
            "Продолжайте работу, Юлия. Желаю вам удачи."
            img 5086
            "Сегодня вы уже не понадобитесь мне..."
            julia "..." #смотрит с обидой

        "Нет, Мистер Фред! Здесь нет никакой связи!":
            #юлия вскакивает
            music Groove2_85
            img 5087
            with fadelong
            julia "Нет, Мистер Фред! Здесь нет никакой связи!"
            "Позвольте мне продолжить выполнять мои прямые профессиональные обязанности!"
            #фред улыбается
            fred "Хорошо, Юлия. Как скажете..."
    #фред присовывает
    return

#
