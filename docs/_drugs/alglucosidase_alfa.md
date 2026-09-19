---
layout: default
title: Alglucosidase Alfa
parent: Nur Modellvorhersage (L5)
nav_order: 22
evidence_level: L5
indication_count: 10
---

# Alglucosidase Alfa
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

# Alglucosidase Alfa: Von Pompe-Krankheit zu Adult Polyglucosan Body Disease

## Zusammenfassung in einem Satz

Alglucosidase alfa ist ein Enzymersatztherapie-Präparat, das Säure-α-Glukosidase (GAA) liefert und ursprünglich für die Pompe-Krankheit (Glykogenspeicherkrankheit Typ II) entwickelt wurde. Das TxGNN-Modell sagt einen möglichen Effekt auf die **Adult Polyglucosan Body Disease (APBD)** voraus, dies wird jedoch derzeit durch **0 klinische Studien** und **0 Veröffentlichungen** gestützt, und die mechanistische Analyse des Evidence-Pakets kommt zu dem Ergebnis, dass das ursächliche Enzym in APBD (GBE1) nicht mit GAA verwandt ist — was darauf hindeutet, dass die Vorhersage eher ein Knowledge-Graph-Artefakt als ein echtes pharmakologisches Signal sein könnte.

---

## Schnellübersicht

| Element | Inhalt |
|---------|--------|
| Ursprüngliche Indikation | Pompe-Krankheit (Glykogenspeicherkrankheit Typ II, GAA-Mangel) — aus dem Rationalisierungstext in diesem Evidence-Paket abgeleitet, da keine formalen `original_indications` oder Zulassungstexte zurückgegeben wurden |
| Vorhergesagte neue Indikation | Adult Polyglucosan Body Disease |
| TxGNN-Vorhersage-Score | 99.47% |
| Evidence-Level | L5 (nur Modellvorhersage, keine unterstützenden Studien) |
| Marktstand Deutschland | Nicht vermarktet (Nicht vermarktet) |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | Aussetzen |

---

## Warum ist diese Vorhersage vertretbar?

Detaillierte Wirkmechanismus-Daten sind in diesem Paket als Datenlücke (DG002) gekennzeichnet, daher ist kein formales MOA-Datensatz verfügbar. Allerdings bestätigt der Rationalisierungstext des Evidence-Pakets unabhängig die bekannte Biologie des Arzneimittels: Alglucosidase alfa ist ein rekombinantes Säure-α-Glukosidase (GAA)-Enzymersatzpräparat, das zur Korrektur der lysosomalen Glykogenansammlung bei der Pompe-Krankheit verwendet wird.

Die vorhergesagte Indikation, Adult Polyglucosan Body Disease, ist ebenfalls eine Glykogenstoffwechselstörung — wird aber durch einen **Mangel des Glykogen-Verzweigungsenzyms (GBE1)** verursacht, nicht durch GAA-Mangel. Nach dem bereitgestellten Rationalisierungstext handelt es sich um einen grundlegend unterschiedlichen enzymatischen Stoffwechselweg: Alglucosidase alfa ersetzt GAA, was einen GBE1-Defekt nicht korrigiert. Der gleiche Widerspruch gilt für Vorhersagen #2 und #3 (GSD IV / GBE1-bezogene Störungen).

Für Vorhersagen #4–#10 (angeborenes Entropium, Ektropium, Horner-Syndrom, Ptosis-Stimmband-Lähmungssyndrom, angeborene kraniofaziale Dysinnervationsstörung, Epiblepharon, Ptosis-Strabismus-ektopisches Augensyndrom) ist der Rationalisierungstext explizit darin, dass es sich um Augenlid-/okuläre oder kraniofaziale Entwicklungsstörungen mit **keinem bekannten biologischen Zusammenhang** zu lysosomaler Glykogenspeicherung oder GAA-Aktivität handelt. Der Rationalisierungstext selbst charakterisiert diese als wahrscheinliche Artefakte der Phänotyp-Name-Ähnlichkeit im Knowledge Graph (z. B. gemeinsame Deskriptoren wie Ptosis/Muskelschwäche, die oberflächlich mit der myopathischen Präsentation der Pompe-Krankheit überlappen), eher als ein echtes mechanistisches Signal.

**Fazit dieses Abschnitts**: Basierend auf der eigenen mechanistischen Bewertung des Evidence-Pakets haben derzeit keine der Top-10-TxGNN-Vorhersagen für dieses Arzneimittel eine vertretbare pharmakologische Begründung. Die hohen TxGNN-Scores (99.1–99.5%) spiegeln die Modellzuversicht im Einbettungsraum wider, nicht bestätigte biologische Plausibilität.

---

## Klinische Studienevidenz

Derzeit sind keine verwandten klinischen Studien registriert.

(Bestätigt über `query_log`: ClinicalTrials.gov- und ICTRP-Suchanfragen für Alglucosidase alfa gegen alle 10 vorhergesagten Indikationen, einschließlich Adult Polyglucosan Body Disease, ergaben am 2026-04-20 0 Ergebnisse.)

---

## Literaturevidenz

Derzeit sind keine relevanten Literaturquellen verfügbar.

(Bestätigt über `query_log`: PubMed-Suchanfragen für Alglucosidase alfa gegen alle 10 vorhergesagten Indikationen ergaben am 2026-04-20 0 Ergebnisse.)

---

## Informationen zum Markt Deutschland

Alglucosidase alfa wird derzeit **nicht vermarktet** in Deutschland nach diesem Evidence-Paket (`market_status: Not marketed`), mit **0 registrierten Zulassungen**. Es stehen keine Lizenzunterlagen zur Verfügung, um zugelassene Indikationstexte zu zitieren.

---

## Sicherheitsaspekte

Die TFDA/Packungsbeilage-Warnhinweise und Kontraindikationsdaten wurden **noch nicht ermittelt** — dies ist im Evidence-Paket als Datenlücke vom Typ **Blocking** (DG001) gekennzeichnet, was bedeutet, dass dieser Kandidat noch nicht in die S1-Sicherheits-Vorbewertungsphase fortschreiten kann. Es wurden keine DDI-Daten gefunden (Abfragestatus: `not_found`).

> Bitte beachten Sie die Packungsbeilage für Sicherheitsinformationen, sobald das TFDA-Quelldokument abgerufen wurde.

---

## Schlussfolgerung und nächste Schritte

**Entscheidung: Aussetzen**

**Begründung:**
Jede der 10 TxGNN-vorhergesagten Indikationen für dieses Arzneimittel weist ein L5-Evidence-Level (nur Modellvorhersage) auf, null klinische Studien und null Literatur. Was noch wichtiger ist: Die mechanistische Analyse des Evidence-Pakets selbst kommt zu dem Ergebnis, dass der führende Kandidat (und #2, #3) ein anderes ursächliches Enzym (GBE1) betreffen als dasjenige, das Alglucosidase alfa anspricht (GAA), und die restlichen Kandidaten (#4–#10) augenheilkundliche/neuromuskuläre Entwicklungsstörungen ohne plausible Verbindung zum Glykogenstoffwechsel sind. Kombiniert mit einer Blocking-Sicherheitsdatenlücke (TFDA-Warnhinweise/Kontraindikationen noch nicht abgerufen) und null Marktautorisierungen in Deutschland, gibt es derzeit keine Grundlage, um diesen Kandidaten voranzubringen.

**Um fortzufahren, ist Folgendes erforderlich:**
- TFDA-Packungsbeilage mit Warnhinweisen/Kontraindikationen, um die Blocking-Lücke (DG001) zu schließen und die S1-Sicherheits-Vorbewertung zu ermöglichen
- Formale DrugBank-basierte MOA-Dokumentation (DG002)
- Eine unabhängige pharmakologische Überprüfung zum Vergleich der GBE1- vs. GAA-Stoffwechselwege, bevor weitere Ressourcen für die Evidenzsammlung bei APBD/GSD IV-bezogenen Vorhersagen investiert werden
- Regulatorische/Zulassungsdokumentation, da Deutschland 0 Autorisierungen zeigt und kein zugelassener Indikationstext zur Referenzierung verfügbar ist
- Falls diese Vorhersagen noch verfolgt werden sollen: vorklinische/in-vitro-Evidenz für GAA-Aktivität in den relevanten Krankheitsmodellen angesichts des völligen Fehlens klinischer oder Literaturunterstützung

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

