# Tab Switch Tracker

A **cross-platform Python script** that tracks which application/window is active on your computer and logs:

- Timestamp
- Previous window
- Current window
- Duration spent on each window

This project is useful for **productivity tracking**, **time management**, or learning Python automation.

---

## Features

- Fully **cross-platform**: works on Windows, macOS, and Linux
- Tracks **process name** + **window title**
- Logs time spent per window (duration)
- Saves logs in **CSV format**
- Modular code structure:
  - `init_csv.py` → initializes CSV with headers
  - `track_window.py` → runs the tracker and appends logs

---

## Installation

1. **Clone the repository:**

```bash
git clone https://github.com/yourusername/tab-switch-tracker.git
cd tab-switch-tracker


2. ** Create a virtual environment **

python -m venv venv

3. ** Activate the virtual environment **

Windows:
```bash
venv\Scripts\activate


MacOS/Linux
source venv/bin/activate


4. ** Install dependencies **

pip install -r windowSwitchReq.txt

--

## Usage

1. ** Initialize CSV file (only needed once) **

```bash
python init_csv.py

2. ** Start tracking windows: **

```bash
python track_window.py

3. ** top tracking: Press CTRL + C **

- Logs are saved in window_log.csv with columns:
    - Time, Previous Window, Current Window, Duration (s)
    