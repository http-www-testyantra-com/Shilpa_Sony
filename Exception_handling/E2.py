def get_value():
    try:
        a = int(input("enter value a "))
        b = a - int(input("enter value b "))
        return a,b
    except ValueError as e:
        print(e)
        return get_value()
    finally:
        print("finally of get_value")

def divison(a,b):
    try:
        c = a/b
        return c
    except ZeroDivisionError as e:
        print(e)
    finally:
        print("finally of div")
def main():
    try:
        a,b = get_value()
        c = divison(a,b)
        print(c)

    except ZeroDivisionError as e:
        print(e)
        main()
    except Exception as e:
        print(e)
        main()
    finally:
        print("process completed")
if __name__ == '__main__':
    main()



