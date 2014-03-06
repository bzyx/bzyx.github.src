Czy wiesz, że ?
###############
:date: 2011-03-24 18:52
:tags: c, jogger.pl, po-polsku
:slug: czy-wiesz-ze
:lang: pl

Utwórz plik z kodem w C++. (np. test.cpp) Napisz cokolwiek, chcesz, byle
by się kompilowało.

.. code:: bash

    gcc test.cpp -Wa,-adhln,-L -g -c > test.txt

Mocno się zdziwiłem gdy zobaczyłem co uzyskałem. Jeśli chcesz swój kod w C++ doprowadzić tylko do postaci asemblera wystarczy opcja -S.

