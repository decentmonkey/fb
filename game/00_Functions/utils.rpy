
init python:
    def getMousePosition():
        import pygame
        x, y = pygame.mouse.get_pos()
        store.mousex = x
        store.mousey = y

    def checkDialogueExists():
        if renpy.get_screen("choice") != None or renpy.get_screen("window") != None:
            return True
        return False

    def mycopytext(t):
        pygame.scrap.put(pygame.scrap.SCRAP_TEXT, t.encode("utf-8"))

label mycopytext_label(txt):
    $ mycopytext(txt)
    return

label bitch(amount, place=False):
    $ global bitchmeter_places
    if place != False:
        if bitchmeter_places.has_key(place):
            return
        $ bitchmeter_places[place] = amount


    if bitchmeterValue > maxBitchness / 2 and amount < 0:
        $ amount *= 3
    if bitchmeterValue <= maxBitchness / 2 and amount > 0:
        $ amount *= 3

    $ bitchmeterValue += amount
    if amount > 0:
        show screen notify ("Bitchness increased!")
    else:
        show screen notify ("Bitchness decreased!")
    return


label photoshop_flash():
    sound snd_photo_capture
    show screen photoshot_screen()
    pause 0.7
    hide screen photoshot_screen
    return

label textonblack(in_text):
    scene black_screen
    with Dissolve(1)
    show screen textonblack_screen(in_text)
    with Dissolve(1)
    pause 1.5
    scene black_screen
    with Dissolve(1)
    return


label textonblack_long(in_text):
    scene black_screen
    with Dissolve(1)
    show screen textonblack_screen(in_text)
    with Dissolve(1)
    $ renpy.pause(5.0, hard=True)
    scene black_screen
    with Dissolve(1)
    return













#
