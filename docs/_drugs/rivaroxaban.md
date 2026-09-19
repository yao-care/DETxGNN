---
layout: default
title: Rivaroxaban
parent: Nur Modellvorhersage (L5)
nav_order: 350
evidence_level: L5
indication_count: 4
---

# Rivaroxaban
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **4** 
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

# Rivaroxaban: Von der Antikoagulationstherapie zur Rheumatoiden Arthritis

## Zusammenfassung in einem Satz

Rivaroxaban ist ein Faktor-Xa-Inhibitor mit gerinnungshemmender Wirkung, der im Evidenzdossier primär im Zusammenhang mit venöser Thromboembolie (TVT/LE) und Vorhofflimmern-assoziierter Antikoagulation aufgeführt wird.
Das TxGNN-Modell sagt eine mögliche Wirksamkeit bei **Rheumatoider Arthritis** voraus, doch diese Vorhersage wird derzeit nur durch **0 direkt relevante klinische Studien** und **4 Publikationen gestützt, von denen keine die RA-Behandlung selbst betrifft** — die Literatur behandelt stattdessen VTE-Management, Thrombin-Generierungs-Assays, DOAC-Adhärenz und einen Fallbericht, in dem RA lediglich eine zufällige Patientencharakteristik war.

## Kurzübersicht

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Formal nicht erfasst (Datenlücke — siehe DG001/DG002); der im Evidenzdossier hinterlegte Wirkstoffklassen-Kontext deutet auf eine antikoagulatorische Anwendung hin (z. B. TVT/LE-Behandlung gemäß referenzierter Studie NCT00786422) |
| Vorhergesagte neue Indikation | Rheumatoide Arthritis |
| TxGNN-Vorhersagewert | 99.57% |
| Evidenzgrad | L5 |
| Marktstatus Deutschland | ✗ Nicht im Markt |
| Anzahl Zulassungen | 0 |
| Empfohlene Entscheidung | Zurückstellen |

## Warum ist diese Vorhersage plausibel?

Derzeit liegen keine detaillierten Daten zum Wirkmechanismus vor (Datenlücke DG002). Basierend auf den im Evidenzdossier hinterlegten mechanistischen Anmerkungen ist Rivaroxaban ein direkter Faktor-Xa-Inhibitor zur Antikoagulation. Es besitzt keine bekannte entzündungshemmende oder immunmodulierende Aktivität, die plausibel in die Synovitis oder die autoimmune Pathologie eingreifen würde, die der rheumatoiden Arthritis zugrunde liegt.

Die recherchierte Literatur stützt keine therapeutische Beziehung: Sie umfasst einen Übersichtsartikel zum VTE-Management, eine methodische Arbeit zu Thrombin-Generierungs-Assays bei Autoimmunerkrankungen, einen DOAC-Adhärenzvergleich bei Vorhofflimmern sowie einen perioperativen Fallbericht, in dem RA lediglich als Komorbidität bei einer Patientin unter oraler Kortikosteroidtherapie auftrat — keine dieser Arbeiten evaluiert Rivaroxaban als Therapie für RA selbst. Die wahrscheinlichste Erklärung für diese TxGNN-Vorhersage ist eine indirekte Netzwerkassoziation (RA-Patienten weisen ein erhöhtes thrombotisches Risiko auf und benötigen möglicherweise eine Antikoagulation) und kein tatsächlicher krankheitsmodifizierender Mechanismus.

Angesichts des Fehlens eines plausiblen mechanistischen Zusammenhangs, zielrelevanter Studien oder unterstützender Literatur sollte diese Vorhersage nur als explorativ betrachtet und ohne neue mechanistische Evidenz nicht weiterverfolgt werden.

## Klinische Studienevidenz

Derzeit keine relevanten klinischen Studien registriert

## Literaturevidenz

| PMID | Jahr | Typ | Journal | Wesentliche Erkenntnisse |
|------|-----|------|------|---------|
| [29621248](https://pubmed.ncbi.nlm.nih.gov/29621248/) | 2018 | Kohortenstudie | PloS one | Vergleich der Adhärenzraten zwischen Rivaroxaban und Apixaban bei Patienten mit nicht-valvulärem Vorhofflimmern; kein Bezug zur RA-Behandlung. |
| [33141212](https://pubmed.ncbi.nlm.nih.gov/33141212/) | 2020 | Übersichtsarbeit | JAMA | Allgemeine Übersicht zu Diagnose und Behandlung von TVT/LE; keine RA-Inhalte. |
| [34175144](https://pubmed.ncbi.nlm.nih.gov/34175144/) | 2021 | Übersichtsarbeit | La Revue de médecine interne | Behandelt den Thrombin-Generierungs-Assay als Instrument zur Beurteilung der Hyperkoagulabilität bei Autoimmunerkrankungen (z. B. Antiphospholipid-Syndrom); evaluiert Rivaroxaban nicht bei RA. |
| [41918541](https://pubmed.ncbi.nlm.nih.gov/41918541/) | 2026 | Fallbericht | Cureus | Fall eines thromboembolischen Schlaganfalls bei einer 88-jährigen Patientin mit Vorhofflimmern und RA unter oraler Steroidtherapie; RA ist eine zufällige Komorbidität, kein Behandlungsziel. |

## Marktinformationen Deutschland

Für Rivaroxaban liegen in diesem Datensatz keine Zulassungsdatensätze vor (Marktstatus: Nicht im Markt, 0 dokumentierte Zulassungen).

## Sicherheitshinweise

Bitte beachten Sie die Fachinformation für Sicherheitsangaben. (Zentrale Warnhinweise, Kontraindikationen und Daten zu Arzneimittelwechselwirkungen sind derzeit nicht verfügbar — siehe Datenlücke DG001, eingestuft als Blocking, die ein S1-Sicherheitsscreening verhindert.)

## Fazit und nächste Schritte

**Entscheidung: Zurückstellen**

**Begründung:**
Die vorhergesagte RA-Indikation weist keine plausible mechanistische Grundlage, keine unterstützenden klinischen Studien und eine Literatur auf, die vollständig am Thema vorbeigeht; der Evidenzgrad ist L5 (nur Modellvorhersage). Dies steht im Einklang mit den drei weiteren TxGNN-vorhergesagten Indikationen für Rivaroxaban in diesem Evidenzdossier (Gicht, HIV-Infektionskrankheit, Brachydaktylie-Syndaktylie-Syndrom), die ebenfalls alle mit Zurückstellen und Evidenzgraden L4–L5 ohne mechanistisch relevante Unterstützung bewertet werden.

**Um fortzufahren, wird Folgendes benötigt:**
- BfArM-Fachinformationsdaten (Warnhinweise, Kontraindikationen) zur Schließung der Blocking-Datenlücke (DG001), bevor ein S1-Sicherheitsscreening erfolgen kann
- Aus DrugBank stammende Daten zum Wirkmechanismus (DG002), um die mechanistische Plausibilität angemessen bewerten zu können
- Falls die RA-Hypothese weiterverfolgt werden soll: präklinische oder mechanistische Studien, die die Faktor-Xa-Hemmung direkt in RA-relevanten Signalwegen testen (z. B. Synovialentzündungsmodelle), da die aktuelle Literatur RA nur als zufällige Komorbidität berührt
- Formale Daten zur ursprünglichen Indikation und Zulassung, die derzeit im Register fehlen, um die Repurposing-Begründung sachgerecht einzuordnen

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

