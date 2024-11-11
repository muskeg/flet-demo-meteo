# flet-demo-meteo

Cette application météo est un exemple d'utilisation du framework Flet pour créer des applications (web et natives) rapidement en Python.


## Exécution

### Prérequis
* Python 3
* (optionel) [git](https://git-scm.com/downloads) 
* (optionel) module de [virtual environment](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/)
* Les modules dans le fichier requirements.txt
  * flet version 0.24.*
  * env-canada


Pour exécuter le script
```
> git clone https://github.com/muskeg/flet-demo-meteo.git
> cd  .\flet-demo-meteo\
flet-demo-meteo> python -m venv .venv
flet-demo-meteo> .\.venv\Scripts\activate
flet-demo-meteo> pip install -r .\requirements.txt
flet-demo-meteo> flet run
```
Si tout se passe comme prévu, l'application se lance:

![alt text](image.png)

## Attributions

* L'application utilise le module [env_canda](https://github.com/michaeldavie/env_canada) pour faciliter récuperer les données météorologiques
* Les icônes de conditions climatiques proviennent d'un [ensemble d'icônes](https://github.com/Makin-Things/weather-icons) destiné à une utilisation à l'intérieur de [Home Assistant](https://www.home-assistant.io/)

