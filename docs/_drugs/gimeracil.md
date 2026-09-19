---
layout: default
title: Gimeracil
parent: Nur Modellvorhersage (L5)
nav_order: 178
evidence_level: L5
indication_count: 10
---

# Gimeracil
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

# Gimeracil: Von Komponente des S-1-Kombinationspräparats zur Dickdarmneoplasie (Colonic Neoplasm)

## Ein-Satz-Zusammenfassung

Gimeracil ist selbst kein eigenständiges Zytostatikum, sondern die DPD-(Dihydropyrimidin-Dehydrogenase)-inhibitorische Komponente des S-1-Kombinationspräparats (Tegafur + Gimeracil + Oteracil). Es wirkt durch Blockierung des 5-FU-Metabolismus und verstärkt dadurch die therapeutische Wirksamkeit. Das TxGNN-Modell prognostiziert, dass es (als Komponente des S-1-Kombinationspräparats) möglicherweise bei **Dickdarmneoplasien (Colonic Neoplasm)** wirksam sein könnte. Derzeit werden diese Prognose durch **8 klinische Studien** und **16 Publikationen** gestützt, darunter 2 abgeschlossene Phase-III-randomisierte kontrollierte Studien. Besonders hervorzuheben ist: Die verfügbare Evidenz betrifft das „S-1-Kombinationspräparat als Ganzes" bei Kolorektalkarzinomen und nicht die Einzelkomponente Gimeracil.

---

## Schnellübersicht

| Merkmal | Inhalt |
|--------|--------|
| Ursprüngliche Indikationen | Keine eigenständigen zugelassenen Indikationen (Gimeracil als Komponente des S-1-Kombinationspräparats, kein direktes Zytostatikum) |
| Prognostizierte neue Indikation | Dickdarmneoplasie (Colonic Neoplasm) |
| TxGNN-Prognosescore | 99.88% |
| Evidenzlevel | L1 (≥2 abgeschlossene Phase-III-RCT) |
| Marktstadt Deutschland/Taiwan | Nicht vermarktet |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | Proceed with Guardrails (bedingte Weiterverfolgung) |

---

## Warum ist diese Vorhersage rational?

DrugBank stellt derzeit keine offizielle Wirkmechanismus-(MOA)-Information für Gimeracil bereit. Basierend auf verfügbarer Literatur und Studiendaten lässt sich ableiten, dass Gimeracil selbst **keine direkte zytostatische Aktivität** besitzt. Seine pharmakologische Rolle besteht darin, das DPD-Enzym zu hemmen und dadurch die Umwandlung und Metabolisierung des aus Tegafur entstehenden 5-FU zu blockieren, wodurch die Plasmakonzentration und die Tumorexposition von 5-FU erhöht werden und die therapeutische Wirkung verstärkt wird. Die Arzneimittelwirkung von Gimeracil muss daher im Kontext des S-1-Kombinationspräparats (Tegafur + Gimeracil + Oteracil) verstanden werden, nicht als Einzelsubstanz.

Dickdarmneoplasien und S-1 gehören – wie die derzeit hauptsächlich zugelassenen Indikationen (z. B. Magenkarzinom) – beide zu Adenokarzinomen des Verdauungstrakts, deren Empfindlichkeit gegenüber 5-FU-haltigen Arzneimitteln auf ähnlichen Mechanismen beruht. Tatsächlich ist das S-1-Kombinationspräparat bereits in Japan und einigen europäischen Ländern (einschließlich Deutschland, wenn Capecitabin/5-FU aufgrund von Hand-Fuß-Syndrom oder kardiovaskulärer Toxizität abgesetzt werden musste) für die Behandlung von Kolorektalkarzinomen zugelassen. Dies ist der Hauptgrund, warum diese TxGNN-Prognose durch eine große Anzahl von klinischen Studien und Publikationen gestützt wird.

Eine wichtige Einschränkung sei betont: Fast alle in diesem Bericht zitierten Daten beziehen sich auf die Wirksamkeit und Sicherheit des „S-1-Kombinationspräparats insgesamt", nicht auf unabhängige pharmakologische Daten der Einzelkomponente Gimeracil. Vor einer abschließenden Entscheidung muss geklärt werden, ob Gimeracil eine klinische Stellung unabhängig vom S-1-Kombinationspräparat hat.

---

## Evidenz aus klinischen Studien

| Studiennummer | Phase | Status | Fallzahl | Hauptergebnis |
|---------------|-------|--------|----------|--------------|
| [NCT00660894](https://clinicaltrials.gov/study/NCT00660894) | Phase 3 | Completed | 1535 | UFT+Leucovorin vs. S-1 zur adjuvanten Therapie des Stadium-III-Kolontumors mit Analyse von Genexpressionsmarkern; unterstützt direkt Wirksamkeit und Sicherheit von S-1 (enthält Gimeracil) bei dieser Indikation |
| [NCT01918852](https://clinicaltrials.gov/study/NCT01918852) | Phase 3 | Completed | 161 | SALTO-Studie: S-1 vs. Capecitabin als First-Line-Therapie von metastasierten Kolorektalkarzinomen, auch mit Bevacizumab kombinierbar |
| [NCT03448549](https://clinicaltrials.gov/study/NCT03448549) | Phase 3 | Unknown | 1191 | Große randomisierte kontrollierte Studie SOX vs. XELOX zur adjuvanten Therapie von Stadium-III-Kolontumoren; Status unklar, Veröffentlichung von Ergebnissen bedarf Überprüfung |
| [NCT02618356](https://clinicaltrials.gov/study/NCT02618356) | Phase 2 | Unknown | 82 | S-1 + Raltitrexed bei metastasierten Kolorektalkarzinomen nach Standardchemotherapie, primärer Endpunkt: progressionsfreies Überleben |
| [NCT00524706](https://clinicaltrials.gov/study/NCT00524706) | Phase 1/2 | Unknown | 42 | S-1 + orales Leucovorin + Oxaliplatin (SOL) bei unbehandelten metastasierten Kolorektalkarzinomen |
| [NCT00974389](https://clinicaltrials.gov/study/NCT00974389) | Phase 2 | Unknown | 40 | S-1 + Bevacizumab bei nicht resezierbarem oder rezidivierendem Kolorektalkarzinom nach Versagen von Irinotecan- und Oxaliplatin-Therapie |
| [NCT02216149](https://clinicaltrials.gov/study/NCT02216149) | Phase 2 | Terminated | 20 | Bewertung der Auswirkungen von S-1 und Capecitabin in Kombination mit Oxaliplatin auf koronaren Blutfluss (sicherheitsorientiert, keine Wirksamkeitsstudie; beendet) |
| [NCT06255379](https://clinicaltrials.gov/study/NCT06255379) | Phase 2 | Not yet recruiting | 52 | Fuquinitinib kombiniert mit S-1 (enthält Gimeracil) zur Therapie von metastasierten Kolorektalkarzinomen in der dritten Linie; noch keine Rekrutierung, nur Zukunftsplan |

---

## Literaturbasierte Evidenz

| PMID | Jahr | Typ | Journal | Hauptergebnis |
|------|------|------|---------|----------------|
| [21875473](https://pubmed.ncbi.nlm.nih.gov/21875473/) | 2011 | Kohortenstudie/Review | Chinese Journal of Cancer | Oxaliplatin + S-1 zur Therapie postoperativer Kolorektalkarzinome; Beobachtung von Wirksamkeit und Nebenwirkungen |
| [21084813](https://pubmed.ncbi.nlm.nih.gov/21084813/) | 2010 | Kohortenstudie | Gan to Kagaku Ryoho | S-1 + Irinotecan bei 87 Patienten mit fortgeschrittenem/rezidivierendem Kolorektalkarzinom; Grad-3-4-Hämatotoxizität in 16,1% der Fälle, Entwicklung eines Risiko-Stratifizierungsmodells |
| [41724114](https://pubmed.ncbi.nlm.nih.gov/41724114/) | 2026 | Realwelt-Bevölkerungsstudie | Eur J Cancer | Sicherheit und Machbarkeit des Wechsels von Capecitabin zu S-1 bei adjuvanter Kolorektalkarzinom-Therapie aufgrund von Hand-Fuß-Syndrom oder kardiovaskulärer Toxizität |
| [20841935](https://pubmed.ncbi.nlm.nih.gov/20841935/) | 2010 | PK-Studie | Gan to Kagaku Ryoho | Pharmakokinetik von S-1 bei peritonealer Metastasierung von Kolorektalkarzinom in Maus-Peritonitis-Modell |
| [20811661](https://pubmed.ncbi.nlm.nih.gov/20811661/) | 2010 | Präklinisch | Oncology Reports | Irinotecan kombiniert mit oralem S-1 (enthält Gimeracil) überwindet 5-FU-Resistenz in humanen Kolorektalkarzinom-Xenotransplantaten |
| [18630468](https://pubmed.ncbi.nlm.nih.gov/18630468/) | 2008 | Fallbericht | Anticancer Research | Fallbericht: S-1 + CPT-11 führte zu kompletter Remission und Erhaltung von Lebermetastasen bei Kolorektalkarzinom |
| [35444144](https://pubmed.ncbi.nlm.nih.gov/35444144/) | 2022 | Fallbericht | Gan to Kagaku Ryoho | Kolorektalkarzinom-Peritonealrezidiv, mehrfache laparoskopische Resektion mit postoperativer adjuvanter Chemotherapie mit Tegafur-haltigen Substanzen |
| [29483452](https://pubmed.ncbi.nlm.nih.gov/29483452/) | 2018 | Fallbericht | Gan to Kagaku Ryoho | Horizontales Kolontumor mit Lebermetastasen und portaler Tumorthrombose, effektive Kontrolle durch Chemotherapie (einschließlich S-1-basierte Chemotherapie-Umstellung) |
| [29394831](https://pubmed.ncbi.nlm.nih.gov/29394831/) | 2017 | Fallbericht | Gan to Kagaku Ryoho | Zäkales Karzinom mit multiplen bilateralen Lebermetastasen; neoadjuvante Chemotherapie mit SOX (Tegafur-Gimeracil-Oteracil + Oxaliplatin) + Panitumumab gefolgt von gestaffelter Leberresektion |
| [30692384](https://pubmed.ncbi.nlm.nih.gov/30692384/) | 2018 | Fallbericht | Gan to Kagaku Ryoho | Kolorektalkarzinom-Rezidiv mit Schmerzen; CT-gesteuerter Nervenblock des Plexus coeliacus mit kompletter Remission (adjuvante postoperative Chemotherapie mit UFT-haltigen Substanzen) |

---

## Informationen zur Zytotoxizität

Gimeracil als Komponente des S-1-Kombinationspräparats (traditionelle Chemotherapie, Fluoropyrimidin-Kombinationen) ist selbst zwar kein direktes zytostatisches Arzneimittel, aber seine pharmakologische Funktion besteht darin, die zytostatische Wirkung von 5-FU zu verstärken. Daher muss es wie ein Chemotherapeutikum gehandhabt und überwacht werden.

| Merkmal | Inhalt |
|--------|--------|
| Zytotoxische Klassifizierung | Komponente des S-1-Kombinationspräparats (Fluoropyrimidin-Klasse); Gimeracil selbst ist ein DPD-Inhibitor und kein direkt zytostatisches Arzneimittel, wirkt durch Verstärkung der zytostatischen Wirkung von 5-FU |
| Myelosuppressionsrisiko | Moderat (Grad-3-4-Hämatotoxizität bei S-1 + Irinotecan-Kombinationen ca. 16,1%, siehe PMID 21084813) |
| Emetogenitätsklassifizierung | Niedrig bis moderat (vergleichbar mit anderen oralen Fluoropyrimidin-Arzneimitteln) |
| Überwachungsparameter | Vollblutbild (einschließlich Differenzialzählung), Nierenfunktion (S-1/Gimeracil-Dosisanpassung je nach Nierenfunktion), Leberfunktion, Elektrolyte |
| Handhabung und Schutz | Bestandteil eines Chemotherapie-Kombinationspräparats; muss nach Handhabungsrichtlinien für zytostatische Arzneimittel behandelt werden |

---

## Sicherheitsaspekte

Bitte beachten Sie die Gebrauchsinformation des Arzneimittels für Sicherheitsinformationen.

(Derzeit sind die Warnhinweise in der Gebrauchsinformation, Kontraindikationen und Arzneimittelwechselwirkungen für TFDA/BfArM fehlende Daten, die als Blocking-Level-Datenlücke DG001 eingestuft sind und müssen daher prioritär ergänzt werden, bevor eine S1-Sicherheitsbewertung durchgeführt werden kann.)

---

## Fazit und nächste Schritte

**Entscheidung: Proceed with Guardrails (bedingte Weiterverfolgung)**

**Begründung:**
- Es gibt 2 abgeschlossene Phase-III-randomisierte kontrollierte Studien (NCT00660894, n=1535; NCT01918852, n=161), die die Wirksamkeit von S-1 (enthält Gimeracil) bei Kolorektalkarzinomen unterstützen, mit Evidenzlevel L1.
- Diese Evidenz bezieht sich jedoch auf das „S-1-Kombinationspräparat als Ganzes" und nicht auf die Einzelkomponente Gimeracil. Darüber hinaus fehlen derzeit sowohl die offizielle Wirkmechanismus-Information für Gimeracil als auch Sicherheitsdaten (Warnhinweise, Kontraindikationen, Arzneimittelwechselwirkungen) aus den TFDA/BfArM-Gebrauchsinformationen. Die Warnhinweise/Kontraindikationen sind auf Blocking-Level eingestuft (DG001), daher „Cannot proceed to S1 safety screening". Es wird daher nicht empfohlen, dies direkt als „Go" einzustufen.

**Zur Weiterverfolgung erforderlich:**
- TFDA/BfArM-Gebrauchsinformation (PDF) mit Analyse der Warnhinweise und Kontraindikationen (DG001, Blocking)
- DrugBank-API-Abfrage des formalen Wirkmechanismus von Gimeracil (DG002, High)
- Klärung, ob Gimeracil eine klinische Stellung unabhängig vom S-1-Kombinationspräparat hat und eigenständige Wirksamkeitsdaten vorliegen
- Ergänzung der Ergebnisse zur Arzneimittelwechselwirkung (DDI) aus Datenbanken

*Hinweis: TxGNN prognostiziert für dieses Arzneimittel weitere 9 kandidatische Indikationen (z. B. villöses Adenom des Zäkums, malignes Granularzelltumor des Magens), die jedoch keine Unterstützung durch klinische Studien oder Literatur haben (Evidenzlevel L5, nur Modellscore). Diese sollten als „Hold" gekennzeichnet werden und nicht weiter verfolgt werden.*

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

