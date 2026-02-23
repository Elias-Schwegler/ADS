# 📘 ADS – SW02: Lineare Datenstrukturen

> **Modul:** Algorithmen & Datenstrukturen (ADS) – FS26, HSLU ICS/AIML
> **Dozent:** Th. Letsch
> **Prüfungsformat:** Open-Book (beliebige Unterlagen erlaubt, **keine elektronischen Hilfsmittel**)
> **Testate:** Übungen 10 & 12 – mind. 1 von 2 muss bestanden sein

---

## 🎯 Lernziele SW02

1. **Array-basierte Listen** und **Linked-Lists** erklären und deren Vor-/Nachteile vergleichen.
2. **Abstrakte Datentypen (ADTs)** beschreiben – insbesondere **Stack**, **Queue** und **Deque**.
3. Eine **Deque** mit einer **doppelt-verketteten Liste** implementieren.
4. Einen **Stack** mit einer **einfach-verketteten Liste** implementieren.
5. Den **Iterator**-Mechanismus in Python und Java verstehen.
6. Die **Laufzeitkomplexität** von verschachtelten Schleifen analysieren.

---

## 📖 Wichtigste Begriffe

| Begriff | Definition |
|---|---|
| **Array-List** | Dynamisches Array – Elemente im zusammenhängenden Speicher, wahlfreier Zugriff O(1) |
| **Linked-List** | Verkettete Liste – Elemente als Knoten mit Zeigern verbunden, kein Index-Zugriff |
| **Singly-Linked-List** | Einfach-verkettete Liste – jeder Knoten hat `element` und `next` |
| **Doubly-Linked-List** | Doppelt-verkettete Liste – jeder Knoten hat `element`, `prev` und `next` |
| **Sentinel Node** | Dummy-Knoten (Header/Trailer) als Wächter am Anfang/Ende der Liste |
| **ADT (Abstrakter Datentyp)** | Abstraktion einer Datenstruktur: definiert **Attribute**, **Operationen** und **Fehlerbedingungen** |
| **Stack** | ADT mit **LIFO**-Prinzip (Last-In, First-Out) |
| **Queue** | ADT mit **FIFO**-Prinzip (First-In, First-Out) |
| **Deque** | Double-Ended Queue – Einfügen/Entfernen an **beiden** Enden möglich |
| **LIFO** | Last-In, First-Out – zuletzt eingefügtes Element wird zuerst entfernt |
| **FIFO** | First-In, First-Out – zuerst eingefügtes Element wird zuerst entfernt |
| **Iterator** | Objekt, das schrittweises Durchlaufen (Scannen/Iterieren) einer Sammlung abstrahiert |
| **Iterable** | Objekt, das einen Iterator erzeugen kann (`__iter__()`) |

---

## 📐 Konzepte & Theorie

### 1. Array-List (Dynamisches Array)

**Funktionsweise:**
- Elemente werden in einem **zusammenhängenden Speicherblock** gespeichert.
- Zugriff über **Index** → O(1).
- Wenn das Array voll ist, wird ein **neues, grösseres Array** alloziert und alle Elemente kopiert → **O(n)** für diesen Einzelfall.

```
Array-List (Kapazität 8):
┌───┬───┬───┬───┬───┬───┬───┬───┐
│ A │ B │ C │ D │ E │   │   │   │
└───┴───┴───┴───┴───┴───┴───┴───┘
  0   1   2   3   4   5   6   7
                        ↑
                    size = 5
```

**Vergrösserung (Resize):**
```
Altes Array (voll):     Neues Array (doppelte Grösse):
┌───┬───┬───┬───┐      ┌───┬───┬───┬───┬───┬───┬───┬───┐
│ A │ B │ C │ D │  →  │ A │ B │ C │ D │   │   │   │   │
└───┴───┴───┴───┘      └───┴───┴───┴───┴───┴───┴───┴───┘
  Alle kopieren: O(n)
```

**Python-Entsprechung:** `list` (built-in)
**Java-Entsprechung:** `java.util.ArrayList`

---

### 2. Singly-Linked-List (Einfach-verkettete Liste)

**Struktur:** Jeder Knoten speichert ein `element` und einen Zeiger `next` auf den nächsten Knoten.

```
head                                      tail
  ↓                                         ↓
┌─────────┐    ┌─────────┐    ┌─────────┐    
│ "BAL" │─→│ "JFK" │─→│ "SFO" │─→ None
└─────────┘    └─────────┘    └─────────┘
```

#### Operation: `addFirst(e)` – O(1)

```
Algorithmus:
1. Neuen Knoten erstellen mit Element e
2. next des neuen Knotens → aktueller head
3. head → neuer Knoten
4. size += 1
```

```
Vorher:  head → [A] → [B] → [C] → None
         neuer Knoten: [X]

Nachher: head → [X] → [A] → [B] → [C] → None
```

#### Operation: `addLast(e)` – O(1) (mit tail-Referenz)

```
Algorithmus:
1. Neuen Knoten erstellen mit Element e, next = None
2. tail.next → neuer Knoten
3. tail → neuer Knoten
4. size += 1
```

#### Operation: `removeFirst()` – O(1)

```
Algorithmus:
1. element = head.element
2. head → head.next
3. size -= 1
4. return element
```

> ⚠️ **Achtung:** `removeLast()` ist bei Singly-Linked-Lists **O(n)**, da der vorletzte Knoten gesucht werden muss!

---

### 3. Doubly-Linked-List (Doppelt-verkettete Liste)

**Struktur:** Jeder Knoten hat `element`, `prev` und `next`. Verwendet **Sentinel-Knoten** (Header und Trailer) als Wächter.

```
header                                              trailer
  ↓                                                    ↓
┌──────┐    ┌─────────┐    ┌─────────┐    ┌─────────┐    ┌──────┐
│ None │←→│ "BAL" │←→│ "JFK" │←→│ "SFO" │←→│ None │
└──────┘    └─────────┘    └─────────┘    └─────────┘    └──────┘
 Sentinel     1. Knoten     2. Knoten     3. Knoten     Sentinel
```

**Vorteile gegenüber Singly-Linked-List:**
- Bidirektionale Traversierung (vorwärts und rückwärts)
- **Alle Operationen am Anfang UND Ende in O(1)**
- Sentinel-Knoten vereinfachen Randfallbehandlung

**Nachteile:**
- Mehr Speicherverbrauch (zusätzlicher `prev`-Zeiger pro Knoten)

#### Operation: `addFirst(e)` mit Sentinels – O(1)

```
Algorithmus:
1. Neuen Knoten erstellen: prev = header, next = header.next
2. header.next.prev → neuer Knoten
3. header.next → neuer Knoten
4. size += 1
```

```
Vorher:  [header] ←→ [A] ←→ [B] ←→ [trailer]
Nachher: [header] ←→ [X] ←→ [A] ←→ [B] ←→ [trailer]
```

#### Operation: `addLast(e)` mit Sentinels – O(1)

```
Algorithmus:
1. Neuen Knoten erstellen: prev = trailer.prev, next = trailer
2. trailer.prev.next → neuer Knoten
3. trailer.prev → neuer Knoten
4. size += 1
```

---

### 4. Abstrakte Datentypen (ADTs)

> Ein **abstrakter Datentyp (ADT)** ist eine mögliche Abstraktion einer konkreten Datenstruktur. Ein ADT spezifiziert:
> - **Datenfelder / Attribute**
> - **Operationen / Methoden** auf und mit den Attributen
> - **Ausnahmen und Fehler** der Methoden

**Beispiel:** ADT-Modellierung eines Börsensystems:
- **Daten:** Kauf/Verkauf-Aufträge
- **Operationen:** `buy(stock, shares, price)`, `sell(stock, shares, price)`, `cancel(order)`
- **Error Conditions:** Kaufen/Verkaufen nicht-existierender Aktien, Cancel nicht-existierender Aufträge

---

### 5. Stack (Stapel) – LIFO

> **Prinzip:** Last-In, First-Out – Das zuletzt eingefügte Element wird zuerst entfernt.

```
         ┌─────┐
  push → │  E  │ ← pop / top
         ├─────┤
         │  D  │
         ├─────┤
         │  C  │
         ├─────┤
         │  B  │
         ├─────┤
         │  A  │
         └─────┘
```

#### Stack ADT – Operationen

| Operation | Beschreibung | Rückgabe |
|---|---|---|
| `push(e)` | Element `e` oben auf den Stack legen | – |
| `pop()` | Oberstes Element entfernen und zurückgeben | Element |
| `top()` | Oberstes Element ansehen (ohne Entfernen) | Element |
| `size()` | Anzahl Elemente im Stack | Integer |
| `is_empty()` | Prüfen ob Stack leer ist | Boolean |

> **Randbedingung:** `pop()` und `top()` auf leerem Stack → Exception oder `None`

#### Stack-Beispiel (Schritt-für-Schritt)

| Operation | Ausgabe | Stack (top → bottom) |
|---|---|---|
| `push(5)` | – | (5) |
| `push(3)` | – | (3, 5) |
| `pop()` | 3 | (5) |
| `push(7)` | – | (7, 5) |
| `pop()` | 7 | (5) |
| `top()` | 5 | (5) |
| `pop()` | 5 | () |
| `pop()` | *EmptyStackException* | () |
| `push(9)` | – | (9) |
| `push(7)` | – | (7, 9) |
| `push(3)` | – | (3, 7, 9) |
| `push(5)` | – | (5, 3, 7, 9) |
| `size()` | 4 | (5, 3, 7, 9) |
| `pop()` | 5 | (3, 7, 9) |

#### Anwendungen von Stacks

- **Direkte Applikationen:**
  - Browserverlauf (Zurück-Button)
  - Undo-Mechanismus in Editoren
  - Kette von Methodenaufrufen (Call-Stack) in der JVM / Python-Interpreter
- **Indirekte Applikationen:**
  - Hilfskonstrukte für andere Algorithmen (z.B. Klammerprüfung)
  - Komponenten für andere Datenstrukturen

#### Array-basierter Stack

Bei der Implementierung mit einem Array:
- Stack-Pointer `t` zeigt auf den Index des obersten Elements
- **Performance:** O(n) Speicher, jede Operation O(1)
- **Limitation:** Maximale Grösse ist bei Konstruktion festgelegt

```
Algorithm push(o):
    if t = S.length - 1 then
        throw IllegalStateException
    else
        t ← t + 1
        S[t] ← o

Algorithm pop():
    if isEmpty() then
        throw EmptyStackException
    else
        e ← S[t]
        S[t] ← None
        t ← t - 1
        return e
```

---

### 6. Queue (Warteschlange) – FIFO

> **Prinzip:** First-In, First-Out – Das zuerst eingefügte Element wird zuerst entfernt.

```
Enqueue →  ┌───┬───┬───┬───┬───┐  → Dequeue
           │ E │ D │ C │ B │ A │
           └───┴───┴───┴───┴───┘
           Ende                Anfang
```

#### Queue ADT – Operationen

| Operation | Beschreibung | Rückgabe |
|---|---|---|
| `enqueue(e)` | Element `e` am **Ende** der Queue einfügen | – |
| `dequeue()` | Element vom **Anfang** entfernen und zurückgeben | Element |
| `first()` | Erstes Element ansehen (ohne Entfernen) | Element |
| `size()` | Anzahl Elemente in der Queue | Integer |
| `is_empty()` | Prüfen ob Queue leer ist | Boolean |

> **Randbedingung:** `dequeue()` und `first()` auf leerer Queue → `null` / `None`

#### Queue-Beispiel (Schritt-für-Schritt)

| Operation | Ausgabe | Queue (front → rear) |
|---|---|---|
| `enqueue(5)` | – | (5) |
| `enqueue(3)` | – | (5, 3) |
| `dequeue()` | 5 | (3) |
| `enqueue(7)` | – | (3, 7) |
| `dequeue()` | 3 | (7) |
| `first()` | 7 | (7) |
| `dequeue()` | 7 | () |
| `dequeue()` | *null* | () |
| `isEmpty()` | *true* | () |
| `enqueue(9)` | – | (9) |
| `enqueue(7)` | – | (9, 7) |
| `size()` | 2 | (9, 7) |
| `enqueue(3)` | – | (9, 7, 3) |
| `enqueue(5)` | – | (9, 7, 3, 5) |
| `dequeue()` | 9 | (7, 3, 5) |

#### Anwendungen von Queues

- **Direkte Applikationen:**
  - Wartelisten (Schalter, Zoll, Skilift) → *First come, first served*
  - Zugriff auf gemeinsame Ressourcen (z.B. Printer-Queue)
  - Multiprogramming, Multithreading
- **Indirekte Applikationen:**
  - Hilfskonstrukte für andere Algorithmen (z.B. BFS)
  - Komponenten für andere Datenstrukturen

---

### 7. Deque (Double-Ended Queue)

> **Prinzip:** Einfügen und Entfernen an **beiden** Enden möglich. Der Name leitet sich ab von: *Double-Ended-Queue → DeQueue → Deque*.

```
addFirst / removeFirst →  ┌───┬───┬───┬───┬───┐  ← addLast / removeLast
                          │ A │ B │ C │ D │ E │
                          └───┴───┴───┴───┴───┘
                         Front                Rear
```

#### Deque ADT – Operationen

| Operation | Beschreibung | Rückgabe |
|---|---|---|
| `addFirst(e)` | Element am **Anfang** einfügen | – |
| `addLast(e)` | Element am **Ende** einfügen | – |
| `removeFirst()` | Erstes Element entfernen und zurückgeben | Element |
| `removeLast()` | Letztes Element entfernen und zurückgeben | Element |
| `first()` | Erstes Element ansehen (ohne Entfernen) | Element |
| `last()` | Letztes Element ansehen (ohne Entfernen) | Element |
| `size()` | Anzahl Elemente | Integer |
| `is_empty()` | Prüfen ob Deque leer ist | Boolean |

> **Randbedingung:** Auslesen eines Elements aus einer leeren Deque → `null` / `None`

> 💡 **Wichtig:** Ein Deque kann sowohl als **Stack** als auch als **Queue** verwendet werden!

---

### 8. Iteratoren

> Ein **Iterator** abstrahiert den Prozess des schrittweisen Scannens/Iterierens über eine Sammlung von Elementen.

#### Python Iterator

```python
# Erzeugung
my_iterator = iter(iterable)
# oder:
my_iterator = iterable.__iter__()

# Benutzung
next_element = next(my_iterator)
# oder:
next_element = my_iterator.__next__()

# Ende der Iteration
# → raise StopIteration
```

#### Java Iterator

```java
// Erzeugung
Iterator<Type> myIterator = iterable.iterator();

// Benutzung
if (myIterator.hasNext()) {
    Type nextElement = myIterator.next();
}

// Ende der Iteration
// myIterator.hasNext() == false
// bzw. throw new NoSuchElementException
```

#### Modifikation während Iteration

| Sprache | Modifikation erlaubt? |
|---|---|
| **Python** | **Ja** (aber nicht empfohlen) |
| **Java** | **Nein** → `ConcurrentModificationException` |

---

## 📊 Klassifizierungen / Vergleiche

### Array-List vs. Linked-List

| Kriterium | Array-List | Singly-Linked-List | Doubly-Linked-List |
|---|---|---|---|
| **Zugriff per Index** | **O(1)** | O(n) | O(n) |
| **addFirst** | O(n) | **O(1)** | **O(1)** |
| **addLast** | O(1) amortisiert | **O(1)** (mit tail) | **O(1)** |
| **removeFirst** | O(n) | **O(1)** | **O(1)** |
| **removeLast** | O(1) | **O(n)** | **O(1)** |
| **Einfügen/Löschen Mitte** | O(n) | O(n) | O(n) (O(1) mit Referenz) |
| **Speicher** | Kompakt, zusammenhängend | Extra Speicher für `next` | Extra für `prev` + `next` |
| **Cache-Freundlichkeit** | **Sehr gut** | Schlecht | Schlecht |

### Vergleich der ADTs: Stack vs. Queue vs. Deque

| Eigenschaft | Stack | Queue | Deque |
|---|---|---|---|
| **Prinzip** | LIFO | FIFO | Beides möglich |
| **Einfügen** | oben (`push`) | hinten (`enqueue`) | vorne **oder** hinten |
| **Entfernen** | oben (`pop`) | vorne (`dequeue`) | vorne **oder** hinten |
| **Kann als Stack dienen?** | ✅ | ❌ | ✅ |
| **Kann als Queue dienen?** | ❌ | ✅ | ✅ |
| **Typische Implementierung** | Array / Linked-List | Array / Linked-List | Doubly-Linked-List |

### Python- und Java-Entsprechungen

| Datenstruktur | Java | Python |
|---|---|---|
| **Array-List** | `java.util.ArrayList` | `list` |
| **Linked-List** | `java.util.LinkedList` | `collections.deque` (Zugriff nur Anfang/Ende) |

---

## ⏱️ Komplexitätsanalyse

### Alle Operationen im Überblick

| Operation | Array-basiert | Singly-Linked | Doubly-Linked (mit Sentinels) |
|---|---|---|---|
| `addFirst(e)` | O(n) | **O(1)** | **O(1)** |
| `addLast(e)` | O(1)* | **O(1)** | **O(1)** |
| `removeFirst()` | O(n) | **O(1)** | **O(1)** |
| `removeLast()` | O(1) | O(n) | **O(1)** |
| `get(i)` / Index | **O(1)** | O(n) | O(n) |
| `size()` | **O(1)** | **O(1)** | **O(1)** |
| `isEmpty()` | **O(1)** | **O(1)** | **O(1)** |
| `first()` / `top()` | **O(1)** | **O(1)** | **O(1)** |
| `last()` | **O(1)** | **O(1)** | **O(1)** |

*\* O(1) amortisiert – gelegentlich O(n) beim Resize*

### Stack (Linked-List-basiert)

| Operation | Zeitkomplexität | Platzkomplexität |
|---|---|---|
| `push(e)` | **O(1)** | O(1) |
| `pop()` | **O(1)** | O(1) |
| `top()` | **O(1)** | O(1) |
| `size()` | **O(1)** | O(1) |
| `is_empty()` | **O(1)** | O(1) |
| **Gesamt (n Elemente)** | – | **O(n)** |

### Array-basierter Stack – Performance

- Falls sich **n** Elemente im Stack befinden → **O(n)** Speicher
- Jede Operation benötigt **O(1)** Laufzeit
- **Limitation:** Maximale Grösse wird bei Konstruktion festgelegt (voll → `IllegalStateException`)

---

### Laufzeitanalyse verschachtelter Schleifen (Übung 1)

Aus der Übung – Analyse des Codes:

```python
for i in range(n):          # n Durchläufe
    for j in range(i):      # 0, 1, 2, ..., n-1 Durchläufe
        # Operation         # → 0 + 1 + 2 + ... + (n-1)
```

**Anwendung der Gaussschen Summenformel:**

$$\sum_{i=0}^{n-1} i = 0 + 1 + 2 + \ldots + (n-1) = \frac{n \cdot (n-1)}{2}$$

→ **O(n²)**

**Ratio-Trick zur empirischen Verifikation:**

| Eingabegrösse `n` | Laufzeit | Ratio (zur vorherigen) |
|---|---|---|
| 1'000 | t₁ | – |
| 2'000 | t₂ | t₂/t₁ ≈ **4** |
| 4'000 | t₃ | t₃/t₂ ≈ **4** |

> 💡 **Ratio ≈ 4 bei Verdopplung → bestätigt O(n²)**, denn `(2n)² / n² = 4`

---

## 💻 Wichtigste Code-Beispiele

### 1. Node-Klasse (Doubly-Linked-List)

> Grundbaustein für die Deque- und Stack-Implementierung mit doppelt-verketteter Liste.

```python
class Node:
    """Knoten einer doppelt-verketteten Liste."""

    def __init__(self, element, prev=None, next_node=None):
        self._element = element   # Gespeichertes Element
        self._prev = prev         # Zeiger auf vorherigen Knoten
        self._next = next_node    # Zeiger auf nächsten Knoten

    @property
    def element(self):
        return self._element

    @element.setter
    def element(self, value):
        self._element = value

    @property
    def prev(self):
        return self._prev

    @prev.setter
    def prev(self, value):
        self._prev = value

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, value):
        self._next = value
```

---

### 2. Deque-Implementierung (Doubly-Linked-List mit Sentinels) – ML

> Verwendet **Sentinel-Knoten** (`_header` und `_trailer`) für vereinfachte Randfallbehandlung. Alle Einfüge-/Entfern-Operationen in **O(1)**.

```python
class DequeEmptyException(Exception):
    """Exception für leere Deque."""
    def __init__(self, message="Deque is empty"):
        super().__init__(message)


class Dequeue:
    """Deque-Implementierung mit doppelt-verketteter Liste und Sentinel-Knoten."""

    def __init__(self):
        # Sentinel-Knoten erstellen (speichern keine echten Daten)
        self._header = Node(None, None, None)
        self._trailer = Node(None, self._header, None)
        self._header.next = self._trailer   # header → trailer verknüpfen
        self._size = 0

    def insert_first(self, element):
        """Element am Anfang der Deque einfügen – O(1)."""
        new_node = Node(element, self._header, self._header.next)
        self._header.next.prev = new_node   # Bisheriger erster Knoten zeigt zurück
        self._header.next = new_node        # Header zeigt auf neuen Knoten
        self._size += 1

    def insert_last(self, element):
        """Element am Ende der Deque einfügen – O(1)."""
        new_node = Node(element, self._trailer.prev, self._trailer)
        self._trailer.prev.next = new_node  # Bisheriger letzter Knoten zeigt vorwärts
        self._trailer.prev = new_node       # Trailer zeigt auf neuen Knoten
        self._size += 1

    def remove_first(self):
        """Erstes Element entfernen und zurückgeben – O(1)."""
        if self.is_empty():
            raise DequeEmptyException()
        node = self._header.next           # Erster echter Knoten
        element = node.element
        self._header.next = node.next      # Header überspringt den Knoten
        node.next.prev = self._header      # Nachfolger zeigt zurück auf Header
        self._size -= 1
        return element

    def remove_last(self):
        """Letztes Element entfernen und zurückgeben – O(1)."""
        if self.is_empty():
            raise DequeEmptyException()
        node = self._trailer.prev          # Letzter echter Knoten
        element = node.element
        self._trailer.prev = node.prev     # Trailer überspringt den Knoten
        node.prev.next = self._trailer     # Vorgänger zeigt vorwärts auf Trailer
        self._size -= 1
        return element

    def first(self):
        """Erstes Element zurückgeben (ohne Entfernen) – O(1)."""
        if self.is_empty():
            raise DequeEmptyException()
        return self._header.next.element

    def last(self):
        """Letztes Element zurückgeben (ohne Entfernen) – O(1)."""
        if self.is_empty():
            raise DequeEmptyException()
        return self._trailer.prev.element

    def size(self):
        """Anzahl Elemente – O(1)."""
        return self._size

    def is_empty(self):
        """Prüft ob Deque leer ist – O(1)."""
        return self._size == 0

    def __str__(self):
        """String-Darstellung der Deque."""
        result = []
        current = self._header.next
        while current != self._trailer:
            result.append(str(current.element))
            current = current.next
        return "[" + ", ".join(result) + "]"
```

#### Beispiel-Nutzung:

```python
d = Dequeue()
d.insert_first(3)     # Deque: [3]
d.insert_first(5)     # Deque: [5, 3]
d.insert_last(7)      # Deque: [5, 3, 7]
print(d.first())      # → 5
print(d.last())       # → 7
print(d.remove_first())  # → 5,  Deque: [3, 7]
print(d.remove_last())   # → 7,  Deque: [3]
print(d.size())          # → 1
```

#### Visualisierung: `insert_first(X)` mit Sentinel-Knoten

```
Vorher:
  [header] ←→ [A] ←→ [B] ←→ [trailer]

Schritt 1: Neuen Knoten erstellen
  new_node = Node(X, header, header.next=A)

Schritt 2: A.prev → new_node
  [header] ←→ [X] ← [A] ←→ [B] ←→ [trailer]
                ↓→ [A]

Schritt 3: header.next → new_node
  [header] ←→ [X] ←→ [A] ←→ [B] ←→ [trailer]

Nachher:
  [header] ←→ [X] ←→ [A] ←→ [B] ←→ [trailer]
```

---

### 3. Stack-Implementierung (Singly-Linked-List) – ML

> Verwendet eine **einfach-verkettete Liste** mit internem `_Node`-Klasse. `push` und `pop` operieren am **Kopf** der Liste → immer O(1).

```python
class EmptyStackException(Exception):
    """Exception für leeren Stack."""
    def __init__(self, message="Stack is empty"):
        super().__init__(message)


class StackImplementation:
    """Stack-Implementierung mit einfach-verketteter Liste (LIFO)."""

    class _Node:
        """Interner Knoten (lightweight)."""
        def __init__(self, element, next_node=None):
            self._element = element
            self._next = next_node

    def __init__(self):
        self._top = None    # Zeiger auf oberstes Element
        self._size = 0

    def push(self, element):
        """Element oben auf den Stack legen – O(1)."""
        # Neuer Knoten zeigt auf bisheriges Top
        self._top = self._Node(element, self._top)
        self._size += 1

    def pop(self):
        """Oberstes Element entfernen und zurückgeben – O(1)."""
        if self.is_empty():
            raise EmptyStackException()
        element = self._top._element
        self._top = self._top._next   # Top wandert zum nächsten Knoten
        self._size -= 1
        return element

    def top(self):
        """Oberstes Element ansehen (ohne Entfernen) – O(1)."""
        if self.is_empty():
            raise EmptyStackException()
        return self._top._element

    def size(self):
        """Anzahl Elemente im Stack – O(1)."""
        return self._size

    def is_empty(self):
        """Prüft ob Stack leer ist – O(1)."""
        return self._size == 0

    def __str__(self):
        """String-Darstellung (Top → Bottom)."""
        result = []
        current = self._top
        while current is not None:
            result.append(str(current._element))
            current = current._next
        return "[" + ", ".join(result) + "]"
```

#### Beispiel-Nutzung:

```python
s = StackImplementation()
s.push(5)             # Stack: [5]
s.push(3)             # Stack: [3, 5]
s.push(7)             # Stack: [7, 3, 5]
print(s.top())        # → 7
print(s.pop())        # → 7,  Stack: [3, 5]
print(s.size())       # → 2
print(s.pop())        # → 3,  Stack: [5]
print(s.pop())        # → 5,  Stack: []
print(s.is_empty())   # → True
```

#### Visualisierung: `push(X)` auf Singly-Linked-List

```
Vorher:
  top → [C] → [B] → [A] → None

push(X):
  new_node = _Node(X, next=top)    # Neuer Knoten zeigt auf altes Top
  top → new_node                   # Top wird aktualisiert

Nachher:
  top → [X] → [C] → [B] → [A] → None
```

---

## 📝 Übungsaufgaben-Zusammenfassung

| Aufgabe | Thema | Kernkonzept |
|---|---|---|
| **1** | Laufzeitanalyse (verschachtelte Schleifen) | Gausssche Summenformel → O(n²), Ratio-Trick bestätigt empirisch |
| **2** | Deque-Implementierung | Doppelt-verkettete Liste mit Sentinel-Knoten, alle Ops O(1) |
| **3** | Stack-Implementierung | Einfach-verkettete Liste, Push/Pop am Kopf, LIFO-Prinzip |

### Aufgabe 1 – Laufzeitanalyse (Detail)

**Gegebener Code:**
```python
for i in range(n):
    for j in range(i):
        # primitive Operation
```

**Analyse:**
- Äussere Schleife: `i` geht von `0` bis `n-1`
- Innere Schleife: `j` geht von `0` bis `i-1` → `i` Durchläufe
- Total innere Operationen: `0 + 1 + 2 + ... + (n-1) = n(n-1)/2`

**Erwartete Komplexität:** O(n²)

**Empirische Verifikation mit Ratio-Trick:**
- Bei **Verdopplung** der Eingabe verdoppelt sich die Zeit um Faktor **≈ 4**
- Dies bestätigt O(n²), da `(2n)²/n² = 4`

### Aufgabe 2 – Deque (Detail)

- Implementierung einer Deque mit **doppelt-verketteter Liste**
- **Sentinel-Knoten** (Header und Trailer) als Wächter → vereinfacht Code
- Methoden: `insert_first`, `insert_last`, `remove_first`, `remove_last`, `first`, `last`, `size`, `is_empty`
- Eigene Exception-Klasse: `DequeEmptyException`

### Aufgabe 3 – Stack (Detail)

- Implementierung eines Stacks mit **einfach-verketteter Liste**
- Interne `_Node`-Klasse (lightweight, keine Properties nötig)
- `push` und `pop` am **Kopf** der Liste → O(1)
- Eigene Exception-Klasse: `EmptyStackException`

---

## ⚠️ Prüfungsrelevante Hinweise

### Typische Aufgabentypen

1. **Ablauf-Tabelle erstellen:** Gegebene Sequenz von Stack/Queue/Deque-Operationen → Zustand nach jeder Operation angeben
2. **Implementierung erklären:** Wie funktioniert `insert_first` / `push` auf einer verketteten Liste?
3. **Komplexität angeben:** Laufzeit von Operationen auf verschiedenen Datenstrukturen
4. **Vergleichstabelle erstellen:** Array-List vs. Linked-List – wann welche verwenden?
5. **Laufzeitanalyse:** Verschachtelte Schleifen analysieren mit Gaussscher Summenformel
6. **ADT vs. Implementierung:** Unterschied erklären

### Häufige Fehlerquellen

| Fehler | Korrekte Lösung |
|---|---|
| `removeLast` auf Singly-Linked-List als O(1) angeben | Ist **O(n)** – Vorgänger muss gesucht werden! |
| Sentinel-Knoten als echte Daten-Knoten zählen | Sentinels speichern **keine Daten**, sie vereinfachen den Code |
| Stack und Queue verwechseln | Stack = **LIFO** (Teller-Stapel), Queue = **FIFO** (Warteschlange) |
| `resize` bei Array-List vergessen | Array-List muss bei vollem Array kopieren → einzelne Operation O(n), amortisiert O(1) |
| Iterator-Modifikation in Java | Java erlaubt **keine** Modifikation → `ConcurrentModificationException` |

### Tricks und Merkregeln

> 🧠 **Stack = Teller-Stapel:** Der letzte Teller, den man drauflegt, nimmt man als erstes wieder weg → **LIFO**

> 🧠 **Queue = Warteschlange am Schalter:** Wer zuerst kommt, wird zuerst bedient → **FIFO**

> 🧠 **Deque = Türsteher an beiden Enden:** Links rein/raus UND rechts rein/raus möglich

> 🧠 **Sentinel-Trick:** Header und Trailer als Dummy-Knoten → `addFirst` und `addLast` brauchen **keine Sonderfallbehandlung** für leere Listen!

> 🧠 **Ratio-Trick (aus SW01):**
> - Verdopplung n → Laufzeit × 2 → **O(n)** (linear)
> - Verdopplung n → Laufzeit × 4 → **O(n²)** (quadratisch)
> - Verdopplung n → Laufzeit × 8 → **O(n³)** (kubisch)

> 🧠 **Gausssche Summenformel:** `1 + 2 + ... + n = n(n+1)/2` → Immer wenn innere Schleife von 0/1 bis `i` läuft → **O(n²)**

---

## 🔗 Verbindung zu vorherigen Wochen

### Aufbau auf SW01

| SW01 Konzept | SW02 Anwendung |
|---|---|
| **O-Notation** | Alle Operationen der neuen Datenstrukturen mit O-Notation klassifiziert |
| **Gausssche Summenformel** | Übung 1: Laufzeitanalyse verschachtelter Schleifen → O(n²) |
| **Ratio-Trick** | Empirische Verifikation der theoretischen Laufzeitanalyse |
| **Primitive Operationen zählen** | Zeiger-Operationen in Linked-Lists zählen (z.B. addFirst = 4 Ops) |
| **Sortier-Algorithmen** | Selection-Sort/Insertion-Sort nutzen intern Arrays – jetzt verstehen wir auch alternative Datenstrukturen (Linked-Lists) |

### Vorschau auf kommende Wochen

| SW | Thema | Bezug zu SW02 |
|---|---|---|
| **03** | Bäume, Traversierungen | Bäume basieren auf verketteten Knoten (ähnlich Linked-List) |
| **04** | Priority-Queue, Heap | Queue-Erweiterung mit Prioritäten |
| **05** | Set, Map, Hashtable | Verwendet Array-Listen und verkettete Listen intern |

---

## 🗺️ Semester-Überblick (Kontext)

| SW | Thema |
|---|---|
| 01 | Asymptotic Analysis, O-Notation, Rekursion |
| **02** | **Stack, Queues, Deques, Iteratoren** ← Du bist hier |
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
