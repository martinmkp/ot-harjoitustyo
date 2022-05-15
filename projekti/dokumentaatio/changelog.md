# Changelog

## Viikko 3
* Projektin aiheeksi vaihdettu Sanapilvi eli Word Cloud
* Luotu WordCloud -luokka, joka:
  * Lukee .txt-tiedoston string-muuttujaksi
  * Poistaa string-muuttujasta välimerkkejä ja suuret kirjaimet
  * Jakaa string-muuttujan listaksi sanoja (str)
  * Luo jokaiselle listan sanalle xy-koordinaatin
* Lisäksi luotu pohja testeille, jossa muutama yksinkertainen testi:
  * Tarkistaa, että suuret alkukirjaimet ja välimerkit poistettu
  * Tarkistaa, että jokaisella sanalla on koordinaatit
* Suoritettu testit coverage-komennon avulla. Coveragen html-raporttia ei lisätty repoon ohjeiden mukaisesti.
* README päivitetty
* .gitignore lisätty
<br />

## Viikko 4
* Korjaukset viime viikon palautteeseen perustuen:
  * Ohjelma osaa nyt lukea dataa ilman kovakoodausta - ainoastaan suhteellinen tiedostopolku tarvitaan
  * .gitignore ei huomioi __pycache__ -tiedostoja
  * HTML-raportin luominen toimii
  * Paranneltu README:n ohjeita
  * Lisätty main.py -tiedosto josta itse projekti suoritetaan
* Ohjelma piirtää sanapilven sanoista matplotlibilla
  * Tällä hetkellä sanat vielä toistensa päällä:
* Lisätty pylint koodin tarkistusta varten ja autopep8 koodin muotoilua varten task.py -tiedostoon
* Ohjelman komennot toimivat Linux-etäkoneella /tmp/ -kansiossa
<br />

## Viikko 5
* Github release lisätty
* Korjaukset viime viikon palautteeseen perustuen
  * Wordcloud-luokan toiminnallisuudet jaettu useampaan luokkaan
  * Tulostuskomennot siirretty main.py -tiedostoon
* Tekstikäyttöliittymän ja sqlite-tietokannan 1. versiot

## Viikko 6
* Tekstikäyttöliittymä siirretty erilliseen tiedostoon
  * main.py ainoastaan ohjelman suoritukseen
* Tekstikäyttöliittymä hyväksyy vain tietynlaisia input-komentoja
* Testikattavuutta kasvatettu
* Arkkitehtuurikuvaus lisätty
* Käyttöohje

## Viikko 7
* Parannuksia sanapilveen
  * Sanapilvet eivät nyt laita sanoja päällekkäin
  * Sanapilven koordinaattiviivat pois näkyvistä
  * Mahdollisuus valita (suunnilleen) ympyrän tai neliön muotoinen sanapilvi
  * Sanapilven värit paremmin erottuviksi
* Pylint-virheiden määrä laskettu alle 3:een
* Luokkien muuttujat, joita ei tarvita globaalisti (esim. testaamiseen) muutettu yksityisiksi

