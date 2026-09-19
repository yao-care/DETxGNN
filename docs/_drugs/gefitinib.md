---
layout: default
title: Gefitinib
parent: Nur Modellvorhersage (L5)
nav_order: 177
evidence_level: L5
indication_count: 10
---

# Gefitinib
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

# Gefitinib: Von nicht-kleinzelligem Lungenkarzinom zur gingivalen Fibromatose (schwaches Signal)

## Zusammenfassung in einem Satz

Gefitinib ist ein oraler EGFR-Tyrosinkinase-Inhibitor, der für EGFR-mutiertes nicht-kleinzelliges Lungenkarzinom (NSCLC) etabliert ist, wie in dieser Evidenzsammlung dokumentierte Literatur bestätigt. Die vom TxGNN-Modell am höchsten bewertete neue Indikation, **Gingivale Fibromatose**, verfügt über **keine unterstützenden klinischen Studien oder Literatur** und keine bekannte mechanistische Verbindung zur EGFR-Biologie – die Rationale der Sammlung selbst kennzeichnet dies als wahrscheinliches Artefakt im Einbettungsraum statt als echtes arzneistoffspezifisches Signal. Über alle 10 vorhergesagten Indikationen in diesem Kandidatenset verfügen nur zwei (Lungenhiluskarzinom, Lungenschulterblatt-Neoplasma – beide anatomische Subtypen von NSCLC) über eine gewisse Literaturrelevanz, und selbst diese stellen eher labelnahe Erweiterungen dar als echte neue Umwidmungskandidaten.

---

## Schnelübersicht

| Punkt | Inhalt |
|-------|--------|
| Original-Indikation | Nicht in Zulassungsdaten vorhanden (Arzneistoff nicht in Deutschland vermarktet); durchgehend in der Literatur der Sammlung selbst als Therapie für EGFR-mutiertes nicht-kleinzelliges Lungenkarzinom (NSCLC) beschrieben |
| Vorhergesagte neue Indikation | Gingivale Fibromatose |
| TxGNN-Vorhersage-Score | 99,89% (Rang 1785 in der internen Rangfolge des Modells) |
| Evidenzstufe | L5 (Modellvorhersage nur, keine Studien oder Literatur) |
| Deutsches Marktstatus | ✗ Nicht vermarktet |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | Zurückstellen |

---

## Warum ist diese Vorhersage angemessen?

Formale DrugBank-MOA-Daten sind als Datenlücke (DG002) in dieser Evidenzsammlung gekennzeichnet. Basierend auf in die Sammlung selbst eingebetteter Literatur (z. B. PMID 24794908, 12841190) ist Gefitinib ein selektiver, ATP-kompetitiver, niedermolekularer Inhibitor der Tyrosinkinase des Epidermalen Wachstumsfaktor-Rezeptors (EGFR), das klinisch zur Behandlung von EGFR-mutiertem NSCLC durch Blockierung von nachgelagerter Proliferations- und Überlebenssignalisierung in Tumorzellen eingesetzt wird.

Für die am höchsten bewertete Vorhersage, **gingivale Fibromatose**, gibt es keine mechanistische Verbindung zu dieser Signalkaskade. Gingivale Fibromatose ist eine gingivo-Bindegewebs-Überwuchsstörung, die mit Signalwegen wie TGF-β/Fibroblasten-Proliferation verbunden ist, nicht mit EGFR-angetriebener epithelialer Malignität. Die der Umwidmungsrationale dieses Kandidaten zugeordnete Begründung besagt explizit, dass der hohe TxGNN-Score wahrscheinlich eine Clusterbildung im Krankheits-Einbettungsraum des Modells widerspiegelt statt ein arzneistoffspezifisches pharmakologisches Signal.

Innerhalb des breiteren Kandidatensets haben nur die beiden Vorhersagen mit einer kohärenten mechanistischen Geschichte eine aussagekräftige Geschichte: **Lungenhiluskarzinom** (Rang 5, L3) und **Lungenschulterblatt-Neoplasma / Pancoast-Tumor** (Rang 9, L4) – beide sind anatomische Subtypen von NSCLCs Gefitinibs bereits zugelassener Indikation. Diese sind nicht so sehr neue Umwidmungshypothesen als vielmehr labelnahe anatomische Erweiterungen, und die zugeordnete Evidenz (ein einzelner Fallbericht, eine ECOG-NSCLC-Stadium-Übersicht, ein nicht verwandter Fall von leptomeningealer Metastasierung) bezieht sich nicht spezifisch auf diese Subtypen. Die verbleibenden 7 Kandidaten (Lungenfibrom, Lungenhamartom, IBMPFD, benigne Lungenneoplasma, ein seltenes genetisches Syndrom, Lungenkeim-Zell-Tumor, junctionale epidermolysis bullosa) zeigen entweder mechanistische Implausibilität, Literatur-Label-Mismatch oder im Fall der junctionalen epidermolysis bullosa einen Mechanismus, der in der **entgegengesetzten** Richtung wirkt (EGFR-Hemmung ist eine bekannte Ursache für Hautbarriere-Toxizität, nicht eine Behandlung für einen Hautbarriere-Defekt).

---

## Klinische Studien-Evidenz

Derzeit sind keine verwandten klinischen Studien registriert.

---

## Literatur-Evidenz

Derzeit ist keine verwandte Literatur verfügbar.

---

## Informationen zum deutschen Markt

Gefitinib verfügt derzeit über **keine Zulassungen** in Deutschland (Marktstatus: nicht vermarktet, Gesamtzulassungen: 0). Aus dieser Evidenzsammlung kann keine Produkttabelle erstellt werden.

---

## Zytotoxizität

Gefitinib ist ein antineoplastisches Mittel (EGFR-gerichtete Therapie für NSCLC, gemäß in dieser Sammlung eingebetteter Literatur), daher gilt dieser Abschnitt.

| Punkt | Inhalt |
|-------|--------|
| Zytotoxizitäts-Klassifikation | Zielgerichtete Therapie (EGFR-Tyrosinkinase-Inhibitor) – kein konventionelles zytotoxisches Mittel |
| Myelosuppressionsrisiko | Niedrig. In dieser Sammlung enthaltene Literatur hebt interstitielle Lungenerkrankung (PMID 20942679, 20949670), QT-Verlängerung (PMID 34474028, 37258113) und kutane Toxizität (PMID 18931563) als charakteristische Nebenwirkungen statt Knochenmarkssuppression, die typisch für zytotoxische Chemotherapie ist, hervor |
| Emetogenitäts-Klassifikation | Niedrig (orales niedermolekulares zielgerichtetes Mittel) |
| Überwachungs-Items | Leberfunktionstests, Lungensymptome/Bildgebung (ILD-Risiko), EKG/QTc, Hauttoxizitätsbewertung; CBC-Baseline angemessen angesichts der onkologischen Anwendung |
| Schutzmaßnahmen bei der Handhabung | Gefitinib ist ein orales Antineoplastikum und erscheint typischerweise auf institutionellen Hazardous-Drug-Listen; Standard-Schutzmaßnahmen für orale Hazardous-Drugs gelten, obwohl es keine Kontrollen für IV-Zytostatika-Rekonstitution/Compoundierung erfordert |

---

## Sicherheitsaspekte

Bitte beachten Sie die Fachinformation für Sicherheitsinformationen.

*(Hinweis: TFDA/deutsche Warnungen und Kontraindikations-Daten sind eine Datenlücke – DG001 – und die Arzneistoff-Wechselwirkungssuche lieferte keine Ergebnisse in dieser Sammlung.)*

---

## Fazit und nächste Schritte

**Entscheidung: Zurückstellen**

**Begründung:**
Keine der 10 vorhergesagten Indikationen in diesem Kandidatenset wird durch angemessene mechanistische oder klinische Evidenz unterstützt: 8 von 10 sind L5 (Modell-Score nur, keine Studien/Literatur) oder mechanistisch implausibel/nicht passend, und die beiden mit dokumentierter Unterstützung (Lungenhiluskarzinom, Lungenschulterblatt-Neoplasma) sind anatomische Subtypen von Gefitinibs bestehender NSCLC-Indikation statt echte neue Umwidmungsmöglichkeiten. Kombiniert mit einer kritischen Sicherheitsdatenlücke (DG001) und dem Status des Arzneistoffs als nicht vermarktet in Deutschland, erfüllt dieser Kandidat nicht die Voraussetzungen, um über S0/S1 hinaus voranzuschreiten.

**Für einen Fortschritt sind folgende Punkte erforderlich:**
- Klärung von DG001: Beschaffung von TFDA/EU SmPC-Warnungen und Kontraindikationen für Gefitinib (Iressa)
- Klärung von DG002: Bestätigung formaler MOA über DrugBank-API statt Literatur-Rückschluss
- Bei Verfolgung von Lungenhiluskarzinom oder Lungenschulterblatt-Neoplasma: Klärung mit Behörden/klinischer Überprüfung, ob diese bereits unter die bestehende NSCLC-Zulassung fallen – ein Anspruch auf „neue Indikation" ist möglicherweise nicht gerechtfertigt
- Vor Überprüfung durch Apotheker erneute Durchsicht oder manuelle Kurierung der TxGNN-Top-10-Ausgabe, angesichts des hohen Anteils mechanistisch implausible oder mit Label nicht übereinstimmend Kandidaten (seltene genetische Syndrome, benigne Tumoren und eine Hautbarriere-Defekt-Erkrankung kombiniert mit einem EGFR-Inhibitor)

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

