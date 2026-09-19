---
layout: default
title: Selinexor
parent: Nur Modellvorhersage (L5)
nav_order: 360
evidence_level: L5
indication_count: 1
---

# Selinexor
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **1** 
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

# Selinexor: Von ursprünglicher Indikation (nicht dokumentiert) zu arzneimittelinduzierter Osteoporose

## Zusammenfassung in einem Satz

> Die ursprüngliche Indikation und der Wirkmechanismus von Selinexor sind **nicht verfügbar** im aktuellen Datensatz (markiert als Datenlücke).
> Das TxGNN-Modell sagt eine mögliche Assoziation mit **arzneimittelinduzierter Osteoporose** voraus, dies kommt jedoch mit **null unterstützenden klinischen Studien** und **null Literaturangaben**,
> und die semantische Beziehung selbst ist mehrdeutig — es ist unklar, ob dies eine *therapeutische* Wirkung oder ein *Nebenwirkungsrisiko* anzeigt.

---

## Schnellübersicht

| Element | Inhalt |
|------|------|
| Ursprüngliche Indikation | Nicht verfügbar (Datenlücke) |
| Vorhergesagte neue Indikation | Arzneimittelinduzierte Osteoporose |
| TxGNN-Vorhersage-Punktzahl | 99.22% |
| Evidenzstufe | L5 |
| Marktstatus in Deutschland | Nicht vermarktet (Nicht vermarktet) |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | Abwarten |

---

## Warum ist diese Vorhersage angemessen?

Derzeit sind detaillierte Daten zum Wirkmechanismus nicht verfügbar (in der Quellen-Evidenzsammlung als Datenlücke markiert). Auch die ursprüngliche Indikation ist nicht erfasst, was bedeutet, dass wir die bekannte Pharmakologie des Arzneimittels nicht gegen die vorhergesagte neue Indikation vergleichen können.

Noch wichtiger ist, dass die vorhergesagte Indikation selbst — „arzneimittelinduzierte Osteoporose" — in diesem Kontext semantisch mehrdeutig ist. Es ist nicht klar, ob das TxGNN-Modell vorschlägt, dass Selinexor **zur Behandlung** von arzneimittelinduzierter Osteoporose **eingesetzt werden könnte**, oder ob es **darauf hinweist, dass** Selinexor **selbst Osteoporose als Nebenwirkung induzieren könnte**. Diese beiden Interpretationen führen zu gegensätzlichen klinischen Schlussfolgerungen (ein therapeutischer Kandidat vs. ein Sicherheitssignal), und die Evidenzsammlung vermerkt ausdrücklich, dass diese Mehrdeutigkeit nicht geklärt wurde.

Angesichts des Fehlens von MOA-Daten, Daten zur ursprünglichen Indikation und etwaiger unterstützender Studien oder Literatur gibt es derzeit keine mechanistische oder klinische Grundlage, um die biologische Plausibilität dieser hohen Vorhersage-Punktzahl (0.992) zu bewerten. Die Punktzahl allein, ohne bestätigende Beweise, ist unzureichend, um das Voranbringen dieses Kandidaten zu rechtfertigen.

---

## Klinische Studienevidenz

Derzeit sind keine damit verbundenen klinischen Studien registriert.

---

## Literaturbeweise

Derzeit ist keine damit verbundene Literatur verfügbar.

---

## Marktinformationen zu Deutschland

Selinexor ist derzeit nicht auf dem deutschen Markt erhältlich (0 Zulassungen im Register); keine Lizenz- oder genehmigten Indikationsdaten sind verfügbar.

---

## Sicherheitsüberlegungen

Bitte beachten Sie die Packungsbeilage für Sicherheitsinformationen.

---

## Fazit und nächste Schritte

**Entscheidung: Abwarten**

**Begründung:**
Die Evidenzstufe beträgt L5 (nur Modellvorhersage, keine klinischen Studien oder Literatur), und zwei blockierende/schweregrad-hohe Datenlücken bleiben bestehen — TFDA-Warnungen/Kontraindikationen und Wirkmechanismus — zusätzlich zu einer ungeklärten Mehrdeutigkeit darüber, ob die vorhergesagte Assoziation eine therapeutische Möglichkeit oder ein Risiko für Nebenwirkungen darstellt.

**Um voranzukommen, ist Folgendes erforderlich:**
- Daten zur ursprünglichen Indikation und zum Wirkmechanismus (MOA) aus DrugBank
- TFDA/BfArM-Packungsbeilagendaten (Warnungen, Kontraindikationen) — derzeit blockierend für Sicherheitsüberprüfung
- Klarstellung darüber, ob „arzneimittelinduzierte Osteoporose" ein Behandlungsziel oder eine Risikoassoziation für Selinexor widerspiegelt
- Unabhängige Suche nach unterstützenden klinischen Studien oder Literatur, bevor dieser Kandidat über S0 hinaus vorangebracht werden kann

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

