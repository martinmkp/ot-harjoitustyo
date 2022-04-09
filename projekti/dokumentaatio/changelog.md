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
  * Tällä hetkellä sanat vielä toistensa päällä
