"""Classes pour les conditions actuelles

"""
import asyncio
from env_canada import ECWeather

class ConditionsIcons:
    pass
class Conditions:
    def __init__(self, coordonnees):
        self._api = ECWeather(coordinates=coordonnees, language="french")
        self.maj()
    
    # weather = test_meteo.hourly_forecasts
    # weather = test_meteo.hourly_forecasts[0]
    # print(weather[0]['condition'])
    # print(weather[0]['icon_code'])

    def maj(self):
        asyncio.run(self._api.update())

    @property
    def temp_actuelle(self):
        self.maj()
        return self._api.conditions['temperature']['value']