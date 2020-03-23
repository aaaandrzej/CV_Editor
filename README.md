# CV_Editor
#### Projekt zaliczeniowy na kurs Code:me - Python zaawansowany

W ramach projektu użytkownik stworzy od podstaw aplikację RESTową służącą do tworzenia i edycji danych CV przy wykorzystaniu frameworku Flask. Aplikacja będzie wspierać autentykację użytkowników za pomocą hasła i ich autoryzację. Projekt nie przewiduje stworzenia frontu do aplikacji - obsługa odbywać się bedzie za pomocą Postman lub podobnego narzędzia.

W celu lepszego poznania i zrozumienia działania aplikacji, uczestnik powinien w jak największym stopniu, samodzielnie zaimplementować konieczną funkcjonalność (np. routing, autoryzacja), ograniczając używanie zewnętrznych modułów do minimum.

W aplikacji będą istnieć trzy grupy użytkowników:
- pracownicy, którzy mają dostęp tylko do swojego CV i mają możliwość jego edycji
- kadry, które nie mają możliwości edycji CV, ale mają możliwość pobierania CV konkretnego użytkownika oraz mogą generować statystyki zbiorcze (np. ilu pracowników posiada znajomość Pythona na każdym z dostępnych poziomów),
- admini, którzy mają uprawnienia takie, jak kadry, a poza tym mają możliwość tworzenia i edycji kont użytkowników.

Na CV pracownika składają się dwa różne rodzaje elementów:
- znajomość wybranej technologii przez pracownika w skali od 1 do 5.
- doświadczenie zawodowe (nazwa firmy, opis projektu, lata pracy)

W wyniku projektu użytkownik nabierze praktycznych umiejętności związanych z:
- projektowaniem poprawnego interfejsu RESTowego
- projektowaniem optymalnego schematu bazy danych
- tworzeniem aplikacji RESTowej z wykorzystaniem Flask i SQLAlchemy
- dobrymi praktykami z zakresu autoryzacji i autentykacji użytkowników
- optymalnym tworzeniem zapytań do bazy danych uwzględniających agregację danych z kilku tabel i obliczanie danych statystycznych

### Sprinty

#### Sprint 1

- Zaprojektowanie interfejsu RESTowego aplikacji i schematu bazy danych.
- Utworzenie nowego projektu pythonowego z zależnością dla frameworku Flask.
- Utworzenie stubów dla wszystkich endpointów RESTowych (z wyjątkiem zarządzania użytkownikami i logowania)

#### Sprint 2
- Dodanie do projektu modułu SQAlchemy.
- Konfigurowanie połączenia z bazą danych i sesji.
- Stworzenie pythonowych modeli dla wszystkich tabel.
- Dodanie do projektu modułu do migracji schematu bazy danych (alembic).
- Implementacja endpointów.

#### Sprint 3
- Dodanie autoryzacji i autentykacji użytkowników.
- Dodanie endpointów do zarządzania użytkownikami i zmiany własnego hasła przez użytkownika.
- Zabezpieczanie aplikacji (endpointów) przed nieuprawnionym dostępem.

#### Sprint 4 (dodatkowy)

Propozycje:
- Zaimplementowanie SSO
- Deployment aplikacji do chmury AWS

#### Test końcowy
Weryfikacja kodu. Rozmowa sprawdzająca nabyte umiejętności i zastosowane rozwiązania.

Do powyższego należy dodać założenia projektu zaliczeniowegoo CODE:ME