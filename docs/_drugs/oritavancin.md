---
layout: default
title: Oritavancin
parent: Nur Modellvorhersage (L5)
nav_order: 283
evidence_level: L5
indication_count: 3
---

# Oritavancin
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **3** 
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

# Oritavancin: Von nicht dokumentierter ursprünglicher Indikation zu Bacteroidaceae-Infektionskrankheiten

## Zusammenfassung in einem Satz

> Oritavancin ist ein Lipoglykopeptid-Antibiotikum; seine ursprüngliche Indikation ist in diesem Evidenzbericht nicht dokumentiert, und das Medikament ist derzeit in dieser Gerichtsbarkeit nicht im Handel.
> Das TxGNN-Modell sagt voraus, dass es möglicherweise wirksam gegen **Bacteroidaceae-Infektionskrankheiten** ist,
> aber **keine klinischen Studien** und **keine Literatur** unterstützen derzeit diese Richtung, und der eigene Wirkmechanismus des Medikaments spricht dagegen.

---

## Schnellerblick

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Nicht verfügbar – keine Zulassungs-/Indikationsdaten vorhanden (nicht im Handel) |
| Vorhergesagte neue Indikation | Bacteroidaceae-Infektionskrankheiten |
| TxGNN-Vorhersage-Score | 99.48% |
| Evidenzgrad | L5 (nur Modellvorhersage, keine Studien oder Literatur) |
| Marktstatus Deutschland | ✗ Nicht im Handel |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | Abwarten |

---

## Warum ist diese Vorhersage sinnvoll?

Detaillierte Wirkmechanismus-Daten sind als Datenlücken gekennzeichnet, aber die eigene mechanistische Begründung dieses Berichts ist aussagekräftig: Oritavancin ist ein **Lipoglykopeptid**-Antibiotikum, das an das D-Ala-D-Ala-Ende von Peptidoglykan-Vorläufern bindet und die Synthese der bakteriellen Zellwand hemmt. Dieser Mechanismus wirkt nur gegen **grampositiv**e Organismen.

**Bacteroidaceae** sind gramnegative Anaerobier, deren Außenmembran das Eindringen großer Glykopeptid-Moleküle blockiert – mechanistisch sollte Oritavancin gegen diese Pathogenfamilie nicht wirksam sein. Der Begründungstext kennzeichnet dies explizit als wahrscheinlich **TxGNN-Falsch-Positiv**, das dadurch entsteht, dass sich Medikament und Krankheit als graphisch benachbarte „Infektionskrankheit"-Knoten befinden, anstatt einen echten pharmakologischen Mechanismus zu teilen.

Die zwei anderen Kandidaten in diesem Bericht (ophthalmischer Herpes zoster – eine Virusinfektion – und *Mycoplasma pneumoniae*-Pneumonie – ein Zellwand-defizientes Bakterium) zeigen das gleiche Muster: hohe TxGNN-Werte gepaart mit mechanistischer Inkompatibilität und null klinischer/Literatur-Unterstützung. Dies ist kein Fall eines plausiblen Signals, das auf Evidenz wartet – der Mechanismus selbst spricht gegen die Vorhersage.

---

## Evidenz aus klinischen Studien

Derzeit sind keine verwandten klinischen Studien registriert.

---

## Literaturbeweise

Derzeit ist keine verwandte Literatur verfügbar.

---

## Informationen zum deutschen Markt

Oritavancin ist in dieser Gerichtsbarkeit nicht im Handel – es sind keine Zulassungsunterlagen verfügbar.

---

## Sicherheitserwägungen

Bitte lesen Sie die Packungsbeilage für Sicherheitsinformationen.

---

## Fazit und nächste Schritte

**Entscheidung: Abwarten**

**Begründung:**
Die am höchsten eingestufte Vorhersage (Bacteroidaceae-Infektionskrankheiten) ist mechanistisch mit dem reinen Grampositiv-Spektrum von Oritavancin unvereinbar, wird durch keinerlei klinische Studien oder Literatur gestützt und spiegelt die L5-Stufe (nur Vorhersage) von TxGNN wider. Die zwei anderen Kandidaten in diesem Bericht zeigen das gleiche Muster mechanistischer Implausibilität, was auf einen systematischen Falsch-Positiv-Cluster statt eines echten Repurposing-Signals hindeutet.

**Um fortzufahren, ist Folgendes erforderlich:**
- Bestätigte Wirkmechanismus- und ursprüngliche Indikationsdaten aus DrugBank/Regulierungsquellen (derzeit als Datenlücken gekennzeichnet)
- TFDA-/Regulierungs-Etikett-Warnungen und Kontraindikationen (blockierende Lücke – erforderlich vor S1-Sicherheitsscreening)
- Unabhängige mikrobiologische oder In-vitro-Evidenz für Aktivität gegen Bacteroidaceae, wenn dieser Kandidat weiterverfolgt werden soll
- Angesichts der mechanistischen Warnsignale wird empfohlen, diesen Kandidaten zugunsten von Vorhersagen mit höherem Evidenzgrad an anderer Stelle in der Pipeline herabzustufen

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

