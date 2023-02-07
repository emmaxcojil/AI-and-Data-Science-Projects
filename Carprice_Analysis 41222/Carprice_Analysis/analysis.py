import tui

def get_car_feature_to_position_map():
    return {
        "car_ID": 0,
        "CarName": 1, "fueltype": 2, "doornumber":3, "carbody": 4,
        "drivewheel": 5, "enginelocation": 6, "wheelbase": 7,
        "carlength":8, "carwidth": 9, "carheight": 10,
        "curbweight": 11, "enginetype": 12, "cylindernumber":13, "enginesize": 14,
        "fuelsystem": 15, "horsepower": 16, "citympg": 17, "highwaympg": 18,
        "price": 19
    }

def get_car_by_id(car_id, carprice_data, carprice_df):
    print(carprice_df[carprice_df["car_ID"] == car_id].T)

def get_car_by_id2(car_id, carprice_data, carprice_df):
    selected_car = None
    # iterate picking car rows (individual lists) from
    # carprice_data (List of lists)
    column_to_index_map = get_car_feature_to_position_map()
    for car in carprice_data:
        # car ID is the first column. 
        # lists support zero-based indexing 
        # i.e. they count from 0 to the length of the list - 1
        # print(car, car_id)
        if int(car[column_to_index_map["car_ID"]].strip()) == car_id:
            selected_car = car
            break
    if selected_car == None:
        raise Exception("Car Not Found")
    tui.started()
    tui.display_car(selected_car, column_to_index_map)
    tui.completed()


def get_cars_by_cylinder_number(cylinder_number, carprice_data, carprice_df):
    # initialize to empty list to get car rows
    # would be a list of lists
    selected_cars = []
    ci_map = get_car_feature_to_position_map()
    # iterate picking car rows (individual lists) from
    # carprice_data (List of lists)
    for car in carprice_data:
        # car ID is the first column.
        # lists support zero-based indexing
        # i.e. they count from 0 to the length of the list - 1
        # print(car, car_id)
        if int(car[ci_map["cylindernumber"]].strip()) == cylinder_number:
            selected_cars.append(car)
    
    if len(selected_cars) == 0:
        raise Exception("No cars with specified cylindernumber")
    tui.started()
    tui.display_cars(selected_cars, ci_map)
    tui.completed()