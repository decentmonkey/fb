label monica_rich_hotel_entrance:
    #render
    #Идет Биф, Моника, Мелани, стоит администратор на рецепшине
    img 6659
    w
    img 6660
    w
    img 6661
    beef "Добрый вечер!"
    "Я веду этих цыпочек на благотворительный вечер!"
    img 6662
    reception "Добрый вечер!"
    img 6663
    reception "Проходите, господа!"
    "Мы Вам рады!"
    img 6664
    w
    img 6665
    w
    #Смотрят друг на друга
    img 6666
    w
    img 6667
    w
    img 6668
    reception_t "Эта шлюха???"
    img 6669
    w
    img 6670
    "Что она делает здесь???"
    img 6671
    w

    img 6672
    with fadelong
    mt "Ну что, сучка, получила???"
    "Убедилась что Я - Леди!"
    "А ты - никто!"

    return

label monica_charity_event_dialogue1:
    #render
    #Моника, Биф, Мелани заходят в зал, их встречает hotel staff
    #звук лифта
    img 6673
    hotel_staff "Дорбый вечер, господа!"
    "Пожалуйста, проходите!"
    img 6674
    "Все уже готово!"
    "Все давно ждут!"

    img 6675
    beef "Ты все подготовил?"
    "Хороший мальчик!"

    img 6676
    beef "Моника, Мелани! Быстро на сцену!"
    "Отрабатывайте свои деньги!"

    img 6677
    mt "Я не поняла! Это что еще такое?!"
    img 6678
    "Почему мой постер завешен одеждой?!?!"
    return

label monica_charity_event_dialogue2:
    #render
    #Моника, Биф, Мелани стоят на сцене и говорят речь
    img 6679
    beef "Господа!"
    "Я рад приветствовать Вас на этом благотворительном вечере!"

    img 6680
    mt "Мелани?! Здесь?!"
    "А почему не Я?!"

    img 6681
    beef "Как Вы знаете, наш журнал является законодателем Моды!"
    "Это самое авторитетное издание из всех подобных!"

    img 6682
    "Мы прошли долгий путь вместе с Вами!"
    "Каждый год, каждый выпуск мы осмысливали новые идеи!"
    "И открывали для себя новые горизонты!"

    img 6683
    "Все имеет свое начало и имеет свой финал!"
    "Сегодня я хочу объявить Вам о том что долгий путь закончен!"
    img 6684
    "Мода больше не является краеугольным камнем нашего творчества!"

    #ропот зала
    w
    img 6685
    "Но, всегда, когда что-то старое заканчивается, что-то новое начинается!"
    "Мы открыли для себя, что все что мы делали с помощью моды..."
    "...Это раскрывали женскую красоту!"
    "Но женская красота сама по себе является ценностью!"
    "Она неподвластна моде и времени!"
    "В любые времена женские линии ценились выше любых других ценностей этого мира!"
    "Это отражено в живописе и поэзии!"

    img 6686
    "Потому новый курс журнала будет направлен на женское тело!"
    "Мы видим в этом огромный потенциал!"
    img 6687
    "И, хоть многие с нами пока не согласны, я уверен что они придут к выводу что мы были правы!"
    img 6688
    "Наши конкуренты последуют за нами!"

    img 6689
    "Многие не верят в то что мы и правда решились на столь серъезный шаг!"
    "Потому я предоставляю слово лицу Модного Журнала..."
    "Монике Бакфетт!!!"
    img 6690
    w
    #восторженный ропот зала
    img 6691
    w

    img 6692
    beef "Ну, давай кукла!"
    "Притворись Моникой Бакфетт!"

    img 6693
    "Помни, что микрофон - это не член!"
    img 6694
    "Ты привыкла сосать члены, но сюда надо говорить!"

    img 6695
    m "Я знаю, Биф!"
    "Заткнись!"

    #уход на сцену где Моника стоит

    #нажатие на Бифа
    img 6697
    beef "Ну, давай кукла!"
    "Притворись Моникой Бакфетт!"
    img 6698
    "Или тебя надо шлепнуть по попке, чтобы ты заговорила?!"

    #нажатие на Мелани
    img 6699
    mt "Мелани смотрит на меня."
    "Интересно что она думает обо всем этом..."

    #нажатие на Монику
    img 6696
    m "..."
    img 6700
    mt "Черт! Что же мне делать?!"
    "Здесь столько прессы..."
    "Может быть объявить что мой журнал захватили?!"
    "Попросить помощи?"
    "Это опасно! Не представляю чем это может грозить!"
    "Возможно самым худшим... Но это единственный шанс..."
    "Очень рискованный!"
    "Что же мне делать???"
    menu:
        "Сказать всем правду!":
            img 6701
            m "Я - Моника Бакфетт!"
            "И я хочу объявить о преступлении, которое совершено в отношении меня!"
            img 6702
            empty_name "Выключается микрофон."
            img 6703
            "Меня незаконно обвинили в том, чего я не совершала!"
            "У меня отняли счета и документы!"
            "И теперь шантажируют, заставляя говорить немыслимые вещи!"
            "Помогите мне!!!"
            #затемнение. спустя несколько часов

            marcus "Что-ж, Миссис Бакфетт!"
            "Хорошая попытка!"
            "Должен признать Вам что я проиграл."
            m "..."
            marcus "Да, я проиграл лучший виски на моем ранчо!"
            "Вы продержались больше одного дня!"
            "И Вы вернулись сюда... Феерично!"
            "Вы отправитесь на Ранчо прямо из этого кабинета..."

            m "НЕЕЕЕЕТ!!!"
            # конец игры
            return

        "Подыграть Бифу. Если я хочу все вернуть назад, то надо быть хитрее...":
            mt "Нет, это слишком рискованно!"
            "Дик говорил что все что со мной сделали - законно."
            "А это значит что я лишь наврежу себе!"
            "Мне надо сказать эти гребаные слова и заработать деньги на чертов галстук!"

            img 6704
            m "..."
            m "Я - Моника Бакфетт!"
            "И я подтверждаю слова Мистера Бифа!"
            "Наш журнал изменит свой курс!"

            #ропот в зале
            img 6705
            m "..."
            beef "Ну, курица! Скажи что-нибудь еще!!!"

            img 6706
            mt "!!!"

            img 6707
            m "Старый курс морально устарел..."
            "Новые времена диктуют новые тренды..."
            img 6708
            "Я благодарна Мистеру Бифу за новые идеи..."
            "Наш журнал должен преобразиться..."
            "Спасибо Вам за то что Вы пришли..."

            img 6709
            beef "Молодец, цыпочка!"
            "Продолжай играть!"

            #появляется рецепшин и смотрит на Монику
            img 6710
            reception_t "Не понимаю..."
            "Она выступает на сцене..."
            img 6711
            "Неужели она правда Леди?"
            "Но этого не может быть!"
            img 6712
            "Мое чутье никогда не обманывало меня!"

            #меняется фон, Моника внизу отвечает на вопросы журналистов
            img 6713
            with fadelong
            reporter1 "Миссис Бакфетт!"
            "Скажите! Почему Вы решили сменить курс?"
            reporter2 "Скажите! Вы готовы поддержать новый курс собственным примером?"
            reporter3 "Мы слышали что Вы только что провели фотосессию!"
            "Вы решили сняться обнаженной?"
            img 6714
            m "Нет, что вы?"
            "Это всего-лишь курс журнала!"
            "Я не собираюсь сниматься обнаженной!"
            "Я - Леди!"
            "И у меня есть достоинство!"
            img 6715
            with fadelong
            reporter1 "Но мы слышали что это необычная фотосессия!"
            "Мы слышали что эта фотосессия достаточно смелая!"
            reporter3 "Расскажите про фотосессию, Миссис Бакфетт!"
            img 6716
            m "Ой! Что Вы? Это обычная фотосессия!"
            reporter2 "Мы слышали что вы принимали необычные позы!"
            img 6717
            m "Ничего особенного..."
            "Просто небольшой смелый эксперимент..."
            img 6718
            reporter1 "Собираетесь-ли Вы продолжать эксперименты?"
            reporter3 "Многие хотели-бы увидеть больше!"
            img 6719
            m "Нет..."
            "Это разовый случай..."
            "Скажите этим МНОГИМ что они могут не рассчитывать на большее!"
            "Интервью закончено!"
            reporter1 "Спасибо, Миссис Бакфетт!"

    return


label monica_charity_event_dialogue3:
    #Моника стоит в зале. Также стоит Филип и Hotel Staff. Моника может подойти к вешалке, которая закрывает постер.
    mt "Все!"
    "Я сказала что хотел этот мерзавец Биф!"
    "Надо идти узнать про деньги!"
    return


label monica_charity_event_dialogue4a:
    #Моника пытается выйти в туалет или на выход
    mt "Я не собираюсь уходить пока не получу деньги от Бифа!"
    return

label monica_charity_event_dialogue4:
    #render
    #Моника разговаривает с Бифом. Рядом сидит Мелани
    img 6720
    m "Биф!"
    "Ты удовлетворен выступлением?"
    beef "Да, цыпочка!"
    "Ты хорошо поработала!"

    img 6721
    m "Биф, ты ничего не забыл?"
    beef "Что ты имеешь ввиду?"

    img 6722
    m "Я про нашу договоренность, Биф!!!"

    img 6723
    beef "Ах! Про это!"
    "У меня нет с собой наличных, детка!"
    "Мне их скоро привезут."
    img 6724
    m "Насколько скоро?"

    img 6725
    beef "В течении часа."
    "Ты пока можешь расслабиться и выпить вина."

    img 6726
    m "Хорошо, Биф."
    "Я подожду..."
    return


label monica_charity_event_dialogue5:
    #render
    #Моника разговаривает с Бифом снова (денег еще нет). Рядом сидит Мелани
    beef "Мне пока не привезли деньги, детка!"
    "Расслабься, выпей вина!"
    return

label monica_charity_event_dialogue6:
    #render
    #Моника разговаривает с Hotel Staff
    img 6767
    hotel_staff "Мэм!"
    "Хорошего вечера!"
    "Надеюсь Вам все нравится!"

    img 6768
    m "Это ты отвечаешь за порядок здесь???"

    img 6769
    hotel_staff "Да, Мэм!"

    img 6770
    m "Почему мое изображение закрыто каким-то хламом?"
    "Кто за это отвечает?!?"

    img 6771
    hotel_staff "Мэм! Простите!"
    "За это отвечаю я, Мэм!"

    "Мне сказали повесить этот постер, но другого места, к сожалению, не нашлось и..."

    img 6772
    m "Мне плевать на место!"
    "Ты в курсе кто изображен на этом постере?!"

    hotel_staff "Я точно не знаю, Мэм! Я..."

    img 6773
    m "НА НЕМ ИЗОБРАЖЕНА Я!!!"

    m "А ты знаешь кто Я???"


    hotel_staff "Вы - Моника Бакфетт, Мэм..." #испуганно

    m "Верно! И не только!"
    menu:
        "Я - та кто уволит тебя за этот проступок!":
            img 6774
            m "Я - та кто уволит тебя за этот проступок!"
            "Ты - мелкий червь, который не понимает величия таких людей как Я!"
            "Можешь считать что ты уже не работаешь здесь!"
            img 6775
            mt "Я поговорю с Бифом! Вместе мы уволим этого недоноска!"
            mt "Ах! Как прекрасно снова чувствовать власть!"
            img 6776
            hotel_staff "Мэм! Простите!"
            "Пожалуйста, не надо!"
            "Я постараюсь все исправить!"
            img 6777
            m "Ты уже упустил свой шанс, мальчик!"
            "Такие люди как я - они не дают второй шанс!"
            "Ты - никчемный бесполезный людишка и не заслуживаешь обслуживать такие мероприятия как это!"
            img 6778
            hotel_staff "..." #жалобный

        "Я понимаю. У тебя много забот...":
            img 6779
            m "Ладно... Я понимаю что у тебя много забот."
            "От тебя требуют многого, а здесь действительно нет больше места..."
            img 6780
            hotel_staff "Мэм! Спасибо что меня понимаете!"
            img 6781
            mt "В конце концов я не в том положении чтобы еще кого-то увольнять..."

    return

label monica_charity_event_dialogue7:
    #render
    #Моника разговаривает с Hotel Staff повторно

    #если Моника нагрубила
    img 6782
    hotel_staff "Мэм! Пожалуйста!"
    "Прошу Вас передумать!"
    m "Я не передумаю, мальчик!"

    #если Моника пожалела
    img 6783
    hotel_staff "Мэм! Прошу прощения!"
    "В следующий раз такого не повторится!"
    return


label monica_charity_event_dialogue8:
    #render
    #Моника знакомится с Филипом
    img 6784
    philip "Добрый вечер, Миссис Бакфетт!"
    "Разрешите представиться? Меня зовут Филип."
    "Позвольте мне угостить Вас вином?"

    img 6785
    mt "Фи! Очередной прилипала!"
    "Надо отшить его!"
    "..."
    "Хотя..."
    "Угостить вином..."
    "Почему бы и нет..."
    "По крайней мере он выглядит богатым..."

    img 6786
    m "Добрый вечер, Филип!"
    "Хорошо... Я позволю тебе угостить меня."
    "Куда ты хочешь пригласить такую даму как Я?"
    img 6787
    philip "Я бы хотел пригласить такую прекрасную даму за столик!"
    m "Хорошо, пойдем..."

    #сидят за столиком

    img 6788
    #звук наливаемого вина
    philip "Мэм! Позвольте я налью Вам вина!"

    img 6789
    m "Итак, Филип..."
    "Расскажи о себе..."
    "Чем ты занимаешься?"

    img 6790
    philip "О, Мэм! Я занимаюсь живописью и антиквариатом!"
    m "Что привело тебя к такому занятию?"

    img 6791
    philip "Мэм! Я люблю вино!"
    "А вино - это продукт, который со временем становится дороже!"
    "К сожалению, время летит быстро и все остальные вещи теряют ценность!"
    "Чего не скажешь про живопись или антиквариат!"

    img 6792
    #до этого вино переделать!
    m "А женщины?"
    img 6793
    philip "Я также очень люблю женщин, Мэм!"

    img 6794
    m "Но как же, на женщин время оказывает влияние, в отличие от живописи..."

    img 6795
    philip "Я люблю настоящих женщин, Мэм!"
    "Леди, таких как Вы!"
    "Я знаю Вас заочно с тех времен, когда Вы только вошли в круги моды!"
    "И скажу, что Вы один из тех драгоценных камней, которые неподвластны времени!"
    img 6796
    "С каждый годом Вы становитесь женственнее и привлекательнее!"
    "Вы - настоящее чудо, Мэм!"

    img 6797
    w
    mt "Хи-хи..."
    #если сучка
    mt "Какой очаровательный плюшевый мишка..."
    "Может быть стоит поиграть с ним..."
    #если не сучка
    mt "Кажется я ему нравлюсь. Стоит узнать про него побольше..."

    img 6798
    m "И как идут Ваши дела, Филип?"
    "Вы достаточно успешны?"

    img 6799
    philip "О! Я весьма успешен, Мэм!"
    "Я не сравнюсь с Вами, но, думаю, мое состояние - это половина Вашего, Мэм!"

    img 6800
    mt "Хм... А он богат..."
    "И, судя по всему, простачок..."
    "Мне бы очень непомешало обзавестись таким..."
    "В конце концов, у него должен быть хороший дом..."
    "Он может дать мне много денег..."
    "И мне будет проще осуществить свою цель..."
    "Это не выглядит сложным."
    "Надо только немного подыграть ему."
    img 6801
    "Конечно, я не собираюсь спать с ним!"
    "Об этом бедняга может только мечтать!"

    img 6802
    m "И на что Вы готовы ради прекрасной женщины, Филип?"
    philip "О, Мэм! Ради прекрасной женщины я готов на все!"

    img 6803
    m "А кто я для Вас, Филип?"
    img 6804
    philip "Мэм! Вы самая прекрасная женщина на свете!"
    "Мое сердце принадлежит Вам!"
    img 6805
    m "Живопись... У меня в доме висит много картин..."

    img 6806
    philip "О! Мэм!"
    "Я бы с радостью пополнил Вашу коллекцию, подарив Вам несколько полотен!"

    "Если бы Вы только согласились поехать ко мне домой..."
    "Я бы показал Вам свои самые лучшие картины!"
    "Вы могли-бы выбрать любые, которые Вам понравятся!"
    "Я буду счастлив подарить их Вам!"

    img 6807
    mt "Хитрец пытается заманить меня к себе в дом..."
    "Я знаю все эти глупые мужские штучки..."
    "У него нет никаких шансов обыграть меня..."
    "А вот картины..."
    "Это неплохие деньги..."
    "А они мне сейчас нужны..."

    img 6808
    m "Филип! Налейте самой прекрасной даме еще вина!"

    img 6809
    philip "Конечно, Мэм!"
    #наливает вино

    img 6810
    with fadelong
    philip "Мэм! Разрешите пригласить Вас на танец!"

    img 6811
    mt "Танец?"
    "У меня ощущение что вино начало слегка давать мне в голову."
    img 6812
    "Вкусный ужин, вино..."
    "Пресса, внимание..."
    "Я начинаю чувствовать себя как раньше..."
    img 6813
    "Может не все так уж и плохо?"
    "Прежняя жизнь возвращается..."
    img 6812
    "Меня все любят и уважают..."
    "У меня есть власть..."
    "Мужчины стараются чтобы понравиться мне..."
    "..."
    img 6814
    "Танец?"
    "Почему-бы и нет?"
    "Но мне надо сначала сходить забрать деньги у Бифа."
    "Они мне уже не понадобятся, скорее всего."
    "Этот Филип покроет любые мои возможные расходы, но все-же..."
    img 6815
    m "Филип."
    "Я не уверена насчет танцев и вообще..."
    "Я отойду и подумаю над твоим предложением..."

    img 6816
    mt "Пусть попереживает..."
    "Надо заставить мужчину бегать за мной..."
    "Вызвать чувство вины..."
    "Тогда он будет в моих руках..."

    img 6817
    philip "Мэм? Я что-то сделал не так?" #грустно
    "Прошу простить меня если так..."

    img 6818
    m "Ты подумай пока, а я скоро вернусь... возможно..."

    return

label monica_charity_event_dialogue9:
    #Моника пытается разговаривать с Филипом, но еще не брала деньги у Бифа.
    mt "Мне надо забрать деньги у Бифа."
    "Филип пусть пока будет в неуверенности..."
    return

label monica_charity_event_dialogue10:
    #render
    #Моника разговаривает с Бифом, рядом сидит Мелани
    img 6728
    m "Биф! Уже прошел час!"
    img 6729
    beef "О! Крошка!"
    "Я вижу ты неплохо отдыхаешь!"
    "Тебе понравилось вино?"

    img 6730
    m "Да, вино довольно вкусное."
    "Оно стоит своих денег."
    "Так что, Биф? Я жду!"

    img 6731
    beef "Иди сюда, цыпочка!"

    img 6732
    beef "Вот, держи!"
    img 6733
    w
    img 6734
    "Твои $ 4.000!"
    img 6735
    m "$ 4.000???"

    img 6736
    "Здесь должно быть $ 5.000!"
    img 6737
    "Мы договаривались!"
    "Ты забыл?!?!"

    img 6738
    beef "Я все помню, цыпочка!"
    "Не повышай на меня голос!"
    "Это деньги за вычетом благотворительного вечера!"
    "Я не стал вычитать сумму взносов, но вычел расходы на еду и напитки!"
    img 6739
    "Ты сама их ела и пила!"
    "И, между прочим, согласилась что вино стоит своих денег!"

    img 6741
    m "Мне нужно $ 5.000!"
    img 6740
    beef "Ничем не могу помочь, детка!"

    img 6742
    m "Ты сволочь!"
    img 6743
    beef "Эй! Детка! Следи за языком!"
    img 6744
    mt "!!!"
    return

label monica_charity_event_dialogue11:
    #Моника разговаривает с собой на сцене
    mt "Вот урод!"
    "Он обманул меня!"
    "Если бы я знала что это вино стоит целую $ 1.000, то я бы не стала его пить!"
    "И, кстати, я думала что этот Филип угощает меня!"
    "Что за мужчины пошли в наше время?!"
    "Пусть не удивляются что их можно только использовать!"
    "Для нормального отношения к себе они совершенно не годятся!"
    "..."
    "Тем не менее..."
    "Мне нужно $ 5.000!"
    "Эта сучка Виктория ясно дала понять, что если денег будет меньше, то я могу даже не приходить!"
    "А с Диком бесполезно пытаться договориться!"
    "Он слепо слушается эту дуру!"
    "Уже вечер и мне надо спешить!"
    "Мне надо идти покупать этот чертов галстук!"
    "А у меня не хватает $ 1.000!"
    "Все складывается так что если я не найду эту $ 1.000, то попаду к Маркусу!!!"
    "О БОЖЕ!!!"
    "Где же мне ее взять?!?!"
    "Может быть стоит ускорить события с Филипом?"
    "Или попробовать уговорить Бифа?"
    return

label monica_charity_event_dialogue12:
    #Моника пытается идти к Бифу до танца с Филипом
    mt "Я думаю проще вытрясти деньги с простачка Филипа, нежели с этого безмозглого наглеца!"
    return

label monica_charity_event_dialogue14:
    #render
    #Моника обращается к Филипу с танцем
    img 6819
    philip "Моника! Вы готовы потанцевать со мной?"
    img 6820
    m "Филип..."
    "Я подумала... Если честно я не уверена..."
    img 6821
    "Ну... Хорошо... Давай потанцуем..."
    "Ты ведь так этого хочешь..."

    img 6822
    philip "Я этого очень хочу, Мэм!"

    #танцуют
    img 6823
    w
    img 6824
    w
    img 6825
    w
    img 6826
    w
    img 6827
    w
    img 6828
    w
    img 6829
    w
    img 6830
    w
    #сменяется музыка на медленную
    img 6831
    with fadelong
    m "А ты неплохо танцуешь, Филип!"
    philip "Я люблю женщин!"
    "А женщины любят танцевать!"
    "Потому я обязан это неплохо уметь!"

    img 6832
    m "Ты прав..."
    "Но, ты знаешь, женщины любят внимание..."

    philip "Я готов уделить Вам все свое внимание, Мэм!"

    img 6833
    m "Я хочу это проверить, Филип!"
    philip "Мэм! Я готов на все!"

    img 6834
    m "На этом вечере я познакомилась еще с одним ценителем искусства."
    img 6835
    "И, оказалось, что в его коллекции как раз есть картина, которую я давно искала."
    img 6836
    "Это очень редкое произведение и, к сожалению, у него уже есть покупатель."
    "Есть возможность опередить покупателя."
    "В случае если я выкуплю эту картину прямо сегодня за наличные деньги."

    img 6837
    "Филип, Вы знаете, я не очень разбираюсь в финансах."
    "И для меня будет сложно очень быстро получить наличность."
    img 6838
    "Поэтому... Если Вы готовы взять на себя эти небольшие хлопоты, то я бы оценила этот жест!"
    img 6839
    "Возможно, я даже согласилась бы когда-нибудь осмотреть Вашу коллекцию картин в Вашем доме!"

    img 6840
    philip "О! Мэм! Я буду рад помочь Вам!"
    img 6841
    "Это для меня сущие пустяки!"
    "Какова сумма этой картины?"

    img 6842
    m "Всего-лишь $ 300.000!"
    "Ничего особенного!"
    img 6843
    "Но деньги нужны прямо сейчас, потому я и обращаюсь к Вам!"
    "Мне многие могут помочь в этой мелочи, но я выбрала именно Вас!"
    img 6844
    mt "Сейчас я раскручу этого тюфяка!"

    img 6845
    philip "Мэм! Я польщен такой честью!"
    "Вы правы что обратились ко мне!"
    img 6846
    "Для меня это совсем небольшие деньги, но Вы знаете..."
    "Я занимаюсь предметами искусства, а значит должен скурпулезно оценивать все за что плачу!"
    "Вы согласны?"

    img 6847
    m "Конечно согласна, Филип!"
    "Я считаю что моя улыбка стоит гораздо больше!"

    img 6848
    philip "Если честно, Мэм, на протяжении вечера я оценивал не Вашу улыбку!"
    m "А что же?"
    philip "Ваш ротик, Мэм!"

    img 6849
    m "В смысле ротик?"
    "Филип, Вы про что?"

    philip "Для этого я и пришел сюда, Мэм!"

    img 6850
    m "Для чего вы пришли???"
    "Филип, я не понимаю Вас!"
    img 6851
    "Говорите яснее!"
    "И поехали скорее за деньгами!"

    img 6852
    philip "Мне давно нравится Ваш ротик, Мэм!"
    "И я пришел чтобы засунуть него свой член..."

    img 6853
    m "ЧТО??? ДА КАК ВЫ СМЕЕТЕ ТАКОЕ ГОВОРИТЬ?!?!"

    img 6854
    philip "Я реалист, Мэм!"
    "И я в курсе того что с Вами случилось."
    img 6855
    "Про это никто не знает, но я весьма хорошо осведомлен."
    img 6852
    "Поэтому если Вы хотите получить что-то от меня, то Вам придется попробовать меня на вкус!"

    img 6856
    m "Ты думаешь что я способна сделать минет за $ 300.000?"
    img 6857
    philip "Я знаю что Вы будете делать минеты, но я хочу быть одним из первых!"
    "Потому я и пришел сюда!"

    img 6858
    w

    menu:
        "$ 30.000.000 и я подумаю!":
            img 6859
            m "Если Вы подымете сумму до $ 30.000.000, то я готова подумать..."
            mt "В конце концов еще один небольшой кошмар, но я смогу решить все свои проблемы!"
        "Вы правда думаете что я стою так мало?":
            img 6860
            m "Вы правда думаете что я стою так мало?"

    img 6861
    philip "Что Вы, Мэм?"
    "Как Вы можете думать обо мне так плохо?"
    "Я хорошо умею считать и я оцениваю Ваш ротик в $ 500!"
    img 6862
    m "ЧТО??? ДА КАК ВЫ СМЕЕТЕ!!!"

    img 6863
    m "Я ухожу!"
    philip "Мэм! Спасибо за танец!"
    "Если захотите потанцевать еще, то пригласите меня!"
    return

label monica_charity_event_dialogue15:
    #Моника размышляет
    mt "ПОДОНОК!!!"
    "Откуда он знает про меня???"
    "И как он смеет использовать мое затруднительное положение в своих гнусных целях?!"
    "Мерзавец!"
    "..."
    "Но что мне делать?"
    "Если я не достану $ 1.000 срочно, то мне конец!"
    "У меня есть лишь несколько минут, пока еще не слишком поздний вечер!"
    "Мне надо подумать, может быть снова поговорить с Бифом?"
    "Или вернуться к Филипу?"
    "У меня нет выбора! Нет выбора!!!"
    "(хмык)"
    return

label monica_charity_event_dialogue16:
    #Моника разговаривает с Бифом, рядом сидит Мелани, уговор насчет дать денег
    img 6745
    m "Биф!"
    "Мне нужна $ 1.000!"

    img 6746
    beef "Детка! Я говорил тебе уже!"
    "Я с тобой полностью рассчитался!"

    img 6747
    mt "Что мне делать?"
    "Может быть попытаться уговорить его?"
    img 6748
    "Мне неудобно делать это при Мелани!"
    img 6747
    menu:
        "Биф! Мы можем отойти на пару минут?":
            pass
        "Уйти.":
            return

    img 6749
    m "Биф! Мы можем отойти на пару минут?"
    img 6750
    beef "Нет, говори!"
    img 6751
    "У меня нет секретов от крошки Мелани!"
    "И у нее от меня тоже!"
    "Правда, Мелани?"

    img 6752
    melanie "Правда, Биф..."

    img 6753
    beef "Вот видишь, цыпочка!"
    menu:
        "Биф, пожалуйста, дай деньги. Я буду хорошей цыпочкой...":
            pass
        "Я ни за что это не скажу! Уйти.":
            return

    img 6754
    m "Биф, пожалуйста, дай деньги. Я буду хорошей цыпочкой..."
    img 6755
    w
    #мелани улыбается
    img 6756
    beef "Хорошей цыпочкой - это какой?"

    img 6755
    mt "Черт! Мне так неудобно говорить при Мелани это!"
    img 6757
    m "Я буду исправно сниматься в фотосессиях и..."
    "И пройду твой кастинг перед следующей съемкой..."
    "Буду послушной..."

    img 6758
    beef "Ха-ха-ха!"
    "Детка, а ты знаешь подход к папочке!"
    img 6759
    "Мелани, как ты думаешь, стоит дать ей эти деньги?"


    #Моника была добра к Мелани
    img 6760
    mt "Мелани, я была добра к тебе! Не вздумай ответить нет!"
    img 6761
    melanie "Да, Биф!"
    "Это хорошая девушка! Она заслуживает твоей доброты!"

    #Моника была зла к Мелани
    img 6761
    melanie "Биф, это решать тебе!"
    "Я плохо знаю ее..."
    img 6762
    mt "Сучка Мелани!!! Не даром я ее не любила!"

    img 6763
    beef "Ха-ха-ха!"
    "Мелани! Я спросил тебя просто так!"
    "В любом случае решать папочке!"
    "..."

    img 6764
    "Хорошо, цыпочка!"
    "Держи $ 1.000 и поехали в офис!"
    "Ты забыла там свою одежду!"
    "Ха-ха-ха!"
    #уезжают в офис
    return

label monica_charity_event_dialogue17:
    #render
    #Моника обращается к Филипу с танцем повторно
    img 6864
    w
    img 6865
    philip "Да, Мэм?"
    "Вы надумали еще потанцевать?"

    menu:
        "Да, давай еще потанцуем.":
            pass
        "Уйти.":
            img 6866
            m "Нет!"
            philip "Мэм! Спасибо за танец!"
            "Если захотите потанцевать еще, то пригласите меня!"
            return

    m "Да, давай еще потанцуем."

    #танцуют
    #музыка
    img 6867
    with fadelong
    w
    img 6868
    philip "Мэм! Продолжим наш светский разговор по поводу Вашего ротика?"

    img 6869
    w
    menu:
        "Я не собираюсь про это говорить!":
            img 6870
            m "Я не собираюсь про это говорить!"
            philip "Мэм! Спасибо за танец!"
            "Если захотите потанцевать еще, то пригласите меня!"
            return
        "Хх... Хорошо... Филип...":
            pass


    m "Хх... Хорошо... Филип..."
    "Давай поговорим про это..."

    img 6871
    philip "Итак... Миссис Бакфетт!"
    "$ 500 и мой член в Вашем прекрасном ротике!"

    img 6872
    m "$ 10.000, Филип..."
    img 6873
    philip "$ 500, Миссис Бакфетт! Сегодня Ваш ротик не стоит больше..."
    "Это как на Бирже! Я покупаю акции на низкой цене!"

    img 6874
    m "Мне нужна хотя бы $ 1.000, Филип!"

    img 6875
    philip "$ 500, Миссис Бакфетт!"
    "Ваш ротик слишком долго говорит! Скоро он начнет дешеветь!"

    img 6876
    m "$ 1.000!!!"
    "Мне никак нельзя меньше!"
    img 6877
    "(хмык)"
    img 6878
    philip "Миссис Бакфетт!"
    "Эта гостиница предоставляет разнообразные услуги!"
    "Я начинаю торопиться и скоро уже ухожу!"
    img 6879
    "Перед уходом мой член побывает в чьем-нибудь ротике!"
    "В Вашем, либо в каком-то другом!"

    img 6880
    m "..." #переживает

    img 6881
    philip "Ну так в чьем?"
    philip "Решайте скорее!"

    img 6882
    m "..."

    img 6883
    philip "Ну?!"

    img 6882
    menu:
        "В МОЕМ! (хмык)":
            pass
        "Мне... Мне надо подумать!":
            img 6884
            m "Мне... Мне надо подумать!"
            philip "Мэм! Спасибо за танец!"
            "Если захотите потанцевать еще, то пригласите меня!"
            return


    img 6885
    m "В МОЕМ!" #очень переживает
    mt "(хмык)"
    img 6886
    w
    img 6887
    philip "Хорошо, Миссис Бакфетт!"
    img 6888
    "Давайте еще немного потанцуем!"
    img 6889
    "Я хочу сделать это до того как испорчу помаду у Вас на губах!"

    #танцуют
    img 6890
    w
    img 6891
    w
    img 6892
    w
    img 6893
    w
    img 6894
    w

    img 6895
    philip "Мне нравится этот танец!"
    "Мне доставляет удовольствием наблюдать за Вашим ротиком!"
    "Ведь через 5 минут мой член будет глубоко в нем!"

    img 6896
    mt "!!!"
    philip "Танцевать при таких обстоятельствах доставляет мне эстетическое удовольствие!"

    img 6897
    mt "!!!"

    img 6891
    w
    img 6892
    w
    img 6893
    w

    img 6898
    philip "Достаточно! Пришла пора испортить Ваш макияж, Миссис Бакфетт!"
    img 6899
    "Идемте!"

    return
label monica_charity_event_dialogue18:
    #render
    #Туалет. Моника. Филип
    img 6900
    m "Куда ты меня привел, Филип?"
    "Это мужской туалет!"
    img 6901
    philip "Миссис Бакфетт!"
    "Мне будет неудобно находиться в женском туалете!"
    img 6902
    "Ну а для Вас, полагаю, нет никакой разницы, ведь так?"
    m "Я думала это будет хотя бы гостиничный номер!"
    img 6903
    philip "О, Мэм!"
    "Гостиничный номер будет стоить гораздо дороже Вашего ротика!"
    "Как Вы знаете, я умею считать деньги!"
    "Поэтому туалет как раз подойдет для этой цели!"

    img 6904
    mt "!!!"

    img 6905
    philip "Итак, Миссис Бакфетт!"
    "Садитесь на колени! Вам будет неудобно принимать мой член стоя!"
    img 6906
    w
    img 6907
    w
    img 6908
    mt "У меня нет времени!"
    "Это единственный выход!"
    "(хмык)"
    img 6909
    philip "Ну!?"
    "Я жду!!!"

    #Моника садится
    img 6910
    w
    img 6911
    philip "Хорошая девочка..."
    #звук раздевания
    img 6912
    with fadelong
    w
    #звук расстегивания змейки
    img 6913
    w
    img 6914
    w
    img 6915
    w

    #Филип подносит член ко рту
    img 6916
    w
    img 6917
    w
    philip "Миссис Бакфетт! Я попрошу Вас открыть свой ротик!"
    "Я мог бы сделать это своим членом..."

    "Но я привык к комфорту!"
    "Я привык что женщины сами открывают свой ротик чтобы принять мой член внутрь!"

    img 6918
    mt "!!!"

    #Моника открывает рот
    img 6919
    with fadelong
    w

    img 6920
    philip "Миссис Бакфетт!"
    "Не могли-бы Вы пошире открыть его?"
    img 6921
    "Наверное Вам оттуда плохо видно..."
    "Но поверьте, мне отсюда видно хорошо!"
    img 6922
    "Ваш ротик недостаточно открыт для того чтобы мой член комфортно вошел в него!"
    img 6923
    w
    img 6924
    w
    img 6925
    w
    img 6926
    w
    img 6927
    w

    img 6928 #?????
    w

    #Моника открывает рот сильнее
    #идет видео минета
    philip "Миссис Бакфетт!"
    "Отлично!"
    "Чувствуется что у Вас недостаток практики!"
    "Но мне это даже нравится!"

    #идет видео минета

    "Если честно, я сомневался что Ваш ротик стоит $ 500!"
    "Я думал что ему больше подходит цена в $ 300!"

    "Но нет!"
    "Теперь я уверен что $ 500 он стоит вполне!"


    #заглядывает рецепшин
    img 6929
    w
    img 6930
    w
    img 6931
    reception_t "Ага!"
    "А я уже начала было сомневаться в своем чутье!"
    "Эта шлюха искусно маскируется!"
    #видео
    img 6933
    "Я почти поверила что она Леди!"
    "В нашей гостинице запрещено заниматься проституцией без разрешения!"
    #видео

    img 6932
    "В прошлый раз она приходила с такой же целью, могу поспорить!"



    #идет видео минета
    img 6934
    w
    philip "АААААААРРГГГХХХ!!!"
    img 6935
    w
    img 6936
    philip "АААААААРРГГГХХХ!!!"

    #Моника сидит со спермой
    img 6937
    w
    img 6938
    w
    img 6939
    w

    img 6940
    philip "Спасибо, Моника Бакфетт!"
    philip "Вы заработали свои $ 500!"

    img 6941
    m "Еще $ 500!"
    img 6942
    philip "?"

    img 6943
    m "Мне нужно еще $ 500!"
    img 6944
    "Пожалуйста! Прошу Вас!!!"

    img 6945
    philip "Миссис Бакфетт!"
    "Почему я должен давать Вам еще $ 500?"
    img 6946
    m "Мне очень надо! ОЧЕНЬ!!!"
    img 6945
    philip "Это не аргумент, Миссис Бакфетт!"
    "Что Вы можете предложить взамен?"

    img 6946
    menu:
        "Я могу сделать это еще раз...":
            img 6947
            m "Мистер..."
            img 6948
            "Я могу..."
            "Я могу сделать это еще раз..."
            img 6949
            "Вы дадите мне еще $ 500..."
            img 6950
            philip "Мэм! Я говорил Вам про то что люблю женщин!"
            "Женщины не стареют и не теряют своей цены, потому что..."
            img 6951
            "Потому что они разные! Разные женщины, Мэм!"
            "Я никогда! Никогда не вставляю два раза член в одну и ту же женщину!"
            "Благодаря этому правилу их у меня много и я могу наслаждаться их вкусом!"
            img 6952
            m "Но пожалуйста, Мистер!"
            img 6953
            philip "Миссис Бакфетт! Я уже купил Ваш ротик!"
            img 6954
            "Я не собираюсь еще раз покупать его!!!"

        "Я не знаю... Мне нечего предложить...":
            img 6955
            m "Мне нечего предложить, но пожалуйста!"
            "Мистер!"
            "Для меня это жизнь или смерть!"

    img 6956
    philip "Хотя..."
    "Знаете что..."
    "Вы сделаете миньет первому мужчине, который зайдет сюда!"
    "Тогда Вы получите еще $ 500!"
    img 6957
    "Вы согласны?"

    m "Я... Я..."

    #Заходит hotel_staff
    img 6958
    hotel_staff "Ой!"
    img 6959
    "Прошу прощения за беспокойство!"
    "Я зайду позже!"
    philip "Эй! Парень!"
    "Постой-ка!"

    hotel_staff "Да, Сэр?"
    philip "Иди-ка сюда!"

    img 6960
    hotel_staff "Да, Сэр? Чем могу быть полезен?"
    img 6961
    philip "У тебя есть член, парень?"
    hotel_staff "Что вы имеете ввиду, Сэр?"

    img 6962
    philip "Член! Есть член у тебя?!"
    "Я имею ввиду ту штуку что должна быть в штанах у каждого мужчины!"
    "Есть она у тебя или ее нет?"

    img 6963
    hotel_staff "Сэр... Конечно есть..."
    "Но я не понимаю зачем этот вопрос."
    "Я могу как-то помочь Вам?"

    img 6964
    philip "Да, парень!"
    "Открой глаза и посмотри!"
    "У меня здесь сидит сучка и сосет бесплатно члены!"
    "У тех кто сюда заходит!"

    img 6965
    "Для тебя бесплатно, конечно."
    "Для меня это кое-что стоит, но я готов потратить эти деньги для такого удовольствия."

    img 6966
    "Ты только посмотри кто это!"
    img 6967
    hotel_staff "МИССИС БАКФЕТТ?!?!" #смотрит с ужасом

    #если Моника была зла к нему, то:
    img 6968
    #

    img 6969 #+
    philip "Да, это она!"
    "Парень! Такой шанс выпадает только раз!"
    "Ты счастливчик!"

    img 6970
    "Моника Бакфетт сидит в туалете и ждет твой член!"
    "Она ждет его!"
    "Ее ротик приглашает твой член! Чтобы ты вставил его!"

    #обращается к Монике
    philip "Ну-ка открой свой ротик!"
    "Приглашай его член!"
    "Иначе не получишь деньги!"

    #Моника открывает рот

    #парень смотрит в ужасе

    #если Моника была добра к нему
    hotel_staff "Сэр!"
    "Но я не могу этого сделать!"
    "Эта женщина была добра ко мне!"
    "Пожалуйста, дайте ей то что она хочет!"
    philip "Ха-ха!"
    "Ладно, парень, как хочешь!"
    #смотрит на Монику
    philip "Можешь закрыть свой ротик! Ты заслужила свои деньги!"
    #Моника закрывает рот
    #call уход на разговор с Бифом

    #если Моника была зла к нему
    hotel_staff "А ведь она собиралась уволить меня!"
    philip "Ха-ха!"
    "Тем более!"
    "Этот ротик заслужил твой член!"
    "Давай! Вставь его! Скорее!"
    hotel_staff "А она ничего мне потом не сделает за это?"
    philip "Парень! Она не сделает тебе ничего!"
    "Не бойся!"
    "Долби ее ротик!"

    #парень начинает ее долбить
    hotel_staff "Простите, Мэм!"
    "Пожалуйста, не увольняйте меня!"
    "Я обязательно учту Ваши пожелания по поводу постера в следующий раз!"

    #парень кончает
    hotel_staff "Сэр, я могу идти?"
    philip "Иди, парень! Ты повеселил меня!"
    philip "Вот Ваши деньги, Миссис Бакфетт!"
    "Я найду Вас когда захочу попробовать Вашу попку!"

    #бросает деньги и они уходят

    m "Пожалуйста!"
    "Не говорите про это никому!!!"
    hotel_staff "Конечно, Мэм!"
    "Я никому не скажу!"
    #уходит на разговор с Бифом и уход
    return


label monica_charity_event_dialogue19:
    #Моника разговаривает с Бифом, рядом сидит Мелани, разговор по поводу того чтобы уехать
    img 6765
    m "Биф! Я ухожу отсюда!"
    imt 6766
    beef "Постой, детка! Мы вместе поедем сейчас в офис!"
    "Ты забыла там свою одежду!"
    "Ха-ха-ха!"
    return

label monica_office_beef_dialogue_evening1:
    #Моника разговаривает с Бифом в офисе
    beef "Детка, ты свободна на сегодня!"
    "Не уверен что ты стоишь $ 5.000, но я подумаю..."

    m "Я могу идти, Биф?"
    beef "А попа! Ты собираешься мне ее показывать или нет?"

    m "Я не буду этого делать, Биф!"
    beef "Ах да! Ты сделаешь это перед следующей фотосессией!"
    mt "!!!"
    "Не будет больше никакой фотосессии, УРОД!!!"

    beef "Можешь идти!"
    return

label monica_office_dialogue1:
    #Моника на улице у своего офиса
    mt "Мне надо скорее бежать к Дику!"
    "Надо купить этот чертов галстук и закончить кошмар!"
    "Через что мне пришлось пройти чтобы добыть эти деньги!"
    "Ужас!"

    return

label monica_dick_office_entrance_dialogue1:
    #Моника на входе в офис Дика
    reception_secretary "Мэм, вы куда?"
    m "Я к Дику Адвокату! Он ждет меня!"
    reception_secretary "Мэм, Мистера Дика уже нет..."
    m "Не может быть! Он должен был дождаться меня!"
    reception_secretary "Мистер Дик с Мисс Викторией ушли 30 минут назад..."
    mt "НЕЕЕТ!!!"
    "Я ОПОЗДАЛА!!!"
    "ЧТО ЖЕ МНЕ ДЕЛАТЬ?!?!"
    "..."
    "Эта сучка говорила что отправит факс с утра..."
    "Мне надо дождаться утро..."
    "Но где мне ждать???"
    "Здесь нет ни одного чертового стула!!!"
    "ЧТО ЭТО ВООБЩЕ ЗА ОФИС!!!"
    "НА УЛИЦЕ ДОЖДЬ!!!"
    "..."
    "Думаю лучшим выходом будет идти в дом..."
    "Завтра пораньше встать и идти сюда..."
    "Да! Это лучший вариант!"

    return

label monica_basement_bedroom_before_sleep1:
    #Моника ложиться спать
    mt "Надо поспать..."
    "Я нашла деньги..."
    "Завтра я приду к Дику и все закончится..."
    "Я лучше забуду про тот кошмар, который мне пришлось пройти, чтобы достать эти деньги..."
    "Я почти у цели..."
    "Я сплю..."
    return



    #
