---
layout: default
title: Simoctocog Alfa
parent: Nur Modellvorhersage (L5)
nav_order: 365
evidence_level: L5
indication_count: 10
---

# Simoctocog Alfa
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

# Simoctocog Alfa: Von Hämophilie A zur Pseudo-von-Willebrand-Krankheit

## Zusammenfassung in einem Satz

> Simoctocog alfa ist ein Präparat mit rekombinanter humaner Gerinnungsfaktor VIII (rFVIII), dessen etablierte therapeutische Klasse Hämophilie A ist.
> Die am höchsten bewertete Vorhersage des TxGNN-Modells deutet auf die **Pseudo-von-Willebrand-Krankheit** hin,
> aber diese Richtung wird derzeit durch **0 klinische Studien** und **0 Publikationen** unterstützt, und die eigene mechanistische Bewertung des Evidenzpakets spricht gegen biologische Plausibilität.

---

## Schnellübersicht

| Element | Inhalt |
|------|------|
| Ursprüngliche Indikation | Hämophilie A (rFVIII-Ersatztherapie) – keine deutschen Lizenzdaten verfügbar, um genaue genehmigte Formulierung zu bestätigen |
| Vorhergesagte neue Indikation | Pseudo-von-Willebrand-Krankheit |
| TxGNN-Vorhersagepunktzahl | 99.997% |
| Evidenzstufe | L5 (nur Modellvorhersage, keine unterstützenden Studien oder Literatur) |
| Deutschland-Marktstatus | Nicht vermarktet |
| Anzahl der Genehmigungen | 0 |
| Empfohlene Entscheidung | Zurückstellen |

---

## Warum ist diese Vorhersage angemessen?

Derzeit sind keine detaillierten Wirkmechanismus-Daten für simoctocog alfa verfügbar (`original_moa: [Data Gap]`). Basierend auf bekannten Informationen in diesem Evidenzpaket (siehe Begründung des Kandidaten Rang 9) ist simoctocog alfa ein Präparat mit rekombinanter humaner Gerinnungsfaktor VIII (rFVIII), dessen etablierte Anwendung die Ersatztherapie bei Hämophilie A ist – eine Erkrankung, die durch absoluten oder relativen Mangel an Gerinnungsfaktor VIII verursacht wird.

Die Pseudo-von-Willebrand-Krankheit (Pseudo-VWD) ist dagegen überhaupt kein Gerinnungsfaktormangel. Sie resultiert aus einer Gain-of-Function-Mutation im Thrombozyten-Glykoprotein-Ib-(GPIb)-Rezeptor, die dazu führt, dass Thrombozyten den Plasma-von-Willebrand-Faktor mit abnorm hoher Affinität binden. Die eigene Analyse der mechanistischen Verbindung des Evidenzpakets merkt ausdrücklich an, dass die rFVIII-Supplementation für diese Erkrankung „keine klare mechanistische Grundlage" hat, und wirft sogar ein **theoretisches Risiko** aus veränderten vWF/FVIII-Komplexwechselwirkungen im Plasma auf.

Zusammengefasst spiegelt der sehr hohe TxGNN-Score sehr wahrscheinlich die Komorbiditäts-Clusterung auf Graph-Ebene unter Blutungsstörungen im Wissensgraph wider, anstatt ein echtes mechanismusgesteuertes Signal zu sein. Unter den zehn bereitgestellten Kandidaten ist **Rang 9 („Hämophilie A mit vaskulärer Abnormität")** der einzige mit einer inhärent plausiblen mechanistischen Begründung, da er in FVIIIs bekanntes mechanistisches Wirkungsgebiet fällt – aber er hat ebenfalls bis heute keine unterstützenden Studien oder Literatur.

---

## Klinische Studienevidenz

Derzeit keine verknüpften klinischen Studien registriert

---

## Literaturbelege

Derzeit keine verknüpfte Literatur verfügbar

---

## Deutschland-Marktinformationen

Dieses Produkt wird derzeit nicht in Deutschland vermarktet (`market_status: Not marketed`, `total_licenses: 0`). Es sind keine Zulassungsunterlagen zur Überprüfung verfügbar.

---

## Sicherheitsüberlegungen

Bitte beachten Sie die Packungsbeilage für Sicherheitsinformationen.

*(Hinweis: `safety.key_warnings` und `safety.contraindications` sind beide als Datenlücken in diesem Evidenzpaket gekennzeichnet, und es wurden keine Arzneimittel-Wechselwirkungsunterlagen gefunden – `ddi.query_status: not_found`.)*

---

## Schlussfolgerung und nächste Schritte

**Entscheidung: Zurückstellen**

**Begründung:**
Alle zehn vom TxGNN vorhergesagten Indikationen für simoctocog alfa befinden sich auf Evidenzstufe L5 – nur Modellvorhersage, ohne unterstützende klinische Studien oder Literatur insgesamt. Für den am höchsten bewerteten Kandidaten beschreibt die eigene Umwidmungsrationale des Arzneimittels die mechanistische Verbindung als fehlend oder sogar richtungsmäßig widersprüchlich, und eine kritische Sicherheitsdatenlücke (DG001, fehlende Warnhinweise/Kontraindikationen, Schweregrad: Blocking) verhindert jede S1-Sicherheitsvorabprüfung.

**Um fortzufahren, ist Folgendes erforderlich:**
- Beheben Sie DG001 (Blocking): Besorgen und analysieren Sie die offizielle Packungsbeilage auf Warnhinweise/Kontraindikationen, bevor weitere Sicherheitsüberprüfungen durchgeführt werden können
- Beheben Sie DG002: Beschaffen Sie detaillierte MOA-Dokumentation von DrugBank oder Herstellerquellen
- Durchsuchen Sie klinische Studienregister (ClinicalTrials.gov, ICTRP) und Literaturdatenbanken speziell auf rFVIII-Verwendung bei Thrombozyten-Funktionsstörungen (Pseudo-VWD, Glanzmann-Thrombasthenie, Scott-Syndrom), um zu testen, ob das TxGNN-Signal irgendein reales investigatives Interesse widerspiegelt
- Falls Sie einen Umwidmungskandidaten überhaupt verfolgen, priorisieren Sie die Neubewertung oder manuelle Überprüfung von **Rang 9 (Hämophilie A mit vaskulärer Abnormität)**, das sich in FVIIIs bekanntem mechanistischen Wirkungsgebiet befindet und leichter zu rechtfertigen ist als der aktuelle am höchsten bewertete Kandidat, trotz derzeit fehlender Studien-/Literaturunterstützung

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

