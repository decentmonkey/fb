default jailDay = 0
default jailDaySceneStage = 0
default jailScenePlace = 0
default jailCageViewed = False

default jailBoobsForFood = False
default jailBoobsForFoodShowed = False
default monicaKnowOverseerName = False

default policeCellMonica1 = "Police_Cell_1_Day_1_1"
default policeCellMonica2 = "Police_Cell_2_Day_1_1"
default policeCellMonicaLabel = "jail_day1_Monica"
default policeCellBedLabel = "jail_day1_Bed"
default policeCellBed2Label = "jail_day1_Bed2"
default policeCellLampLabel = "jail_day1_Lamp"
default policeCellSortirLabel = "jail_day1_Sortir"
default policeCellCageLabel = "jail_day1_Cage"
default policeCellStageName1 = "scene_Police_Cell_1_Day_1_1"
default policeCellStageName2 = "scene_Police_Cell_2_Day_1_1"

label jail_day1:
    $ jailDay = 1
    $ jailDaySceneStage = 0
    $ jailScenePlace = 0
    $ policeCellStageName1 = "scene_Police_Cell_1_Day_1_1"
    $ policeCellStageName2 = "scene_Police_Cell_2_Day_1_1"
    sound highheels_short_walk
    img black_screen
    with fade
    sound snd_jail_door
    $ renpy.pause(1.0)
    img 2190
    with fadelong
    m "ОТПУСТИТЕ МЕНЯ!!!"
    "НЕ ТРОГАЙТЕ МЕНЯ!!!"
    img 2191
    "КТО-НИБУДЬ!!!"
    "ПОМОГИТЕ!!!!"

    img 2192
    with fadelong
    policeman1 "Заткнись, сучка!"
    "А не то выбъем тебе все зубы!"

    img 2193
    m "Пожалуйста!"

    policeman2 "Заткнись!"


    sound highheels_short_walk
    img 2194
    with fadelong
    policeman1 "Боб!"
    "Принимай свежее мясо!"
    img 2195
    "Смотри какую сучку мы тебе привели!"
    "Гордая!"
    "Кусается!"
    img 2196
    overseer "Луис, ты же знаешь что я не люблю шумных сучек."
    img 2197
    policeman1 "Не понимаю тебя, Боб!"
    "Мне наоборот такие нравятся."
    img 2198
    overseer "Луис, попробуй посидеть тут целыми днями."
    img 2199
    "У меня от них уже болит голова!"
    img 2200
    "Ладно, бросайте ее в камеру прямо за мной."
    img 2201
    policeman2 "Окей, Боб!"
    "..."
    "Двигай своей аппетитной задницей, сучка!"
    img 2202
    m "Да как вы смеете? Я..."

    policeman2 "Заткнись и иди!"

    #
    sound highheels_short_walk
    img 5089
    with fadelong
    w
    img 5090
    with fade
    $ renpy.pause(1)
    sound snd_jail_door
    $ renpy.pause(1)
    img black_screen
    with Dissolve(1)
    sound snd_handcuffs

    $ renpy.pause(1)
    policeman1 "На пол, Живо!!"
    sound snd_bodyfall
    img 5091
    with fadelong
    policeman1 "Отдыхай, детка!"
    "Теперь это твой новый дом."

    policeman2 "..."
    img 5092
    with fadelong
    "Ты одета не по форме, сучка!"
    img 5093
    with fade
    "Здесь нельзя находиться в такой одежде!"
    "Ну-ка снимай!"

    #
    sound snd_break_dress
    img black_screen
    with Dissolve(1)

    img black_screen
    with Dissolve(1)
    img 5094
    with fadelong
    m "НЕТ!!!"
    img 5095
    w
    img 5096
    "МОЕ ПЛАТЬЕ!!!"
    img 5097
    policeman1 "Оно тебе больше не нужно."
    sound snd_jail_door
    img black_screen
    with Dissolve(1)
    $ renpy.pause(2)
    sound snd_jail_lock
    img 5098
    with fadelong
    policeman2 "Мы к тебе как-нибудь заглянем, возможно."

    $ objectives_list = []
    $ add_objective("freedom", _("Избежать наказания"), c_red, 0)
    $ cloth_type = "Jail"
    $ cloth = "Lingerie"
    $ inventory = []

    call jail_day1_1
    return

label jail_day1_1:
    music I_Feel_You
    call change_scene("police_jail_scene", "Fade_long", False)
    return


    #

    #

    return

label jail_day1_2:
    img 2203
    with fadelong
    w
    img 2204
    mt "Этого не может быть!"
    "Не может быть!!!"
    img 2205
    mt "ЭТОГО НЕ МОЖЕТ БЫТЬ!!!"
    "..."
    img 2206
    mt "Это все происходит не со мной!"
    "Это не я!"
    img 2207
    mt "Это..."
    "Это..."
    img 2208
    mt "ЭТО СОН!"
    "ТОЧНО!"
    "Я СПЛЮ!"
    "Я просто сплю!"
    img 2209
    mt "Я проснусь и все это исчезнет."
    "Это просто какой-то кошмар."
    img 2210
    mt "Не бери в голову, Моника."
    img 2211
    "Тебе надо лечить нервы."
    "..."
    img 2212
    "Мне надо больше бывать на свежем воздухе."
    "И меньше общаться с никчемными людьми."
    "Совершенно бесполезными."
    "Они тратят мои нервы и не приносят результата."
    img 2213
    "В итоге вот, посмотрите!"
    "Такие кошмары как-будто это все наяву!"
    return

label jail_day1_3:
    music Groove2_85
    # подходит
    img 5117
    with fadelong
    w
    img 2214
    overseer "Эй!"
    "Ты!"
    "..."
    "Ты там жива?"
    img 2215
    m "Что вам надо?"
    img 2216
    overseer "Я принес тебе баланду."
    "Можешь ее есть."
    img 2217
    m "Что это???"
    "Что это за жуть?"
    "И почему так мало??"
    img 2218
    overseer "А ты хотела чтобы было много?"
    "Ты не перепутала место?"
    "В стране кризис!"
    "И первые на ком экономят - это заключенные!"
    "Так что ешь пока даю!"
    img 2219
    mt "..."

    "Это сон."
    "Это сон."

    "Мне надо идти прилечь."
    "Я проснусь и все это исчезнет."
    "..."
    img 2220
    mt "Моника!"
    "Ты никому не никогда не позволишь так общаться с тобой!"
    "А тем более во сне!!!"

    img 2221
    music Pyro_Flow
    m "Эй!"
    "Ты еще мне смеешь тыкать?"
    "Я дам тебе совет что делать с этой баландой!"
    "Можешь одеть ее себе на голову!"
    "После этого бегать передо мной туда-сюда."
    "И кудахтать!"
    img 2222
    "Выполняй!"
    img 2223
    overseer "Что?"
    "Да ты охренела, стерва?"
    "Я к тебе со всей душой, а ты мне так!"
    img 2224
    "Больше ты еды не увидишь!"
    img 2225
    m "Сам жри свои помои, чмо!"
    img 2226
    overseer "Еще одно слово и я вытащю тебя за волосы!"
    $ jailDaySceneStage = 2
    $ policeCellStageName1 = "scene_Police_Cell_1_Day_1_2"
    $ policeCellStageName2 = "scene_Police_Cell_2_Day_1_2"
    $ policeCellMonica1 = "Police_Cell_1_Day_1_2"
    $ policeCellMonica2 = "Police_Cell_2_Day_1_2"
    music I_Feel_You
    call refresh_scene_fade()
    return

label jail_day1_Monica(obj_name, obj_data):
    if jailDaySceneStage == 0:
        $ jailDaySceneStage = 1
        call jail_day1_2()
        return
    if jailDaySceneStage == 1:
        mt "Мне надо кого-то позвать!"
        "Я не могу находиться здесь!!!"

    if jailDaySceneStage == 2:
        mt "Это всего-лишь сон! Мне надо лечь спать!"
    return

label jail_day1_Bed(obj_name, obj_data):
    if jailDaySceneStage == 2:
        if act == "h":
            img 2227
            with fade
            mt "Все, пойду спать."
            "Хоть немного подняла настроение себе."
            "Хотя есть все-таки хочется."
            img 2228
            "Но ведь во сне все-равно нельзя поесть."

            menu:
                "Лечь спать":
                    pass
                "Не ложиться":
                    return
            img 2229
            with fadelong
            mt "Жуткая кровать."
            "Я в первый раз такое вижу."
            "Это ужас!"
            img 2230
            "Как хорошо что это просто сон!"
            "Все, ложусь спать."
            img 2231
            "Пока, Маркус!"
            call jail_day2()
            return


    mt "Жуткая кровать."
    "Я в первый раз такое вижу."
    "Это ужас!"
    return
label jail_day1_Bed2(obj_name, obj_data):
    mt "Эта другая кровать..."
    "Эта камера рассчитана на двоих?"
    "Я надеюсь здесь не поселят еще одну девушку?"
    "Моника! О чем ты думаешь?"
    "Тебе надо убираться отсюда, скорее!!!"
    return
label jail_day1_Lamp(obj_name, obj_data):
    if jailDay == 1:
        mt "Эта лампа светит ядовитым светом..."
        return
    if jailDay > 1:
        if obj_data["action"] == "l":
            mt "Эта лампа светит ядовитым светом..."
            "Она мешает мне спать! Я не могу заснуть из-за нее!"
            "Почему этот свет никогда не выключается?"
            "И почему у других он не такой ядовитый как у меня?"
        if act == "h":
            mt "Может как-то выключить ее..."
            "..."
            sound snd_woman_pain
            "Ай, она горячая!!!"

    return
label jail_day1_Sortir(obj_name, obj_data):
    if obj_data["action"] == "l":
        img 5088
        with fade
        mt "Какой ужас!"
        "О БОЖЕ!"
        call refresh_scene_fade()
        return
    if obj_data["action"] == "h":
        mt "Если честно, я не хочу подходить к ЭТОМУ..."
        "Если только мне совсем не захочется..."
        "Но, в любом случае, я буду делать это только пока никто не видит!"
    return
label jail_day1_Cage(obj_name, obj_data):
    if jailDay == 1:
        mt "Я не хочу подходить туда."
        "Там цела толпа заключенных... мужчин..."
        "Эти животные будут пялиться на меня..."

    return
