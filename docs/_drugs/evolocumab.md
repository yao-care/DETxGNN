---
layout: default
title: Evolocumab
parent: Nur Modellvorhersage (L5)
nav_order: 188
evidence_level: L5
indication_count: 6
last_modified_at: 2026-11-24
description: "Evolocumab: vorhergesagte neue Indikation Symptomatische Form der Hämophilie bei weiblichen Trägerinnen (Evidenzstufe L5). Ursprüngliche Indikation: Dyslipidämien"
monitor_inn: "EVOLOCUMAB"
predicted_indications: ["symptomatic form of hemophilia in female carriers", "familial apolipoprotein C-II deficiency", "thrombocytopenic purpura", "factor XI deficiency", "hemophilia A with vascular abnormality", "disease of catalytic activity"]
---

# Evolocumab
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **6** 
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

## Evolocumab: Symptomatische Form der Hämophilie bei weiblichen Trägerinnen
{: .text-alpha }

## Zusammenfassung

Evolocumab ist ein monoklonaler Antikörper, der ursprünglich zur Behandlung von Dyslipidämien und Hypercholesterinämie eingesetzt wurde.
Das TxGNN-Modell sagt voraus, dass er bei der **symptomatischen Form der Hämophilie bei weiblichen Trägerinnen** wirksam sein könnte.
Dafür liegen derzeit **keine klinischen Studien** und **keine Publikationen** vor; die Vorhersage beruht allein auf dem Modell.

## Kurzübersicht

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Dyslipidämien; Hypercholesterinämie |
| Vorhergesagte neue Indikation | Symptomatische Form der Hämophilie bei weiblichen Trägerinnen |
| TxGNN-Vorhersagewert | 0,9982 |
| Evidenzstufe | L5 |
| Marktstatus in Deutschland | Im Handel (gültige Zulassungen: 1 von 1) |
| Anzahl der Zulassungen | 1 (gültig: 1) |
| Empfohlene Entscheidung | Hold |

## Warum ist diese Vorhersage (nicht) plausibel?

Laut dem Abschnitt „Mechanism of Action“ der von der US-amerikanischen FDA genehmigten Fachinformation (Prescribing Information) für Evolocumab (inoffizielle Übersetzung): „Evolocumab ist ein humaner monoklonaler IgG2-Antikörper, der gegen die humane Proproteinkonvertase Subtilisin/Kexin Typ 9 (PCSK9) gerichtet ist. PCSK9 bindet an den Low-Density-Lipoprotein-Rezeptor (LDLR) auf der Oberfläche von Hepatozyten und fördert den Abbau des LDLR in der Leber.“ Englischer Originalwortlaut: "Evolocumab is a human monoclonal IgG2 directed against human proprotein convertase subtilisin kexin type 9 (PCSK9). PCSK9 binds to the low-density lipoprotein receptor (LDLR) on the surface of hepatocytes to promote LDLR degradation within the liver." ([DailyMed: Repatha (evolocumab) prescribing information, Amgen USA Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=cd61e902-166d-4aa6-9f3c-a18c1008d07e), Fassung vom 2026-10-12; abgerufen am 2026-11-19). Bekannt ist, dass Evolocumab ein PCSK9-hemmender Antikörper ist: Er erhöht die Verfügbarkeit von LDL-Rezeptoren und senkt dadurch das LDL-Cholesterin.

Ein plausibler mechanistischer Zusammenhang mit der neuen Indikation ist nicht erkennbar. Beschwerden bei Hämophilie-Trägerinnen entstehen durch eine verminderte Aktivität von Faktor VIII oder IX infolge X-chromosomaler Varianten und des X-Inaktivierungsmusters. Dies hat mit PCSK9 oder dem LDL-Stoffwechsel nichts zu tun. Der hohe TxGNN-Wert ist eine rein graphbasierte Vorhersage und durch keine Studie oder Publikation gestützt.

### Weitere vorhergesagte Indikationen (alle Evidenzstufe L5, Entscheidung Hold)

| Rang | Vorhergesagte Indikation | TxGNN-Wert | Einschätzung |
|------|------|------|------|
| 2 | Familiärer Apolipoprotein-C-II-Mangel | 0,9950 | Nur indirekte Plausibilität; der Defekt der Lipoproteinlipase-Aktivierung wird durch PCSK9-Hemmung nicht behoben |
| 3 | Thrombozytopenische Purpura | 0,9942 | Kein mechanistischer Zusammenhang (Autoimmunprozess bzw. ADAMTS13-Mangel) |
| 4 | Faktor-XI-Mangel | 0,9929 | Kein Einfluss auf die intrinsische Gerinnungskaskade |
| 5 | Hämophilie A mit Gefäßanomalie | 0,9922 | Kein Einfluss auf Faktor VIII |
| 6 | Erkrankung der katalytischen Aktivität | 0,9908 | Unspezifische Ontologie-Kategorie, klinisch nicht verwertbar |

## Klinische Studien

Derzeit sind keine zugehörigen klinischen Studien registriert.

## Literaturevidenz

Derzeit ist keine zugehörige Literatur verfügbar.

## Informationen zum deutschen Markt

<!-- licenses:begin -->

| Zulassungsnummer | Produktname | Wirkstoff(e) | Therapeutisches Gebiet (EMA, englisch) | Status |
|------|------|------|------|------|
| EMEA/H/C/003766 | Repatha | Evolocumab | Dyslipidemias; Hypercholesterolemia | Gültig |

Quelle: EMA – Medicines output (zentral zugelassene Humanarzneimittel); Produktname, Wirkstoffe und therapeutisches Gebiet im englischen Original. Nationale Zulassungen (BfArM) und Tierarzneimittel sind in diesen Daten nicht enthalten.

<!-- licenses:end -->

## Sicherheitsaspekte

**Arzneimittelwechselwirkungen / Pharmakologie:** Verzeichnet ist die Wechselwirkung mit dem Zielmolekül PCSK9 (Proprotein-Convertase Subtilisin/Kexin Typ 9), an das Evolocumab als Antikörper bindet. Dies entspricht dem beabsichtigten Wirkprinzip und ist keine klinische Wechselwirkung mit einem anderen Arzneimittel.

Für Warnhinweise und Gegenanzeigen bitte die Fachinformation heranziehen.

## Fazit und nächste Schritte

**Entscheidung: Hold**

**Begründung:**
Die Vorhersage beruht ausschließlich auf einem Graphmodell, ohne Studien oder Publikationen, und es besteht kein plausibler mechanistischer Zusammenhang zwischen PCSK9-Hemmung und Hämophilie bei Trägerinnen.

<!-- review:begin de-lic-20261106-evolocumab-1 -->

> **Prüfkorrektur (2026-11-06)**: Ursprünglich stand hier: „Die Vorhersage beruht ausschließlich auf einem Graphmodell, ohne Studien oder Publikationen, und es besteht kein plausibler mechanistischer Zusammenhang zwischen PCSK9-Hemmung und Hämophilie bei Trägerinnen. Zudem ist die einzige in Deutschland erfasste Zulassung erloschen.“ Entfernt: Die Aussage, die Zulassungen seien erloschen, widerrufen oder ungültig, stimmte nicht mit den Zulassungsdaten überein (EMA-Daten zu zentral zugelassenen Arzneimitteln, Stand 2026-11-06). In den Daten (EMA-Daten zu zentral zugelassenen Arzneimitteln) sind für dieses Arzneimittel 1 Zulassungen erfasst, davon 1 gültig; die aktuellen Zahlen stehen in der Schnellübersicht und bei den Marktinformationen. Quelle: [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx).

<!-- review:end de-lic-20261106-evolocumab-1 -->

**Für ein Weiterverfolgen wäre erforderlich:**
- Fachinformation (Warnhinweise und Gegenanzeigen) von BfArM bzw. EMA, da die Sicherheitsprüfung sonst nicht fortgesetzt werden kann
- Detaillierte Wirkmechanismus-Daten (MOA), z. B. aus DrugBank
- Eine biologisch begründete Hypothese sowie präklinische Daten, die einen Zusammenhang mit der Gerinnung belegen
- Klärung des aktuellen Zulassungsstatus von Evolocumab (Repatha) in Deutschland
- Gegebenenfalls Prüfung von Rang 2 (Apolipoprotein-C-II-Mangel) als biologisch am ehesten nachvollziehbarer Kandidat, ebenfalls zunächst mit präklinischer Absicherung

<!-- review:begin log -->

## Prüfprotokoll

Nachfolgend das Prüfprotokoll dieser Seite: Aussagen, die mit den amtlichen Zulassungsdaten (EMA-Daten zu zentral zugelassenen Arzneimitteln) abgeglichen wurden. Korrekturen beschränken sich auf grundlegende Sachangaben; Modellvorhersagen, Evidenzstufen und Schlussfolgerungen wurden nicht umgeschrieben. Die Aussage, dass keine Daten zum Wirkmechanismus vorliegen, wurde durch einen Auszug aus der angegebenen amtlichen Fachinformation (mit inoffizieller Übersetzung) ersetzt.

| Prüfdatum | Punkt | Maßnahme | Quelle |
|------|------|------|------|
| 2026-11-06 | Entfernt: „Zudem ist die einzige in Deutschland erfasste Zulassung erloschen“ | Korrigiert | [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx) |
| 2026-11-19 | Aussage „keine Daten zum Wirkmechanismus“ durch Auszug aus der US-Fachinformation ersetzt | Aussage, dass keine Daten zum Wirkmechanismus vorliegen, durch einen belegten Auszug ersetzt | [DailyMed: Repatha (evolocumab) prescribing information, Amgen USA Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=cd61e902-166d-4aa6-9f3c-a18c1008d07e) |

<!-- review:end log -->

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

