---
layout: default
title: Mannitol
parent: Nur Modellvorhersage (L5)
nav_order: 245
evidence_level: L5
indication_count: 10
---

# Mannitol
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

# Mannitol: Von der Anwendung als osmotisches Diuretikum zum Nephrogenen Syndrom der unangemessenen Antidiurese

## Zusammenfassung in einem Satz

> Mannitol ist ein lange etabliertes osmotisches Diuretikum; formale Datensätze zur ursprünglichen Indikation und zum Wirkmechanismus sind derzeit nicht im Evidenzpaket verfügbar, obwohl es klinisch weithin für die Anwendung bei erhöhtem intrakraniellem/intraokularem Druck und oligurischen Zuständen bekannt ist.
> Das TxGNN-Modell sagt voraus, dass es möglicherweise wirksam sein könnte bei der **Nephrogenen Syndrom der unangemessenen Antidiurese (NSIAD)**,
> aber diese Vorhersage wird derzeit durch **0 klinische Studien** und nur **1 lose verwandte Publikation** gestützt, und sollte eher als ein hypothesengenerierendes Signal denn als verwertbare Evidenz betrachtet werden.

---

## Schnellübersicht

| Eintrag | Inhalt |
|------|------|
| Ursprüngliche Indikation | Nicht verfügbar in behördlichen Daten (0 Lizenzen vorhanden); basierend auf bekannter Pharmakologie wird Mannitol historisch als osmotisches Diuretikum für zerebrales/okuläres Ödem und akute oligurische Zustände verwendet |
| Vorhergesagte neue Indikation | Nephrogenes Syndrom der unangemessenen Antidiurese (NSIAD) |
| TxGNN-Vorhersage-Score | 99.97% |
| Evidenzstufe | L5 |
| Marktstatus Deutschland | ✗ Nicht vermarktet |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | Halten |

---

## Warum ist diese Vorhersage vernünftig?

Derzeit sind detaillierte Wirkmechanismus-Daten für dieses Arzneimittel nicht im Evidenzpaket verfügbar (`original_moa: [Data Gap]`). Basierend auf bekannten pharmakologischen Informationen ist Mannitol ein Zuckeralkohol-Osmotikum, das freies Wasser in das vaskuläre Kompartiment zieht und die renale Ausscheidung von freiem Wasser fördert; es wird seit langem klinisch verwendet, um den intrakraniellen und intraokularen Druck zu senken und die Urinausscheidung in akuten oligurischen Zuständen aufrechtzuerhalten.

Die für NSIAD vorgebrachte mechanistische Begründung besagt, dass ein osmotisches Diuretikum theoretisch die Clearance von freiem Wasser erhöhen und dadurch die für NSIAD charakteristische Verdünnungshyponatriämie korrigieren könnte. Der einzige für diese Kombination abgerufene Literaturartikel (PMID 26706473) ist jedoch eine allgemeine Übersichtsarbeit über Fallstricke bei der Beurteilung von Hyponatriämie – er **erwähnt nicht** Mannitol oder NSIAD spezifisch, und bietet keine direkte experimentelle oder klinische Unterstützung für diese Arzneimittel-Erkrankungs-Kombination.

Es ist auch zu vermerken, dass eine niedriger bewertete Vorhersage in demselben Evidenzpaket (Rang 9, nephrogene Diabetes insipidus) Mannitol/Osmotika als Stoffe kennzeichnet, die zu einer **Diabetes-insipidus-ähnlichen übermäßigen Wasserausscheidung führen können**, anstatt sie zu behandeln – die entgegengesetzte physiologische Richtung. Dies wirft Fragen zur Plausibilität der NSIAD-Vorhersage auf, die vor weiteren Investitionen geklärt werden sollten.

---

## Evidenz aus klinischen Studien

Derzeit sind keine verwandten klinischen Studien registriert

---

## Literaturbelege

| PMID | Jahr | Typ | Zeitschrift | Wichtigste Erkenntnisse |
|------|------|------|------|---------|
| [26706473](https://pubmed.ncbi.nlm.nih.gov/26706473/) | 2016 | Übersichtsartikel | European journal of internal medicine | Allgemeine Übersichtsarbeit über häufige diagnostische Fallstricke bei der Beurteilung hyponatriämischer Patienten; erwähnt Mannitol oder NSIAD nicht spezifisch |

---

## Sicherheitsaspekte

Bitte konsultieren Sie die Packungsbeilage für Sicherheitsinformationen.

---

## Schlussfolgerung und nächste Schritte

**Entscheidung: Halten**

**Begründung:**
Die Vorhersage basiert ausschließlich auf dem algorithmischen Score von TxGNN (L5, keine Studien, ein lose verwandter Übersichtsartikel); es gibt keine direkte mechanistische oder klinische Evidenz, die Mannitol mit NSIAD verbindet, und es existiert ein plausibles gegensätzliches Sicherheitssignal (osmotisches Mittel-induzierter Wasserverlust) an anderer Stelle in diesem Evidenzpaket, das nicht geklärt wurde.

**Um fortzufahren, wird Folgendes benötigt:**
- Bestätigte ursprüngliche Indikation und MOA-Daten für Mannitol (derzeit als Blocking/High data gaps, DG001–DG002 gekennzeichnet)
- TFDA/BfArM-Etikettenprüfung, um den offensichtlichen Widerspruch zwischen „behandelt NSIAD" und „kann Diabetes-insipidus-ähnliche Wasserausscheidung induzieren" zu klären
- Präklinische oder fallbasierte Evidenz, die Mannitol direkt bei NSIAD/SIADH-assoziierter Hyponatriämie testet, bevor es über S0 hinausgeht

**Zusätzliche Anmerkung:** Unter den 10 von TxGNN vorhergesagten Indikationen in diesem Paket sind die meisten (Ränge 1, 3, 5–10) L5/Halten mit geringer oder fehlender unterstützender Evidenz. Der einzige Kandidat mit einer dokumentierten, etablierten klinischen Begründung – Mannitols ergänzende Rolle bei osmotischer Diurese zur Verringerung rhabdomyolyse-bedingter Nierenschädigungen während Krisen maligner Hyperthermie (Rang 4, L4/S1, „Forschungsfrage") – könnte eine produktivere Linie sein, die verfolgt werden kann, wenn weitere Umnutzungsarbeiten an diesem Arzneimittel geplant sind.

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

