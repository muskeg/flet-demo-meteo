import flet as ft
from env_canada import ECWeather
import meteo.conditions as conditions
import meteo.previsions as previsions


def main(page: ft.Page):
    page.add(ft.SafeArea(ft.Text("Hello, Flet!")))

    test_meteo = ECWeather(coordinates=(45.630001, -73.519997))


ft.app(main)
