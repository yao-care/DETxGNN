---
layout: default
title: Ivabradine
parent: Nur Modellvorhersage (L5)
nav_order: 215
evidence_level: L5
indication_count: 6
---

# Ivabradine
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **6** 
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

# Ivabradine: Von (ursprüngliche Indikation noch nicht dokumentiert) zu Hypertrichose

## Zusammenfassung in einem Satz

> Ivabradine (DB09083) verfügt derzeit über keine dokumentierte ursprüngliche Indikation oder Wirkmechanismus-Daten in diesem Evidenzpaket, und es ist in Deutschland nicht zugelassen (0 Genehmigungen).
> Das TxGNN-Modell sagt eine potenzielle Relevanz für **Hypertrichose (Erkrankung)** mit einer Punktzahl von **99.79%** voraus,
> aber diese Vorhersage wird derzeit durch **0 klinische Studien** und **0 Publikationen** gestützt — es handelt sich um ein modellgestütztes Signal ohne unabhängige Evidenz.

---

## Schneller Überblick

| Element | Inhalt |
|---------|--------|
| Ursprüngliche Indikation | Nicht verfügbar — keine Lizenz oder Indikationstexte im Evidenzpaket (Datenlücke) |
| Vorhergesagte neue Indikation | Hypertrichose (Erkrankung) |
| TxGNN-Vorhersage-Punktzahl | 99.79% |
| Evidence Level | L5 |
| Marktstatus Deutschland | ✗ Nicht zugelassen |
| Anzahl der Genehmigungen | 0 |
| Empfohlene Entscheidung | Halten |

---

## Warum ist diese Vorhersage plausibel?

Derzeit sind detaillierte Wirkmechanismus-Daten für Ivabradine in diesem Evidenzpaket nicht verfügbar, und es wurde auch keine ursprüngliche Indikation dokumentiert. Ohne diese Grundlage kann anhand der bereitgestellten Daten allein keine pharmakologische Verbindung zwischen der ursprünglichen Anwendung und Hypertrichose hergestellt werden.

Es ist auch erwähnenswert, dass alle sechs Erkrankungen, die TxGNN für dieses Medikament identifiziert hat, in einen sehr niedrigen Konfidenzbereich fallen (Rang 3008–9476 aus dem gesamten Vorhersageraum) und sich um seltene kongenitale/genetische Syndrome gruppieren — Hypertrichose, Ambras-Typ kongenitale Hypertrichose, ein Fehlbildungssyndrom mit Zahn-/Parodontal-Merkmalen, Dandy-Walker-Malformationssyndrom, eine isolierte genetische Haarschaftanomalie und nephrogenisches SIAD. Bei Rang 2 (Ambras-Syndrom) dokumentiert das Evidenzpaket selbst bereits die mechanistische Bewertung explizit: Dies ist eine monogene Störung, die mit der Region 8q24.3 in der Nähe von *TRPS1* verknüpft ist, mit **keinem Bezug zu HCN/If-Kanal-Pharmakologie**, und die Reviewer-Begründung empfiehlt bereits **Halten** ohne mechanistische Unterstützung. Dieses Muster in der gesamten Serie — seltene genetische Syndrome ohne offensichtliche Wirkstoff-Ziel-Verbindung — deutet darauf hin, dass die Hypertrichose-Vorhersage wahrscheinlich dieselbe Schwäche aufweist, anstatt ein echtes Repurposing-Signal widerzuspiegeln.

Angesichts des Fehlens von Wirkmechanismus, ursprünglicher Indikation und jeglicher unterstützender Studien- oder Literaturevidenz sollte diese Vorhersage als nicht validierte Modellausgabe behandelt werden, anstatt als eine mechanistisch begründete Hypothese.

---

## Evidenz aus klinischen Studien

Derzeit sind keine verwandten klinischen Studien registriert

---

## Evidenz aus Literatur

Derzeit keine verwandte Literatur verfügbar

*(Hinweis: Literatur, die an anderer Stelle in diesem Evidenzpaket zurückgegeben wird, z. B. unter „Fehlbildungssyndrom mit Zahn-/Parodontal-Bestandteil", bezieht sich auf Parodontitis und zahnmedizinische Mikrobiologie, nicht auf Hypertrichose, und ist hier nicht anwendbar.)*

---

## Informationen zum Markt in Deutschland

Ivabradine verfügt derzeit über keine deutsche Marktzulassung in diesem Evidenzpaket (0 Lizenzen, Marktstatus „nicht zugelassen"). Es sind keine Produktnamen, Darreichungsformen oder genehmigten Indikationstexte für die Extraktion verfügbar.

---

## Sicherheitsaspekte

Bitte beachten Sie die Packungsbeilage für Sicherheitsinformationen.

*(Wichtige Warnungen, Kontraindikationen und Arzneimittelwechselwirkungsdaten sind alle als Datenlücken in diesem Evidenzpaket gekennzeichnet. Der Abruf von TFDA-Etiketten-Warnungen/Kontraindikationen ist als eine blockierende Datenlücke (DG001) gekennzeichnet, was bedeutet, dass eine formale Sicherheit (S1)-Bewertung nicht durchgeführt werden kann, bis diese behoben ist.)*

---

## Schlussfolgerung und nächste Schritte

**Entscheidung: Halten**

**Begründung:**
Es gibt keine Wirkmechanismus-Daten, keine ursprüngliche Indikation in den Unterlagen, keine unterstützenden klinischen Studien oder Literatur für die vorhergesagte Indikation, und das Medikament ist derzeit nicht auf dem deutschen Markt zugelassen. In Verbindung mit der Tatsache, dass eine verwandte Vorhersage in der gleichen Serie (Ambras-Syndrom) bereits als mechanistisch implausibel bewertet wurde, erfüllt dieser Kandidat nicht die Schwelle, um über ein L5-Modellsignal hinaus voranzuschreiten.

**Um voranzukommen, werden folgende Maßnahmen benötigt:**
- Beheben Sie DG001 (TFDA/deutsche Etiketten-Warnungen/Kontraindikationen) — blockiert derzeit jegliche Sicherheit (S1)-Bewertung
- Beheben Sie DG002 (Wirkmechanismus von DrugBank), um die biologische Plausibilität für Hypertrichose zu bewerten
- Bestätigen Sie die ursprünglichen genehmigten Indikationen für Ivabradine aus behördlichen Quellen
- Gezielte Literatursuche speziell zur HCN/If-Kanal-Beteiligung in der Haarfollikel-Biologie, falls vorhanden, da in dieser Abfrage nichts zurückgegeben wurde
- Führen Sie die Evidenzsammlung erneut durch, sobald die Wirkmechanismus- und Indikationsdatenlücken geschlossen sind, bevor Sie diesen Kandidaten neu bewerten

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

