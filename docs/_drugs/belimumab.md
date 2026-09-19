---
layout: default
title: Belimumab
parent: Nur Modellvorhersage (L5)
nav_order: 48
evidence_level: L5
indication_count: 6
---

# Belimumab
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **6** 
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

# Belimumab: Von Systemischem Lupus Erythematodes zur Primären Sekretionstörung von Blutplättchen

## Zusammenfassung in einem Satz

Belimumab ist ein gegen BAFF/BLyS gerichteter monoklonaler Antikörper, der ursprünglich zur Behandlung des Systemischen Lupus Erythematodes (SLE) verwendet wird, um das Überleben von B-Zellen und die Produktion von Autoantikörpern zu unterdrücken.
Das TxGNN-Modell sagt voraus, dass es möglicherweise wirksam gegen **primäre Sekretionstörung von Blutplättchen** sein könnte,
aber diese Richtung wird derzeit durch nur **1 klinische Studie** (mechanistisch unabhängig) und **0 Veröffentlichungen** gestützt.

---

## Schnellübersicht

| Element | Inhalt |
|--------|--------|
| Ursprüngliche Indikation | Systemischer Lupus Erythematodes (SLE) |
| Vorhergesagte neue Indikation | Primäre Sekretionstörung von Blutplättchen |
| TxGNN-Vorhersage-Score | 99.96% |
| Evidenzstufe | L5 |
| Marktstatus Deutschland | Nicht vermarktet |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | Zurückhalten |

---

## Warum ist diese Vorhersage angemessen?

Detaillierte DrugBank-Wirkungsmechanismus-Daten sind für Belimumab in diesem Evidenzpaket nicht verfügbar. Basierend auf der mechanistischen Begründung, die die Vorhersagen begleitet, ist bekannt, dass Belimumab als gegen BAFF/BLyS gerichteter monoklonaler Antikörper wirkt, der das Überleben von B-Zellen hemmt und die Erzeugung von Autoantikörpern reduziert, und auf dieser Grundlage ist es für SLE zugelassen.

Primäre Sekretionstörung von Blutplättchen ist ein hereditärer Defekt in der Granulasekretion von Blutplättchen — eine strukturelle/funktionelle Blutplättchenanomalie, keine durch B-Zellen oder Antikörper vermittelte Erkrankung. Es gibt keinen etablierten biologischen Weg, der die BAFF/B-Zell-Hemmung mit der Freisetzung von Blutplättchengranula verbindet. Der hohe Score des TxGNN-Modells für diese Indikation ist daher am ehesten ein Wissensgraph-Assoziationsartefakt und nicht eine echte mechanismusgesteuerte Hypothese.

Erwähnenswert ist, dass unter den sechs für Belimumab vorhergesagten Indikationen **fetale und neonatale alloimmune Thrombozytopenie (Rang 4)** eine vergleichsweise plausiblere mechanistische Begründung hat, da es sich um eine antikörperbedingte Erkrankung handelt — aber sie hat ebenfalls keine unterstützenden klinischen oder Literaturbelege zu diesem Zeitpunkt. Alle sechs Vorhersagen bleiben auf Evidenzstufe L5.

---

## Klinische Studienevidenz

| Studiennummer | Phase | Status | Einschluss | Wichtigste Ergebnisse |
|---------|------|------|------|---------|
| [NCT01610492](https://clinicaltrials.gov/study/NCT01610492) | Phase 2 | Abgeschlossen | 14 | Studie von Belimumab bei PLA2R-Antikörper-positiver idiopathischer membranöser Glomerulonephritis — **nicht verwandt mit Blutplättchenstörungen**; Datenbankindikationsabweichung, bewertet mit C (nicht unterstützend) |

---

## Literaturbelege

Derzeit sind keine entsprechenden Literaturbelege verfügbar.

---

## Marktinformationen Deutschland

Belimumab wird in Deutschland nach diesem Evidenzpaket nicht vermarktet (0 Zulassungen in der Akte).

---

## Sicherheitsüberlegungen

Bitte beachten Sie die Packungsbeilage für Sicherheitsinformationen.

---

## Fazit und nächste Schritte

**Entscheidung: Zurückhalten**

**Begründung:**
Trotz eines hohen TxGNN-Vorhersage-Scores befasst sich die einzige zugehörige klinische Studie mit einer unverwandten Indikation, es gibt keine unterstützende Literatur, und der vorgeschlagene Mechanismus (BAFF/B-Zell-Hemmung) hat keine etablierte Verbindung zu Sekretionstörungen von Blutplättchengranula. Die Evidenzbasis ist unzureichend, um weitere Bewertung zu rechtfertigen.

**Um voranzuschreiten, wird Folgendes benötigt:**
- Bestätigte MOA und DDI/Kontraindikationsdaten von DrugBank/Hersteller (aktuell als Blocking/High Datenlücken gekennzeichnet)
- Präklinische oder mechanistische Studien, die direkt die BAFF/B-Zell-Wege mit Defekten der Blutplättchengranulasekretion verbinden
- Echte krankheitsgerechte klinische Studien oder Fallberichte in Patientenpopulationen mit Blutplättchen-Sekretionstörungen
- Falls ein alternativer Wirkstoffkandidat verfolgt wird, Priorisierung der Neubewertung von **fetaler und neonataler alloimmune Thrombozytopenie**, die eine kohärentere (allerdings noch unbewiesene) mechanistische Hypothese hat

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

