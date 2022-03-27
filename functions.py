import fastf1
import fastf1.plotting

def get_fastests_d_v(driver, session):
    fast = session.laps.pick_driver(driver).pick_fastest()
    car_data = fast.get_car_data().add_distance()
    d = car_data['Distance']
    v = car_data['Speed']
    return d, v