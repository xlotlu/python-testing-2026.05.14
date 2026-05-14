
Chestii despre Python:
----------------------

În Python __totul__ e un obiect!

în Python excepțiile sunt folosite pentru flow control, by design!

(flow control = "cum curge programul")


Ce (cum) testăm?
----------------

Testele au valoare de specificații !
(mai devreme sau mai târziu)


Exemplu de specificație low-level:

    Funcția is_valid_age returnează:
    - True pentru valori între 18 inclusiv și 60 exclusiv
    - False pentru toate celelalte valori

Exemplu de specificație high-level:

    Personalul acceptat pentru angajare va avea vârsta
    între 18 și 60 de ani, inclusiv respectiv exclusiv.

Exemplu de specificație și mai high-level, "user stories":
    user  = rolul ce îl are utilizatorul dpdv al sistemului
            ("admin", "manager", "collaborator", "anonymous")
    story = o funcționalitate a sistemului, povestită ca poveste

    Exemplu:
    Ca administrator de sistem, vreau să pot adăuga un utilizator nou,
    cu nume, username, parolă, și rol în sistem.

    Rolurile vor fi unul dintre: "admin", "manager", "collaborator", "anonymous".

        Din acesta se generează task-uri:
        - users: name, username, password, role 
        - admin interface
    




"regular" cases
corner cases = situații rare(!), improbabile
boundary cases = unde o diferență (mică) de la o valoare la alta generează schimbare în sistem



Forma canonică de rulat (în shell) unittest-uri:
------------------------------------------------

# un singur fișier:
python -m unittest myfile.py

# (sau modul)
python -m unittest mymodule

# sau mai multe fișiere deodată:
python -m unittest myfile1.py myfile2.py etc.py

# forma canonică-canonică de rulat în producție,
# folosind discover:
python -m unittest discover -s myfolder_with_tests




Instalare de pachete:
---------------------

(în shell-ul de sistem)

pip install ipython


Essential wisdom:
-----------------

There are 2 really hard things in computing:
- naming things
- cache invalidation
- off-by-one errors

