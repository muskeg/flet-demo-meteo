"""Classes de vues pour l'application météo.

Ce module contient les classes de vues pour l'application météo. Ces classes
sont utilisées pour afficher les conditions actuelles et les prévisions
météorologiques.
"""

from dateutil import tz
import flet as ft
import meteo.conditions as conditions
import meteo.previsions as previsions
import meteo.icones as icones

class VueConditionsActuelles(ft.Container):
    """Vue des conditions météorologiques actuelles."""
    def __init__(self, coord, nom_ville):
        super().__init__()
        self.expand = True
        self._ville = conditions.Conditions(coord)
        self._nom_ville = nom_ville
        self._utczone = tz.tzutc()
        self._localzone = tz.tzlocal()
        self._naive_utc = self._ville.temps_observation
        self._heure_maj = self._naive_utc.astimezone(self._localzone).strftime('%Y-%m-%d %H:%M')
        self.content = ft.Container(
            content = ft.Column(
                controls = [
                    ft.Row(
                        # controls = [
                        #     ft.Text(
                        #         "Conditions actuelles",
                        #         size = 30,
                        #     ),
                        # ],
                        # alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    ft.Row(
                        controls = [
                            ft.Container(
                                content=ft.Text(
                                    f"{self._ville.condition_actuelle}",
                                    size = 18,
                                    text_align = ft.TextAlign.CENTER,
                                ),
                                alignment = ft.alignment.center,
                                expand = True,
                            )
                        ],
                        alignment = ft.MainAxisAlignment.CENTER,
                        expand = True,
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
                                self._ville.temp_actuelle,
                                size = 80,
                            ),
                            ft.Container(
                                ft.Text(
                                    "°C",
                                    size = 25,
                                ),
                                margin = ft.margin.only(top=-15),
                            )
                        ],
                        alignment = ft.MainAxisAlignment.CENTER,
                        expand = True,
                    ),
                    ft.Row(
                        controls = [
                            ft.Container(
                                content = ft.Icon(
                                    ft.icons.COMPRESS,
                                    size = 19,
                                    tooltip = "Pression"
                                ),
                                margin=ft.margin.only(right=-5),
                            ),
                            ft.Text(
                                f"{self._ville.pression_actuelle} kPa",
                                size = 17,
                            ),
                            ft.Container(
                                content = ft.Icon(
                                    ft.icons.AIR,
                                    size = 19,
                                    tooltip = "Vent"
                                ),
                                margin=ft.margin.only(right=-5, left=10),
                            ),
                            ft.Text(
                                f"{self._ville.vent_actuel} km/h",
                                size = 17,
                            ),
                            ft.Container(
                                content = ft.Icon(
                                    ft.icons.WATER_DROP,
                                    size = 19,
                                    tooltip = "Humidité"
                                ),
                                margin = ft.margin.only(right=-5, left=10),
                            ),
                            ft.Text(
                                f"{self._ville.humidite_actuelle}%",
                                size = 17,
                            ),
                        ],
                        alignment = ft.MainAxisAlignment.CENTER,
                        expand = True,
                    ),
                    ft.Row(
                        controls = [
                            ft.Text(
                                f"(m.à.j.: {self._heure_maj})",
                                size = 14,
                            ),
                        ],
                        alignment = ft.MainAxisAlignment.CENTER,
                        expand = True,
                    ),

                ],
            ),
        )

class JourPrevision(ft.Container):
    """Vue d'une prévision météorologique pour une journée."""
    def __init__(self, date, prevision):
        super().__init__()
        # self._date = date.date()
        self._date = date
        self._prevision = prevision.prevision_un_jour(self._date)
        self._max_temp = str(self._prevision['temperature_high'])
        self._min_temp = str(self._prevision['temperature_low'])
        if self._min_temp is None:
            self._min_temp = "-"
        self.padding = ft.padding.symmetric(horizontal = 10, vertical = 20)
        self.border_radius = 25
        self.width = 70
        self.bgcolor = "#0e0f1a"
        self.border = ft.border.all(1, "#0a0a17")
        self.content = ft.Container(
            content = ft.Column(
                controls = [
                    ft.Container(
                        content = ft.Image(
                            src = icones.Icones['ICONE_' + self._prevision['icon_code']].value,
                            height = 25,
                            fit = ft.ImageFit.CONTAIN,
                        ),
                        alignment = ft.alignment.center,
                        margin = ft.margin.only(bottom = 15, top = 10),
                    ),
                    ft.Row(
                        controls = [
                            ft.Text(f"{self._max_temp}°C", size=12, color=ft.colors.WHITE),
                        ],
                        alignment = ft.MainAxisAlignment.CENTER,
                    ),
                    ft.Row(
                        controls = [
                            ft.Text(f"{self._min_temp}°C", size=11, color=ft.colors.BLUE_GREY_400),
                        ],
                        alignment = ft.MainAxisAlignment.CENTER,
                    ),
                    ft.Row(
                        controls = [
                            ft.Text(self._date.strftime('%a')),
                        ],
                        alignment = ft.MainAxisAlignment.CENTER,
                    ),
                ],
                spacing = 4
            ),
        )


class VuePrevisions(ft.Container):
    """Vue des prévisions météorologiques."""
    def __init__(self, coord, nom_ville):
        super().__init__()
        self.expand = True
        self._ville = previsions.Previsions(coord)
        self._nom_ville = nom_ville
        self.content = ft.Container(
            content = ft.Column(
                controls = [
                    # ft.Row(
                    #     controls = [
                    #         ft.Text(f"Prévisions pour {self._nom_ville}", size = 30),
                    #     ],
                    # ),
                    ft.Row(
                        controls = self.__liste_jours(),
                    ),
                ],
            ),
        )

    def __liste_jours(self):
        """Liste des prévisions pour les 5 prochains jours."""
        for date in self._ville.prevision_5_jours:
            yield JourPrevision(date, self._ville)
