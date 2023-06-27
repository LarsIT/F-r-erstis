# TutSoSe23-prvt Hausarbeit
Das Readme dient als Übersicht und Plan der Hausarbeit.

## Thema  

Thema der Hausarbeit ist das automatische extrahieren von sinnvollen Keywords eines Textes. Mit der Hausarbeit können 9 Punkte als Klausurvorleistung erzielt werden. <br>
Das Programm soll für jeden Text 3 Keywordlisten erstellen und ausgeben, jeweils eine basierend auf eine der Keyword-Extraction Methoden (s. Keyword Extraction). <br>

**Ziel** ist es ein Programm zu schreiben, bzw zu vervollständigen, welches man als Hilfsmittel nutzen kann um begründete Aussagen über einen Text und seine Inhalte zu treffen.

### Keyword Extraction

wir werden 3 Herangehensweisen nutzen um die Keywords zu extrahieren

- Wordcount
- Collocation-count
- TF-IDF(Term Frequency - Inverse Document Frequency)

# Information zu den Aufgaben

Es gibt **5 Funktionen** die erstellt werden sollen, davon bringt jede einen Punkt, **die Textbeschaffung** mittels einer API Abfrage und die **Berechnung der TF-IDF Werts** welche beide auch einen Punkt bringen. Die restlichen 2 Punkte gibt es bei für die Präsentation der Ergebnisse. <br>
Um zu Präsentieren müssen nicht alle Funktionen gemacht worden sein, außerdem wird es dann noch "Präsentationstexte" geben, damit ihr nicht einfach da steht und alle den gleichen Kram erzählt :)

Ihr könnt diese README gerne als Checkliste benutzen, füllt dafür einfach die folgenden Kästchen z.B. mit einem "x" aus wenn ihr die Aufgabe erledigt habt.

Es gibt 2 Arten von Aufgaben, *Aufgaben* und *Funktionen*. Aufgaben sind Aufgaben die in main.py bearbeitet werden sollen, Funktionen sollen in ihren respektiven Dateien bearbeitet werden. Vorlagen zu den jeweiligen Funktionen liegen vor. <br>
Auf diese Weise behalten wir unsere Hauptdatei aufgeräumter und übersichtlicher.

Es wird sehr wahrscheinlich euer erster Ansatz nicht funktionieren, das ist nicht schlimm :) <br>
Daher lest euch eure Fehlermeldungen durch und arbeitet mit dem VS-Code Debugger (oder einem anderem Debugging-Tool), den VS-Code Debugger werden wir auch noch im Tutorium behandeln, schadet aber nicht wenn ihr das auch schonmal selber macht ;)

Lasst euch nicht von den Variablen irritieren die im Format '"var_name":dtype[...] = ...' initialisiert werden, den Teil nach dem Doppelpunkt nennt man Typehint, also ein Hinweis welche Datentyp diese Variable haben soll. <br>
Es gibt viele Möglichkeiten die Aufgaben zu lösen, daher sind auch die Code Vorlagen nur Vorschläge die benutzt werden können. Aber wenn ihr andere von den Typehints und den Anweisungen komplett abweisende Herangehensweisen wählt müsst ihr auch die main.py Datei anpassen, denn diese ist auf die Typehints und Anweisungen zugeschnitten.<br>
**ABER** die Ausgabe im Terminal von den Ergebnissen pro Dokument sollte im Format...

```
Titel von Dokument
Keywords die durch Wordcount entstehen
Keywords die durch Collocations entstehen
Keywords die durch TF-IDF entstehen
```
...sein. <br>
Das ist für die Vergleichbarkeit der Ergebnisse


---

# Checkliste Aufgaben

- ### 1. [ ] API Abfrage
- ### 2. [ ] clean_text()
- ### 3. [ ] count_elements()
- ### 4. [ ] compute_tf()
- ### 5. [ ] compute_idf()
- ### 6. [ ] TF-IDF berechnen
- ### 7. [ ] collocations() ODER collocations_simple()

---
***WICHTIG*** Begriffsklärung

Dokument: Ein Text <br>
Corpus/Korpus: Sammlung von Texten <br>


---

# Aufgabenstellungen

## 1. API Abfrage - Aufgabe

> ### bearbeitungsort: main.py

Da wir noch keine Texte zum analysieren haben müssen wir uns diese zunächst beschaffen. Die Texte stammen von der Zeitung **TheGuardian**, wir beschaffen uns diese mit deren öffentlicher API-Schnittstelle. Dafür liegt ein api_key in main.py vor, sowie api-search-tags in dem res Ordner in article_tags.py. 

Lest euch die Dokumentation der API durch um herauszufinden wie ihr mit den gegebenen Tags an die benötigten Texte kommt.

[Guardian API DOCUMENTATION](https://open-platform.theguardian.com/documentation/)

Die Aufgabe ist es hier die Text-Zusammenfassungen zum Corpus hinzuzufügen.

---

## 2. clean_text() - Funktion

> ### Bearbeitungsort: general.py

Erstelle eine Funktion welche einen Text als Input nimmt und alle "delimiter" entfernt. Die Funktion soll diesen "gesäuberten" Text wieder ausgeben.

---

## 3. count_elements() - Funktion

> ### Bearbeitungsort: collocation.py

Erstelle eine Funktion die eine Liste von Strings als Parameter nimmt diese zählt und ein Dictionary erstellt um für jedes gezählte Element eine Häufigkeit festzuhalten.
Zuletzt soll die Funktion auch das Häufigkeitsdictionary nach den Häufigkeiten absteigend sortieren und dieses Dictionary ausgeben.

Tipp: Schaut euch für das Sortieren mal lambda-Funktion an :)

---

## 4. compute_tf() - Funktion

> ### Bearbeitungsort: calculations.py

Erstelle eine Funktion die die relative Wort-Häufigkeit von jedem Wort eines Dokuments berechnet und ein Dictionary, mit den Wörten als Key und deren Häufigkeit in dem Dokument als Value, ausgibt.
Die Funktion nimmt eine Liste von Wörtern als Parameter.

Um die relative Häufigkeit auszurechnen braucht ihr die Gesamtanzahl der Wörter vom Dokument, da wir sonst den Worten keine Gewichtung, beim auftreten, zuweisen können.

---

## 5. compute_idf - Funktion

> ### Bearbeitungsort: calculations.py

Erstelle eine Funktion welche für jedes Wort die inverse Dokumentenhäufigkeit(IDF) berechnet. Als Parameter wird ein Set von allen Wörten die im Corpus vorkommen benötigt, sowie der Corpus selbst.
Als Ausgabe brauchen wir ein Dictionary mit dem Wort als Key und dem IDF-Wert als Value.

Es gibt im Internet viele Quellen zum nachlesen wie man den IDF berechnet. Also, ran an die Recherche!

---

## 6. TF-IDf berechnen - Aufgabe

> ### Bearbeitungsort: main.py 

Der tf_idf score muss pro Dokument berechnet werden.
Berechne ihn und füge ihn zu tf_idf_complete hinzu.
tf_idf_complete soll eine Liste sein mit einem Dictionary pro Dokument, jedes Dictionary hat ein Wort als Key und seinen TF-IDF Scord als Value.

---

## 7. filter_elements() - Funktion

> ### Bearbeitungsort: general.py

Erstelle eine Funktion die 2 Parameter akzeptiert. Das erste ist ein Dictionary, welches gefiltert werden soll. Das 2. Parameter "condition" ist die Kondition an der das Dicitonary gefiltert werden soll, die Funktion soll ein gefiltertes Dictionary wieder ausgeben.

---

## 8. Collocation

> ### Bearbeitungsort: collocation.py

Collocations sind Wortpaare die im Dokument vorkommen. <br>
Ihr könnt euch hier entscheiden ob ihr eine simple oder komplexe Version der collocation-Funktion erstellt. Die Versionen unterscheiden sich in der länge der Wortpaare die sie ausgeben kann. <br>
Beide Funktionen geben eine Liste von Wortpaaren, die im Dokument vorkommen, aus.

Wenn ihr die fortgeschrittene Version nicht macht, macht Aufgabe 9 wenig Sinn, daher schaut euch Aufgabe 8.1 wenigstens an und versucht euch hier dran.

#### **8.1** collocations() - Funktion (Fortgeschritten)

Die Fortgeschrittene Version kann eine beliebig lange Wortpaarlänge ausgeben.

Ein Tipp zum überprüfen ob die Funktion richtig funktioniert: <br>
Es gibt immer (n-l+1) Collocations, mit n = Gesamtanzahl_Worte und l = variable_länge 

Tipp:  Ich habe eine weitere Funktion benutzt -> merge_str (Hilfsfunktion für 8.1), Vorlage dazu ist auch in collocation.py

##### merge_str (Hilfsfunktion):
Erstelle eine Funktion die Strings zusammenfügt. <br>
Dafür nehmen wir eine Liste von Strings als Parameter, fügen die Elemente dieser Liste zusammen und geben den zusammenfügten String aus

#### **8.2** collocation_simple() - Funktion

Die simple Version soll nur eine Wortpaarlänge von 2 ausgeben, daher wird hier nur ein Parameter benötigt, die Wortliste (s. Aufgabe 2).
Sie gibt eine Liste von Wortpaaren die im Dokument vorkommen aus.
 
