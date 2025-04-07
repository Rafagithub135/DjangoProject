import platform

def main():
    message()

def message():
        print("The current version of Python is:  {}" . format(platform.python_version()))

if __name__ == "__main__":
    main()