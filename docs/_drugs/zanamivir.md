---
layout: default
title: Zanamivir
parent: Nur Modellvorhersage (L5)
nav_order: 504
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-12
description: "Zanamivir: vorhergesagte neue Indikation Pyelonephritis (Evidenzstufe L5). Ursprüngliche Indikation: Influenza (humane Influenza)"
monitor_inn: "ZANAMIVIR"
predicted_indications: ["pyelonephritis", "disorder of tyrosine metabolism"]
---

# Zanamivir
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **2** 
{: .fs-6 .fw-300 }

---

## Inhaltsverzeichnis
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmazeutischer Bewertungsbericht

</div>

## Zanamivir: Von Influenza zu Pyelonephritis
{: .text-alpha }

## Zusammenfassung

Zanamivir ist ein Neuraminidase-Hemmer, der ursprünglich zur Behandlung der humanen Influenza eingesetzt wurde. Das TxGNN-Modell sagt voraus, dass es bei **Pyelonephritis** wirksam sein könnte. Dafür liegen jedoch **keine klinischen Studien** und **keine Publikationen** vor; die Vorhersage stützt sich allein auf den Modellscore.

---

## Kurzüberblick

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Influenza (humane Influenza) |
| Vorhergesagte neue Indikation | Pyelonephritis |
| TxGNN-Vorhersagescore | 0,9984 |
| Evidenzlevel | L5 |
| Marktstatus in Deutschland | Im Handel (gültige Zulassungen: 1 von 1) |
| Anzahl der Zulassungen | 1 (gültig: 1) |
| Empfohlene Entscheidung | Hold |

---

## Warum ist diese Vorhersage (nicht) plausibel?

Zu Zanamivir liegen in den für diesen Bericht zusammengestellten Daten derzeit keine detaillierten Angaben zum Wirkmechanismus vor. Bekannt ist, dass Zanamivir ein viraler Neuraminidase-Hemmer ist, dessen Wirksamkeit bei Influenza belegt ist.

Pyelonephritis ist dagegen überwiegend eine bakterielle Infektion der Niere, meist durch *E. coli*. Ein plausibler Mechanismus, der beide Erkrankungen verbindet, ist nicht erkennbar. Bakterielle Neuraminidasen (Sialidasen) werden zwar gelegentlich als Virulenzfaktoren diskutiert, für Zanamivir ist aber keine etablierte Wirkung gegen sie bei Harnwegsinfektionen belegt.

Die Vorhersage ist daher vermutlich ein Artefakt des TxGNN-Modells (Deep Learning), das auf der gemeinsamen Kategorie „Infektion“ beruht und nicht auf einem biologischen Zusammenhang.

---

## Evidenz aus klinischen Studien

Derzeit sind keine zugehörigen klinischen Studien registriert.

---

## Evidenz aus der Literatur

Derzeit ist keine zugehörige Literatur verfügbar.

---

## Informationen zum Markt in Deutschland

| Zulassungsnummer | Produktname | Darreichungsform | Zugelassene Indikation |
|---------|------|------|-----------|
| EMEA/H/C/004102 | Dectova | – | Influenza (humane Influenza) |

Der Hersteller ist GlaxoSmithKline Trading Services Limited.

<!-- review:begin de-lic-20261106-zanamivir-1 -->

> **Prüfkorrektur (2026-11-06)**: Ursprünglich stand hier: „Diese Zulassung ist aufgehoben (Status: cancelled), der Hersteller ist GlaxoSmithKline Trading Services Limited.“ Entfernt: Die Aussage widersprach den Zulassungsdaten (EMA-Daten zu zentral zugelassenen Arzneimitteln, Stand 2026-11-06). In den Daten (EMA-Daten zu zentral zugelassenen Arzneimitteln) sind für dieses Arzneimittel 1 Zulassungen erfasst, davon 1 gültig; die aktuellen Zahlen stehen in der Schnellübersicht und bei den Marktinformationen. Quelle: [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx).

<!-- review:end de-lic-20261106-zanamivir-1 -->

---

## Sicherheitsaspekte

- **Kontraindikationen aus dem Wissensgraphen (kein Packungsbeilagentext):** Im TxGNN-Wissensgraphen (PrimeKG) sind Kontraindikationskanten zu folgenden Erkrankungen hinterlegt: Epilepsie, chronisch obstruktive Lungenerkrankung (COPD), schwere früh beginnende COPD, Bronchialerkrankungen und Delir.
- **Arzneimittelwechselwirkungen:** Es wurden 8 Wechselwirkungen gefunden (Quelle: DDInter).
  - Moderat: Insulin human (inhalativ, schnell wirksam)
  - Schweregrad unbekannt: Clarithromycin, Loratadin, Montelukast, Ketotifen, Fexofenadin, Ibuprofen, Diclofenac

Für weitere Sicherheitsinformationen, insbesondere Warnhinweise und Gegenanzeigen, ist die Packungsbeilage bzw. Fachinformation heranzuziehen.

---

## Fazit und nächste Schritte

**Entscheidung: Hold**

**Begründung:**
Die Vorhersage beruht ausschließlich auf einem hohen Modellscore (Evidenzlevel L5), ohne klinische Studien und ohne Literatur. Es gibt keinen plausiblen Wirkmechanismus zwischen einem viralen Neuraminidase-Hemmer und einer überwiegend bakteriellen Nierenentzündung. Zudem ist das Arzneimittel in Deutschland derzeit im Handel (1 von 1 Zulassungen gültig).

**Für ein Weiterverfolgen sind folgende Punkte erforderlich:**
- Belastbare Daten zum Wirkmechanismus (MOA) von Zanamivir
- Präklinische Belege für eine Wirkung gegen Erreger der Pyelonephritis (z. B. bakterielle Sialidasen)
- Auswertung der Warnhinweise und Gegenanzeigen aus der Fachinformation, da diese Daten fehlen und ein Sicherheits-Screening bislang nicht möglich ist
- Klärung der Verfügbarkeit und Darreichungsform

<!-- review:begin de-lic-20261106-zanamivir-2 -->

> **Prüfkorrektur (2026-11-06)**: Ursprünglich stand hier: „Klärung der Verfügbarkeit und Darreichungsform, da die einzige deutsche Zulassung aufgehoben ist“ Entfernt: Die Aussage widersprach den Zulassungsdaten (EMA-Daten zu zentral zugelassenen Arzneimitteln, Stand 2026-11-06). In den Daten (EMA-Daten zu zentral zugelassenen Arzneimitteln) sind für dieses Arzneimittel 1 Zulassungen erfasst, davon 1 gültig; die aktuellen Zahlen stehen in der Schnellübersicht und bei den Marktinformationen. Quelle: [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx).

<!-- review:end de-lic-20261106-zanamivir-2 -->

---

## Anhang: Zweite Vorhersage (kurz bewertet)

Die zweitplatzierte Vorhersage, **Störung des Tyrosinstoffwechsels** (TxGNN-Score 0,9902), ist ebenfalls nicht belegt (Evidenzlevel L5, Entscheidung: Hold). Die drei aufgefundenen Publikationen betreffen ausschließlich Neuraminidase-Hemmer bei Influenza (Oseltamivir-Resistenz, ein Messverfahren zur Neuraminidase-Hemmung, die N294S-Mutation) und nicht den Tyrosinstoffwechsel. Die Treffer dürften auf Stichwortüberschneidungen beruhen, etwa durch Aminosäurebegriffe. Es gibt keine bekannte Verbindung zwischen Tyrosinstoffwechselstörungen und der Neuraminidase-Hemmung.

<!-- review:begin log -->

## Prüfprotokoll

Nachfolgend das Prüfprotokoll dieser Seite: Aussagen, die mit den amtlichen Zulassungsdaten (EMA-Daten zu zentral zugelassenen Arzneimitteln) abgeglichen wurden. Korrekturen beschränken sich auf grundlegende Sachangaben; Modellvorhersagen, Evidenzstufen und Schlussfolgerungen wurden nicht umgeschrieben.

| Prüfdatum | Punkt | Maßnahme | Quelle |
|------|------|------|------|
| 2026-11-06 | Entfernt: „iese Zulassung ist aufgehoben (Status: cancelled), d“ | Korrigiert | [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx) |
| 2026-11-06 | Entfernt: „da die einzige deutsche Zulassung aufgehoben ist“ | Korrigiert | [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx) |

<!-- review:end log -->

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

