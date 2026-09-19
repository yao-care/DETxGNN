---
layout: default
title: Lipegfilgrastim
parent: Nur Modellvorhersage (L5)
nav_order: 234
evidence_level: L5
indication_count: 5
---

# Lipegfilgrastim
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

# Lipegfilgrastim: Von der Unterstützung der Neutrophilenproduktion zur primären Blutplättchen-Freisetzungsstörung

## Zusammenfassung in einem Satz

> Lipegfilgrastim ist ein pegylierter G-CSF-Analogstoff, dessen etablierte biologische Rolle die Stimulation der Neutrophilenproduktion (Granulozyten) ist; ein formales Originalindikations-Datensatz ist nicht in diesem Nachweispaket vorhanden.
> Das TxGNN-Modell prognostiziert, dass es möglicherweise wirksam sein kann für **primäre Freisetzungsstörung von Blutplättchen**,
> aber **0 klinische Versuche** und **0 Publikationen** unterstützen diese Richtung derzeit – die Prognose ist nur Modellausgabe.

## Schnellübersicht

| Element | Inhalt |
|---------|--------|
| Ursprüngliche Indikation | Nicht formal dokumentiert (kein `original_indications`-Datensatz); mechanistisch wird das Arzneimittel als G-CSF-Rezeptor-Agonist beschrieben, der die Neutrophilen-Proliferation/Differenzierung unterstützt |
| Prognostizierte neue Indikation | Primäre Freisetzungsstörung von Blutplättchen |
| TxGNN-Prognosewert | 99.93% |
| Evidenzstufe | L5 |
| Marktstatus Deutschland | ✗ Nicht auf dem Markt |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | Aussetzen |

## Warum ist diese Prognose sinnvoll?

Derzeit sind detaillierte Wirkmechanismus-Daten nicht verfügbar (`original_moa` ist eine Datenlücke). Basierend auf den in diesem Nachweispaket vorliegenden Informationen ist Lipegfilgrastim ein pegylierter G-CSF-Analogstoff, der am G-CSF-Rezeptor wirkt, um die Granulozyten-(Neutrophilen-)Proliferation und -Differenzierung zu fördern. Dies ist ein gut definierter Effekt auf die myeloide Reihe, kein Effekt auf die Blutplättchen-Reihe.

Kritisch ist, dass das Nachweispaket selbst besagt, dass es **keine bekannte mechanistische Verbindung** zwischen G-CSF-Rezeptor-Signalisierung und Blutplättchen-Freisetzung/Granula-Defekten gibt – die prognostizierte Indikation „primäre Freisetzungsstörung von Blutplättchen" beinhaltet eine unterschiedliche Pathophysiologie (Defekte bei der Freisetzung dichter/Alpha-Granula in Blutplättchen), die sich nicht mit der Granulozyten-Kolonien-Stimulation überlappt. Der Prognosewert wird daher rein durch das TxGNN-Graphenmodell angetrieben, ohne unterstützende Nachweise aus klinischen Versuchen, Fachliteratur oder biologischer Rationale.

Angesichts des Fehlens einer plausiblen mechanistischen Verbindung und fehlender unterstützender Nachweise sollte dieser Kandidat nur als exploratives Signal behandelt werden, nicht als Arzneimittel-Umpositionierungs-Hypothese, die für weitere Verfolgung bereit ist.

## Evidenz aus klinischen Versuchen

Derzeit sind keine zugehörigen klinischen Versuche registriert

## Evidenz aus der Fachliteratur

Derzeit ist keine zugehörige Fachliteratur verfügbar

## Marktinformationen für Deutschland

Lipegfilgrastim hält derzeit keine Marktzulassungen in diesem Datensatz (`total_licenses: 0`); der Marktstatus wird als nicht auf dem Markt dokumentiert. Es sind keine Zulassungsunterlagen verfügbar, die zusammengefasst werden können.

## Sicherheitsaspekte

Bitte entnehmen Sie Sicherheitsinformationen der Packungsbeilage.

*(Hinweis: TFDA/BfArM-Etikett-Warnungen und Kontraindikationen werden in diesem Nachweispaket als **blockierende** Datenlücke (DG001) gekennzeichnet – dies muss behoben werden, bevor eine S1-Sicherheitsprüfung durchgeführt werden kann.)*

## Schlussfolgerung und nächste Schritte

**Entscheidung: Aussetzen**

**Begründung:**
Die Evidenzstufe ist L5 (nur Modellprognose), mit null klinischen Versuchen oder Fachliteratur, und das Nachweispaket selbst erklärt ausdrücklich, dass es keine bekannte mechanistische Beziehung zwischen der G-CSF-Wirkung des Arzneimittels und der prognostizierten Blutplättchen-Freisetzungsstörung gibt. Es gibt derzeit keine Grundlage, diesen Kandidaten voranzutreiben.

**Um fortzufahren, ist Folgendes erforderlich:**
- Formale Wirkmechanismus-Daten (MOA) von DrugBank (DG002 – hoher Schweregrad)
- TFDA/BfArM-Etikett-Warnungen und Kontraindikationen (DG001 – blockierender Schweregrad)
- Eine biologisch plausible Rationale, die G-CSF-/Granulozyten-Pfade mit Blutplättchen-Freisetzungsstörungen verbindet, idealerweise unterstützt durch präklinische Daten
- Mindestens Fallberichte oder Beobachtungsdaten, bevor weitere Bewertung in Betracht gezogen wird
- Bestätigung der tatsächlich ursprünglichen zugelassenen Indikationen des Arzneimittels, die derzeit in den Quelldaten fehlen

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

