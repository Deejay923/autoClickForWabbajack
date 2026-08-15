# Wabbajack Auto Click Type Shit

An automated script for clicking download buttons and scrolling through archive headers in Wabbajack.

## What It Does

This script continuously monitors the screen for:
- **Download buttons** — automatically clicks them when detected
- **Archive headers** — scrolls down when a new header appears

Perfect for automating repetitive clicking and scrolling tasks during Wabbajack installations.

## Requirements

- Python 3.x
- `pyautogui` library
  ```bash
  pip install pyautogui
  ```

## Setup

1. Place your button and trigger images in the same directory as the script:
   - **Download buttons**: `slowDownload.png`, `slowDownload2.png`, etc.
   - **Archive headers**: `downloadArchive.png`, `downloadArchive2.png`

2. Adjust the image file names in the script if your images are named differently.

3. Fine-tune detection:
   - `CHECK_INTERVAL` — delay between checks (default: 1 second)
   - `SCROLL_AMOUNT` — scroll distance (default: -300)
   - `confidence=0.8` — image matching sensitivity (adjust if needed)

## Usage

```bash
python wabbajackAutoClickTypeShit.py
```

The script will:
- Loop continuously, scanning for download buttons
- Scroll once when it detects a new archive header
- Click any download button it finds
- Rest for 5 seconds after clicking to allow page refresh

Press **CTRL+C** to stop the script.

## Notes

- Requires screen capture permissions (works on Windows with `pyautogui`)
- Images must be visible on screen at detection time
- Uses 0.8 confidence threshold for image matching; adjust if getting false positives/negatives
