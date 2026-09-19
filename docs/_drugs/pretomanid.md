---
layout: default
title: Pretomanid
parent: Nur Modellvorhersage (L5)
nav_order: 319
evidence_level: L5
indication_count: 5
---

# Pretomanid
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **5** 
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

# Pretomanid: Von arzneimittelresistenter Tuberkulose bis Candidose

## Zusammenfassung in einem Satz

> Pretomanid ist ein antimykobakterielles Prodrug, das als Teil des BPaL-Regimes zur Behandlung arzneimittelresistenter Tuberkulose verwendet wird. Das TxGNN-Modell prognostiziert, dass es bei **Candidose** wirksam sein könnte, aber diese Vorhersage wird derzeit durch **0 klinische Studien** und **0 Publikationen** gestützt, und die zugrunde liegende Rationale selbst weist darauf hin, dass sich der Mechanismus nicht auf Pilzerreger überträgt.

---

## Schnellübersicht

| Element | Inhalt |
|------|------|
| Ursprüngliche Indikation | Arzneimittelresistente Tuberkulose als Teil des BPaL-Regimes (nicht im bereitgestellten Regulierungsdatensatz aufgeführt – aus Literaturbelegen abgeleitet) |
| Vorhergesagte neue Indikation | Candidose |
| TxGNN-Vorhersagepunktzahl | 99.69% |
| Evidenzstufe | L5 |
| Marktstatus Deutschland | ✗ Nicht auf dem Markt |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | **Abwarten** |

---

## Warum ist diese Vorhersage angemessen?

Detaillierte offizielle Wirkmechanismus-Daten sind derzeit nicht verfügbar (Daten-Engpass). Basierend auf den in der begleitenden Literaturevidenz verfügbaren Informationen ist Pretomanid ein Nitroimidazooxazin-Prodrug, das durch die Deazaflavin-abhängige Nitroreduktase (Ddn), ein für Mykobakterien spezifisches Enzym, aktiviert werden muss. Nach der Aktivierung erzeugt es reaktive Stickstoffspezies, die die Mykolsäuresynthese hemmen (aerobe Bedingungen) oder als Atemgift wirken, das Stickstoffmonoxid freisetzt (anaerobe Bedingungen). Dieser Aktivierungsweg ist einzigartig für die Gattung *Mycobacterium*.

Candidose wird durch *Candida*-Arten (Pilze) verursacht, denen das Ddn-Enzymsystem und der Mykolsäuresyntheseweg vollständig fehlen. Es gibt daher keine plausible mechanistische Verbindung zwischen der bekannten Zielbiologie von Pretomanid und Pilzinfektionen. Der hohe TxGNN-Score spiegelt höchstwahrscheinlich wider, dass das Modell Pretomanid mit einem breiten „antimikrobiellen/antiinfektiven" Knoten-Cluster im Wissensgraphen verbindet, anstatt zielspezifische Evidenz für antimykotische Aktivität zu finden.

Diese Bedenken werden durch die zweitrangige Vorhersage des Modells, **Lepra** (Rang 2, Punktzahl 99.27%), verstärkt, die – obwohl sie die Gattung *Mycobacterium* mit der ursprünglichen Indikation teilt und daher biologisch plausibler erscheint – direkt durch experimentelle Evidenz im Evidenzpaket selbst widersprochen wird (PMID 17005816: *M. leprae* ist natürlicherweise resistent gegen PA-824/Pretomanid, wahrscheinlich aufgrund unzureichender Ddn-Aktivität). Die verbleibenden Top-5-Vorhersagen (koronare Herzkrankheit, Myokardischämie, ALCAPA) haben überhaupt keine mechanistische Grundlage und widersprechen im Falle von kardiovaskulären Indikationen aktiv Pretomanids bekanntem QT-Verlängerungsrisiko. Zusammengefasst haben derzeit keine der Top-5-TxGNN-Vorhersagen für dieses Arzneimittel glaubwürdige mechanistische oder empirische Unterstützung.

---

## Evidenz aus klinischen Studien

Derzeit sind keine verwandten klinischen Studien registriert

---

## Literaturevidenz

Derzeit ist keine verwandte Literatur verfügbar

---

## Marktinformationen Deutschland

Pretomanid ist **derzeit nicht in Deutschland auf dem Markt** — es sind keine Zulassungsdossiers im Regulierungsdatensatz vorhanden (0 Zulassungen, 0 aufgezeichnete Darreichungsformen).

---

## Sicherheitsaspekte

Bitte beachten Sie die Fachinformation für Sicherheitsinformationen.

**Hinweis (aus dem Kontext des Evidenzpakets, kein formaler Sicherheitsdatenbankeintrag):** Die Umwidmungsrationale für kardiovaskuläre Vorhersagen (Ränge 3–4) bezieht sich auf ein bekanntes Risiko der QT-Intervallverlängerung, das mit Pretomanid verbunden ist. Dies sollte als Signal behandelt werden, um es gegen die offizielle Fachinformation zu überprüfen, sobald diese verfügbar ist, und nicht als bestätigter Befund.

---

## Schlussfolgerung und nächste Schritte

**Entscheidung: Abwarten**

**Rationale:**
Die am höchsten bewertete Vorhersage (Candidose) hat null unterstützende klinische Studien oder Literatur, und der bekannte Wirkmechanismus des Arzneimittels erstreckt sich nicht auf Pilzerreger. Die nächst beste durch Evidenz unterstützte Vorhersage (Lepra) wird direkt durch In-vitro-Resistenzdaten widerlegt, und niedriger bewertete Vorhersagen (kardiovaskuläre Indikationen) haben keine mechanistische Grundlage und widersprechen einem bekannten kardialen Sicherheitsrisiko. Es gibt keine glaubwürdige Evidenzbasis, um eine der aktuellen Top-5-Vorhersagen weiter zu verfolgen.

**Zum Fortfahren ist Folgendes erforderlich:**
- Beheben Sie DG001 (Blockierung): Erhalten Sie TFDA/BfArM-Beschriftungswarnungen und Kontraindikationen, bevor ein S1-Sicherheits-Screening durchgeführt werden kann
- Beheben Sie DG002: Bestätigen Sie den Wirkmechanismus über DrugBank API-Abfrage
- Wenn Candidose weiter verfolgt werden soll, generieren oder suchen Sie präklinische In-vitro-Daten zur antimykotischen Empfindlichkeit für Pretomanid gegen *Candida* spp.
- Angesichts der Lepra-Resistenzbefunde weitere Lepra-Untersuchungen deprioritisieren, sofern nicht neue experimentelle Erkenntnisse auftauchen
- Keine weiteren Maßnahmen bezüglich kardiovaskulärer Vorhersagen (Ränge 3–5) empfohlen ohne plausible mechanistische Hypothese

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

