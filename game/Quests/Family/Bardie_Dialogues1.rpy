label bardieDialogue1:
    if cloth != "Governess":
        mt "Я не хочу разговаривать с ним в таком виде."
        "Мне надо переодеться!"
        return
    #render+
    #Моника говорит с Барди в его комнате
    music Hidden_Agenda
    img 5798
#    imgr Dial_Bardie_1
    bardie "Я тебя сюда устроил, помнишь?"
    "Ты мне должна!"
    img 5799
#    imgl Dial_begin37_2
    m "Я тебе ничего не должна, мальчик!"
    "Веди себя вежливо по отношению ко старшим!"

    music Power_Bots_Loop
    img 5800
#    imgr Dial_Bardie_2
    bardie "Ах ты так!"
    bardie_t "Ну она у меня попляшет!"

    $ monicaBardieOffended1 = True

    music casualMusic
    return
