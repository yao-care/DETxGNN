---
layout: default
title: Eribulin
parent: Nur Modellvorhersage (L5)
nav_order: 155
evidence_level: L5
indication_count: 10
---

# Eribulin
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

# Eribulin: Von Weichgewebssarkom/Liposarkom zu Fibroblastischem Neoplasma (Solitary Fibrous Tumor / Fibrosarkom-Spektrum)

## Zusammenfassung in einem Satz

Eribulin ist ein Inhibitor der Mikrotubuli-Dynamik, der bereits gegen Weichgewebssarkome, einschließlich Liposarkom, eingesetzt wird. Von 10 durch TxGNN vorhergesagten Indikationen zeigt das stärkste, evidenzgestützte Signal auf **Fibroblastisches Neoplasma** (umfassend Solitary Fibrous Tumor und Fibrosarkom/Myxofibrosarkom), unterstützt durch **1 abgeschlossene Phase-II-Studie** und **8 Veröffentlichungen** — der einzige Kandidat in dieser Gruppe mit Bestätigung aus der Praxis; die anderen 9 Vorhersagen bleiben nur modellbasiert (L5), mit mehreren, die in der Quellenrationale ausdrücklich als wahrscheinliche Graph-Verknüpfungsartefakte gekennzeichnet sind.

---

## Schnellübersicht

| Element | Inhalt |
|---------|--------|
| Original-Indikation | Nicht verfügbar aus deutschen Zulassungsdaten (Arzneimittel nicht vermarktet); das Evidenzpaket bestätigt, dass Eribulin bereits eine anerkannte Indikation in Weichgewebssarkom / Liposarkom durch Hemmung der Mikrotubuli-Dynamik hat |
| Vorhergesagte neue Indikation | Fibroblastisches Neoplasma (Solitary Fibrous Tumor / Fibrosarkom-Spektrum) |
| TxGNN-Vorhersage-Score | 99.36% |
| Evidenzstufe | L3 (1 abgeschlossene, nicht randomisierte Phase-II-Studie + mehrere präklinische Studien) |
| Status auf dem deutschen Markt | ✗ Nicht vermarktet |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | Fortfahren mit Schutzmaßnahmen |

---

## Warum ist diese Vorhersage sinnvoll?

Detaillierte strukturierte MOA-Daten (DrugBank-Feld) sind derzeit eine Datenlücke. Allerdings beschreibt die in mehreren prognostizierten Indikationen in diesem Evidenzpaket eingebettete Umpositionierungsrationale Eribulin konsistent als **Inhibitor der Mikrotubuli-Dynamik / Anti-Mitose-Mittel**, mit bereits in Weichgewebssarkom nachgewiesener Wirksamkeit, einschließlich einer anerkannten Liposarkom-Indikation (ausdrücklich für die myxoides-Liposarkom-Vorhersage, Rang 5, erwähnt).

Fibroblastische Neoplasien — Solitary Fibrous Tumor (SFT), Fibrosarkom und Myxofibrosarkom — gehören zur gleichen breiten Weichgewebssarkom-Familie wie Liposarkom. Sie weisen hochproliferative Biologie mesenchymalen Ursprungs auf, die mechanistisch von der Mikrotubuli-Funktion abhängt, was sie zu einer biologisch plausiblen Erweiterung von Eribulins bekannter Anti-Tumor-Aktivität macht, anstatt eines unverwandten Indikationsbereichs.

Diese mechanistische Plausibilität wird durch echte Daten gestärkt: Eine abgeschlossene Phase-II-Studie (ERASING, NCT03840772) testete speziell Eribulin bei fortgeschrittenem SFT, und mehrere unabhängige präklinische Studien (2021–2025) zeigen Eribulin-Aktivität — einschließlich Synergie mit rekombinanter Methioninase — in Fibrosarkom- und Myxofibrosarkom-Zelllinien und patientengestützten Xenotransplantaten. Diese Kombination aus einer abgeschlossenen klinischen Studie plus konsistenter präklinischer Literatur ist einzigartig unter den 10 Kandidaten in diesem Paket; neun andere Vorhersagen (z. B. Familiäres Mittelmeerfieber, Mesotheliom-Subtypen, Adenomatoid-Tumor) haben keine unterstützenden Studien oder Literatur und sind ausdrücklich in der Quellenrationale als niedrige mechanistische Plausibilität oder wahrscheinliches TxGNN-Graph-Artefakt annotiert.

---

## Evidenz aus klinischen Studien

| Studiennummer | Phase | Status | Teilnehmerzahl | Wichtigste Erkenntnisse |
|---------|------|--------|------|---------|
| [NCT03840772](https://clinicaltrials.gov/study/NCT03840772) | Phase 2 | Abgeschlossen | 16 | Italian Sarcoma Group-Studie (ERASING) zur Bewertung von Eribulin bei fortgeschrittenem Solitary Fibrous Tumor |

---

## Evidenz aus der Literatur

| PMID | Jahr | Typ | Zeitschrift | Wichtigste Erkenntnisse |
|------|-----|------|------|---------|
| [38136399](https://pubmed.ncbi.nlm.nih.gov/38136399/) | 2023 | Übersichtsartikel | Cancers | Diagnostik und Behandlungslandschaft des extrameningealen SFT; diskutiert Chemotherapie einschließlich Mikrotubuli-targeting Mittel |
| [28284173](https://pubmed.ncbi.nlm.nih.gov/28284173/) | 2017 | Präklinisch (PDX) | Eur J Cancer | Patientengestützte SFT-Xenotransplantate sagen Empfindlichkeit gegenüber Doxorubicin/Dacarbazin voraus und heben Eribulin/Trabectedin als möglicherweise wirksam hervor |
| [38423656](https://pubmed.ncbi.nlm.nih.gov/38423656/) | 2024 | Präklinisch (in vitro) | Anticancer Research | Rekombinante Methioninase wirkt synergistisch mit Eribulin gegen Fibrosarkom-Zellen, verschont aber normale Fibroblasten |
| [39197933](https://pubmed.ncbi.nlm.nih.gov/39197933/) | 2024 | Präklinisch (in vitro) | Anticancer Research | Rekombinante Methioninase erhöht die Eribulin-Wirksamkeit um das 16-fache in eribulin-resistenten HT1080-Fibrosarkom-Zellen |
| [40295012](https://pubmed.ncbi.nlm.nih.gov/40295012/) | 2025 | Präklinisch (in vivo) | In Vivo | Super-eribulin-resistente Fibrosarkom-Zellen werden maligner, werden aber synergistisch durch Eribulin + Methionin-Restriktion bei Mäusen kontrolliert |
| [39625530](https://pubmed.ncbi.nlm.nih.gov/39625530/) | 2024 | Präklinisch (Zellkultur) | Human Cell | Etablierung einer neuen Myxofibrosarkom-Zelllinie (SMU-MFS) für zukünftige Arzneimitteltests, einschließlich Mikrotubuli-targeting Mittel |
| [34383271](https://pubmed.ncbi.nlm.nih.gov/34383271/) | 2021 | Präklinisch (Zellkultur) | Human Cell | Etablierung einer patientengestützten Myxofibrosarkom-Zelllinie (NCC-MFS4-C1) als Modell für die Behandlungsentwicklung |
| [35906852](https://pubmed.ncbi.nlm.nih.gov/35906852/) | 2023 | Fallbericht | Genes Chromosomes Cancer | Ansprechen auf Entrectinib (nicht Eribulin) bei NTRK-Fusion malignem peripherem Nervenscheidentumor; einbezogen über Erkrankungsklassen-Verknüpfung, nicht Eribulin-spezifisch — schwache Relevanz |

---

## Marktinformation Deutschland

Eribulin hält derzeit **keine Zulassung in Deutschland** (0 Lizenzen in der Datei); keine Produkt-/Darreichungsformdaten sind in diesem Evidenzpaket verfügbar.

---

## Zytotoxizität

| Element | Inhalt |
|--------|--------|
| Zytotoxizitätsklassifizierung | Konventionelle Zytotoxika (Inhibitor der Mikrotubuli-Dynamik / Anti-Mitose-Mittel) |
| Myelosuppression-Risiko | Bitte beachten Sie die Warnhinweise und Vorsichtsmaßnahmen in der Gebrauchsinformation (keine Toxizitätsdaten in diesem Datensatz) |
| Emetogenitätsklassifizierung | Bitte beachten Sie die Warnhinweise und Vorsichtsmaßnahmen in der Gebrauchsinformation |
| Überwachungselemente | Bitte beachten Sie die Warnhinweise und Vorsichtsmaßnahmen in der Gebrauchsinformation |
| Schutzmaßnahmen beim Umgang | Antineoplastisches Mittel — Handhabungsvorsichtsmaßnahmen für zytotoxische Arzneimittel nach institutionellem Protokoll erforderlich |

---

## Sicherheitsaspekte

Bitte beachten Sie die Gebrauchsinformation für Sicherheitsinformationen. Wichtige Warnhinweise, Kontraindikationen und Arzneimittelwechselwirkungsdaten sind in diesem Evidenzpaket nicht verfügbar (gekennzeichnet als blockierende Datenlücke, ausstehend: Beschaffung der TFDA-Kennzeichnung).

---

## Fazit und nächste Schritte

**Entscheidung: Fortfahren mit Schutzmaßnahmen**

**Begründung:**
Fibroblastisches Neoplasma ist der einzige der 10 durch TxGNN vorhergesagten Indikationen, der durch eine abgeschlossene klinische Studie und konsistente präklinische Literatur gestützt wird; allerdings ist die Studie klein (n=16), nicht randomisiert, und weder Vergleichsgruppe noch Überlebensergebnisse sind in diesem Paket berichtet, daher bleibt die Evidenz vorläufig (L3).

**Um fortzufahren, wird Folgendes benötigt:**
- TFDA/Deutsche Kennzeichnungsdaten (Warnhinweise, Kontraindikationen) — derzeit eine blockierende Datenlücke, die eine vollständige S1-Sicherheitsprüfung verhindert
- Strukturierte MOA-Daten von DrugBank zur formalen Bestätigung des Mikrotubuli-Inhibitions-Mechanismus
- Wirksamkeits-/Sicherheitsergebnisse (nicht nur Studienregistrierung) aus NCT03840772
- Eine größere, idealerweise randomisierte Studie in SFT/Fibrosarkom, um über L3 hinauszugehen
- DDI- und Kontraindikationsprofil vor Fortgang über die aktuelle Überprüfungsphase hinaus
- Bewertung des regulatorischen Zugangswegs angesichts der Tatsache, dass Eribulin derzeit nicht auf dem deutschen Markt vermarktet wird

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

