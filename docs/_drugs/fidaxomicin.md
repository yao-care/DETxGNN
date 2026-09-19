---
layout: default
title: Fidaxomicin
parent: Nur Modellvorhersage (L5)
nav_order: 168
evidence_level: L5
indication_count: 9
---

# Fidaxomicin
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **9** 
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

# Fidaxomicin: Von Clostridioides-difficile-Infektion zu Staphylokokken-Verbrühungssyndrom

## Zusammenfassung in einem Satz

Fidaxomicin ist ein Makrolid-Antibiotikum mit engem Spektrum, dessen einzige etablierte klinische Verwendung die Behandlung einer *Clostridioides-difficile*-Infektion (CDI) ist, wobei es lokal im Darm wirkt mit vernachlässigbarer systemischer Absorption.
Das TxGNN-Modell sagt voraus, dass es möglicherweise wirksam gegen das **Staphylokokken-Verbrühungssyndrom (SSSS)** sein könnte,
aber derzeit **0 klinische Studien** und **0 Publikationen** unterstützen diese spezifische Vorhersage, und der zugrunde liegende Mechanismus spricht gegen systemische Wirksamkeit.

## Schnelle Übersicht

| Punkt | Inhalt |
|-------|--------|
| Ursprüngliche Indikation | *Clostridioides-difficile*-Infektion (gemäß etablierter klinischer Verwendung; nicht auf diesem Markt registriert – keine Zulassungsdaten verfügbar) |
| Vorhergesagte neue Indikation | Staphylokokken-Verbrühungssyndrom |
| TxGNN-Vorhersage-Score | 99.71% |
| Evidenzebene | L5 |
| Marktstatus in Deutschland | Nicht vermarktet (Nicht vermarktet) |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | Zurückhalten |

## Warum ist diese Vorhersage angemessen?

Derzeit sind detaillierte Daten zum Wirkmechanismus nicht verfügbar (Datenlücke). Basierend auf bekannter klinischer Verwendung ist Fidaxomicin ein Makrolid-Antibiotikum mit engem Spektrum, das die bakterielle RNA-Polymerase hemmt; seine Wirksamkeit wurde speziell für *C.-difficile*-assoziierte Diarrhö etabliert, wobei es fast ausschließlich im Darmlumen wirkt – die systemische Absorption nach oraler Gabe beträgt weniger als 1%.

Dieses pharmakokinetische Profil ist das zentrale Problem für die vorhergesagte Indikation. SSSS ist eine systemische dermatologische Erkrankung, die durch exfoliative Toxine von *Staphylococcus aureus* verursacht wird und ein Arzneimittel mit aussagekräftiger systemischer (oder zumindest hautpenetrierender) Bioverfügbarkeit und Aktivität gegen Staphylokokken erfordert. Fidaxomicin erreicht keines von beiden: seine Verteilung ist im Wesentlichen auf den Gastrointestinaltrakt beschränkt, und sein Antibiotika-Spektrum ist eher auf *C. difficile* und verwandte anaerobe gram-positive Organismen ausgerichtet als auf typische kutane *S.-aureus*-Stämme.

Angesichts dieser Unstimmigkeit sollte die Vorhersage als statistische Assoziation interpretiert werden, die das TxGNN-Modell zutage gefördert hat, statt als mechanistisch gestützte Hypothese. Derzeit gibt es keine pharmakokinetischen, mikrobiologischen oder klinischen Belege, die die Lücke zwischen Fidaxomicins bekanntem Verhalten und den Anforderungen der SSSS-Behandlung schließen.

## Klinische Studien

Derzeit sind keine verwandten klinischen Studien registriert.

## Literaturbelege

Derzeit ist keine verwandte Literatur verfügbar.

## Informationen zum deutschen Markt

Dieses Arzneimittel hält derzeit keine Zulassungen in dieser Gerichtsbarkeit (0 erfasste Lizenzen); es kann keine Produkt-/Zulassungstabelle erstellt werden.

## Sicherheitsaspekte

Bitte beziehen Sie sich auf die Packungsbeilage für Sicherheitsinformationen. TFDA-Kennzeichnungswarnungen, Kontraindikationen und Arzneimittelwechselwirkungs-Daten sind derzeit nicht verfügbar (gekennzeichnet als **blockierende** Datenlücke – DG001), was an sich eine S1-Sicherheits-Vorabprüfung für diesen Kandidaten verhindert.

## Fazit und nächste Schritte

**Entscheidung: Zurückhalten**

**Begründung:**
Die topgerankte Vorhersage (SSSS) hat Evidenzebene L5 – ein TxGNN-statistischer Score ohne unterstützende klinische Studien oder Literatur – und die bekannte Pharmakokinetik des Arzneimittels (darmgebunden, <1% systemische Absorption) sprechen mechanistisch gegen Wirksamkeit in einer systemischen staphylokokkalen Hauterkrankung. Das Arzneimittel ist auch in dieser Gerichtsbarkeit nicht vermarktet (0 Zulassungen), und für eine S1-Bewertung erforderliche Sicherheitsdaten sind derzeit blockiert (DG001).

**Um voranzukommen, ist Folgendes erforderlich:**
- TFDA-/offizielle Kennzeichnungs-Daten zu Warnungen, Kontraindikationen und Wechselwirkungen (blockierende Lücke, DG001)
- Bestätigter Wirkmechanismus aus DrugBank oder Primärliteratur (Hochprioritäts-Lücke, DG002)
- Präklinische oder in-vitro-Belege für Fidaxomicin-Aktivität gegen *S.-aureus*-Stämme, die für SSSS relevant sind
- Pharmakokinetische Daten, die ausreichende systemische/dermale Exposition demonstrieren, falls systemische Anwendung erwogen wird
- Anmerkung: Rang 8 (*S.-aureus*-Pneumonie, L4, ein Zitat auf Review-Ebene) ist vergleichbar schwach und keine stärkere Alternative ohne Primärbelege

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

