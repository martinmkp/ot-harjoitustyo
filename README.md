# Ohjelmistotekniikka, harjoitustyö

## Aihe: Sanapilvi

## Dokumentaatio
[Vaatimusmäärittely](https://github.com/martinmkp/ot-harjoitustyo/blob/main/projekti/dokumentaatio/vaatimusmaarittely.md)
<br />
[Työaikakirjanpito](https://github.com/martinmkp/ot-harjoitustyo/blob/main/projekti/dokumentaatio/tyoaikakirjanpito.md)
<br />
[Changelog](https://github.com/martinmkp/ot-harjoitustyo/blob/main/projekti/dokumentaatio/changelog.md)


## Projektin kuvaus:
Sovelluksen tarkoitus on luoda annetusta tekstitiedostosta sanapilvi.
Sanapilvi on kuvaaja, jossa näytetään tekstissä esiintyvät eri sanat.
Sanojen koko vastaa niiden yleisyyttä tekstissä: mitä useammin sana esiintyy,
sitä suurempi se on. Sovellusta voi käyttää esim. tekstianalyysin työkaluna.

## Riippuvuudet
* Python 3.8
* Numpy 1.22.3
* Coverage 6.3.2
* Invoke 1.7.0
* Pytest 7.1.1
<br />
Puuttuvat kirjastot, esim. Numpy, voidaan asentaa komennolla:
```
pip3 install <nimi>==<versionumero>
```

## Poetryn asennus ja alustus
```
poetry install
```
```
poetry run invoke build
```



## Komentorivitoiminnot
* Ohjelman suorittaminen:
```
poetry run invoke start
```
* Testaus:
```
poetry run invoke test
```
* Testikattavuus
```
poetry run invoke coverage-report
```

