"""Module de prévisions météorologiques 

Ce module contient la classe Previsions qui permet de récupérer les prévisions météorologiques
d'une station météo donnée.
"""

import asyncio
from datetime import datetime, timedelta
from collections import OrderedDict
from env_canada import ECWeather

class Previsions:
    """Classe pour les prévisions météorologiques"""
    def __init__(self, coordonnees):
        self._api = ECWeather(coordinates=coordonnees, language="french")
        self._previsions_par_dates = self.__previsions_par_dates()
        self.maj()

    def maj(self):
        """Mise à jour des prévisions météorologiques"""
        asyncio.run(self._api.update())

    @property
    def previsions(self):
        """Prévisions horaires"""
        self.maj()
        return self._api.hourly_forecasts

    @property
    def previsions_jour(self):
        """Prévisions journalières"""
        self.maj()
        return self._api.daily_forecasts

    def __previsions_par_dates(self):
        """Prévisions par dates"""
        self.maj()
        temp_actuelle = self._api.conditions['temperature']['value']
        grouped_data_by_day = OrderedDict()
        for entry in self.previsions_jour:
            day = entry['timestamp'].date()
            if day not in grouped_data_by_day:
                grouped_data_by_day[day] = {
                    'period': entry['period'],
                    'text_summary': entry['text_summary'],
                    'icon_code': entry['icon_code'],
                    'precip_probability': entry['precip_probability'],
                    'timestamp': entry['timestamp'],
                    'temperatures': [entry['temperature']]
                }
            else:
                grouped_data_by_day[day]['temperatures'].append(entry['temperature'])
        for day, entry in grouped_data_by_day.items():
            temps = entry['temperatures']
            if len(temps) == 2:
                temperature_high = max(temps)
                temperature_low = min(temps)
            elif temp_actuelle > temps[0]:
                temperature_high = temp_actuelle
                temperature_low = temps[0]
            else:
                temperature_high = temps[0]
                temperature_low = temp_actuelle
            entry['temperature_high'] = temperature_high
            entry['temperature_low'] = temperature_low
            del entry['temperatures']
        grouped_data_by_day = dict(grouped_data_by_day)

        return grouped_data_by_day

    @property
    def prevision_5_jours(self):
        """Prévisions pour les 5 prochains jours"""
        aujourdhui = datetime.now().date()
        previsions = {}
        for x in range(0, 5):
            date = aujourdhui + timedelta(days=x)
            if date in self._previsions_par_dates:
                previsions[date] = self._previsions_par_dates[date]
                # yield date, self.__previsions_par_dates[date]
        return previsions

    def prevision_un_jour(self, date):
        """Prévisions pour une journée précise"""
        prevision = self._previsions_par_dates[date]
        return prevision
