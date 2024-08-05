from prac_09.unreliable_car import UnreliableCar

my_unreliable_car = UnreliableCar("BYD", 100, 80)
my_unreliable_car2 = UnreliableCar("TLC", 100, 10)

for i in range(1,7):
    print(f"{my_unreliable_car.name} has driven {my_unreliable_car.drive(i)}")
    print(f"{my_unreliable_car2.name} has driven {my_unreliable_car2.drive(i)}")

print(my_unreliable_car)
print(my_unreliable_car2)

