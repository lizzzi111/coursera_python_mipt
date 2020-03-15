#!/usr/bin/env python
# coding: utf-8

# In[27]:


class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = carrying

    def get_photo_file_ext():
        return os.path.splitext(self.photo_file_name)[1]

class Car(CarBase):
    
    car_type = 'car'
    
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super(Car, self).__init__(brand, photo_file_name, carrying)
        self.passenger_seats_count = passenger_seats_count


class Truck(CarBase):
    
    car_type = 'truck'
    
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super(Truck, self).__init__(brand, photo_file_name, carrying)
        if body_whl=='NotValid':
            self.body_length = 0.0
            self.body_width = 0.0
            self.body_height = 0.0
        else:
            characteristics = body_whl.split('x')
            self.body_length = characteristics[0]
            self.body_width = characteristics[1]
            self.body_height = characteristics[2]
    
    def get_body_volume(self):
        return self.body_length * self.body_width * self.body_height

class SpecMachine(CarBase):
    
    car_type = 'specmachine'
    
    def __init__(self, brand, photo_file_name, carrying, extra):
        super(SpecMachine, self).__init__(brand, photo_file_name, carrying)
        self.extra = extra


# In[59]:


def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)  # пропускаем заголовок
        for row in reader:
            if len(row) < 7:
                continue
            if row[0] == 'car':
                #def __init__(self, brand, photo_file_name, carrying, passenger_seats_count)
                car = Car(row[1], row[3], float(row[5]), row[2])
            elif row[0] == 'truck':
                
                try:
                    slit = row[4].split('x')[1]
                    body_whl = row[4]
                except:
                    body_whl = 'NotValid'
                #__init__(self, brand, photo_file_name, carrying, body_whl)
                car = Truck(row[1], row[3], float(row[5]), body_whl)
            elif row[0] == 'spec_machine':
                #brand, photo_file_name, carrying, extra
                car = SpecMachine(row[1], row[3], float(row[5]), row[6])
            else:
                continue
            car_list.append(car)
    return car_list


# In[65]:


if __name__ == '__main__':
    cars = get_car_list('coursera_week3_cars.csv')
    for car in cars:
        print(car.brand)

