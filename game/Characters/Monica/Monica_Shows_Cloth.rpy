label monica_show_cloth(obj_name, obj_data):
    if cloth_type == "Lingerie":
        if cloth == "Lingerie1":

            imgc inv_lingerie1

            m "Очень милое белье."

            "Мне в нем очень удобно!"

            "Я всегда одеваю только самое лучшее!!"
            w
        if cloth == "Lingerie2":
            imgc inv_lingerie2
            m "Этот пеньюар может свести с ума любого."
            "Хи-хи..."

        if cloth == "Lingerie3":
            imgc inv_lingerie3
            m "Последняя модель от самого модного дома белья!"

    if cloth_type == "HomeCloth":
        if cloth == "HomeCloth1":
            imgc inv_homecloth1
            m "Этот свитер очень теплый, но в то же время дышит."

            "Миленько..."
            w
        if cloth == "HomeCloth2":
            imgc inv_homecloth2
            m "Сегодня я решила ходить дома в чем-то более свободном, не стесняющим движений."
            "Очень удобно!"

        if cloth == "HomeCloth3":
            imgc inv_homecloth3
            m "Эта яркая пижама задает мне хорошее настроение прямо с утра!"

    if cloth_type == "BusinessCloth":
        if cloth == "BusinessCloth1":
            imgc inv_businesscloth1_look
            "Я всегда одеваю только самое лучшее!!"
        if cloth == "EveningDress":
            imgc inv_eveningdress
            m "Это платье не такое уж и дорогое."
            "Не уверена что оно мне подходит."
            "Но выглядит довольно красиво."
            "Надеюсь никто не поймет что оно стоит меньше 10000$!"
            "Фи!"
        if cloth == "BusinessCloth2":
            imgc inv_businesscloth2
            m "Я - Босс!"
            "Если кто-то сомневается в этом, тот будет иметь дело СО МНОЙ!"
            "Хи-хи!"
        if cloth == "BusinessCloth3":
            imgc inv_businesscloth3
            m "У меня чудное настроение сегодня!"
            "Меня ждет столько интересных дел!!"
            "Я в предвкушении!"
            "Это платье соответствует моему настроению!!"

    return

label monica_show_lingerie_image:
    if cloth == "Lingerie1":
        imgc inv_lingerie1

    return
