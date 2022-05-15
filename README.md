# Ohjelmistotekniikka, harjoitustyö: Sanapilvi

## Release
[Viikon 5 release](https://github.com/martinmkp/ot-harjoitustyo/releases/tag/viikko_5)

## Dokumentaatio
[Käyttöohje](https://github.com/martinmkp/ot-harjoitustyo/blob/main/projekti/dokumentaatio/kayttoohje.md)
<br />
[Vaatimusmäärittely](https://github.com/martinmkp/ot-harjoitustyo/blob/main/projekti/dokumentaatio/vaatimusmaarittely.md)
<br />
[Työaikakirjanpito](https://github.com/martinmkp/ot-harjoitustyo/blob/main/projekti/dokumentaatio/tyoaikakirjanpito.md)
<br />
[Changelog](https://github.com/martinmkp/ot-harjoitustyo/blob/main/projekti/dokumentaatio/changelog.md)
<br />
[Arkkitehtuurikuvaus](https://github.com/martinmkp/ot-harjoitustyo/blob/main/projekti/dokumentaatio/arkkitehtuuri.md)


## Projektin kuvaus:
Sovelluksen tarkoitus on luoda annetusta tekstitiedostosta sanapilvi.
Sanapilvi on kuvaaja, jossa näytetään tekstissä esiintyvät eri sanat.
Sanojen koko vastaa niiden yleisyyttä tekstissä: mitä useammin sana esiintyy,
sitä suurempi se on. Sovellusta voi käyttää esim. tekstianalyysin työkaluna.

## Riippuvuudet
Projekti on testattu seuraavilla versioilla:
* Python 3.8
* autopep8 1.6.0
* Coverage 6.3.2
* Invoke 1.7.0
* Pytest 7.1.1
* pylint 2.13.5
* adjustText 0.7.3
* Numpy 1.22.3

## Poetryn asennus ja alustus
* Asennus
```
poetry install
```
* Ympäristön käynnistys
```
poetry shell
```

## Komentorivitoiminnot
Seuraavat komennot suoritetaan repon kandiossa "/projekti/"
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
poetry run invoke coverage
```
```
poetry run invoke coverage-report
```
* Koodin laadun analysointi Pylint-työkalulla
```
poetry run invoke lint
```
* Koodin muotoilu automaattisesti
```
poetry run invoke format
```

