label splashscreen:
    return
    scene black
    image videoIntro_Video = Movie(play="video/Intro_Video.mkv", fps=30)
    show videoIntro_Video
    $ renpy.pause(2.0, hard=True)
    $ renpy.pause(68.0)
    stop music fadeout 0.5
    img black_screen
    with Dissolve(0.5)
    img all_over_18
    with Dissolve(0.7)
    $ renpy.pause(2.0)
    img black_screen
    with Dissolve(0.7)
    return

    wclean
    img decentmonkey_logo
    with fade
    pause 3.0
    img all_over_18
    with fade
    pause 3.0
    scene black
    with dissolve
    return
