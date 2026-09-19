---
layout: default
title: Sevoflurane
parent: Nur Modellvorhersage (L5)
nav_order: 362
evidence_level: L5
indication_count: 10
---

# Sevoflurane
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

# Sevoflurane: Von der Allgemeinanästhesie zur Prinzmetal-Angina

## Zusammenfassung in einem Satz

Sevoflurane ist ein in der klinischen Praxis weit verbreitetes inhalatives Allgemeinanästhetikum zur Anästhesieeinleitung und -aufrechterhaltung.
Das TxGNN-Modell sagt voraus, dass es möglicherweise therapeutisches Potenzial für **Prinzmetal-Angina (vasospastische Angina)** besitzt,
aber derzeit existieren **keine klinischen Studien und keine Literaturbelege**, die diese Richtung unterstützen – es handelt sich um ein reines Netzwerk-Extrapolationsergebnis des Modells.

---

## Schnellübersicht

| Element | Inhalt |
|---------|--------|
| Ursprüngliche Indikation | Anästhesieeinleitung und -aufrechterhaltung (inhalatives Anästhetikum; dieser Evidence Pack enthält keine formalen Fachinformationstexte zur ursprünglichen Indikation) |
| Vorhergesagte neue Indikation | Prinzmetal Angina (vasospastische Angina) |
| TxGNN-Vorhersagepunktzahl | 99.78% |
| Evidenzebene | L5 (nur Modellvorhersage, keine tatsächliche Forschung) |
| Status auf dem taiwanesischen Markt | Nicht vermarktet |
| Anzahl der Lizenzen | 0 |
| Empfohlene Entscheidung | **Hold** |

---

## Warum wirkt diese Vorhersage plausibel?

Derzeit liegen für Sevoflurane noch keine strukturierten Daten zu den detaillierten Wirkmechanismen (MOA) vor (DrugBank-Abfrage steht noch aus),
aber basierend auf bekannter klinischer Pharmakologie kann Sevoflurane als inhalatives Anästhetikum nachweislich durch Aktivierung von **ATP-sensitiven Kaliumkanälen (K_ATP-Kanal)**
die „anästhetische Präkonditionierung (anesthetic preconditioning)" induzieren, die einen gewissen Schutzeffekt vor myokardialer Ischämie bietet – dies ist ein bekannter unterstützender Effekt in der Herzanästhesie.

Der pathophysiologische Kern der Prinzmetal-Angina liegt jedoch bei der **Koronararterienspasmus**, wobei therapeutische Mechanismen auf die Regulierung von Kalziumionenkanälen der vaskulären glatten Muskulatur ausgerichtet sind (wie Kalziumkanalblocker).
Dies stellt eine andere Ebene des Wirkmechanismus dar als die durch anästhetische Präkonditionierung vermittelte „myokardiale Ischämietoleranz". Zwischen beiden existiert nur eine indirekte Verbindung durch das Konzept des „myokardialen Schutzes",
und es gibt keinen direkten Beweis dafür, dass Sevoflurane selbst Koronararterienspasmus lindern oder verhindern kann. Diese Vorhersage sollte als statistische Extrapolation des TxGNN-Wissensgraphen betrachtet werden,
nicht als evidence-basierte Wirkmechanismus-Hypothese.

---

## Belege aus klinischen Studien

Derzeit sind keine registrierten klinischen Studien zu diesem Thema vorhanden.

---

## Literaturbelege

Derzeit sind keine Literaturbelege verfügbar.

---

## Informationen zum taiwanesischen Markt

Sevoflurane wurde in diesem Datensatz **bislang noch nicht auf dem taiwanesischen Markt zugelassen**, daher können keine Lizenzierungsdaten aufgeführt werden (`total_licenses = 0`).

---

## Sicherheitsüberlegungen

Die wesentlichen Sicherheitsdaten für dieses Kandidatenarzneimittel (TFDA-Fachinformationen Warnhinweise, Kontraindikationen, Arzneimittelwechselwirkungen) sind **derzeit noch nicht verfügbar**,
und diese Lücke wurde als **Blocking (DG001)** gekennzeichnet – bis diese geschlossen werden, ist ein Übergang zur nächsten Phase der Sicherheitsinitialbeurteilung (S1) nicht möglich.
Es wird empfohlen, zunächst die offiziellen Fachinformationen von der BfArM-Website herunterzuladen und die Warnhinweise und Kontraindikationen zu analysieren.

Bis die Daten ergänzt sind, sollten Sie bitte die Warnhinweise und Vorsichtsmaßnahmen aus der Originalfachinformation (package insert) als Grundlage heranziehen.

---

## Schlussfolgerung und nächste Schritte

**Entscheidung: Hold**

**Begründung:**
Die höchstbewertete vorhergesagte Indikation (Prinzmetal angina) verfügt über völlig mangelnde Belege aus klinischen Studien oder Literatur zur Unterstützung, der Wirkmechanismus-Zusammenhang ist schwach und basiert auf indirekten Rückschlüssen;
gleichzeitig fehlen dem Kandidatenarzneimittel TFDA-Fachinformationen zu Sicherheitsaspekten (Blocking-Level-Lücke), weshalb es nicht in die Sicherheitsinitialbeurteilung eingehen kann.
Zur Verdeutlichung: Die übrigen 9 vorhergesagten Indikationen in diesem Evidence Pack (Tourette-Syndrom, Fibromyalgie, Tendinitis,
idiopathische granulomatöse Myositis, Myositis fibrosa, nephrogenes SIAD, Trichotillomanie,
Migräne-Störung, Myositis mit Einschlüssen) sind ebenfalls alle Hold, und die bestehende Literatur besteht überwiegend aus „Patientenfall- und Folgeberichten über Operationen unter Anästhesie aufgrund der ursprünglichen Erkrankung" oder
Vergleichsstudien von Anästhesieverfahren, die durch Verwechslung von Arzneimittelnamen und Krankheitsnamen entstehen (confounding), und stellen keine therapeutischen Belege dar.
Nephrogenes SIAD könnte sogar durch die bei der Sevoflurane-Metabolisierung entstehenden anorganischen Fluorid-Ionen verursachte Nierentoxizität zu einer potenziellen Kontraindikationsrichtung führen.

**Falls fortgefahren werden soll, müssen folgende Daten ergänzt werden:**
- TFDA-Fachinformationen PDF-Analyse zur Beschaffung von Warnhinweisen und Kontraindikationen (DG001, Blocking)
- DrugBank-API-Abfrage für vollständige Wirkmechanismus-Daten (DG002, High)
- Falls die Prinzmetal-Angina-Hypothese validiert werden soll, müssen Mechanismus-Forschungen auf in-vitro-/Tier-Ebene zur Koronararterien-Glattmuskulatur ergänzt werden, als Voraussetzung für die Einleitung prospektiver klinischer Beobachtungen

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

