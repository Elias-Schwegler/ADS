# 📄 How to Read PDFs – Agent-Anleitung

> **Zweck:** Der Agent kann PDF-Dateien nicht direkt mit `view_file` lesen. Diese Anleitung beschreibt, wie man PDFs (z.B. Vorlesungsfolien) in lesbaren Text umwandelt.

---

## Methode: PyMuPDF (fitz)

**PyMuPDF** ist bereits installiert (`pip install pymupdf`) und extrahiert Text seitenweise aus PDF-Dateien.

### Vorhandenes Helper-Script

Das Script liegt unter `Slides/extract_pdf.py` und kann direkt verwendet werden:

```bash
python Slides/extract_pdf.py "Pfad/zur/Datei.pdf" "Pfad/zur/Ausgabe.txt"
```

### Script-Inhalt (falls neu erstellt werden muss)

```python
import fitz
import sys

pdf_path = sys.argv[1]
output_path = sys.argv[2]

doc = fitz.open(pdf_path)
num_pages = len(doc)

with open(output_path, 'w', encoding='utf-8') as f:
    for i, page in enumerate(doc):
        text = page.get_text()
        f.write(f'=== PAGE {i+1} ===\n')
        f.write(text)
        f.write('\n\n')

doc.close()
print(f'Done. Extracted {num_pages} pages to {output_path}')
```

### Workflow für den Agent

1. **PDF identifizieren** – z.B. `Slides/week-01.pdf`
2. **Text extrahieren** – `python Slides/extract_pdf.py "Slides/week-01.pdf" "Slides/week01_text.txt"`
3. **Text lesen** – `view_file` auf die generierte `.txt`-Datei anwenden
4. **Aufräumen** – temporäre `.txt`-Dateien nach Verarbeitung löschen

### Hinweise

- Das Output-Format trennt Seiten mit `=== PAGE X ===` Markern
- Bei sehr grossen PDFs (>100 Seiten) ggf. in Teilen lesen (`StartLine`/`EndLine`)
- **Bilder und Diagramme** in PDFs werden **nicht** extrahiert – nur Text
- Für Slide-Decks: Der extrahierte Text enthält Überschriften, Bullet Points und Annotationen, aber kein Layout
