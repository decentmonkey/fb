label monica_office_entrance_beef_dialogue1:
    #render
    #Разговор Моники с Бифом около входа в лифт (появляется когда Моника пытается поехать на нем)
    img 6298
    w
    img 6299
    beef "Детка? Ты хочешь попасть наверх?"
    img 6300
    m "Кто вы?"
    beef "Меня зовут Биф!"
    img 6301
    m "Биф, ты знаешь код?"
    beef "Конечно, детка!"
    img 6302
    "Код 4287!"
    img 6303
    m "Спасибо, Мистер!" #кривит лицо
    #звук лифта
    img 6304
    beef "О! Не за что, детка!"
    "Интересно, как такая попка прошла мимо меня?"
    img 6305
    m "Что Вы имеете ввиду?!"
    "Как Вы позволяете себе разговаривать со мной?!"
    img 6306
    beef "Детка, ты ведь едешь сниматься в студии, правда?"
    img 6307
    w
    #звук jump1
    #шлепает ее по попе
    img 6308
    w
    img 6309
    "Алексу влетит за то, что решил скрыть от меня такую цыпочку!"
    img 6310
    m "Я не цыпочка!"
    "Отвали от меня, урод!"
    beef "Ха-ха-ха!"
    return

label monica_office_secretary_dialogue1:
    #render
    #Моника разговаривает с секретаршей. (срабатывает даже если Моника идет в студию или в офис)
    img 6311
    secretary "МИССИС БАКФЕТТ!!!"
    "ЭТО ВЫ?!?!"
    img 6312
    "О БОЖЕ!"
    #звук jump1
    img 6313
    w
    #подбегает и обнимает ее
    img 6314
    m "Привет, дорогуша!"
    "Не ожидала увидеть меня?"
    img 6315
    secretary "Миссис Бакфетт!"
    "Приходил страшный человек, он говорил страшные вещи про Вас!"
    "Что Вы сидели в тюрьме!"
    "Миссис Бакфетт! Скажите что это неправда!"
    img 6316
    m "Это неправда, дорогуша." #выделываясь как обычно
    "У меня были кое-какие проблемы, но я их решила."
    img 6317
    secretary "Это значит что Вы вернулись?!"
    "Как хорошо!!!"
    img 6318
    "Миссис Бакфетт!"
    "Пожалуйста!"
    "Выгоните того жуткого человека, который занял Ваш кабинет!"
    img 6319
    m "Что там за существо, дорогуша?!"
    "Как его зовут? Кто он?"
    img 6320
    secretary "Миссис Бакфетт! Его зовут Биф!"
    "Он занял Ваше место и..."
    "И делает какие-то непотребные вещи, Миссис Бакфетт!"
    "Просто ужасные!"
    img 6321
    m "Биф говоришь?!?!" #она его встретила внизу
    img 6322
    m "Хм... Дорогуша, видишь-ли..."
    "Я правда решила основную массу своих неожиданно возникших проблем..."
    "Но кое-что я еще не успела решить."
    "Тебе, скорее всего, придется потерпеть его еще немного."
    img 6323
    "Но я обещаю тебе что скоро я приду и выгоню всех!"
    "И этого негодяя что посмел занять мое место, пока меня не было!" #злая
    "И любых сотрудников, кто хоть как-то сотрудничал с ним во время моего отсутствия!"
    m "А сейчас, покажи мне где он сидит???"
    "Этот негодяй!"
    img 6324
    secretary "Миссис Бакфетт!"
    "Он сидит в Вашем кабинете!"
    "Прямо в Вашем кабинете, Миссис Бакфетт!"
    "(хмык)"
    img 6325
    m "Пойду побеседую с ним!"
    return

label monica_office_secretary_dialogue2:
    #render
    #Моника разговаривает с секретаршей повторно
    img 6326
    secretary "Миссис Бакфетт!"
    "Пожалуйста! Возвращайтесь скорее!"
    #если Моника сегодня не просила деньги, то появляется меню выбора
    menu:
        "Попросить деньги в долг.":
            img 6327
            m "Не переживай, дорогуша!"
            "Я скоро вернусь!"
            img 6328
            "..."
            "Кстати, дорогая..."
            img 6326
            secretary "Да, Миссис Бакфетт?"
            img 6329
            m "Скажи, у тебя не будет немного денег?"
            img 6326
            secretary "Миссис Бакфетт! Я пока не видела зарплаты здесь, после Вашего ухода..."
            #если у Моники меньше 5 долларов, то дает, иначе нет
            if money > 5:
                img 6330
                secretary "Поэтому у меня нет никаких денег сейчас, Миссис Бакфетт!"
                "Простите!"
                img 6331
                m "Ничего, дорогая, не бери в голову..."
            else:
                #
                img 6332
                secretary "У меня есть только кредитная карточка, но мне надо платить за ипотечный кредит."
                "У меня есть $ 5 наличными и все..."
                img 6333
                m "Дорогуша, дай мне, пожалуйста, эти $ 5..."
                img 6334
                secretary "Но Миссис Бакфетт! Зачем Вам какие-то $ 5?"
                "Я даже не понимаю, для чего?"
                img 6335
                m "Не бери в голову, дорогуша."
                "Я хочу купить кофе в автомате, а у меня нет мелочи..."
                "Карту я забыла дома..."

                secretary "Да, Миссис Бакфетт!"
                "Конечно, держите..."
                #дает 5 баксов


        "Уйти.":
            img 6336
            m "Не переживай, дорогуша!"
            "Я скоро вернусь!"

    return

label monica_office_photostudio_alex_dialogue1:
    #render
    #Моника разговаривает с Алексом в фотостудии (первый приход)
    img 6350
    w
    img 6351
    w
    img 6352
    alex_photograph "Миссис Бакфетт!"
    "Здравствуйте!"
    img 6353
    m "Здравствуй, Алекс..."
    img 6354
    alex_photograph "Миссис Бакфетт, Вас давно не было!"
    "У нас произошли большие изменения!"
    m "Я немного в курсе, Алекс..."
    img 6355
    alex_photograph "Миссис Бакфетт! Вы теперь будете у нас моделью?"
    "У меня много идей по поводу композиций с Вашим прекрасным видом!"
    img 6356
    m "Еще чего!"
    "Я не собираюсь сниматься ни в чем, пока не наведу порядок здесь!"
    img 6357
    alex_photograph "Да, Миссис Бакфетт! Конечно!"
    img 6358
    w
    return

label monica_office_cabinet_beef_dialogue1:
    #render
    #Моника разговаривает с Бифом первый раз. На столе сидит Мелани.
    #Мелани замечает Монику и выходит
    #подходит к Монике и здоровается
    img 6359
    w
    img 6360
    w
    img 6361
    w
    img 6362
    w
    img 6363
    w
    img 6364
    w
    #музыка Мелани zigzag
    img 6365
    w
    img 6366
    w
    img 6367
    w
    img 6368
    w
    img 6369
    w
    img 6370
    w
    img 6371
    w
    img 6372
    w
    img 6373
    w
    img 6374
    w
    img 6375
    w
    img 6376
    w
    img 6377
    w
    img 6378
    w
    img 6379
    w
    img 6380
    w
    img 6381
    melanie "Здравствуйте, Миссис Бакфетт!"
    #оглядывает ее вид (шлюха)
    img 6382
    "Рада видеть Вас!"
    img 6383
    m "Здравствуй, Мелани."
    img 6384
    "Я смотрю ты не теряешь времени даром..."
    img 6385
    melanie "Миссис Бакфетт..."
    #уходит
    img 6386
    w
    img 6387
    w


    #Моника наедине с Бифом
    img 6388
    beef "О! Цыпочка!"
    "Алекс клялся что не прятал тебя!"
    "Значит он, все-таки, врал и решил исправить свою вину прислав тебя ко мне?"
    "Ха-ха!"

    img 6389
    m "Это значит ты Биф?!"
    "Мерзавец!"
    "Как ты посмел занять мое место?!"

    img 6390
    beef "Эй! Цыпочка! Полегче!"
    "Ты кто такая?!"
    "Это у тебя такой косплей?"
    "Пытаешься произвести впечатление на меня?"
    "Ха-ха-ха!"

    img 6391
    m "Я - ТА, НА ЧЬЕМ СТУЛЕ ТЫ СИДИШЬ!"
    img 6392
    "МЕНЯ ЗОВУТ МОНИКА БАКФЕТТ!"
    img 6393
    "И Я БЫ СОВЕТОВАЛА ТЕБЕ ВСТАТЬ С МОЕГО СТУЛА!"
    img 6394
    "ПОКА Я НЕ ОТОРВАЛА ТЕБЕ ТВОИ ЯЙЦА К ЧЕРТЯМ!!!" #злая наезжает нагнувшись над столом

    img 6395
    beef "Ого!"
    "Это какая-то шутка?"
    "Должно быть ты самозванка?" #Биф озабочен
    img 6396
    "..." #у Бифа озарение, улыбается
    img 6397
    m "!!!"
    img 6398
    beef "Это отлично!"
    "У тебя так натурально получается играть!"
    "Цыпочка! Я думаю у меня есть для тебя работа!"
    img 6399
    m "Цыпочка?! Играть?!"
    "Что ты несешь, урод?!"
    "Мне нет резона играть саму себя!"
    "Вставай с моего стула!"
    "БЫСТРО!!!"

    img 6400
    beef "Нет, этого не может быть..."
    "Насколько мне известно, Моника Бакфетт - опасный преступник, которого ждет суровое наказание..."
    "Если это действительно Вы..."
    img 6401
    "Вы сбежали?!?!?"
    "Тогда я блокирую лифт и вызываю полицию..."
    img 6402
    "Пожалуйста! Пожалуйста! Не делайте мне ничего!"
    "Если хотите, садитесь на это кресло!"
    "Я представляю насколько Вы опасны!"

    img 6403
    m "Полиция???"
    img 6404
    mt "ЧЕРТ! КАКАЯ ПОЛИЦИЯ!!!"
    "ПОЧЕМУ ВСЕ ВРЕМЯ ПОЛИЦИЯ?!?!"

    img 6405
    beef "Алло! Полиция?!" #по телефону

    img 6406
    mt "Заблокировать лифт??? Полиция???"
    mt "ЧЕРТ!"
    mt "НЕТ!!!"

    img 6407
    mt "Мне надо что-то придумать! Как избежать полиции???"
    "..."
    "Я снова вляпалась!!!"
    "Думай, Моника!!!"

    img 6408
    beef "Полиция?! Я в опасности, помогите мне!"
    "Здесь опасная преступница!"
    "Она угрожает мне!"

    img 6409
    mt "ЧЕРТ!"
    "Как мне остановить его???"
    "..."
    img 6410
    "Он говорил что не верит что это я, и что я хорошо играю сама себя..."
    "Мне надо притвориться что это не Я!"
    "Надо расслабить его!"
    "Потом что-нибудь придумаю!"
    "А сейчас надо решить проблему, любой ценой!"
    "Иначе конец!"
    "Маркус будет очень рад заполучить меня с заявлением об угрозах от этого слизняка!"
    "О БОЖЕ!!!"
    img 6411
    m "Эй! Биф!" #Кокетливо встает
    "Не бойся!"
    "Ты правда здорово напугался?!"
    img 6412
    "Я - молодец, я провела тебя!"
    "Как тебе мой талант?"

    img 6413
    beef "???"
    "Так ты не Моника Бакфетт?"

    img 6414
    m "Конечно нет, глупый!"

    img 6415
    beef "Извините!" #кладет трубку
    img 6416
    "Черт, цыпочка!"
    "Ты так похожа на нее!"
    "Я действительно поверил!"

    img 6417
    "Иди ко мне на коленки, скорее!"
    "Надо пожалеть папочку!"

    img 6418
    m "Я... не собираюсь никуда садиться!"
    img 6419
    "Как ты вообще здесь оказался и кто ты такой?"

    img 6420
    beef "Я - Биф!"
    "Владелец Модного Журнала!"
    "Да - это Я"
    "Я - это Биф!"
    "Я люблю себя! Вау!"

    img 6421
    mt "СЛИЗНЯК!!!"

    img 6422
    beef "Так значит ты цыпочка от Алекса?"
    "А почему ты не хочешь ко мне на коленки?"
    "Ты ведь знаешь, детка, что с таким как я нужно дружить..."
    img 6423
    "Я ведь могу тебя сделать моделью, ты понимаешь?" #подмигивает

    img 6424
    mt "!!!"
    "СВОЛОЧЬ!!!"
    "ЕСЛИ БЫ НЕ ПОЛИЦИЯ, Я БЫ УБИЛА ЕГО ПРЯМО ЗДЕСЬ!!!"
    "ААААААААА!!!!"

    img 6425
    m "У меня нет желания становиться моделью!"

    img 6426
    beef "Я бы мог дать тебе работу, детка!"
    "Ты так похожа на Монику Бакфетт, что никто не увидит разницы!"
    "У меня крутой журнал и я решил сменить его курс!"
    "И если бы Моника Бакфетт одобрила его и рассказала бы всем об этом, то это был бы большой плюс!"
    img 6427
    "К тому же многие задают вопросы где эта сучка!"
    "А мне не всегда получается объяснить журналистам что она не должна интересовать их, потому что есть Я!"
    img 6428
    mt "!!!"
    "КТО Я???"

    img 6429
    mt "КАК МНЕ СДЕРЖАТЬСЯ???"
    "Я ХОЧУ ОТОРВАТЬ ЯЙЦА ЭТОМУ УРОДУ!!!"
    "ПРЯМО СЕЙЧАС!!!"
    img 6430
    "Но тогда я попаду в руки к Маркусу, сразу же!"
    "(хмык)"

    img 6431
    m "Меня не интересует твоя работа, Биф!"

    img 6432
    beef "Хорошо, цыпочка."
    "Зачем же ты тогда пришла сюда?"

    img 6433
    m "Я... Я пришла просто напугать тебя, Биф!"

    img 6434
    beef "Ха-ха-ха!"
    "У тебя крутой нрав, цыпочка!"
    "Смею заметить!"
    "Пытаешь произвести на меня впечатление, понимаю..."
    "Мне нравятся такие цыпочки!"

    img 6435
    mt "Я больше не могу выдерживать этого урода..."
    "У меня все кипит внутри!"
    "Мне стоит убраться отсюда!"

    #подходит и берет за подбородок
    #звук ходьбы
    img 6436
    with fadelong
    m "До свидания, Биф!"
    img 6437
    "Еще увидимся!"

    img 6438
    beef "До свидания, цыпочка!"
    "Я буду звать тебя Моника Бакфетт! Ха-ха-ха!"

    #Моника выходит

    mt "Это было..."
    "Очень..."
    "Сложно..."
    "Сдержаться и не прибить этого слизняка."
    "Обычно я подобных стираю в порошок за пару минут..."
    "А здесь..."
    "На моем кресле, за моим столом сидит этот Биф, а я ничего не могу сделать!"
    "Но я сделаю! Я верну себе эту компанию!"
    "И первое что я сделаю - это выкину этого Бифа!!!"
    "Он будет разносить газеты всю свою оставшуюся жизнь!!!"
    "Или флаеры!!! Да!!!"
    "Клянусь!!!"

    return

label monica_office_cabinet_beef_dialogue2:
    #Моника пытается пойти в кабинет Бифа после разговора первого дня
    mt "Я не собираюсь идти к этому слизняку!"
    "Если я приду к нему снова, то только затем, чтобы выкинуть его отсюда!!!"
    return

label monica_office_photostudio_melanie_dialogue1:
    #render
    melanie "Миссис Бакфетт!"
    "Еще раз, рада Вас видеть!"
    m "Да, Мелани, я тоже рада."
    "Как тебе твой новый Босс?"
    melanie "Такой же Босс как и все, Миссис Бакфетт."
    m "И что, тебя он устраивает?"
    melanie "Миссис Бакфетт, я уверена в своих силах..."
    menu:
        "Да, я примерно понимаю в чем заключаются они, твои силы...":
            m "Да, я примерно понимаю в чем заключаются они, твои силы..."
            mt "Конечно, со мной у нее эти фокусы не проходили..."
            melanie "Миссис Бакфетт... Вы выглядите потрясающе." #осматривает Монику (whore)
            "Ваш вкус настолько изыскан, что недоступен моему пониманию..."
            mt "Сучка!"
            "Я понимаю что такой Босс как сейчас тебе кажется лучше."
            "Но поверь, я скоро вернусь на свое место..."
            melanie "Я была бы очень рада этому, Миссис Бакфетт..."
        "Мелани, ни один мужчина не устоит перед тобой!":
            m "Мелани, ни один мужчина не устоит перед тобой!"
            "Я понимаю что такой Босс как сейчас тебе кажется лучше."
            "Но поверь, я скоро вернусь на свое место..."
            melanie "Спасибо..."
            melanie "Я была бы очень рада этому, Миссис Бакфетт..."
    return



label monica_office_secretary_dialogue3:
    #render
    #Моника разговаривает с секретаршей когда приходит получать работу. (срабатывает даже если Моника идет в студию или в офис)
    img 6337
    secretary "Миссис Бакфетт!!!"
    "Пожалуйста, помогите мне!"
    img 6336
    m "Дорогая, что случилось?"
    img 6338
    secretary "Эти люди..."
    "Они требуют от меня делать такие вещи..."
    "Я не могу, Миссис Бакфетт!"
    "Вы ведь знаете мои моральные принципы!"
    "А здесь творится... ТАКОЕ!!!"
    "Они говорят что если я не буду слушаться, то потребуют срочный возврат всех кредитов, которые мне выдавала компания!"
    "А если я их быстро не верну, то они посадят меня в тюрьму!"
    img 6339
    "Миссис Бакфетт, вы представляете себе???"
    "Пожалуйста, помогите мне!"
    "Выгоните этих людей скорее, пожалуйста!"
    img 6340
    mt "Вот мерзавцы!!!"
    "Что они тут вытворяют пока меня нет?!?!"
    "Мне надо скорее возвращать все назад!"
    img 6341
    m "Дорогая, не беспокойся!"
    "С тобой ничего не сделают, я даю слово!"
    "Скоро я вернусь и все будет как прежде!"
    img 6337
    secretary "Миссис Бакфетт! Возвращайтесь скорее, прошу ВАС!!!"

    return

label monica_office_secretary_dialogue4:
    #Моника разговаривает с секретаршей когда приходит получать работу, но еще не пятница.
    #render
    img 6342
    secretary "Миссис Бакфетт!"
    "Мистера Бифа сейчас нет на месте!"
    img 6343
    m "Когда он будет?"
    img 6344
    secretary "Он сказал что будет в пятницу!"
    "Но Вы знаете, он говорит что хочет и совершенно не обладает дисциплиной!"
    img 6343
    m "Хорошо, дорогая, спасибо."
    return


label monica_office_cabinet_beef_dialogue2a:
    #render
    #Моника заходит в кабинет Бифа, второй раз, для разговора о работе
    img 6439
    mt "Ну что-ж... Биф..."
    mt "Поговорим с ним о том чтобы получить работу..."
    img 6440
    "Посмотрим что он хочет от меня..."
    "Если я хочу вернуть назад компанию, то мне стоит находиться где-то здесь, рядом..."
    "А работа - это хороший повод..."
    "Тем более что у меня нет больше никаких идей где взять деньги для Дика..."
    "Так что я могу достигнуть двух целей сразу!"

    return

label monica_office_cabinet_beef_dialogue3:
    #render
    #Моника разговаривает с Бифом второй раз, уже о работе.
    img 6441
    beef "О! Цыпочка! Ты вернулась!"
    img 6442
    m "Биф!"
    "Что ты говорил по поводу работы?"
    img 6443
    beef "По поводу работы?"
    "Хм... Ты знаешь..."
    "Я хотел чтобы ты снималась для журнала под видом Моники Бакфетт..."

    #если с Мелани отношения хорошие
    img 6444
    "Но я думаю что предпочту Мелани на эту роль."
    "Хотя она и отзывалась о тебе хорошо."
    "Похоже что вы откуда-то знакомы..."

    #если с Мелани отношения плохие
    img 6444
    "Но когда Мелани узнала об этом, то она убедила чтобы я оставил ее..."
    "Она боится что ты займешь пъедестал вместо нее."
    "Она такая каръеристка..."
    "Ха-ха-ха!"

    img 6445
    m "Я лучше Мелани!"
    img 6446
    beef "Ха-ха-ха!"
    "Конечно лучше! Ведь ты похожа на Монику Бакфетт!"
    img 6447
    m "Послушай, Биф!"
    "Да, Мелани топ модель."
    "Но ты говорил что хочешь сменить курс журнала."
    img 6448
    "И что тебе очень помогло бы, если бы сама Бакфетт объявила об этом!"
    img 6449
    beef "Хм..."
    "Возможно ты права..."
    "Пресса пока не пронюхала про то что Бакфетт сидит в тюрьме."
    "И я бы не хотел чтобы это случилось очень скоро."
    img 6450
    "Такая говорящая кукла как ты мне бы очень пригодилась..."
    img 6451
    mt "!!!"
    "НЕНАВИЖУ!!!"

    img 6452
    beef "Так что я предлагаю тебе сделать серию фотосессий, посвященную смене курса журнала."
    "За каждую фотосессию я предлагаю тебе $ 1.000."
    "К тому же, думаю, можно будет оборудовать офис для тебя, чтобы ты могла общаться с прессой."
    "А также с партнерами журнала."
    "Я смогу продавать твое личико."
    "Какое-то время."

    img 6453
    m "$ 5.000!!!"
    img 6454
    mt "Отлично! Я смогу находиться здесь..."
    "Это будет началом моего плана по возвращению компании!"

    img 6455
    beef "Что ты имеешь ввиду под $ 5.000?"

    img 6456
    m "$ 5.000 за каждую фотосессию!"
    img 6457
    beef "А ты весьма амбициозна для цыпочки с улицы!"
    img 6458
    "Судя по твоему виду, ты делаешь минет за $ 10!"
    "Не слишком-ли быстрый рост для какой-то шлюхи?"

    img 6459
    mt "!!!"
    mt "Каждый раз когда я общаюсь с ним, я хочу убить его!"

    img 6460
    beef "Тем более тебя будет окружать пресса, поклонники!"
    "Я уверен ты не испытывала и доли той славы, что имела сучка Бакфетт!"

    img 6461
    mt "Испытывала! Я и есть она!!!"
    "А ты - никто! И время докажет это!!!"

    img 6462
    m "Я не думаю что ты найдешь другую модель, которая больше похожа на Миссис Бакфетт чем я!"
    "Так что я ухожу! А ты хорошенько подумай!"
    #начинает уходить

    img 6463
    beef "Окей, цыпочка!"
    "Когда-нибудь увидимся!"
    img 6464
    w
    img 6465
    w
    img 6466
    m "Что? Ты не будешь останавливать меня?"
    img 6467
    beef "Конечно нет!"
    img 6468
    mt "!!!"
    img 6469
    beef "Ладно! Цыпочка!"
    "Я дам тебе $ 5.000!"
    "Но я не обещаю тебе их регулярно!"
    "Я посмотрю еще стоишь-ли ты этих денег!"
    img 6470
    mt "!!!"
    img 6471
    beef "Итак, ты согласна?"
    m "Да, я согласна..."

    img 6472
    beef "Отлично!"
    "Если честно, Мелани отказалась от этой серии фотосессий."
    "Она сказала что не хочет иметь ничего общего с полным обнажением."
    img 6473
    "Хорошо что мне подвернулась такая цыпочка как ты, которая не имеет проблем с этим!"
    img 6474
    m "С чем общего??? С ОБНАЖЕНИЕМ?!?!?"
    img 6475
    beef "Ну да, этот журнал слишком скучный!"
    "Сейчас такое уже не модно."
    "Деньги приносит что-нибудь погорячее!"
    img 6476
    m "Я не собираюсь раздеваться ни за какие деньги!!!"
    "До свидания!!!"
    img 6477
    beef "Если передумаешь, заглядывай!"
    return

label monica_office_secretary_dialogue5:
    #Моника выходит в локацию секретарши
    mt "ЧТО ОНИ СОБРАЛИСЬ СДЕЛАТЬ С МОИМ ЖУРНАЛОМ?!?!"
    mt "Полное обнажение???"
    "И этот мерзавец еще и предлагает МНЕ это сделать?!"
    "МНЕ - МОНИКЕ БАКФЕТТ!!!"
    "ОБНАЖАТЬСЯ В СВОЕМ ЖЕ ЖУРНАЛЕ?!?!"
    "Моника!"
    "Это все слишком далеко зашло!"
    "Тебе надо как-то скорее разобраться со всем этим!"
    "Эти мерзавцы, которые меня окружают..."
    "Как же мне выпутаться и сохранить достоинство?!"
    "..."
    "Дик... Сегодня пятница..."
    "Если сегодня вечером не будет денег, то мне конец..."
    "Что же мне делать???"
    "Он сказал серия фотосессий..."
    "Плавная смена курса журнала..."
    "Мне нужна всего одна фотосессия."
    "Мне нужны эти гребаные $ 5.000!"
    "Я отнесу их Дику, мы купим ему галстук и он перестанет шантажировать меня..."
    "Он всего-лишь хочет доказательство моей лояльности."
    "Если я докажу ему что я ему друг, то он изменит отношение ко мне..."
    "Он придумает как вернуть мне документы и деньги..."
    "Я уверена он знает как это сделать, но проверяет меня..."
    "..."
    "Итак, одна фотосессия..."
    "Мне надо убедить этого негодяя сделать одну нейтральную фотосессию..."
    "Безобидную."
    "Тем более будет полезно миру напомнить о себе..."
    "Я надеюсь за это Маркус не заберет меня?"
    "Нет, не должен..."
    "Мне надо успеть!!!"

    return

label monica_office_cabinet_beef_dialogue4:
    #render
    #Моника разговаривает с Бифом третий раз.
    img 6478
    beef "О! Цыпочка! Ну как, ты надумала?"
    img 6479
    m "Биф! Ты сказал это будет серия фотосессий..."
    "Ты предлагаешь мне обнажаться сразу или постепенно?"
    img 6480
    beef "Конечно постепенно, цыпочка!"
    "Аудитория журнала не примет слишком быстрых перемен..."
    "Мы начнем с начала и закончим чем-то очень горячим."
    "Тебе понравится!"
    "Ха-ха-ха!"
    img 6481
    beef "Ну что, ты согласна?"
    menu:
        "Согласиться.":
            pass

        "Отказаться.":
            img 6482
            m "Я еще подумаю, Биф!"
            return

    img 6483
    m "Хорошо, Биф!"
    "Но только при условии того что мне не надо раздеваться на первой же фотосессии!"
    img 6484
    beef "Конечно, цыпочка!"
    "Перед камерой тебе раздеваться не придется в этот раз!"
    "Только передо мной!"

    img 6485
    m "ЧТО?!?!"

    img 6486
    beef "Ха-ха-ха!"
    beef "Когда я пришел сюда, то обнаружил несколько забавных традиций!"
    "Одна из них - это осмотр модели перед съемками!"
    img 6487
    "Модель должна раздеться передо мной и продемонстрировать свои навыки!"

    m "ЧТО?!?!"

    img 6488
    mt "ЧЕРТ! Я ЗАБЫЛА ПРО ЭТО!"
    "Но это же были мои шалости..."
    "Причем здесь этот Биф и Я?!?"

    img 6489
    m "Биф... Я..."
    "Я думаю это необязательно, ведь правда?!"

    img 6490
    beef "Ха-ха-ха!"
    "Детка! Смею тебя огорчить!"
    img 6491
    w
    img 6492
    "Тебе придется это сделать в следующий раз!"
    "Так как уже нет на это времени!"
    "Сегодня будет небольшой благотворительный вечер, посвященный моему журналу."
    "Я хочу чтобы ты сделала фотосессию и поехала со мной."
    "Там тебе надо будет сказать небольшую речь о смене курса нашего журнала."

    img 6493
    m "Мне? Речь?!"
    "Ты хочешь чтобы я сама заявила об этом?!"

    img 6492
    beef "Конечно! Как я и говорил!"
    "Ты очень похожа на Монику Бакфетт!"
    img 6494
    "Потому я и держу такую цыпочку как ты!"

    img 6495
    "При этом там будет вкусная еда и дорогое вино!"

    img 6496
    m "Это... После фотосессии?"

    img 6497
    mt "Вкусная еда... дорогое вино..."
    "Благотворительный вечер..."
    "Черт... Как же я соскучилась по этому!!!"
    img 6498
    "Это и есть мой образ жизни, а не то чем мне приходится заниматься сейчас..."
    "По какому-то небольшому недоразумению..."

    img 6499
    beef "Да! Детка!"
    "И тебе стоит поторопиться!"
    "Не переживай!"
    "Ты покажешь мне свою попку в следующий раз!"

    img 6500
    mt "УБЛЮДОК!!!"
    m "Мне идти в фотостудию?"
    beef "Да! Детка!"

    img 6501
    "Беги! И повиляй попой!"
    img 6502
    w

    return

label monica_office_secretary_dialogue6:
    #Моника пытается зайти в кабинет к Бифу или выйти из офиса до конца фотосессии
    mt "Мне надо идти в фотостудию..."
    return

label monica_office_photostudio_alex_dialogue2:
    #render
    #Моника разговаривает с Алексом в фотостудии (фотосессия)
    alex_photograph "Миссис Бакфетт!"
    "Мистер Биф сказал что мне надо провести фотосессию с Вами!"
    "Вы будете участвовать?"
    menu:
        "Да, буду...":
            pass
        "Пока нет...":
            m "Пока нет..."
            return

    m "Да, буду..."
    "Что мне одеть?"
    "Я ведь не буду сниматься в этом?!"

    alex_photograph "Это была бы замечательная идея!"
    "К сожалению, Мистер Биф сказал одеть то платье, в котором Вы снимались в прошлый раз!"
    "Но я бы попросил Вас сначала сделать несколько кадров в этом наряде!"
    "Он Вам очень идет, у Вас потрясающий вкус!"

    m "Ты издеваешься?!"

    alex_photograph "Но Вы бы иначе не надели его, так ведь?"

    m "Ну... Вообще-то да..."
    "Это мой маленький эксперимент."
    "Но я бы пока не хотела широко освещать его."
    "Поэтому Алекс... Не надо делать никаких лишних кадров, хорошо?"

    alex_photograph "Как скажете, Миссис Бакфетт!"

    "Вы можете переодеться, все готово!"

    menu:
        "Переодеться.":
            pass
        "Уйти.":
            return

    #переодевание

    alex_photograph "Вы выглядите потрясающе, Миссис Бакфетт!"
    m "Спасибо, Алекс..."

    m "Но я уже снималась в этом платье..."
    "Думаешь будет уместно делать две одинаковые фотосессии в одном и том же?"

    alex_photograph "Это РАЗНЫЕ фотосессии, Миссис Бакфетт!"

    alex_photograph "Начинайте, позировать!"
    "Мотор!"

    #фотосессия Моники обычная

    alex_photograph "Миссис Бакфетт! Сядьте, пожалуйста, на этот стул!"
    m "Зачем?"
    alex_photograph "Я фотограф! Я вижу композицию со стороны!"
    m "Ладно..."

    #фотосессия Моники со стулом

    alex_photograph "Миссис Бакфетт! Сядьте, пожалуйста, вот так..."
    #сажает Монику в развратную позу
    m "Алекс! Я не собираюсь сниматься в такой позе!"
    "Ты сошел с ума?!?"

    alex_photograph "Миссис Бакфетт! Это необходимо!"

    m "Алекс! Ты, кажется, давал слово что больше не будешь брать подобные ракурсы!"
    alex_photograph "Да, Миссис Бакфетт! Я давал слово что буду делать как скажет Босс!"

    m "А кто твой Босс?!"

    alex_photograph "Мистер Биф! И он сказал мне брать все возможные ракурсы!"

    mt "Вот сволочь!"
    m "Я не буду так сниматься!"
    m "Мы закончили фотосессию! Хватит и того что снято!"

    alex_photograph "Миссис Бакфетт!"
    "Тогда я вынужден сообщить Мистеру Бифу о срыве фотосессии..."

    m "Мы сделали достаточно кадров!"

    #если Моника зла к Алексу
    alex_photograph "Мы не сделали самого главного, Миссис Бакфетт."
    "Но я имею права настаивать..."
    "Я сообщу Мистеру Бифу..."
    mt "ЧЕРТ! НЕ ХВАТАЛО ЕЩЕ СРЫВА ФОТОСЕССИИ!!!"
    "Это значит что Биф не даст мне деньги..."
    "И я не поеду на благотворительный вечер..."
    "А я так хочу туда!"

    #если Моника добра к Алексу
    alex_photograph "Миссис Бакфетт!"
    "Я знаю что Вы цените меня как профессионала."
    "И я понимаю что Вы не хотите делать эти кадры..."
    "Но это приказ Мистера Бифа."
    "Если я ослушаюсь, то меня уволят!..."


    m "Хорошо, Алекс."
    "Давай сделаем пару кадров, но постарайся брать ракурсы поприличнее, хорошо!"

    "Хорошо, Мэм!"
    "Как скажете!"

    #Идет фотосессия с пошлыми ракурсами

    alex_photograph "Мы закончили, Мэм!"
    "Хотите переодеться назад?"

    mt "Вот еще! Теперь это мое платье!!!"
    "Я не собираюсь переодеваться в те тряпки!"
    "Ни за что!"

    m "Нет, Алекс."
    "Мне понравилось это платье, я оставлю его."

    alex_photograph "Но Мэм..."
    "Это реквизит фотостудии и..."

    m "Алекс, достаточно."

    alex_photograph "Мэм..."

    mt "Итак, надо вернуться к Бифу..."

    return

label monica_office_secretary_dialogue7:
    #Моника обращается к секретарше одетая в платье
    img 6345
    secretary "МИССИС БАКФЕТТ!!!"
    "Вы бесподобны в этом платье!"
    img 6346
    "Вы займете свой кабинет с завтрашнего дня?"
    img 6347
    m "Хм... Дорогая..."
    "Может быть не с завтрашнего, но скоро..."
    "Обещаю тебе!"
    img 6348
    secretary "Спасибо, Миссис Бакфетт!"
    "Я жду! Эти люди... они..."
    "Они угрожают мне и..."
    img 6349
    m "Я знаю, дорогая, подожди немного..."
    img 6348
    secretary "Да, Миссис Бакфетт!"
    "Я жду ВАС!"

    return


label monica_office_cabinet_beef_dialogue5:
    #render
    #Моника разговаривает с Бифом после фотосессии.
    m "Биф!"
    "Я закончила фотосессию!"
    "И я жду свои деньги..."
    beef "О! Цыпочка!"
    "Сообщи моей секретарше свои реквизиты и деньги будут переведены в течении..."
    "Ну... Может быть месяца..."

    m "ЧТО???"
    "МНЕ НУЖНЫ ДЕНЬГИ СЕЙЧАС, ПРЯМО СЕЙЧАС!"

    beef "Банки уже не работают, детка!"

    m "Биф!"
    "Мне нужны деньги! Сейчас же!"
    "Иначе можешь забыть про речь, которую я должна сказать на благотворительном вечере!"
    "Я просто уйду!"

    beef "Детка, я сказал, что банки уже не работают!"

    m "Мне нужны наличные, Биф!"
    "И прямо сейчас!"

    beef "Ха-ха-ха!"
    "Какой темперамент!"

    beef "Хорошо!"
    "Если ты уйдешь сейчас, то я не успею посмотреть на твою голую попку!"
    "Я заплачу тебе наличными, но только после речи на благотворительном вечере!"

    m "Я не верю тебе! Какие гарантии, Биф?!"

    beef "Гарантии???"
    "Ты знаешь, что расчет наличными сам по себе является незаконным!"

    "Ты хочешь чтобы я заплатил тебе деньги без оформления бумаг и еще хочешь каких-то гарантий?!"
    "Мои гарантии - это твой ротик!"
    "Он должен говорить то что скажу я и только тогда ты получишь свои деньги!"

    m "Биф, если я скажу речь, я получу деньги?"
    beef "Конечно, цыпочка!"
    "Я понимаю, ты стесняешься."
    "Но не переживай, это небольшой вип зал, там будет мало людей."
    "В основном пресса."

    "Я же не рассчитывал что найду такую цыпочку!"
    "В следующий раз я позабочусь чтобы мою новую куклу увидели все!"

    mt "!!!"

    beef "Поехали, детка!"
    "Уже пора!"
    "И не забудь вернуть платье назад после вечера!"

    m "Я оставлю это платье себе! Оно мое!"

    beef "Нет! Даже не обсуждается!"
    "Я не позволю чтобы шлюха за $ 10 ходила сниматься в платье от Модного Журнала!"
    "А вдруг кто-нибудь узнает это платье?!"
    "Что тогда?!"

    m "Я поставлю пятно на него!"

    beef "Только попробуй!"
    "И тогда твой гонорар пойдет на погашение стоимости платья!"

    mt "!!!"

    beef "Закрой свой ротик, пока я не заткнул его своим членом!"
    "Ты будешь открывать его когда скажу Я!"
    "А сейчас поехали!"

    mt "!!!"
    return
    #
