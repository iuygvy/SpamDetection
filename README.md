# System wykrywania spamu w wiadomościach e-mail
Projekt implementuje system klasyfikujący wiadomości e-mail jako "spam" lub "nie spam". Opiera się o dwie technologie:
- CNN (sieć konwolucyjna)
- MLP (perceptron wielowarstwowy)

Dane wykorzystane do trenowania modelu to Enron-Spam dataset, zawierający ponad 33 tysiące wiadomości e-mail.

## Instrukcja uruchomienia
Zalecane jest najpierw pobranie notebooka **SpamDetection.ipynb** oraz pliku requirements.txt. Na samym początku notebook instaluje wszystkie wymagane biblioteki. Można to również zrobić bez pobierania notebooka, przez wpisanie w konsoli:
```
pip install -r requirements.txt
```
### Trenowanie modelu
1. Pobierz notebook SpamDetection.ipynb oraz folder tuner_trials i umieść je w jednym folderze.
2. Notebook krok po kroku poprowadzi cię przez proces trenowania modelu.

### Testowanie modelu na własnych danych
1. Pobierz pliki: spam_detector.h5, TestUserInput.py, tokenizer_msg.pkl oraz tokenizer_subj.pkl i umieść je w tym samym folderze.
2. W konsoli wpisz:
```
python TestUserInput.py
```
3. Program będzie kolejno pytał cię o podanie tematu oraz treści wiadomości e-mail (wpisz "exit" w temacie aby zakończyć).
   
**UWAGA - jako, że zbiór na którym uczony był program zawierał wyłącznie wiadomości w języku angielskim, również tylko w takim języku powinien być on testowany.**
