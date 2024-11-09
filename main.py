"""Démo du framework Flet avec l'API d'Environnement Canada pour la météo.

Ce script est une démo de l'utilisation du framework Flet pour créer une
application web simple qui affiche les prévisions météorologiques d'Environnement
Canada pour une station météo donnée.
"""

import flet as ft
import meteo.conditions as conditions
import meteo.previsions as previsions


def main(page: ft.Page):
    page.title = "Météo"
    page.padding = ft.padding.all(40)
    page.window.width = 800
    page.window.height = 300
    page.window.resizable = False
    page.add(ft.SafeArea(ft.Text("Hello, Flet!")))
    page.add(ft.Text("Hello, Flet!"))
    meteo_montreal = conditions.Conditions((45.50884, -73.58781))
    print(meteo_montreal.temp_actuelle)
    # print(test_meteo.hourly_forecasts)


ft.app(target=main, assets_dir="assets")

if __name__ == "__main__":
    main(page = ft.Page)