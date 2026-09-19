---
layout: default
title: Alpelisib
parent: Nur Modellvorhersage (L5)
nav_order: 25
evidence_level: L5
indication_count: 1
---

# Alpelisib
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **1** 
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

# Alpelisib: Von fortgeschrittenem Brustkrebs zur pulmonalen Hypertonie

## Zusammenfassung in einem Satz

Alpelisib ist ein PI3Kα (PIK3CA)-selektiver Inhibitor, dessen strukturierte Felder zur ursprünglichen Indikation und zum Wirkmechanismus derzeit in den regulatorischen Unterlagen fehlen. Die unterstützende Literatur in diesem Evidenzpaket bezieht sich jedoch wiederholt auf seine Verwendung bei fortgeschrittenem Brustkrebs. Das TxGNN-Modell sagt eine mögliche neue Indikation in **pulmonaler Hypertonie** voraus (Score 99,03%), aber diese Vorhersage wird derzeit nur durch eine nicht relevante klinische Studie und zwei Tier-3-Publikationen unterstützt – von denen eine einen medikamenteninduzierten Lungentoxizitätssignal berichtet, der der Behandlungshypothese widerspricht. Angesichts des Fehlens von direkter Wirksamkeitsevidenz und einer ungelösten Sicherheitsdatenlücke ist dieser Kandidat noch nicht bereit, das erste Screening-Stadium zu überschreiten.

---

## Schnellübersicht

| Element | Inhalt |
|------|------|
| Ursprüngliche Indikation | Nicht in strukturierten regulatorischen Daten verfügbar (siehe Datenlücken); Literaturkontext deutet auf fortgeschrittenem HR+/HER2- Brustkrebs hin |
| Vorhergesagte neue Indikation | Pulmonale Hypertonie |
| TxGNN-Vorhersagescore | 99,03% |
| Evidenzstufe | L5 |
| Status auf dem deutschen Markt | ✗ Nicht vermarktet |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | Aussetzen |

---

## Warum ist diese Vorhersage vertretbar?

Detaillierte Wirkmechanismus-Daten für Alpelisib sind in den aktuellen regulatorischen Unterlagen nicht vorhanden (gekennzeichnet als eine Datenlücke mit hohem Schweregrad). Basierend auf den in diesem Paket verfügbaren Belegen ist Alpelisib ein PI3Kα (PIK3CA)-selektiver Inhibitor, und die begleitende Literatur und Studiendaten deuten darauf hin, dass es bei fortgeschrittenem HR+/HER2-negativem Brustkrebs verwendet wird.

Die mechanistische Begründung für die Vorhersage der Pulmonalen Hypertonie basiert auf der theoretisch bekannten Rolle des PI3K/Akt/mTOR-Signalwegs bei der Proliferation glatter Muskelzellen in den Lungengefäßen und dem Gefäßumbau – ein Weg, der präklinisch als potenzielles therapeutisches Ziel bei Pulmonalarterieller Hypertonie (PAH) erforscht wird. Diese Signalweg-assoziierte Beziehung ist wahrscheinlich der Treiber des hohen TxGNN-Scores.

Jedoch bleibt diese Verbindung rein mechanistisch. Es gibt keine direkten Belege für die Wirksamkeit von Alpelisib in PAH-Modellen oder bei Patienten. Noch wichtiger ist, dass die Literatur in diesem Paket das gegenteilige Signal zeigt: Alpelisib wurde berichtet, interstitielle Lungenkrankheit (ILD) zu induzieren, und die Hemmung des PI3Kα-Signalwegs wurde mit biventrikluärer Herzatrophie und rechtsventrikulärer Dysfunktion in präklinischen Modellen assoziiert. Beide Befunde stellen potenzielle Mechanismen für **Verschlimmerung** statt Behandlung der Pulmonalen Hypertonie dar, daher sollten die aktuellen Belege als Sicherheitswarnung statt als unterstützender Befund gelesen werden.

---

## Klinische Studienevidenz

| Studiennummer | Phase | Status | Teilnehmerzahl | Wichtigste Ergebnisse |
|---------|------|------|------|---------|
| [NCT06705504](https://clinicaltrials.gov/study/NCT06705504) | N/A | Abgeschlossen | 435 | Retrospektive Real-World-Studie von Ribociclib vs. **Alpelisib** bei fortgeschrittenem/metastasierendem HR+/HER2- Brustkrebs. **Nicht relevant für pulmonale Hypertonie** – die Studie bewertet eine andere Indikation (Brustkrebs) und ihr primärer Vergleicher ist Ribociclib, nicht Alpelisib; gekennzeichnet als Daten-Mismatch (Relevanzgrad C) und sollte nicht als unterstützender Beleg behandelt werden. |

---

## Literaturevidenz

| PMID | Jahr | Typ | Journal | Wichtigste Ergebnisse |
|------|-----|------|------|---------|
| [35730191](https://pubmed.ncbi.nlm.nih.gov/35730191/) | 2023 | Fallbericht | J Oncol Pharm Pract | Berichtet über Alpelisib-induzierte interstitielle Lungenkrankheit (ILD) bei einem Patienten mit fortgeschrittenem Brustkrebs – ein pulmonales Toxizitätssignal, keine Evidenz für Nutzen bei pulmonaler Hypertonie. |
| [31039672](https://pubmed.ncbi.nlm.nih.gov/31039672/) | 2019 | Präklinisch/Experimentell | J Am Heart Assoc | PI3Kα-Signalweg-Hemmung kombiniert mit Doxorubicin verursachte biventrikluäre Herzatrophie und rechtsventrikuläre Dysfunktion in einem Tiermodell – erhöht die Bedenken bezüglich Rechtsherzeffekte statt eine PAH-Behandlungslogik zu unterstützen. |

---

## Marktinformationen für Deutschland

Alpelisib hat derzeit keine Marktgenehmigung in Deutschland registriert (0 Zulassungen; Marktstatus: nicht vermarktet).

---

## Zytotoxizität

Die verfügbaren Belege (Literaturkontext, der auf „fortgeschrittenem Brustkrebs" verweist, und ein PI3Kα-selektiver Wirkmechanismus) deuten darauf hin, dass Alpelisib eine Krebstherapie ist, die als gezielte Therapie verwendet wird, nicht als konventionelles Zytotoxikum. Strukturierte DrugBank-Kategorisierung und Toxizitätsdaten sind in diesem Evidenzpaket nicht vorhanden.

| Element | Inhalt |
|------|------|
| Zytotoxizitätsklassifizierung | Gezielte Therapie (PI3Kα-Inhibitor) – kein konventionelles Zytotoxikum |
| Myelosuppressions-Risiko | Bitte beachten Sie die Warnhinweise und Vorsichtsmaßnahmen in der Fachinformation |
| Emetogenitätsklassifizierung | Bitte beachten Sie die Warnhinweise und Vorsichtsmaßnahmen in der Fachinformation |
| Überwachungselemente | Lungenfunktion/Atemwegssymptome (angesichts des ILD-Signals in der obigen Literatur); bitte beachten Sie die Fachinformation für die vollständige Überwachungsliste |
| Schutzmaßnahmen beim Umgang | Bitte beachten Sie die Warnhinweise und Vorsichtsmaßnahmen in der Fachinformation |

---

## Sicherheitsüberlegungen

Bitte beachten Sie die Fachinformation für Sicherheitsinformationen. Wichtige Warnungen, Kontraindikationen und Arzneimittelwechselwirkungsdaten für Alpelisib sind derzeit nicht in diesem Evidenzpaket verfügbar (dies ist als eine **blockierende** Datenlücke gekennzeichnet — DG001 —, die gelöst werden muss, bevor dieser Kandidat zur S1-Sicherheitsprüfung übergehen kann).

---

## Fazit und nächste Schritte

**Entscheidung: Aussetzen**

**Begründung:**
Keine direkten klinischen oder präklinischen Belege unterstützen die Wirksamkeit von Alpelisib bei pulmonaler Hypertonie – die einzige registrierte klinische Studie ist eine nicht relevante Brustkrebs-Studie, und die beiden verfügbaren Publikationen deuten auf ein pulmonales/kardiakales Toxizitätssignal statt auf therapeutischen Nutzen hin. Dies wird durch eine blockierende Datenlücke in den TFDA/EU-Fachinformationen-Sicherheitsdaten verschärft, die verhindert, dass der Kandidat zur S1-Sicherheitsevaluationsstufe voranschreitet.

**Um weiterzugehen, ist folgendes erforderlich:**
- Fachinformation Warnungen/Kontraindikationen Daten (DG001, blockierend – erforderlich für S1-Sicherheitsprüfung)
- Bestätigter Wirkmechanismus und ursprüngliche genehmigte Indikation (DG002, hoch)
- DrugBank-Medikamentenkategorisierung und Toxizitätsklassifizierungsdaten
- Arzneimittelwechselwirkungsprofil (DDI-Profil)
- Direkte präklinische oder klinische Belege für Alpelisib-Aktivität bei pulmonaler Hypertonie/PAH-Modellen, insbesondere zur Adressierung der oben identifizierten ILD- und Rechtsventrikulär-Dysfunktions-Sicherheitssignale

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

