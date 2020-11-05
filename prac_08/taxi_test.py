from prac_08.taxi import Taxi

prius_taxi = Taxi('Prius 1', 100)

prius_taxi.drive(40)
print('Current fare is ${}'.format(prius_taxi.get_fare()))

prius_taxi.add_fuel(40)
prius_taxi.start_fare()
prius_taxi.drive(100)
print('Current fare is ${}'.format(prius_taxi.get_fare()))
