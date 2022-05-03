# Käyttöohje

Tämä dokumentti sisältää ohjeet [releasen](https://github.com/martinmkp/ot-harjoitustyo/releases) suorittamiseen.

## Alustustoimenpiteet

Aluksi, asennetaan ohjelman riippuvuudet:
```
poetry install
```

ja käynnistetään ympäristö:

```
poetry shell
```

## Ohjelman käynnistäminen

Siirry aluksi komentorivillä projektin kansioon "../projekti/". Ohjelma käynnistetään komennolla:

```
poetry run invoke start
```

## Ohjelman käyttö tekstikäyttöliittymän kautta

Kun ohjelma on käynnistetty, sitä käytetään tekstikäyttöliittymän kautta. Tämä tapahtuu komentorivillä.
Ohjelmassa voi lukea tekstidataa joko sqlite-tietokannasta, tai "../projekti/" -kansiossa olevasta "/data_folder/"
kansiosta. Datasta voi piirtää sanapilven, joka tallennetaan automaattisesti "../projekti/" -kansiossa olevaan kansioon
/word_clouds/ .png-tiedostona. 
Ohjelman käyttö tekstikäyttöliittymän kautta on yksinkertaista: Tekstikäyttöliittymä kertoo käyttäjälle 
jokaisessa vaiheessa, mitä tämän tulee tehdä.


## Tekstidatatiedostojen lisääminen

Käyttäjä voi lukea dataa omasta tekstidatatiedostostansa (.txt) lisäämällä sen kansioon "../projekti/data_folder/".
