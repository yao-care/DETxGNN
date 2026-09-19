---
layout: default
title: Entacapone
parent: Nur Modellvorhersage (L5)
nav_order: 147
evidence_level: L5
indication_count: 10
---

# Entacapone
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

# Entacapone (Entacapon): Von der Parkinson-Krankheit zur PLA2G6-assoziierten Neurodegeneration

## Einzeilenzusammenfassung

Entacapone ist ein COMT-(Catechol-O-Methyltransferase-)Hemmer, der als Zusatztherapie zu Levodopa bei der Parkinson-Krankheit angewendet wird.
Das TxGNN-Modell sagt vorher, dass es wirksam sein könnte gegen **PLA2G6-assoziierte Neurodegeneration**,
wird aber derzeit durch **0 klinische Studien** und **0 Publikationen** unterstützt — es ist eine reine Modellvorhersage ohne reale Evidenz.

## Schnelläberblick

| Element | Inhalt |
|---------|--------|
| Ursprüngliche Indikation | Parkinson-Krankheit, Zusatztherapie zu Levodopa/Carbidopa (COMT-Hemmer) — basierend auf bekanntem Wirkstoffklassenhintergrund; nicht durch Zulassungsdaten in diesem Evidenzpaket bestätigt |
| Vorhergesagte neue Indikation | PLA2G6-assoziierte Neurodegeneration |
| TxGNN-Vorhersage-Score | 99.76% |
| Evidenzstufe | L5 |
| Marktstatus in Deutschland | Nicht im Handel (Nicht im Handel) |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | Halten |

## Warum ist diese Vorhersage vernünftig?

Derzeit sind detaillierte Wirkmechanismus-Daten in diesem Evidenzpaket nicht verfügbar (gekennzeichnet als High-Severity-Datenlücke `DG002`). Basierend auf bekanntem Hintergrundwissen ist Entacapone ein peripherer COMT-Hemmer, der den enzymatischen Abbau von Levodopa blockiert und seine Verfügbarkeit im Zentralnervensystem verlängert. Seine bewiesene Wirksamkeit liegt in der Verringerung von motorischen Fluktuationen („Wearing-off") bei der Parkinson-Krankheit, wenn es zusammen mit Levodopa verabreicht wird.

PLA2G6-assoziierte Neurodegeneration (PLAN, einschließlich infantiler neuroaxonaler Dystrophie und ihrer atypischen spätmanifesten Formen) ist eine unterschiedliche Krankheit, die durch Verlust der PLA2G6-Phospholipase-A2-Funktion und Eisenakkumulation im Gehirn verursacht wird. Einige atypische, spätmanifeste PLAN-Subtypen können sich mit parkinsonismus-ähnlicher Rigidität und Dystonie präsentieren, was der einzige Punkt der klinischen Überlappung mit der zugelassenen Verwendung von Entacapone ist — wenn solche Patienten mit Levodopa behandelt würden, könnte Entacapone theoretisch eine adjuvante Rolle spielen.

Dies ist jedoch eine indirekte, schlussfolgende Verbindung. Die Kernpathologie des PLA2G6-Mangels (Phospholipase-Dysfunktion, Eisenablagerung) überlappt nicht mechanistisch mit dem COMT-/Dopamin-Stoffwechsel-Signalweg, den Entacapone anzielt. Der hohe TxGNN-Score spiegelt wahrscheinlich eher die Nähe zwischen „Neurodegeneration"- und „Bewegungsstörungs"-Knoten im zugrunde liegenden Wissensgraph wider als eine echte pharmakologische Beziehung. Keine klinischen Studien oder Literatur unterstützen derzeit diese spezifische Wirkstoff-Krankheits-Paarung.

## Klinische Studienevidenz

Derzeit sind keine verwandten klinischen Studien registriert.

## Literaturevidenz

Derzeit ist keine verwandte Literatur verfügbar.

## Sicherheitsaspekte

Bitte beachten Sie die Packungsbeilage für Sicherheitsinformationen.

*(Hinweis: TFDA/BfArM-Etikettenwarnungen und Kontraindikationen sind in diesem Evidenzpaket als blockierende Datenlücke (`DG001`) gekennzeichnet — dies muss vor jeder Sicherheitsvorabenbewertung gelöst werden.)*

## Schlussfolgerung und nächste Schritte

**Entscheidung: Halten**

**Begründung:**
Die Evidenzstufe ist L5 (nur Modellvorhersage) — es gibt keine klinischen Studien, keine Publikationen und keinen direkten Molekülmechanismus, der die COMT-Hemmungsaktivität von Entacapone mit der Kernpathologie der PLA2G6-assoziierten Neurodegeneration verbindet. Das Evidenzpaket selbst kennzeichnet dies als wahrscheinliches Wissensgrafen-Einbettungsartefakt statt eines echten pharmakologischen Signals.

**Um fortzufahren, wird Folgendes benötigt:**
- Behebung von `DG001` (TFDA/BfArM-Packungsbeilage-Warnungen und Kontraindikationen) — blockiert derzeit jede Sicherheitsvorabenbewertung
- Behebung von `DG002` (bestätigte Wirkmechanismus-Daten von DrugBank), um die mechanistische Plausibilität ordnungsgemäß zu bewerten
- Präklinische/mechanistische Studien, die speziell Entacapone in PLA2G6-Mangel-Krankheitsmodellen testen
- Bestätigung, ob atypische spätmanifeste PLAN-Patienten mit parkinsonismus-ähnlichen Merkmalen eine klinisch bedeutsame Untergruppe darstellen, die adressiert werden sollte

---

### Ergänzende Anmerkung: Andere Kandidaten in diesem Evidenzpaket

Dieser Bericht beschränkt sich auf die Rang-1-Vorhersage, wie durch das Berichtsformat angegeben, aber das Evidenzpaket ordnet 10 kandidatische Indikationen für Entacapone ein, und die stärksten mechanistischen und Evidenzsignale befinden sich **nicht** auf Rang 1. Drei andere Kandidaten wurden mit Entscheidungsstufe S1 („Forschungsfrage") statt Halten bewertet und können einer unabhängigen Bewertung bedürfen:

| Rang | Krankheit | TxGNN-Score | Evidenzstufe | Anmerkungen |
|------|-----------|-------------|--------------|-------------|
| 4 | Paralysis agitans, Juvenile, of Hunt | 99,60% | L4 | Historischer Name für Früh-Onset-Parkinson/Parkinson-Plus-Syndrom — direkte mechanistische Überlappung mit der zugelassenen Verwendung von Entacapone, aber keine Studien/Literatur, die diese spezifische Early-Onset-Untergruppe ansprechen. |
| 7 | Lewy-Körper-Demenz | 99,25% | L4 | Gleiche α-Synucleinopathie-Familie wie die Parkinson-Krankheit; 1 Phase-1-Bildgebungsstudie ([NCT04246437](https://clinicaltrials.gov/study/NCT04246437)) und 3 Literatureinträge existieren, obwohl keine davon Entacapone direkt testen. |
| 10 | Progressive supranukleäre Lähmung–Corticobasales Syndrom | 99,04% | L4 | Atypischer Parkinsonismus (Tau-getrieben, nicht Synuclein); 1 nichtinterventionelle Beobachtungs-Ganganalyse-Studie ([NCT02994719](https://clinicaltrials.gov/study/NCT02994719)) existiert. |

Alle zehn Kandidaten bleiben bei S0/S1 (Halten oder Forschungsfrage) — keiner rechtfertigt derzeit eine Entscheidung „Weitergehen" oder „Mit Schutzmaßnahmen fortfahren". Wenn weitere Investition gerechtfertigt ist, sind Ränge 4, 7 und 10 bessere Ausgangspunkte als Rang 1, angesichts ihrer stärkeren mechanistischen Nähe zu Entacapones etabliertem dopaminergem Signalweg.

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

