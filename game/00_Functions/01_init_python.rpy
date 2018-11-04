python early:

    def img_disp(l):
        return l.simple_expression()
#        return l.string()
    def img_exec(s):
        global dialogue_active_flag, screenActionHappened

        try:
            imagePath = img_find_path(renpy.eval(s))
        except:
            imagePath = img_find_path(s)

        if (renpy.get_screen("say") != None or renpy.get_screen("choice") != None or renpy.get_screen("window") != None or dialogue_active_flag == True) and persistent.pause_before_change_slide == True:
            renpy.hide_screen("say")
            renpy.hide_screen("choice")
            renpy.hide("window")
            renpy.show_screen("dialogue_down_arrow")
            renpy.pause()
            renpy.hide_screen("dialogue_down_arrow")
            dialogue_active_flag = False
        renpy.scene()
        renpy.show_screen("show_image_screen", imagePath)
        image_screen_scene_flag = False
        screenActionHappened = True
    def img_pred(s):
        return [Image(img_find_path(s))]
    renpy.register_statement("img", parse=img_disp, execute=img_exec, predict=img_pred) #кастомный scene

    def imgl_exec(s):
        global dialogue_active_flag, screenActionHappened
        renpy.show_screen("dialogue_image_black_overlay")
        renpy.show_screen("dialogue_image_left", img_find_path(s), config.screen_width / 2, config.screen_height)
        screenActionHappened = True

    renpy.register_statement("imgl", parse=img_disp, execute=imgl_exec, predict=img_pred)

    def imgr_exec(s):
        global dialogue_active_flag, screenActionHappened
        renpy.show_screen("dialogue_image_black_overlay")
        renpy.show_screen("dialogue_image_right", img_find_path(s), config.screen_width / 2, config.screen_height)
        screenActionHappened = True

    renpy.register_statement("imgr", parse=img_disp, execute=imgr_exec, predict=img_pred)

    def imgcenter_exec(s):
        global dialogue_active_flag, screenActionHappened
        renpy.show_screen("dialogue_image_black_overlay")
        renpy.show_screen("dialogue_image_center", img_find_path(s), config.screen_width / 2, config.screen_height)
        screenActionHappened = True

    renpy.register_statement("imgc", parse=img_disp, execute=imgcenter_exec, predict=img_pred)

    def saywrapper_parse(lex):
        who = lex.simple_expression()
        what = lex.simple_expression()
#        what = lex.string()
        if what == None:
            what = who
            who = "Noone"
        return (who,what)

    def saywrapper_lint(o):
        who, what = o
        try:
            eval(who)
        except:
            renpy.error("Character not defined: %s" % who)

        tte = renpy.check_text_tags(what)
        if tte:
            renpy.error(tte)


    def saywrapper_execute(o):
        global last_dialogue_character
        global dialogue_active_flag, screenActionHappened
        who, what = o
        if who == "Noone":
            who = last_dialogue_character
        else:
            last_dialogue_character = who
        who = eval(who)
        what = what[1:-1]
#        what = re.sub(r'\n' , '\s', what)
        dialogue_active_flag = True
        screenActionHappened = True

        if persistent.auto_clipboard == True:
            copy_what = re.sub("\!\s{1,}", "!\n", what)
            copy_what = re.sub("\?\s{1,}", "?\n", copy_what)
            copy_what = re.sub("\.\s{1,}", ".\n", copy_what)
            mycopytext(copy_what) #put into clipboard

        renpy.say(who, what)

    renpy.register_statement("", parse=saywrapper_parse, execute=saywrapper_execute, lint = saywrapper_lint, translatable=True) #враппер для say, чтобы подымать флаг активного диалога


    def w_parse(l):
        return None

    def w_exec(o):
        global dialogue_active_flag, screenActionHappened
        renpy.hide_screen("say")
        renpy.hide_screen("choice")
        renpy.hide("window")
        renpy.show_screen("dialogue_down_arrow")
        renpy.pause()
        renpy.hide_screen("dialogue_down_arrow")
        dialogue_active_flag = False
        screenActionHappened = True

    def wclean_exec(o):
        global dialogue_active_flag, screenActionHappened
        renpy.hide_screen("say")
        renpy.hide_screen("choice")
        renpy.hide("window")
        renpy.pause()
        dialogue_active_flag = False
        screenActionHappened = True

    renpy.register_statement("w", parse=w_parse, execute=w_exec) #w - оператор ожидания с мигающей стрелкой
    renpy.register_statement("wclean", parse=w_parse, execute=wclean_exec) #w - оператор ожидания с мигающей стрелкой

    def wc_exec(o):
        global dialogue_active_flag
        dialogue_active_flag = False

    renpy.register_statement("wc", parse=w_parse, execute=wc_exec) #wait dialogue clear, удаляет флаг того что висит открытый диалог (для пикч)


    def sound_parse(l):
        return l.simple_expression()

    def sound_exec(o):
        checkPath = "Sounds/" + str(o) + ".ogg"
        if renpy.loadable(checkPath):
            renpy.play(checkPath, channel="sound")
        checkPath = "Sounds/" + str(o) + ".wav"
        if renpy.loadable(checkPath):
            renpy.play(checkPath, channel="sound")

    renpy.register_statement("sound", parse=sound_parse, execute=sound_exec) #sound - оператор воспроизведения звука

    def music_parse(l):
        return l.simple_expression()

    def music_exec(o):
        try:
            musicName = renpy.eval(o)
        except:
            musicName = o
        checkPath = "Music/" + str(musicName) + ".ogg"
        if renpy.loadable(checkPath):
            renpy.music.play(checkPath, channel="music", loop=True, fadeout=1.0, fadein=1.0)

    renpy.register_statement("music", parse=music_parse, execute=music_exec) #music - оператор воспроизведения музыки


    def video_parse(l):
        return l.simple_expression()
    def video_exec(o):
        try:
            videoName = get_filename(renpy.eval(o))
        except:
            videoName = get_filename(o)
        print(videoName)
        playing_video = Movie(play=videoName, channel="movie") #?????


    renpy.register_statement("video", parse=video_parse, execute=video_exec) #video - оператор воспроизведения видео
