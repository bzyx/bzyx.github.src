ONP
###
:date: 2009-11-28 20:42
:tags: politechnika śląska, jogger.pl, po-polsku
:slug: onp
:lang: pl

.. figure:: |filename| /images/2009/HP_35_Calculator.jpg
    :alt: "http://upload.wikimedia.org/wikipedia/commons/0/0e/HP_35_Calculator.jpg"

    HP-35 (obraz z http://wikimedia.org )

HP-35
~~~~~

To dziwne coś, na zdjęciu jest pierwszym kieszonkowym kalkulatorem
naukowym. Powstałym w 1972 roku. Te urządzenie powinno być ważne,
ponieważ zawiera układy scalone, LED. Magazyn Forbes ASAP uznał go za
jedno za jeden z "produktów wszech czasów, które zmieniły świat",a
niedawno otrzymał nagrodę IEEE Milestone, jednak nie było by tego
wszystkiego gdyby nie wynalazek powstały 21 lat wcześniej. Do
zaimplementowania naukowych działań użyto RPN

ONP=RPN
~~~~~~~

Odwrotna Notacja Polska, opracowana w 1951 przez Jana Łukasiewicza, jest
wielkim polskim wkładem w światową informatykę, o czym mało kto wie. Ten
całkiem prosty zapis, pozwolił na znaczne uproszczenie oprogramowywania
rożnych operacji. ONP była używana nie tylko w kalkulatorach, ale nadal
jest obecna w informatyce w m.in PostScript-cie.

Jak to wygląda
^^^^^^^^^^^^^^

Przykład w notacji infiksowej (zapis klasyczny)

    sin(a)\*x+b

Zapis w ONP

    asinx\*b+

Coś większego:

    (sin a \* (x+y))/(a \* cos (Nb - x)-sin(x + b\*y) +c)

w ONP:

    asinxy+\*a\*bNx-cos-xb+y\*sinc+/

Widać wyraźnie jak taki zapis uprasza skomplikowane działania z punktu
widzenia prostej maszyny liczącej. Nie mamy zadanych nawiasów.

A to wszystko w nawiązaniu do...
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

... zajęć z Podstaw Informatyki, dawno nie pisałem nic tutaj, bo studia
jakoś chorobliwie zabierają mi czas i wszelką motywację. Zauważam :(, że
studiowanie informatyki, znacznie różni się od tego jak sobie to
wyobrażałem, ale nie ma tego złego co by na dobre nie wyszło. :) Różne
dziwne ciekawostki pozwalają na rozwój i budzą ciekawość, tylko czy
przyda mi się to jeszcze kiedykolwiek... poza egzaminem w II semestrze.

Ciekawe, czy tylko na studiach inżynierskich na Politechnice Śląskiej
tego uczą?

Linki
^^^^^

`ONP na Wikipedii`_
`HP-35 na EN.WIkipedia`_
`Artykuł o RPN(ONP) w HP Journal`_
`Artykuł o RPN w "The Museum of HP Calculators"`_

.. _ONP na Wikipedii: http://pl.wikipedia.org/wiki/ONP
.. _HP-35 na EN.WIkipedia: http://en.wikipedia.org/wiki/HP-35
.. _Artykuł o RPN(ONP) w HP Journal: http://www.hp.com/hpinfo/abouthp/histnfacts/museum/personalsystems/0023/other/0023hpjournal02.pdf
.. _Artykuł o RPN w "The Museum of HP Calculators": http://www.hpmuseum.org/rpn.htm
