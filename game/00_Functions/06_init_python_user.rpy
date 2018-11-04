init python:
    def get_bitchmeter_description():
        global bitchmeterValue, maxBitchness
        bitchmeter_captions = ["Shy Girl", "Decent Girl", "Casual Girl", "Hot-Tempered", "Bitch", "Complete Bitch", "Bitch from the Hell"]

#        if bitchmeterValue < float(maxBitchness) / 100 * 20:
        if bitchmeterValue <= 153:
            return bitchmeter_captions[0]
        if bitchmeterValue <= float(maxBitchness) / 100 * 49:
            return bitchmeter_captions[1]
        if bitchmeterValue <= float(maxBitchness) / 100 * 51:
            return bitchmeter_captions[2]
        if bitchmeterValue < float(maxBitchness) / 100 * 60:
            return bitchmeter_captions[3]
        if bitchmeterValue < float(maxBitchness) / 100 * 80:
            return bitchmeter_captions[4]
        if bitchmeterValue < float(maxBitchness) / 100 * 100:
            return bitchmeter_captions[5]
        if bitchmeterValue >= maxBitchness:
            return bitchmeter_captions[6]


    def changeDayTime(dayTime):
        global day_time, day_suffix, day
        if dayTime == day_time:
            return
        if dayTime == "evening":
            day_time = "evening"
            day_suffix = "_Evening"
            return
        if dayTime == "day":
            day_time = "day"
            day_suffix = ""
            day = day + 1
            return
        return

    def get_scene_label(scene_label):
        global sceneStages
        for idx in reversed(range(0, len(sceneStages))):
            if renpy.has_label(scene_label + sceneStages[idx]):
                return scene_label + sceneStages[idx]
        return scene_label
