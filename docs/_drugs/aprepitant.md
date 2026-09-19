---
layout: default
title: Aprepitant
parent: Nur Modellvorhersage (L5)
nav_order: 33
evidence_level: L5
indication_count: 10
---

# Aprepitant
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

# Aprepitant: Erkundung einer Neuindikation vom Antiemetikum zum nephrogenischen Syndrom der inadäquaten Antidiuretikumsekretion

## Zusammenfassung in einem Satz

> Aprepitant (DB00673) ist ein Antiemetikum der Klasse der NK1-Rezeptor-Antagonisten (derzeit nicht in Taiwan zugelassen).
> Das TxGNN-Modell sagt voraus, dass es möglicherweise gegen das **nephrogenische Syndrom der inadäquaten Antidiuretikumsekretion (nephrogenic syndrome of inappropriate antidiuresis)** wirksam sein könnte,
> aber es gibt derzeit **keine klinischen Studien oder Literaturbelege**, nur einen reinen Modellvorhersage-Score mit Evidenzgrad L5.

---

## Schnellübersicht

| Kategorie | Inhalt |
|-----------|--------|
| Ursprüngliche Indikationen | Nicht in diesem Evidence Pack enthalten (`original_indications` ist leer) |
| Vorhergesagte neue Indikation | Nephrogenisches Syndrom der inadäquaten Antidiuretikumsekretion |
| TxGNN-Vorhersage-Score | 99.97% (Rang 616) |
| Evidenzgrad | L5 (nur Modellvorhersage, keine klinischen Studien, keine Literatur) |
| Zulassungsstatus in Taiwan | Nicht zugelassen |
| Anzahl Genehmigungen | 0 |
| Empfohlene Entscheidung | Hold |

---

## Warum ist diese Vorhersage plausibel?

Derzeit liegen keine Daten zum Wirkmechanismus vor (`original_moa: [Data Gap]`); dies ist ein Datengap mit hohem Schweregrad (DG002) für diesen Fall, der durch separate Abfrage der DrugBank ergänzt werden muss. Ohne Wirkmechanismus-Daten und Aufzeichnungen über ursprüngliche Indikationen ist eine aussagekräftige Bewertung der pharmakologischen Verbindung zwischen „Antiemetikum" und „nephrogenisches Syndrom der inadäquaten Antidiuretikumsekretion" nicht möglich.

Die `repurposing_rationale.mechanistic_link` ist eindeutig gekennzeichnet: „Keine bekannten mechanistischen Verknüpfungen, auch keine klinischen Studien oder Literaturbelege vorhanden, nur Modellvorhersage-Score." Dies bedeutet, dass diese Vorhersage derzeit vollständig auf der Ähnlichkeitsinferenz des TxGNN-Wissensgraphen beruht und noch keine biologische oder klinische Evidenz aufweist.

**Beobachtungen zu anderen Kandidatenindikationen (zur Information, nicht Hauptfokus dieser Bewertung):**

| Rang | Indikation | TxGNN-Score | Bemerkung |
|-----|-----------|----------|----------|
| 3 | Pulmonale Hypertonie | 99.90% | Die einzige begleitende Literatur ist eine Phase-I-Studie mit Pazopanib+Cisplatin zur Behandlung von Nierenzellkarzinom, die mit Aprepitant oder pulmonaler Hypertonie in keiner Beziehung steht; wird als Suchstörung bewertet |
| 6 | Malformationssyndrom mit odontalen/parodontalen Komponenten | 99.86% | Alle 20 begleitenden Literaturangaben beziehen sich auf parodontale Erkrankungen, haben keine mechanistische Verbindung zu Aprepitant, wird ebenfalls als Suchstörung bewertet |
| 9 | Subarachnoidale Blutung | 99.85% | Der Substanz P/NK1-Rezeptor-Weg ist bekannt als an der Störung der Blut-Hirn-Schranke und dem Hirnödem nach SAH beteiligt (hauptsächlich Tierstudien); mechanistisch theoretisch möglich, aber bei dieser Suche wurden keine tatsächlichen klinischen Studien oder Literaturangaben gefunden; bleibt somit ein reiner Modellscore |

Oben wird gezeigt: Ein hoher Score bedeutet nicht starke Evidenz. Literaturangaben bei Rang 3 und 6 werden nach Überprüfung als nicht relevante Störsignale identifiziert, Rang 9 hat theoretische mechanistische Möglichkeiten, aber gleichzeitig mangelnde empirische Unterstützung; muss als Priorität für zukünftige Literaturabfragen aufgelistet werden.

---

## Klinische Studienevidenz

Derzeit keine relevanten registrierten klinischen Studien verfügbar.

## Literaturevidenz

Derzeit keine relevanten Literaturdaten zur Bewertung verfügbar.

## Marktinformationen für Taiwan

Aprepitant ist derzeit **nicht in Taiwan zugelassen**, es liegen keine Arzneimittelgenehmigungen vor (`total_licenses: 0`), es liegen auch keine Darreichungsform- oder Verabreichungsrouteninformationen vor.

---

## Sicherheitsüberlegungen

- **Fachinformationen Warnhinweise/Kontraindikationen**: Fachinformationen der TFDA wurden noch nicht beschafft (DG001, Blocking-Level-Gap), eine vollständige S1-Sicherheitsbewertung ist erforderlich, bis offizielle Fachinformation-PDFs heruntergeladen und analysiert wurden.
- **Arzneimittelwechselwirkungen**: Abfrageergebnis ist `not_found`, derzeit keine Daten verfügbar.

> Hinweis: Da fehlende Fachinformationsdaten ein Blocking-Level-Gap darstellen, kann in diesem Fall **keine vollständige Sicherheitsbewertung** durchgeführt werden. Derzeit wird „Bitte beachten Sie die in der Arzneimittelfahninformation angegebenen Sicherheitsinformationen" als Prinzip angewendet. Nach Ergänzung sollte eine Neubewertung durchgeführt werden.

---

## Schlussfolgerung und Folgemaßnahmen

**Entscheidung: Hold**

**Begründung:**
- Die Vorhersage für eine neue Indikation wird nur durch den TxGNN-Modellscore unterstützt (L5), es gibt keine klinischen Studien oder Literaturbelege;
- Ursprüngliche Indikation und Wirkmechanismus-Daten fehlen, eine Argumentation zur mechanistischen Verknüpfung kann nicht aufgestellt werden;
- Die TFDA-Fachinformationen zur Sicherheit sind ein Blocking-Level-Gap, eine grundlegende Sicherheitsbewertung kann noch nicht abgeschlossen werden;
- Das Arzneimittel ist derzeit nicht in Taiwan zugelassen, es liegen keine Genehmigungen und Darreichungsform-Informationen vor.

**Wenn weitere Fortschritte erforderlich sind, müssen folgende Punkte ergänzt werden:**
- Download und Analyse der offiziellen TFDA-Fachinformation, um Warnhinweise, Kontraindikationen und Darreichungsforminformationen zu erhalten (DG001)
- Abfrage der DrugBank-API, um die vollständigen Aprepitant-Wirkmechanismus-Daten zu erhalten (DG002)
- Spezifische Literatursuche der Substanz P/NK1-Rezeptor-Weg-Hypothese bei Rang 9 (subarachnoidale Blutung), um zu bestätigen, ob verwertbare Evidenz vorhanden ist
- Ausschluss von Störsignal-Literatur bei Rang 3 und 6, um Fehlbewertung als unterstützende Evidenz zu vermeiden

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

