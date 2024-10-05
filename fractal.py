import turtle


def koch_snowflake_segment(t, length, level):
    if level == 0:
        t.forward(length)
    else:
        length /= 3.0
        koch_snowflake_segment(t, length, level - 1)
        t.left(60)
        koch_snowflake_segment(t, length, level - 1)
        t.right(120)
        koch_snowflake_segment(t, length, level - 1)
        t.left(60)
        koch_snowflake_segment(t, length, level - 1)


def koch_snowflake(t, length, level):
    for _ in range(3):
        koch_snowflake_segment(t, length, level)
        t.right(120)


def main():
    try:
        level = int(input("Введіть рівень рекурсії для сніжинки Коха (ціле число): "))

        if level < 0:
            print("Рівень рекурсії не може бути негативним.")
            return

    except ValueError:
        print("Введено некоректне значення. Введіть ціле число.")
        return

    screen = turtle.Screen()
    screen.bgcolor("white")
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-150, 90)
    t.pendown()

    koch_snowflake(t, 300, level)

    t.hideturtle()
    screen.mainloop()


if __name__ == "__main__":
    main()
