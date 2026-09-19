---
layout: default
title: Orbifloxacin
parent: Nur Modellvorhersage (L5)
nav_order: 282
evidence_level: L5
indication_count: 10
---

# Orbifloxacin
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

# Orbifloxacin: Von veterinärmedizinischen Bakterieninfektionen zu Herzerkrankungen

## Zusammenfassung in einem Satz

Orbifloxacin ist ein Fluorchinolon-Antibiotikum, das für die veterinärmedizinische Verwendung entwickelt wurde (keine bestätigte Indikation beim Menschen oder Wirkmechanismus-Daten in diesem Evidenzpaket). Die Top-Rangfolge-Vorhersage des TxGNN-Modells ist **Herzerkrankung**, aber dieser Kandidat hat **keine klinischen Studien** und **keine relevante Literatur**, und die mechanistische Überprüfung des Evidenzpakets kennzeichnet ihn als wahrscheinlich Modellrauschen – Fluorchinolone sind mechanistisch nicht mit Herzerkrankungen verbunden und sind stattdessen für kardiovaskuläre Sicherheitsrisiken bekannt (QT-Verlängerung).

---

## Schnellübersicht

| Element | Inhalt |
|---------|--------|
| Ursprüngliche Indikation | Nicht dokumentiert im Evidenzpaket (veterinärmedizinisches Fluorchinolon-Antibiotikum gemäß Wirkstoffklasse) |
| Prognostizierte neue Indikation | Herzerkrankung |
| TxGNN-Vorhersage-Score | 99.94% |
| Evidenzstufe | L5 |
| Marktstatus Deutschland | ✗ Nicht vermarktet |
| Anzahl der Genehmigungen | 0 |
| Empfohlene Entscheidung | Aussetzen |

---

## Warum ist diese Vorhersage angemessen?

Detaillierte Daten zum Wirkmechanismus sind für Orbifloxacin in diesem Evidenzpaket nicht verfügbar. Basierend auf bekannten Wirkstoffklassen-Informationen ist Orbifloxacin ein Fluorchinolon-Antibiotikum, das bakterielle DNA-Gyrase und Topoisomerase IV hemmt – ein Mechanismus ohne etablierte biologische Verbindung zu Herzerkrankungen.

Wichtiger ist, dass die mit diesem Kandidaten bereitgestellte Umpositionierungs-Rationale die Vorhersage selbst als wahrscheinlich **Modellrauschen** kennzeichnet: Fluorchinolone als Wirkstoffklasse sind mit einem bekannten kardiovaskulären Sicherheitssignal verbunden (QT-Intervall-Verlängerung und Kardiotoxizität), was das Gegenteil einer therapeutischen Begründung für Herzerkrankungen ist. Alle zehn der Top-bewerteten Vorhersagen von TxGNN für dieses Arzneimittel (Herzerkrankung, mehrere angeborene/chromosomale Syndrome, Herzklappenstörungen) weisen keine unterstützenden klinischen Studien oder Literatur-Evidenzen auf, und die Rationale für jede unabhängig voneinander kommt zu dem Schluss, dass es keine plausible mechanistische Verbindung gibt.

Angesichts dessen sollte die Vorhersage nicht als echtes Umpositionierungs-Signal interpretiert werden, sondern als ein Artefakt des Embedding-Raums, das zu diesem Zeitpunkt keine weitere mechanistische Rechtfertigung erfordert.

---

## Klinische Studien-Evidenz

Derzeit sind keine verwandten klinischen Studien registriert.

---

## Literatur-Evidenz

Derzeit ist keine verwandte Literatur verfügbar.

*(Hinweis: eine nicht verwandte pharmakokinetische Studie, PMID [22029792](https://pubmed.ncbi.nlm.nih.gov/22029792/), wurde für eine niedriger bewertete, mechanistisch nicht verwandte Vorhersage – „Störung der Fukoglykoosan-Synthese" – zurückgegeben und unterstützt nicht die Herzerkrankungs-Indikation.)*

---

## Marktstatus Deutschland

Orbifloxacin hat keine Vermarktungsgenehmigungen in Deutschland (0 Lizenzen verzeichnet); das Arzneimittel ist derzeit nicht vermarktet.

---

## Sicherheitsüberlegungen

Weitere Sicherheitsinformationen finden Sie in der Packungsbeilage. TFDA-Etikett-Warnungen/Kontraindikationen und DDI-Daten sind derzeit nicht verfügbar (gekennzeichnet als blockierender Datenlücke im Quell-Evidenzpaket), was selbst eine Sicherheits-Vor-Screening für diesen Kandidaten ausschließt.

---

## Schlussfolgerung und nächste Schritte

**Entscheidung: Aussetzen**

**Rationale:**
Die Top-Vorhersage (Herzerkrankung, Score 99.94%) hat keine unterstützenden klinischen Studien oder Literatur, und die mechanistische Analyse des Evidenzpakets selbst kennzeichnet sie als wahrscheinlich Modellrauschen, widersprochen durch das bekannte Kardiotoxizitäts-Risiko von Fluorchinolonen. Alle anderen Top-10-Vorhersagen sind ähnlich nicht unterstützte angeborene/genetische Syndrome ohne plausible Verbindung zum antibakteriellen Mechanismus des Arzneimitels. Das Arzneimittel ist auch nicht in Deutschland vermarktet und hat keine bestätigte Indikation beim Menschen.

**Folgendes ist erforderlich, um fortzufahren:**
- TFDA/offizielle Etikett-Daten (Warnungen, Kontraindikationen) zur Behebung der blockierenden Datenlücke (DG001)
- Bestätigter Wirkmechanismus über DrugBank (DG002)
- Jegliche reale oder präklinische Evidenz, die Fluorchinolon-Pharmakologie spezifisch mit Herz-Kreislauf-Erkrankungen verbindet, bevor dieser Kandidat erneut berücksichtigt wird
- Angesichts der aktuellen Ergebnisse wird empfohlen, diesen Kandidaten in der Umpositionierungs-Pipeline ohne neue Evidenz zu deprioritisieren

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

