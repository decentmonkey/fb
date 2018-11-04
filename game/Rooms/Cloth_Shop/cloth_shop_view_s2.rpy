#s2ClothShopStage

default s2ClothShopCashierView1 = False

label cloth_shop_view1_s2:
    $ print "enter_cloth_shop_view1_s2"
    $ miniMapData = []

    $ scene_name = "cloth_shop_view1_s2"
    $ scene_caption = _("Clothing Shop")
    $ clear_scene_from_objects(scene_name)

    $ scene_image = "scene_Cloth_Shop_View1"

    if s2ClothShopStage == 1:
        $ add_object_to_scene("Cloth1", {"type":2, "base":"Cloth_Shop_View1_Cloth1", "click" : "cloth_shop_view1_environment2", "actions" : "l", "zorder" : 0})
        $ add_object_to_scene("Cloth2", {"type":2, "base":"Cloth_Shop_View1_Cloth2", "click" : "cloth_shop_view1_environment2", "actions" : "lw", "zorder" : 0})
        $ add_object_to_scene("Cloth3", {"type":2, "base":"Cloth_Shop_View1_Cloth3", "click" : "cloth_shop_view1_environment2", "actions" : "l", "zorder" : 0})
        $ add_object_to_scene("Cloth4", {"type":2, "base":"Cloth_Shop_View1_Cloth4", "click" : "cloth_shop_view1_environment2", "actions" : "lw", "zorder" : 0})
        $ add_object_to_scene("Cloth5", {"type":2, "base":"Cloth_Shop_View1_Cloth5", "click" : "cloth_shop_view1_environment2", "actions" : "l", "zorder" : 0})
        $ add_object_to_scene("Cloth6", {"type":2, "base":"Cloth_Shop_View1_Cloth6", "click" : "cloth_shop_view1_environment2", "actions" : "lw", "zorder" : 0})
        $ add_object_to_scene("Cloth7", {"type":2, "base":"Cloth_Shop_View1_Cloth7", "click" : "cloth_shop_view1_environment2", "actions" : "l", "zorder" : 0})
        $ add_object_to_scene("Cloth8", {"type":2, "base":"Cloth_Shop_View1_Cloth8", "click" : "cloth_shop_view1_environment2", "actions" : "l", "zorder" : 0})

        $ add_object_to_scene("Mannequin", {"type":2, "base":"Cloth_Shop_View1_Mannequin", "click" : "cloth_shop_view1_environment2", "actions" : "l", "zorder" : 0})
        $ add_object_to_scene("Pouf1", {"type":2, "base":"Cloth_Shop_View1_Pouf1", "click" : "cloth_shop_view1_environment2", "actions" : "l", "zorder" : 0})
        $ add_object_to_scene("Pouf2", {"type":2, "base":"Cloth_Shop_View1_Pouf2", "click" : "cloth_shop_view1_environment2", "actions" : "l", "zorder" : 0})
#        $ add_object_to_scene("Rack1", {"type":2, "base":"Cloth_Shop_View1_Rack1", "click" : "cloth_shop_view1_environment2", "actions" : "l", "zorder" : 0})
#        $ add_object_to_scene("Rack2", {"type":2, "base":"Cloth_Shop_View1_Rack2", "click" : "cloth_shop_view1_environment2", "actions" : "l", "zorder" : 0})

    $ add_object_to_scene("Teleport_Cashier", {"type":2, "base":"Cloth_Shop_View1_Cashier", "click" : "cloth_shop_view1_teleport2", "actions" : "lw", "zorder" : 0})
    $ add_object_to_scene("Teleport_Dressing_Room", {"type":2, "base":"Cloth_Shop_View1_DressingRoom", "click" : "cloth_shop_view1_teleport2", "actions" : "lw", "zorder" : 0})
    $ add_object_to_scene("Teleport_View2", {"type":3, "text" : _("ИДТИ ДАЛЬШЕ"), "rarrow" : "arrow_up_2", "base":"Cloth_Shop_View1_Teleport_View2", "click" : "cloth_shop_view1_teleport2", "xpos" : 183, "ypos" : 929, "zorder":11})
    $ add_object_to_scene("Teleport_Street_Cloth_Shop", {"type":3, "text" : _("НАЗАД НА УЛИЦУ"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "cloth_shop_view1_teleport2", "xpos" : 960, "ypos" : 956, "zorder":11})

    if clothShopInited == False:
        call cloth_shop_init()

    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label cloth_shop_view1_teleport2(obj_name, obj_data):
    if obj_name == "Teleport_View2":
        if s2ClothShopStage == 1:
            if s2ClothShopCashierView1 == False:
                $ s2ClothShopCashierView1 = True
                call after_jail_cloth_shop_cashier1()
                return
            else:
                call after_jail_cloth_shop_cashier3()
                return
        call change_scene("cloth_shop_view2")
        return
    if obj_name == "Teleport_Dressing_Room":
        if obj_data["action"] == "l":
            if s2ClothShopStage >= 4:
                mt "Там примерочная."
                return

            mt "Там примерочная."
            mt "Может быть там получится спрятаться?"
            return
        if obj_data["action"] == "w":
            call change_scene("cloth_shop_dressing_room")
            return
    if obj_name == "Teleport_Cashier":
        if obj_data["action"] == "l":
            mt "Насколько мне видно отсюда, там касса."
            return
        if obj_data["action"] == "w":
            if s2ClothShopStage == 1:
                if s2ClothShopCashierView1 == False:
                    $ s2ClothShopCashierView1 = True
                    call after_jail_cloth_shop_cashier1()
                    return
                else:
                    call after_jail_cloth_shop_cashier3()
                    return
            call change_scene("cloth_shop_cashier")
            return
    if obj_name == "Teleport_Street_Cloth_Shop":
        if s2ClothShopStage == 1:
            mt "Нет! Я не уйду отсюда! Здесь тепло и сухо!"
            return
        call change_scene("street_cloth_shop", "Fade_long")
        return
    return

label cloth_shop_view1_environment2(obj_name, obj_data):
    if obj_name == "Sofa":
        if s2ClothShopStage == 3:
            call after_jail_cloth_shop_cashier9()
            return

    if obj_name == "Chocolate":
        if act == "l":
            mt "Ага! Вот она!"
            "Шоколадка!"
            "Я заслужила ее!!!"
        if act == "h":
            call after_jail_cloth_shop_cashier8()
            return

    if obj_name == "Mannequin":
        mt "Какой-то менекен..."
        mt "Мне за ним не спрятаться!"
        return
    if obj_name == "Pouf1" or obj_name == "Pouf2":
        mt "Я не спрячусь здесь..."
        return
    if obj_name == "Cloth1":
        mt "Я не спрячусь здесь..."
        return
    if obj_name == "Cloth2":
        mt "Я не спрячусь здесь..."
        return
    if obj_name == "Cloth3":
        mt "Я не спрячусь здесь..."
        return
    if obj_name == "Cloth4":
        mt "Я не спрячусь здесь..."
        return
    if obj_name == "Cloth5":
        mt "Я не спрячусь здесь..."
        return
    if obj_name == "Cloth6":
        mt "Я не спрячусь здесь..."
        return
    if obj_name == "Cloth7":
        mt "Я не спрячусь здесь..."
        return
    if obj_name == "Cloth8":
        mt "Я не спрячусь здесь..."
        return

    return
