 # Henkilötiedot
    Elias Mäntykoski 772299 bioIT 6.5.2022

 # Yleiskuvaus
    Kasino korttipeli graafisella käyttöliittymällä. Jokaisella kierroksella pelaajille ja pöytään jaetaan neljä
    korttia. Kierroksella pelaajat voivat vuorotelle lunastaa pöydästä kortteja kädessä olevilla korteilla.
    Kierroksen lopussa pisteet lasketaan sääntöjen mukaisesti. Pelin voi tallentaa missä tahansa vaiheessa.

 # Käyttöohje
    Ohjelma aloitetaan ajamalla main tiedosto. Tämän jälkeen se kysyy inputeilla sääntöversion, pelaajien määrän ja pelaajien nimet.
    Tästä eteenpäin peliä pelataan graafisella käyttöliittymällä. Kortin klikkaaminen valitsee tai poistaa sen valituista. Ruudun 
    vasemmalla puolella olevilla napella siirrytään seuraavaan vuoroon, otetaan pöydästä kortteja, tallennetaan tai ladataan peli ja lopetetaan ohjelma.
    Jos yrität tehdä kiellettyjä liikkeitä, ohjelma tulostaa siitä selityksen. Kun joku pelaajista voittaa pelin, ohjelma kertoo voittajan ja pistetilantee.
    Peliä ladatessa peli pitää aloittaa vaikka yhdellä pelaajalla (ei väliä) ja sen jälkeen painaa "load game" nappia.

 # Ulkoiset kirjastot
    Ei ole

 # Ohjelman rakenne
    Ohjelmassa on pienet luokat pelaajalle, kortille, kortin grafiikalle ja pakalle. Main alustaa graafisen käyttöliittymän, napit, auttaa pelin pyörittämisessä yleisellä tasolla
    ja lopettaa pelin. Suurin osa pelin logiikasta on game luokassa. Siellä hoidataan vuorot, korttien ottaminen, uusien korttien piirtaminen, jne.

 # Algoritmit
    Tärkeimmät algoritmit ovat vuoron laillisuuden tarkastaminen ja misäärikasinoa varten algoritmi, joka tarkistaa onko pelaajan mahdollista ottaa kortteja.
    Game.valid_move() käy läpi valitut kortit ja tarkastaa, että niiden arvo on yhtäsuuri. Game.move_available() muodostaa pöydässä olevista korteista kaikki mahdolliset summat
    (maksimissaan 6 korttia per summa, koska 7:n kortin summa on aina vähintään 17, jota ei voi pöydästä ottaa) ja tarkistaa onko jonkun kädessä olevan kortin arvo yhtäsuuri.

 # Tietorakenteet
    Mitään omia tietorakenteita en tarvinnut. Käytin enimmäkseen listoja kortteja varten.

 # Tiedostot
    Ohjelma tallentaa pelin tilanteen tekstitiedostoon ja voi lukea sen tekstitiedostosta. Tiedosto on ihmisen luettavissa ja kirjoitettavissa, mutta sen pitää olla täydellisesti
    tehty, että ohjelma ymmärtää sen. Tiedoston rakenne on kuvailtu "save format" tiedostossa.

 # Testaus
    Tein ohjelmaan joitain testejä. Enimmäkseen kuitenkin testasin sitä pelaamalla ja tulostamalla haluamiani arvoja, että voin katsoa miten ne muuttuvat pelin edetessä.

 #Tunnetut puutteet ja viat
    Pelin lataamisen jälkeen peli välillä hajosi. Luulen, että sain ongelman korjattua, mutten ole ihan varma eikä minulla ole ollut liikaa aikaa testata. Muita vikoja
    en ole löytänut, mutta epäilen että bugeja löytyy vielä, jos ohjelmaa alkaa kunnolla käymään läpi.

 # 3 parasta ja heikointa
    Heikko: Koodin selkeys. Minulla tuli kiire viimeisellä viikolla, jonka takia en suunnitellut kovin pitkälle eteenpäin. Tämän takia olisin varmasti voinut toteutaa
    asiota paremmin ja selkeämmin, mutta en ehtinyt. En esimerkiksi käyttänyt game.player_cards monessa paikkaa, koska unohdin sen olemassaolon tauon jälkeen.

 # Poikkeamat suunnitelmassa
    Suunnitelmaan ei tullut mitään merkitseviä muutoksia. Aikataulu muuttui aika paljon, mutta se oli odotettavissa.

 # Työjärjestys ja aikataulu
    Checkpoint 1: 12H
    Checkpoint 2: 1H
    Checkpoint 3:
    Viikko 16 n. 8h
    Viikko 17 n. 3h
    Viikko 18 n. 22h

 # Arvio lopputuloksesta
    Suurin tyytymättömyyden kohde minulla on projektin lopussa kiireessä tehdyt ratkaisut. Ohjelmassa on paljon hiottavaa ja paranneltavaa.
    Valitsin tämän projektin, että voin itse tämän pohjalta kehittää oman korttipelin halutessani. Jos aloitan tästä oman projektin, voin siinä korjata asioita.
    Muuten olen tyytyväinen projektiini

 # Viitteet
    Kurssimateriiali
    https://www.geeksforgeeks.org/
    https://stackoverflow.com/
    https://www.qt.io/
    

 # Liitteet


