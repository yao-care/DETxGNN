---
layout: default
title: Denosumab
parent: Nur Modellvorhersage (L5)
nav_order: 120
evidence_level: L5
indication_count: 2
---

# Denosumab
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **2** 
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

# Denosumab: Ursprüngliche Indikation unklar → Vorhergesagte Anwendung bei schwerer nichtproliferativer diabetischer Retinopathie

## Zusammenfassung in einem Satz

> Die ursprüngliche zugelassene Indikation für Denosumab kann aus dem aktuellen Nachweispaket nicht bestätigt werden (keine Lizenz- oder Indikationstexte verfügbar), obwohl es allgemein als ein gegen RANKL gerichteter monoklonaler Antikörper bekannt ist, der bei knochenbezogenen Erkrankungen verwendet wird.
> Das TxGNN-Modell sagt eine mögliche Rolle bei **schwerer nichtproliferativer diabetischer Retinopathie** voraus,
> aber diese Vorhersage wird derzeit durch **0 klinische Studien** und **0 Publikationen** gestützt – es ist eine reine algorithmische Extrapolation ohne direkte Evidenz.

---

## Schnellübersicht

| Element | Inhalt |
|---------|--------|
| Ursprüngliche Indikation | Nicht verfügbar — sowohl `original_indications` als auch `taiwan_regulatory.licenses` sind in diesem Nachweispaket leer |
| Vorhergesagte neue Indikation | Schwere nichtproliferative diabetische Retinopathie |
| TxGNN-Vorhersage-Score | 99.63% (Rang 4724) |
| Evidenzebene | **L5** (nur Modellvorhersage) |
| Marktstatus | Nicht vermarktet (Nicht vermarktet) |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | **Aufschub** |

---

## Warum ist diese Vorhersage plausibel?

Derzeit sind detaillierte Wirkmechanismus-Daten nicht verfügbar (DG002, DrugBank-Abfrage ausstehend). Die mit diesem Paket bereitgestellte Begründung der vorhergesagten Indikation beschreibt die Arbeitshypothese direkt: Die Vorhersage erweitert eine **RANKL/OPG-Achsen-Hypothese** — die bereits als relevant für diabetische Retinopathie im Allgemeinen gekennzeichnet ist — auf einen spezifischen Krankheitssubtyp (schwere nichtproliferative Erkrankung). Die Begründung vermerkt jedoch ausdrücklich, dass dies „eine reine Knowledge-Graph-Knoten-Ähnlichkeits-Extrapolation durch den TxGNN-Algorithmus, der jeglicher subtyp-spezifischen biologischen Argumentation entbehrt," ist und durch keine direkte oder indirekte klinische Daten gestützt wird.

Es gibt einige indirekte Hinweise für die **breitere** Kategorie der diabetischen Retinopathie (TxGNN Rang 2, Score 99.23%, Evidenzebene L4), die die vermutete biologische Grundlage sind, aus der diese Vorhersage für den schweren Subtyp extrapoliert wird:

- **OPG–RANKL-Korrelation**: Osteoprotegerin (OPG), der Köder-Rezeptor für RANKL, wurde bei Patienten mit diabetischer Retinopathie als erhöht berichtet und korreliert mit der Krankheitsschwere — was darauf hindeutet, dass die RANKL/OPG-Achse an retinaler Gefäßpathologie (Entzündung, vaskuläres Remodeling) beteiligt sein kann. Dies ist eine korrelativen Biomarker-Assoziation, kein etablierter kausaler Behandlungsmechanismus, und die Richtung der Wirkung (Denosumab *hemmt* RANKL, während die Assoziation mit *erhöhtem* OPG besteht) ist nicht vollständig konsistent mit einer einfachen kausalen Erklärung.
- Eine Real-World-Kohortenstudie aus 2024 (PMID [38899553](https://pubmed.ncbi.nlm.nih.gov/38899553/), Henney et al., *Diabetes Obes Metab*) ergab, dass die Anwendung von Denosumab mit einer reduzierten Inzidenz von Typ-2-Diabetes und niedrigeren Raten von mikrovaskulären Komplikationen (einschließlich Retinopathie) im Vergleich zu Bisphosphonaten assoziiert war — ein Beobachtungssignal, kein Interventions-Wirksamkeitsergebnis für Retinopathie selbst.

Keine Evidenz in diesem Paket behandelt spezifisch den **schweren nichtproliferativen** Subtyp, den Rang 1 vorhersagt; alle verfügbaren Signale beziehen sich auf diabetische Retinopathie als breite Kategorie.

---

## Klinische Studien-Evidenz

Derzeit keine verwandten klinischen Studien für schwere nichtproliferative diabetische Retinopathie registriert.

*Kontext: Es existiert eine Phase-3-Studie im breiteren Raum der diabetischen Retinopathie/Denosumab — [NCT00925600](https://clinicaltrials.gov/study/NCT00925600) (abgeschlossen, n=769) — aber sie bewertete die Linsentrübungs- (Kataraktbildungs-) Sicherheit bei Prostatakrebspatienten unter Denosumab zur Knochenverlust-Prävention, nicht die Wirksamkeit bei Retinopathie. Sie wurde durch Evidenzbewertung als **C/niedrige Relevanz** klassifiziert und bietet nur ophthalmologischen Sicherheitskontext, keine Wirksamkeitsevidenz.*

---

## Literatur-Evidenz

Derzeit ist keine verwandte Literatur speziell für schwere nichtproliferative diabetische Retinopathie verfügbar.

*Kontext: Zwei Publikationen unterstützen die breitere Kategorie der diabetischen Retinopathie (zitiert in der obigen Mechanismus-Diskussion) — eine 2024 Real-World-Kohorten-/Metaanalyse (PMID 38899553) und eine 2023 Fraktur-Risiko-Kohorte (PMID 36960265) mit niedrigerer Relevanz. Keine behandelt den schweren Subtyp oder bietet Interventions-Wirksamkeitsdaten.*

---

## Marktinformationen

Derzeit keine Zulassungen verfügbar (Produktstatus: Nicht vermarktet, 0 Zulassungen).

---

## Sicherheitsaspekte

Bitte beachten Sie die Packungsbeilage für Sicherheitsinformationen.

*Hinweis: Lokale (TFDA-äquivalente) Etikettenwarnungen und Kontraindikationen konnten für dieses Nachweispaket nicht abgerufen werden (DG001, **Blockierende** Schweregrad) — dies allein verhindert eine S1-Sicherheitsvorabprüfung für diesen Kandidaten.*

---

## Fazit und nächste Schritte

**Entscheidung: Aufschub**

**Begründung:**
Die vorhergesagte Indikation (schwere nichtproliferative diabetische Retinopathie) hat keine direkte klinische Studien- oder Literatursupport und ein L5-Evidenzniveau — dies ist eine nicht validierte Knowledge-Graph-Extrapolation aus einer breiteren, selbst nur schwach gestützten (L4, korrelativ) Krankheitsassoziation. In Kombination mit einer Datenlücke zu lokalen Etikettenwarnungen/Kontraindikationen kann der Kandidat noch nicht in die Sicherheitsvorabprüfung eintreten.

**Um fortzufahren, wird das Folgende benötigt:**
- TFDA/lokale Packungsbeilage-Warnungen und Kontraindikationen (DG001, blockierend — erforderlich vor jeder S1-Sicherheitsbewertung)
- Denosumab-Wirkmechanismus-Daten von DrugBank (DG002)
- Ursprüngliche Indikations- und Lizenzierungsdaten (derzeit vollständig nicht vorhanden in diesem Paket)
- Präklinische oder translatorische Evidenz, die die RANKL/OPG-Achse kausal (nicht nur korrelativ) mit diabetischer Retinopathie verknüpft, und spezifisch mit dem schweren nichtproliferativen Subtyp
- Falls stattdessen das breitere Signal der diabetischen Retinopathie (Rang 2) verfolgt wird, sind prospektive mechanistische oder Interventionsstudien erforderlich, um über die aktuelle kohortale und korrelativen Evidenzgrundlagen hinauszugehen

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

