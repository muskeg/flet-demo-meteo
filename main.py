import asyncio
import flet as ft
from env_canada import ECWeather
import meteo.conditions as conditions
import meteo.previsions as previsions


def main(page: ft.Page):
    page.add(ft.SafeArea(ft.Text("Hello, Flet!")))

    test_meteo = ECWeather(coordinates=(45.50884, -73.58781))
    asyncio.run(test_meteo.update())
    print(test_meteo.station_id)
    print(test_meteo.hourly_forecasts)

ft.app(main)
