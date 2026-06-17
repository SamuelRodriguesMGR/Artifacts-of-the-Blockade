# Вы можете расположить сценарий своей игры в этом файле.


image TanyaW = "images/TanyaW.jpg"
image TanyaL = "images/TanyaL.jpg"
image diary_Jenya = "images/diary_Jenya.jpg"
image diary_grand = "images/diary_grand.jpg"

default selected_chapter = ""

# Игра начинается здесь:

label start:
    call prologue from _call_prologue

    jump chapter_hub


screen chapter_select():

    imagemap:
        ground "images/artifacts.JPG"
        hover "images/artifacts.JPG"

        hotspot (100, 200, 280, 340) action [
            SetVariable("selected_chapter", "bread"),
            Jump("confirm_chapter")
        ]
        hotspot (500, 200, 280, 340) action [
            SetVariable("selected_chapter", "metronom"),
            Jump("confirm_chapter")
        ]
        hotspot (850, 200, 240, 340) action [
            SetVariable("selected_chapter", "flask"),
            Jump("confirm_chapter")
        ]
        hotspot (1200, 200, 240, 340) action [
            SetVariable("selected_chapter", "sledge"),
            Jump("confirm_chapter")
        ]
        hotspot (1480, 209, 100, 130) action [
            SetVariable("selected_chapter", "diary_tani"),
            Jump("confirm_chapter")
        ]
        hotspot (1610, 200, 240, 340) action [
            SetVariable("selected_chapter", "toys"),
            Jump("confirm_chapter")
        ]

label confirm_chapter:

    "Начать эту главу?"

    if chapters[selected_chapter] == 0:
        menu:
            "Изучить артефакт":
                $ chapters[selected_chapter] = 1
                $ renpy.jump(selected_chapter)

            "Пройти мимо":
                $ chapters[selected_chapter] = 2
    
    elif chapters[selected_chapter] == 1:
        "Я уже посмотрел его"

    else:
        "Мне он не интересен"

    jump chapter_hub



label chapter_hub:
    scene artifacts

    $ uncompleted = sum(1 for chapter in chapters.values() if chapter != 0)

    if uncompleted >= 5:

        $ completed = sum(1 for chapter in chapters.values() if chapter == 1)
        "Пройдено [completed] глав."

        if completed == 2:
            jump ending2
        elif completed == 3:
            jump ending3
        elif completed == 4:
            jump ending4
        elif completed == 5:
            jump ending5
        elif completed == 6:
            jump ending6
        else:
            jump ending1


    else:
        call screen chapter_select

    jump chapter_hub