# Generative KI in Python

Dies ist das Repository für den **LinkedIn Learning** Kurs `Generative KI in Python`. Den gesamten Kurs finden Sie auf [LinkedIn Learning][lil-course-url].

![COURSENAME][lil-thumbnail-url] 

Python ist die ideale Programmiersprache für die praktische Umsetzung von künstlicher Intelligenz in Ihren Anwendungen. Florence Maurice bringt Ihnen die neuesten Tools und Technologien nahe  und versetzt Sie mit diesem LinkedIn Learning-Kurs in die Lage, generative KI-Anwendungen mit der OpenAI API und Python zu erstellen. Am Ende des Kurses haben Sie wichtige Begriffe wie Tokens, Embeddings und Funktionen kennengelernt und Sie beherrschen zwei zentrale APIs für die Programmierung von KI-Anwendungen.
Mit der Hilfe von zahlreichen Challenges/Solutions-Einheiten können Sie das erworbene Wissen immer wieder testen und anschließend Ihre Lösung mit der Ihrer Trainerin vergleichen.


## Anleitung

Dieses Repository hat Ordner für die einzelnen Kapitel.


## Installation

1. Um diese Übungsdateien nutzen zu können, müssen Sie folgendes installiert haben:
   
   - Python
     
außerdem müssen Sie

- in .env den OpenAI-API-Key angeben
- in .env für das Beispiel mit openweathermap.org auch WEATHER_API_KEY schreiben
- in .streamlit/secrets.toml den OpenAI-API-Key bei den Streamlit-Beispiele

Zudem müssen die Bibliotheken installiert werden.

Es empfiehlt sich, vorher eine virtuelle Umgebung anzulegen.

(Windows)

```
python -m venv env
```

(MacOS)

```
python3 -m venv env
```

## Virtuelle Umgebung aktivieren

(Windows)
```
env\Scripts\activate
```
(MacOS)

```
source env/bin/activate
```

Damit alles wie in den Videos gezeigt funktioniert, sollten die in requirements.txt angegebenen Versionen installiert werden.
Das geht über:

```
pip install -r requirements.txt
```

bzw. eventuell

```
pip3 install -r requirements.txt
```

2. Klonen Sie das Repository in Ihre lokale Maschine unter Verwendung von terminal (Mac), CMD (Windows) oder ein anderes Werkzeug mit grafischer Bedienoberfläche wie SourceTree.


## Autorin
**Florence Maurice**

_Autorin und Trainerin_

Sehen Sie sich andere Kurse der Autorin auf [LinkedIn Learning](https://www.linkedin.com/learning/instructors/florence-maurice) an.


[0]: # (Replace these placeholder URLs with actual course URLs)
[lil-course-url]: https://www.linkedin.com/learning/generative-ki-in-python
[lil-thumbnail-url]: https://media.licdn.com/dms/image/v2/D4E0DAQESV8BSxWYpcQ/learning-public-crop_675_1200/learning-public-crop_675_1200/0/1725877566510?e=2147483647&v=beta&t=pWa8jvdq6ZiCg8JNUKu4wddVlTxENbiAeR1s0I6gX2s
