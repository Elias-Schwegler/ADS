# 📘 ADS – SW03: Allgemeine- und Binärbäume, Speicherverfahren, Baumtraversierungen

> **Modul:** Algorithmen & Datenstrukturen (ADS) – FS26, HSLU ICS/AIML
> **Dozent:** Th. Letsch
> **Woche:** SW03 – 02.03.2026
> **Thema:** Allgemeine- und Binär-Bäume, Speicherverfahren für Bäume, Baumtraversierungen
> **Prüfungsformat:** Open-Book (beliebige Unterlagen erlaubt, **keine elektronischen Hilfsmittel**)
> **Testate:** Übungen 10 & 12 – mind. 1 von 2 muss bestanden sein

---

## 🎯 Lernziele SW03

1. Sie **verstehen wie Bäume aufgebaut** sind.
2. Sie **wissen wie Bäume gespeichert** werden (verlinkt und Array-basiert).
3. Sie können folgende **Traversierungen anwenden**:
   - **Preorder**
   - **Postorder**
   - **Breadth-First**
   - **Inorder** (nur für Binärbäume)
4. Sie können einen **Array-basierten Baum implementieren** (`VectorTree`).

---

## 📖 Wichtigste Begriffe

| Begriff | Definition |
|---|---|
| **Baum (Tree)** | Abstrakte, hierarchische Datenstruktur aus Knoten in Eltern-Kind-Relation |
| **Wurzel (Root)** | Knoten ohne Elternknoten – oberster Knoten des Baums |
| **Interner Knoten** | Knoten mit mindestens einem Kind (z.B. A, B, C, F) |
| **Externer Knoten (Blatt)** | Knoten ohne Kinder (z.B. E, I, J, K, G, H, D) |
| **Tiefe (Depth)** | Anzahl Vorgänger eines Knotens (= Anzahl Kanten zur Wurzel) |
| **Höhe (Height)** | Maximale Tiefe des Teilbaums mit Wurzel v; Blatt: 0, Interner Knoten: 1 + max(Höhe der Kinder) |
| **Subtree (Unterbaum)** | Baum bestehend aus einem Knoten und allen seinen Nachfolgern |
| **Sibling** | Zwillingsknoten – Knoten mit demselben Elternknoten |
| **Vorgänger (Ancestor)** | Eltern, Grosseltern, etc. eines Knotens |
| **Nachfolger (Descendant)** | Kind, Grosskind, etc. eines Knotens |
| **Binärer Baum** | Baum, bei dem jeder interne Knoten höchstens zwei Kinder hat (links, rechts) |
| **Echter Binärbaum** | Binärer Baum, bei dem jeder interne Knoten **exakt** zwei Kinder hat |
| **Kante (Edge)** | Verbindung zwischen Eltern- und Kindknoten |
| **Position** | Abstraktion für Knoten im Tree ADT |
| **Rank** | Index-Position eines Knotens bei Array-basierter Speicherung |
| **Traversierung** | Systematisches Besuchen aller Knoten eines Baums |

---

## 📐 Konzepte & Theorie

### 1. Was ist ein (Informations-) Baum?

Bäume repräsentieren in der Informatik **abstrakte, hierarchische Strukturen**. Ein Baum besteht aus **Knoten**, welche in **Eltern-Kind-Relation** stehen.

**Anwendungen:**
- **Organigramm** (Unternehmensstruktur)
- **Dateisystem** (Ordner → Unterordner → Dateien)
- **Programmierungsumgebungen** (DOM, AST)
- **Arithmetische Ausdrücke** (Syntaxbäume)

```
Beispiel: Dateisystem als Baum

              Computer
            /    |     \
          C:\   D:\   F:\Backup
         / \     |
    Windows Users A&D   CompB
            / | \
       nicole britta jens
```

---

### 2. Baum-Terminologie

```
                    A           ← Wurzel (Root), Tiefe 0, Höhe 3
                 /  |  \
               B    C    D      ← Tiefe 1
             /  \    |
            E    F   G   H     ← Tiefe 2
                /|\
               I J K           ← Tiefe 3 (Blätter)
```

| Eigenschaft | Beschreibung | Beispiel (obiger Baum) |
|---|---|---|
| **Wurzel** | Kein Elternknoten | A |
| **Interne Knoten** | Min. 1 Kind | A, B, C, F |
| **Externe Knoten (Blätter)** | Keine Kinder | E, I, J, K, G, H, D |
| **Siblings** | Gleicher Elternknoten | {B, C, D} sind Siblings |
| **Tiefe von F** | Anzahl Vorgänger | 2 (A → B → F) |
| **Höhe von F** | 1 + max(Höhe Kinder) | 1 + max(0,0,0) = 1 |
| **Höhe des Baums** | Höhe der Wurzel | 3 |

> 💡 **Merke:** Die **Höhe** gibt die **Anzahl Ebenen** des Baumes an.

---

### 3. Tiefe – Definition und Algorithmus

> **Tiefe von v** = Anzahl Vorgänger von v (ohne v selbst!) = Anzahl Kanten auf dem Pfad von der Wurzel zum Knoten v.

**Rekursive Definition:**
- Falls v die Wurzel ist → `depth(v) = 0`
- Sonst → `depth(v) = 1 + depth(parent(v))`

```
Beispiel: Inhaltsverzeichnis als Baum

        Concurrency       Tiefe: 0
        /         \
  1. Motivations  2. Methods   References    Tiefe: 1
    /    \        /    |    \
1.1 Shared 1.2 Coop  2.1  2.2  2.3 Agents   Tiefe: 2
```

**Pseudocode:**
```
Algorithm depth(T, v):
    if v is the root of T then
        return 0
    else
        return 1 + depth(T, v.parent())
```

**Laufzeit:** O(d_v) wobei d_v die Tiefe von v ist. Im Worst Case O(n) bei einem entarteten Baum (Kette).

---

### 4. Höhe – Definition und Algorithmus

> **Höhe von v** = Höhe des Teilbaumes mit Wurzel v

**Rekursive Definition:**
- **Externer Knoten (Blatt):** `height(v) = 0`
- **Interner Knoten:** `height(v) = 1 + max(height(w))` für alle Kinder w von v

```
Beispiel: Fahrzeug-Hierarchie

  Tiefe: 0    Fahrzeug          Höhe: 3
              /       \
  Tiefe: 1  Nutzfahrzeug  Spassfahrzeug    Höhe: 2
            / \         / |  \
  Tiefe: 2 Lastwagen Bus Combi Cabrio ..  Höhe: 1
                              / \
  Tiefe: 3                 rot  weiss     Höhe: 0
```

**Pseudocode:**
```
Algorithm height(T, v):
    h = 0
    for all children w of v:
        h = max(h, 1 + height(T, w))
    return h
```

**Laufzeit:** O(n) – jeder Knoten wird genau einmal besucht.

---

### 5. Tree ADT (Abstrakter Datentyp)

Die **Position** dient im Tree ADT als Abstraktion für **Knoten**.

**Zugriff auf das Element:** `Element Position.getElement()`

| Kategorie | Methode | Beschreibung |
|---|---|---|
| **Zugriff** | `root()` | Position der Wurzel zurückgeben |
| **Zugriff** | `parent(p)` | Position des Elternknotens von p |
| **Zugriff** | `children(p)` | Liste der Kindpositionen von p |
| **Zugriff** | `numChildren(p)` | Anzahl Kinder von p |
| **Abfrage** | `isInternal(p)` | Hat p mindestens ein Kind? |
| **Abfrage** | `isExternal(p)` | Hat p keine Kinder? (= Blatt) |
| **Abfrage** | `isRoot(p)` | Ist p die Wurzel? |
| **Hilfs** | `size()` | Gesamtanzahl Knoten |
| **Hilfs** | `isEmpty()` | Ist der Baum leer? |
| **Hilfs** | `iterator()` | Iterator über alle Elemente |

---

### 6. Binäre Bäume

> Ein **binärer Baum** ist ein Baum mit folgenden Eigenschaften:
> 1. Jeder interne Knoten besitzt **höchstens zwei** Kinder (**exakt** zwei bei *echten Binärbäumen*).
> 2. Die Kinder eines Knotens sind ein **geordnetes Paar** (links, rechts).

**Alternative rekursive Definition:**
Ein binärer Baum ist entweder:
- ein Baum bestehend aus keinem oder einem einzelnen Knoten, **oder**
- ein Baum, dessen Wurzel ein geordnetes Paar Kinder besitzt, welche selber wieder binäre Bäume sind.

```
Beispiel: Binärer Baum

          A
         / \
        B    C
       / \     \
      D   E     F
             \
              I
```

**Anwendungen binärer Bäume:**
- Arithmetische Ausdrücke (Syntaxbäume)
- Entscheidungsprozesse (ja/nein)
- Suchen (Binary Search Tree – kommt in SW06)

---

### 7. Binärbaum ADT

Der **BinaryTree ADT** erweitert den Tree ADT, d.h. er **erbt alle Methoden** des Tree ADT.

**Zusätzliche Methoden:**

| Methode | Beschreibung |
|---|---|
| `left(p)` | Position des linken Kindes von p |
| `right(p)` | Position des rechten Kindes von p |
| `sibling(p)` | Position des Geschwisterknotens von p |

---

### 8. Speicherverfahren für Bäume

#### 8.1 Verlinkte Baum-Knoten (allgemeiner Baum)

Ein Baumknoten wird repräsentiert durch ein **Objekt** mit:
- **Element** (gespeicherter Wert)
- **Elternknoten** (Referenz auf Parent)
- **Sequence mit Kindknoten** (z.B. verkettete Liste der Kinder)

```
Knoten-Struktur (allgemeiner Baum):
┌──────────────┬──────────────┬──────────────┐
│ Ref Element  │  Ref Parent  │ Ref Children │
└──────┬───────┴──────┬───────┴──────┬───────┘
       ↓              ↓              ↓
    Element       Elternknoten    [X]→[Y]→[Z]
                                  (Kinderliste)
```

#### 8.2 Verlinkte Baum-Knoten (Binärbaum)

Bei Binärbäumen kann man auf die Sequence **verzichten** und direkt Referenzen speichern:
- **Element**
- **Eltern Knoten** (Referenz)
- **Linker Kind Knoten** (Referenz, oder `None`/`∅`)
- **Rechter Kind Knoten** (Referenz, oder `None`/`∅`)

```
Knoten-Struktur (Binärbaum):
        ┌─────────┐
        │ Element │
        ├─────────┤
  ∅ ←── │ Parent  │ ──→ Elternknoten
        ├────┬────┤
        │ L  │ R  │
        └──┬─┴──┬─┘
           ↓    ↓
        Links  Rechts
        Kind   Kind
```

```
Beispiel: Binärbaum B mit verlinkten Knoten

            B (parent=∅)
           / \
     (parent=B)  (parent=B)
          A         D
         / \       / \
        ∅   ∅  (p=D) (p=D)
               C       E
              /\      /\
             ∅  ∅    ∅  ∅
```

#### 8.3 Array-basierte Speicherung (VectorTree) ⭐

Die Knoten werden in einem **Array** gespeichert. Die Position im Array wird durch den **Rank** bestimmt.

> ⚠️ **Schlüsselformeln für Array-basierte Bäume:**

| Formel | Beschreibung |
|---|---|
| `rank(root) = 1` | Wurzel steht an Index 1 (Index 0 bleibt leer/`None`) |
| `rank(leftChild) = 2 * rank(parent)` | Linkes Kind = doppelter Index des Elternknotens |
| `rank(rightChild) = 2 * rank(parent) + 1` | Rechtes Kind = doppelter Index + 1 |
| `rank(parent) = rank(node) // 2` | Elternknoten = ganzzahlige Division durch 2 |

```
Beispiel: Baum → Array-Abbildung

Baum:               Array:
      A (rank 1)     Index: [0]  [1]  [2]  [3]  [4]  [5]  [6]  [7]
     / \              Wert: None  A    B    D   None  F   None None
    B   D (2, 3)      
     \                ...weiter bei tieferen Ebenen:
      F  (rank 5)     [8]  [9]  [10]  [11]  ...
                      None None   G     H   None ...
   / \
  G   H (10, 11)
```

**Navigationsbeispiel (rank = 5, Knoten F):**
- Parent: `5 // 2 = 2` → Index 2 → **B** ✓
- Left child: `5 * 2 = 10` → Index 10 → **G** ✓
- Right child: `5 * 2 + 1 = 11` → Index 11 → **H** ✓

> ⚠️ **Wichtig:**
> - Index 0 bleibt **immer `None`** (unused)
> - Array-Länge ist immer eine **2er-Potenz**
> - Array wird nur **vergrössert**, nie verkleinert
> - Mehrfache (gleiche) Keys werden **nicht** unterstützt

---

## 📐 Baumtraversierungen

### Übersicht

Bei einer Baumtraversierung werden **alle Knoten** eines Baumes auf systematische Art besucht.

| Traversierung | Besuchsreihenfolge | Datenstruktur | Geeignet für |
|---|---|---|---|
| **Preorder** | Knoten **vor** seinen Kindern | Stack (rekursiv) | Drucken von Dokumenten, Kopieren |
| **Postorder** | Knoten **nach** seinen Kindern | Stack (rekursiv) | Speicherberechnung, Löschen |
| **Breadth-First** | Ebene für Ebene (links → rechts) | **Queue** | Kürzester Pfad, Level-Order |
| **Inorder** | Links → Knoten → Rechts (nur Binärbaum!) | Stack (rekursiv) | Sortierte Ausgabe, Zeichnen |

---

### Preorder Traversierung

> In einer Preorder Traversierung wird ein Knoten **vor** seinen Nachfolgern besucht.

**Pseudocode:**
```
Algorithm preOrder(v):
    visit(v)                    ← Knoten zuerst besuchen
    for each child w of v:
        preOrder(w)             ← dann rekursiv die Kinder
```

**Beispiel: Dokument-Struktur**
```
                    1
               Make Money Fast!
              /        |        \
         2              5              9
    1. Motivations   2. Methods    References
       /    \         /   |   \
   3        4      6      7      8
  1.1 Greed 1.2   2.1    2.2    2.3
           Avidity Stock  Ponzi  Bank
                  Fraud  Scheme Robbery

Preorder: 1, 2, 3, 4, 5, 6, 7, 8, 9
```

> 💡 **Merkregel:** Zuerst sich selbst, dann alle Kinder von links nach rechts.

---

### Postorder Traversierung

> In einer Postorder Traversierung wird ein Knoten **nach** seinen Nachfolgern besucht.

**Pseudocode:**
```
Algorithm postOrder(v):
    for each child w of v:
        postOrder(w)            ← zuerst rekursiv die Kinder
    visit(v)                    ← dann den Knoten besuchen
```

**Beispiel: Speicherberechnung in Dateisystem**
```
                          9
                        cs16/
                      /    |    \
                   3         7        8
              homeworks/  programs/  todo.txt
               /    \     /   |   \    1K
            1       2    4    5    6
          h1c.doc h1nc  DDR  Stocks Robot
           3K     2K   .java .java .java
                       10K   25K   20K

Postorder: 1, 2, 3, 4, 5, 6, 7, 8, 9
→ Zuerst Blätter (Dateien), dann Ordner (Summe der Kinder)
```

> 💡 **Anwendung:** Berechnung des Speicherplatzes – ein Ordner benötigt die Summe aller Unterordner/Dateien.

---

### Breadth-First Traversierung (Level-Order)

> In einer Breadth-First Traversierung werden zuerst alle Knoten einer **Tiefe t** besucht, bevor die Knoten der Tiefe **t+1** besucht werden.

**Pseudocode (verwendet eine Queue!):**
```
Algorithm breadthFirst():
    Initialize queue Q containing root
    while Q not empty do:
        v = Q.dequeue()
        visit(v)
        for each child w in children(v) do:
            Q.enqueue(w)
```

```
Beispiel: Breadth-First Traversierung

             1
           /   \
         2       3
        / \     / \
       4   5   6   7

Queue-Ablauf:
  Start:    Q = [1]
  Schritt 1: dequeue 1, visit 1, enqueue [2, 3]     → Q = [2, 3]
  Schritt 2: dequeue 2, visit 2, enqueue [4, 5]     → Q = [3, 4, 5]
  Schritt 3: dequeue 3, visit 3, enqueue [6, 7]     → Q = [4, 5, 6, 7]
  Schritt 4: dequeue 4, visit 4                     → Q = [5, 6, 7]
  Schritt 5: dequeue 5, visit 5                     → Q = [6, 7]
  Schritt 6: dequeue 6, visit 6                     → Q = [7]
  Schritt 7: dequeue 7, visit 7                     → Q = []

  Besuchsreihenfolge: 1, 2, 3, 4, 5, 6, 7
```

> 💡 **Merke:** Breadth-First ist die **einzige** Traversierung, die eine **Queue** statt Rekursion/Stack verwendet.

---

### Inorder Traversierung (nur für Binärbäume!)

> In einer Inorder Traversierung wird ein Knoten **nach** seinem linken Subtree und **vor** seinem rechten Subtree besucht.

**Pseudocode:**
```
Algorithm inOrder(v):
    if hasLeft(v):
        inOrder(left(v))        ← zuerst linken Teilbaum
    visit(v)                    ← dann den Knoten
    if hasRight(v):
        inOrder(right(v))       ← dann rechten Teilbaum
```

**Beispiel: Darstellung von binären Bäumen**
```
Koordinaten-Zuordnung:
  x(v) = inorder Rang von v
  y(v) = Tiefe von v

             6
            / \
           2    8
          / \  / \
         1  4  7  9
           / \
          3   5

Inorder: 1, 2, 3, 4, 5, 6, 7, 8, 9  ← sortiert!
```

> ⚠️ **Prüfungsrelevant:** Bei einem **Binary Search Tree** liefert die Inorder-Traversierung die Elemente in **sortierter Reihenfolge**!

---

### Anwendung: Arithmetische Ausdrücke

#### Ausgabe (printExpression) – basiert auf Inorder

> Spezialisierung der Inorder Traversierung für vollständig geklammerte Ausdrücke.

**Pseudocode:**
```
Algorithm printExpression(v):
    if hasLeft(v):
        print("(")
        printExpression(left(v))
    print(v.element())
    if hasRight(v):
        printExpression(right(v))
        print(")")
```

```
Beispiel: Arithmetischer Ausdruck als Baum

              +
            /   \
           ×     ×
          / \   / \
         2   -  3   b
            / \
           a   1

Inorder mit Klammern: ((2 × (a − 1)) + (3 × b))
```

#### Auswertung (evalExpr) – basiert auf Postorder

> Rekursive Methode, die den **Wert eines Unterbaums** liefert.

**Pseudocode:**
```
Algorithm evalExpr(v):
    if isExternal(v):
        return v.element()           ← Blatt = Zahlenwert
    else:
        x ← evalExpr(leftChild(v))   ← Wert linker Teilbaum
        y ← evalExpr(rightChild(v))  ← Wert rechter Teilbaum
        ◇ ← Operator bei v           ← z.B. +, -, ×, /
        return x ◇ y                 ← Ergebnis berechnen
```

```
Beispiel: Auswertung von ((2 × (5 − 1)) + (3 × 2))

              +
            /   \
           ×     ×
          / \   / \
         2   -  3   2
            / \
           5   1

Postorder-Auswertung:
  evalExpr(5) = 5
  evalExpr(1) = 1
  evalExpr(-) = 5 - 1 = 4
  evalExpr(2) = 2
  evalExpr(×links) = 2 × 4 = 8
  evalExpr(3) = 3
  evalExpr(2) = 2
  evalExpr(×rechts) = 3 × 2 = 6
  evalExpr(+) = 8 + 6 = 14 ✓
```

---

## 📊 Klassifizierungen / Vergleiche

### Allgemeiner Baum vs. Binärer Baum

| Eigenschaft | Allgemeiner Baum | Binärer Baum |
|---|---|---|
| **Max. Kinder pro Knoten** | Unbegrenzt | 2 (links & rechts) |
| **Kindanordnung** | Sequenz (Liste) | Geordnetes Paar |
| **Inorder-Traversierung** | ❌ Nicht definiert | ✅ Definiert |
| **Array-Speicherung** | Nicht effizient | ✅ Effizient (Rank-Formeln) |
| **Typische Anwendungen** | Dateisysteme, XML | Suche, Ausdrücke, Heaps |

### Verlinkte vs. Array-basierte Speicherung

| Kriterium | Verlinkte Knoten | Array-basiert (VectorTree) |
|---|---|---|
| **Speicher** | Nur belegte Knoten | Ggf. viele leere Positionen |
| **Navigation zu Kind** | O(1) via Referenz | O(1) via `2*rank` / `2*rank+1` |
| **Navigation zu Eltern** | O(1) via Referenz | O(1) via `rank // 2` |
| **Einfügen/Löschen** | O(1) (Referenzen umhängen) | O(1) Wert setzen + ggf. Array vergrössern |
| **Speichereffizienz** | ✅ Gut | ❌ Schlecht bei unbalancierten Bäumen |
| **Cache-Freundlichkeit** | ❌ Schlecht | ✅ Gut (zusammenhängendes Array) |
| **Geeignet für** | Allgemeine Bäume | Binärbäume (bes. vollständige) |

### Traversierungsvergleich

| Eigenschaft | Preorder | Postorder | Inorder | Breadth-First |
|---|---|---|---|---|
| **Besuchszeitpunkt** | Vor Kindern | Nach Kindern | Zwischen L/R | Ebenenweise |
| **Nur Binärbäume?** | Nein | Nein | **Ja** | Nein |
| **Datenstruktur** | Stack (Rekursion) | Stack (Rekursion) | Stack (Rekursion) | **Queue** |
| **Laufzeit** | O(n) | O(n) | O(n) | O(n) |
| **Anwendung** | Drucken, Kopieren | Löschen, Speicher | Sortierte Ausgabe | Level-Order |

---

## ⏱️ Komplexitätsanalyse

### Traversierungen

| Algorithmus | Best Case | Average Case | Worst Case | Speicher |
|---|---|---|---|---|
| **Preorder** | O(n) | O(n) | O(n) | O(h) Stack |
| **Postorder** | O(n) | O(n) | O(n) | O(h) Stack |
| **Inorder** | O(n) | O(n) | O(n) | O(h) Stack |
| **Breadth-First** | O(n) | O(n) | O(n) | O(w) Queue |

> h = Höhe des Baums, w = maximale Breite (max. Knoten auf einer Ebene)

### Tiefe und Höhe

| Algorithmus | Laufzeit | Beschreibung |
|---|---|---|
| `depth(v)` | **O(d_v)** | d_v = Tiefe von v; worst case O(n) bei entartetem Baum |
| `height(v)` | **O(n)** | Muss alle Knoten im Unterbaum besuchen |

### VectorTree-Operationen (Array-basiert)

| Operation | Laufzeit | Beschreibung |
|---|---|---|
| `root()` | **O(1)** | Direkter Zugriff auf Index 1 |
| `parent(k)` | **O(n)** | Suche nach k im Array mit `index()`, dann `// 2` |
| `leftChild(k)` | **O(n)** | Suche nach k, dann `* 2` |
| `rightChild(k)` | **O(n)** | Suche nach k, dann `* 2 + 1` |
| `isRoot(k)` | **O(1)** | Vergleich mit `_binary_tree[1]` |
| `isExternal(k)` | **O(n)** | Suche nach k + Prüfung der Kind-Positionen |
| `isInternal(k)` | **O(n)** | Negation von `isExternal(k)` |
| `setRoot(k)` | **O(n)** | Ggf. alten Teilbaum entfernen |
| `setLeftChild(p, c)` | **O(n)** | Ggf. Subtree entfernen + Array vergrössern |
| `setRightChild(p, c)` | **O(n)** | Ggf. Subtree entfernen + Array vergrössern |
| `size()` | **O(1)** | Direkter Zugriff auf `_size` |

> ⚠️ **Hinweis:** Die O(n)-Laufzeit kommt durch die `_position(node)`-Methode, die mit `list.index(node)` das gesamte Array durchsucht. Eine optimierte Implementation könnte O(1) erreichen mit einem Dictionary für die Position.

### Wichtige Formelsammlung

| Eigenschaft | Formel |
|---|---|
| **Kanten im Baum** | Ein Baum mit **n** Knoten hat genau **n − 1** Kanten |
| **Binärbäume aus 3 Knoten** | 5 Grundformen × 3! = **30** verschiedene Bäume |
| **Rank linkes Kind** | `rank(left) = 2 × rank(parent)` |
| **Rank rechtes Kind** | `rank(right) = 2 × rank(parent) + 1` |
| **Rank Eltern** | `rank(parent) = rank(node) // 2` |
| **Array-Grösse** | Immer eine **2er-Potenz** (verdoppeln bei Bedarf) |
| **Gausssche Summenformel** | `Σ i (i=0..n-1) = n(n−1)/2` → O(n²) |

---

## 💻 Wichtigste Code-Beispiele

### 1. Tiefe berechnen (rekursiv)

> Berechnet die Tiefe eines Knotens im Baum durch rekursives Aufsteigen zum Elternknoten.

```python
def depth(tree, v):
    """Berechnet die Tiefe von Knoten v im Baum.
    Tiefe = Anzahl Vorgänger (Kanten zur Wurzel).
    Laufzeit: O(d_v), wobei d_v die Tiefe von v ist."""
    if tree.is_root(v):
        return 0                          # Wurzel hat Tiefe 0
    else:
        return 1 + depth(tree, tree.parent(v))  # Rekursiv aufsteigen
```

---

### 2. Höhe berechnen (rekursiv)

> Berechnet die Höhe eines Knotens durch rekursives Absteigen zu den Kindern.

```python
def height(tree, v):
    """Berechnet die Höhe von Knoten v im Baum.
    Höhe = maximale Tiefe im Unterbaum.
    Laufzeit: O(n), besucht jeden Knoten einmal."""
    h = 0
    for w in tree.children(v):            # Für jedes Kind
        h = max(h, 1 + height(tree, w))   # Maximum der Kinderhöhen + 1
    return h                              # Blatt: Schleife läuft nicht → h = 0
```

---

### 3. Traversierungen in Python

```python
def preorder(v, visit_func):
    """Preorder: Knoten VOR seinen Kindern besuchen."""
    visit_func(v)                         # Zuerst den Knoten besuchen
    for child in v.children:              # Dann alle Kinder (links → rechts)
        preorder(child, visit_func)


def postorder(v, visit_func):
    """Postorder: Knoten NACH seinen Kindern besuchen."""
    for child in v.children:              # Zuerst alle Kinder (links → rechts)
        postorder(child, visit_func)
    visit_func(v)                         # Dann den Knoten besuchen


def inorder(v, visit_func):
    """Inorder: Nur für Binärbäume!
    Links → Knoten → Rechts."""
    if v.left is not None:                # Zuerst linken Teilbaum
        inorder(v.left, visit_func)
    visit_func(v)                         # Dann den Knoten
    if v.right is not None:               # Dann rechten Teilbaum
        inorder(v.right, visit_func)


def breadth_first(root, visit_func):
    """Breadth-First: Ebene für Ebene, verwendet Queue.
    Einzige Traversierung die NICHT rekursiv ist."""
    from collections import deque
    queue = deque([root])                 # Queue mit Wurzel initialisieren
    while queue:                          # Solange Queue nicht leer
        v = queue.popleft()               # Vordersten Knoten entnehmen (dequeue)
        visit_func(v)                     # Knoten besuchen
        for child in v.children:          # Alle Kinder hinten anfügen (enqueue)
            queue.append(child)
```

---

### 4. Arithmetischer Ausdruck ausgeben (Inorder)

```python
def print_expression(v):
    """Gibt einen arithmetischen Ausdruck vollständig geklammert aus.
    Basiert auf Inorder-Traversierung."""
    if v.left is not None:                # Hat linkes Kind → öffnende Klammer
        print("(", end="")
        print_expression(v.left)          # Linken Teilbaum ausgeben
    print(v.element, end="")              # Element/Operator ausgeben
    if v.right is not None:               # Hat rechtes Kind → schliessende Klammer
        print_expression(v.right)         # Rechten Teilbaum ausgeben
        print(")", end="")
```

---

### 5. Arithmetischen Ausdruck auswerten (Postorder)

```python
def eval_expression(v):
    """Wertet einen arithmetischen Ausdrucksbaum rekursiv aus.
    Basiert auf Postorder-Traversierung.
    Blätter = Zahlen, interne Knoten = Operatoren."""
    if v.left is None and v.right is None:  # Blatt = Zahlenwert
        return v.element
    else:
        x = eval_expression(v.left)         # Linken Teilbaum auswerten
        y = eval_expression(v.right)        # Rechten Teilbaum auswerten
        op = v.element                      # Operator bei diesem Knoten
        if op == '+': return x + y
        elif op == '-': return x - y
        elif op == '*': return x * y
        elif op == '/': return x / y
```

---

### 6. VectorTree – Array-basierter Binärbaum (Musterlösung) ⭐

> Vollständige Musterlösung der Übungsaufgabe 2. Implementiert einen Binärbaum mit einem Array (Python `list`).

```python
import enum

# Eigene Exception für fehlende Knoten
class NoSuchNodeException(Exception):
    def __init__(self, err):
        super().__init__(err)

ROOT_INDEX = 1   # Wurzel steht an Index 1 (Index 0 = None)

class VectorTree:
    """Array-basierter Binärbaum.
    Speichert Knoten in einem Array, wobei:
      - rank(root) = 1
      - rank(leftChild)  = 2 * rank(parent)
      - rank(rightChild) = 2 * rank(parent) + 1
      - rank(parent)     = rank(node) // 2
    """

    class _child_side(enum.Enum):
        """Enum zur Unterscheidung links/rechts."""
        LEFT = enum.auto()
        RIGHT = enum.auto()

    def __init__(self):
        """Initialisiert leeren Baum mit Array [None, None]."""
        self._binary_tree = []
        self._binary_tree.append(None)   # Index 0: unused
        self._binary_tree.append(None)   # Index 1: Platz für Root
        self._size = 0

    def root(self):
        """Gibt das Wurzelelement zurück. O(1)."""
        return self._binary_tree[ROOT_INDEX]

    def set_root(self, root):
        """Setzt die Wurzel. Entfernt ggf. alten Teilbaum. O(n)."""
        if self.root() != None:
            self._remove(ROOT_INDEX)     # Alten Baum komplett entfernen
        self._binary_tree[ROOT_INDEX] = root
        self._size = 1

    def parent(self, child):
        """Gibt den Elternknoten zurück. O(n) wegen _position()."""
        if self.is_root(child):
            return None                  # Wurzel hat keinen Elternknoten
        return self._binary_tree[self._position(child) // 2]

    def left_child(self, parent):
        """Gibt das linke Kind zurück. O(n)."""
        return self._get_child(parent, VectorTree._child_side.LEFT)

    def right_child(self, parent):
        """Gibt das rechte Kind zurück. O(n)."""
        return self._get_child(parent, VectorTree._child_side.RIGHT)

    def _get_child(self, parent, child_side):
        """Hilfsmethode: Kind-Knoten holen."""
        child_pos = self._child_pos_by_value(parent, child_side)
        if not self._has_node_at_position(child_pos):
            return None
        return self._binary_tree[child_pos]

    def _child_pos_by_value(self, parent, child_side):
        """Berechnet Kind-Position anhand des Eltern-WERTES."""
        return self._child_pos_by_index(self._position(parent), child_side)

    def _child_pos_by_index(self, parent_pos, child_side):
        """Berechnet Kind-Position anhand des Eltern-INDEX.
        Links: 2 * parent_pos
        Rechts: 2 * parent_pos + 1"""
        return parent_pos * 2 + (0 if child_side == VectorTree._child_side.LEFT else 1)

    def is_internal(self, node):
        """Prüft ob Knoten intern ist (hat Kinder). O(n)."""
        return not self.is_external(node)

    def is_external(self, node):
        """Prüft ob Knoten ein Blatt ist (keine Kinder). O(n)."""
        left_child_pos = self._child_pos_by_value(node, VectorTree._child_side.LEFT)
        right_child_pos = left_child_pos + 1
        if self._has_node_at_position(left_child_pos) or \
           self._has_node_at_position(right_child_pos):
            return False                 # Hat mindestens ein Kind → intern
        else:
            return True                  # Keine Kinder → Blatt

    def _has_node_at_position(self, pos):
        """Prüft ob an Position pos ein Knoten existiert."""
        if pos > (len(self._binary_tree) - 1):
            return False                 # Position ausserhalb des Arrays
        return self._binary_tree[pos] != None

    def is_root(self, node):
        """Prüft ob Knoten die Wurzel ist. O(1)."""
        return node == self._binary_tree[ROOT_INDEX]

    def set_right_child(self, parent, child):
        """Rechtes Kind setzen. Entfernt ggf. alten Teilbaum. O(n)."""
        self._set_child(parent, child, VectorTree._child_side.RIGHT)

    def set_left_child(self, parent, child):
        """Linkes Kind setzen. Entfernt ggf. alten Teilbaum. O(n)."""
        self._set_child(parent, child, VectorTree._child_side.LEFT)

    def _set_child(self, parent, child, child_side):
        """Hilfsmethode: Kind setzen mit Aufräumarbeit."""
        self._remove_child(parent, child_side)   # Altes Kind-Subtree entfernen
        child_pos = self._child_pos_by_value(parent, child_side)
        self._assure_size(child_pos)             # Array ggf. vergrössern
        if self._binary_tree[child_pos] == None:
            self._size += 1
        self._binary_tree[child_pos] = child

    def _remove(self, node_pos):
        """Entfernt Knoten und alle Nachfolger rekursiv. O(Teilbaumgrösse)."""
        for child_side in VectorTree._child_side:
            child_pos = self._child_pos_by_index(node_pos, child_side)
            if self._has_node_at_position(child_pos):
                self._remove(child_pos)          # Rekursiv Kinder entfernen
        self._binary_tree[node_pos] = None       # Knoten auf None setzen
        self._size -= 1

    def size(self):
        """Anzahl Knoten im Baum. O(1)."""
        return self._size

    def _position(self, node):
        """Findet den Index des Knotens im Array. O(n).
        Wirft NoSuchNodeException wenn nicht gefunden."""
        try:
            pos = self._binary_tree.index(node)
        except ValueError:
            raise NoSuchNodeException("No node:" + node)
        return pos

    def _assure_size(self, pos):
        """Vergrössert das Array auf mindestens pos Einträge.
        Verdoppelt die Grösse (2er-Potenz Strategie)."""
        current_length = len(self._binary_tree)
        if pos >= current_length:
            new_length = 2 * current_length
            i = current_length
            while i < new_length:
                self._binary_tree.append(None)
                i += 1

    def print_vector(self, message):
        """Debug-Ausgabe des internen Arrays."""
        print("\n" + message)
        print(self._binary_tree)
```

#### Beispiel-Session (aus dem Test):

```python
vt = VectorTree()

vt.set_root('A')
# Array: [None, 'A']

vt.set_right_child('A', 'D')
# Array: [None, 'A', None, 'D']

vt.set_left_child('A', 'B')
# Array: [None, 'A', 'B', 'D']

vt.set_right_child('B', 'F')
# Array: [None, 'A', 'B', 'D', None, 'F', None, None]
#                  1    2    3    4     5    6     7

vt.set_right_child('F', 'H')
# Array wird verdoppelt!
# [None, 'A', 'B', 'D', None, 'F', None, None,
#  None, None, None, 'H', None, None, None, None]
#                          11 (= 5*2+1)

vt.set_left_child('F', 'G')
# [None, 'A', 'B', 'D', None, 'F', None, None,
#  None, None, 'G', 'H', None, None, None, None]
#               10 (=5*2)  11 (=5*2+1)

# Navigation:
print(vt.parent('H'))         # → 'F'  (Index 11 // 2 = 5 → 'F')
print(vt.left_child('F'))     # → 'G'  (Index 5 * 2 = 10 → 'G')
print(vt.is_external('H'))    # → True (keine Kinder)
print(vt.is_internal('F'))    # → True (hat Kinder G und H)
```

---

## 📝 Übungsaufgaben-Zusammenfassung

| Aufgabe | Thema | Kernkonzept |
|---|---|---|
| **1a** | Binärbäume aus 3 Knoten zählen | 5 Grundformen × 3! Permutationen = **30 Bäume** |
| **1b** | Blätter-Reihenfolge bei Traversierung | Preorder, Postorder und Inorder liefern Blätter **immer in gleicher Reihenfolge** |
| **1c** | Beweis: n Knoten → n−1 Kanten | **Vollständige Induktion**: n=1 hat 0 Kanten; bei n→n+1 wird genau 1 Kante hinzugefügt |
| **2** | VectorTree (Array-basierter Binärbaum) | Implementation mit Rank-Formeln, Array-Verdopplung, rekursives Löschen |

### Aufgabe 1a – Detail: 30 Binärbäume aus A, B, C

Es gibt **5 strukturelle Grundformen** eines Binärbaums mit 3 Knoten:

```
  ○       ○       ○       ○       ○
 /       / \       \     /         \
○       ○   ○       ○   ○           ○
 \                 /       \       /
  ○               ○         ○     ○
```

Für jede Form können die 3 Knoten A, B, C **permutiert** werden:
→ 5 × 3! = 5 × 6 = **30 verschiedene Bäume**

> ⚠️ **Wichtig:** Die Reihenfolge beim Einfügen und die Manipulier-Reihenfolge ergeben völlig andere Bäume!

### Aufgabe 1b – Detail: Blätter-Reihenfolge

Die Reihenfolge der **Blätter** (externe Knoten) ist bei **Preorder**, **Postorder** und **Inorder** Traversierung **immer identisch**.

Beispiel mit Baum (A in der Root, B und C als Blätter links/rechts):
- Preorder: A, **B**, **C** → Blätter: B, C
- Postorder: **B**, **C**, A → Blätter: B, C
- Inorder: **B**, A, **C** → Blätter: B, C ✓

### Aufgabe 1c – Detail: Beweis n Knoten → n−1 Kanten

**Vollständige Induktion:**

**Basis (n=1):** Ein Baum mit 1 Knoten hat 0 Kanten. ✓ (1 − 1 = 0)

**Induktionsschritt (n → n+1):**
Wenn man einen Knoten zum Baum hinzufügt, muss genau **eine Kante** hinzugefügt werden (Verbindung zum Elternknoten).
→ Somit hat der Baum stets eine Kante weniger als Knoten. ✓

---

## ⚠️ Prüfungsrelevante Hinweise

### Typische Aufgabentypen

1. **Traversierungs-Reihenfolge angeben** – Für einen gegebenen Baum die Preorder/Postorder/Inorder/Breadth-First Reihenfolge aufschreiben
2. **Rank-Berechnungen** – Array-Index für einen Knoten im VectorTree berechnen (Eltern, Kinder)
3. **Baum-Eigenschaften bestimmen** – Tiefe, Höhe, Anzahl Knoten/Blätter
4. **Binärbäume zählen/zeichnen** – Alle möglichen Formen für n Knoten
5. **Beweis per Induktion** – z.B. n Knoten → n−1 Kanten
6. **Pseudocode/Python-Code lesen** – Traversierungsalgorithmen verstehen und anwenden
7. **Arithmetische Ausdrucksbäume** – Ausdruck als Baum zeichnen, auswerten, ausgeben

### Häufige Fehlerquellen

| Fehler | Korrekt |
|---|---|
| Inorder auf allgemeine Bäume anwenden | Inorder ist **nur für Binärbäume** definiert! |
| Tiefe ≠ Höhe verwechseln | **Tiefe** = Abstand zur Wurzel (nach oben); **Höhe** = Abstand zum tiefsten Blatt (nach unten) |
| Array-Index 0 verwenden | Index 0 bleibt **immer `None`**, Wurzel ist bei **Index 1** |
| Rank-Formel falsch | Links: `2 × parent`, Rechts: `2 × parent + 1`, Eltern: `node // 2` |
| Breadth-First mit Stack | Breadth-First verwendet eine **Queue**, nicht einen Stack! |
| Blätter-Reihenfolge verschieden | Pre/Post/Inorder liefern Blätter **immer gleich** |
| Anzahl Kanten falsch | Ein Baum mit n Knoten hat immer **n − 1** Kanten |

### Tricks und Merkregeln

| Regel | Erklärung |
|---|---|
| 🌲 **„Wurzel oben"** | In der Informatik wachsen Bäume **nach unten** (Wurzel oben, Blätter unten) |
| 🔢 **„Links × 2, Rechts × 2 + 1"** | Rank-Formeln für Array-basierte Bäume merken |
| 📦 **„Pre = Vorher, Post = Nachher, In = Dazwischen"** | Wann wird der aktuelle Knoten besucht |
| 🔄 **„Breadth-First = Queue"** | Einzige Traversierung die **iterativ** mit Queue arbeitet |
| 📐 **„Höhe = Ebenen"** | Die Höhe eines Baums = Anzahl Ebenen (praktische Anschauung) |
| 🧮 **Ratio-Trick** | Verdopplung → x4 = O(n²), x2 = O(n), x8 = O(n³) |

---

## 🔗 Verbindung zu vorherigen Wochen

### Aufbau auf SW01 (O-Notation, Rekursion)

- **Rekursion** ist das zentrale Werkzeug für Baumtraversierungen (Tiefe, Höhe, Pre/Post/Inorder sind alle rekursiv)
- **O-Notation** wird verwendet um Traversierungen (O(n)) und einzelne Operationen des VectorTree zu analysieren
- **Gausssche Summenformel** aus SW01 bleibt relevant für allgemeine Laufzeitanalysen

### Aufbau auf SW02 (Stack, Queue, Deque)

- **Queue** wird direkt für die **Breadth-First Traversierung** verwendet (`enqueue`/`dequeue`)
- **Stack** (implizit durch Rekursion) wird für Pre/Post/Inorder Traversierungen verwendet
- **Array-basierte Datenstrukturen** – VectorTree nutzt ein dynamisches Array ähnlich der Array-List Konzepte aus SW02
- **Array-Verdopplungsstrategie** (2er-Potenz) aus SW02 wird im VectorTree wiederverwendet

### Vorausblick auf SW04 (Priority-Queue, Heap)

- Ein **Heap** ist ein spezieller Binärbaum, der Array-basiert gespeichert wird (gleiche Rank-Formeln!)
- Die Baumtraversierungen werden in späteren Wochen für **Binary Search Trees** (SW06) und **Graphen** (SW11-12) erweitert

---

> 📌 **Tipp:** Üben Sie das händische Durchführen aller 4 Traversierungen an verschiedenen Bäumen – das ist die häufigste Prüfungsaufgabe zu diesem Thema!
