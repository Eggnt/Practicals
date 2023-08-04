from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    my_silver_service_taxi = SilverServiceTaxi("Fancy Taxi", 100, 2)
    my_silver_service_taxi.drive(18)
    print(f"{my_silver_service_taxi}\nCurrent Fare: {my_silver_service_taxi.get_fare()}")


main()
