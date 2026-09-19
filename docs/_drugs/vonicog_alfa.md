---
layout: default
title: Vonicog Alfa
parent: Nur Modellvorhersage (L5)
nav_order: 429
evidence_level: L5
indication_count: 10
---

# Vonicog Alfa
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

# Vonicog Alfa: Von unbestätigter Originalindikation zur primären Sekretionstörung der Thrombozyten

## Zusammenfassung in einem Satz

> Die Originalindikation von Vonicog alfa ist in diesem Nachweispaket nicht dokumentiert (keine genehmigten Indikationen in den Dateien, Wirkmechanismus wird als Datenlücke gekennzeichnet).
> Die am höchsten bewertete Vorhersage des TxGNN-Modells ist **Primäre Sekretionstörung der Thrombozyten**,
> doch dieses Signal wird durch **0 klinische Studien** und **0 Publikationen** gestützt, und die eigene mechanistische Begründung des Modells kennzeichnet es als wahrscheinlich eine **falsch-positive semantische Assoziation** statt einer echten pharmakologischen Verbindung.

---

## Kurzübersicht

| Artikel | Inhalt |
|---------|--------|
| Originalindikation | Nicht verfügbar — keine genehmigten Indikationen in den Dateien für dieses Arzneimittel im aktuellen Datensatz |
| Vorhergesagte neue Indikation | Primäre Sekretionstörung der Thrombozyten |
| TxGNN-Vorhersage-Score | 99.98% |
| Evidenzgrad | L5 |
| Marktstatus in Deutschland | Nicht vermarktet |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | Zurückstellen |

---

## Warum ist diese Vorhersage angemessen?

Derzeit sind detaillierte Daten zum Wirkmechanismus für Vonicog alfa nicht verfügbar (als Datenlücke mit hohem Schweregrad gekennzeichnet, DG002 — ausstehende Abfrage über die DrugBank-API). Allerdings deuten mechanistische Beschreibungen, die an anderer Stelle in diesem Nachweispaket vorhanden sind (in der Begründung für andere Kandidaten-Indikationen, z. B. Rang 4 „Hämophilie"), darauf hin, dass Vonicog alfa ein **rekombinanter humaner von-Willebrand-Faktor (rVWF)** ist, dessen Grundmechanismus die Wiederherstellung der VWF-Plasmakonzentration zur Förderung der Thrombozytenadhäsion und der Hämostase ist und sekundär die Stabilisierung des endogenen Faktor VIII umfasst.

Speziell für die am höchsten bewertete Vorhersage — **primäre Sekretionstörung der Thrombozyten** — argumentiert die mechanistische Analyse des Nachweispakets selbst **gegen** die biologische Plausibilität: Diese Störung (z. B. Thrombozytenspeicherkrankheit) entsteht durch einen Defekt in der Thrombozytengranula-Sekretion, nicht durch VWF-Plasmakonzentration oder -funktion. Die Begründung besagt ausdrücklich, dass der hohe TxGNN-Vorhersage-Score wahrscheinlich einen gemeinsamen Semantik-Cluster zum Thema „Blutungsneigung" im Knowledge Graph widerspiegelt, anstelle eines echten gemeinsamen pharmakologischen Mechanismus, weshalb dieser Kandidat die niedrigste Evidenzklasse (L5) aufweist.

Im Gegensatz dazu haben andere Kandidaten weiter unten auf dieser gleichen Vorhersageliste (insbesondere Rang 4 „Hämophilie" und Rang 6/7 für von-Willebrand-Erkrankungsvarianten) eine viel direktere und verteidigbare mechanistische Verbindung zur rVWF-Ersatztherapie und werden durch tatsächliche Phase-3-Studiendaten und Literaturbelege gestützt — siehe Fazit für Details.

---

## Evidenz aus klinischen Studien

Derzeit keine zugehörigen klinischen Studien registriert

---

## Literaturbelege

Derzeit keine zugehörige Literatur verfügbar

---

## Marktinformationen für Deutschland

Vonicog alfa ist **derzeit nicht in Deutschland vermarktet** (`market_status: Not marketed`) und hat **0 registrierte Zulassungen**. Es sind keine Produkt- oder Lizenzunterlagen zur Zusammenfassung verfügbar.

---

## Sicherheitsüberlegungen

Weitere Sicherheitsinformationen entnehmen Sie bitte der Packungsbeilage.

*(Hinweis: TFDA-Etikettenwarnungen und Kontraindikationen sind in diesem Nachweispaket als blockierende Datenlücke gekennzeichnet — DG001 — was bedeutet, dass die Sicherheitsbewertung (S1) nicht offiziell fortgesetzt werden kann, bis diese behoben ist.)*

---

## Schlussfolgerung und nächste Schritte

**Entscheidung: Zurückstellen**

**Begründung:**
Die am höchsten bewertete vorhergesagte Indikation (primäre Sekretionstörung der Thrombozyten) hat keine Unterstützung durch klinische Studien oder Literatur, wird mit der niedrigsten Evidenzklasse (L5) bewertet, und die eigene mechanistische Begründung des Modells deutet darauf hin, dass die Vorhersage wahrscheinlich eine trügerische semantische Assoziation darstellt statt eines echten pharmakologischen Signals. Unter Berücksichtigung der Tatsache, dass das Arzneimittel in Deutschland nicht vermarktet wird und die Sicherheits-Etikettierungsdaten eine blockierende Datenlücke darstellen, gibt es derzeit keine Grundlage, um diesen spezifischen Kandidaten weiterzuverfolgen.

**Um fortfahren zu können, wird Folgendes benötigt:**
- DG001 (blockierend) beheben: Beschaffung und Analyse des TFDA/EU-Produktetiketts für Warnhinweise und Kontraindikationen, bevor eine S1-Sicherheitsbewertung durchgeführt werden kann
- DG002 (Hoch) beheben: Wirkmechanismus über die DrugBank-API bestätigen, um die Aussagen zur mechanistischen Plausibilität zu validieren
- Die formal genehmigten Originalindikation(en) des Arzneimittels, die in diesem Datensatz derzeit fehlen, bestätigen
- Falls für dieses Arzneimittel eine Neupositionierung verfolgt wird, sollte die Bewertung zu höherrangigeren Kandidaten umgelenkt werden, die bereits in dieser gleichen Vorhersage-Menge vorhanden sind — insbesondere **Rang 4 (Hämophilie, L2, 4 Phase-3-Studien + 1 Tier-1-RCT)**, wobei zu beachten ist, dass die zugrunde liegende Studienpopulation tatsächlich eine von-Willebrand-Erkrankung statt einer klassischen Hämophilie A/B darstellt; daher muss die Indikationsbezeichnung vor der Anwendung überprüft werden

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

