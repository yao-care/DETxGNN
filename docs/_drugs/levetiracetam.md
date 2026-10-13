---
layout: default
title: Levetiracetam
parent: Nur Modellvorhersage (L5)
nav_order: 268
evidence_level: L5
indication_count: 10
---

# Levetiracetam
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

# Levetiracetam: Von Epilepsie zu Status epilepticus

## Zusammenfassung

Levetiracetam ist ein Antiepileptikum, das ursprünglich zur Behandlung der Epilepsie zugelassen wurde. Das TxGNN-Modell sagt als bestbelegte neue Richtung **Status epilepticus** voraus (Platz 9 der Vorhersageliste), gestützt durch **16 klinische Studien** und **20 Publikationen**, darunter zwei Phase-3-Studien. Die an Rang 1 gelisteten Indikationen (z. B. visuelle Epilepsie) haben dagegen keinerlei krankheitsspezifische Evidenz. Die Vorhersage zum Status epilepticus ist zudem eher eine Erweiterung der bestehenden Epilepsie-Anwendung als eine echte Neuausrichtung.

---

## Kurzüberblick

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Epilepsie |
| Vorhergesagte neue Indikation | Status epilepticus (bestbelegte Vorhersage; die Rangfolge nach TxGNN-Score führt „visuelle Epilepsie“ an) |
| TxGNN-Vorhersagewert | 99,91 % (für Status epilepticus); 99,98 % für den Rang-1-Kandidaten „visuelle Epilepsie“ |
| Evidenzstufe | L1 (für Status epilepticus) |
| Marktstatus in Deutschland | Nur erloschene Zulassungen |
| Anzahl Zulassungen | 9 (alle erloschen) |
| Empfohlene Entscheidung | Proceed with Guardrails (für Status epilepticus) |

---

## Warum ist diese Vorhersage plausibel?

Für die Wirkweise liegen in den zusammengestellten Daten keine detaillierten Angaben vor. Aus der Literatur geht jedoch hervor, dass Levetiracetam an das synaptische Vesikelprotein SV2A bindet und die Freisetzung von Neurotransmittern moduliert. Dadurch wird die neuronale Übererregbarkeit gedämpft.

Epilepsie und Status epilepticus gehören zum selben Krankheitsspektrum: Status epilepticus ist ein prolongierter bzw. sich wiederholender Anfall, bei dem die Mechanismen der Anfallsbeendigung versagen. Ein Wirkstoff, der Anfälle unterdrückt, kann daher plausibel auch in dieser Situation wirken. Die Phase-3-Studie ESETT zeigte vergleichbare Wirksamkeit von Levetiracetam, Fosphenytoin und Valproat bei benzodiazepinrefraktärem Status epilepticus.

Einschränkend ist festzuhalten: Weil das Arzneimittel ohnehin bei Anfällen eingesetzt wird, handelt es sich hier eher um eine zulassungsnahe Anwendung als um echtes Repurposing. Der Zulassungsstatus für diese konkrete Indikation sollte geprüft werden.

Die übrigen Kandidaten sind schwächer belegt:
- **Audiogene Anfälle** und **Startle-Epilepsie** (L3): Tiermodelle, eine veterinärmedizinische RCT bei Katzen bzw. kleine, unkontrollierte humane Studien.
- **Lesen-, Essen-, Miktions-, Denk- und Orgasmus-induzierte Anfälle**, **visuelle Epilepsie** (L4/L5): nur indirekte oder keine Evidenz; die hohen Scores spiegeln vermutlich die Nähe zur Epilepsie im Wissensgraphen wider.
- **Beta-Ketothiolase-Mangel** (L5): keine mechanistische Begründung, vermutlich ein Artefakt des Wissensgraphen.

---

## Klinische Studien (Status epilepticus)

| Studiennummer | Phase | Status | Teilnehmende | Kernaussagen |
|---------|------|------|------|---------|
| [NCT01960075](https://clinicaltrials.gov/study/NCT01960075) | Phase 3 | Abgeschlossen | 478 | ESETT: Levetiracetam vs. Fosphenytoin vs. Valproat bei benzodiazepinrefraktärem Status epilepticus |
| [NCT01150331](https://clinicaltrials.gov/study/NCT01150331) | Phase 3 | Abgeschlossen | 203 | i.v. Levetiracetam plus Clonazepam vs. Clonazepam allein in der Präklinik |
| [NCT02920060](https://clinicaltrials.gov/study/NCT02920060) | Phase 2 | Abgeschlossen | 80 | Levetiracetam vs. Valproat bei Kindern mit refraktärem konvulsivem Status epilepticus |
| [NCT04926844](https://clinicaltrials.gov/study/NCT04926844) | Phase 2 | Abgeschlossen | 144 | Levetiracetam plus Midazolam bei generalisiertem konvulsivem Status epilepticus bei Kindern |
| [NCT00362141](https://clinicaltrials.gov/study/NCT00362141) | Phase 2 | Unbekannt | 12 | Sicherheit und Verträglichkeit von Levetiracetam als Zusatztherapie |
| [NCT07046611](https://clinicaltrials.gov/study/NCT07046611) | Phase 2/3 | Rekrutierend | 124 | Ketamin plus Levetiracetam vs. Levetiracetam allein bei Kindern |
| [NCT06907173](https://clinicaltrials.gov/study/NCT06907173) | Phase 3 | Rekrutierend | 770 | KESETT: Ketamin-Zusatz zu Levetiracetam bei etabliertem Status epilepticus |
| [NCT06403150](https://clinicaltrials.gov/study/NCT06403150) | Phase 4 | Abgeschlossen | 62 | Levetiracetam vs. Fosphenytoin bei konvulsivem Status epilepticus |
| [NCT04176887](https://clinicaltrials.gov/study/NCT04176887) | Phase 4 | Unbekannt | 60 | Levetiracetam vs. Phenytoin bei Status epilepticus im Kindesalter |
| [NCT07052136](https://clinicaltrials.gov/study/NCT07052136) | Nicht zutreffend | Abgeschlossen | 138 | Levetiracetam vs. Valproinsäure bei Kindern mit Status epilepticus |

Weitere registrierte Studien (u. a. NCT07098728, NCT06067412, NCT07163572, NCT02056236, NCT05756621) betreffen Vergleiche mit Phenobarbital, Phenytoin oder Brivaracetam bzw. postanoxische Zustände; zwei Phase-2/3-Studien (NCT02726867, NCT00603135) wurden zurückgezogen.

---

## Literaturevidenz (Status epilepticus)

| PMID | Jahr | Typ | Zeitschrift | Kernaussagen |
|------|-----|------|------|---------|
| [31774955](https://pubmed.ncbi.nlm.nih.gov/31774955/) | 2019 | RCT | N Engl J Med | Drei Antikonvulsiva bei benzodiazepinrefraktärem Status epilepticus im Vergleich |
| [32203691](https://pubmed.ncbi.nlm.nih.gov/32203691/) | 2020 | Sekundäranalyse einer RCT | Lancet | ESETT nach Altersgruppen: Levetiracetam, Fosphenytoin, Valproat |
| [33190679](https://pubmed.ncbi.nlm.nih.gov/33190679/) | 2020 | RCT | Health Technol Assess | EcLiPSE: Levetiracetam als Alternative zu Phenytoin bei Kindern |
| [38580318](https://pubmed.ncbi.nlm.nih.gov/38580318/) | 2024 | Review | Semin Neurol | Update zur pharmakologischen Therapie; Phenytoin, Valproat und Levetiracetam mit ähnlichem Sicherheits- und Wirksamkeitsprofil |
| [35333156](https://pubmed.ncbi.nlm.nih.gov/35333156/) | 2022 | Evidenzsynthese | Health Technol Assess | Präklinische und notfallmedizinische Behandlung des konvulsiven Status epilepticus bei Erwachsenen |
| [38830068](https://pubmed.ncbi.nlm.nih.gov/38830068/) | 2024 | Review | Continuum | Notfallmanagement des Status epilepticus |
| [38117319](https://pubmed.ncbi.nlm.nih.gov/38117319/) | 2024 | Review | Intensive Care Med | Status epilepticus auf der Intensivstation |
| [34659919](https://pubmed.ncbi.nlm.nih.gov/34659919/) | 2021 | Übersichtsarbeit | Cureus | Phenytoin vs. Levetiracetam |
| [39626562](https://pubmed.ncbi.nlm.nih.gov/39626562/) | 2025 | Leitlinie | Brain Dev | Japanische Leitlinie zum pädiatrischen Status epilepticus 2023 |
| [37391637](https://pubmed.ncbi.nlm.nih.gov/37391637/) | 2023 | Review | Pediatr Rev | Benzodiazepine, Levetiracetam, Fosphenytoin und Valproat können Status epilepticus wirksam beenden |

---

## Markt in Deutschland

Alle neun in den Daten geführten Zulassungen sind erloschen (Einträge mit EMEA-Nummern, also zentrale europäische Zulassungen).

| Zulassungsnummer | Produktname | Darreichungsform | Zugelassene Indikation |
|---------|------|------|-----------|
| EMEA/H/C/000277 | Keppra | – | Epilepsie |
| EMEA/H/C/002244 | Levetiracetam ratiopharm | – | Epilepsie |
| EMEA/H/C/002290 | Levetiracetam Accord | – | Epilepsie |
| EMEA/H/C/002783 | Levetiracetam Hospira | – | Epilepsie |
| EMEA/H/C/002355 | Levetiracetam Actavis | – | Epilepsie |

Vier weitere erloschene Zulassungen (Teva, Sun, Matever, Actavis Group) sind in den Daten ebenfalls geführt.

---

## Sicherheitsaspekte

Für Warnhinweise und Gegenanzeigen aus der Fachinformation liegen keine Daten vor. Bitte die Fachinformation zu Rate ziehen.

Ergänzend ergaben sich folgende Hinweise:

- **Kontraindikationen aus dem Wissensgraphen** (keine Packungsbeilagen-Angaben, nur Verknüpfungen im Wissensgraphen): Angststörung, neurotische Störung, dysthyme Störung, psychotische Störung, schizophreniforme und schizoaffektive Störung, psychische Störungen allgemein, Depersonalisationsstörung, Nierenerkrankung, Lebererkrankung, Gallenblasenerkrankung, Pyoureter sowie hämatologische Auffälligkeiten (Neutropenie, Agranulozytose, Leukopenie, Panzytopenie).
- **Arzneimittelwechselwirkungen**: 100 Wechselwirkungen erfasst. Als moderat eingestuft sind Morphin (auch liposomal), Dronabinol, Metoclopramid, Nabilon, Opium und Sibutramin. Weitere Wechselwirkungen (u. a. Pantoprazol, Omeprazol, Metformin, Vancomycin) sind ohne bekannte Einstufung gelistet.
- **Literaturhinweise zu Nebenwirkungen**: Hyponatriämie, Gingivahyperplasie, Anfallsverschlechterung unter Levetiracetam sowie Reizbarkeit.

---

## Fazit und nächste Schritte

**Entscheidung: Proceed with Guardrails** (für Status epilepticus)

**Begründung:**
- Zwei abgeschlossene Phase-3-Studien (ESETT, n = 478; n = 203) sowie mehrere Phase-2-Studien stützen den Einsatz bei Status epilepticus. Die Indikation liegt jedoch nah an der bestehenden Epilepsie-Anwendung.
- Die übrigen Kandidaten (visuelle, audiogene, Startle-, Lesen-, Essen-, Miktions-, Denk- und Orgasmus-induzierte Anfälle sowie Beta-Ketothiolase-Mangel) bleiben bei „Hold“ bzw. „Research Question“, da humane kontrollierte Daten fehlen.

**Für das weitere Vorgehen erforderlich:**
- Fachinformation (BfArM) mit Warnhinweisen und Gegenanzeigen beschaffen und auswerten; dieser Punkt blockiert derzeit das Sicherheitsscreening.
- Zulassungsstatus für Status epilepticus prüfen; in den Daten sind nur erloschene Zulassungen geführt, der aktuelle Marktstatus muss geklärt werden.
- Detaillierte Wirkmechanismusdaten (z. B. aus DrugBank) ergänzen.
- Leitplanken definieren: altersgerechte Dosierung, Nierenanpassung, Überwachung psychiatrischer und verhaltensbezogener Nebenwirkungen sowie Einsatz erst nach Benzodiazepinen als Erstlinie.
- Für Startle-Epilepsie und audiogene Anfälle ggf. prospektive Studien am Menschen planen.
## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

