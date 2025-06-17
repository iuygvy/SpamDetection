# System wykrywania spamu w wiadomościach e-mail
Projekt implementuje system klasyfikujący wiadomości e-mail jako "spam" lub "nie spam". Opiera się o dwie technologie:
- CNN (sieć konwolucyjna)
- MLP (perceptron wielowarstwowy)

Dane wykorzystane do trenowania modelu to Enron-Spam dataset, zawierający ponad 33 tysiące wiadomości e-mail.

## Instrukcja uruchomienia
Zalecane jest najpierw pobranie notebooka **SpamDetection.ipynb** oraz pliku **requirements.txt**. Na samym początku notebook instaluje wszystkie wymagane biblioteki. Można to również zrobić bez pobierania notebooka, przez wpisanie w konsoli:
```
pip install -r requirements.txt
```
### Trenowanie modelu
1. Pobierz notebook **SpamDetection.ipynb** oraz plik **best_hyperparameters.json** i umieść je w jednym folderze. Jeśli chcesz samemu znaleźć najlepsze hiperparametry, zalecane jest również pobranie folderu **tuner_trials**.
2. Notebook krok po kroku poprowadzi cię przez proces trenowania modelu.

### Testowanie modelu na własnych danych
1. Pobierz pliki: **spam_detector.h5**, **TestUserInput.py**, **tokenizer_msg.pkl** oraz **tokenizer_subj.pkl** i umieść je w jednym folderze.
2. W konsoli wpisz:
```
python TestUserInput.py
```
3. Program będzie kolejno pytał cię o podanie tematu oraz treści wiadomości e-mail (wpisz "exit" w temacie aby zakończyć).
   
**UWAGA - jako, że zbiór na którym uczony był program zawierał wyłącznie wiadomości w języku angielskim, również tylko w takim języku powinien być on testowany.**

## Architektura modelu
Model składa się z dwóch głównych części:

- Po pierwsze, wykorzystałem warstwy konwolucyjne (CNN), które działają jak filtr — przeszukują tekst i wykrywają lokalne wzorce, np. charakterystyczne wyrażenia lub kombinacje słów typowe dla spamu. To podejście sprawdza się dobrze przy analizie tekstu, bo pozwala uchwycić znaczenie fragmentów zdania — niezależnie od ich dokładnego położenia.

- Następnie wyniki z warstw konwolucyjnych trafiają do klasycznego bloku MLP, czyli multilayer perceptronu — czyli kilku gęsto połączonych warstw neuronowych. To część, która łączy wszystkie informacje i podejmuje ostateczną decyzję — czy dana wiadomość to spam, czy nie.

Dodatkowo do wejścia MLP dołączyłem cechy pomocnicze, takie jak długość wiadomości, liczba cyfr czy znaków specjalnych. Dzięki temu model mógł patrzeć nie tylko na treść, ale i na strukturę wiadomości.

W celu znalezienia jak najlepszych hiperparametrów modelu, wykorzystałem KerasTuner i wykonałem ponad 100 prób z różnymi parametrami. Wyniki prób zapisane są w folderze tuner_trials.

## Motywacja
Spam to wciąż bardzo powszechny problem — zarówno w e-mailach, jak i w innych kanałach komunikacji. Codziennie wysyłane są miliony wiadomości, które mają na celu oszustwa, reklamy albo po prostu generują szum informacyjny. Ręczna moderacja takich treści byłaby nie tylko kosztowna, ale też zupełnie niewydajna. 

Dobrze działające filtry spamu pozwalają nie tylko oszczędzić czas użytkowników, ale też zwiększają ich bezpieczeństwo, chroniąc przed phishingiem czy złośliwym oprogramowaniem. 

Dodatkowo, coraz łatwiej jest generować spam automatycznie — przy pomocy AI, botów czy skryptów. Dlatego skuteczne, inteligentne metody filtrowania są dziś ważniejsze niż kiedykolwiek wcześniej.

## Cel
Celem projektu było stworzenie systemu, który automatycznie rozpoznajewiadomości spamowe na podstawie ich treści i innych cech. Zależało mi na tym, aby klasyfikacja nie opierała się wyłącznie na słowach kluczowych, ale uwzględniała szerszy kontekst — np. długość wiadomości, częstość słów, obecność podejrzanych wzorców. 

Ostatecznym celem było osiągnięcie jak najwyższej skuteczności w klasyfikacji — przyjednoczesnym ograniczeniu tzw. błędów alarmowych, czyli sytuacji, w których zwykła wiadomość zostaje błędnie oznaczona jako spam.
