---
layout: default
title: Turoctocog Alfa
parent: Nur Modellvorhersage (L5)
nav_order: 415
evidence_level: L5
indication_count: 10
---

# Turoctocog Alfa
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **10** 
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

# Turoctocog Alfa: Von der Gerinnungsfaktor-Substitutionstherapie zur Primary Release Disorder of Platelets

## Zusammenfassung in einem Satz

Turoctocog alfa ist ein rekombinantes Faktor-VIII-Präparat. In diesem Evidence Pack stellt DrugBank weder die genehmigten Indikationen noch detaillierte Wirkmechanismen bereit (Datenlücke). Aus der Modell-Rationale ist jedoch bekannt, dass die klinisch etablierte Anwendung die Gerinnungsfaktor-VIII-Substitutionstherapie ist. Das TxGNN-Modell prognostiziert eine mögliche Wirksamkeit bei **Primary Release Disorder of Platelets** (Primäre Blutplättchen-Sekretionsstörung). Derzeit gibt es jedoch **0 klinische Versuche** und **0 Publikationen** zur Unterstützung, und das Modell selbst hat bereits deutlich gemacht, dass dieser Zusammenhang biologisch unplausibel ist.

---

## Schnellübersicht

| Punkt | Inhalt |
|-------|--------|
| Ursprüngliche Indikation | Datenlücke (DrugBank original_indications leer; in Taiwan nicht vermarktet, keine Zulassungsdaten; bekannte klinische Anwendung ist Faktor-VIII-Substitutionstherapie) |
| Prognostizierte neue Indikation | Primary release disorder of platelets |
| TxGNN-Prognose-Score | 99,99 % (ursprünglicher Score 0.9999269, Rang 141) |
| Evidenzstufe | L5 (nur Modellprognose, keine klinischen Versuche oder Publikationen) |
| Marktstatus in Taiwan | Nicht vermarktet |
| Anzahl der Genehmigungen | 0 |
| Empfohlene Entscheidung | Hold |

---

## Warum ist diese Prognose plausibel?

Derzeit sind keine detaillierten Wirkmechanismus-Daten (MOA) verfügbar. Basierend auf verfügbaren öffentlichen Informationen gehört Turoctocog alfa zur Klasse der rekombinanten Faktor-VIII-Präparate, deren Wirksamkeit bei Faktor-VIII-Mangel (z. B. Hämophilie A) als Substitutionstherapie klinisch nachgewiesen ist. Der Wirkmechanismus besteht darin, das fehlende endogene Faktor-VIII-Protein zu ersetzen und so die Tenase-Komplexfunktion wiederherzustellen, um die Gerinnung zu fördern.

In diesem Evidence Pack hat das Modell selbst für diese Top-1-Prognose jedoch bereits klargestellt: Die Pathologie der Primary Release Disorder of Platelets liegt im Defekt der Blutplättchen-Granula-Sekretion, nicht in einer Störung der Gerinnungsfaktor-Pfade. Zwischen Faktor VIII und dem Blutplättchen-Sekretionsmechanismus besteht **keine direkte physiologische Verbindung**. Mit anderen Worten: Dieser hohe Prognose-Score ist das Ergebnis der Mustererkennung durch das TxGNN-Graphen-Neuronennetz, ohne mechanistische Begründung und ohne klinische oder Publikationsevidenz.

Bemerkenswert ist, dass der in diesem Evidence Pack aufgeführte fünfte Kandidat – „Acquired coagulation factor deficiency" (erworbener Gerinnungsfaktor-Mangel) – eine offensichtlich stärkere mechanistische Assoziation aufweist. Falls dieser Erkrankungsbegriff den erworbenen Faktor-VIII-Mangel einschließt, würde er direkt der bekannten Pharmakologie von Turoctocog alfa entsprechen. Dies bleibt jedoch eine Extrapolation auf Arzneimittelklassen-Ebene der bekannten Anwendungen und keine evidenzgestützte Aussage für diesen spezifischen Wirkstoff. Die Evidenzstufe erreicht nur L4 (Research-Question-Phase) und ist nicht ausreichend, um eine aktive Verfolgung zu unterstützen.

---

## Weitere prognostizierte Indikationen (Rang 2–10) – Schnellübersicht

Um die Gesamtheit der TxGNN-Prognosen vollständig darzustellen, werden die übrigen 9 Kandidatenindikationen wie folgt zusammengefasst:

| Rang | Erkrankungsname | Score | Evidenzstufe | Empfehlung | Anmerkungen |
|------|-----------------|-------|--------------|------------|-----------|
| 2 | Pseudo-von-Willebrand disease | 99,99 % | L5 | Hold | Blutplättchen-GPIb-Rezeptor-Defekt, Wirkmechanismus spekulativ, keine klinischen Daten |
| 3 | Glanzmann thrombasthenia | 99,99 % | L5 | Hold | GPIIb/IIIa-Defekt; Faktor VIII beeinflusst Blutplättchen-Membran-Glykoprotein-Funktion nicht |
| 4 | Scott syndrome | 99,95 % | L5 | Hold | Phospholipid-Externalisierungsdefekt; Faktor VIII kann den zugrunde liegenden Defekt nicht beheben |
| 5 | Acquired coagulation factor deficiency | 99,95 % | L4 | Research Question | Einziger Kandidat mit direktem Wirkmechanismus-Match, aber ohne arzneimittelspezifische Evidenz |
| 6 | Bleeding diathesis due to collagen receptor defect | 99,91 % | L5 | Hold | GPVI-Defekt und Gerinnungsfaktor-Pfade sind unabhängig |
| 7 | Hemorrhagic disorder due to constitutional thrombocytopenia | 99,91 % | L5 | Hold | Thrombozytopenie; Faktor VIII kann die Blutplättchenzahl nicht erhöhen |
| 8 | Flood factor deficiency | 99,61 % | L5 | Hold | Erkrankungsname ist kein standardisierter medizinischer Begriff; vermutlich Datentranslationsfehler |
| 9 | Thrombotic thrombocytopenic purpura | 99,54 % | L5 | **Hold (Sicherheit ausgeschlossen)** | ⚠️ TTP ist eine thrombotische Erkrankung; die Gabe des pro-koagulierenden Faktor VIII könnte die Mikrothrombenbildung verschärfen; der Wirkmechanismus ist der Erkrankungspathologie **entgegengesetzt**. Sollte prioritär ausgeschlossen werden; keine weitere Bewertung empfohlen |
| 10 | Hereditary thrombocytosis with transverse limb defect | 99,52 % | L5 | Hold | Seltenes entwicklungs-assoziiertes Syndrom ohne plausible physiologische Beziehung zu Faktor VIII |

**Sicherheits-Flagge**: Rang 9, Thrombotic Thrombocytopenic Purpura (TTP), ist eine Gegenindikations-Kandidatin. Die Verabreichung von Gerinnungsfaktoren könnte die Mikrogefäß-Thrombose-Pathologie verschärfen. Sollte auf die Liste der nicht zu verfolgenden Kandidaten gesetzt werden, um Missbrauch in künftiger Forschung zu vermeiden.

---

## Klinische Versuchsevidenz

Derzeit keine entsprechenden Versuchsregistrierungen vorhanden.

---

## Publikationsevidenz

Derzeit keine entsprechenden Publikationsdaten vorhanden.

---

## Marktinformation Taiwan

Turoctocog alfa ist derzeit **in Taiwan nicht vermarktet** und hat keine Zulassungsdaten.

---

## Sicherheitserwägungen

Siehe Fachinformation (Warnhinweise und Vorsichtsmaßnahmen).

Ergänzende Anmerkung: Dieses Evidence Pack kennzeichnet die BfArM-Fachinformationen-Warnhinweise und Kontraindikationen als **Blocking-Level-Datenlücke (DG001)**. Solange diese Lücke nicht geschlossen ist, kann dieser Wirkstoff die S1-Sicherheitsprüfungsphase nicht einleiten. Die Wirkmechanismus-Daten (DG002) sind ebenfalls eine High-Level-Lücke, die die Zuverlässigkeit der mechanistic-link-Analyse einschränkt.

---

## Fazit und nächste Schritte

**Entscheidung: Hold**

**Begründung:**
- Die Top-1-Prognose (Primary release disorder of platelets) hat eine Evidenzstufe von L5 ohne klinische Versuchs- oder Publikationsevidenz, und das Modell selbst hat bereits klargestellt, dass die biologische Plausibilität schwach ist.
- In Taiwan nicht vermarktet, keine Zulassungsdaten verfügbar, und BfArM-Sicherheitsdaten sind eine Blocking-Level-Lücke; eine Vollendung der S1-Sicherheitsprüfung ist noch nicht möglich.

**Für einen Fortschritt erforderlich:**
- BfArM-Fachinformationen-Warnhinweise und Kontraindikationen (DG001, Blocking, erfordert PDF-Fachinformations-Download und -Analyse)
- DrugBank-Wirkmechanismus (MOA)-Detaildaten (DG002, High, erfordert Abfrage der DrugBank-API)
- Falls die Verfolgung von Rang-5-Kandidat (Acquired coagulation factor deficiency) in Betracht gezogen wird: arzneimittelspezifische klinische Versuchs- oder Publikationsevidenz für diese Indikation erforderlich, nicht nur Klassenextrapolation
- Explizites Ausschließen von Rang-9-Kandidat (TTP) aus allen künftigen Entwicklungsprozessen, um Sicherheitsrisiko durch entgegengesetzte Wirkmechanismus-Richtung zu vermeiden

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

