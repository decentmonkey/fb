label monica_gas_station_thief_dialogue1:
    #Моника заходит на заправку (голодная)
    mt "На этой заправке продается еда."
    "Если я буду осторожна, то могу украсть какое-нибудь пирожное..."
    "Но стоит-ли мне рисковать?"
    return

    #Моника заходит на заправку (сытая)
    mt "Что я здесь делаю?"
    mt "Есть я пока не хочу, а говорить с этой кассиршей мне не о чем..."

    return

label monica_gas_station_thief_dialogue2:
    #Моника ворует еду
    menu:
        "Украсть еду.":
            pass
        "Не делать этого.":
            mt "Я не стану рисковать..."
            return

    #render
    mt "Думаю не будет ничего страшного если я украду одно пирожное..."
    "Я заслужила его за все то что пережила..."

    return
