PSI, a sprawdzanie pisowni...
#############################
:date: 2009-12-20 13:28
:tags: qt, jogger.pl, po-polsku
:slug: psi-a-sprawdzanie-pisowni
:lang: pl


.. figure:: |filename| /images/2009/PSI.png
    :alt: "PSI"

    PSI


Wpisujesz coś w edytorze tekstu – widzisz błąd – poprawiasz go.
Wpisujesz coś w przeglądarce – widzisz błąd – poprawiasz go. Wpisujesz
coś w komunikatorze – nie widzisz błędu – nie poprawiasz go. Najwyższa
pora na zmiany, jako że używam PSI mój opis będzie dotyczył tego właśnie
komunikatora. Zasadniczo, przedstawię 2 możliwości postępowania – metodę
prostą i skuteczną oraz metodę wymagającą więcej pracy ale za to
aktualniejszą.

Introduction
~~~~~~~~~~~~

Historycznie
^^^^^^^^^^^^

Zacznijmy od początku (jeśli nie interesują Cię szczegóły dotyczące
sprawdzania pisowni w PSI omiń ten akapit), w komunikatorze PSI
standardowo wbudowana jest funkcja sprawdzania pisowni, oparta o program
Aspell, niestety po instalacji programu nie ma żadnego słownika z
polskimi wyrazami, lecz nie ma co panikować ponieważ wpisanie umiejętnej
frazy do naszej ulubionej wyszukiwarki znajdzie nam podpowiedź czego
szukać. Prawdopodobnie zostaniemy skierowani na stronę z której
pobierzemy jakąś wersję słownika i będziemy zadowoleni... No prawie
zadowoleni, bo po chwili spostrzeżemy się, że jednak więcej wyrazów jest
podkreślonych niż niepodkreślonych, a dlaczego tak jest? Na te i inne
pytania znajdziecie odpowiedzi w tym wpisie.

Jeśli pobierzemy i zainstalujemy w poprawny sposób oryginalny pakiet
języka polskiego dla Aspella to staniemy się posiadaczami słownika z
2002 roku (chodzi mi o słownik języka Polskiego dostępny na
http://aspell.net/win32/), stworzonego przez bezimiennego autora i
kiedyś dodanego na stronę Aspella, jak można się spodziewać są pewne
„luki” w tym słowniku i nie wszystko (a może większość) z tego co
wpiszemy będzie oznaczana jako błędny tekst. Lecz dla Ciebie to nic
złego, ponieważ w tym wpisie znajdziesz instrukcję jak zainstalować
słownik, który został zaktualizowany w ciągu ostaniach... 24 godzin na
tronie sjp.pl znajdziemy najpopularniejszy w sieci słownik języka
polskiego używany w wielu projektach, charakteryzuje się tym, że nowe
pliki z nim pojawiają się codziennie. Co nam jest na rękę :)

A jaki jest haczyk?
^^^^^^^^^^^^^^^^^^^

Prędzej czy później z pewnością to pytanie pojawiło się w twojej głowie,
bo przecież świat nie jest tak różowy. No nie jest, przeprowadziłem mały
test z użyciem PSI którego wyniki prezentuje wykres.

.. figure:: |filename| /images/2009/PSIMEM.jpeg
    :alt: "Wykres zużycia pamięci"

    Wykres zużycia pamięci

Jak głosi tytuł chodzi o ilość zużywanej pamięci przez komunikator,
wersja podstawowa bez sprawdzania pisowni to w moim przypadku 34 MB
użytej pamięci (jak na dzisiejsze standardy to mało), po zainstalowaniu
słownika z 2002 roku liczba ta wzrasta do 62 MB (czyli o 45 %), jeśli
zainstalujemy słownik najnowszej generacji wartość użytej pamięci
jeszcze bardziej wzrośnie, aż do 105 MB (czyli o 68% od wartości
początkowej). Moim zdaniem to dużo, nawet jeśli popatrzymy, że trudno
kupić komputer z mniej niż 1 GB pamięci RAM. Jednakże, uważam że takie
poświęcenie raczej nie wpłynie na komfort pracy, a z pewnością osoba z
którą piszemy uzna nas, za kogoś z wyższych sfer :)

Dobra, przeboleję to, więc co mam zrobić?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Zasadniczo przedstawię 2 drogi dojścia do celu, pierwsza będzie dla
wszystkich, bo jest prosta, łatwa i przyjemna – nie wymaga dużych
nakładów pracy. Druga jest przeznaczona, do bardziej świadomych
użytkowników komputerów. Doprowadza do tego samego celu co metoda 1,
jednak pozwala na operowanie na najnowszej z dostępnych wersji słownika,
co dla niektórych jest bardzo ważne. Zanim przejdziesz do dalszych
kroków, aby nie było nieporozumień, chciałbym ustalić parę rzeczy. Obie
metody były sprawdzane na systemach Microsoft Windows XP, z PSI w wersji
0.14 i nie gwarantuję, że będą działać na innych (powinny, aczkolwiek
mogą wystąpić nieznaczne różnice), zakładam że program PSI jest
zainstalowany w katalogu „C:\\Program Files\\Psi”, w przeciwnym wypadku
musisz pamiętać aby odpowiednio zmieniać ścieżkę adekwatnie do podanej.

Wersja normalna
^^^^^^^^^^^^^^^

Pobierasz tą paczkę (`link`_), waży około 30 MB i rozpakowujesz jej
zawartość gdziekolwiek, następnie wszystkie znajdujące się w niej pliku
kopiujesz do folderu „C:\\Program Files\\Psi\\aspell\\dict” i w
programie uruchamiasz sprawdzanie pisowni Menu Ogólne -> Preferencje ->
Inne, zaznaczasz opcję sprawdzanie pisowni.

Wersja muszę-być-aktualny
^^^^^^^^^^^^^^^^^^^^^^^^^

Na początku udajesz się na stronę (`Aspell`_) i pobierasz `program
główny`_ i `paczkę z językiem polskim`_ do niego. Instalujesz w
kolejności takiej w jakiej miały zostać pobrane. Znów zakładam, że
instalacja odbyła się do „C:\\Program Files\\Aspell”. Kolejny krok:
wchodzisz na stronę (http://www.sjp.pl/slownik/ort/) i pobierasz plik o
nazwie sjp-aspell5-pl-6.0\_(data)-0.tar.gz rozpakowujesz go. Niestety
format kompresji to nie żaden zip lub rar, więc rozpakowujemy „kolejne
archiwa” tak długo aż zamiast jednego pliku będziemy mieć kilka :) Teraz
pobieramy specjalny skrypt
(`link <http://www.sendspace.com/file/k77ezy>`__) i kopiujemy go do
katalogu z pobranym słownikiem. Uruchamiamy skrypt i po chwili (około
minuty) działania program powinien się zamknąć, Teraz przechodzimy do
katalogu „C:\\Program Files\\Aspell\\dict” i kopiujemy znajdujące się
tam pliki (najważniejsze jest to czy plik pl.rws ma >60 MB jeśli nie ma
to prawdopodobnie popełniliśmy jakiś błąd) do katalogu „C:\\Program
Files\\Psi\\aspell\\dict”, a a następnie plik pl.dat z katalogu
„C:\\Program Files\\Aspell\\data” również do „C:\\Program
Files\\Psi\\aspell\\dict” uruchamiamy sprawdzanie pisowni i jeśli
wszystko zrobiliśmy dobrze, nasz psi powinien teraz znać bardzo dużo
słów.

Coś nie działa
^^^^^^^^^^^^^^

Najprawdopodobniej nie masz lub masz złą zmienną środowiskową LANG. Bez
obaw, zaraz opanujemy sytuację:

- Prawym przyciskiem myszy kliknij ikonę Mój komputer, a następnie na polecenie Właściwości.
- Wybierz kartę Zaawansowane.
- Kliknij przycisk Zmienne środowiskowe.
- Kliknij na Nowa, w polu nazwa wpisz LANG, a w polu wartość pl. (Ewentualnie jeśli była inna edytuj ją do tej postaci

Możliwe jest, że po tych zmiannach PSI nie będzie w języku polskim, po
prostu zmień nazwę pliku o rozszerzeniu qm z folderu "C:\\Program
Files\\Psi" na psi\_pl.qm. Teraz wszystko powinno działać.

The End
^^^^^^^

To już niestety wszystko, mam nadzieję, że teraz twój PSI znakomicie
sprawdza gafy jakie popełniasz podczas pisania i pomaga poprawić Ci je.
Oczywiście, życzę Ci aby było ich jak najmniej!

Miałeś jakiś problem? Nie rozumiesz czegoś? A może po prostu chcesz coś
dodać od siebie, zapraszam do komentowania :)

Post Scriptum (4.03.2014)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Od publikacji tego artykułu minęło już parę ładnych lat. Pozostawiam go głównie jako wskazówkę informacyjną. Od dawna nie używam już PSI, ani systemu Windows. Liczę, że komuś ta wiedza może do czegoś się przydać :)

.. _link: http://www.sendspace.com/file/nxf81y
.. _Aspell: http://aspell.net/win32/
.. _program główny: http://ftp.gnu.org/gnu/aspell/w32/Aspell-0-50-3-3-Setup.exe
.. _paczkę z językiem polskim: http://ftp.gnu.org/gnu/aspell/w32/Aspell-pl-0.50-2-3.exe
