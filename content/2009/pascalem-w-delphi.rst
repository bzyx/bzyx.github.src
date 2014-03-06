Pascalem w Delphi...
####################
:date: 2009-12-28 14:46
:tags: politechnika śląska, projekt, po-polsku, jogger.pl
:slug: pascalem-w-delphi
:lang: pl

Sam nie tak dawno broniłem zasadności używania języka Pascal na polskich
uczelniach u kogoś na Joggerze. Nazwałem wtedy ten język dydaktycznym,
który uczy dobrych nawyków. Chyba jednak trochę rozminąłem się z prawdą,
bo tak jest tylko w bardzo prostych zastosowaniach Pascala, a potem...

Napisz „Prosty program”
~~~~~~~~~~~~~~~~~~~~~~~

Piszę sobie, a raczej muszę napisać :( drugi program na zaliczenie
programowania komputerów I, dostał mi się, jakże akademicki przykład
**porządnej** aplikacji w Pascalu. Tytuł brzmi mniej więcej następująco
*„Napisz program do zarządzania domową biblioteką”*. Żeby nie było tak
łatwo, musiałem wymyślić kilka założeń jakie aplikacja będzie spełniać:

-  obsługa „użytkowników” - tzn. wydzielam administratora, który może
   dodawać pozycje i nowych użytkowników, oraz zwykłych użytkowników
   którzy mogą tylko wypożyczać książki – konta na identyfikator i hasło
-  Baza danych oparta na odpowiednio dobranej dynamicznej strukturze
   danych, ja wybrałem listę dwukierunkową powstałą z rekordów
   zawierających oprócz wiadomych pól: tytuł, autora, kategorię, liczbę
   książek i użytkowników którzy mają ją wypożyczoną
-  Program musi zapisywać i odczytywać dane z dysku, tu planuję
   tworzenie kilku(2) plików
-  Program powinien być w jak największym stopniu idioto-odporny, na to
   akurat znalazłem dosyć prosty sposób, mogę wykorzystywać Win32Crt, a
   tam z kolei znajduje się funkcja SmartInput, opisana `tu`_. W skrócie
   przygotowuje coś w rodzaju pola edycji, w którym możemy określić typ
   akceptowalnych danych i ich długość maksymalną, więc część problemu z
   głowy...

w języku Pascal
~~~~~~~~~~~~~~~

.. figure:: |filename| /images/2009/delphi7.png
    :alt: "Delphi 7 IDE"

    Borland Delphi 7


Jednak nie ma że boli, pamiętajmy z czym mamy do czynienia – przecież to
Pascal w dodatku połączony z Delphi 7, tutaj nic nie działa tak jak
działać powinno, znane funkcje stają się nieznane, tak jak kolorowanie
składni niby jest ale go nie ma.

Tworzenie programu w tym IDE jest męką (jak dla mnie), jedyny dobry
sposób to użycie zewnętrznego edytora np. Notepad++ w którym tworze
funkcję/procedurę tam przynajmniej widzę, czy każdy begin ma swojego
enda, a następnie przekopiowanie tego do Delphi 7-"nie ma, że boli".
Jednak na 99% i tak zostaniemy obdarowani jakimś ostrzeżeniem albo po
prostu zapomnimy średnika lub co gorsze użyjemy go przed else.

i uśmiechnij się, mówiąc „dy-dak-ty-czny”!
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Te słowo chyba będzie mnie prześladować, o ile rozumiem sens
oprogramowywania listy dwukierunkowej(chociaż to po trosze wynajdywanie
koła na nowo), to jednak tworzenie funkcji która będzie wyszukiwać
fragmentu jednego wyrazu na początku drugiego wydaje mi się lekką
przesadą, a na to właśnie się zanosi, kochane delphi chyba nie rozumie
moich zamiarów i skrywa swe tajemne funkcje.

Nie wiem czy tu da się w jakimiś logiczny i prosty sposób podzielić kod
na kilka plików, czego mi bardzo brakuje - ciągłe przeskakiwanie góra
dół :( Nie wspominając już o programowaniu obiektowym, które było by w
tym przypadku (według mnie) zbawieniem.

Niestety, life is brutal - Masz Pascala i pisz. Pokaż, że potrafisz.
Potem napisz jeszcze sprawozdanie w którym podkreślisz zalety Pascala i
to jak wiele się dzięki niemu nauczyłeś.

*To sobie ponarzekałem, a teraz wracam do kodzenia*

.. _tu: http://www.zieglersoft.dk/public/win32crt.asp
