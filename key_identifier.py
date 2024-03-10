from pynput import keyboard

# Define a function to be called when a key is pressed
def on_press(key):
    try:
        print(f'Key {key} pressed')
    except AttributeError:
        print(f'Special key {key} pressed')

# Create a listener for keyboard events
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()  # Join the listener to the main thread to keep it running
