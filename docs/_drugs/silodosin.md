---
layout: default
title: Silodosin
parent: Nur Modellvorhersage (L5)
nav_order: 363
evidence_level: L5
indication_count: 6
---

# Silodosin
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

# Silodosin: Von Benigner Prostatahyperplasie zu Ambras type Hypertrichosis universalis congenita

## Zusammenfassung in einem Satz

> Silodosin ist ein hochselektiver α1A-adrenerger Rezeptorantagonist, pharmakologisch zur Behandlung der benignen Prostatahyperplasie (BPH)/Symptome der unteren Harnwege eingesetzt.
> Die Top-Vorhersage des TxGNN-Modells ist **Ambras type hypertrichosis universalis congenita** (Score 99.99%),
> aber diese Vorhersage wird derzeit durch **null klinische Studien** und **null Publikationen** gestützt, ohne bekannten Mechanismuspfad, der eine α1A-Blockade mit der Haarfollikel-Biologie verbindet.

---

## Schnellübersicht

| Element | Inhalt |
|------|------|
| Ursprüngliche Indikation | Benigne Prostatahyperplasie / Symptome der unteren Harnwege (abgeleitet aus Arzneimittelklasse und Umwidmungs-Rationale-Text; nicht im Paket vorhanden — `original_indications` ist leer) |
| Vorhersagte neue Indikation | Ambras type hypertrichosis universalis congenita |
| TxGNN-Vorhersage-Score | 99.99% (Modellrang 168) |
| Evidenzstufe | L5 |
| Deutschland Marktstatus | Nicht vermarktet |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | Zurückstellen |

---

## Warum ist diese Vorhersage angemessen?

Detaillierte Wirkmechanismus-Daten sind nicht verfügbar (`original_moa: [Data Gap]`). Basierend auf der Arzneimittelklasse und dem im Vorhersagefeld eingebetteten Rationale-Text ist Silodosin ein hochselektiver α1A-adrenerger Rezeptorantagonist, der hauptsächlich auf die glatte Muskulatur der Prostata und der unteren Harnwege wirkt, und es wird angenommen, dass er für BPH eingesetzt wird.

Ambras type hypertrichosis universalis congenita ist eine seltene angeborene Störung, die mit Chromosomenumlagerungen und Haarfollikel-Entwicklungsgenen verbunden ist. Es gibt keinen etablierten biologischen Pfad, der die periphere α1A-Rezeptorblockade mit der Regulation des Haarfollikelwachstums verbindet — arzneimittelinduzierte Hypertrichose ist üblicherweise eher mit Kaliumkanal-Öffnern (z. B. Minoxidil) assoziiert, nicht mit α-adrenerger Antagonismus. Das Rationale-Feld des Pakets selbst kennzeichnet dies ausdrücklich als Fall mit hohem Score und fehlendem Mechanismus, was bedeutet, dass die TxGNN-Assoziation wahrscheinlich eher Embedding-Space-Rauschen als ein biologisch fundiertes Signal widerspiegelt.

Alle fünf weiteren Kandidaten in diesem Paket (Hypertrichose, Malformationssyndrom mit odontaler/parodontaler Komponente, Dandy-Walker-Malformation, Haarschaftanomalie, familiäre Trichomegalie) folgen dem gleichen Muster: sehr hohe TxGNN-Scores kombiniert mit fehlenden klinischen Studienergebnissen und, wo Literatur existiert, abgestimmte Publikationen, die keinen Bezug zum Arzneimittel haben (siehe unten).

---

## Klinische Studienevidenz

Derzeit sind keine verwandten klinischen Studien registriert.

---

## Literaturevidenz

Derzeit ist keine verwandte Literatur verfügbar.

*(Anmerkung: Rang-3-Kandidat „Malformationssyndrom mit odontaler/parodontaler Komponente" lieferte 20 Parodontitis-bezogene Publikationen, aber keine erwähnt Silodosin oder α1-Antagonisten — diese werden als irrelevante Co-Auftritt-Treffer betrachtet, nicht als unterstützende Evidenz für die Top-Vorhersage.)*

---

## Deutschland-Marktinformationen

Silodosin hat derzeit keine Marktzulassungsunterlagen in Deutschland (`total_licenses: 0`, `licenses: []`). Dieses Arzneimittel wird nicht im deutschen Datensatz, der von diesem Paket abgedeckt wird, vermarktet.

---

## Sicherheitsaspekte

Bitte beachten Sie die Packungsbeilage für Sicherheitsinformationen.

*(Anmerkung: `safety.key_warnings` und `safety.contraindications` sind beide in diesem Paket als Datenlücken gekennzeichnet — Element DG001, Schweregrad „Blocking", blockiert speziell die S1-Sicherheitsvorbewertung bis zur Abrufung des TFDA-Labels.)*

---

## Schlussfolgerung und nächste Schritte

**Entscheidung: Zurückstellen**

**Rationale:**
Die Vorhersage trägt einen hohen TxGNN-Score, aber null klinische oder Literaturunterstützung, keinen plausiblen Mechanismuspfad, und das Arzneimittel wird derzeit nicht in Deutschland vermarktet. In Kombination mit einer Sicherheitsdatenlücke mit Blocking-Schweregrad (DG001) und fehlenden MOA-Daten (DG002) erfüllt dieser Kandidat nicht die Mindestanforderungen, um zur Sicherheitsvorbewertung (S1) zu gelangen.

**Zum Fortfahren ist Folgendes erforderlich:**
- TFDA-Label (Warnungen/Kontraindikationen) Abruf zur Behebung von DG001 (Blocking)
- Bestätigter MOA aus DrugBank zur Behebung von DG002 und Ermöglichung der Mechanismus-Bewertung
- Bestätigte ursprüngliche Indikation und Deutschland/Taiwan-Marktstatus (derzeit nicht in Quelldaten vorhanden)
- Präklinische oder Fallbeispiel-Evidenz, die α1-adrenerge Antagonismus mit Haarfollikel- oder angeborener Hypertrichose-Pfaden verbindet — keine existiert derzeit
- Falls keine solche Evidenz auftaucht, sollte dieser Kandidat zugunsten anderer TxGNN-Vorhersagen mit tatsächlicher Studien-/Literaturunterstützung deprioritiert werden

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

