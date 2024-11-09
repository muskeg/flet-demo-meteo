"""Démo du framework Flet avec l'API d'Environnement Canada pour la météo.

Ce script est une démo de l'utilisation du framework Flet pour créer une
application web simple qui affiche les prévisions météorologiques d'Environnement
Canada pour une station météo donnée.
"""

import asyncio
import flet as ft
from env_canada import ECWeather
import meteo.conditions as conditions
import meteo.previsions as previsions


def main(page: ft.Page):
    page.title = "Météo"
    page.padding = ft.padding.all(40)
    page.window.width = 800
    page.window.height = 300
    page.window.resizable = False
    page.add(ft.SafeArea(ft.Text("Hello, Flet!")))
    test_meteo = ECWeather(coordinates=(45.50884, -73.58781), language="french")
    asyncio.run(test_meteo.update())
    weather = test_meteo.hourly_forecasts
    # weather = test_meteo.hourly_forecasts[0]
    print(weather[0]['condition'])
    print(weather[0]['icon_code'])
    print(test_meteo.station_id)
    # print(test_meteo.hourly_forecasts)


ft.app(target=main, assets_dir="assets")

if __name__ == "__main__":
    main(page = ft.Page)