Damit die Beispiele funktionieren:

- wird Python benötigt

außerdem:

- in .env den OpenAI-API-Key angeben
- in .env für das Beispiel mit openweathermap.org auch WEATHER_API_KEY schreiben
- in .streamlit/secrets.toml den OpenAI-API-Key bei den Streamlit-Beispiele

Außerdem müssen die Bibliotheken installiert werden.

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
env\Scripts\activate

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
