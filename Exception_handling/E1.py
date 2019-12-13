#exception
def main():
    try:
        return 10
    except:
        return 20
    finally:
        return 30

if __name__ == '__main__':
    print(main())