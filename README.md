# Covid19Umbria

![PyPI](https://img.shields.io/pypi/v/covid19umbria)

Covid-19 statistics for Regione Umbria, based on the [public API](https://apistore.regione.umbria.it/store/apis/info?name=COVID-19&version=1.0.0&provider=admin&tag=Agenda%20digitale-group).

Cf. also the [Dashboard COVID-19 Regione Umbria](https://github.com/Regione-Umbria/coronavirus).

Partially inspired by the [covid](https://github.com/ahmednafies/covid) package.

## Installation

    pip install covid19umbria

## Usage

See the [example](example.py).

### Get All Data

```python
from covid19umbria import Covid19Umbria

covid19 = Covid19Umbria()
covid19.get_data()
```

### Get Currently Active cases

```python
current_active = covid19.get_current_active_cases()
```

### Get New Active Active cases

```python
new_active = covid19.get_new_confirmed_cases()
```

### Get Total Recovered cases

```python
recovered = covid19.get_total_recovered()
```

### Get Total Deaths

```python
deaths = covid19.get_total_deaths()
```
