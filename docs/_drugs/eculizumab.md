---
layout: default
title: Eculizumab
parent: Nur Modellvorhersage (L5)
nav_order: 134
evidence_level: L5
indication_count: 10
---

# Eculizumab
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

# Eculizumab: Von komplementvermittelten Erkrankungen zu zyklischer Hämatopoese

## Zusammenfassung in einem Satz

Eculizumab ist ein monoklonaler Antikörper gegen das Komplementprotein C5, historisch etabliert für hämolytische und komplementvermittelte Erkrankungen wie PNH und aHUS (gemäß Hintergrundliteratur in dieser Evidenzsammlung, obwohl formale Indikationen und Labeldaten hier nicht bereitgestellt werden). Die Top-Vorhersage des TxGNN-Modells ist **zyklische Hämatopoese**, eine genetische (ELANE-gesteuerte) Neutopenie-Erkrankung – diese Vorhersage wird jedoch derzeit durch **null klinische Studien** und **null Publikationen** gestützt, was sie zu einer reinen modellgenerierten Hypothese ohne unabhängige Evidenz macht.

---

## Schnellübersicht

| Element | Inhalt |
|---------|--------|
| Ursprüngliche Indikation | In dieser Evidenzsammlung nicht formal bereitgestellt (Wirkstoff ist ein bekannter Anti-C5-Komplementhemmer; Literatur in dieser Sammlung erwähnt PNH, aHUS und refraktäre generalisierte Myasthenia gravis als etablierte Anwendungen – nicht unabhängig als offizielle Labeldaten bestätigt) |
| Vorhergesagte neue Indikation | Zyklische Hämatopoese |
| TxGNN-Vorhersage-Score | 99,97% |
| Evidenzstufe | L5 |
| Status auf dem deutschen Markt | ✗ Nicht im Handel |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | Aussetzen |

---

## Warum ist diese Vorhersage sinnvoll?

Detaillierte Daten zum Wirkmechanismus sind derzeit nicht in strukturierter Form verfügbar (`original_moa: [Data Gap]`). Basierend auf Informationen in der begleitenden Literatur ist Eculizumab ein monoklonaler Antikörper, der das Komplementprotein C5 bindet, dessen Spaltung blockiert und die Bildung des terminalen Membranangriffskomplexes (MAC) verhindert – ein in komplementvermittelten hämolytischen und thrombotischen Mikroangiopathie-Erkrankungen etablierter Mechanismus (z. B. PNH, aHUS).

Die zyklische Hämatopoese wird jedoch durch *ELANE*-Genmutationen verursacht, die die Verarbeitung von Neutrophilen-Elastase und die zyklische Regulation der Granulopoese stören – ein zelleigener myeloider Reifungsdefekt ohne etablierte Verbindung zur Komplementaktivierung. Wie in der Begründung zu dieser Vorhersage explizit angemerkt wird, existiert „keine bekannte Schnittmenge" zwischen dem terminalen Komplementweg und der zyklischen Granulopoese-Regulation.

Diese Vorhersage stellt daher ein Graph-Embedding-Nähe-Signal (TxGNN-Netzwerk-Ähnlichkeit) dar, nicht eine mechanistisch begründete Hypothese. Das gleiche Muster zeigt sich bei den Rängen 2–9 der Kandidatenliste (JAGN1-Mangel, X-gebundene SCN, CXCR2-Mangel, CSF3R-Mangel usw.) – alle sind angeborene Neutopenie/Immundefekt-Syndrome, die durch unterschiedliche, nicht-komplementbezogene Wege verursacht werden, und keines hat unterstützende Studien oder Literatur. Bei den Rängen 4 und 10 wurde Literatur *abgerufen*, aber bei der Überprüfung besteht sie ausschließlich aus bereits bekannten Indikationen von Eculizumab (PNH, aHUS, TMA, Myasthenia gravis) und nicht verwandten CD59-Mutations-Fallberichten – ein Keyword-Matching-Artefakt statt direkter Evidenz für die vorhergesagte Erkrankung selbst.

---

## Evidenz aus klinischen Studien

Derzeit sind keine entsprechenden klinischen Studien registriert.

---

## Evidenz aus der Literatur

Derzeit ist keine entsprechende Literatur verfügbar.

*(Anmerkung: Bei zwei niedriger eingestuften Kandidaten in dieser Evidenzsammlung – angeborenes Neutopenie-Myelofibrose-Nephromegalie-Syndrom, Rang 4; und primäre Plättchen-Freisetzungsstörung, Rang 10 – wurden Literaturergebnisse gefunden, aber alle waren bestätigte Fehlpaarungen, die bereits zugelassene Indikationen von Eculizumab erwähnen, nicht die Kandidaten-Erkrankungen selbst, und werden daher nicht als unterstützende Evidenz für die Top-Vorhersage gezählt.)*

---

## Informationen zum deutschen Markt

Eculizumab wird derzeit **nicht** auf dem deutschen Markt vermarktet, wie aus den regulatorischen Daten dieser Evidenzsammlung hervorgeht, und es sind keine Zulassungsunterlagen verfügbar.

---

## Sicherheitsaspekte

Bitte konsultieren Sie die Fachinformation für Sicherheitsinformationen. (Wichtige Warnhinweise, Kontraindikationen und Daten zu Wechselwirkungen werden in dieser Evidenzsammlung als **blockierende** Datenlücke gekennzeichnet – Fachinformations-/TFDA-Daten wurden noch nicht abgerufen, was ein Fortschreiten zur S1-Sicherheitsscreening-Phase verhindert.)

---

## Fazit und nächste Schritte

**Entscheidung: Aussetzen**

**Begründung:**
Die höchstbewertete Vorhersage (zyklische Hämatopoese) hat keine mechanistische Begründung, keine klinischen Studien und keine Literaturunterstützung – sie erfüllt nur die niedrigste Evidenzstufe (L5, nur Modellvorhersage). In Kombination mit fehlenden MOA-Daten und einer **blockierenden** Sicherheitsdatenlücke (keine Fachinformations-/Kontraindikationsdaten) kann dieser Kandidat nicht über das anfängliche Screening hinausgehen.

**Zur Fortschreitung ist Folgendes erforderlich:**
- Abrufen von formalen Fachinformationen / TFDA-Warnhinweisen und Kontraindikationen zur Beseitigung der blockierenden Datenlücke (DG001)
- Abrufen von strukturierten MOA-Daten aus DrugBank zur Ermöglichung einer ordnungsgemäßen mechanistischen Verknüpfungsanalyse (DG002)
- Unabhängige Studie zur biologischen Plausibilität (in vitro/in vivo) zur Verbindung zwischen C5-Inhibition und ELANE-gesteuerter Granulopoese, falls diese Hypothese weiter verfolgt werden soll
- Wiederholung der Literatur-/Studiensuche mit krankheitsspezifischen Synonymen, um weitere Keyword-Matching-Artefakte auszuschließen, bevor ein Kandidat aus diesem Set über S0 hinaus eskaliert wird

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

