
# Experiment No. 09
# WAP to Implement Mutual Exclusion Algorithm

from threading import Timer, Lock

cs = 0
pro = 1
current_process = None
timer = None

lock = Lock()


def exit_process():
    global cs, current_process, timer

    with lock:
        if cs == 1:
            print("\nProcess", current_process,
                  "exited Critical Section.")

            if timer is not None:
                timer.cancel()
                timer = None

            cs = 0
            current_process = None


def enter_process():
    global cs, pro, current_process, timer

    with lock:
        if cs == 0:
            current_process = pro
            cs = 1

            print("\nProcess", pro,
                  "entered Critical Section.")

            print("Process will automatically exit after 5 seconds.")
            print("Press e to exit earlier.")

            timer = Timer(5, exit_process)
            timer.daemon = True
            timer.start()

            pro += 1

        else:
            print("\nError: Another process is currently executing!")


print("===== MUTUAL EXCLUSION ALGORITHM =====")

while True:

    print("\n1 - Enter Critical Section")
    print("e - Exit Critical Section")
    print("q - Quit Program")

    choice = input("Enter your choice: ").lower().strip()

    if choice == '1':
        enter_process()

    elif choice == 'e':
        with lock:
            occupied = (cs == 1)

        if occupied:
            exit_process()
        else:
            print("\nNo process is currently executing.")

    elif choice == 'q':
        exit_process()
        print("\nProgram terminated.")
        break

    else:
        print("\nInvalid choice! Please try again.")
