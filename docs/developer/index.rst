Geliştirici Kılavuzu
====================

**E/R Diagram**

   .. figure:: erDiagram.png
      :scale: 80 %
      :alt: ER Diagram
      :align: center

Veritabanındaki tablolar arası bağıntılar Er diagramda gösterilmiştir. Veritabanı "initialize_db.py" da tanımlanıp bazı değerler atanmıştır.

**initialize_db.py örnek kod**
   .. code-block:: python

      cursor.execute("""DROP TABLE IF EXISTS COUNTER""")
      cursor.execute("""CREATE TABLE COUNTER (N INTEGER)""")
      cursor.execute("""INSERT INTO COUNTER (N) VALUES (0)""")




.. toctree::

   member1
   member2
   member3
   member4
   member5
