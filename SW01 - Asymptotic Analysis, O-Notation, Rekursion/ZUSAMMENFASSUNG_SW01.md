# 📘 ADS – SW01: Asymptotic Analysis, O-Notation, Rekursion

> **Modul:** Algorithmen & Datenstrukturen (ADS) – FS26, HSLU ICS/AIML
> **Dozent:** Th. Letsch
> **Prüfungsformat:** Open-Book (beliebige Unterlagen erlaubt, **keine elektronischen Hilfsmittel**)
> **Testate:** Übungen 10 & 12 – mind. 1 von 2 muss bestanden sein (Abgabe Fr 01.05.26 / Fr 15.05.26)

---

## 🎯 Lernziele SW01

1. Die **Komplexität einer Codesequenz analysieren** und mit der **O-Notation klassifizieren** und beschreiben.
2. Ein **rekursives Problem** mit Python lösen.

---

## 📖 Wichtigste Begriffe

| Begriff | Definition |
|---|---|
| **Algorithmus** | Step-by-step Anweisung zum Lösen eines Problems mit begrenztem Zeitaufwand |
| **Primitive Operation** | Elementare Rechenoperation, die in konstanter Zeit ausführbar ist |
| **Laufzeitkomplexität** | Anzahl primitiver Operationen als Funktion der Eingabegrösse `n` |
| **Worst Case** | Maximale Anzahl Operationen über alle möglichen Eingaben der Grösse `n` |
| **Best Case** | Minimale Anzahl Operationen über alle möglichen Eingaben der Grösse `n` |
| **O-Notation (Big-O)** | Qualitative Aussage über das Laufzeitverhalten eines Algorithmus ab einer bestimmten Grösse |
| **Iteration** | Wiederholte Ausführung eines Codeabschnitts (Schleifen: `for`, `while`) |
| **Rekursion** | Eine Funktion ruft sich selbst auf (direkt oder indirekt) |
| **Direkte Rekursion** | Funktion ruft sich selbst wieder auf |
| **Indirekte Rekursion** | Funktion A ruft B auf, B ruft A wieder auf |
| **Verankerung (Base Case)** | Endbedingung einer Rekursion, die den Abbruch sicherstellt |
| **Gausssche Summenformel** | `1 + 2 + ... + n = n * (n+1) / 2` |
| **In-Place** | Algorithmus arbeitet direkt auf der übergebenen Datenstruktur, ohne zusätzlichen Speicher |
| **Arithmetische Folge** | Folge mit konstantem Differenz-Schritt `d` zwischen aufeinanderfolgenden Gliedern |

---

## 📐 Primitive Operationen (Zählregeln)

Folgende Operationen werden als **je 1 primitive Operation** gezählt:

| Operation | Beispiel |
|---|---|
| Evaluation eines Ausdrucks | `a + b`, `x > y` |
| Zuweisung eines Wertes | `x = 5` |
| Indexieren eines Arrays | `A[i]` |
| Aufruf einer Methode / Funktion | `foo()` |
| Verlassen einer Methode (return) | `return x` |

### Wie wird gezählt? – Beispiel `arrayMax`

```
Algorithm arrayMax(A, n)           # Operationen
currentMax = A[0]                  → 2   (1 Index + 1 Zuweisung)
for i = 1 to n-1 do               → 1 + 2n (1 Init + n Vergleiche + n Inkremente)
    if A[i] > currentMax then      → 2(n-1) (1 Index + 1 Vergleich) × (n-1)
        currentMax = A[i]          → 2(n-1) (1 Index + 1 Zuweisung) × (n-1) [Worst Case]
    { increment counter i }        → 2(n-1)
return currentMax                  → 1
```

| Fall | Formel | Vereinfacht |
|---|---|---|
| **Worst Case** | `2 + (1+2n) + 3×2(n-1) + 1` | **8n − 2** |
| **Best Case** | `2 + (1+2n) + 2×2(n-1) + 1` | **6n** |

> 💡 **Erkenntnis:** Konstante Faktoren und tiefere Potenzen haben keinen Einfluss auf die O-Notation!

---

## 📊 Komplexitätsklassen (O-Notation)

### Definition

> **f(n) ist O(g(n))**, wenn es eine positive Konstante **c** und ein **n₀** gibt, so dass:
> **f(n) ≤ c · g(n)** für alle **n ≥ n₀**

### Beispiel
- `2n + 10 ≤ 3·n` für `n ≥ 10` → also: `2n + 10` ist **O(n)**

### Übersicht der Komplexitätsklassen (aufsteigend)

| O-Notation | Name | Typisches Muster | Beispiel |
|---|---|---|---|
| **O(1)** | Konstant | Direktzugriff | Array-Index `A[i]` |
| **O(log n)** | Logarithmisch | Halbieren | Binäre Suche |
| **O(n)** | Linear | Einfache Schleife | Lineare Suche, `arrayMax` |
| **O(n log n)** | Linearithmisch | Divide & Conquer | Merge-Sort (spätere SW) |
| **O(n²)** | Quadratisch | Verschachtelte Schleifen | Selection-Sort, Insertion-Sort |
| **O(2ⁿ)** | Exponentiell | Brute-Force | Alle Teilmengen |
| **O(n!)** | Faktoriell | Alle Permutationen | Traveling Salesman |

### Wichtige Regel: Konstanten ignorieren

- `102n + 105` → **lineare** Funktion → O(n)
- `105n² + 108n` → **quadratische** Funktion → O(n²)

> Bei der O-Abschätzung dominiert immer die **höchste Potenz**, konstante Faktoren fallen weg.

---

## ⏱️ Zeitgrössen & Praxis-Beispiel

### Zweierpotenzen als Referenzgrössen

| Symbol | Wert | Ungefähr |
|---|---|---|
| **1K** | 2¹⁰ | 1'024 ≈ Tausend |
| **1M** | 2²⁰ | 1'048'576 ≈ Million |
| **1G** | 2³⁰ | ≈ Milliarde |
| **4G** | 2³² | ≈ 4 Milliarden |

### Kundensuche: Linear vs. Logarithmisch

| | Linear O(n) | Logarithmisch O(log n) |
|---|---|---|
| **1 Kunde** | 10 µs | 10 µs |
| **1 Mio. Kunden** | 10 s | ≈ 200 µs (≈ 20 × 10 µs) |
| **Speedup** | – | **50'000× schneller!** |

> 💡 Dies zeigt die enorme praktische Relevanz der Komplexitätsklasse!

---

## 🔄 Sortier-Algorithmen (SW01)

### Selection-Sort (Sortierung durch direktes Auswählen)

**Prinzip:**
1. Alle Elemente in eine unsortierte Sequenz einfügen → **O(n)**
2. Wiederholt das **kleinste Element** aus der unsortierten Sequenz suchen und entnehmen:
   - `n + (n-1) + (n-2) + ... + 2 + 1 = n(n+1)/2` → **O(n²)**

**Gesamtlaufzeit: O(n²)**

### Insertion-Sort (Sortierung durch direktes Einfügen)

**Prinzip:**
1. Elemente nacheinander in eine **sortierte Sequenz** einfügen (an richtiger Position):
   - `1 + 2 + ... + (n-1) + n = n(n+1)/2` → **O(n²)**
2. Sortierte Sequenz sequentiell entnehmen → **O(n)**

**Gesamtlaufzeit: O(n²)**

### In-Place Insertion-Sort (wichtig für Prüfung!)

**Prinzip:**
- Linker Teil = sortiert, rechter Teil = unsortiert
- Nächstes Element (`cur`) rechts nehmen
- Durch **move-Operationen** (Verschieben) Platz schaffen im sortierten Teil
- Erstes Element gilt bereits als "sortiert" (Länge 1)

```python
def insertion_sort(data):
    """Sortiert eine Liste mit dem In-Place Insertion-Sort Algorithmus."""
    for k in range(1, len(data)):   # Ab Index 1 (Index 0 = bereits "sortiert")
        cur = data[k]               # Aktuelles Element merken
        j = k
        while j > 0 and data[j - 1] > cur:  # Solange Vorgänger grösser
            data[j] = data[j - 1]   # Element nach rechts verschieben
            j -= 1
        data[j] = cur               # cur an richtige Position einfügen
```

### Laufzeitmessung (aus Übung – empirische Bestätigung O(n²))

| List-Size | Zeit (ms) | Ratio zur vorherigen |
|---|---|---|
| 512 | 3.7 | – |
| 1'024 | 16.3 | **4.4×** |
| 2'048 | 70.4 | **4.3×** |
| 4'096 | 280.9 | **4.0×** |
| 8'192 | 1133.7 | **4.0×** |

> 💡 **Ratio ≈ 4 bei Verdopplung → bestätigt O(n²)**, denn `(2n)² / n² = 4`

---

## 🔁 Rekursion

### Konzept

| | Iteration | Rekursion |
|---|---|---|
| **Prinzip** | Schleife (`for`, `while`) | Funktion ruft sich selbst auf |
| **Steuerung** | Schleifenbedingung | Base Case (Verankerung) |
| **Speicher** | Variablen | Call-Stack (pro Aufruf ein Frame) |

### Klassisches Beispiel: Fakultät (`n!`)

**Mathematische Definition:**
- `n! = 1 · 2 · 3 · ... · (n-1) · n`
- Rekursiv: `f(n) = n · f(n-1)` mit `f(0) = 1`

```python
def factorial(n):
    if n == 0:      # Base Case (Verankerung!)
        return 1
    else:
        return n * factorial(n - 1)  # Rekursiver Aufruf
```

**Ablauf für `factorial(5)`:**
```
factorial(5) = 5 * factorial(4)
             = 5 * 4 * factorial(3)
             = 5 * 4 * 3 * factorial(2)
             = 5 * 4 * 3 * 2 * factorial(1)
             = 5 * 4 * 3 * 2 * 1 * factorial(0)
             = 5 * 4 * 3 * 2 * 1 * 1
             = 120
```

### Übungs-Beispiel: Rekursive Summe (`0 + 1 + 2 + ... + n`)

```python
def recursive_sum(n):
    if n == 0:      # Base Case
        return 0
    else:
        return n + recursive_sum(n - 1)

# Verifikation: recursive_sum(100) = 5050
# Explizit:     n * (n + 1) // 2   = 5050  (Gausssche Summenformel)
```

---

## 📏 Präfix-Durchschnitte: O(n²) vs. O(n)

### Variante 1: Quadratisch – O(n²)

```python
def prefix_averages_quadratic(X):
    """Berechnet Präfix-Durchschnitte in O(n²)."""
    n = len(X)
    A = [0] * n
    for i in range(n):
        s = X[0]
        for j in range(1, i + 1):    # Innere Schleife: 1+2+...+(n-1) → O(n²)
            s += X[j]
        A[i] = s / (i + 1)
    return A
```

### Variante 2: Linear – O(n) (optimiert)

```python
def prefix_averages_linear(X):
    """Berechnet Präfix-Durchschnitte in O(n)."""
    n = len(X)
    A = [0] * n
    s = 0
    for i in range(n):
        s += X[i]               # Laufende Summe statt Neuberechnung!
        A[i] = s / (i + 1)
    return A
```

> 💡 **Verschachtelte Schleifen** → typisches Zeichen für **O(n²)**. Durch clever akkumulieren kann oft auf **O(n)** reduziert werden.

---

## 📝 Gausssche Summenformel (immer wieder relevant)

$$\sum_{i=1}^{n} i = 1 + 2 + 3 + \ldots + n = \frac{n \cdot (n+1)}{2}$$

**Anwendung in ADS:** Kommt immer vor bei verschachtelten Schleifen wo die innere Schleife von 1 bis `i` läuft:
- `1 + 2 + ... + (n-1)` = `n(n-1)/2` → O(n²)

---

## 🧮 Übungsaufgaben SW01 (Zusammenfassung)

| Aufgabe | Thema | Kernkonzept |
|---|---|---|
| **1** | Arithmetische Folgen | Rekursive, iterative & explizite Form bestimmen |
| **2** | Arithmetische Reihen | Summenformeln in rekursiver, iterativer & expliziter Form |
| **3** | Rekursive Summe | `recursive_sum(n)` implementieren (analog `factorial()`) |
| **4** | Insertion-Sort | In-Place implementieren & Laufzeitmessung beobachten |

### Aufgabe 1 – Arithmetische Folgen (Formel-Schema)

Für eine Folge mit Startwert `a₁` und Differenz `d`:

| Form | Formel |
|---|---|
| **Rekursiv** | `aₙ = aₙ₋₁ + d` mit `a₁` gegeben |
| **Iterativ** | `aₙ = a₁ + Σ d (n-1 mal)` |
| **Explizit** | `aₙ = a₁ + (n-1) · d` |

**Beispiel (b):** `5, 13, 21, 29, ...` → `a₁ = 5`, `d = 8` → `aₙ = 5 + (n-1)·8 = 8n - 3`

### Aufgabe 2 – Arithmetische Reihen

Allgemeine Summenformel: **`sₙ = n · (a₁ + aₙ) / 2`**

---

## ⚠️ Prüfungsrelevante Hinweise

1. **Open-Book:** Alle Unterlagen erlaubt, aber **keine elektronischen Hilfsmittel** → Zusammenfassungen auf Papier vorbereiten!
2. **Musteraufgaben:** Werden zur Verfügung gestellt
3. **Typische Prüfungsaufgaben SW01:**
   - Primitive Operationen zählen an einem gegebenen Pseudocode
   - O-Notation bestimmen / klassifizieren
   - Verschachtelte Schleifen analysieren
   - Rekursive Funktion schreiben / Ablauf nachvollziehen
   - Sortieralgorithmen (Selection-Sort, Insertion-Sort) erklären / anwenden
4. **Ratio-Trick:** Verdoppelt sich die Eingabe und vervierfacht sich die Zeit → **O(n²)**
5. **Gausssche Summenformel** auswendig kennen
6. **Verankerung bei Rekursion** nicht vergessen (häufiger Fehler!)

---

## 🗺️ Semester-Überblick (Kontext)

| SW | Thema |
|---|---|
| **01** | **Asymptotic Analysis, O-Notation, Rekursion** ← Du bist hier |
| 02 | Stack, Queues, Deques, Iteratoren |
| 03 | Allgemeine- und Binär-Bäume, Traversierungen |
| 04 | Priority-Queue, Heap |
| 05 | Set, Map, Hashtable |
| 06 | Binary-Search-Tree |
| 07 | AVL-Tree, Splay-Tree |
| 08 | Merge-Sort, Quick-Sort |
| 09 | Sorting Lower-Bound, Radix-Sort |
| 10 | Graphen: Grundlagen, Aufspannende Bäume (**Testat 1**) |
| 11 | Graph-Traversierungen, DFS, BFS |
| 12 | Digraphs, DAG, Topologische Sortierung (**Testat 2**) |
| 13 | Gewichtete Graphen, Shortest Path |
