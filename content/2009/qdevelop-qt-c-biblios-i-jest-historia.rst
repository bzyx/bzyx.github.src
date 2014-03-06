QDevelop, Qt, C++ - Biblios... i jest historia.
###############################################
:date: 2009-01-29 14:26
:tags: projekt, qt, po-polsku, jogger.pl
:slug: qdevelop-qt-c-biblios-i-jest-historia
:lang: pl

Wyobraź sobie, że w pewnego dnia zostajesz wkręcony do pewnego
bezsensownego szkolnego projektu (twoim zdaniem ;p). Masz przygotować,
12 stron internetowych, dla biblioteki w celu poinformowania
potencjalnych czytelników jakie rocznice literackie są obchodzone w
danym miesiącu. Jeśli chodzi o strony, hmmm porażka, nawet Web 1.0 to
nie ma być. Coś w stylu napisane w MS Office Word i zapisane jako strona
HTML. Ale problem jest tu, że tą humanitarną pracę masz wykonać przez
ferie zimowe, a każdy miesiąc to około 15 biografii, czyli +/- 180
nazwisk. ;/ Na szczęście interesuje się programowaniem ;)

| Każda osoba jest opisana mniej więcej tak:

(link do obrazka przepadł)

Więc jest zachowana jakaś logiczna kolejność, wg. której można coś
stworzyć.

Specyfikacja problemu:

- formularz wprowadzający dane
- zapis w sprecyzowanym systemie "dd.MM"-"która rocznica" "czego
   rocznica" "Imię i Nazwisko" "(Daty krańcowe)" "Krótka notka o osobie"
- zapis do pliku tekstowego i HTML

Ostatnio pod choinkę sprawiłem sobie `książkę`_ o nurtującej mnie
tematyce. Potaniłem połączyć zło konieczne, z samo doskonaleniem. Co z
tego wszyło, o tym na koniec. Na co dzień korzystam z Windowsa XP i
Mandrivy 2009.0 (jak na razie jako jedyny Linux obsługuje mojego Radeona
poprawnie), z bibliotek opisywanych w książce, mnie interesuje głównie
Qt, do wx-ów zamierzam wrócić później. Wcześniej uczyłem się C++, z
`Symfonii C++ Standard`_ i `Pasji C++`_, teraz zabieram się za `Thinking
in C++`_. Autorzy "C++. Wykorzystaj potęgę..." używają odpowiednio
wxDev-C++ i Dev-C++, mi te środowisko nie przypadło do gusty, chyba dla
tego że jest takie stare i masa komplikacji aby skompilować coś opartego
na Qt. Ostatnio głośno było o `QtCretorze`_, ale w tej chwili dla mnie
to przerost formy nad treścią. Cała aplikacja po prostu nie mieści się
na monitorze i nie da się jakoś dobrze pisać. Więc odpada. Potem było
Eclipse i jego dodatek pozwalający na tworzenie w Qt, jednak ten potwór
jakoś mnie odrzucił. Potem próbowałem jeszcze Code::Blocks,
bezskutecznie. Miałem ochotę włączyć Worda i pisać to ręcznie, ale...

... znalazłem go `QDevelop`_, to było to czego szukałem. Nie wiem
dlaczego tak trudno go znaleźć w Google, ale od teraz będzie
popularniejszy. Ten wieloplatformowy edytor przypadł mi do gustu, wykrył
zainstalowane Qt i MinGW, na Mandrivie zresztą po kompilacji i
doinstalowaniu paczek z qt też wszystko działało sprawnie. Mój projekt
napisany na windowsie, bez skompilował się na Linuksie, wiem że to nie
sprawa edytora tylko bibliotek, ale chodzi o to, że w cudowny sposób,
projekt jest przenoszalny i działa. Jak dla mnie QDevelop jest równy
funkcjonalnością QtCreatorowi, ale nie zajmuje masy pamięci, mieści się
na monitorze i pozwala na ukrycie wszystkiego co w danej chwili nie jest
potrzebne. No i przemawia w ojczystym języku. O samym programie postaram
się kiedyś jeszcze napisać, a dla wszystkich którzy już teraz chcą go
wypróbować, zalecam wyłączenie opcji auto kompilacji w ustawieniach,
ponieważ u mnie mało by nie zabiła mojego staruszka.

A teraz o moim projekcie, o ile zasługuje na takie miano. Nazwałem go
Biblios, nawet dorósł do wersji 2. Programik pozwala na szybkie
wprowadzanie danych o osobie, bo do obsługi wystarczy klawiatura klawisz
"Tab" pozwala na skakanie między polami. A kombinacja "Alt+D" dodaje
osobę, a "Alt+W" przygotowuje pola na przyjęcie kolejnej. Udało mi się
zaimplementować zapisywanie plików .txt jak również .html. Jestem
świadom tego czego programik robić jeszcze nie potrafi. Np. ustawianie
kodowania pliku HTML, ale i tak uważam, że to jest dobrze.

Postanowiłem udostępnić kod mojego programu razem z plikami
wykonywalnymi i bibliotekami dla windowsa, dla liuksa binaria dodam
później. Czekam na wasze opnie, wskazówki lub jakiekolwiek inne
komentarze w jakikolwiek sposób związane z poruszanym przeze mnie
tematem. No i gratuluje wszystkim tym, którzy przeczytali to wszystko i
zrozumieli "Co autor miał na myśli"™

- Pobierz Biblios v2: http://dl.getdropbox.com/u/168268/Biblios%20v2.zip
- Wersja dla Linux: http://dl.getdropbox.com/u/168268/Biblios_v2_linux.zip

.. _książkę: http://helion.pl/ksiazki/cppwyk.htm
.. _Symfonii C++ Standard: http://bzyx.jogger.pl/atom/content/html/150/www.ifj.edu.pl/~grebosz/symfonia_c++_std_p.html
.. _Pasji C++: http://www.ifj.edu.pl/~grebosz/pasjap.html
.. _Thinking in C++: http://helion.pl/ksiazki/thicpp.htm
.. _QtCretorze: http://www.qtsoftware.com/developer/qt-creator
.. _QDevelop: http://qdevelop.org/
