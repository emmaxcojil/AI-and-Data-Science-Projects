import csv
import analysis
import tui
import pandas as pd
import os

def load_file():
    data, df = None, None
    path = input("Please enter absolute path to CSV data or [exit]: ").strip()
    if path == "exit":
        return data, df
    try:
        if not os.path.exists(path):
            raise Exception("Invalid path entered")
        data = read_data(path)
        df = pd.read_csv(path)
        return (data, df)
    except Exception as e:
        tui.error(e.args[-1])
        return data, df

def read_data(file_path):
    tui.started(f"Reading data from {file_path}")
    data = []
    with open(file_path) as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for line in csv_reader:
            data.append(line)
    tui.completed("File loaded successfully")
    return data

def check_data_loaded(data_list):
    if data_list == None:
        return False
    return True
    

def get_car_by_id(data_list, data_df):
    if not check_data_loaded(data_list):
        tui.error("No Data Loaded. Load data to retrieve car.")
        return
    try:
        data_list_len = len(data_list)
        car_id = int(input("Enter car ID: "))
        # check if car_id < 1 and > data_list_len
        # print("data_list_len", data_list_len, "car ID", car_id)
        if car_id < 1 or car_id > data_list_len:
            raise Exception("Car not found")
        analysis.get_car_by_id(car_id, data_list, data_df)
    except ValueError:
        tui.error("Enter a valid integer ID")
    except Exception as err:
        tui.error(err.args[-1])


def get_cars_by_cylinder_number(data_list, data_df):
    if not check_data_loaded(data_list):
        tui.error("No Data Loaded. Load data to retrieve car.")
        return
    try:
        cylinder_number = int(input("Enter car by cylinder_number: "))
        # check if car_id < 1 and > data_list_len
        # print("data_list_len", data_list_len, "car ID", car_id)
        if cylinder_number < 1 or cylinder_number > 12:
            raise Exception("Car not found")
        analysis.get_cars_by_cylinder_number(cylinder_number, data_list, data_df)
    except ValueError:
        tui.error("Enter a valid integer ID")
    except Exception as err:
        tui.error(err.args[-1])

def run():
    carprice_data = None
    carprice_df = None

    while True:
        selection = tui.menu()
        #print(selection)
        if selection == "load_file":
            carprice_data, carprice_df = load_file()
            #print(type(carprice_data))
            #print(carprice_data)
        elif selection == "carbyid":
            get_car_by_id(carprice_data, carprice_df)
        elif selection == "cylindernumber":
            get_cars_by_cylinder_number(carprice_data, carprice_df)
        elif selection == "exit":
            break
        else:
            tui.error("Invalid Selection!")

if __name__ == "__main__":
    run()