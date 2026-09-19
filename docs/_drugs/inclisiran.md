---
layout: default
title: Inclisiran
parent: Nur Modellvorhersage (L5)
nav_order: 201
evidence_level: L5
indication_count: 10
---

# Inclisiran
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

# Inclisiran: Ursprüngliche Indikation nicht dokumentiert → Vorhergesagte Anwendung bei Kaliummangelerkrankung

## Zusammenfassung in einem Satz

> Die ursprüngliche zugelassene Indikation von Inclisiran und dessen Wirkmechanismus sind im vorliegenden Nachweispaket nicht verfügbar (gekennzeichnet als Datenlücken). Die höchstplatzierte Vorhersage des TxGNN-Modells für diesen Wirkstoff ist **Kaliummangelerkrankung**, aber diese Vorhersage wird derzeit durch **0 klinische Studien** und **0 Publikationen** gestützt — es handelt sich um einen reinen Modellscore ohne empirische Belege aus der Praxis.

---

## Schnellübersicht

| Posten | Inhalt |
|--------|--------|
| Ursprüngliche Indikation | Nicht verfügbar (keine zugelassenen Indikationen dokumentiert; Regulatorische Zulassungsliste ist leer) |
| Vorhergesagte neue Indikation | Kaliummangelerkrankung |
| TxGNN-Vorhersagescore | 99.93% |
| Evidenzstufe | L5 |
| Marktstatus Deutschland | Nicht vermarktet (Nicht vermarktet) |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | **Zurückstellen** |

---

## Warum ist diese Vorhersage angemessen?

Detaillierte Wirkmechanismus-Daten (MOA) für Inclisiran sind in diesem Nachweispaket nicht verfügbar — sie sind als **hochgradige Datenlücke** gekennzeichnet, die einen DrugBank-API-Abruf erfordert. Die ursprüngliche zugelassene Indikation ist auch in diesem Datensatz leer, und der Wirkstoff hat derzeit **null regulatorische Zulassungen** in Deutschland (Nicht vermarktet).

Da sowohl die ursprüngliche Indikation als auch der Wirkmechanismus hier undokumentiert sind, kann die mechanistische Plausibilität nicht aus ersten Prinzipien bewertet werden. Das Feld „Rationale" des Nachweispakets für diesen spezifischen Kandidaten ist explizit und unmissverständlich:

> „Kein bekannter PCSK9/siRNA-Mechanismus bezieht sich auf Kalium-Ionen-Homöostase; dies ist rein ein hoher TxGNN-Score ohne unterstützende Belege."

Zum Kontext: Andere Einträge in demselben Nachweispaket beschreiben Inclisiran als eine **PCSK9-gerichtete siRNA**, die hauptsächlich zur Senkung des LDL-Cholesterins verwendet wird — aber diese Wirkstoffklasse hat keine etablierte oder hypothetische Verbindung zum Kaliumhaushalt. Mit anderen Worten: Das Embedding-Modell hat einen hohen Ähnlichkeitsscore erzeugt, aber es gibt keine biologische Hypothese, klinische Studie oder Literatur, die Inclisirans bekannte Pharmakologie mit dieser vorhergesagten Indikation verbindet.

Angesichts des völligen Fehlens einer mechanistischen Begründung oder klinischen/literarischen Unterstützung sollte diese höchstplatzierte Vorhersage nur als **niedriges Konfidenz-Explorationssignal** behandelt werden.

---

## Klinische Studiennachweise

Derzeit keine verwandten klinischen Studien registriert.

---

## Literaturbelege

Derzeit keine verwandte Literatur verfügbar.

---

## Marktinformation Deutschland

Inclisiran wird derzeit **nicht vermarktet** in Deutschland gemäß diesem Nachweispaket — es gibt 0 registrierte Zulassungen und keine Zulassungsunterlagen zur Zusammenfassung.

---

## Sicherheitsaspekte

Bitte beachten Sie die Gebrauchsinformation für Sicherheitsinformationen.

---

## Schlussfolgerung und nächste Schritte

**Entscheidung: Zurückstellen**

**Begründung:**
Die höchstplatzierte vorhergesagte Indikation (Kaliummangelerkrankung) hat null klinische Studien und null Literaturunterstützung (L5 — nur Modellvorhersage), und der Wirkstoff selbst fehlen grundlegende Referenzdaten (ursprüngliche Indikation, Wirkmechanismus, Sicherheitskennzeichnung), die sogar eine mechanistische Plausibilitätsbewertung ermöglichen würden. Es gibt derzeit keine verwertbaren Belege, um diesen Kandidaten voranzubringen.

**Zur Fortführung ist Folgendes erforderlich:**
- Abruf der TFDA/EMA-Gebrauchsinformation (Warnhinweise, Kontraindikationen) — derzeit eine **Blockierende** Datenlücke (DG001)
- Abruf des bestätigten Wirkmechanismus über DrugBank-API — derzeit eine **hochgradige** Datenlücke (DG002)
- Bestätigung der tatsächlichen zugelassenen Indikation(en) von Inclisiran, da dieses Nachweispaket keine dokumentiert hat
- **Datenqualitäts-Flag für dieses Paket**: Ein separater Kandidat im gleichen Datensatz (Rang 8, „Aortenmissbildung", L2/S1) zitiert zwei Phase-3-Studien (NCT06597019, NCT06597006) — aber beide Studien untersuchen tatsächlich **pädiatrische familiäre Hypercholesterinämie**, nicht Aortenmissbildung. Dies deutet auf ein Indikations-Verknüpfungs-Missverständnis in der Evidence-Pipeline hin, das korrigiert werden sollte, bevor dieser Kandidat (oder ein anderer in diesem Paket) als „L2"-Unterstützung zitiert wird
- Falls eine tatsächlich evidence-gestützte Neupositionierungsrichtung für Inclisiran benötigt wird, sind die oben erwähnten familiär-Hypercholesterinämie-bezogenen Studien ein vielversprechenderer Ausgangspunkt als die aktuelle höchstplatzierte, null-evidence-Vorhersage

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

