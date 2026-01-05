import csv

csv_file = 'window_log.csv'
fieldnames = ['timestamp', 'window_title', 'duration', 'is_active']

def csv_init(file_path=csv_file):
    try:
        # "X" MODE OPENS A FILE FOR EXCLUSIVE CREATION, FAILS IF THE FILE ALREADY EXISTS
        with open(csv_file, 'x', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(fieldnames)
    except FileExistsError as FE:
        print(f"{FE} : The file '{file_path}' already exists. Initialization skipped.")
        pass

if __name__ == "__main__":
    csv_init()