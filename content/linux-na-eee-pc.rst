"Linux na Eee PC..."
####################
:date: 2010-04-19 12:48
:tags: jogger.pl, po-polsku, linux
:slug: linux-na-eee-pc
:lang: pl

| 

.. raw:: html

   </p>

.. raw:: html

   <p>

    *...lub innego netbooka.*

.. raw:: html

   </p>

.. raw:: html

   </p>

Jestem zadowolonym posiadaczem Asusa eee pc 1000HE i wszystko co
opisuję, zostało sprawdzone dokładnie na tym modelu, lecz powinno
również w 100% sprawdzić się na innym dowolnym komputerze z serii Eee
PC, lub nawet dowolnym netbooku.

.. raw:: html

   </p>

(prawdopodobnie eee-control by nie działało) Mam nadzieję, że pomogłem.
A zaawansowani użytkownicy niech mi wybaczą...

.. raw:: html

   </p>

.. raw:: html

   </p>

Dystrybucja
~~~~~~~~~~~

.. raw:: html

   </p>

Po pierwsze nie brałem pod uwagę żadnych konstrukcji typu Notebook Remix
lub Mobilin. Chciałem całkowicie normalny system. Podczas wyboru
kierowałem się tym aby standardowym środowiskiem było KDE.

.. raw:: html

   </p>

.. raw:: html

   </p>

.. raw:: html

   <div style="margin-left: 2em;">

.. raw:: html

   </p>

.. raw:: html

   <div style="margin-left: 2em;">

1) Mój pierwszy wybór Kubuntu, nie dotrwało nawet do 1 aktualizacji...

.. raw:: html

   </div>

.. raw:: html

   </p>

.. raw:: html

   <div style="margin-left: 2em;">

2) Druga była Fedora 12, pobieram .iso za pomocą Unetbotin #link#
kopiuję na pen-drive, próbuję bootować, błąd i restart komputera...

.. raw:: html

   </div>

.. raw:: html

   </p>

.. raw:: html

   <div style="margin-left: 2em;">

3) Trochę zdegustowany, postanowiłem sięgnąć po dystrybucję która
jeszcze nigdy mnie nie zawiodła. Tak samo było i tym razem. Mój wybór
padł na Mandrivę 2010 One, która to jest zachwalana jako system `netbook
friendly`_.

.. raw:: html

   </div>

.. raw:: html

   </p>

.. raw:: html

   <p>

.. raw:: html

   </div>

.. raw:: html

   </p>

.. raw:: html

   </p>

Krótkie HowTo
~~~~~~~~~~~~~

.. raw:: html

   </p>

Założenia: Korzystasz z Windows XP, masz pod ręką pen-drive >=700MB.
chwilę czasu, łącze z internetem

.. raw:: html

   </p>

.. raw:: html

   </p>

.. raw:: html

   <div style="margin-left: 2em;">

.. raw:: html

   </p>

.. raw:: html

   <div style="margin-left: 2em;">

1) Pobierasz obraz Mandrivy. Ja pobrałem z `stąd`_

.. raw:: html

   </div>

.. raw:: html

   </p>

.. raw:: html

   <div style="margin-left: 2em;">

2) Pobierasz narzędzie Mandriva Seed z `tego miejsca.`_

.. raw:: html

   </div>

.. raw:: html

   </p>

.. raw:: html

   <div style="margin-left: 2em;">

3) Teraz za pomocą Mandriva Seed kopiujesz obraz .iso na swojego
pen-drivea .

.. raw:: html

   </div>

.. raw:: html

   </p>

.. raw:: html

   <div style="margin-left: 2em;">

4) Uruchomienie ponownie komputera, z podłączonym pen-drivem i zmiana
ustawień bios, lub przytrzymanie klawisza ESC podczas startu (tylko eee)

.. raw:: html

   </div>

.. raw:: html

   </p>

.. raw:: html

   <div style="margin-left: 2em;">

5) Uruchomienie Mandrivy - nie powinno być najmniejszego problemu.
Następnie uruchomienie instalatora. Co do partycjonowania, ja
przeprowadziłem je będąc jeszcze na Windowsie użyłem narzędzia `EASEUS
Partition Master Home Edition`_ i wydzieliłem z dysku D (zakładam, że
jest standardowy układ zaproponowany przez Asusa) trochę miejsca, tak
aby Mandriva maiła gdzie założyć swoje partycje.

.. raw:: html

   </div>

.. raw:: html

   </p>

.. raw:: html

   <div style="margin-left: 2em;">

6) W ostatnim kroku wybrałem instalację GRUBa na kartę pamięci (w moim
przypadku w instalatorze sdc), po to aby nie nadpisywać MBR dysku
twardego. Oczywiście jeśli chcesz możesz pozostawić domyślne ustawienia,
jednak wcześniej zapoznaj się z `tym`_ kiedy to w nie do końca
przemyślany sposób wykonywałem instalację...

.. raw:: html

   </div>

.. raw:: html

   </p>

.. raw:: html

   <div style="margin-left: 2em;">

7) Wszystko poszło łatwo, system zainstalowany. Podłącz internet,
najłatwiej kablem Ethernetowym .Następnie zastosuj się do porad
`stąd <http://mandriva.org.pl/pierwsze-kroki/71-konfiguracja-repozytoriow-oraz-instalacja-oprogramowania.html>`__.
W ten sposób zwiększysz liczbę repozytoriów z oprogramowaniem.
Zaktualizuj cały system. W moim przypadku było to około 400 MB do
pobrania.

.. raw:: html

   </div>

.. raw:: html

   </p>

.. raw:: html

   <div style="margin-left: 2em;">

8) System zaproponuje restart. Wykonaj go. Potem przejdź do narzędzia
konfiguracja komputera. Wybierz instalację oprogramowania i zainstaluj
eee-control.

.. raw:: html

   </div>

.. raw:: html

   </p>

.. raw:: html

   <p>

.. raw:: html

   </div>

.. raw:: html

   </p>

.. raw:: html

   </p>

Teraz przyszła pora, aby rozkoszować się twoim nowo zainstalowanym
systemem. W przypadku mojego modelu wszystko działało od razu. A ikonka
eee w zasobniku pozwala łatwo sterować wydajnością i włączonymi
peryferiami naszego eee. Miłej zabawy z Mandrivą ;)

.. raw:: html

   </p>

PS. Co zaskakuje, podczas lekkiej pracy, wentylator może się całkowicie
wyłączyć, na Windowsie to niemożliwe... ;>

.. raw:: html

   </p>

PPS. Po zainstalowaniu systemu pewnie chcesz sformatować pen-drive i
wtedy zdajesz sobie sprawę, że twoje GB gdzieś zniknęły i masz raptem
około 700 MB miejsca. Niestety ale narzędzie Mandriva Seed używa znanego
linuksiarzom `dd`_ co przejawia pozorną zmianą rozmiaru. Jak temu
zaradzić? Można wykonać kopię MBR przed użyciem narzędzia Seed i
przywrócić ją po lub zrobić tak jak ja "mądry Polak po szkodzie" x2.
Użyć `TestDisk-a`_, wyczyścić całego mbr-a a następnie za pomocą np.
narzędzia "`zarządzania dyskami`_\ " utworzyć na nowo partycję na całym
obszarze.

.. raw:: html

   </p>

I jeszcze jedno, co do wydajności KDE na takim sprzęcie, całość bez
przeprowadzania zmian w trybie powersave działa znakomicie, żadnych
smużeń, przycięć, przy włączonych standardowych efektach graficznych :)

.. raw:: html

   </p>

    <p>
    -Why ? -For SKNLiWO :)
    </p>




.. _netbook friendly: http://wiki.mandriva.com/en/2010.0_Tour#Netbook_friendly
.. _stąd: http://www2.mandriva.com/downloads/?p=linux-one&mirror=ftp%3A%2F%2Fftp.pbone.net%2Fpub%2Fmandrakelinux%2Fofficial%2Fiso%2F2010.0&l=pl
.. _tego miejsca.: http://www2.mandriva.com/downloads/?p=seed
.. _EASEUS Partition Master Home Edition: http://www.partition-tool.com/personal.htm
.. _tym: http://bzyx.jogger.pl/2010/01/10/zapamietac-linux-na-laptopie-stracony-mbr/
.. _dd: http://pl.wikipedia.org/wiki/Dd
.. _TestDisk-a: http://www.cgsecurity.org/wiki/TestDisk_Download
.. _zarządzania dyskami: http://support.microsoft.com/kb/309000/pl
.. _SKNLiWO: http://liwo.polsl.pl/SKNLIWO/informacje-o-sknliwo
