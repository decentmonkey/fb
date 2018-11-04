default monicaMonkeysStage = 0
default steveOffended1 = False

default monkeysOffended1 = False
default monkeysOffended2 = False
default monkeysOffended3 = False
default monkeysOffended4 = False

default monkeysSeenMelanie = False

default monicaMonkeysStageDropFlag = False

default grayMouse2WhoreOffended = False

label monica_office_monkeys_interact(obj_name, obj_data):
    if obj_data["action"] == "l":
        m "Жалкие существа."
        "Я могу их прогнать прямо сейчас."
        "Но могу и поиграть с ними!"
    if obj_data["action"] == "t":
        if monicaMonkeysStage == 1:
            jump monkeys_monica_office1_3
        if monicaMonkeysStage == 2:
            jump monkeys_monica_office1_4
    return

label monica_office_monkey_exit_blocked(obj_name, obj_data):
    mt "Я не могу уйти, пока здесь они.
    Мне надо решить что с ними делать."
    return

label monkeys_monica_office1(obj_name, obj_data):
    $ remove_objective("go_work")
    $ monicaOfficeWorkMonkeysPlanned = False
    $ monicaOfficeSteveCall1Planned = False
#    $ monicaOfficeCabinetMonkeys = True
    $ scene_transition = "Fade_long"
    $ autorun_to_object("monica_office_cabinet_table", "monkeys_monica_office1_2")
    sound snd_phone1
    call refresh_scene() from _call_refresh_scene_12
    return

label monkeys_monica_office1_2:
#    pause 2
    sound snd_phone2

    secretary "Добрый день еще раз."

    "Это секретарь Миссис Бакфетт."

    "Вы можете поднятся."

    "Она в своем кабинете ожидает вас."

    $ entranceMonkeys = False

    pause 2

    sound snd_phone1
    pause 2
    sound snd_phone2

    img 1155
    steve "Да, Моника.
    Я тебя слушаю."

    img 1156
    m "Моника? Слушаю????"

    "ЭТО Я ТЕБЯ СЛУШАЮ, СТИВ!!!"

    "Мы с тобой договаривались об аренде!"

    "Секретарь сказала что платежа так и нет."

    "ГДЕ ОН???"

    steve "Моника."

    "Я все сделал как мы договаривались."

    "Может быть это банк задерживает?"

    sound snd_lift
    pause 4
#    $ renpy.pause(4, hard=True)
    sound highheels_run1
#    $ renpy.pause(2, hard=True)
    wc
    img 1159
    with fadelong

    m "Банк задерживает?"

    "Да, такое бывает."

    "Если денег завтра не будет, то я съезжу в банк проверю сама."

    steve "Конечно, Моника."

    "Ты можешь проверить."

    "Я тебя никогда не обманывал."

    img 1157
    m "Ты?"

    "Никогда не обманывал?"

    img 1158
    "ДА Я ЗНАЮ ТЕБЯ ОЧЕНЬ ХОРОШО!!!"

    menu:
        "Обозвать Стива.":
            $ steveOffended1 = True
            call bitch(2, "steve_offended1") from _call_bitch_38
            img 1160
            with fade
            m "ТЫ!!"

            "МЕШОК С ДЕРЬМОМ!!!"
            img 1161
            sound snd_gulp
            model1 "(испуганно сглатывает)"

            img 1162
            sound snd_gulp
            model2 "(испуганно сглатывает)"

        "Выразиться мягче.":
            m "Ты!
            Обманщик!"

    img 1163
    m "ТАК ЧТО НЕ ДУМАЙ ЧТО Я НЕ ПРОВЕРЮ!!!"

    "Разговор закончен."

    img 1164
    "НА СЕГОДНЯ!!!"

    img 1165
    with fade
    music All_Stars_Loop
    m "Так."

    "А это у нас еще кто?"

    menu:
        "Обозвать их мартышками.":
            call bitch(2, "monkeys_offend1") from _call_bitch_39
            $ monkeysOffended1 = True
            "А, это те две мартышки, которые стояли внизу?"
            img 1166
            sound snd_gulp
            model1 "(испуганно сглатывает)"

            img 1167
            sound snd_gulp
            model2 "(испуганно сглатывает)"

            img 1168
            m "И вы считаете что можете быть моделями?"

        "Начать разговор.":
            $ monkeysOffended1 = False
            if entranceTalkedWithMonkeys == False:
                call bitch(-1, "monkeys_offend1") from _call_bitch_40
                m "Я никогда вас не видела."
            else:
                call bitch(-8, "monkeys_offend1") from _call_bitch_41
                m "Я видела вас внизу, вы мне нагрубили"
                img 1166
                sound snd_gulp
                model1 "(испуганно сглатывает)"

                img 1167
                sound snd_gulp
                model2 "(испуганно сглатывает)"
                m "Но я не держу обиды.
                Вы не знали с кем разговариваете."

            img 1168
            m "Итак, вы считаете что можете быть моделями?"



    img 1169
    model1 "Мэм."

    "Вообще-то да."

    "Мы хотим попробовать."

    model2 "Нам очень нужна работа."

    "Мы будем стараться."

    m "Хорошо."

    "Встаньте обе передо мной!"

    "И покажите что из себя представляете."

    img 1170
    model1 "Мэм..."

    "Вы собираетесь проводить кастинг с нами обеими одновременно?"

    model2 "Мэм."

    "Может быть есть возможность провести его по отдельности?"

    if monkeysOffended1 == True:
        m "У меня нет времени возиться с вами по отдельности."
    else:
        m "Ничего страшного, не стесняйтесь."

    m "Итак."

    m "Покажите что умеете."

    "Принимайте разные позы."

    "Привлеките внимание."

    model1 "Хорошо, Мэм."
    model2 "Хорошо, Мэм."

    img 1171
    w
    img 1172
    w
    img 1173
    w
    img 1174
    w
    img 1175
    w
    img 1176
    w
    img 1177
    w
    img 1178
    w
    img 1179
    w
    img 1180
    w
    img 1181
    w
    img 1182

    music casualMusic

    m "Стоп."

    "Стоп. Стоп."

    img 1183
    "Это никуда не годится."

    "Не вижу никакого эффекта."


    $ subst_to_object("Teleport_Monica_Office_Secretary", "monica_office_monkey_exit_blocked")
    $ monicaMonkeysStage = 1
    $ monicaOfficeCabinetMonkeys = True
    $ scene_transition = "Fade"
    call refresh_scene() from _call_refresh_scene_13
    return

label monkeys_monica_office1_3:
    menu:
        "Они никуда не годятся, но я продолжу издеваться над ними.":
            $ monkeysOffended2 = True
            call bitch(2, "monkeys_offend2") from _call_bitch_42

        "Выгнать их":
            jump monkeys_monica_office1_get_out

    if monkeysOffended1 == True:
        "Возможно дело в ваших обносках."
    else:
        "Возможно дело в ваших вещах, что на вас одеты."

    "Снимите одежду."

    "До белья."

    model1 "Хорошо, Мэм."
    model2 "Хорошо, Мэм."

    sound snd_fabric1
    music All_Stars_Loop

    img 1184
    with fadelong

    img 1186
    w
    img 1187
    w
    img 1188
    w
    img 1185
    m "Обернитесь."

    img 1189
    w
    img 1190
    w
    img 1191
    w
    img 1192
    m "Хорошо."

    "Начинайте."

    img 1193
    w
    img 1194
    w
    img 1195
    w
    img 1196
    w
    img 1197

    m "Стоп."
    music:casualMusic

    img 1198
    w
    img 1199
    mt "Ну что это за убожество?"

    "Надо будет еще раз высказать секретарше неудовольствие по поводу тех кого она ко мне посылает."

    "Ну что это такое?"

    "Какие из них модели?"

    "Я бы таких даже уборщицами не взяла."

    "Вот такие люди."

    "Все пытаются куда-то подняться."
    "Чего-то добиться."

    "А сами они кто?"

    "Как они могут сравнивать себя с такими как Я?"

    "У каждого свое место в жизни."

    img 1200
    "Я богатая. Красивая."

    if monkeysOffended1 == True:
        "А они жалкие ничтожества."
    else:
        "А они маленькие людишки."

    "Корчатся сейчас передо мной.
    На что-то надеются."

    "Пора их выгнать."

    "Надо решить."

    if entranceTalkedWithMonkeys == True:
        mt "Хотя стой.
        Они же мне что-то сказали там внизу."

        "Хм.
        Неважно что они там говорили."

        "Важно то что сейчас они подчиняются мне."

        "Будут делать все что я скажу."

        "Потому что Я сверху, а они - снизу."

        img 1201
        "Мне нравится это использовать :)"

    music casualMusic
    $ subst_to_object("Teleport_Monica_Office_Secretary", "monica_office_monkey_exit_blocked")
    $ monicaMonkeysStage = 2
    $ monicaOfficeCabinetMonkeysSuffix = "2"
    $ monicaOfficeCabinetMonkeys = True
    $ scene_transition = "Fade"
    call refresh_scene() from _call_refresh_scene_14
    return

label monkeys_monica_office1_4:

    menu:
        "Заставить их полностью раздеться. Ха-ха!!!":
            $ monkeysOffended3 = True
            call bitch(8, "monkeys_offend3") from _call_bitch_43

        "Выгнать их":
            jump monkeys_monica_office1_get_out

    m "Девочки!"

    img 1198
    model1 "Да, Мэм."
    model2 "Да, Мэм."

    m "Вы знаете.
    Что-то в вас есть."

    "Для того чтобы все получилось, вам надо продолжать."

    model1 "Мэм, но что продолжать?"

    "Мы стараемся изо всех сил!"

    m "Все просто."

    "Снимите одежду."

    model2 "Мэм, но у нас и так снята одежда."

    m "Неужели?"

    "Раздевайтесь полностью."

    img 1202
    model1 "Мэм, но зачем..."
    model2 "Мэм, мы стесняемся..."

    img 1203
    m "Если вы не готовы раздеться, значит вы не готовы получить работу."

    "Мне надо увидеть полностью своих моделей."

    "Оценить их."

    "У меня ответственная работа."

    "Я возглавляю очень популярный журнал.
    С хорошей репутацией."

    "Мы профессионалы, поэтому требуется неукоснительно соблюдать качество."

    "Если вы готовы стать профессионалами, то должны делать все что я скажу..."

    img 1204
    "ИЛИ МОЖЕТЕ УХОДИТЬ!"

    img 1205
    w
    img 1206
    music RocknRoll_loop
    w
    img 1207
    w
    img 1208
    w
    img 1209
    w
    img 1210
    w
    img 1211
    m "Встать сюда."

    img 1212
    w
    img 1213
    w
    img 1214
    w
    img 1215
    w
    img 1216

    m "Встаньте спиной."

    img 1217
    w
    img 1218
    w
    img 1219
    w
    img 1220
    m "Нагнитесь сильнее."

    img 1221
    w
    img 1222
    w
    img 1223
    w
    img 1224
    m "Не поняла!"

    "Я, кажется, приказала раздеться."

    "Что это на тебе болтается?"

    "Что ты там прячешь??!"

    "Я должна знать моделей досконально!
    Вам нечего скрывать от меня!"

    "И положи руки на свой зад, как это сделала твоя подруга!"

    img 1225
    w
    img 1226
    w
    img 1227

    m "На четвереньки задом ко мне!"

    img 1228
    mt "Хорошо что моя секретарь не видит этого."

    "Ее высокоморальная душа не выдержала бы этого."

    "Но что поделать.
    Надо воспитывать таких как эти..."

    "Хи-хи."

    img 1229
    w
    img 1230
    w
    img 1231
    w
    img 1232
    w
    img 1235
    w
    img 1236
    w
    img 1237
    w
    img 1238
    w
    img 1239
    w
    img 1240
    w
    img 1241
    w
    img 1242
    w
    img 1243
    w
    img 1245
    w
    img 1246
    w

    mt "..."

    mt "Так, пора заканчивать этот цирк."

#
    img 1247
    music casualMusic
    m "ТАК СТОП."

    "СТОП. СТОП!"

    "Вставайте и одевайтесь!"

    sound snd_fabric1
    img 1248
    with fadelong
    model1 "Мэм, мы приняты?"

    img 1249
    m "Вы не подходите."

    "Можете уходить."

    img 1250
    model1 "Мэм, но как?"
    model2 "Мы думали мы Вам подходим?"

    "Все что мы здесь сейчас делали..."

    img 1251
    m "Вы проходили кастинг."

    "Вы его завалили."

    "До свидания."

    img 1252
    model1 "Мэм, но пожалуйста!"

    "Дайте нам шанс!"

    "Проведите с нами фотосессию, хотя бы одну!"

    model2 "Вы не должны так просто нас выгнать!"

#    $ subst_to_object("Teleport_Monica_Office_Secretary", "monica_office_monkey_exit_blocked")
#    $ monicaMonkeysStage = 3
#    $ monicaOfficeCabinetMonkeysSuffix = "1"
#    $ monicaOfficeCabinetMonkeys = True
#    $ scene_transition = "Fade"
#    call refresh_scene()
#    return

#label monkeys_monica_office1_5:

    img 1253
    m "Не должна так просто вас выгнать?"

    "Хорошо."

    "Кто вы?"

    "Откуда?"

    img 1254
    m "И почему я не должна вас выгнать?"

    img 1255
    model1 "У меня нет родителей.
    И никто мне не помогает."

    "Я учусь.
    Мне надо платить деньги за учебу."

    "Завтра последний день!"

    "Мне надо заработать хоть что-нибудь!"

    img 1256
    model2 "Я приехала издалека."

    "У меня нет денег."

    "И мне уже сегодня нечего есть."

    img 1257
    m "О Боже!"

    "Нечего есть..."

    "Нечем платить...."

    "Это все глупые аргументы, не достойные обсуждения в обществе, к которому я принадлежу."

    "Это принято обсуждать в ваших кругах."

    "Бедняков и неудачников."

    img 1258
    m "Вот вы хотите устроиться на работу."

    "А у вас проблемы."

    "Не знаю понимаете-ли вы или нет, но мне не нужны на работе люди с проблемами."

    "Независимо от вашего вида."

    "Если есть проблемы, значит нет работы."

    img 1259
    "Да и ваш вид."

    "Ну посмотрите на себя!"

    "Как вы с такими формами вообще могли придти на кастинг?"

    menu:
        "Показать им как выглядят настоящие модели.":
            m "..."

        "Прогнать их сейчас же!":
            jump monkeys_monica_office1_get_out_now


    img 1260
    "Знаете что?"

    "Я добрый человек."

    "Я дам вам кое-какие знания на будущее."

    "Я покажу вам как выглядят и ведут себя настоящие модели."

    img 1261
    "Идите в студию."

    jump monkeys_monica_photostudio1


label monkeys_monica_office1_get_out:

    if monicaMonkeysStageDropFlag == False:
        if monkeysOffended1 == True:
            call bitch(2, "monkeys_offend_getout_1") from _call_bitch_44
            m "Знаете что, мартышки?!
            Вы мне не подходите!"
        else:
            call bitch(1, "monkeys_offend_getout_1") from _call_bitch_45
            m "Нет, извините, но вы мне точно не подходите!"
    if monicaMonkeysStage == 2 and monicaMonkeysStageDropFlag == False:
        m "Одевайтесь."
        sound snd_fabric1
        $ monicaMonkeysStageDropFlag = True
        $ monicaOfficeCabinetMonkeysSuffix = "1"
        $ scene_transition = "Fade_long"
        $ autorun_to_object("monica_office_cabinet_table", "monkeys_monica_office1_get_out")
        call refresh_scene() from _call_refresh_scene_15
        return

    menu:
        "Показать им как выглядят настоящие модели.":
            m "Знаете что?"

            "Я добрый человек."

            "Я дам вам кое-какие знания на будущее."

            "Я покажу вам как выглядят и ведут себя настоящие модели."

            "Идите в студию."
            jump monkeys_monica_photostudio1

        "Прогнать их сейчас же!":
            jump monkeys_monica_office1_get_out_now
    return

label monkeys_monica_office1_get_out_now:

    if monkeysOffended1 == True:
        call bitch(1, "monkeys_offend_getout_1") from _call_bitch_46
        m "Убирайтесь вон, сейчас же!"
    else:
        m "Пожалуйста, покиньте мой офис!
        У меня и так много работы!"

    $ monicaOfficeDickIncomingCallPlanned = True
    $ autorun_to_object("monica_office_cabinet_table", "dickIncomingCallDay1")
    sound highheels_run1
    music casualMusic
    $ subst_to_object("Teleport_Monica_Office_Secretary", False)
    $ monicaMonkeysStage = 3
    $ monicaOfficeCabinetMonkeysSuffix = "1"
    $ monicaOfficeCabinetMonkeys = False
    $ photoStudioOpened = True
    $ photostudioEmpty = True
    $ scene_transition = "Fade_long"
    $ add_objective("go_work", _("Продолжить работать"), c_green, 20)
#    $ autorun_to_object("monica_office_photostudio", "monica_office_photostudio_autorun_monica_day_1")
    call refresh_scene() from _call_refresh_scene_16
    return


label monkeys_monica_photostudio1:
    $ melaniePhotoShotProcessed = True

    show screen notify(_("Кастинг модели убежали в фотостудию..."))
    $ photoStudioOpened = True
    sound highheels_run1
    music casualMusic
    $ subst_to_object("Teleport_Monica_Office_Secretary", False)
    $ monicaMonkeysStage = 3
    $ monicaOfficeCabinetMonkeysSuffix = "1"
    $ monicaOfficeCabinetMonkeys = False
    $ photoStudioOpened = True
    $ scene_transition = "Fade_long"
    $ add_objective("go_photostudio", _("Идти в фотостудию"), c_green, 20)
    $ autorun_to_object("monica_office_photostudio", "monica_office_photostudio_autorun_monica_day_1")
    call refresh_scene() from _call_refresh_scene_17
    return

label monkeys_monica_photostudio1_2:
    $ remove_objective("go_photostudio")
    $ monkeysSeenMelanie = True

    music ZigZag

    img 1262
    img 1263
    alex_photograph "Добрый день, Мэм!"
    img 1264

    melanie "Здравствуйте, Миссис Бакфетт!
    Вы сегодня отлично выглядите!"

    img 1265
    m "Спасибо, Мелани.
    Ты, в целом тоже ничего."

    "Хотя до меня тебе, конечно, далеко."

    img 1266
    melanie "Мэм, конечно!"

    "Вы просто идеал красоты!"

    img 1267
    "Вы так хорошо смотритесь на обложке нового журнала!"

    img 1268
    "Вам завидуют все модели!"

    img 1269
    m "Еще бы."

    "Но к делу."

    img 1270
    "Алекс, Мелани.
    Покажите этим двум школьницам как снимаются настоящие фотомодели."

    img 1271
    alex_photograph "Конечно, Мэм!
    Мы как раз проводим фотосессию!"

    "Мелани, ты готова?"

    img 1272
    melanie "Конечно, Алекс!"

    img 1273
    alex_photograph "Тогда начинаем!"

    music Molten_Alloy
    "Мотор!"

    img black_screen
    with Dissolve(1.0)

    img 1274
    call photoshop_flash() from _call_photoshop_flash
    w
    img 1275
    call photoshop_flash() from _call_photoshop_flash_1
    w
    img 1276
    call photoshop_flash() from _call_photoshop_flash_2
    w
    img 1277
    call photoshop_flash() from _call_photoshop_flash_3
    w
    img 1278
    call photoshop_flash() from _call_photoshop_flash_4
    w
    img 1279
    call photoshop_flash() from _call_photoshop_flash_5
    w
    img 1280
    call photoshop_flash() from _call_photoshop_flash_6
    w
    img 1281
    call photoshop_flash() from _call_photoshop_flash_7
    w
    img 1282
    call photoshop_flash() from _call_photoshop_flash_8
    w
    img 1283
    call photoshop_flash() from _call_photoshop_flash_9
    w
    img 1284
    w
    img 1285
    call photoshop_flash() from _call_photoshop_flash_10
    w
    img 1286
    call photoshop_flash() from _call_photoshop_flash_11
    w
    img 1287
    call photoshop_flash() from _call_photoshop_flash_12
    w
    img 1288
    call photoshop_flash() from _call_photoshop_flash_13
    w
    img 1289
    call photoshop_flash() from _call_photoshop_flash_14
    w
    img 1290
    call photoshop_flash() from _call_photoshop_flash_15
    w
    img 1291
    call photoshop_flash() from _call_photoshop_flash_16
    w
    img 1292
    call photoshop_flash() from _call_photoshop_flash_17
    w
    img 1293
    call photoshop_flash() from _call_photoshop_flash_18
    w
    img 1294
    call photoshop_flash() from _call_photoshop_flash_19
    w
    img 1295
    call photoshop_flash() from _call_photoshop_flash_20
    w
    img 1296
    w
    img 1297
    call photoshop_flash() from _call_photoshop_flash_21
    w
    img 1298
    call photoshop_flash() from _call_photoshop_flash_22
    w
    img 1299
    call photoshop_flash() from _call_photoshop_flash_23
    w
    img 1300
    call photoshop_flash() from _call_photoshop_flash_24
    w
    img 1301
    call photoshop_flash() from _call_photoshop_flash_25
    w
    img 1302
    call photoshop_flash() from _call_photoshop_flash_26
    w
    img 1303
    w
    img 1304
    call photoshop_flash() from _call_photoshop_flash_27
    w
    img 1305
    w
    img 1306

    m "Довольно"


    music casualMusic
    img 1307
    melanie "Мэм, вам понравилось?"

    menu:
        "Сделать Мелани замечание.":
            $ melanieOffended1 = True
            call bitch(2, "melanie_offended1") from _call_bitch_47
            img 1308
            m "В целом неплохо, Мелани."

            "Я смотрю ты поправилась немного."

            "Следи за собой, пожалуйста."

            "На твое место много желающих."

            img 1309

            melanie "Конечно, Мэм!"

            "Я буду стараться лучше!"

        "Сказать что понравилось.":
            $ melanieOffended1 = False
            call bitch(-2, "melanie_offended1") from _call_bitch_48
            img 1308
            m "Ты молодец, Мелани.
            Ты выглядишь просто потрясающе!"

            img 1309
            melanie "Спасибо, Мэм!
            Мне очень приятно!"

    img 1310
    m "Алекс."
    img 1311
    alex_photograph "Да, Мэм!"

    img 1310
    alex_photograph "В целом ты неплохо работаешь, но..."

    img 1311
    alex_photograph "Да, Мэм?"

    img 1310
    m "Я уже упоминала тебе как-то про это."

    "Ты берешь слишком откровенные и эротичные кадры."

    "У них, конечно, есть своя аудитория."

    "Но у нас приличный журнал.
    И некоторые ракурсы выглядят неподобающе."

    menu:
        "Сказать что он будет уволен если ослушается":
            call bitch(2, "alexphotograph_offended1") from _call_bitch_49
            $ alexPhotographOffended1 = True
            img 1312
            m "Если ты, все-же, не перестанешь этого делать, то лишишся работы."

            "Ты меня понял, Алекс?"

            img 1311
            alex_photograph "Да, Мэм!"
            "Я Вас понял!"

            img 1312
            m "И?"

            img 1311
            alex_photograph "Такого больше не повторится, Мэм!"

            "Я клянусь!
            Все будет так как скажет мой Босс!"

            img 1312
            m "А кто Босс?"

            img 1313
            alex_photograph "Конечно Вы, Мэм!"


        "Попросить его войти в мое положение.":
            call bitch(-2, "alexphotograph_offended1") from _call_bitch_50
            $ alexPhotographOffended1 = False
            m "Алекс, я знаю что ты лучший фотограф, которого я только могу найти."
            "Но, пожалуйста, войди в мое положение
            На кону репутация журнала."
            img 1311
            alex_photograph "Мэм, я обещаю что исправлюсь!"

            "Больше никаких откровенных ракурсов."

    img 1314
    m "Хорошо.
    Вы свободны."

    $ melanieAlexBeforePhotoshoot = False
    $ melanieAlexAfterPhotoshoot = True

    img 1315
    with fadelong
    m "Ну что, вы все поняли?"

    img 1316
    model1 "Да, нам все понятно."

    model2 "Мэм, но может все-таки?"

    menu:
        "Я СКАЗАЛА БЫСТРО ВОН ОТСЮДА! МАЛЯВКИ!!!":
            $ monkeysOffended4 = True
            call bitch(2, "monkeys_offend4") from _call_bitch_51

            img 1317
            m "ТАК."

            "БЫСТРО ВОН ОТСЮДА!"

            "МОЕ ТЕРПЕНИЕ ЗАКОНЧИЛОСЬ!"

            "ВОН!!!!"


        "Мое решение окончательно. Мне очень жаль что так вышло.":
            $ monkeysOffended4 = True
            call bitch(-2, "monkeys_offend4") from _call_bitch_52
            img 1315
            "Мое решение окончательно.
            Мне очень жаль что так вышло."
            img 1316
            model1 "Да, Мэм.
            Мы понимаем.
            До свидания."

    $ monicaOfficeDickIncomingCallPlanned = True
    $ autorun_to_object("monica_office_cabinet_table", "dickIncomingCallDay1")
    sound highheels_run1
    $ add_objective("go_work", _("Продолжить работать в своем офисе"), c_green, 20)
    $ scene_transition = "Fade_long"
    call refresh_scene() from _call_refresh_scene_18

    return


label monkeys_melanie_alex_after_photoshoot1(obj_name, obj_data):
    if obj_name == "AlexPhotograph":
        img 1319
        alex_photograph "Мэм, я обещаю что исправлюсь!
        Больше никаких откровенных ракурсов."
        img 1320
        w
    if obj_name == "Melanie":
        img 1318
        melanie "Мэм, вы великолепны!"
        w
    return
















#
