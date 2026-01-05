import csv
import time
from datetime import datetime
import pygetwindow as gw
from csv_init import csv_file, fieldnames

def log_windows(CSV_FILE=csv_file):
    
    last_window = None
    try:
        while True:
            active_window = gw.getActiveWindow()
            if active_window is None:
                time.sleep(0.5)
                continue

            current_window_title = active_window.title
            if last_window != current_window_title:
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                
                # APPEND TO CSV FILE
                with open(CSV_FILE, 'a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([fieldnames])

                print(f"{timestamp}: {last_window} >> {current_window_title}")
                last_window = current_window_title

            time.sleep(0.5)

    except KeyboardInterrupt as KI:
        print(f"{KI} : Window tracking stopped by user.")

if __name__ == "__main__":
    log_windows()