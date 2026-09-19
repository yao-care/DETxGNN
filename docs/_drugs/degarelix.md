---
layout: default
title: Degarelix
parent: Nur Modellvorhersage (L5)
nav_order: 118
evidence_level: L5
indication_count: 10
---

# Degarelix
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

# Degarelix: Von der GnRH-Antagonisten-Therapie zur Hypertrichose

## Zusammenfassung in einem Satz

> Degarelix ist ein GnRH-(Gonadotropin-Releasing-Hormon-)Antagonist. Dieses Evidenzpaket enthält jedoch keine formalen Quellen für ursprüngliche Indikationen und Wirkmechanismus (Datenlücken DG001, DG002).
> Das TxGNN-Modell sagt voraus, dass es möglicherweise gegen **Hypertrichose (Hypertrichosis)** wirksam sein könnte,
> aber derzeit gibt es **keine klinischen Studien** und **keine direkt relevanten Fachliteraturquellen**, die diese Richtung unterstützen, und die Wirkmechanismus-Verbindung selbst wird als „äußerst schwache Schlussfolgerung" gekennzeichnet.

---

## Schnellübersicht

| Punkt | Inhalt |
|------|--------|
| Ursprüngliche Indikationen | Im Evidenzpaket nicht enthalten (`original_indications` ist ein leeres Array) |
| Vorhergesagte neue Indikationen | Hypertrichose (mehrfaches Haarwachstum) |
| TxGNN-Vorhersagescore | 99.99% (Rang 275) |
| Evidenzebene | L5 (nur Modellvorhersage, keine klinischen Studien oder Fachliteraturstütze) |
| Marktstatus | Nicht vermarktet |
| Zulassungsanzahl | 0 |
| Empfohlene Entscheidung | **Hold** |

---

## Warum diese Vorhersage möglicherweise/nicht vernünftig sein könnte

Die Datenbank stellt derzeit keinen formalen Wirkmechanismus zur Verfügung (MOA ist als Datenlücke markiert, DG002, Schweregrad Hoch) und keine Quellen für ursprüngliche Indikationen von Degarelix. Nach der öffentlichen pharmakologischen Klassifizierung gehört Degarelix zur Klasse der GnRH-Rezeptor-Antagonisten, die durch Hemmung der hypophysären LH/FSH-Sekretion die Keimdrüsenhormonkonzentrationen (wie Testosteron) senken. Dieses Hintergrundwissen ist jedoch nicht Teil der diesem Evidenzpaket beiliegenden Quelldaten, sondern dient nur als Referenz zum Verständnis der Modellausgaben und **sollte nicht als Grundlage für Sicherheits- oder Indikationserweiterungsentscheidungen herangezogen werden**.

Die an erster Stelle rangierte vorhergesagte Indikation Hypertrichose wird in ihrer `repurposing_rationale` klar erläutert: Falls es sich um androgen-getriebene erworbene Hypertrichose handelt, könnte theoretisch die Senkung des Testosterons möglicherweise das Haarwachstum verlangsamen, aber diese Schlussfolgerung ist „äußerst schwach" und die Ätiologie der Hypertrichose ist heterogen. **Es gibt keine direkte Fachliteratur oder Versuchsbelege**, die dies unterstützen. Dies bedeutet, dass diese Vorhersage derzeit nur auf der Ebene der Einbettungs-Ähnlichkeit (L5 / S0) steckenbleibt und noch keine überprüfbaren biologischen oder klinischen Belege für diese Indikation vorhanden sind.

Bemerkenswert ist, dass die an vierter Stelle rangierte Kandidatenindikation (parodontale/zahnartige entwicklungsbezogene Syndrome) zwar 20 Fachliteraturquellen aufweist, aber nach Überprüfung zeigt sich, dass alle diese rein allgemeine Parodontologie-Forschung sind (z. B. Zusammenhang zwischen Diabetes und Parodontalerkrankung, Richtlinien zur Parodontalbehandlung usw.), **erwähnen Degarelix oder GnRH-Antagonisten überhaupt nicht**. Dies ist Rauschen, das durch Schlüsselwortabgleich entsteht, und nicht drogenspezifische Belege. Die Wirkmechanismus-Verbindungen der übrigen Kandidatenindikationen (Ambras-Syndrom, Dandy-Walker-Missbildung, Haarschaft-Gen-Anomalien, Urtikaria, Pubertitas praecox usw.) werden auch alle als ohne vernünftige biologische Grundlage bewertet oder die Wirkmechanismus-Richtung ist entgegengesetzt (z. B. familiale männerlimitierte Pubertitas praecox ist eine Gonadotropin-unabhängige Pathologie, GnRH-Antagonisten können theoretisch nicht wirken).

---

## Klinische Studienbelege

Derzeit sind keine relevanten Studieneintragungen vorhanden.

---

## Fachliteraturbelege

Derzeit sind keine relevanten Fachliteraturdaten vorhanden.

---

## Marktzulassungsinformationen

Derzeit können keine Marktzulassungsdaten abgerufen werden (`total_licenses = 0`, Marktstatus: Nicht vermarktet).

---

## Sicherheitsüberlegungen

Bitte lesen Sie die Fachinformation für Sicherheitsinformationen.

(Die in diesem Evidenzpaket enthaltenen wichtigsten Warnhinweise, Kontraindikationen und Abfrageergebnisse zu Arzneimittelwechselwirkungen sind alle Datenlücken; `DG001` wurde als Blocking-Ebene markiert. Das Fehlen dieser Daten bedeutet, dass **eine S1-Sicherheitsbewertung nicht abgeschlossen werden kann**.)

---

## Schlussfolgerung und nächste Schritte

**Entscheidung: Hold**

**Begründung:**
Alle 10 vorhergesagten Indikationen dieses Kandidatenwirkstoffs sind L5-Ebene (reine Modellvorhersage, keine klinischen Studien oder vertrauenswürdigen Fachliteraturbelege). Die an erster Stelle rangierte Hypertrichose hat auch eine Wirkmechanismus-Verbindung, die selbst als „äußerst schwache Schlussfolgerung" bewertet wird. Gleichzeitig sind ursprüngliche Indikationen, MOA und Fachinformationen zur Sicherheit alle Datenlücken und reichen nicht aus, um irgendeine Indikation in die nächste Bewertungsphase voranzutreiben.

**Zur Fortsetzung müssen folgende Daten ergänzt werden:**
- TFDA (oder zuständige Behörden) offizielle Fachinformationen – Warnhinweise und Kontraindikationen (DG001, Blocking, erfordert Download und Analyse des offiziellen PDF)
- Formale Degarelix-Wirkmechanismus-Quellen, wie Abfrageergebnisse aus DrugBank API (DG002, Hoch)
- Direkte klinische Studien oder Wirkmechanismus-Forschungsliteratur für Hypertrichose oder andere Kandidatenindikationen (derzeit vollständig fehlend)
- Überprüfung der Fachliteratur-Abgleich-Logik der an vierter Stelle rangiert Kandidatenindikation, um Schlüsselwort-Rauschen zu vermeiden, das die Ressourcenverteilung der nachfolgenden Evidenzsammlungsarbeiten irreleitet

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

