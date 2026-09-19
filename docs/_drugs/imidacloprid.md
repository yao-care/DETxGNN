---
layout: default
title: Imidacloprid
parent: Nur Modellvorhersage (L5)
nav_order: 198
evidence_level: L5
indication_count: 9
---

# Imidacloprid
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **9** 
{: .fs-6 .fw-300 }

---

## Inhaltsverzeichnis
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmazeutischer Bewertungsbericht

</div>

# Imidacloprid: Vom Insektizid zum Cauda-Equina-Syndrom

## Zusammenfassung in einem Satz

> Imidacloprid ist ein Neonikotinoid-Insektizid ohne genehmigte medizinische Indikation; es ist kein zugelassenes Arzneimittel.
> Das TxGNN-Modell sagt voraus, dass es möglicherweise wirksam bei **Cauda-Equina-Syndrom** ist,
> aber diese Vorhersage wird durch **0 klinische Studien** und **0 Publikationen** gestützt, und der eigene Wirkmechanismus des Arzneistoffs (Insekten-selektive Nikotinacetylcholin-Rezeptor-(nAChR)-Agonisten mit minimaler Wirbeltier-Affinität) bietet keine biologische Grundlage für diese oder eine der anderen Kandidaten-Indikationen.

---

## Schnellübersicht

| Element | Inhalt |
|--------|--------|
| Ursprüngliche Indikation | Nicht zutreffend — Imidacloprid ist ein Neonikotinoid-Insektizid, kein zugelassenes Arzneimittel für Menschen |
| Vorhergesagte neue Indikation | Cauda-Equina-Syndrom |
| TxGNN-Vorhersage-Score | 99.99% (Rang 208 von allen Kandidaten-Erkrankungen) |
| Evidenzgrad | L5 (nur Modellvorhersage, keine unterstützenden Studien) |
| Marktstatus in Deutschland | ✗ Nicht vermarktet |
| Anzahl der Zulassungen | 0 |
| Empfehlung | **Halten** |

---

## Warum ist diese Vorhersage sinnvoll?

Das ist sie nicht. Imidacloprid ist ein Insekten-selektiver Nikotinacetylcholin-Rezeptor-(nAChR)-Agonist. Seine Selektivität für Insekten-Typ-nAChR-Untereinheiten gegenüber Wirbeltier-nAChR — kombiniert mit sehr niedriger Affinität zum Wirbeltier-Rezeptor — ist genau die pharmakologische Grundlage für sein Sicherheitsprofil als Insektizid. Dies ist das Gegenteil einer Eigenschaft, nach der man suchen würde, wenn man einen Wirkstoff für eine menschliche neurologische Erkrankung neu bewerten würde.

Das Cauda-Equina-Syndrom ist ein mechanisch-kompressives neurologisches Notfall (Nervenwurzelkompression im lumbosakralen Spinalkanal), typischerweise verursacht durch Bandscheibenvorfall, Tumor, Trauma oder Infektion. Es gibt keinen plausiblen pharmakologischen Weg, auf dem ein Wirbeltier-nAChR-sparendes Insektizid Nervenwurzelkompression behandeln würde. Der TxGNN-Score spiegelt höchstwahrscheinlich Graphen-Topologie-Ähnlichkeit (gemeinsame Metadaten oder indirekte Netzwerkpfade) wider, anstatt eines zugrunde liegenden biologischen Signals — diese Interpretation ist konsistent mit der eigenen Bewertung des Evidenzpakets.

Die gleiche Schlussfolgerung gilt für die anderen acht eingestuften Vorhersagen in diesem Evidenzpaket (veraltete neurogene Blasendysfunktion, Reizdarmsyndrom, Ösophaguserkrankungen, Mitralklappenprolapс und seine Subtypen, neurozirkulatorische Asthenie): alle werden mit L5 bewertet, alle haben Empfehlungen zum „Halten" und keine weist eine dokumentierte mechanistische Verbindung zur bekannten Pharmakologie von Imidacloprid auf. Wo klinische Studien oder Literatur für niedriger eingefärbte Kandidaten abgerufen wurden (z. B. Reizdarmsyndrom, Ösophaguserkrankung), bestätigen Anmerkungen des Bewerters, dass dies falsch-positive Treffer sind — die abgerufenen Studien betreffen nicht verwandte Interventionen (osteopathische Manipulationen, Strahlentherapie, Endoskopie-Techniken), die allein aufgrund von Krankheitsname-Überlappung eingezogen wurden, nicht weil sie Imidacloprid untersuchten. Der eine echte Imidacloprid-bezogene Datensatz (PMID 29506575) ist eine veterinärmedizinische Studie eines topischen Imidacloprid-Moxidectin-Antiparasitikums bei Hunden mit Ösophagus-Spirocercosis — eine parasitäre Infektion, keine menschliche Ösophaguserkrankung und nicht relevant für die Neuanwendung beim Menschen.

---

## Evidenzlage aus klinischen Studien

Derzeit sind keine zugehörigen klinischen Studien registriert.

---

## Evidenzlage aus Literatur

Derzeit ist keine zugehörige Literatur verfügbar.

---

## Marktinformationen für Deutschland

Imidacloprid besitzt keine Vermarktungszulassungen in Deutschland (0 Lizenzen registriert). Es ist registriert und wird ausschließlich als landwirtschaftliches/veterinärmedizinisches Insektizid verwendet (z. B. Floh-/Zeckenprodukte zum Auftragen, Pflanzenschutz), nicht als Arzneimittel für den Menschen.

---

## Sicherheitsaspekte

Bitte beachten Sie die Fachinformation für Sicherheitsinformationen.

*(Hinweis: Das Evidenzpaket kennzeichnet TFDA-ähnliche Kennzeichnung/Warnhinweise und Kontraindikationsdaten als blockierenden Datenmangel — dies muss aus regulatorischen Quellen wie Fachinformationen für Veterinärprodukte und Pestizid-Sicherheitsdatenblättern behoben werden, bevor weitere Bewertungen durchgeführt werden, da keine Fachinformation für die Humanmedizin vorhanden ist.)*

---

## Fazit und nächste Schritte

**Entscheidung: Halten**

**Begründung:**
Imidacloprid ist kein Arzneimittel für den Menschen, hat keine Vermarktungszulassung in Deutschland und keine der neun von TxGNN vorhergesagten Indikationen (einschließlich des am höchsten eingestuften Cauda-Equina-Syndroms) werden durch klinische Studien, Literatur oder eine plausible mechanistische Begründung unterstützt. Die Kern-Pharmakologie des Arzneistoffs — Sparing von Wirbeltier-nAChR — spricht gegen, nicht für die therapeutische Neuanwendung beim Menschen. Dieser Kandidat erfüllt nicht die minimale Evidenzschwelle, um über S0 hinaus voranzukommen.

**Zur Fortsetzung ist Folgendes erforderlich:**
- Bestätigung von Sicherheits-/Toxikologiedaten für Menschen (derzeit ein blockierender Datenmangel) — kritisch angesichts der Verwendung von Imidacloprid als Pestizid
- Unabhängige mechanistische Validierung, die erklärt, warum ein Wirbeltier-nAChR-sparendes Insektizid irgendeine Aktivität bei den vorhergesagten Indikationen hätte
- Neubewertung der TxGNN-Vorhersage selbst, angesichts der hohen Wahrscheinlichkeit, dass dies eher Graphen-Topologie-Artefakte als biologisch begründete Signale sind
- Falls keine der oben genannten Punkte nachgewiesen werden kann, sollte dieser Kandidat deprioritisiert/geschlossen werden, anstatt ihn auf unbestimmte Zeit zu halten

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

