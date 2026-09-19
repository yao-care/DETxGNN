---
layout: default
title: Roxadustat
parent: Mittlere Evidenz (L3-L4)
nav_order: 355
evidence_level: L4
indication_count: 4
---

# Roxadustat
{: .fs-9 }

Evidenzniveau: **L4** | Vorhergesagte Indikationen: **4** 
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

# Roxadustat: Von renaler Anämie zum Trockenen Auge

## Zusammenfassung in einem Satz

> Roxadustat ist ein HIF-Prolyl-Hydroxylase-Inhibitor (HIF-PHI), der zur Behandlung der renalen Anämie bei Patienten mit chronischer Nierenerkrankung eingesetzt wird.
> Das TxGNN-Modell prognostiziert, dass es möglicherweise wirksam gegen das **Trockene Auge** sein könnte,
> doch wird dies derzeit nur durch **1 Beobachtungsstudie** und **keine Publikationen** gestützt, von denen keine die therapeutische Wirkung von Roxadustat auf das Trockene Auge direkt überprüft.

---

## Schnelle Übersicht

| Element | Inhalt |
|------|------|
| Ursprüngliche Indikation | Renale Anämie (mit chronischer Nierenerkrankung assoziierte Anämie) – aus dem Kontext der klinischen Studie abgeleitet; nicht als strukturiertes Feld in diesem Nachweispaket vorhanden |
| Vorhergesagte neue Indikation | Trockenes Auge |
| TxGNN-Vorhersagescore | 99.51% |
| Evidenzstufe | L4 |
| Marktstatus Deutschland | Nicht vermarktet |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | Zurückstellen |

---

## Warum ist diese Vorhersage vernünftig?

Derzeit ist kein strukturierter Wirkmechanismus-Datensatz für dieses Arzneimittel verfügbar (`original_moa` ist als Datenlücke gekennzeichnet, DG002). Die Begründung des Nachweispakets für die Umwidmung identifiziert Roxadustat jedoch als einen **HIF-Prolyl-Hydroxylase-Inhibitor (HIF-PHI)**, der HIF-1α/2α stabilisiert, um die Produktion von endogenem Erythropoietin (EPO) hochzuregulieren – der Wirkmechanismus, der seiner Verwendung bei renaler Anämie zugrunde liegt.

Die Verbindung zum Trockenen Auge ist schwach und indirekt. Die einzige unterstützende klinische Studie (NCT06287879) testet Roxadustat überhaupt nicht als Behandlung für das Trockene Auge – es ist eine **Beobachtungsstudie**, die die Funktion und Morphologie der Meibom-Drüsen bei Patienten mit renaler Anämie untersucht, die zufällig mit Symptomen des Trockenen Auges auftreten, wobei Roxadustat nur als eine der Hintergrund-Anämiebehandlungen erwähnt wird, die diese Patienten erhalten. Es gibt keinen mechanistischen oder empirischen Beweis dafür, dass HIF-Stabilisierung die Funktion der Meibom-Drüsen oder die Stabilität des Tränenfilms verbessert; das gleichzeitige Auftreten lässt sich plausibel durch gemeinsame Komorbiditäten (chronische Nierenerkrankung/Urämie) statt durch einen Arzneimitteleffekt erklären.

Angesichts des Fehlens einer Interventionsstudie oder Literatur, die Roxadustat direkt für das Trockene Auge testet, sollte diese Vorhersage als ein hypothesengenerierendes Signal aus dem Wissensgraph betrachtet werden, anstatt als ein durch Evidenz gestützter Umwidmungskandidat.

---

## Klinische Studienevidenzen

| Studiennummer | Phase | Status | Einschreibung | Wichtigste Erkenntnisse |
|---------|------|------|------|---------|
| [NCT06287879](https://clinicaltrials.gov/study/NCT06287879) | NA | Unbekannt | 50 | Beobachtungsstudie zur Charakterisierung der Meibom-Drüsenfunktion und Morphologie bei Patienten mit renaler Anämie und Symptomen des Trockenen Auges; Roxadustat/EPO als Hintergrund-Anämiebehandlungen aufgeführt, nicht als Intervention bei Trockenem Auge bewertet (Relevanzgrad: C) |

---

## Literaturnachweise

Derzeit keine verwandte Literatur verfügbar.

---

## Marktinformationen Deutschland

Roxadustat wird derzeit auf diesem Markt **nicht vermarktet** – 0 Zulassungen in den Unterlagen, und keine Lizenzeinträge sind im Nachweispaket verfügbar.

---

## Sicherheitsaspekte

- **Wichtige Warnungen**: Für dieses Arzneimittel sind derzeit keine formalen Packungsbeilage-Warnungs-/Kontraindikationsdaten verfügbar (blockierende Datenlücke; TFDA-Etikett wurde noch nicht abgerufen und analysiert).
- **Wichtiges mechanistisches Sicherheitssignal (aus Nachweispaket)**: Eine niedriger bewertete TxGNN-Vorhersage (Plattenepithelkarzinom, Rang 4) hebt eine entgegengesetzt gerichtete Besorgnis hervor – HIF-1α/2α-Stabilisierung ist ein etablierter Treiber von Tumorwachstum, Angiogenese und Metastasenbildung in vielen soliden Tumoren, einschließlich Plattenepithelkarzinom. Dies ist im Nachweispaket als eine **bekannte Sicherheitsüberlegung für die Verwendung von Roxadustat bei Patienten mit aktiver oder früherer Malignität** gekennzeichnet, nicht als eine therapeutische Gelegenheit, und sollte in jede Risikobewertung für dieses Arzneimittel einfließen.

---

## Schlussfolgerung und nächste Schritte

**Entscheidung: Zurückstellen**

**Begründung:**
Die einzige verfügbare Evidenz (eine nicht-interventionale Studie mit unbekanntem Status, bewertet mit Relevanzgrad C) testet nicht die Wirkung von Roxadustat auf das Trockene Auge, und keine Literatur unterstützt diese Indikation. Kombiniert mit einer blockierenden Datenlücke bei der TFDA-Sicherheitskennzeichnung und dem nicht vermarkteten Status des Arzneimittels gibt es unzureichende Evidenz, um diesen Kandidaten voranzubringen.

**Um voranzuschreiten, wird Folgendes benötigt:**
- TFDA-Kennzeichnung/Warnungen und Kontraindikationen (DG001, blockierend)
- Bestätigte Wirkmechanismus-Daten von DrugBank (DG002)
- Eine Interventionsstudie oder präklinische Studie, die direkt die Wirkung von Roxadustat auf das Trockene Auge/Tränenfilm-Ergebnisse testet
- Literatursuche, die speziell HIF-PHI-Effekte auf Erkrankungen der Augenoberfläche adressiert
- Eine formale Sicherheitsüberprüfung des Malignität-bezogenen mechanistischen Signals (HIF-Stabilisierung und Tumorförderung), bevor weitere Indikationserweiterung in Betracht gezogen wird

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

