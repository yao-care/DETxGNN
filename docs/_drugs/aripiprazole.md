---
layout: default
title: Aripiprazole
parent: Hohe Evidenz (L1-L2)
nav_order: 34
evidence_level: L1
indication_count: 10
---

# Aripiprazole
{: .fs-9 }

Evidenzniveau: **L1** | Vorhergesagte Indikationen: **10** 
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

# ARIPIPRAZOL: Von antipsychotischer Anwendung zur Behandlung affektiver Störungen (Zusatztherapie)

## Zusammenfassung in einem Satz

> Aripiprazol ist ein Dopamin-D2/D3-Partialagonist-Antipsychotikum; diese Evidence-Sammlung dokumentiert seine ursprüngliche zugelassene Indikation nicht (Datenlücke), obwohl reale Fachinformationen Schizophrenie und bipolare Störung Typ I aufführen.
> Das TxGNN-Modell prognostiziert, dass es möglicherweise wirksam für **Major Affektive Störung** (Zusatzbehandlung der Major Depression) sein könnte,
> mit **60+ klinischen Studien** und **20 Publikationen**, die diese Richtung derzeit unterstützen, einschließlich einer abgeschlossenen Phase-3-Studie, die diese Anwendung bereits in der klinischen Praxis etabliert.

> ⚠️ **Datenvermerk**: `drug.original_indications` und `taiwan_regulatory.licenses` sind beide in dieser Evidence-Sammlung leer, und `market_status` zeigt „Not marketed" (Nicht vermarktet). Dies steht im Widerspruch zur gut dokumentierten globalen Zulassungsgeschichte von Aripiprazol (Abilify®) und sollte vor der Verwendung dieses Berichts für regulatorische Entscheidungen gegen Quelldaten überprüft werden.

---

## Schnellübersicht

| Element | Inhalt |
|------|------|
| Ursprüngliche Indikation | **[Datenlücke]** — nicht erfasst in der Evidence-Sammlung (`original_indications` leer) |
| Prognostizierte neue Indikation | Major Affektive Störung (Zusatztherapie zu Antidepressiva bei MDD) |
| TxGNN-Vorhersage-Score | 99.62% |
| Evidence-Level | L1 |
| Markt-Status (diesen Datensatz) | Nicht vermarktet / 0 Zulassungen erfasst |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | Mit Schutzmaßnahmen fortfahren |

---

## Warum ist diese Vorhersage angemessen?

Derzeit sind detaillierte Wirkmechanismus-Daten nicht in dieser Evidence-Sammlung verfügbar (`original_moa` = [Datenlücke]). Basierend auf bekannter Pharmakologie, die in der Begründung für die Umwidmung angegeben ist, ist Aripiprazol ein **Dopamin-D2/D3-Partialagonist**, mit zusätzlicher **5-HT1A-Partialagonist**- und **5-HT2A-Antagonist**-Aktivität. Dieses Rezeptorprofil ist die etablierte pharmakologische Grundlage für seine Verwendung als Antidepressiva-Augmentations-Agent.

Die prognostizierte neue Indikation — Major Affektive Störung / Major Depression (MDD) — ist mechanistisch kontinuierlich mit Aripiprazols bekannter antipsychotischer Aktivität: Partielle dopaminerge und serotonerge Modulation soll monoaminerge Dysregulation, die bei therapieresistenter Depression eine Rolle spielt, korrigieren. Tatsächlich hat die Augmentation von Antidepressiva mit Aripiprazol bereits regulatorische Zulassung und umfangreiche klinische Validierung außerhalb dieses Datensatzes erhalten (z. B. FDA-Zulassung als Zusatz bei MDD), was die TxGNN-Vorhersage bestätigt und wesentlich unterstützt.

Die Evidence-Sammlung selbst kennzeichnet einen wichtigen Vorbehalt: Da `original_indications` und `licenses` leer sind, kann die interne Konsistenz zwischen „ursprünglicher Indikation" und „prognostizierter Indikation" aus diesem Datensatz allein nicht überprüft werden. Die mechanistische Begründung sollte daher als durch externes Wissen bestätigt gelesen werden, nicht durch die regulatorischen Felder dieser Evidence-Sammlung.

---

## Klinische Studienevidenz

| Studiennummer | Phase | Status | Einschreibung | Wichtigste Ergebnisse |
|---------|------|------|------|---------|
| [NCT00683852](https://clinicaltrials.gov/study/NCT00683852) | Phase 3 | Abgeschlossen | 225 | Pivotale doppelblinde, Plazebo-kontrollierte Studie von reduzierter Dosis Aripiprazol als Zusatz zu Antidepressiva bei MDD mit unzureichendem Ansprechen auf vorherige Behandlung |
| [NCT00876343](https://clinicaltrials.gov/study/NCT00876343) | Phase 3 | Abgeschlossen | 586 | Plazebo-kontrollierte Parallelgruppen-Studie von Aripiprazol als Zusatz zu SSRI/SNRI bei MDD |
| [NCT00105196](https://clinicaltrials.gov/study/NCT00105196) | Phase 3 | Abgeschlossen | 349 | 14-wöchige randomisierte, doppelblinde, Plazebo-kontrollierte Zusatz-Studie bei MDD mit unvollständigem Ansprechen auf offene antidepressive Therapie |
| [NCT02046564](https://clinicaltrials.gov/study/NCT02046564) | Phase 3 | Abgeschlossen | 412 | ASC-01 (Aripiprazol/Sertralin-Kombination) vs. Sertralin-Monotherapie bei MDD mit unzureichendem Ansprechen |
| [NCT01567527](https://clinicaltrials.gov/study/NCT01567527) | Phase 3 | Abgeschlossen | 731 | 52-wöchige Plazebo-kontrollierte Studie von IM-Depotaripiprazol als Erhaltungstherapie bei bipolarer Störung Typ I |
| [NCT01284218](https://clinicaltrials.gov/study/NCT01284218) | N/A | Abgeschlossen | 23,514 | Retrospektive Real-World-Datenbankanalyse der Gesundheitsnutzung/Kosten mit Zusatz-Aripiprazol vs. anderen Augmentations-Therapien bei MDD |
| [NCT01429831](https://clinicaltrials.gov/study/NCT01429831) | Phase 4 | Abgeschlossen | 300 | Taiwanesische Real-World-Beobachtungsstudie zur Wirksamkeit/Verträglichkeit der Aripiprazol-Augmentation bei MDD mit unzureichendem Ansprechen |
| [NCT00953745](https://clinicaltrials.gov/study/NCT00953745) | N/A | Abgeschlossen | 43 | PET/fMRT-Mechanismus-Studie zur Prüfung der Dopamin-Pfad-Hypothese für Aripiprazol-Augmentation bei therapieresistenter Depression |
| [NCT00873795](https://clinicaltrials.gov/study/NCT00873795) | N/A | Abgeschlossen | 41 | Kleine vergleichende Studie von niedrig-Dosis Aripiprazol + Sertralin vs. Sertralin allein bei neu aufgetretener MDD |
| [NCT05473741](https://clinicaltrials.gov/study/NCT05473741) | N/A | Abgeschlossen | 51 | Longitudinale Kohorte zum Risiko von Durchbruch-Symptomen bei remittierten Patienten unter Langzeit-Antipsychotika-Erhaltungstherapie |

---

## Literatur-Evidenz

| PMID | Jahr | Typ | Zeitschrift | Wichtigste Ergebnisse |
|------|-----|------|------|---------|
| [38669232](https://pubmed.ncbi.nlm.nih.gov/38669232/) | 2024 | RCT-Metaanalyse | PLoS One | Größte systematische Übersicht/Metaanalyse von RCTs zu Aripiprazol- oder Bupropion-Augmentation und -Wechsel bei therapieresistenter Depression/MDD |
| [34986373](https://pubmed.ncbi.nlm.nih.gov/34986373/) | 2022 | Netzwerk-Metaanalyse | J Affect Disord | Vergleicht Wirksamkeit und Therapieabbruch bei Augmentations-Wirkstoffen (einschließlich Aripiprazol) bei therapieresistenter Depression |
| [36961650](https://pubmed.ncbi.nlm.nih.gov/36961650/) | 2023 | RCT | CNS Drugs | Pivotale Sicherheits-/Verträglichkeits-/Pharmakokinetik-Studie von 2-monatlichem Depot-Aripiprazol bei Schizophrenie und bipolarer Störung Typ I |
| [38219278](https://pubmed.ncbi.nlm.nih.gov/38219278/) | 2024 | Systematische Übersicht | Neuropsychopharmacol Rep | Netzwerk-Metaanalyse zum Vergleich von Brexpiprazol, Aripiprazol und Plazebo bei MDD bei japanischen Patienten |
| [36239033](https://pubmed.ncbi.nlm.nih.gov/36239033/) | 2023 | RCT | J Psychopharmacol | Randomisierte, doppelblinde, Plazebo-kontrollierte Studie von Aripiprazol-Zusatztherapie bei MDD mit somatischen Symptomen (mit EEG-Befunden) |
| [34167174](https://pubmed.ncbi.nlm.nih.gov/34167174/) | 2021 | Systematische Übersicht/Metaanalyse | Prim Care Companion CNS Disord | Langzeit-Wirksamkeit und Verträglichkeit von Zusatz-Aripiprazol bei MDD |
| [35510505](https://pubmed.ncbi.nlm.nih.gov/35510505/) | 2023 | Systematische Übersicht/Metaanalyse | Psychol Med | Wirksamkeit und Sicherheit/Verträglichkeit von Antipsychotika (Monotherapie und Zusatz) bei MDD im Erwachsenenalter |
| [37149344](https://pubmed.ncbi.nlm.nih.gov/37149344/) | 2023 | Übersicht | Psychiatr Clin North Am | Übersicht der Pharmakotherapie bei therapieresistenter Depression: Antidepressiva und atypische Antipsychotika, einschließlich Aripiprazol |
| [36855876](https://pubmed.ncbi.nlm.nih.gov/36855876/) | 2023 | Übersicht | Am J Psychiatry | Übersicht von antipsychotischen Pharmakotherapien bei therapieresistenter Depression im sich entwickelnden therapeutischen Kontext |
| [21254788](https://pubmed.ncbi.nlm.nih.gov/21254788/) | 2011 | Übersicht | CNS Drugs | Übersicht und Implikationen der Ergebnisse klinischer Studien für Aripiprazol als Zusatztherapie bei MDD |

---

## Marktinformationen Deutschland

In dieser Evidence-Sammlung wurden keine Vermarktungsgenehmigungen gefunden (`taiwan_regulatory.total_licenses = 0`, `licenses = []`, `market_status = "Not marketed"`). Dies steht im Widerspruch zur bekannten globalen Zulassungsgeschichte von Aripiprazol und sollte als Datenlücke behandelt werden, die einer Quellenüberprüfung bedarf, anstatt als faktische Aussage über die Abwesenheit auf dem Markt.

---

## Sicherheitserwägungen

Bitte beachten Sie die Packungsbeilage für Sicherheitsinformationen. (`key_warnings`, `contraindications` und `ddi` sind alle nicht ausgefüllt / [Datenlücke] in dieser Evidence-Sammlung.)

---

## Schlussfolgerung und nächste Schritte

**Entscheidung: Mit Schutzmaßnahmen fortfahren**

**Begründung:**
Die prognostizierte Indikation wird durch L1-Evidenz gestützt — eine abgeschlossene Phase-3-RCT (NCT00683852) sowie mehrere zusätzliche abgeschlossene Phase-3-Studien, eine große Real-World-Datenbankanalyse (n=23,514) und mehrere RCT-Metaanalysen — und ist richtungsmäßig konsistent mit Aripiprazols gut etablierter Real-World-Anwendung als Antidepressiva-Augmentation. Allerdings sind kritische Arzneimittel-Felder (MOA, Sicherheitswarnungen, Kontraindikationen, DDI, Marktgenehmigungen, ursprüngliche Indikation) alle Datenlücken in diesem Paket, was eine vollständige S1-Sicherheits-Vorbewertung blockiert.

**Zur Fortsetzung sind folgende Punkte erforderlich:**
- TFDA/Zulassungs-Fachinformation (仿單) Warnungen und Kontraindikationen (aktuell blockierende Datenlücke, DG001)
- Verifizierte Arzneimittel-MOA aus DrugBank (DG002)
- Übereinkunft der `original_indications` / `market_status` / `licenses`-Felder mit dem bekannten Real-World-Zulassungsstatus von Aripiprazol
- Arzneimittelwechselwirkungs- (DDI) -Profil, besonders für die Kombination von Antidepressiva/Antipsychotika bei MDD-Augmentation

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

