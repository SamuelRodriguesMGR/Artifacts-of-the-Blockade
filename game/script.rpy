# Вы можете расположить сценарий своей игры в этом файле.


# Игра начинается здесь:
label start:
    call prologue from _call_prologue
    # call bread from _call_bread
    call metronom from _call_metronom

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
