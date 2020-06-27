import csv
import os


class CarBase:

    def __init__(self, brand, photo_file_name, carrying):

        ext_list = [".jpg", ".jpeg", ".png", ".gif"]

        self.brand = brand
        if self.get_photo_file_ext() in ext_list:
            self.photo_file_name = photo_file_name
        try:
            self.carrying = float(carrying)
        except ValueError:
            pass

    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)[1]


class Car(CarBase):

    car_type = 'car'

    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        try:
            super(Car, self).__init__(brand, photo_file_name, carrying)
        except AttributeError:
            pass
        try:
            self.passenger_seats_count = int(passenger_seats_count)
        except ValueError:
            pass


class Truck(CarBase):

    car_type = 'truck'

    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super(Truck, self).__init__(brand, photo_file_name, carrying)
        if body_whl:
            param = body_whl.split("x")
            if len(param) == 3:
                self.body_length = float(param[0])
                self.body_width = float(param[1])
                self.body_height = float(param[2])
            else:
                self.body_length = self.body_width = self.body_height = 0.0
        else:
            self.body_length = self.body_width = self.body_height = 0.0

    def get_body_volume(self):
        return self.body_length * self.body_width * self.body_height


class SpecMachine(CarBase):

    car_type = 'spec_machine'

    def __init__(self, brand, photo_file_name, carrying, extra):
        super(SpecMachine, self).__init__(brand, photo_file_name, carrying)
        self.extra = extra


def get_car_list(csv_filename):
    with open(csv_filename, encoding='utf-8') as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)  # пропускаем заголовок
        car_list = []
        for row in reader:
            try:
                if row[0] == "car":
                    car_list.append(Car(row[1], row[5], row[3], row[2]))
                if row[0] == "truck":
                    car_list.append(Truck(row[1], row[5], row[3], row[4]))
                if row[0] == "spec_machine":
                    car_list.append(SpecMachine(row[1], row[5], row[3], row[6]))
            except Exception:
                pass

    return car_list