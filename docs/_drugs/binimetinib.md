---
layout: default
title: Binimetinib
parent: Nur Modellvorhersage (L5)
nav_order: 57
evidence_level: L5
indication_count: 0
---

# Binimetinib
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **0** 
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

# Binimetinib: Bewertung der Umwidmung von Arzneimitteln — Unzureichende Daten für vollständige Bewertung

## Zusammenfassung in einem Satz

Binimetinib (Mektovi) ist ein selektiver MEK1/2-Inhibitor, der international zur Behandlung von BRAF-V600E/K-mutanten, nicht resezierbaren oder metastasierten Melanomen in Kombination mit Encorafenib zugelassen ist. Das aktuelle Evidence Pack enthält **keine TxGNN-vorhergesagten Indikationen** und weist kritische Datenlücken bei Wirkmechanismus und Sicherheitsangaben auf, was eine vollständige Bewertung der Umwidmung in dieser Phase unmöglich macht. **Empfohlene Maßnahme: Zurückstellen — Datenlücken vor dem Fortfahren beheben.**

---

## Schnellübersicht

| Element | Inhalt |
|---------|--------|
| Ursprüngliche Indikation | BRAF-V600E/K-mutantes, nicht resezierbares oder metastasiertes Melanom (international; keine Taiwan-Zulassung) |
| Vorhergesagte neue Indikation | — (Keine TxGNN-Vorhersagen zurückgegeben) |
| TxGNN-Vorhersage-Bewertung | — |
| Evidenzebene | — |
| Taiwan-Marktstatus | ✗ Nicht auf dem Markt |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | **Zurückstellen** |

---

## Warum keine Umwidmungsvorhersage verfügbar ist

Die TxGNN-Pipeline hat für Binimetinib (DB11967) in diesem Evidence Pack keine vorhergesagten Indikationen zurückgegeben. Ohne mindestens eine Kandidatenindikation können die Kernabschnitte zur Umwidmungsbegründung, klinische Studienevidenzen und Literaturevidenzabschnitte nicht ausgefüllt werden.

Zur Kontextualisierung: Binimetinib ist ein gut charakterisiertes kleines Molekül, das die RAS→RAF→MEK→ERK-Signalwegachse (MAPK-Weg) blockiert. Die MEK-Hemmung wurde in mehreren soliden Tumortypen über Melanom hinaus untersucht — einschließlich NSCLC, Darmkrebs, Bauchspeicheldrüsenkrebs und mehreren hämatologischen Malignomen — was darauf hindeutet, dass gültige Umwidmungskandidaten wahrscheinlich vorhanden sind. Die Abwesenheit von Vorhersagen spiegelt höchstwahrscheinlich ein Problem bei der Pipeline-Ausführung wider, nicht einen echten Mangel an biologischem Signal. Erneutes Ausführen der TxGNN-Pipeline ist die unmittelbare Priorität.

---

## Taiwan-Marktinformationen

Binimetinib wird **in Taiwan nicht vermarktet**. Es sind keine TFDA-zugelassenen Produkte, genehmigten Indikationen oder Dosierungsformulare verfügbar.

> Hinweis: Das Abfragelog bestätigt, dass ein TFDA-Packungsbeilage-Datensatz abgerufen wurde (Abfrage-ID 4, Status: erfolgreich), aber die Warn- und Gegenanzeigenfelder wurden nicht in das Evidence Pack eingefügt. Diese Daten müssen extrahiert werden, bevor die Sicherheitsbewertung fortgesetzt werden kann.

---

## Zytotoxizität

Binimetinib ist eine antineoplastische zielgerichtete Therapie. Die folgende Tabelle gibt bekannte Eigenschaften der Arzneimittelklasse wider.

| Element | Inhalt |
|---------|--------|
| Zytotoxizitätsklassifizierung | Zielgerichtete Therapie — MEK1/2-Kinase-Inhibitor (nicht-konventionelle Zytotoxika) |
| Myelosuppressions-Risiko | Niedrig bis moderat |
| Emetogenitätsklassifizierung | Niedrig |
| Zu überwachende Elemente | Blutbild mit Differenzierung, Leberfunktionstests (ALT/AST), CPK, EKG (QTc-Intervall), ophthalmologische Bewertung (retinale Ereignisse), Blutdruck |
| Handhabungsschutz | Standardmäßige Vorsichtsmaßnahmen zur Handhabung oraler Antineoplastika gelten |

---

## Sicherheitsaspekte

Bitte beachten Sie die Packungsbeilage für Sicherheitsinformationen.

Die TFDA-Packungsbeilage-Abfrage gab ein Ergebnis zurück, aber wichtige Warnungen und Gegenanzeigen wurden nicht in dieses Evidence Pack eingefügt (Datenlücke DG001, Schweregrad: Blockierend). Daten zu Arzneimittelwechselwirkungen wurden auch in der DDI-Datenbankabfrage nicht gefunden. Diese Lücken müssen behoben werden, bevor das Arzneimittel die Sicherheitsprüfung bestehen kann.

---

## Fazit und nächste Schritte

**Entscheidung: Zurückstellen**

**Begründung:**
Das Evidence Pack ist auf zwei Ebenen kritisch unvollständig: Das TxGNN-Modell hat keine vorhergesagten Indikationen zurückgegeben, und sowohl die Wirkmechanismus- als auch die Sicherheitsdatenfelder sind nicht ausgefüllt. Eine verantwortungsvolle Umwidmungsbewertung erfordert mindestens eine Kandidatenindikation und ein bestätigtes Sicherheitsprofil — keine dieser Bedingungen ist hier erfüllt.

**Um fortzufahren, wird Folgendes benötigt:**

- **\[Priorität 1\]** Führen Sie die TxGNN-Vorhersage-Pipeline für Binimetinib (DB11967) erneut aus und bestätigen Sie, dass das Modell eine gültige Arzneimitteleinbettung empfängt
- **\[Priorität 2\]** Parsen Sie die TFDA-Packungsbeilage-PDF, um wichtige Warnungen, Gegenanzeigen und Vorsichtsmaßnahmen zu extrahieren (behebt DG001 — derzeit blockierend)
- **\[Priorität 3\]** Befragen Sie die DrugBank-API nach vollständigen Wirkmechanismus-Daten (behebt DG002)
- **\[Priorität 4\]** Ergänzen Sie um internationalen Zulassungsstatus (FDA/EMA), um einen vollständigen behördlichen Kontext bereitzustellen, angesichts des Fehlens einer Taiwan-Zulassung

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

