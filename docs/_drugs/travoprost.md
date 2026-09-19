---
layout: default
title: Travoprost
parent: Nur Modellvorhersage (L5)
nav_order: 413
evidence_level: L5
indication_count: 10
---

# Travoprost
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

# Travoprost: Vom Offenwinkelglaukom zu viszeraler Kalziphylaxis

## Zusammenfassung in einem Satz

Travoprost ist ein Prostaglandin-F2α- (PGF2α-) Analogon, das klinisch zur Senkung des Augendrucks bei Patienten mit Offenwinkelglaukom/Augendruckerhöhung eingesetzt wird. Das TxGNN-Modell sagt viszerale Kalziphylaxis als höchstbewertete neue Indikation vorher, aber es gibt derzeit **keine klinischen Studien oder Literaturbeweise**, die diese Assoziation unterstützen, und mechanistisch existiert auch keine bekannte Verbindung. Dies ist daher eine reine Modellvorhersage.

---

## Übersichtstabelle

| Aspekt | Inhalt |
|--------|--------|
| Ursprüngliche Indikationen | Offenwinkelglaukom/Augendruckerhöhung (basierend auf klinischen Studiendaten im Evidenzbericht; das Datenbank-Feld `original_indications` ist derzeit leer) |
| Vorhergesagte neue Indikationen | Viszerale Kalziphylaxis |
| TxGNN-Vorhersagescore | 99.9998% |
| Evidenzgrad | L5 (nur Modellvorhersage, keine echten Forschungsdaten) |
| Status auf dem deutschen Markt | Not marketed |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | Hold |

---

## Warum ist diese Vorhersage sinnvoll?

Das Datenbank-Feld `original_moa` enthält derzeit keine Informationen. Nach wiederholten Darstellungen des Wirkmechanismus im Evidenzbericht ist bekannt, dass Travoprost ein Prostaglandin-F2α- (PGF2α-) Analogon ist, das am FP-Rezeptor wirkt und klinisch zur Erhöhung der uveoskleralen Drainage zur Senkung des Augendrucks eingesetzt wird; einige Literaturstellen deuten auch darauf hin, dass es vaskuläre Glattmuskelrelaxation und lokale vaskuläre Remodellierung (MMP-Hochregulation) induzieren kann.

Bezüglich der in dieser Rangliste an erster Stelle stehenden vorhergesagten Indikation „Viszerale Kalziphylaxis" macht die Wirkmechanismus-Analyse des Evidenzberichts selbst jedoch eindeutig klar: **Es gibt keine bekannte Verbindung zwischen FP-Rezeptor-Agonismus und dem Pathomechanismus der viszeralen Kalziphylaxis (Nebenschilddrüsen-bedingte Störung des Kalzium-Phosphor-Metabolismus und vaskuläre Glattmuskelverkalkung)**. Dies deutet darauf hin, dass diese Vorhersage eine Assoziationsableitung aus dem TxGNN-Wissensgraph ist und nicht auf pharmakologischen Überlegungen beruht.

Bemerkenswert ist, dass die aktuelle Kandidatenliste insgesamt 10 hochbewertete TxGNN-Vorhersagen enthält, von denen nur „vascular disease" (Rang 5) klinische Studien und Literaturbeweise aufweist; jedoch handelt es sich bei der überwiegenden Mehrheit dieser Studien um Glaukom-/Augendruck-bezogene Forschung, die als Grad C eingestuft wird (geringe Relevanz, Indikationsfehlklassifizierung), und nicht um echte Unterstützung für die therapeutische Wirksamkeit bei Gefäßerkrankungen. Die übrigen 8 Kandidaten (einschließlich Thoracic-outlet-Syndrom, vaskuläre Unterentwicklung, Blue-Toe-Syndrom, spontane koronare Arteriendissektion und vaskuläre Endotheliome) haben keinerlei klinische Studien- oder Literaturbelege; einige Wirkmechanismus-Analysen deuten sogar darauf hin, dass sie theoretisch möglicherweise schädlich sein könnten (z. B. potenzielle Risiken durch MMP-Induktion bei Erkrankungen mit bereits bestehenden vaskulären Strukturanomalien). Insgesamt wurde für dieses Arzneimittel bislang keine Repositionierungsrichtung mit pharmakologischer Grundlage und evidenzbasierter Unterstützung ermittelt.

---

## Klinische Studienevidenz

Es gibt derzeit keine entsprechenden Registrierungen klinischer Studien.

---

## Literaturbeweise

Es gibt derzeit keine entsprechende Literatur.

---

## Informationen zum deutschen Markt

Travoprost ist derzeit auf dem deutschen Markt **not marketed**; keine Prüf-/Zulassungsdossiers oder Autorisierungsdatensätze sind zur Auflistung verfügbar.

---

## Sicherheitsaspekte

Bitte konsultieren Sie die Fachinformation des Arzneimittels für Sicherheitsinformationen.

(Zusätzlich: In `data_gaps` wird eine Blocking-Lücke DG001 aufgelistet — TFDA-Fachinformation Warnungen/Kontraindikationen wurden noch nicht erhalten. Dies ist eine notwendige Voraussetzung für den Eintritt in die S1-Sicherheitsbewertung und muss prioritär behandelt werden.)

---

## Schlussfolgerung und nächste Schritte

**Entscheidung: Hold**

**Begründung:**
Diese Vorhersage (Viszerale Kalziphylaxis) wird als L5 bewertet — nur mit TxGNN-Modellscore, ohne klinische Studien- oder Literaturbeweise, und die Wirkmechanismus-Analyse des Evidenzberichts selbst hat bereits eindeutig eine pharmakologische Assoziation ausgeschlossen. Gleichzeitig ist das Arzneimittel auf dem Zielmarkt (Deutschland) not marketed, Sicherheitsdaten (Warnungen, Kontraindikationen, DDI) fehlen vollständig, und die notwendigen Voraussetzungen für den Eintritt in die nächste Bewertungsphase sind nicht erfüllt.

**Sofern Fortschritte angestrebt werden, müssen folgende Lücken geschlossen werden:**
- TFDA/Originalfachinformation Warnungen und Kontraindikationsdaten (DG001, Blocking)
- DrugBank oder Originalherstellerdaten zur Bestätigung des formalen MOA (DG002, High)
- Durchführung einer Literatur-/In-vitro-Recherche auf Wirkmechanismus-Ebene zur Frage, ob FP-Rezeptor-Agonismus den Kalzium-Phosphor-Metabolismus oder die vaskuläre Verkalkung beeinflusst, um die biologische Plausibilität dieser Vorhersage zu bestätigen oder auszuschließen
- Falls zukünftig die Richtung „vascular disease" bewertet werden soll, müssen Recherchen mit korrekten Schlüsselwörtern wiederholt und fehlklassifizierte Glaukom-Studien ausgeschlossen werden, um echte relevante Evidenzen für Gefäßerkrankungen zu gewinnen

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

