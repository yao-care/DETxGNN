---
layout: default
title: Guanfacine
parent: Nur Modellvorhersage (L5)
nav_order: 220
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-14
description: "Guanfacine: vorhergesagte neue Indikation Faziodigitogenitales Syndrom (Aarskog-Scott-Syndrom) (Evidenzstufe L5). Ursprüngliche Indikation: Aufmerksamkeitsdefizit-/Hyperaktivitätsstörung (ADHS)"
monitor_inn: "Guanfacine"
predicted_indications: ["faciodigitogenital syndrome", "chondromyxoid fibroma", "trichotillomania", "manic bipolar affective disorder", "restless legs syndrome", "Tourette syndrome"]
---

# Guanfacine
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **7** 
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

# Guanfacin: Vom Aufmerksamkeitsdefizit-/Hyperaktivitätssyndrom (ADHS) zum Faziodigitogenitalen Syndrom

## Zusammenfassung

Guanfacin wurde ursprünglich zur Behandlung der Aufmerksamkeitsdefizit-/Hyperaktivitätsstörung (ADHS) zugelassen. Das TxGNN-Modell sagt voraus, dass es beim **Faziodigitogenitalen Syndrom** (Aarskog-Scott-Syndrom) wirksam sein könnte. Für diese Vorhersage liegen derzeit **keine klinischen Studien** und **keine Publikationen** vor; sie beruht ausschließlich auf der Modellberechnung.

---

## Schnellübersicht

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Aufmerksamkeitsdefizit-/Hyperaktivitätsstörung (ADHS) |
| Vorhergesagte neue Indikation | Faziodigitogenitales Syndrom (Aarskog-Scott-Syndrom) |
| TxGNN-Vorhersagewert | 99,97 % |
| Evidenzstufe | L5 |
| Marktstatus in Deutschland | Nur erloschene/aufgehobene Zulassungen (derzeit nicht vermarktet) |
| Anzahl der Zulassungen | 2 (beide aufgehoben) |
| Empfohlene Entscheidung | Hold (zurückstellen) |

---

## Warum ist diese Vorhersage nachvollziehbar?

Zum Wirkmechanismus liegen in den für diesen Bericht zusammengestellten Daten keine detaillierten Angaben vor. Pharmakologisch ist bekannt, dass Guanfacin an den α2-Adrenozeptoren (α2A, α2B, α2C) angreift. Die α2A-Agonie im präfrontalen Kortex unterstützt Aufmerksamkeit und exekutive Funktionen und bildet die Grundlage der zugelassenen ADHS-Anwendung.

Das Aarskog-Scott-Syndrom ist eine seltene genetische Erkrankung. Zu ihren Merkmalen gehören auch Verhaltensauffälligkeiten wie ADHS-Symptome. Daraus ergibt sich eine **indirekte, rein symptomatische Begründung**: Guanfacin könnte diese Verhaltensmerkmale beeinflussen, nicht aber die Grunderkrankung. Diese Überlegung ist bislang durch keine Daten belegt. Der hohe Vorhersagewert sollte daher als reine Rechenvorhersage verstanden werden.

---

## Klinische Evidenz

Derzeit sind keine zugehörigen klinischen Studien registriert.

---

## Literaturevidenz

Derzeit liegt keine zugehörige Literatur vor.

---

## Marktinformationen Deutschland

| Zulassungsnummer | Produktname | Darreichungsform | Zugelassene Indikation |
|---------|------|------|-----------|
| EMEA/H/C/003759 | Intuniv (Takeda Pharmaceuticals International AG, Irland) | – | Aufmerksamkeitsdefizit-/Hyperaktivitätsstörung (ADHS) |
| EMEA/H/C/006312 | Paxneury (Neuraxpharm Pharmaceuticals S.L.) | – | Aufmerksamkeitsdefizit-/Hyperaktivitätsstörung (ADHS) |

Beide Zulassungen haben den Status „aufgehoben".

---

## Sicherheitsaspekte

- **Kontraindikationen aus der Wissensgraph-Analyse** (TxGNN/PrimeKG, Beziehungen zwischen Wirkstoff und Erkrankung, **kein** Text aus der Fachinformation): Es werden Zusammenhänge mit folgenden Erkrankungen genannt:
  - Kreislauf- und Herzerkrankungen: orthostatische Hypotonie, posturales orthostatisches Tachykardiesyndrom, Hypotonie, Myokardinfarkt, Koronarthrombose, koronare Herzkrankheit, AV-Block bzw. AV-Dissoziation, Herzblock, zerebrovaskuläre Erkrankungen
  - Neurologische und psychische Erkrankungen: Multisystematrophie, Angststörung, neurotische Störung, dysthyme Störung
  - Organerkrankungen: Lebererkrankung, Gallenblasenerkrankung, chronische Nierenerkrankung, chronisches Nierenversagen, terminale Niereninsuffizienz
  - Sonstige: Hämoglobinopathie, Obstipation
- **Wechselwirkungen:** Die Abfrage lieferte keine Wechselwirkungen mit anderen Arzneimitteln, sondern nur pharmakologische Zielstrukturen: α2A-, α2B- und α2C-Adrenozeptor. Als klinische Anwendungen werden Bluthochdruck, ADHS und Angststörungen genannt.

Für Warnhinweise und weitere Sicherheitsinformationen ist die Fachinformation heranzuziehen.

---

## Fazit und nächste Schritte

**Entscheidung: Hold (zurückstellen)**

**Begründung:**
Für das Faziodigitogenitale Syndrom gibt es weder Studien noch Publikationen. Der hohe Vorhersagewert stützt sich allein auf das Modell, und die einzige mechanistische Überlegung (ADHS-ähnliche Verhaltensmerkmale) ist indirekt und nicht belegt.

**Für ein Weiterkommen ist Folgendes erforderlich:**
- Fachinformation (Warnhinweise, Gegenanzeigen) vom BfArM beschaffen und auswerten, da dies derzeit die Sicherheitsbewertung blockiert
- Detaillierte Wirkmechanismusdaten (z. B. über DrugBank) ergänzen
- Gezielte Literaturrecherche zu Verhaltenssymptomen beim Aarskog-Scott-Syndrom und zum Einsatz von α2-Agonisten
- Regulatorische Lage klären: Die deutschen Zulassungen sind aufgehoben, eine Wiederverfügbarkeit oder ein Einsatz außerhalb der Zulassung müsste geprüft werden
- Hinweis zur Priorisierung: Unter den weiteren vorhergesagten Indikationen ist das **Tourette-Syndrom** am besten belegt (zwei abgeschlossene Studien, darunter eine Phase-3-Studie mit 35 Teilnehmenden, sowie Leitlinienempfehlungen für α2-Agonisten bei Tics mit ADHS). Es wäre der naheliegendere Kandidat für eine vertiefte Bewertung.
## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

