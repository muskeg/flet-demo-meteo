"""Classes pour les conditions actuelles

"""
import asyncio
from env_canada import ECWeather

class Conditions:
    """Classe des conditions météorologiques actuelles"""
    def __init__(self, coordonnees):
        self._api = ECWeather(coordinates=coordonnees, language="french")
        self.maj()

    def maj(self):
        """Mise à jour des conditions actuelles"""
        asyncio.run(self._api.update())

    @property
    def temp_actuelle(self):
        """Température actuelle"""
        self.maj()
        return self._api.conditions['temperature']['value']

    @property
    def condition_actuelle(self):
        """Condition actuelle"""
        self.maj()
        return self._api.conditions['condition']['value']

    @property
    def code_icone(self):
        """Icône pour la condition actuelle"""
        self.maj()
        return self._api.conditions['icon_code']['value']

    @property
    def humidite_actuelle(self):
        """Humidité actuelle"""
        self.maj()
        return self._api.conditions['humidity']['value']

    @property
    def pression_actuelle(self):
        """Pression actuelle"""
        self.maj()
        return self._api.conditions['pressure']['value']

    @property
    def vent_actuel(self):
        """Vitesse du vent actuelle"""
        self.maj()
        return self._api.conditions['wind_speed']['value']

    @property
    def temps_observation(self):
        """Temps de l'observation"""
        self.maj()
        return self._api.conditions['observationTime']['value']
