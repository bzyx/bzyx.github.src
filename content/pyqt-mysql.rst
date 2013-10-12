PyQt + MySQL
############
:date: 2012-02-15 18:42
:tags: python, qt, pyqt, po-polsku, jogger.pl
:slug: pyqt-mysql
:lang: pl

*W sumie to piszę to dla własnej pamięci, żeby już nigdy nie musieć
kombinować kilka godzin dlaczego nie mam połączenia z bazą danych...*

.. raw:: html

   </p>

Otóż PyQt ma sterownik MySQLa w standardzie, tylko czasami jakby nie
wszytko chce działać od razu i nikt nie wie dlaczego, w sumie cały
internet. Sam ciągle nie wiem czemu to nie działało, skoro coś
analogicznego dla SQLite działa.

.. raw:: html

   </p>

Otóż jeśli dostaniesz "Driver not loaded " wypróbuj to:

.. raw:: html

   </p>

.. raw:: html

   </p>
.. code-block:: python

  # this little monkey has to be here
  app = QApplication(sys.argv)


  # rest of the code
  db = QSqlDatabase.addDatabase("QMYSQL")

  db.setHostName ( db_host )
  db.setUserName ( db_user )
  db.setPassword ( db_passwd )
  db.setDatabaseName ( db_db )
  db.setPort ( db_port )
  
  db.setConnectOptions("CLIENT_SSL=1;CLIENT_IGNORE_SPACE=1")
  db.open()
  
  defaultDB = QSqlDatabase.database()
  query = QSqlQuery("SELECT * FROM Users")
  
  qe = query.exec_()
  print "query exec" , query.exec_()
  if not qe:              # if error
      print QSqlQuery.lastError( query ).text()
  else:                   # else display returned values
      while query.next():
	  print "query value" , query.value(0).toString()
  
  
  db.close()
   
http://wklej.org/id/689436/

.. raw:: html

   </p>

.. raw:: html

   </p>

U mnie, jak ręką odjął... ;)

.. raw:: html

   </p>

http://stackoverflow.com/questions/7402963/qsql-connect-and-read-from-database-example-driver-not-loaded

.. raw:: html

   </p>

