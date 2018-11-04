init python:
    def Ani(img_name, frames, delay=.1, loop=True, reverse=True, effect=None, start=1, ext="png", **properties):
        args = []
        for i in range(start, start + frames):
            args.append(renpy.display.im.image(img_name + str(i) + "." + ext))
            if reverse or loop or (i < start + frames - 1):
                args.append(delay)
                args.append(effect)
        if reverse: # обратная анимация, если нужна
            for i in range(start + frames - 2, start, -1):
                args.append(renpy.display.im.image(img_name + str(i) + "." + ext))
                if loop or (i > start + 1):
                    args.append(delay)
                    args.append(effect)
        return anim.TransitionAnimation(*args, **properties)
    # время появления/затухания звуков
    fade_time = 1.0
    # регистрируем каналы, чтобы звуки не прерывали друг друга
    channels = ["rain", "thunder1", "thunder2", "thunder3"]
    for i in channels:
        renpy.music.register_channel(i, "sfx", True)
    # воспроизводим звуки на своих каналах
    # либо на канале sound, если нужный канал не зарегистрирован
    def splay(name, channel=None, loop=False, fadein=fade_time, fadeout=fade_time):
        if not channel in channels:
            channel = None
        if channel is None:
            if name in channels:
                channel = name
            else:
                channel = "sound"
        fn = "sounds/" + name + ".ogg"
        renpy.music.play(fn, channel=channel, loop=loop, fadeout=fadeout, fadein=fadein)
    # постепенно останавливаем звуки или один звук, если на входе не список
    def sstop(channel=channels, fadeout=fade_time):
        if isinstance(channel, list):
            for i in channel:
                renpy.music.stop(i, fadeout=fadeout)
        else:
            renpy.music.stop(channel, fadeout=fadeout)
    # новое положение молний
    xa = renpy.random.random()
    def newxa():
        global xa
        xa = renpy.random.random()
        renpy.restart_interaction()
    # функция → action
    SPlay = renpy.curry(splay)
    SStop = renpy.curry(sstop)
    NewXA = renpy.curry(newxa)

init:
    # пустая картинка
    image none = Null(1, 1)
    # анимация дождя
    image rain = Ani("images/Sprites/Rain/rain", 5, .1, reverse=False)
    # анимация молнии
#    image lightning = Overlays/white_screen.jpg
#    image lightning = Ani("lightning", 3, .025)
    # мерцание молнии
    image light:
        yalign 0 yanchor 0
        # пусто
        "none"
        4.5
        xzoom 1.0
        "lightning"
        .1
        "none"
        .1
        "lightning"
        .1
        "none"
        1.5
        # зеркальное отражение
        xzoom -1.0
        "lightning"
        .1
        "none"
        .05
        "lightning"
        .1
        repeat
