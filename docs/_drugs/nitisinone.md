---
layout: default
title: Nitisinone
parent: Nur Modellvorhersage (L5)
nav_order: 317
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-24
description: "Nitisinone: vorhergesagte neue Indikation Renale tubuläre Azidose (Evidenzstufe L5). Ursprüngliche Indikation: Tyrosinämien"
monitor_inn: "NITISINONE"
predicted_indications: ["renal tubular acidosis", "galactosemia", "serpinopathy with toxic serpin polymerization", "C1 inhibitor deficiency", "glycogen storage disease", "adult polyglucosan body disease", "glycogen storage disease due to glucose-6-phosphatase deficiency", "Griscelli syndrome", "granulomatous disease, chronic, X-linked", "ermine phenotype"]
---

# Nitisinone
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **10** 
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

## Nitisinon: Renale tubuläre Azidose
{: .text-alpha }

## Zusammenfassung

Nitisinon ist ein Wirkstoff, der ursprünglich zur Behandlung von Tyrosinämien zugelassen wurde.
Das TxGNN-Modell sagt voraus, dass er bei **renaler tubulärer Azidose** wirksam sein könnte.
Dafür liegen derzeit **keine klinischen Studien** und **keine Publikationen** vor. Die Vorhersage beruht allein auf dem Modell.

---

## Kurzüberblick

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Tyrosinämien |
| Vorhergesagte neue Indikation | Renale tubuläre Azidose |
| TxGNN-Vorhersagewert | 0,9996 |
| Evidenzniveau | L5 |
| Marktstatus in Deutschland | Im Handel (gültige Zulassungen: 2 von 2) |
| Anzahl der Zulassungen | 2 (gültig: 2) |
| Empfohlene Entscheidung | Hold |

---

## Warum ist diese Vorhersage plausibel?

Laut dem Abschnitt „Mechanism of Action“ der von der US-amerikanischen FDA genehmigten Fachinformation (Prescribing Information) für Nitisinone (inoffizielle Übersetzung): „Nitisinon ist ein kompetitiver Inhibitor der 4-Hydroxyphenylpyruvat-Dioxygenase, eines Enzyms, das im Tyrosin-Abbauweg der Fumarylacetoacetat-Hydrolase (FAH) vorgeschaltet ist. Durch Hemmung des normalen Tyrosinabbaus bei Patienten mit HT-1 verhindert Nitisinon die Akkumulation der katabolen Zwischenprodukte Maleylacetoacetat und Fumarylacetoacetat.“ Englischer Originalwortlaut: "Nitisinone is a competitive inhibitor of 4-hydroxyphenyl-pyruvate dioxygenase, an enzyme upstream of fumarylacetoacetate hydrolase (FAH) in the tyrosine catabolic pathway. By inhibiting the normal catabolism of tyrosine in patients with HT-1, nitisinone prevents the accumulation of the catabolic intermediates maleylacetoacetate and fumarylacetoacetate." ([DailyMed: Nityr (nitisinone) prescribing information, Cycle Pharmaceuticals Ltd.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=00fd1905-27e4-420e-8dc5-a69e4ddc1526), Fassung vom 2026-10-21; abgerufen am 2026-11-19). Bekannt ist, dass Nitisinon das Enzym 4-Hydroxyphenylpyruvat-Dioxygenase (HPPD) im Tyrosinabbau hemmt. Dadurch wird die Anhäufung toxischer Stoffwechselprodukte (z. B. Succinylaceton) bei hereditärer Tyrosinämie Typ 1 verhindert.

Bei Tyrosinämie Typ 1 tritt häufig eine Nierentubulusfunktionsstörung (Fanconi-Typ) auf, die sich unter Nitisinon bessern kann. Dies ist jedoch eine sekundäre Nierenwirkung der Tyrosinämie und **kein belegter Zusammenhang mit der primären renalen tubulären Azidose**. Der sehr hohe Modellwert ist eine reine Vorhersage. Die mechanistische Verbindung ist daher bisher nur indirekt und hypothetisch.

---

## Evidenz aus klinischen Studien

Derzeit sind keine zugehörigen klinischen Studien registriert.

---

## Evidenz aus der Literatur

Für die renale tubuläre Azidose liegt derzeit keine zugehörige Literatur vor.

Zur Einordnung: Für andere Vorhersagen (Galaktosämie, Glykogenspeicherkrankheit) gibt es lediglich übergreifende Übersichtsarbeiten zu kindlichen Stoffwechsel-Lebererkrankungen. Diese stützen die Vorhersage nur indirekt.

---

## Marktinformationen Deutschland

<!-- licenses:begin -->

| Zulassungsnummer | Produktname | Wirkstoff(e) | Therapeutisches Gebiet (EMA, englisch) | Status |
|------|------|------|------|------|
| EMEA/H/C/000555 | Orfadin | nitisinone | Tyrosinemias | Gültig |
| EMEA/H/C/004582 | Nityr | nitisinone | Tyrosinemias | Gültig |

Quelle: EMA – Medicines output (zentral zugelassene Humanarzneimittel); Produktname, Wirkstoffe und therapeutisches Gebiet im englischen Original. Nationale Zulassungen (BfArM) und Tierarzneimittel sind in diesen Daten nicht enthalten.

<!-- licenses:end -->

---

## Sicherheitsaspekte

- **Kontraindikationen/Warnhinweise aus der Wissensgraph-Analyse (keine Packungsbeilage):** Im TxGNN-Wissensgraphen (PrimeKG) sind Kontraindikationskanten zu folgenden Erkrankungen hinterlegt: Nierenerkrankung, Pyoureter, Thrombozytopenie, Leukopenie, Hypophosphatämie und Tyrosinämie. Diese Angaben stammen nicht aus dem Beipackzettel und sind klinisch zu prüfen.
- **Arzneimittelwechselwirkungen:** Insgesamt wurden 100 Wechselwirkungen erfasst. In der vorliegenden Auswahl überwiegen Wechselwirkungen mittleren Schweregrads (moderat), darunter Abirateron, Isotretinoin, Nifedipin, Ibuprofen, Aldesleukin, Pioglitazon, Amiodaron, Amlodipin, Amobarbital, Apalutamid, Aprepitant, Atazanavir, Avatrombopag, Baricitinib, Dexamethason, Bexaroten, Bicalutamid, Ingwer und topisches Abametapir. Armodafinil wurde als geringfügig (minor) eingestuft.

Für weitere Sicherheitsinformationen (Warnhinweise, Gegenanzeigen) ist die Fachinformation heranzuziehen.

---

## Fazit und nächste Schritte

**Entscheidung: Hold**

**Begründung:**
Für die renale tubuläre Azidose gibt es ausschließlich eine Modellvorhersage ohne Studien oder Publikationen (Evidenzniveau L5). Der mechanistische Zusammenhang ist nur indirekt.

<!-- review:begin de-lic-20261106-nitisinone-1 -->

> **Prüfkorrektur (2026-11-06)**: Ursprünglich stand hier: „Der mechanistische Zusammenhang ist nur indirekt, und die deutschen Zulassungen sind aufgehoben.“ Entfernt: Die Aussage widersprach den Zulassungsdaten (EMA-Daten zu zentral zugelassenen Arzneimitteln, Stand 2026-11-06). Die aktuelle Zahl und der Status der Zulassungen stehen in der Schnellübersicht und in der Tabelle bei den Marktinformationen. Quelle: [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx).

<!-- review:end de-lic-20261106-nitisinone-1 -->

**Für ein Weiterkommen sind folgende Schritte nötig:**
- Auswertung der Fachinformation (Warnhinweise, Gegenanzeigen), da diese Sicherheitsdaten derzeit fehlen und eine Sicherheitsprüfung blockieren
- Detaillierte Wirkmechanismusdaten (z. B. aus DrugBank)
- Präklinische oder klinische Belege für einen Effekt bei primärer renaler tubulärer Azidose, abgegrenzt von der sekundären Tubulopathie bei Tyrosinämie Typ 1
- Klärung des Zulassungsstatus und der Verfügbarkeit in Deutschland

<!-- review:begin log -->

## Prüfprotokoll

Nachfolgend das Prüfprotokoll dieser Seite: Aussagen, die mit den amtlichen Zulassungsdaten (EMA-Daten zu zentral zugelassenen Arzneimitteln) abgeglichen wurden. Korrekturen beschränken sich auf grundlegende Sachangaben; Modellvorhersagen, Evidenzstufen und Schlussfolgerungen wurden nicht umgeschrieben. Die Aussage, dass keine Daten zum Wirkmechanismus vorliegen, wurde durch einen Auszug aus der angegebenen amtlichen Fachinformation (mit inoffizieller Übersetzung) ersetzt.

| Prüfdatum | Punkt | Maßnahme | Quelle |
|------|------|------|------|
| 2026-11-06 | Entfernt: „und die deutschen Zulassungen sind aufgehoben“ | Korrigiert (überarbeitet am 2026-11-24; frühere Fassung im Protokoll erhalten) | [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx) |
| 2026-11-19 | Aussage „keine Daten zum Wirkmechanismus“ durch Auszug aus der US-Fachinformation ersetzt | Aussage, dass keine Daten zum Wirkmechanismus vorliegen, durch einen belegten Auszug ersetzt | [DailyMed: Nityr (nitisinone) prescribing information, Cycle Pharmaceuticals Ltd.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=00fd1905-27e4-420e-8dc5-a69e4ddc1526) |

<!-- review:end log -->

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

