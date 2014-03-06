ST7565R - AVR
#############
:date: 2011-11-27 15:10
:tags: projekt,  avr, politechinka śląska, po-polsku, jogger.pl
:slug: st7565r-avr
:lang: pl

Nie tak dawno zaopatrzyłem się w wyświetlacz graficzny zakupiony `tu`_ z
racji korzystnej ceny jak na wyświetlacze graficzne. Ma całe 128x64 px i
potrafi obsługiwać różne rozmiary czcionek więc względem wszystkiego
opartego na HD4470 jest bezkonkurencyjny - dla mnie ;)

Krótkie spojrzenie na `specyfikację`_ i możemy wpaść w zachwyt
wyświetlacz ma interfejs szeregowy i od procesora wymaga raptem 5 linii.
Za to nadrabia ilością dołączonych kondensatorów. Co było dla mnie
ważne, pracuje na 3.3V wiec jest kompatybilny z nowoczesnymi
konstrukcjami, które coraz częściej ustalają napięcie zasilania na tym
poziomie.

Dochodząc do sedna doczytamy, że całością steruje kontroler ST7565R.
Jedno zapytanie do Google i już się cieszymy, bo ktoś się natrudził i
stworzył bibliotekę do obsługi tego kontrolera w mikrokontrolerach AVR
Atmega. Niestety tak pięknie nie jest gdy chcemy korzystać z AVR
Studio...

Szukając różnych bibliotek, uznałem że najlepsza będzie `dogm128`_
trochę się zasmuciłem, gdyż biblioteka ta wg twórcy obsługuje
wyświetlacze serii `DOGM`_, ale przyglądając się specyfikacji i
wyglądowi stwierdziłem, że mam taki sam tylko pod inną nazwą.

Biblioteka jest w dwóch wersjach dla Arduino i "czystych" AVRów. Wersji
dla Arduino nie próbowałem, bo swój projekt opieram bezpośrednio na
procesorze Atmega328 działającym na 3.3V (odpada konwersja napięć z
Arduino). Więc pobieramy wersję dla AVR `stąd`_. Rozpakowujemy i teraz
zaczynają się małe schody, korzystając z Linuksa nie ma problemu
instalujemy "gcc-avr" i "avrdude", robimy make i make upload, oczywiście
trzeba zmienić typ procesora i to gdzie mamy podłączony programator.
Wszystko działa znakomicie - sprawdziłem (bo to tam na początku udało mi
się w ogóle uruchomić tą bibliotekę). Ale zdecydowałem, że ten projekt
zrobię na Windowsie i w AvrStudio 4.19 (chociaż mam coraz większe
wątpliwości i pewnie użyję Eclipse z pluginem do AVR).

dogm128 i AvrStudio
~~~~~~~~~~~~~~~~~~~

Mamy pobraną i rozpakowaną bibliotekę np. w C:\\dogm128, mamy też
zainstalowany pakiet WinAvr np. w C:\\WinAVR-20100110. Kolejnym krokiem
jest ściągnięcie i zainstalowanie `MSYS`_ np. w C:\\msys.

Teraz zmieniamy nazwę pliku C:\\dogm128\\lib\\Makefile.dogm128 na
C:\\dogm128\\lib\\Makefile. Edytujemy nazwę procesora, prędkość, typ
wyświetlacza - ja wybrałem DDOGM128\_HW. Następnie zmieniamy
AVRTOOLSPATH na AVRTOOLSPATH:=C:/WinAVR-20100110/bin/ .

Otwieramy cmd i wpisujemy:

.. code:: bash

    set PATH=C:\\WinAVR-20100110\\bin;C:\\WinAVR-20100110\\utils\\bin;C:\\WinAVR-20100110\\avr\\include;C:\\msys\\1.0\\bin

    set PATH=%PATH%;%SystemRoot%\\System32

Teraz możemy przejść do katalogu z biblioteką cd C:\\dogm128\\lib.
Wykonujemy "make all" Jeśli wszystko pójdzie z planem dostaniemy nasz
bardzo potrzebny plik libdog.a .

Pora na konfigurację AVR Studio, w sumie jest całkiem prosta, ale lepiej
napisać ;) W opcjach projektu w Iclude Directories dodajemy katalog
"C:\\dogm128\\lib\\", w Libaries znów " "C:\\dogm128\\lib\\" i
przenosimy do Link with These Objects libdog.a.

Teraz do projektu dodajemy plik dogm128.h, ja skopiowałem jego zawartość z takiego samego pliku w katalogu lib a następnie usunąłem
komentarz z linii #define DOGM128\_HW.

Napisałem następujący prosty program bazując na przykładach dołączonych
do biblioteki.

Kod: http://wklej.org/id/635690/ (bo coś formatowanie się popsuło, dawno
nic tu nie pisałem)

avr-size mówi że ma on 4760 B, a pomiar ilość wolnej pamięci RAM to
1875B. Jak dla mnie jest super ;) Dokumentację funkcji można zleźć tutaj
: http://code.google.com/p/dogm128/wiki/cref. A, na dowód że działa
dołączam zdjęcie, układu działającego na 2 bateriach AA. Z wewnętrznym
oscylatorem 8 Mhz, procesor jak napisałem wcześniej Atmega328P.
Kondensatory użyłem wszystkie takie same 4.7uF, ważne aby było to
elektrolity. Dla pewniejszego działania zasilanie powinno iść przez
100nF, ale dla celów póki co prototypowych może być tak jak jest póki
działa ;)

.. figure:: |filename| /images/2011/IMG187.jpg
    :alt: "IMG187.jpg"

    Fot. 1

.. figure:: |filename| /images/2011/IMG188.jpg
    :alt: "IMG188.jpg"

    Fot. 2


Parę fotek więcej można zobaczyć tu: https://picasaweb.google.com/bzyx90/AVRSMiWAEIProjekt



.. _tu: http://allegro.pl/sklep/9015460_artronic-spj
.. _specyfikację: http://artronic.pl/o_produkcie.php?id=1143?
.. _dogm128: http://code.google.com/p/dogm128/
.. _DOGM: http://www.lcd-module.de/
.. _stąd: http://code.google.com/p/dogm128/downloads/list
.. _MSYS: http://www.mingw.org/wiki/MSYS
.. _AVR - SMiW - AEI Projekt: https://picasaweb.google.com/bzyx90/AVRSMiWAEIProjekt?authuser=0&feat=embedwebsite
