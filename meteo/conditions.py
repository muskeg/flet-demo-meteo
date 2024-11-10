"""Classes pour les conditions actuelles

"""
import asyncio
from env_canada import ECWeather

class Conditions:
    def __init__(self, coordonnees):
        self._api = ECWeather(coordinates=coordonnees, language="french")
        self.maj()

    def maj(self):
        asyncio.run(self._api.update())

    @property
    def temp_actuelle(self):
        self.maj()
        return self._api.conditions['temperature']['value']

    @property
    def condition_actuelle(self):
        self.maj()
        return self._api.conditions['condition']['value']

    @property
    def icone_actuelle(self):
        self.maj()
        return self._api.conditions['icon_code']['value']

    @property
    def humidite_actuelle(self):
        self.maj()
        return self._api.conditions['humidity']['value']

    @property
    def pression_actuelle(self):
        self.maj()
        return self._api.conditions['pressure']['value']

    @property
    def vent_actuel(self):
        self.maj()
        return self._api.conditions['wind_speed']['value']

    @property
    def temps_observation(self):
        self.maj()
        return self._api.conditions['observationTime']['value']
