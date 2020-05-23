# CV_Editor
##### Projekt zaliczeniowy na kurs Code:me - Python zaawansowany - Gdańsk, 2020

#### Aplikacja CV_Editor ma za zadanie umożliwienie przeglądu, dodawania, usuwania oraz edycji rekordów w bazie danych odpowiadających CV użytkowników.<br>

#### Korzystanie z aplikacji możliwe jest na 2 sposoby:<br>
- przez przeglądarkę internetową, po wejściu na adres http://127.0.0.1:5000/cv/
- przez postmana, curl, lub inne narzędzie mogące komunikować się z API pod adresem http://127.0.0.1:5000/api/cv/ - zakładając, że w konfiguracji aplikacji opcja API została włączona (UWAGA: w obecnej wersji aplikacji API nie jest zabezpieczone hasłem, a API jest domyślnie wyłączone)

#### Logowanie się do aplikacji:
- aplikacja dostępna jest po zalogowaniu się - w wersji podstawowej funkcjonuje jeden użytkownik "admin" a jego hasło przechowywane jest w pliku konfiguracyjnym config.py

#### Wymagania aplikacji:
- Python 3.8
- zainstalowane zależności z pliku requirements.txt
- przed pierwszym uruchonieniem aplikacji należy stworzyć bazę danych uruchamiając "plik db_recreate.py" znajdujący się w katalogu "/app"

#### Uruchomianie aplikacji:
- aby uruchomić serwer aplikacji, po spełnieniu wymagań, należy uruchomić plik "main.py" znajdujący się w katalogu "/app"

#### Struktura plików aplikacji:
/app - katalog z plikami aplikacji, zawierający między innymi plik "main.py" służący do uruchomienia aplikacji
/app/sql - pliki sql odpowiadające za komunikację z bazą danych
/app/templates - pliki html odpowiedzialne za prezentowanie informacji w przeglądarce
CV_Editor.db - domyślny plik bazy danych aplikacji
db_recreate.py - skrypt tworzący (lub odtwarzający podstawową wersję) bazę danych

#### Autor zezwala na dowolne korzystanie z aplikacji oraz wprowadzanie zmian we własnym zakresie, aczkolwiek nie ręczy za żadne skutki powyższych - każdy korzysta z niej na własną odpowiedzialność.

#### Kontakt do autora:
- andrzej.szulc@gmail.com

