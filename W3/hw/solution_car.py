import csv
import os
import sys

ext_list = [".jpg", ".jpeg", ".png", ".gif"]


class CarBase:
    def __init__(self, car_type, brand, carrying, photo_file_name=None):
        self.car_type = car_type
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = carrying

    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)[1]


class Car(CarBase):
    def __init__(self, car_type, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(car_type, brand, photo_file_name, carrying)
        try:
            self.passenger_seats_count = passenger_seats_count
        except ValueError:
            pass


class Truck(CarBase):
    def __init__(self, car_type, brand, photo_file_name, carrying, body_whl):
        super().__init__(car_type, brand, photo_file_name, carrying)
        param = body_whl.split("x")
        try:
            self.body_length = float(param[0])
            self.body_width = float(param[1])
            self.body_height = float(param[2])
        except ValueError:
            pass

    def get_body_volume(self):
        return self.body_length * self.body_width * self.body_height


class SpecMachine(CarBase):
    def __init__(self, car_type, brand, photo_file_name, carrying, extra):
        super().__init__(car_type, brand, photo_file_name, carrying)
        try:
            self.extra = extra
        except ValueError:
            pass

def get_car_list(csv_filename):
    with open(csv_filename, encoding='utf-8') as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)  # пропускаем заголовок
        car_list = []
        for row in reader:
            try:
                if row[0] == "car":
                    car_list.append(Car(row[0], row[1], row[5], row[3], row[2]))
                if row[0] == "truck":
                    car_list.append(Truck(row[0], row[1], row[5], row[3], row[4]))
                if row[0] == "spec_machine":
                    car_list.append(SpecMachine(row[0], row[1], row[5], row[3], row[6]))
            except:
                pass

    return car_list


def _main():
    path = sys.argv[1]
    cars = get_car_list(path)
    print(len(cars))
    for car in cars:

        try:
            print(car.get_body_volume())
        except:
            pass


if __name__ == "__main__":
    _main()