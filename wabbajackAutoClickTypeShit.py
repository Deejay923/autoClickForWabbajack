import time
import pyautogui

# Configuration
CHECK_INTERVAL = 1

# List of target download button variations
BUTTON_IMAGES = [
    'images/slowDownload.png',
    'images/slowDownload2.png',
    'images/slowDownload3.png',
    'images/slowDownload4.png',
    'images/slowDownload5.png',
    'images/slowdownload6.png',
    'images/slowDownload7.png',
]

# List of archive header trigger variations
TRIGGER_IMAGES = [
    'images/downloadArchive.png',
    'images/downloadArchive2.png',
]

SCROLL_AMOUNT = -300

print("Wabbajack Auto Click Type Shit Engaged")
print("Looping continuously, looking for button type shit. Will scroll when an archive trigger is detected.")
print("Press CTRL+C to stop ya bish")

# Track if we have already handled scrolling for the current visible archive header
has_scrolled_for_current_archive = False

while True:
    try:
        # STEP 1: Scan for ANY matching trigger image
        trigger_location = None
        detected_trigger = None

        for trigger_file in TRIGGER_IMAGES:
            try:
                loc = pyautogui.locateOnScreen(trigger_file, confidence=0.8)
                if loc is not None:
                    trigger_location = loc
                    detected_trigger = trigger_file
                    break
            except (pyautogui.ImageNotFoundException, Exception):
                continue

        # If no archive header is visible, reset the scroll lock for the next one
        if trigger_location is None:
            has_scrolled_for_current_archive = False

        # STEP 2: Scroll ONLY if a trigger is visible AND we haven't scrolled for it yet
        if trigger_location is not None and not has_scrolled_for_current_archive:
            print(f"New trigger '{detected_trigger}' detected! Performing single scroll...")
            pyautogui.scroll(SCROLL_AMOUNT)
            has_scrolled_for_current_archive = True  # Lock until header leaves the screen
            time.sleep(0.6)  # Settle time

        # STEP 3: Continuous check for download buttons
        button_clicked = False
        for image_file in BUTTON_IMAGES:
            try:
                button_location = pyautogui.locateOnScreen(image_file, confidence=0.8)
                if button_location is not None:
                    button_center = pyautogui.center(button_location)
                    print(f"Found {image_file}! Clicking...")
                    pyautogui.click(button_center)

                    button_clicked = True
                    time.sleep(5)  # Rest to allow the download start/page refresh
                    break
            except (pyautogui.ImageNotFoundException, Exception):
                continue

        # If no buttons are clicked, rest before the next cycle
        if not button_clicked:
            time.sleep(CHECK_INTERVAL)

    except KeyboardInterrupt:
        print("\nScript stopped ya bish")
        break
    