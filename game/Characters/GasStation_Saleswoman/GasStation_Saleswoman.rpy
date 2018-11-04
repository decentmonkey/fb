label gas_saleswoman_scene1: #начало, фоткает себя и общается с парнем, лаская себя
    $ gasStationSaleswomanAlmostCummed = False
    img 4134
    music Loved_up
    gas_boyfriend "Привет, Кристина"
    saleswoman "Привет, милый!"
    gas_boyfriend "Ты на работе?"
    saleswoman "Да, я на работе."

    img 4135
    gas_boyfriend "Я соскучился по тебе!
    Очень давно не видел тебя!"
    saleswoman "Да, милый.
    Ты уже слишком задержался в своей далекой командировке!"
    gas_boyfriend "Кристина, у тебя есть немного времени на меня? Я хочу тебя кое о чем попросить."
    saleswoman "Конечно есть, милый!"
    gas_boyfriend "Ведь ты на работе, тебе можно отвлечься немного? Вдруг из посетителей кто-то зайдет?"
    img 4136
    saleswoman "Фи!
    Конечно, милый!"
    img 4137
    "Работа? Там все-равно никого нет.
    И у нас не работает компьютер."
    "Так что мне нет дела зайдет кто-то или нет!"
    "Так о чем ты хотел меня попросить, милый?"

    img 4138
    gas_boyfriend "Я так соскучился по тебе!
    Хочу чтобы ты... кхмм.. разделась для меня..."

    img 4139
    saleswoman "Чтобы я сделала ЧТО?
    Разделась?"
    "По телефону?"
    gas_boyfriend "Кхм.. Ну, как бы.."
    "ДА! Милая! Я хочу чтобы ты разделась для меня по телефону!"
    "Это немного скрасит нашу разлуку!"
    saleswoman "Это что-то вроде селфи?"
    gas_boyfriend "Да, милая, можно назвать это селфи..."
    "Можешь устроить для меня небольшое селфи?"

    img 4140
    saleswoman "Селфи? Я люблю делать селфи!"
    "Так бы сразу и сказал!
    Хорошо, я сделаю для тебя селфи."
    "Но только обещай мне что будешь себя потом хорошо вести!"
    "И будешь меня слушаться всегда!"
    gas_boyfriend "Конечно, Кристина!
    Я обещаю!"
    "Я буду слушаться тебя!"
    "А сейчас покажи мне себя, скорее!"

    img 4141
    saleswoman "И что ты хочешь?
    Чтобы я сняла пиджак?"
    gas_boyfriend "Да, Кристиночка!
    Сними его!"

    sound snd_fabric1
    img 4142
    with fadelong
    saleswoman "Хорошо, милый!
    Мне так больше идет?"
    img 4143
    gas_boyfriend "Да, Кристиночка!
    Тебе так идет больше!"
    "Можешь, пожалуйста, снять эту блузку?"
    img 4144
    saleswoman "Эту блузку?
    А ты помнишь про свое обещание?
    Можешь его подтвердить?"
    gas_boyfriend "Конечно, Кристиночка!
    Я всегда буду слушаться тебя, сними блузку пожалуйста!"
    "Скорее!"
    saleswoman "Хорошо, милый..."
    sound snd_fabric1
    img 4145
    with fadelong
    saleswoman "Готово!"
    img 4146
    gas_boyfriend "Кристина!
    Ты потрясающая!"
    "Убери, пожалуйста, свою ручку!"
    "Я хочу увидеть твою грудь!"
    img 4147
    saleswoman "Вот так?"
    img 4148
    saleswoman "Так я тебе нравлюсь?"
    gas_boyfriend "Кристиночка! Ты прекрасна!"
    saleswoman "Хочешь чтобы я убрала руку?"
    gas_boyfriend "Да, Кристиночка! Очень хочу!"
    img 4149
    saleswoman "Хорошо..."
    img 4150
    saleswoman "Я тебе нравлюсь?"
    gas_boyfriend "Ты самая потрясающая девушка на свете!"
    img 4151
    saleswoman "Хочешь чтобы я еще что-нибудь сняла, милый?"
    "Тебе нравится моя юбочка?"
    gas_boyfriend "Мне она очень! Очень нравится, Кристиночка!"
    "Можешь ее опустить вниз, пожалуйста?"
    img 4152
    saleswoman "Хорошо, милый..."
    img 4153
    saleswoman "Так хватит? Или еще?"
    gas_boyfriend "Еще, Кристиночка! Сними ее полностью!"
    img 4154
    saleswoman "Хорошо, милый..."
    $ scene_transition = "Fade"
    if obj_data["action"] == "t":
        $ autorun_to_object("gas_station_view_door", "gas_saleswoman_monica_comment1_2")
    else:
        $ autorun_to_object("gas_station_view_door", "gas_saleswoman_monica_comment1")
    music casualMusic
    call refresh_scene()
    return

    "Ты этого хочешь? Я как раз собиралась расслабиться!"

    img 4136
    "Хочешь меня увидеть? Хорошо!"

    img 4137
    "Работа? Там все-равно никого нет."
    img 4138
    "И у нас не работает компьютер."

    img 4139
    "Так что мне нет дела зайдет кто-то или нет!"

    img 4140
    "Приготовься, милый."

    img 4141
    "Наши отношения еще не такие чтобы ты мог видеть это вживую, но по телефону я это сделать могу!"

    return

label gas_saleswoman_scene1_2:
    music Loved_up
    img 4155
    with fadelong
    saleswoman "Я красивая?"
    gas_boyfriend "Кристина, ты просто божественна!"
    "Спереди!"
    img 4156
    saleswoman "Хочешь посмотреть меня сзади?"
    menu:
        "Да, Кристиночка! Очень хочу!":
            pass
        "Ты мне очень нравишься! Но мне пора!":
            return False
    gas_boyfriend "Да, Кристиночка! Очень хочу!"
    img 4157
    saleswoman "Хорошо, милый!"
    img 4158
    saleswoman "Как я тебе?
    Тебе нравится моя фигура?"
    img 4159
    saleswoman "Я худенькая?"
    gas_boyfriend "Ты очень худенькая, Кристиночка!"
    img 4160
    saleswoman "Худенькая?
    Значит у меня нет попы?"
    img 4161
    gas_boyfriend "Кристиночка! У тебя просто восхитительная попа!"
    img 4162
    saleswoman "Спасибо, милый..."
    img 4163
    saleswoman "Тебе она нравится?"
    img 4164
    saleswoman "Хотел бы ее сейчас потрогать?"
    menu:
        "Да, Кристиночка! Очень хотел бы!":
            pass
        "Я ее обязательно потрогаю, когда вернусь, но сейчас мне пора!":
            return False
    img 4165
    gas_boyfriend "Да, Кристиночка! Очень хотел бы!"
    img 4166
    saleswoman "Только потрогать?"
    menu:
        "Нет! Не только потрогать!":
            pass
        "А что у тебя еще есть?":
            jump gas_saleswoman_scene1_2_sub1
    img 4167
    gas_boyfriend "Нет! Не только потрогать!"
    img 4168
    gas_boyfriend "Я хотел бы прикоснуться к ней губами и всю ее расцеловать!"
    img 4169
    #4170?
    saleswoman "Очень бы хотел?
    Очень-очень?"
    gas_boyfriend "Я бы очень-очень хотел расцеловать твою попу сейчас!"

    saleswoman "Только попу?"
label gas_saleswoman_scene1_2_sub1:
    img 4171
    saleswoman "У меня есть еще кое-что!"
    img 4172
    gas_boyfriend "Кристиночка, мне плохо видно!"
    "Можешь, пожалуйста, показать поближе?"
    img 4173
    saleswoman "Хорошо, милый!"
    saleswoman "Смотри что у меня еще есть..."
    img 4174
    gas_boyfriend "Да, Кристиночка! Твоя аппетитная киска!"
    img 4175
    saleswoman "Что бы ты хотел с ней сделать?"
    img 4176
    gas_boyfriend "Кристиночка! Твою киску я бы тоже расцеловал!"
    "Как жаль что я не вижу ее!"
    "Эти трусики... Они все закрывают!"
    img 4177
    saleswoman "Тебе нравятся мои трусики?"
    gas_boyfriend "Мне очень нравятся твои трусики, Кристиночка!"
    saleswoman "Хочешь чтобы я сняла их?"
    menu:
        "ДА! ОЧЕНЬ ХОЧУ!!!":
            pass
        "Я их обязательно сниму потом, но сейчас мне пора!":
            return False
    gas_boyfriend "ДА! ОЧЕНЬ ХОЧУ!!!"
    saleswoman "Хочешь посмотреть как я это делаю?"

    menu:
        "Да! Очень хочу посмотреть как ты это делаешь!":
            pass
        "Просто сними их скорее!":
            return True

    img 4178
    saleswoman "Хорошо, милый...
    Смотри!"
    img 4179
    saleswoman "Тебе хорошо видно, милый?"
    img 4180
    gas_boyfriend "Это просто божественное зрелище!"
    img 4181
    saleswoman "Так хватит? Или продолжать?"
    img 4182
    gas_boyfriend "Кристиночка! Снимай скорее!
    Я уже не могу терпеть увидеть твою киску!"
    return True


label gas_saleswoman_scene2: #продавщица испуганно прерывается криком из зала
    call gas_saleswoman_scene1_2()
    img 4183
#    saleswoman "saleswoman scene2"
    music Power_Bots_Loop
    m "ЭЙ!
    ЗДЕСЬ КТО-НИБУДЬ ЕСТЬ?!"
    saleswoman "ОЙ!!!"
    img 4184
    saleswoman "Милый, там кто-то пришел! Мне надо идти!"
    if _return == True:
        gas_boyfriend "А как же Я?"
        img 4185
        saleswoman "Не забывай, я на работе!"
        "А ты обещал теперь слушаться меня!"
        "Позвони мне через 5 минут!"
        gas_boyfriend "Хорошо, Кристиночка!"
        img 4186
        saleswoman "Кого там принесло?
        Обломали мне весь кайф..."
    else:
        gas_boyfriend "Хорошо, милая, мне все-равно надо идти!"
        img 4186
        saleswoman "Кого там принесло?"

    music casualMusic
    return

label gas_saleswoman_scene1_1: #сцена когда разбивается бутылка
    #jump testlabel1
    call gas_saleswoman_scene1_2()
    if _return == False:
        sound snd_bottle_break
        music Power_Bots_Loop
        w
        img 4183
        w
        sound snd_fabric1
        img 4186
        with fadelong
        saleswoman "Кого там принесло?"
        return
    img 4187
    saleswoman "Хорошо, милый... Сейчас..."
    img 4188
    w
    img 4189
    w
    img 4190
    w
    img 4191
    w
    img 4192
    saleswoman "Тебе хорошо видно, милый?"
    gas_boyfriend "Кристиночка, можешь, пожалуйста, раздвинуть ножки?"
    "Мне плохо видно!"
    img 4193
    saleswoman "Хочешь чтобы моя киска попозировала для селфи?"
    menu:
        "Да, очень хочу!":
            pass
        "Я все увидел что хотел! Кристиночка, мне пора!":
            jump gas_saleswoman_scene1_1_end
    gas_boyfriend "Да, очень хочу!"
    img 4194
    saleswoman "Хорошо, милый...
    Сейчас положу телефон, чтобы тебе было все лучше видно..."
    img 4195
    saleswoman "Тебе меня хорошо видно, милый?"
    img 4196
    gas_boyfriend "Кристиночка, я тебя вижу, но я не вижу твою киску!"
    img 4197
    saleswoman "А так?"
    gas_boyfriend "Кристиночка, можешь встать поближе?"
    img 4198
    saleswoman "Так?"
    gas_boyfriend "Еще ближе!"

    img 4199
    saleswoman "Хочешь как следует все разглядеть?"
    gas_boyfriend "Да, Кристиночка! Очень хочу!"
    img 4200
    saleswoman "Так тебе хорошо видно?"
    img 4201
    "Тебе нравится?"
    menu:
        "Да, Кристиночка! Мне очень нравится!":
            pass
        "Да, очень нравится, но мне пора бежать!":
            jump gas_saleswoman_scene1_1_end
    gas_boyfriend "Да, Кристиночка! Мне очень нравится!"
    img 4202
    saleswoman "А так?"
    img 4203
    saleswoman "Так тебе нравится?"
    img 4204
    saleswoman "Или слишком близко?"
    img 4205
    saleswoman "Я могу отодвинуться подальше, если хочешь..."
    img 4206
    gas_boyfriend "Нет, мне очень нравится!
    Побудь так немного, в такой позе!"
    "Я уже почти кончил!"
    img 4207
    saleswoman "Ишь ты какой хитрый!
    Решил сделать это без меня?"
    img 4208
    saleswoman "Я отодвинулась немного подальше!"
    img 4209
    saleswoman "Тебе нравится моя грудь?"
    img 4210
    saleswoman "Хотел бы ее поласкать?"
    img 4211
    saleswoman "Что-то ты замолчал...
    Что ты там делаешь?
    Смотришь на грудь?"
    img 4212
    saleswoman "Или на мою киску?"
    img 4213
    saleswoman "Посмотри на мои ножки... Они нравятся тебе?"
    gas_boyfriend "Да, Кристиночка! Мне очень нравятся твои ножки!"
    "Они бесконечно длинные!"

    img 4214
    saleswoman "Ты думаешь ты единственный кто может кончить по телефону?"
    music Loved_up2
    "Знаешь что у меня есть?"
    gas_boyfriend "Что?"
    img 4215
    saleswoman "Вот что!"
    img 4216
    gas_boyfriend "Кристина! Откуда у тебя это?!"
    img 4217
    saleswoman "Милый, мне нужен кто-то пока тебя нет.
    Хи-хи..."
    img 4218
    saleswoman "Посмотри на него!"
    img 4219
    saleswoman "Правда он милый?"
    img 4220
    saleswoman "Милый, почему ты молчишь?"
    "Ты ревнуешь?"
    img 4221
    saleswoman "Милый, не надо ревновать.
    Он очень похож на твой член!"
    "Я специально его подобрала!"
    "Такой же большой как у тебя!"
    img 4222
    saleswoman "ЧМОК!"
label testlabel1:
    img 4223
    saleswoman "МММмммммммнннннн..."
    img 4224
    saleswoman "Милый, представь что это ты..."
    img 4225
    saleswoman "Представил?"
    img 4226
    saleswoman "Я тоже хочу представить..."
    "Можно?"
    img 4227
    saleswoman "Или нельзя?...."

    saleswoman "Я...
    Не могу...
    Сдержаться..."
    img 4228
    music Turbo_Tornado
    saleswoman "ААааааахххх!!!!"
    img 4229
    saleswoman "О Боже!
    Как хорошо!!!..."
    img 4230
    saleswoman "ААааааахххх!!!!"
    scene black
    image videoGas_Girl_1_1 = Movie(play="video/Gas_Girl_1_1.mp4", fps=30)
    show videoGas_Girl_1_1
    wclean
    img 4231
    saleswoman "Аааааааа!!!!"
    scene black
    image videoGas_Girl_1_2 = Movie(play="video/Gas_Girl_1_2.mp4", fps=30)
    show videoGas_Girl_1_2
    wclean
    img 4232
    gas_boyfriend "Кристина! Кристина, ты здесь??"
    img 4233
    saleswoman "Аааа?? Что???"
    img 4234
    saleswoman "Ты что-то говоришь?
    Я не могу... остановиться..."
    img 4235
    saleswoman "ААааааахххх!!!!"
    scene black
    image videoGas_Girl_1_3 = Movie(play="video/Gas_Girl_1_3.mp4", fps=30)
    show videoGas_Girl_1_3
    wclean
    img 4236
    gas_boyfriend "Кристина! Кристина, ты где??"
    img 4237
    saleswoman "О Боже! Как хорошо!"
    scene black
    image videoGas_Girl_1_4 = Movie(play="video/Gas_Girl_1_4.mp4", fps=30)
    show videoGas_Girl_1_4
    wclean
    img 4246
    gas_boyfriend "Кристина! Ты меня слышишь???"
    img 4238
    saleswoman "Не могу остановиться, ААААааааа!!!"
    scene black
    image videoGas_Girl_1_5 = Movie(play="video/Gas_Girl_1_5.mp4", fps=30)
    show videoGas_Girl_1_5
    wclean
    img 4247
    gas_boyfriend "Кристина! Алло!!!"
    img 4239
    w
    img 4242
    saleswoman "Еще, еще, ЕЩЕЕЕЕЕ!!!!"
    scene black
    image videoGas_Girl_1_6 = Movie(play="video/Gas_Girl_1_6.mp4", fps=30)
    show videoGas_Girl_1_6
    wclean
    scene black
    image videoGas_Girl_1_7 = Movie(play="video/Gas_Girl_1_7.mp4", fps=30)
    show videoGas_Girl_1_7
    wclean
    scene black
    image videoGas_Girl_1_1 = Movie(play="video/Gas_Girl_1_1.mp4", fps=30)
    show videoGas_Girl_1_1
    wclean
    img 4240
    gas_boyfriend "Кристина! Где ты???"
    img 4241
    saleswoman "ДА.. АААААА!!!!"
    scene black
    image videoGas_Girl_1_9 = Movie(play="video/Gas_Girl_1_9.mp4", fps=30)
    show videoGas_Girl_1_9
    wclean
    img 4243
    gas_boyfriend "Кристина! Ты меня слышишь???"
    img 4244
    saleswoman "ЕЩЕЕЕЕЕ!!!!"
    scene black
    image videoGas_Girl_1_10 = Movie(play="video/Gas_Girl_1_10.mp4", fps=30)
    show videoGas_Girl_1_10
    wclean
    img 4248
    gas_boyfriend "Кристина! Где ты???"
    scene black
    image videoGas_Girl_1_11 = Movie(play="video/Gas_Girl_1_11.mp4", fps=30)
    show videoGas_Girl_1_11
    wclean
    $ gasStationSaleswomanAlmostCummed = True
    img 4245
    saleswoman "Я почти кончила! 10 секунд!!!"

    img 4248
    sound snd_bottle_break
    sound_from_side "(Звук разбивающегося стекла)"
    w
    img 4249
    stop music
    sound plastinka
    w
    img 4250
    w
    img 4251
    stop sound fadeout 0.5
    music Power_Bots_Loop
    w
    img 4252
    w
    img 4253
    saleswoman "Кого там принесло?"
    w
    sound snd_fabric1
    img 4186
    with fadelong
    "Обломали мне весь кайф..."
    w
    return





















label gas_saleswoman_scene1_1_end:
    music Power_Bots_Loop
    sound snd_bottle_break
    w
    img 4183
    w
    sound snd_fabric1
    img 4186
    with fadelong
    saleswoman "Кого там принесло?"
    return


label gas_saleswoman_dialogue1:
    img Gas_Station_Monica_OilTrader_1
    with fadelong
    saleswoman "Добрый день, Мэм.
    Это вы кричали?"

    m "Я кричала?
    Между прочим, я здесь жду вас уже больше часа!"

    img Gas_Station_Monica_OilTrader_3
    saleswoman "Меня не было 10 минут.
    Я была в туалете."
    img Gas_Station_Monica_OilTrader_4
    m "Это неважно, я жду достаточно, чтобы иметь претензии к вам.
    Мне нужно залить бензин."
    img Gas_Station_Monica_OilTrader_5
    saleswoman "Мэм, у нас не работает компьютер и я не могу залить бензин."
    img Gas_Station_Monica_OilTrader_6
    m "Если вы не зальете бензин, то я свяжусь в вашим Боссом."
    "И я расскажу ему что вас не было на рабочем месте."
    img Gas_Station_Monica_OilTrader_5
    saleswoman "Мэм, не стоит беспокоить моего Босса.
    Он очень строгий.
    Я залью Вам бензин"
    img Gas_Station_Monica_OilTrader_6
    m "Сразу бы так!"


    #диалог с Моникой
    $ gasStationQuestCompleted = True
    $ gasStationQuestCompletedJust = True
    return

label gas_saleswoman_scene3: #разбивается бутылка
    call gas_saleswoman_scene1_1() from _call_gas_saleswoman_scene1_1_1
    music Funk_Soul1
    call bitch(7, "gas_saleswoman_decision") from _call_bitch_53
    $ gasStationSaleswomanMischiefed = True
    $ gasStationSaleswomanMischiefInProgress = False
    $ remove_objective("gas_cashier_mischief")
    $ remove_objective("find_gas_cashier")

    img Gas_Station_Monica_OilTrader_1
    with fadelong

    saleswoman "Добрый день, Мэм.
    Это вы разбили бутылку?"

    m "Я разбила?
    Между прочим, я здесь жду вас уже больше часа!"

    img Gas_Station_Monica_OilTrader_3
    saleswoman "Меня не было 10 минут.
    Я была в туалете."

    img Gas_Station_Monica_OilTrader_4
    m "Это неважно, я жду достаточно, чтобы иметь претензии к вам.
    Мне нужно залить бензин."

    img Gas_Station_Monica_OilTrader_5
    saleswoman "Мэм, у нас не работает компьютер и я не могу залить бензин."

    img Gas_Station_Monica_OilTrader_6
    m "Девочка.
    У тебя проблема не с компьютером, а с твоей внешностью."

    "Я понимаю, тебе только и делать что торговать бензином.
    На большее у тебя не хватит ни красоты, ни мозгов."

    img Gas_Station_Monica_OilTrader_7
    "Но если ты не хочешь до конца своей жизни мыть полы.
    То ты сейчас же свяжешься с начальством и решишь проблему."

    img Gas_Station_Monica_OilTrader_8
    m "Передай что перед тобой стоит Моника Бакфетт."

    img Gas_Station_Monica_OilTrader_9
    saleswoman "Мэм, одну минуту."

    img Gas_Station_Monica_OilTrader_10
    with fadelong
    sound snd_phone1
    pause 1.5
    sound snd_phone2
    saleswoman "Добрый день, Босс.
    У меня здесь стоит женщина."

    "Она представилась как Моника Бакфетт."

    "Она требует залить бензин, но у меня не работает компьютер."

    "Она настаивает.
    Потребовала чтобы я связалась с Вами."

    saleswoman_boss "Повтори еще раз, кто стоит?"

    img Gas_Station_Monica_OilTrader_11
    saleswoman "Моника Бакфетт."
    saleswoman_boss "Ясно, наливай ей бензин."

    img Gas_Station_Monica_OilTrader_12
    saleswoman "Босс, но..."

    saleswoman_boss "Налей, потом уладим документы."

    img Gas_Station_Monica_OilTrader_13
    saleswoman "Босс, еще секунду..."

    img Gas_Station_Monica_OilTrader_14
    saleswoman "О Боже!"

    img Gas_Station_Monica_OilTrader_15
    "Она разбила самое дорогое вино, которое было на витрине!"

    menu:
        "Обвинить во всем кассиршу":
            call bitch(10, "gas_station_monicalied") from _call_bitch_54
            $ gasStationMonicaLied = True
        "Согласиться на возмещение ущерба":
            call bitch(-5, "gas_station_monicalied") from _call_bitch_55
            $ gasStationMonicaLied = False

    if gasStationMonicaLied == True:
        img Gas_Station_Monica_OilTrader_16
        m "Я не разбивала его.
        Оно стояло на самом краю."

        "И когда я проходила, оно чуть не упало на меня.
        Оно разбилось и чуть не поранило меня осколками."

        img Gas_Station_Monica_OilTrader_17
        m "Если вы не извинитесь передо мной за этот инцидент, то я подам в суд на вашу компанию."

        img Gas_Station_Monica_OilTrader_18
        saleswoman_boss "Я все слышал.
        Извинись перед ней."

        "Немедленно."

        img Gas_Station_Monica_OilTrader_19
        saleswoman "Но Босс...
        Кто будет платить за эту бутылку."

        saleswoman_boss "Стоимость бутылки будет вычтена из твоей зарплаты."

        img Gas_Station_Monica_OilTrader_20
        saleswoman "Но как...
        Она стоит больше чем я зарабатываю за месяц."

        img Gas_Station_Monica_OilTrader_21
        saleswoman_boss "Впредь будь внимательнее.
        А сейчас извинись перед мэм."

        saleswoman_boss "Я все сказал.
        До свидания."
    else:
        img Gas_Station_Monica_OilTrader_29
        m "Да, я случайно задела бутылку.
        Я оставлю свою визитку, чтобы вы прислали мне счет."
        "Можете умножить его в 3 раза, но это не отменяет того что я ждала вашу сотрудницу больше часа!"
        "И я требую извинений!"

        img Gas_Station_Monica_OilTrader_22
        saleswoman_boss "Я все слышал.
        Извинись перед ней."
        "Немедленно."

        saleswoman "Но Босс, меня не было 10 минут!"
        saleswoman_boss "Это неважно, тебя не было на рабочем месте!
        Извинись или будешь уволена."
        saleswoman_boss "Я все сказал.
        До свидания."


    sound snd_phone_short_beeps
    img Gas_Station_Monica_OilTrader_22
    w
    img Gas_Station_Monica_OilTrader_23
    w
    img Gas_Station_Monica_OilTrader_22
    w
    img Gas_Station_Monica_OilTrader_23
    w

    img Gas_Station_Monica_OilTrader_24
    with fadelong
    saleswoman "...
    Мэм...."

    "Я...."

    img Gas_Station_Monica_OilTrader_25
    m "Ну, я жду?"

    img Gas_Station_Monica_OilTrader_26
    saleswoman "Я прошу прощения..."

    "За..."

    "За то, что...."

    img Gas_Station_Monica_OilTrader_27
    m "Ну??"

    img Gas_Station_Monica_OilTrader_28
    saleswoman "Я прошу прощения за то что меня долго не было."

    if gasStationMonicaLied == True:
        "И за то что я плохо поставила бутылку на витрину."

    "Впредь такого не повторится.
    Пожалуйста, извините меня."

    img Gas_Station_Monica_OilTrader_29
    m "Не так-то ты искренне извиняешься, как я погляжу.
    Дай-ка телефон своего босса."

    img Gas_Station_Monica_OilTrader_30
    saleswoman "Мэм, пожалуйста!
    Я искренне извиняюсь!"

    "Простите меня!
    Правда!"

    img Gas_Station_Monica_OilTrader_31
    m "Ладно.
    Так уж и быть."

    "Надеюсь впредь будешь внимательнее."
    mt "Хи-хи"

    $ gasStationQuestCompletedJust = True
    $ gasStationQuestCompleted = True
    music casualMusic
    return

label gas_salewoman_sorry_dialogue:
#    img Gas_Station_Monica_OilTrader_8
    if gasStationSaleswomanMischiefed == True:
        saleswoman "Мэм, такого больше не повторится.
        Пожалуйста, извините."
    else:
        saleswoman "Мэм, как вы видите я на рабочем месте.
        Чем могу быть Вам полезна?"

    return

label gas_saleswoman_monica_comment1:
    m "Или мне просто показалось?..."
    return
label gas_saleswoman_monica_comment1_2:
    m "Или мне просто показалось?..."
    jump gas_station_door_talk
    return
