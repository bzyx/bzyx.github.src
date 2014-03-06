Bluetooth z Allegro
###################
:date: 2009-07-06 14:01
:tags:  jogger.pl, po-polsku, linux, funny
:slug: bluetooth-z-allegro
:lang: pl

Po co mi Bluetooth?
^^^^^^^^^^^^^^^^^^^

Jako posiadacz stacjonarnego komputera, który zbliża się do rangi
starszego pokolenia, bluetooth nigdy nie był mi potrzeby.

Pewnego szczęśliwego dnia zostałem obdarowany bezprzewodową myszką
komputerową ASUS `N554`_. Wtedy zostałem "zmuszony" do zakupienia modułu
bluetooth. Po sprawdzeniu oferty sklepów w okolicy i komisów z
telefonami, uznałem że na allegro najtaniej... 14,45 (z przesyłką),
sprzęt taki sam.

Po 2 miesiącach używania chciałbym się podzielić moimi spostrzeżeniami
na ten temat.

Co to jest ten "Bluetooth"?
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Polska wikipedia mówi na ten temat,

Bluetooth /ˈbluːtuːθ/ - technologia bezprzewodowej komunikacji
krótkiego zasięgu pomiędzy różnymi urządzeniami elektronicznymi,
takimi jak klawiatura, komputer, laptop, palmtop, telefon komórkowy
i wieloma innymi.

Jest to darmowy standard opisany w specyfikacji IEEE 802.15.1. Jego
specyfikacja obejmuje trzy klasy mocy nadawczej 1-3 o zasięgu 100,
10 oraz 1 metra w otwartej przestrzeni. Najczęściej spotykaną klasą
jest klasa druga. Technologia korzysta z fal radiowych w paśmie ISM
2,4 GHz.

popularnie przyjęło się, Bluetooth to nie tylko standard transmisji
danych, ale także urządzenia, które podłączamy do komputera powalające
na transmisję danych w tym standardzie. Możliwości jakie oferują tego
typu urządzenia są szeroko opisane na `wikipedii`_, wymienię kilka:
sterowanie komputerem przez interfejs HID, przesyłanie plików i
kontaktów do i z urządzeń mobilnych, prowadzenie rozmów przez specjalne
słuchawki bluetooth, drukowanie przez specjalne drukarki bluetooth.

Typowe adaptery Bluetooth spotykane w sklepach, na aukcjach.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: |filename| /images/2009/BLUETOOTH-1.jpg
    :alt: "BLUETOOTH-1.jpg"

    Fot. 1

.. figure:: |filename| /images/2009/DSC_2952.jpg
    :alt: "DSC_2952.jpg"

    Fot. 2

.. figure:: |filename| /images/2009/677567075.jpg
    :alt: "677567075.jpg"

    Fot. 3


Zasadniczo, dla każdego coś się znajdzie, istnieją różne kombinacje
kolorowe i rozmiarowe również. Chińskie fabryki mają dosyć szeroki
asortyment. I tak adapter z fot. 2 ma "większy" zasięg, niż ten z fot.
1. A ten z fot. 3 pasuje do przenośnych komputerów, choć w stacjonarnych
również się sprawuje, sam taki mam.

"Naga" prawda o Bluetooth z Allegro.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. image:: |filename| /images/2009/116862296996940258.jpg
    :alt: "116862296996940258.jpg"


To nie jest żart, ani fotomontaż, adaptery z antenka nie mają większego
zasięgu niż te bez niej. Nie ma żadnego fizycznego połączenia anteny z
układem na płytce

A zasięg, między tym malutkim z Fot. 3 a takim z Fot. 1 lub Fot. 2, moim
zdaniem nie widać żadnej różnicy. Moja mysz współpracowała z odległości
max ok. 3 m, podobnie telefony, więc bez rewelacji, a już na pewno nie
to o czym zapewniają nas ochoczo na wszystkich aukcjach sprzedawcy 130
m! To, jakiś żart i nieporozumienie z ich strony, ponieważ chińszczyzna
jaką sprzedają nawet nie nie nie osiąga tych ok. 10 z klasy 2

Zdają się sytuacje, że urządzenie ni stąd i zowąd się zawiesza i nie
odpowiada, wtedy jedyną możliwością jest ponowne uruchomienie komputera.

Zdarzają się przypadki, kiedy urządzenie (najprawdopodobniej z powodu
zbyt wysokiej temperatury), traci chwilowo kontakt z np. myszką. Choć
między adapterem jest 35 cm i troszkę drzewa. Wtedy warto mięć
podłączoną alternatywną na USB lub PS/2

Nie radzę np. przesyłać pików na telefon jednocześnie korzystając z
myszki, początkowo możemy odczuć duże spowolnienie w reaktywności myszy,
które po czasie w magiczny sposób mija...

Ceny
^^^^

Przedziały cenowe są różne, w tej chwili na Allegro.pl kupimy adaptery
już za 6 zł do 50-60 zł, w sklepach i komisach z telefonami, w mojej
okolicy, adaptery kosztują około 40-50 zł.

Cenowo rozbieżność jest duża, jednakże nigdy nie możemy być pewni, że
zakupione przez nas urządzenie za 60 zł nie będzie zbudowane w ten sam
sposób jak te za 6 zł

Oprogramowanie
^^^^^^^^^^^^^^

O samym sprzęcie powiedziane zostało już dużo, a jak wygląda sprawa z
oprogramowaniem, w przypadku mojego adaptera dostałem przestarzałą
wersję programu `BlueSoil`_, oczywiście bez możliwości aktualizacji. Na
moim systemie MS Windows XP SP3, adapter nie został wykryty prawidłowo i
nie obeszło się bez dodatkowego oprogramowania jakim jest BlueSoleil ,
alternatywą są sterowniki `Widcomm`_, które na moim komputerze nie
działały zbyt stabilnie.

Pod systemem Linux, mamy do dyspozycji `BlueZ`_, którego ja łączę z
`KBluetooth`_ w efekcie udaje mi się przesyłać pliki na telefon, ale
myszki nie obsługuje jak narzazie (nie zagłębiałem jeszcze tematu)

Podsumowanie
^^^^^^^^^^^^

Adapter Bluetooth to przydatna rzecz ponieważ można zrezygnować z kilku
kabli na biurku, aczkolwiek ma pewne minusy, musimy pamiętać o
ograniczonym zasięgu, słabym oprogramowaniu do obsługi, no i cena nie
powinna być wyznacznikiem jakości, przy zakupie.

Moim zdaniem, mimo pewnych wad warto mieć Bluetooth w komputerze, w
dobie rosnącej ilości urządzeń mobilnych mało kto ma przy sobie kabel
transmisyjny, ale prawie każdy ma Bluetooth.

W uprzywilejowanej sytuacji są tu wszyscy użytkownicy komputerów
przenośnych, mających już Bluetooth wbudowany w obudowę.

.. _N554: http://my.asus.com/600/html/share/5/icon/accessory/product/bluetooth/index.htm
.. _wikipedii: http://pl.wikipedia.org/wiki/Profile_systemu_Bluetooth
.. _BlueSoil: http://www.bluesoleil.com/products/index.asp?topic=bluetooth-mobilephone-headset
.. _Widcomm: http://www.searchengines.pl/Bluetooth-sterowniki-Widcomm-t61164.html
.. _BlueZ: http://www.bluez.org/
.. _KBluetooth: http://bluetooth.kmobiletools.org/
