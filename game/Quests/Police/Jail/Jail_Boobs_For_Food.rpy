label jail_boobs_for_food:
    if jailDay == 4:
        img 5159
        with fade
        w
        img 5160
        w
        img 5162
        music Loved_up2
        with fadelong
        w
        img 5161
        with fade
        w
        img 5164
        w
        img 5165
        w
        img 5166
        w
        img 5167
        w
        music Groove2_85

    if jailDay == 5:
        music Loved_up2
        img 5174
        with fade
        w
        img 5175
        with fade
        w
        img 5176
        w
        img 5177
        w
        img 5178
        w
        img 5179
        w
        music Groove2_85
    if jailDay == 6:
        music Loved_up2
        img 5184
        with fadelong
        w
        img 5185
        w
        img 5186
        w
        img 5187
        w
        img 5188
        w
        img 5189
        w
        music Groove2_85

    if jailDay == 7:
        music Loved_up2
        img 5193
        with fadelong
        w
        img 5194
        w
        img 5195
        w
        img 5196
        w
        img 5197
        w
        img 5198
        w
        img 5199
        w
        music Groove2_85

    if jailDay == 8:
        music Loved_up2
        img 5203
        with fadelong
        w
        img 5204
        w
        img 5205
        w
        img 5206
        with fadelong
        w
        img 5207
        w
        img 5208
        w
        img 5209
        w
        img 5210
        w
        img 5211
        w
        img 5212
        w
        img 5213
        with fade
        w
        music Groove2_85

    if jailDay == 9 and jailDaySceneStage == 0:
        img 5218
        with fadelong
        mt "О БОЖЕ!!!"
        "КАК МЕНЯ ДОСТАЛ ЭТОТ КРЕТИН!!!"
        overseer "Ну? Так что?"
        img 5219
        m "Сейчас..."
        img 5220
        with fade
        w
        music Loved_up2
        img 5221
        with fade
        w
        img 5222
        with fade
        w
        img 5223
        with fade
        w
        img 5224
        with fade
        w
        img 5225
        with fade
        w
        img 5226
        with fade
        w
        img 5227
        with fade
        w
        music Groove2_85

    if jailDay == 9 and jailDaySceneStage == 2:
        music Loved_up2
        img 5233
        with fade
        w
        img black_screen
        with Dissolve(1)
        img 5234
        with fade
        w
        img 5235
        with fade
        w
        img 5236
        with fade
        w
        img 5237
        with fade
        w
        img 5238
        with fade
        w
        img 5239
        with fade
        w
        stop music
        sound Jump2
        img 5240
        with hpunch
        overseer "Дай потрогать."
        music Pyro_Flow
        img 5241
        m "Сэр! Что значит потрогать?!"
        "Мы так не договаривались!"
        img 2429
        overseer "Я смотрю тебе надоела еда?!"
        img 5242
        "И ты не хочешь чтобы я еще куда-то ходил по твоим дурацким просьбам?"
        img 5243
        with fadelong
        w
        img 5244
        with fadelong
        w
        img 5245
        with fade
        menu:
            "Дать потрогать...":
                pass
        music Loved_up2
        m "Нет... Сэр..."
        img 5246
        with fade
        "Сейчас..."
        img 5247
        with fade
        "Можете трогать..."
        img 5248
        with fade
        w
        img 5249
        with fade
        w
        img 5250
        with fade
        w
        img 5251
        with fade
        w
        music Groove2_85
        img 5252
        mt "НЕНАВИЖУ!!!"
        img 5253
        "Я УБЬЮ ЕГО!!! УБЬЮ!!!"
        img 5254
        m "ДОСТАТОЧНО!!!"
        img 5255
        "Вы получили что хотели..."

    if jailDay == 10:
        img 5263
        w
        img 5264
        with fadelong
        m "Хорошо, Сэр..."
        img 5265
        with fade
        w
        sound snd_jail_door
        img black_screen
        with Dissolve(1)
        img 5266
        with fadelong
        m "Аххххх!!"
        "Что вы делаете?!"
        img 5267
        overseer "Всего-лишь трогаю тебя за сиськи!"
        "Ты ведь хочешь узнать хорошие новости?"
        menu:
            "Дать потрогать...":
                pass
        music Loved_up2
        img 5268
        w
        img 5269
        w
        img 5270
        w
        img 5271
        w
        sound Jump2
        img 5272
        w
        img 5273
        w
        img 5274
        w
        img 5275
        w
        img 5276
        w
        img 5277
        w
        img 5278
        w
        img 5279
        w
        img 5280
        w
        img 5281
        w
        img 5282
        w
        img 5283
        w
        img 5284
        w
        music Groove2_85
        img 5285
        w
        img 5286
        m "ХВАТИТ!!!"


#    m ".."
    # показывает сиськи
    # day4
    # day5
    # day6
    # day9 2 стадии (вторая - jailDaySceneStage == 2, еще и трогает)
    # day10 веселая но сдержанная, трогает
    return


label jail_boobs_for_food_end:
    # Моника знает имя Боба
    music Hidden_Agenda
    img 5460
    m "Стойте!"
    "Сэр!"
    "Я умею быть вежливой..."
    img 5461
    overseer "Да? Докажи!"
    img 5462
    m "Мистер Боб!"
    "Не могли бы Вы покормить меня?"
    "Я хорошо веду себя..."
    img 5461
    overseer "Надо же!"
    "Ты вспомнила как меня зовут?"
    "Я надеюсь тебе никто не подсказывал?"
    "Например эти ребята напротив..."
    img 5462
    m "Нет... Сэр..."
    img 5461
    overseer "Хорошо если так. Эти ребята просто так ничего не делают."
    "С ними связываются только шлюхи."
    "Ты ведь не такая, правда?"
    img 5462
    m "Нет... Сэр..."
    "Спасибо что предупредили."
    img 5461
    overseer "Так уж и быть. Если ты приличная девушка, то я буду кормить тебя..."
    img 5463
    m "Спасибо... Сэр..."
    music Groove2_85
    $ jailBoobsForFood = False
    return
