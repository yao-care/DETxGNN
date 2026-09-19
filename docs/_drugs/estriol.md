---
layout: default
title: Estriol
parent: Mittlere Evidenz (L3-L4)
nav_order: 157
evidence_level: L3
indication_count: 1
---

# Estriol
{: .fs-9 }

Evidenzniveau: **L3** | Vorhergesagte Indikationen: **1** 
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

# Estriol: Vom [nicht spezifizierten Indikation] zur Amenorrhoe

## Zusammenfassung in einem Satz

> Estriol ist ein schwaches, natürlich vorkommendes Östrogen; keine zugelassene Indikation oder Wirkmechanismus-Daten sind in diesem Evidenzpaket dokumentiert, und das Arzneimittel wird derzeit nicht in Deutschland vermarktet.
> Das TxGNN-Modell sagt potenzielle Wirksamkeit für **Amenorrhoe** voraus (spezifisch funktionelle hypothalamische Amenorrhoe, FHA), mit einer Vorhersagequote von **99.18%**.
> Die Unterstützungsevidenz ist jedoch gering und teilweise nicht übereinstimmend: Es wurden nur **3 klinische Studien** gefunden, alle mit niedriger Relevanzbeurteilung (zwei sind sehr wahrscheinlich Estetrol/Drospirenon-Kontrazeptiva-Studien, nicht Estriol), zusammen mit **13 Literaturrecords**, die meisten ohne Abstracts oder direktem Fokus auf Estriol.

---

## Kurzüberblick

| Item | Inhalt |
|------|------|
| Ursprüngliche Indikation | Nicht verfügbar — keine Indikationsdaten dokumentiert (Arzneimittel nicht vermarktet, `original_indications` leer) |
| Vorhergesagte neue Indikation | Amenorrhoe (funktionelle hypothalamische Amenorrhoe / FHA) |
| TxGNN-Vorhersagequote | 99.18% |
| Evidenzgrad | L3 |
| Marktstatus in Deutschland | ✗ Nicht vermarktet |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | Zurückstellen |

---

## Warum ist diese Vorhersage vernünftig?

Derzeit sind detaillierte Wirkmechanismus-Daten für Estriol nicht verfügbar. Basierend auf bekannter Pharmakologie ist Estriol ein natürlich vorkommendes, vergleichsweise schwaches Östrogen. Der Repurposing-Grund hier ist kein Estriol-spezifischer Mechanismus, sondern ein allgemeiner Östrogen-Klassen-Mechanismus: Exogene Östrogen-Supplementierung kann die Rückkopplung der hypothalamisch-hypophysär-ovariellen (HPO) Achse modulieren und die pulsatile LH-Sekretion wiederherstellen, was das therapeutische Prinzip zugrunde liegt der Hormonersatzbehandlung bei funktioneller hypothalamischer Amenorrhoe (FHA) oder vorzeitiger Ovarialinsuffizienz (POI).

Wichtig ist, dass dieser mechanistische Zusammenhang für die gesamte Östrogen-Klasse gilt und nicht spezifisch für Estriol ist — die Evidenz, die ihn stützt, ist überwiegend indirekt, aus der allgemeinen FHA/POI-Hormonersatz-Literatur gezogen und nicht aus Estriol-spezifischen vergleichenden Studien mit Amenorrhoe-Behebung als primärem Wirksamkeitsendpunkt. Eine Kohorten-/Pilotstudie (PMID 22137494) untersucht direkt die Auswirkung von Estriol auf die LH-Sekretion bei FHA-Patienten, was der stärkste verfügbare direkte Datenpunkt ist, aber sie steht allein ohne bestätigende RCTs.

Ein Vorbehalt zur klinischen Versuchsevidenz: Zwei der drei abgerufenen Studien (NCT04090957, NCT04209543) haben Titel und Designmerkmale (Phase 3, große Enrollmentanzahl, "Estetrol"), die stark darauf hindeuten, dass sie sich mit **Estetrol (E4)** befassen, einem anderen Östrogen, wahrscheinlich in einer kombinierten oralen Kontrazeption — nicht Estriol. Diese sollten als Übereinstimmungen mit niedriger Konfidenz behandelt werden, bis zur manuellen Verifizierung, nicht als direkte Unterstützung für diesen Kandidaten.

---

## Klinische Versuchsevidenz

| Studiennummer | Phase | Status | Enrollmentanzahl | Wesentliche Ergebnisse |
|---------|------|------|------|---------|
| [NCT04487392](https://clinicaltrials.gov/study/NCT04487392) | Phase 2 | Zurückgezogen (N=0) | 0 | Untersuchte Photobiomodulation (nicht Estriol) für postmenopausale vulvovaginale Atrophie; Studie zurückgezogen, keine Daten generiert. Niedrige Relevanz (Grad C). |
| [NCT04090957](https://clinicaltrials.gov/study/NCT04090957) | Phase 3 | Abgeschlossen | 1,015 | Bewertete Estetrol (E4), wahrscheinlich in einer kombinierten oralen Kontrazeption, für Hitzewallungen; Amenorrhoe/Blutungsprofil wahrscheinlich ein sekundärer Endpunkt. Arzneimittel-Identitätsmismatch verdächtigt — **nicht bestätigt als Estriol** (Grad C). |
| [NCT04209543](https://clinicaltrials.gov/study/NCT04209543) | Phase 3 | Abgeschlossen | 1,570 | Schwesterstudie zur obigen (Estetrol/E4Comfort Study I); gleiche Arzneimittel-Identitätsbedenken (Grad C). |

**Anmerkung:** Keiner der drei Studien bietet bestätigte, direkte Evidenz für die Wirksamkeit von Estriol bei der Behandlung von Amenorrhoe. Manuelle Verifizierung der Arzneimittel-Identität wird empfohlen, bevor diese als unterstützende Evidenz verwendet werden.

---

## Literaturische Evidenz

| PMID | Jahr | Typ | Zeitschrift | Wesentliche Ergebnisse |
|------|-----|------|------|---------|
| [22137494](https://pubmed.ncbi.nlm.nih.gov/22137494/) | 2012 | Kohortenstudie/Pilotstudie | Fertility and Sterility | Die Estriol-Verabreichung modulierte die LH-Sekretion bei Frauen mit funktioneller hypothalamischer Amenorrhoe — der direkteste relevante Estriol-spezifische Befund. |
| [37371858](https://pubmed.ncbi.nlm.nih.gov/37371858/) | 2023 | Übersichtsarbeit | Biomedicines | Überblick über niedrig dosierte Östrogene als neuroendokrine Modulatoren in FHA, mit Diskussion der Auslösung von positiven Rückkopplungsmechanismen, die Gonadotropin-Pulsatilität wiederherstellen. |
| [16526238](https://pubmed.ncbi.nlm.nih.gov/16526238/) | 2005 | Kohortenstudie | Medicinski pregled | Östrogen-Gestagen-Therapie verbesserte Lipid-/Hormonprofil bei vorzeitiger primärer Ovarialinsuffizienz (hypergonadotrope Amenorrhoe). |
| [14194444](https://pubmed.ncbi.nlm.nih.gov/14194444/) | 1964 | ausstehend | J Obstet Gynaecol Br Commonw | Historische Studie zu Gonadotropinen bei idiopathischer sekundärer Amenorrhoe; kein Abstract verfügbar. |
| [4102186](https://pubmed.ncbi.nlm.nih.gov/4102186/) | 1971 | Fallbericht | Lancet | Endokrinologische Befunde bei zwei Patienten mit vorzeitiger Ovarialinsuffizienz; kein Abstract verfügbar. |
| [2949864](https://pubmed.ncbi.nlm.nih.gov/2949864/) | 1986 | Beobachtungsstudie | Zhong Xi Yi Jie He Za Zhi | Beobachtungen zu Veränderungen der Gonadenfunktion bei Frauen mit Amenorrhoe/Oligomenorrhoe; kein Abstract verfügbar. |
| [13931724](https://pubmed.ncbi.nlm.nih.gov/13931724/) | 1963 | ausstehend | J Clin Endocrinol Metab | Wirkmechanismus von Ovulationshemmern; kein Abstract verfügbar. |
| [4254759](https://pubmed.ncbi.nlm.nih.gov/4254759/) | 1971 | Fallbericht | Br J Psychiatry | Falldiskussion zur Anorexia nervosa (eine bekannte Ursache für FHA); kein Abstract verfügbar. |
| [4307531](https://pubmed.ncbi.nlm.nih.gov/4307531/) | 1969 | ausstehend | Fertility and Sterility | Vergleichende Auswirkungen von Östrogenen auf Amylase-Spiegel im Zervikalschleim; kein Abstract verfügbar. |
| [7026111](https://pubmed.ncbi.nlm.nih.gov/7026111/) | 1981 | Übersichtsarbeit | Clin Obstet Gynecol | Allgemeine Übersicht zu Neoplasien und hormoneller Kontrazeption; nur tangential verwandt. |

**Anmerkung:** Nur 2 der 10 aufgelisteten Elemente (PMID 22137494, 37371858) befassen sich direkt und spezifisch mit Estriol/niedrig dosiertem Östrogen in FHA. Die übrigen sind ältere, niedrigrangige Records ohne Abstracts, zur Vollständigkeit aufgenommen, aber von begrenztem unabhängigem Anspruchswert.

---

## Marktinformationen für Deutschland

Estriol wird derzeit **nicht in Deutschland vermarktet** — keine BfArM-Zulassungen sind in diesem Evidenzpaket dokumentiert (`total_licenses: 0`).

---

## Sicherheitsüberlegungen

Bitte lesen Sie die Fachinformation für Sicherheitsinformationen.

*(Anmerkung: `key_warnings`, `contraindications`, und DDI-Daten sind alle in diesem Evidenzpaket als Datenlücken gekennzeichnet — siehe DG001, eine Blocking-Schweregrad-Lücke, die eine anfängliche Sicherheitsbewertung (S1) verhindert, bis TFDA/BfArM-Labelldaten erhalten werden.)*

---

## Fazit und Nächste Schritte

**Entscheidung: Zurückstellen**

**Begründung:**
Der TxGNN-Score ist hoch, und eine direkt relevante Pilotstudie (PMID 22137494) unterstützt einen plausiblen Mechanismus, aber die Gesamtqualität der Evidenz ist schwach: Es existiert keine bestätigte Estriol-spezifische RCT, zwei der drei abgerufenen klinischen Studien betreffen wahrscheinlich ein anderes Arzneimittel (Estetrol) und sollten nicht als Unterstützung gezählt werden, und eine Blocking-Schweregrad-Sicherheitsdatenlücke (DG001) verhindert jede anfängliche Sicherheitsbewertung. Dies stimmt mit der eigenen S1-„Forschungsfrage"-Stagierung des Evidenzpakets überein.

**Zum Fortfahren ist folgendes notwendig:**
- Behebung von DG001: Erhalten Sie TFDA/BfArM-Labelwarnungen und Kontraindikationen für Estriol
- Behebung von DG002: Erhalten Sie bestätigte Wirkmechanismus-Daten von DrugBank
- Manuelle Verifizierung der Arzneimittel-Identität für NCT04090957 und NCT04209543 (Estriol vs. Estetrol), bevor diese als Evidenz gezählt werden
- Identifizieren oder in Auftrag geben einer Estriol-spezifischen kontrollierten Studie bei FHA/POI-Patienten mit Amenorrhoe-Behebung als primärem Endpunkt
- Bestätigen Sie ursprüngliche zugelassene Indikation(en) für Estriol, die derzeit in diesem Evidenzpaket fehlen

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

