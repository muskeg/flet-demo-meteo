"""Démo du framework Flet avec l'API d'Environnement Canada pour la météo.

Ce script est une démo de l'utilisation du framework Flet pour créer une
application web simple qui affiche les prévisions météorologiques d'Environnement
Canada pour une station météo donnée.
"""

import flet as ft
from meteo.vues import VueConditionsActuelles, VuePrevisions
class TemperatureVille(ft.Container):
    """Classe de présentation principale"""
    def __init__(self):
        super().__init__()
        self._nom_ville = "Montréal"
        self._coord_ville = (45.50884, -73.58781)
        self.affiche_layout()

    def affiche_layout(self):
        """Fonction qui affiche le layout."""
        self._dropdown_ville = ft.Dropdown(
            width=270,
            on_change=self.drop_change,
            label = "Ville",
            options=[
                ft.dropdown.Option(text="Montréal"),
                ft.dropdown.Option(text="Québec"),
                ft.dropdown.Option(text="Iqaluit"),
            ],
        )
        self._dropdown_ville.value = self._nom_ville
        self._conditions_ville = VueConditionsActuelles(self._coord_ville, self._nom_ville)
        self._prevision_ville = VuePrevisions(self._coord_ville, self._nom_ville)
        self.content = ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.Text(
                            f"Météo {self._nom_ville}",
                            size=40,
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Row(
                    controls = [
                        self._conditions_ville,
                    ],
                    alignment = ft.MainAxisAlignment.CENTER,
                ),
                ft.Row(
                    controls = [
                        self._prevision_ville,
                    ],
                    alignment = ft.MainAxisAlignment.CENTER,
                ),
                ft.Row(
                    controls = [
                        self._dropdown_ville
                    ],
                ),
                ft.Container(
                margin = ft.margin.only(top = -20),
                content = ft.Row(
                        controls = [
                            ft.ElevatedButton(
                                content = ft.Container(
                                    content = ft.Row(
                                        controls = [
                                            ft.Icon(
                                                ft.icons.REFRESH,
                                                size = 22,
                                            ),
                                            ft.Text(
                                                "Rafraichir",
                                                size = 18,
                                            ),
                                        ],
                                        alignment = ft.MainAxisAlignment.CENTER,
                                        expand = True,
                                    ),
                                    height = 45,
                                    width = 135,
                                    margin = ft.margin.only(left = -13),
                                ),
                            ),
                        ],
                    ),
                ),
            ],
            spacing = 40,
        )

    def drop_change(self, event):
        """Fonction qui gère le changement de la ville sélectionnée dans le dropdown."""
        if event.data == "Montréal":
            self._nom_ville = "Montréal"
            self._coord_ville = (45.50884, -73.58781)
        elif event.data == "Québec":
            self._nom_ville = "Québec"
            self._coord_ville = (46.8131, -71.2075)
        elif event.data == "Iqaluit":
            self._nom_ville = "Iqaluit"
            self._coord_ville = (63.74944, -68.52167)
        else:
            pass
        self.affiche_layout()
        self.update()

    def clic_bouton(self, _):
        """Fonction qui gère le clic sur le bouton de rafraichissement."""
        self.affiche_layout()
        self.update()

def main(page: ft.Page):
    """Fonction d'orchestration de l'application météo."""
    page.theme_mode = "dark"
    page.title = "Météo"
    page.padding = ft.padding.all(0)
    page.window.width = 500
    page.window.height = 800
    page.window.resizable = False
    page.window.maximizable = False
    page.window.title_bar_hidden = True
    interface = TemperatureVille()
    page.add(
        ft.Row(
            [
                    ft.WindowDragArea(
                        ft.Container(
                            ft.Text("Météo Flet"),
                            padding=10
                        ),
                        expand=True,
                        maximizable = False,
                    ),
                    ft.IconButton(
                        ft.icons.CLOSE,
                        padding = 10,
                        on_click=lambda _: page.window.close()
                    )
            ],
        ),
    )
    page.add(
        ft.Container(
            content = interface,
            padding = ft.padding.all(40),
        ),
    )

ft.app(target=main, assets_dir="assets")

if __name__ == "__main__":
    main(page = ft.Page)
