default bettyLocation = "none"

label bettyInteract1(obj_name, obj_data):
    if act == "l":
        mt "Это Бетти..."
        "Редкая сучка!"
        "Она следит за мной, за каждым моим шагом."
        "Мне надо быть осторожнее с ней, пока..."
        "Она еще поплатится за свое ко мне отношение!"
    if act == "t":
        if bettyLocation == "Bedroom1":
            if day_time == "day":
                call bettyDialogue1()
                return
    return
