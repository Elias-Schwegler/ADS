# 🤖 ADS Wochen-Zusammenfassung – Prompt-Template

> **Zweck:** Diesen Prompt bei jeder neuen Semesterwoche verwenden, damit der Agent automatisch eine optimale Prüfungszusammenfassung im gleichen Format erstellt.

---

## Prompt (Copy-Paste für jede neue Woche)

```
Erstelle eine umfassende Prüfungszusammenfassung für die aktuelle Semesterwoche (SWXX) des Moduls "Algorithmen & Datenstrukturen" (ADS, HSLU).

Das Ausgabeformat ist ein Markdown-File namens ZUSAMMENFASSUNG_SWXX.md im entsprechenden SW-Ordner.

### Struktur & Inhalt (in dieser Reihenfolge):

1. **Header**: Modulname, Dozent, Wochennummer, Thema, Prüfungsformat-Erinnerung
2. **🎯 Lernziele**: Exakt aus den Folien übernommene Lernziele
3. **📖 Wichtigste Begriffe**: Tabelle mit Begriff + Definition aller neuen Konzepte
4. **📐 Konzepte & Theorie**: Detaillierte Erklärung der durchgenommenen Konzepte mit:
   - Definitionen und Formeln
   - Visuelle Darstellungen (ASCII-Art / Tabellen wo hilfreich)
   - Schritt-für-Schritt Ablaufbeispiele
5. **📊 Klassifizierungen / Vergleiche**: Tabellen die Algorithmen, Datenstrukturen oder Verfahren gegenüberstellen (Laufzeit, Vor-/Nachteile)
6. **⏱️ Komplexitätsanalyse**: Für jeden besprochenen Algorithmus:
   - Worst Case, Best Case, Average Case (falls relevant)
   - O-Notation
   - Zähl-Schema (wie werden Operationen gezählt)
7. **💻 Wichtigste Code-Beispiele**: Alle relevanten Implementierungen in **Python**, mit:
   - Kommentaren auf Deutsch
   - Erklärung des Algorithmus vor dem Code
   - Code aus den Musterlösungen (ML) bevorzugen
8. **📝 Übungsaufgaben-Zusammenfassung**: Tabelle aller Übungen mit Thema und Kernkonzept
9. **⚠️ Prüfungsrelevante Hinweise**: 
   - Typische Aufgabentypen
   - Häufige Fehlerquellen
   - Tricks und Merkregeln
10. **🔗 Verbindung zu vorherigen Wochen**: Kurzer Rückbezug, wie der Stoff aufbaut

### Wichtige Regeln:
- **Sprache:** Deutsch (Fachbegriffe dürfen Englisch bleiben)
- **Code:** Ausschliesslich Python
- **Quellen:** Alle PDFs im SW-Ordner durchlesen (Folien, Übungen AS & ML)
- **Hinweise auf Prüfungsinhalte** aus anderen Dokumenten extrahieren (z.B. Semesterplan, Testate, Einführungsfolien)
- **Formeln** in lesbarer Form darstellen
- **Emojis** als Section-Icons verwenden für schnelles Scannen
- **Tabellen** bevorzugen für Vergleiche und Übersichten
- Das File soll so vollständig sein, dass man damit alleine die Prüfung bestehen kann
- **Gausssche Summenformel und ähnliche Schlüsselformeln** immer hervorheben
- **Ratio-Trick** bei Laufzeitmessungen erklären (Verdopplung → x4 = O(n²), etc.)
```

---

## Ordnerstruktur-Erwartung

```
ADS/
├── Informationen zum Modul/
│   ├── Semesterplan_v1.0.pdf
│   ├── Testate/Testate_v1.0.pdf
│   └── Lehrmittel/
├── SW01 - .../
│   ├── 00_Introduction_v1.0.pdf
│   ├── 01_ComplexityRecursion_v1.0.pdf
│   ├── U01_Python_AS/   (Aufgabenstellung)
│   ├── U01_Python_ML/   (Musterlösung)
│   └── ZUSAMMENFASSUNG_SW01.md  ← Output
├── SW02 - .../
│   ├── *.pdf
│   ├── U02_Python_AS/
│   ├── U02_Python_ML/
│   └── ZUSAMMENFASSUNG_SW02.md  ← Output
├── ...
└── Prompt.md  ← Diese Datei
```

## Hinweise für den Agent

- Zuerst den **SW-Ordner** der aktuellen Woche auslesen
- PDFs mit `pymupdf` (fitz) extrahieren und als `.txt` zwischenspeichern
- Python-Dateien direkt lesen (sowohl AS als auch ML)
- Semesterplan und Testate-Info für Kontext konsultieren
- ZUSAMMENFASSUNG aus vorherigen Wochen lesen für Querverweise
- Temporäre `.txt`-Dateien nach dem Erstellen der Zusammenfassung entfernen
