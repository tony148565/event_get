

def types_trans(tt):
    types = ["noType", "Learning", "Arts", "CategoryEnum.Investm", "Sports", "Family", "Health", "Business", "Outdoor",
             "Other", "CategoryEnum.Startup", "Photography", "CategoryEnum.Handmad", "CategoryEnum.Design",
             "Entertainment"]
    chinese_types = ["旅遊", "學習", "藝文", "演出", "展覽", "其他", "運動", "娛樂"]
    translate_types = ["Tourism", "Learning", "Arts", "Show", "Exhibition", "Other", "Sports", "Entertainment"]
    flag = 0
    for i, j in zip(chinese_types, translate_types):
        if tt == i:
            tt = j
    for i in types:
        if tt == i:
            flag = 1
            break
    if flag == 0:
        tt = types[0]
    return tt

