# Вы можете расположить сценарий своей игры в этом файле.


image TanyaW = "images/TanyaW.jpg"
image TanyaL = "images/TanyaL.jpg"
image diary_Jenya = "images/diary_Jenya.jpg"
image diary_grand = "images/diary_grand.jpg"


# Игра начинается здесь:
label start:
    # call prologue from _call_prologue
    # call bread from _call_bread
    # call metronom from _call_metronom
    # call flask from _call_flask
    call diary_tani from _call_diary_tani
    

    # e "Hello world"

    # show eileen
    # with dissolve

    # e "Вы создали новую игру Ren'Py."

    # hide eileen

    # e "Добавьте сюжет, изображения и музыку и отправьте её в мир!"

    # menu:
    #     "Кто я?":
    #         e "хз"
    #     "Я тебя помню":
    #         e "сдаюсь"

    return
