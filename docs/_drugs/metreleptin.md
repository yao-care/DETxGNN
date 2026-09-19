---
layout: default
title: Metreleptin
parent: Nur Modellvorhersage (L5)
nav_order: 254
evidence_level: L5
indication_count: 10
---

# Metreleptin
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

# Metreleptin: Fehlende Daten zu Originalindikationen → Familiale verallgemeinerte Lentiginose (familiär generalisierte linsenförmige Flecken)

## Einzeilenzusammenfassung

Metreleptin (DrugBank ID: DB09046) ist ein Leptinrezeptor-Agonist, aber dieses Evidence Pack bietet keine Daten zu seinen ursprünglichen zugelassenen Indikationen und zum detaillierten Wirkmechanismus. Das TxGNN-Modell listet **familiale verallgemeinerte Lentiginose** als die am höchsten bewertete vorhergesagte neue Indikation auf (Punktzahl: 99.71%), aber **es gibt derzeit keine klinischen Studien oder Literaturbelege**, was auf eine reine Modellvorhersage auf dieser Ebene hindeutet.

---

## Überblick

| Merkmal | Inhalt |
|---------|--------|
| Originalindikation | Daten fehlend (Evidence Pack nicht bereitgestellt, Lizenzen leer) |
| Vorhergesagte neue Indikation | Familiale verallgemeinerte Lentiginose (familiär generalisierte linsenförmige Flecken) |
| TxGNN Vorhersage-Score | 99.71% (Rang 3992) |
| Evidenzstufe | L5 (reine Modellvorhersage, keine tatsächliche Forschung) |
| Zulassungsstatus in Taiwan | Nicht vermarktet |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | Hold |

---

## Warum ist diese Vorhersage plausibel?

Derzeit sind keine detaillierten Wirkmechanismus-Daten für metreleptin verfügbar (original_moa ist eine Datenlücke). Nach verfügbaren Informationen ist metreleptin ein rekombinantes humanes Leptinanalogon, das auf den Leptinrezeptor wirkt und hauptsächlich bei leptinmangelbedingter Lipodystrophie eingesetzt wird. Jedoch stellt dieses Evidence Pack keinen offiziellen Zulassungstext für diese ursprüngliche Indikation zur Verfügung, daher kann sie in diesem Bericht nicht bestätigt und aufgelistet werden.

Die am höchsten bewertete vorhergesagte Indikation, familiale verallgemeinerte Lentiginose, gehört zum LEOPARD-/Noonan-Syndrom-Spektrum (RASopathie, pigmentierungsassoziiertes genetisches Syndrom) und **zeigt keine bekannten mechanistischen Zusammenhänge** mit dem Leptinsignalweg. Das Repurposing-Rationale im Evidence Pack macht auch deutlich, dass diese Punktzahl möglicherweise artifizielle Assoziationen widerspiegelt, die durch mangelnde Verfügbarkeit von Daten bei seltenen Krankheitsknoten im Wissensgraph entstehen, und nicht eine biologisch plausible Vorhersage darstellt.

Eine weitere Überprüfung der Kandidatenindikationen in den Rängen 2–10 (gastrokutane Syndrome, Moynahan-Syndrom, rhabdoides Tumor, OPD-Weißlock-Syndrom, CAL-SCE-Syndrom, Acromelanose, LAAN-Syndrom, benigne Nebennierentumoren, periphere Nervenscheidentumoren) zeigt, dass diese alle extrem seltene genetische Syndrome oder Tumoren ohne etablierte Verbindungen zur Leptinphysiologie sind, und **keine einzige wird durch klinische Studien oder Literatur gestützt**. Die Evidenzstufen sind alle L5 und die Empfehlungen sind alle Hold. Insgesamt hat diese Charge von Vorhersagen derzeit nur explorative Natur und entbehrt der Evidenzbasis für den Eintritt in eine klinische Bewertung.

---

## Klinische Studienevidenz

Derzeit sind keine relevanten klinischen Studien registriert.

---

## Literaturbelege

Es ist derzeit keine relevante Literatur verfügbar.

---

## Taiwan-Marktzulassungsinformationen

Metreleptin ist derzeit nicht auf dem taiwanischen Markt zugelassen und es liegen keine Zulassungsdaten vor.

---

## Sicherheitserwägungen

Bitte konsultieren Sie die Fachinformation für Sicherheitsaspekte.

(Hinweis: BfArM Fachinformation Warnungen/Kontraindikationen-Daten sind eine **Blocking**-Datenlücke DG001 und wurden noch nicht beschafft; dies ist eine notwendige Voraussetzung, die vor Eintritt in die S1-Sicherheitsinitialbewertung erfüllt werden muss.)

---

## Fazit und nächste Schritte

**Entscheidung: Hold**

**Begründung:**
Die Evidenzstufen der zehn am höchsten bewerteten vorhergesagten Indikationen sind alle L5 (nur Modellpunkte, ohne klinische Studien oder Literaturbelege), und dem Arzneimittel selbst fehlen Originalindikationen, Wirkmechanismus und taiwanische Fachinformation-Sicherheitsdaten (einschließlich 1 Blocking-Datenlücke). Derzeit kann keine Sicherheitsinitialbewertung durchgeführt werden, daher wird Hold empfohlen.

**Um voranzufahren, müssen folgende Lücken geschlossen werden:**
- BfArM Fachinformation Warnungen/Kontraindikationen-Daten (DG001, Blocking, benötigt PDF-Download und -Analyse der Fachinformation)
- DrugBank MOA Detaildaten (DG002, benötigt Query der DrugBank-API)
- Offizieller Originaltext für die zugelassenen Originalindikationen von metreleptin, um eine Basis für den mechanistischen Vergleich mit vorhergesagten Indikationen zu etablieren
- Durchführung von ergänzenden Suchen in PubMed/ClinicalTrials.gov/ICTRP für die Kandidatenindikationen in den Rängen 1–3, um zu bestätigen, ob indirekte Nachweise existieren, die in der aktuellen Datenbank nicht erfasst sind

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

