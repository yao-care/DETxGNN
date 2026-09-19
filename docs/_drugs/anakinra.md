---
layout: default
title: Anakinra
parent: Mittlere Evidenz (L3-L4)
nav_order: 30
evidence_level: L3
indication_count: 10
---

# Anakinra
{: .fs-9 }

Evidenzniveau: **L3** | Vorhergesagte Indikationen: **10** 
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

# Anakinra: Auf dem Weg zum familiären Mittelmeerfieber und anderen IL-1-vermittelten autoinflammatorischen Syndromen

## Eine Zusammenfassung in einem Satz

> Anakinra ist ein rekombinanter IL-1-Rezeptor-Antagonist (IL-1-Rezeptor-Antagonist), und dieses Nachweispaket stellt keine strukturierten Daten zu seinen ursprünglichen zugelassenen Indikationen bereit.
> Das TxGNN-Modell hat für dieses Medikament **10 potenzielle neue Indikationen** identifiziert, von denen die meisten zur Familie der autoinflammatorischen Erkrankungen gehören;
> Diejenige mit der höchsten Evidenzunterstützung ist das **familiäre Mittelmeerfieber (Familial Mediterranean Fever, FMF, autosomal-rezessiver Typ)**,
> das derzeit durch **20 Publikationen** unterstützt wird (keine registrierten klinischen Studien), sowie das **pyogene autoinflammatorische Syndrom (PAPA/PSTPIP1-assoziierte Krankheitsgruppe)** das gleiche Evidenzniveau für die Weiterführung der Bewertung erreicht.

---

## Schnellübersicht

> Diese Bewertung ist ein Multi-Indikations-Nachweispaket (`TW-DB00026-multi`), wobei die folgende Tabelle anhand des Kandidaten **FMF** mit dem höchsten Evidenzniveau und der stärksten Handlungsfähigkeit dargestellt wird; eine vollständige Übersicht der 10 potenziellen Indikationen finden Sie unter "Übersicht aller vorhergesagten Indikationen" weiter unten.

| Element | Inhalt |
|---------|--------|
| Ursprüngliche Indikationen | Von diesem Nachweispaket nicht bereitgestellt (`original_indications` ist leer, keine Daten zu Taiwan-/deutschen Arzneimittellizenzen) |
| Representative vorhergesagte neue Indikation | Autosomal recessive familial Mediterranean fever (familiäres Mittelmeerfieber) |
| TxGNN-Vorhersagepunktzahl | 99,89 % (Rang 1819) |
| Evidenzniveau | L3 |
| Marktbedingungen in Deutschland | ✗ Not marketed |
| Anzahl Arzneimittelzulassungen | 0 |
| Entscheidungsempfehlung | Proceed with Guardrails (Weiterführung mit Einschränkungen) |

---

## Übersicht aller vorhergesagten Indikationen

| Rang | Erkrankung | TxGNN-Punktzahl | Evidenzniveau | Entscheidungsphase | Empfehlung |
|------|-----------|-----------------|----------------|-------------------|-----------|
| 1 | Extracutaneous mastocytoma | 99,93 % | L5 | S0 | Hold |
| 2 | Hepatic infarction | 99,89 % | L5 | S0 | Hold |
| 3 | **Familial Mediterranean fever (AR)** | 99,89 % | **L3** | S3 | **Proceed with Guardrails** |
| 4 | Aggressive systemic mastocytosis | 99,88 % | L4 | S1 | Research Question |
| 5 | Hepatic veno-occlusive disease | 99,88 % | L5 | S0 | Hold |
| 6 | Peliosis hepatis | 99,85 % | L5 | S0 | Hold |
| 7 | Oligoarticular JIA (ANA-negative) | 99,85 % | L4 | S1 | Research Question |
| 8 | Oligoarticular JIA (ANA-positive) | 99,85 % | L4 | S1 | Research Question |
| 9 | **Pyogenic autoinflammatory syndrome (PAPA/PSTPIP1 group)** | 99,83 % | **L3** | S3 | **Proceed with Guardrails** |
| 10 | Unclassified autoinflammatory syndrome | 99,81 % | L4 | S1 | Research Question |

**Wichtigste Beobachtung**: Die TxGNN-Punktzahl selbst hat eine begrenzte Unterscheidungskraft (Punktzahldifferenz zwischen den ersten 10 nur 0,13 Prozentpunkte), die tatsächliche Durchführbarkeit hängt davon ab, ob die Literaturevidenz den Mechanismus unterstützt – die höchstbewerteten beiden Kandidaten (Mastocytoma, hepatic infarction) haben tatsächlich überhaupt keine Literatur- oder Versuchsevidenz, was reine Modellspekulation darstellt (L5); diejenigen, die tatsächlich die Weiterführungsschwelle erreichen, sind die beiden autoinflammatorischen Krankheitsfamilien mit den Rängen 3 und 9.

---

## Warum diese Vorhersage sinnvoll ist

Dieses Nachweispaket stellt keine strukturierten Daten zum Wirkmechanismus von Anakinra bereit (`original_moa: [Data Gap]`, entsprechend `DG002`), aber durch mechanistische Assoziationsanalyse der Kandidatenindikationen (`repurposing_rationale.mechanistic_link`) kann die pharmakologische Grundlage wiederhergestellt werden: **Anakinra ist ein rekombinanter IL-1-Rezeptor-Antagonist (IL-1Ra), der durch konkurrenziellen Antagonismus am IL-1-Rezeptor die IL-1α/IL-1β-vermittelte Entzündungssignalisierung hemmt**.

Dieser Mechanismus erklärt, warum sich das Modell stark auf die Krankheitsfamilie "autoinflammatorische Syndrome (autoinflammatory syndromes)" konzentriert:

- **FMF (Rang 3)**: Verursacht durch *MEFV*-Genmutationen, die zu Überaktivierung des pyrin-Inflammasoms und massiver IL-1β-Freisetzung führen, ist eine autosomal-rezessiv vererbte autoinflammatorische Erkrankung. Der Mechanismus des IL-1-Rezeptor-Antagonisten korrespondiert direkt mit dieser Pathologie, und klinisch ist Anakinra bereits eine etablierte Real-World-Anwendung für Colchicin-resistentes FMF (obwohl nicht in den offiziellen Indikationen dieses Nachweispakets erfasst).
- **Pyogenes autoinflammatorisches Syndrom / PAPA-Spektrum (Rang 9)**: Verursacht durch *PSTPIP1*-Genmutationen, die zu abnormaler Wechselwirkung zwischen pyrin und PSTPIP1, Überaktivierung des Inflammasoms und übermäßiger IL-1β-Sekretion führen, korrespondiert der Mechanismus ebenfalls direkt mit der Pharmakologie von Anakinra, und es gibt bereits mehrere Fallserien und systematische Übersichten, die die klinische Wirksamkeit unterstützen.

Im Gegensatz dazu haben Kandidaten mit gleich hohen Punktzahlen wie Mastocytoma (KIT-Mutation), Hepatic infarction (Gefäßverschluss), Hepatic veno-occlusive disease (Endothelschaden/Gerinnungsaktivierung), Peliosis hepatis (unklarer Mechanismus) etc., deren Kernpathologie nicht auf IL-1-vermittelter Entzündung basiert, schwache mechanistische Assoziationen, sind Fälle, in denen die TxGNN-Punktzahl und biologische Plausibilität auseinandergehen, **sollten nicht allein aufgrund der TxGNN-Punktzahl vorangetrieben werden**.

Die Mastocytosis (Rang 4) erfordert besondere Aufmerksamkeit bei der Literaturevidenz: Die beiden verfügbaren Publikationen sind beide **Schnitzler-Syndrom**-Fallberichte (IL-1-getriebenes chronisches Urtikaria-assoziiertes monoklonales Protein), nicht das typische KIT D816V-getriebene aggressive systemische Mastozytose, was eine Fehlanpassung der Krankheitsentität darstellt und nicht als direkte Unterstützung dieser Indikation betrachtet werden kann.

---

## Klinische Versuchsevidenz

Derzeit gibt es für alle 10 vorhergesagten Indikationen **keine registrierten relevanten klinischen Studien** (`clinical_trials` und `ictrp_trials` sind beide leere Arrays). Dies ist auch der Grund, warum FMF und PAPA nur L3 (Beobachtungsstudien/Fallserien-Ebene) erreichen und nicht höhere Niveaus.

---

## Literaturevidenz

### Indikation 3: Familiäres Mittelmeerfieber (FMF) – 20 Publikationen, erste 10 aufgelistet

| PMID | Jahr | Typ | Zeitschrift | Wichtigste Erkenntnisse |
|------|------|------|-----------|----------------------|
| [23322405](https://pubmed.ncbi.nlm.nih.gov/23322405/) | 2013 | Review | Clin Rev Allergy Immunol | Übersicht über IL-1β-Biologika zur Behandlung von FMF |
| [21277619](https://pubmed.ncbi.nlm.nih.gov/21277619/) | 2011 | Review/Fallserien | Semin Arthritis Rheum | IL-1-gerichtete Medikamente bei FMF: Fallserien und Literaturübersicht |
| [34550430](https://pubmed.ncbi.nlm.nih.gov/34550430/) | 2022 | Kohorte | Rheumatol Int | Canakinumab wirksam bei FMF mit Colchicin-Resistenz oder -Intoleranz versus Anakinra |
| [28585601](https://pubmed.ncbi.nlm.nih.gov/28585601/) | 2017 | Fallserien | JPMA | Anakinra/Canakinumab erfolgreich bei Behandlung von 4 Kindern mit Colchicin-resistentem FMF |
| [23928237](https://pubmed.ncbi.nlm.nih.gov/23928237/) | 2013 | Fallbericht | Joint Bone Spine | FMF mit Spondylarthritis-Myositis, erfolgreiche Anakinra-Behandlung |
| [19033248](https://pubmed.ncbi.nlm.nih.gov/19033248/) | 2009 | Fallbericht | Nephrol Dial Transplant | Anakinra erfolgreich bei FMF-Behandlung und Follow-up nach Nierentransplantation |
| [25945034](https://pubmed.ncbi.nlm.nih.gov/25945034/) | 2015 | Fallserien | Drug Des Devel Ther | Canakinumab als Rettungstherapie bei FMF mit Versagen konventioneller Behandlung |
| [21931121](https://pubmed.ncbi.nlm.nih.gov/21931121/) | 2012 | Fallserien | Nephrol Dial Transplant | IL-1-Hemmer bei FMF mit Amyloidose und Nierenversagen zeigen signifikante Wirksamkeit |
| [26861613](https://pubmed.ncbi.nlm.nih.gov/26861613/) | 2016 | Kohorte/Genetik | Gene | IL-1Ra und IL-4 Genvarianten assoziiert mit FMF-Risiko (türkische Population) |
| [30686512](https://pubmed.ncbi.nlm.nih.gov/30686512/) | 2019 | Review | Presse Med | FMF-Übersicht, einschließlich pyrin/MEFV Mechanismuserklärung |

### Indikation 9: Pyogenes autoinflammatorisches Syndrom (PAPA/PSTPIP1-assoziierte Krankheitsgruppe) – 19 Publikationen, erste 10 aufgelistet

| PMID | Jahr | Typ | Zeitschrift | Wichtigste Erkenntnisse |
|------|------|------|-----------|----------------------|
| [38259483](https://pubmed.ncbi.nlm.nih.gov/38259483/) | 2023 | Systematische Übersicht | Front Immunol | Systematische Übersicht zu Wirksamkeit und Sicherheit von Anakinra/Canakinumab bei PSTPIP1-assoziierten autoinflammatorischen Erkrankungen |
| [39006661](https://pubmed.ncbi.nlm.nih.gov/39006661/) | 2024 | Fallbericht/Review | Cureus | Fallbericht und Literaturübersicht zu Anakinra-Behandlung von PAPASH-Spektrum-Erkrankungen |
| [27448064](https://pubmed.ncbi.nlm.nih.gov/27448064/) | 2016 | Review | Hautarzt | Rolle von Anakinra bei schwerer Akne durch autoinflammatorische Erkrankungen verursacht |
| [21745697](https://pubmed.ncbi.nlm.nih.gov/21745697/) | 2012 | Fallbericht | J Am Acad Dermatol | Erstbeschreibung des PASH-Syndroms, Unterscheidung vom PAPA-Syndrom |
| [22161697](https://pubmed.ncbi.nlm.nih.gov/22161697/) | 2012 | Kohorte | Arthritis Rheum | Genotyp/Phänotyp und klinischer Verlauf von 5 PAPA-Syndrom-Patienten |
| [21532836](https://pubmed.ncbi.nlm.nih.gov/21532836/) | 2010 | Review | Curr Genomics | Übersicht über klinische, molekulare und genetische Merkmale des PAPA-Syndroms |
| [38006373](https://pubmed.ncbi.nlm.nih.gov/38006373/) | 2023 | Review | Acta Dermatovenerol Croat | Behandlungsherausforderungen bei langfristiger Remission des PAPA-Syndroms |
| [34778321](https://pubmed.ncbi.nlm.nih.gov/34778321/) | 2021 | Fallbericht/Review | Front Med | Nierenbeteiligung bei PSTPIP1-assoziierten autoinflammatorischen Erkrankungen |
| [25683018](https://pubmed.ncbi.nlm.nih.gov/25683018/) | 2015 | Fallbericht | Clin Exp Dermatol | Patient mit PSTPIP1-Neumutation mit Pyoderma gangrenosum, Akne und ulzerativer Kolitis |
| [28628471](https://pubmed.ncbi.nlm.nih.gov/28628471/) | 2017 | Fallbericht | Clin Exp Rheumatol | Hämatologische Manifestation und milder autoinflammatorischer Phänotyp bei PSTPIP1 E250K-Mutation |

Die übrigen 8 Kandidatenindikationen (Mastocytoma, Hepatic infarction, Aggressive systemic mastocytosis, Hepatic VOD, Peliosis hepatis, beide Typen von oligoartikulärer JIA, Unclassified autoinflammatory syndrome) haben 0–2 Publikationen mit Evidenz, von denen viele unvollständige Übereinstimmung der Krankheitsentität oder generelle Übersichtscharaktere aufweisen, was derzeit nicht ausreichend ist, um Weiterführung zu unterstützen. Details finden Sie in der Tabelle "Übersicht aller vorhergesagten Indikationen".

---

## Informationen zum deutschen Markt

Anakinra (DB00026) ist in dieser Datenbank als **Not marketed (`market_status: Not marketed`, `total_licenses: 0`)** gekennzeichnet, ohne verfügbare Arzneimittelzulassungsdaten, daher können keine Informationen zu Darreichungsform/zugelassene Indikationen bereitgestellt werden.

---

## Sicherheitsaspekte

Die Sicherheitsfelder dieses Nachweispakets (`key_warnings`, `contraindications`) sind alle Datenlücken, und `DG001` (BfArM-Packungsbeilage-Warnungen/Gegenanzeigen) ist als **Blocking**-Ebene gekennzeichnet, was explizit beeinflusst, ob dieser Fall in die S1-Sicherheitsinitalprüfung eingehen kann.

> Bitte konsultieren Sie die Arzneimittelbeilage für Sicherheitsinformationen; vor Schließung der Datenlücken bei Packungsbeilage-Warnungen und Gegenanzeigen kann die Sicherheit in diesem Fall nicht vollständig bewertet werden.

---

## Fazit und nächste Schritte

**Entscheidung: Proceed with Guardrails (begrenzt auf FMF und PAPA/PSTPIP1-assoziierte Indikationen) / Hold (übrige 8 Kandidaten)**

**Begründung:**
- Die beiden Kandidaten FMF und Pyogenes autoinflammatorisches Syndrom (PAPA-Spektrum) haben eine eindeutige mechanistische Assoziation (IL-1-getriebene Inflammasom-Überaktivierung), werden durch mehrere Real-World-Literaturpublikationen unterstützt und sind bereits klinisch etablierte Off-Label-Anwendungen, erreichen L3/S3 und können unter bestimmten Bedingungen vorangetrieben werden.
- Die übrigen 8 Kandidaten (einschließlich der höchstbewerteten TxGNN-Kandidaten Mastocytoma und Hepatic infarction) haben schwache mechanistische Assoziationen oder überhaupt keine Literatur-/Versuchsevidenz, sind L4-L5 und sollten auf Hold bleiben, nicht allein aufgrund der Modellpunktzahl vorangetrieben werden.

**Erforderlich vor Weiterführung:**
- **`DG001` (Blocking)**: TFDA/Originalbeilage-Volltext zu Warnungen und Gegenanzeigen (PDF herunterladen und analysieren), dies ist eine Voraussetzung für den Eintritt in die S1-Sicherheitsinitalprüfung.
- **`DG002` (High)**: Strukturierte MOA-Daten durch DrugBank-API-Abfrage, um die Strenge der mechanistischen Assoziationsanalyse zu verstärken.
- Daten zu ursprünglichen zugelassenen Indikationen (dieses Paket `original_indications` ist leer), um Ähnlichkeitsvergleiche zwischen ursprünglichen und neuen Indikationen zu ermöglichen.
- Für den Kandidaten Aggressive systemic mastocytosis ist eine Klärung der Fehlanpassung zwischen Schnitzler-Syndrom in der Literatur und der Zielkrankheitsentität (KIT D816V-getrieben) erforderlich, um Missverstndnis durch Einzelfallevidenz zu vermeiden.
- Falls die Weiterführung zur formalen klinischen Bewertung der Kandidaten FMF/PAPA angestrebt wird, wird empfohlen, zuerst zu überprüfen, ob relevante prospektive Studien oder registrierte Versuche existieren (derzeit alle 0).

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

