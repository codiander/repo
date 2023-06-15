def func():
    myschedule=[]
    import schedule
    import time
    import win10toast

    not1 = win10toast.ToastNotifier()

    choice = "yes"
    while choice == "yes":
        title = input("enter the title:")
        message = input("enter the message:")
        tim = input("enter the time:")
        ms = [title, message, tim]
        myschedule.append(ms)

        choice = input("enter your choice:")
        while choice == "yes":
            title = input("enter the title:")
            message = input("enter the message:")
            tim = input("enter the time:")
            ms = [title, message, tim]
            try:
                myschedule.append(ms)
                choice = input("enter your choice:")

            except:
                pass

    for i in myschedule:

        def functionmaker():
            not1.show_toast(i[0], i[1], duration=12)

        schedule.every().day.at(i[2]).do(functionmaker)

        while True:
            schedule.run_pending()

func()