from prac_06.guitar import Guitar
# test the correct output
guitar1 = Guitar("Gibson L-5 CES", 1922)
print(f"{guitar1.name} get_age()- Expected 100 Got {guitar1.get_age()}")
print(f"{guitar1.name} is_vintage()- Expected True Got {guitar1.is_vintage()}")

guitar2 = Guitar("Another Guitar", 2013)
print(f"{guitar2.name} get_age()- Expected 9 Got {guitar2.get_age()}")
print(f"{guitar2.name} is_vintage()- Expected False Got {guitar2.is_vintage()}")