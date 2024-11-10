"""Démo du framework Flet avec l'API d'Environnement Canada pour la météo.

Ce script est une démo de l'utilisation du framework Flet pour créer une
application web simple qui affiche les prévisions météorologiques d'Environnement
Canada pour une station météo donnée.
"""

from datetime import datetime
from dateutil import tz
import flet as ft
import meteo.conditions as conditions
import meteo.previsions as previsions
import meteo.icones as icones


class VueConditionsActuelles(ft.Container):
    def __init__(self, coord, nom_ville):
        super().__init__()
        self._ville = conditions.Conditions(coord)
        self._nom_ville = nom_ville
        self._utczone = tz.tzutc()
        self._localzone = tz.tzlocal()
        self._naive_utc = self._ville.temps_observation
        self._heure_maj = self._naive_utc.astimezone(self._localzone).strftime('%Y-%m-%d %H:%M')
        print(icones.Icones['ICONE_' + self._ville.icone_actuelle].value)
        self.content = ft.Container(
            content = ft.Column(
                controls = [
                    ft.Row(
                        controls = [
                            ft.Text(
                                 "Conditions actuelles",
                                 size = 30,
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    ft.Row(
                        controls = [
                            ft.Container(
                                content=ft.Text(
                                    f"{self._ville.condition_actuelle}",
                                    size = 14,
                                ),
                                padding=ft.padding.only(top=15, bottom=0),
                                margin=ft.margin.only(bottom=-15),
                            )
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    ft.Row(
                        controls = [
                            ft.Container(
                                ft.Image(
                                    src = icones.Icones['ICONE_' + self._ville.icone_actuelle].value,
                                    height = 100,
                                    fit = ft.ImageFit.CONTAIN,
                                ),
                            ),
                            ft.Text(
                                f"{self._ville.temp_actuelle}°C",
                                size = 60,
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    ft.Row(
                        controls = [
                            ft.Container(
                                content = ft.Icon(
                                    ft.icons.COMPRESS,
                                    size = 12,
                                    tooltip = "Pression"
                                ),
                                margin=ft.margin.only(right=-5),
                            ),
                            ft.Text(
                                f"{self._ville.pression_actuelle} kPa",
                                size = 12,
                            ),
                            ft.Container(
                                content = ft.Icon(
                                    ft.icons.AIR,
                                    size = 12,
                                    tooltip = "Vent"
                                ),
                                margin=ft.margin.only(right=-5, left=10),
                            ),
                            ft.Text(
                                f"{self._ville.vent_actuel} km/h",
                                size = 12,
                            ),
                            ft.Container(
                                content = ft.Icon(
                                    ft.icons.WATER_DROP,
                                    size = 12,
                                    tooltip = "Humidité"
                                ),
                                margin=ft.margin.only(right=-5, left=10),
                            ),
                            ft.Text(
                                f"{self._ville.humidite_actuelle}%",
                                size = 12,
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    ft.Row(
                        controls = [
                            ft.Text(
                                f"Observé à {self._nom_ville} / {self._heure_maj}",
                                size = 12,
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),

                ],
            ),
        )

def main(page: ft.Page):
    print(list(icones.Icones))
    print(icones.Icones.ICONE_00.value)
    print(icones.Icones.ICONE_00.name)
    print(icones.Icones["ICONE_00"].value)
    page.title = "Météo"
    page.padding = ft.padding.all(40)
    page.window.width = 800
    page.window.height = 800
    page.window.resizable = False
    montreal = (45.50884, -73.58781)
    conditions_montreal = VueConditionsActuelles(montreal, "Montréal")
    page.add(conditions_montreal)

    # print(test_meteo.hourly_forecasts)


ft.app(target=main, assets_dir="assets")

if __name__ == "__main__":
    main(page = ft.Page)