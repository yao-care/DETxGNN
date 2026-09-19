---
layout: default
title: Grazoprevir
parent: Nur Modellvorhersage (L5)
nav_order: 186
evidence_level: L5
indication_count: 10
---

# Grazoprevir
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

# Grazoprevir: Von Hepatitis C zu HIV-Infektionskrankheit

## Zusammenfassung in einem Satz

Grazoprevir ist ein HCV-NS3/4A-Proteasehemmer, der als Bestandteil der Fixkombination Zepatier® (Grazoprevir + Elbasvir) vermarktet wird und zur Behandlung der chronischen Hepatitis-C-Virus(HCV)-Genotyp-1-, 4- und 6-Infektion eingesetzt wird. TxGNN prognostiziert einen Score von 99,73% für „HIV-Infektionskrankheit", aber bei der Überprüfung beschreiben alle unterstützenden klinischen Studien und Literaturquellen die Behandlung von HCV bei Patienten, die mit HIV koinfiziert sind – nicht die Behandlung von HIV selbst. Dies ist sehr wahrscheinlich ein Datenbankko-Vorkommen-Artefakt und keine echte pharmakologische Signatur, und das Evidenzpaket selbst kennzeichnet diese Begründung explizit.

## Schnellübersicht

| Element | Inhalt |
|---------|--------|
| Ursprüngliche Indikation | Chronische Hepatitis-C-Virus(HCV)-Infektion, Genotyp 1, 4, 6 – als Proteasehemmer-Komponente von Zepatier® (Grazoprevir + Elbasvir). (Nicht im strukturierten Feld `original_indications` vorhanden; abgeleitet aus konsistenten Evidenzen über Studien/Literatur in diesem Paket.) |
| Prognostizierte neue Indikation | HIV-Infektionskrankheit |
| TxGNN-Prognosescore | 99,73% |
| Evidenzstufe | L5 (nur Modellvorhersage; keine Studie behandelt HIV mit Grazoprevir direkt) |
| Taiwan-Marktstatus | Nicht vermarktet (Nicht vermarktet) |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | **Halten** |

## Warum ist diese Vorhersage angemessen?

Detaillierte formale MOA-Daten für Grazoprevir wurden als Datenlücke in diesem Evidenzpaket gekennzeichnet. Die Evidenz selbst (Studienbeschreibungen und Literaturabstrakte) identifiziert Grazoprevir jedoch konsistent als einen **HCV-NS3/4A-Proteasehemmer**, der mit dem NS5A-Hemmer Elbasvir unter der Marke Zepatier® kombiniert wird, um eine anhaltende virologische Ansprechrate (SVR) bei chronischer HCV-Infektion zu erreichen.

Entscheidend ist, dass **dieser Mechanismus keine bekannte Relevanz für HIV hat**. HIV erfordert die Hemmung seiner eigenen Protease-, Reverse-Transkriptase- oder Integrase-Enzyme – keine davon sind strukturell mit der HCV-NS3/4A-Protease verwandt. Jede einzelne klinische Studie und Literaturquelle, die für diesen Kandidaten gefunden wurde, beschreibt die Behandlung von **HCV** bei Patienten, die auch HIV tragen (HIV/HCV-Koinfektionspopulationen), die HCV-Heilungsraten (SVR12), Leberfibrose, kardiovaskuläres Risiko oder Arzneimittelwechselwirkungen mit Antiretroviralen bewerten. Keine bewertet Grazoprevir als Behandlung für HIV selbst, und keine Virus-Unterdrückung oder CD4/Viruslast-Endpunkt für HIV wird in diesem Evidenzsatz irgendwo gemeldet.

**Schlussfolgerung dieses Abschnitts: Die Vorhersage wird weder mechanistisch noch klinisch unterstützt.** Sie spiegelt höchstwahrscheinlich ein Graphen-Embedding-Artefakt wider, das durch das häufige Co-Vorkommen von „Grazoprevir" und „HIV" in Studienmetadaten für HCV/HIV-koinfizierte Kohorten verursacht wird, anstatt eines echten Umpositionierungssignals.

## Klinische Studienevidenz

| Studiennummer | Phase | Status | Rekrutierung | Wichtigste Ergebnisse |
|---------|------|------|------|---------|
| [NCT02105662](https://clinicaltrials.gov/study/NCT02105662) | Phase 3 | Abgeschlossen | 218 | C-EDGE CO-INFECTION: GZR+EBR für **HCV** GT1/4/6 bei HIV/HCV-koinfiziert, therapienaive Probanden – bewertet HCV-SVR12, nicht HIV-Ergebnisse. |
| [NCT01717326](https://clinicaltrials.gov/study/NCT01717326) | Phase 2 | Abgeschlossen | 573 | C-WORTHY: GZR+EBR±RBV für **HCV**; Arm mit HIV/HCV-Koinfizierung eingeschlossen, primärer Endpunkt ist HCV-SVR12. |
| [NCT02252016](https://clinicaltrials.gov/study/NCT02252016) | Phase 3 | Abgeschlossen | 159 | GZR+EBR für **HCV** GT1/4/6 bei Patienten mit angeborenen Blutungsstörungen, mit/ohne HIV-Koinfizierung. |
| [NCT02785666](https://clinicaltrials.gov/study/NCT02785666) | Phase 3 | Abgeschlossen | 150 | Swiss HCVree Trial: „treat, counsel, cure" Strategie für **HCV** bei HIV-positiven MSM; HIV selbst ist kein Behandlungsziel. |
| [NCT02057003](https://clinicaltrials.gov/study/NCT02057003) | N/A | Unbekannt | 1000 | HEPAVIR-Kohorte: Wirksamkeit/Verträglichkeit von DAA-Regimen für **HCV** bei HIV/HCV-koinfizierte Patienten in der Praxis. |
| [NCT02600325](https://clinicaltrials.gov/study/NCT02600325) | Phase 3 | Abgeschlossen | 80 | DAHHS-2: GZR+EBR für **akute HCV** Genotyp 1/4 bei HIV-positiven Personen. |
| [NCT02897596](https://clinicaltrials.gov/study/NCT02897596) | Phase 3 | Unbekannt | 62 | GZR/EBR für frühe chronische **HCV** GT1/4 bei HIV-koinfizierte Patienten (8 vs. 12 Wochen). |
| [NCT03037151](https://clinicaltrials.gov/study/NCT03037151) | Phase 4 | Unbekannt | 100 | Sicherheit/Fibroseverbesserung mit GZR+EBR für **HCV** GT1/6, zirrhose, mit oder ohne HIV. |
| [NCT03098121](https://clinicaltrials.gov/study/NCT03098121) | Phase 4 | Abgeschlossen | 40 | GZR+EBR für **HCV** GT1 bei PWID/MSM mit HIV-Koinfizierung, vorherige Peg-IFN/RBV-Erfahrung. |
| [NCT03823911](https://clinicaltrials.gov/study/NCT03823911) | Phase 4 | Abgeschlossen | 87 | Kardiovaskuläre Ergebnisse nach **HCV**-Eradikation bei HIV/HCV-koinfiziert vs. HIV-monoinfinziert Kontrollen – keine HIV-Wirksamkeitsstudie. |

**Jede oben genannte Studie behandelt HCV in einer HIV-positiven Population; keine behandelt HIV als Zielkrankheit.**

## Literaturevidenz

| PMID | Jahr | Typ | Journal | Wichtigste Ergebnisse |
|------|-----|------|------|---------|
| [26423374](https://pubmed.ncbi.nlm.nih.gov/26423374/) | 2015 | RCT | The Lancet HIV | C-EDGE CO-INFECTION: Wirksamkeit/Sicherheit von GZR+EBR für **HCV** bei HIV/HCV-koinfizierte Patienten. |
| [25467560](https://pubmed.ncbi.nlm.nih.gov/25467560/) | 2015 | RCT (Phase 2) | Lancet | C-WORTHY: 8 vs. 12 Wochen GZR+EBR±RBV für **HCV** GT1 mono- und HIV/HCV-Koinfizierung. |
| [28689442](https://pubmed.ncbi.nlm.nih.gov/28689442/) | 2017 | Übersicht | Expert Opin Drug Metab Toxicol | Überprüfung von Arzneimittelwechselwirkungen zwischen DAAs (einschl. Grazoprevir) und Antiretroviralen bei HIV-Patienten, die wegen HCV behandelt werden. |
| [30745392](https://pubmed.ncbi.nlm.nih.gov/30745392/) | 2019 | PK-Studie | Antimicrob Agents Chemother | PK-Wechselwirkungen von Elbasvir/Grazoprevir mit HIV-Proteasehemmern (Ritonavir, Atazanavir, Lopinavir, Darunavir). |
| [30541077](https://pubmed.ncbi.nlm.nih.gov/30541077/) | 2019 | DDI-Studie | J Antimicrob Chemother | Wechselwirkungsbewertung zwischen Elbasvir/Grazoprevir und HIV-Integrase-Hemmern (Raltegravir, Dolutegravir). |
| [32246857](https://pubmed.ncbi.nlm.nih.gov/32246857/) | 2020 | Systematische Übersicht/Meta-Analyse | J Gastroenterol Hepatol | Netzwerk-Meta-Analyse der Wirksamkeit/Sicherheit von DAA-Regimen für **HCV** bei HIV/HCV-koinfizierte Patienten. |
| [28417245](https://pubmed.ncbi.nlm.nih.gov/28417245/) | 2017 | Übersicht | Drugs | Umfassende Überprüfung von Elbasvir/Grazoprevir für chronische **HCV** GT1/4. |
| [30233138](https://pubmed.ncbi.nlm.nih.gov/30233138/) | 2018 | Übersicht | Drug Des Devel Ther | Sicherheits- und Wirksamkeitsevidenz für Elbasvir/Grazoprevir bei **HCV**. |
| [27603877](https://pubmed.ncbi.nlm.nih.gov/27603877/) | 2016 | Übersicht | Expert Rev Clin Pharmacol | MOA, PK/PD, Wirksamkeits- und Sicherheitsprüfung von Elbasvir/Grazoprevir für **HCV** GT1/4. |
| [26849059](https://pubmed.ncbi.nlm.nih.gov/26849059/) | 2016 | Übersicht | Expert Opin Drug Metab Toxicol | Pharmakodynamik/Pharmakokinetik von Elbasvir und Grazoprevir bei **HCV**-Behandlung. |

**Keine der obigen Literaturquellen bewertet Grazoprevir als Anti-HIV-Mittel** – die DDI/PK-Papiere beschreiben, wie man Grazoprevir sicher mit Antiretroviralen kombiniert, wenn man HCV bei HIV-positiven Patienten behandelt, nicht die Anti-HIV-Wirksamkeit von Grazoprevir selbst.

## Taiwan-Marktinformationen

Grazoprevir (und die Zepatier®-Kombination) wird **derzeit nicht in Taiwan vermarktet** – 0 registrierte Zulassungen, keine Darreichungsformen aufgezeichnet. Dies bedeutet, dass keine lokalen behördlichen oder sicherheitsrelevanten Kennzeichnungsinformationen verfügbar sind zum Überprüfen.

## Sicherheitserwägungen

Strukturierte Sicherheitsdaten (wichtige Warnhinweise, Kontraindikationen, DDI-Datenbank) waren für diesen Kandidaten nicht verfügbar. Das Literatur-Evidenzpaket enthält jedoch quellengestützte Pharmakokinetik-Interaktionsdaten, die für jede künftige HIV-bezogene Verwendung relevant sind:

- **Arzneimittelwechselwirkungen (aus Literatur, nicht aus strukturierten DDI-Daten):** Elbasvir/Grazoprevir zeigt klinisch signifikante pharmakokinetische Wechselwirkungen mit Ritonavir-geboosterten HIV-Proteasehemmern (Ritonavir, Atazanavir, Lopinavir, Darunavir) und mit HIV-Integrase-Hemmern (Raltegravir, Dolutegravir) (PMID [30745392](https://pubmed.ncbi.nlm.nih.gov/30745392/), [30541077](https://pubmed.ncbi.nlm.nih.gov/30541077/)). Diese Wechselwirkungen sind für HIV/HCV-koinfizierte Patienten, die beide Wirkstoffklassen gleichzeitig erhalten, wichtig, deuten aber nicht auf Anti-HIV-Aktivität von Grazoprevir hin.

Für alle anderen Sicherheitsinformationen verweisen Sie bitte auf die Packungsbeilage, sobald sie von der TFDA formal überprüft wurde.

## Fazit und nächste Schritte

**Entscheidung: Halten**

**Begründung:**
Der TxGNN-Score (99,73%) wird durch keine Studien- oder Literaturevidenz der direkten Behandlung von HIV mit Grazoprevir unterstützt. Alle 10+ Studien und 20 Literaturquellen, die identifiziert wurden, sind HCV-Behandlungsstudien, die in HIV/HCV-koinfizierte Populationen durchgeführt wurden – ein klassisches Co-Vorkommens-Artefakt in Wissensgraph-Modellen. Es gibt keinen bekannten oder plausiblen molekularen Mechanismus (Grazoprevir zielt auf HCV-NS3/4A-Protease; HIV ist abhängig von Protease/Reverse-Transkriptase/Integrase aus einer nicht verwandten Retrovirus-Familie), der die Anti-HIV-Aktivität unterstützt. Grazoprevir wird auch derzeit nicht in Taiwan vermarktet.

**Um fortzufahren, ist Folgendes erforderlich (bevor dies als etwas anderes als Halten betrachtet werden kann):**
- In-vitro-Assay-Daten, die Grazoprevir-Aktivität gegen HIV-Protease, Reverse-Transkriptase oder Integrase bestätigen (oder widerlegen)
- Formale DrugBank/TFDA-MOA und Kennzeichnungsdokumentation (derzeit eine Datenlücke)
- Falls das In-vitro-Signal negativ ist (erwartet), sollte dieser Kandidat eher geschlossen als vorangebracht werden

**Hinweis zu anderen bewerteten Vorhersagen in diesem Paket:** Ränge 2–10 (HBV, HEV, HAV, tierische Hepatitis, Omsk-Hämorrhagisches Fieber, SIV, FIV, eine seltene neurodevelopmentale Störung) wurden auch überprüft und zeigen das gleiche oder schwächere Muster – alle als „Halten" bewertet (L5, keine echte mechanistische oder klinische Unterstützung), außer Rang 7 (Kyasanur-Waldkrankheit), das als **Forschungsfrage** mit niedriger Priorität gekennzeichnet wurde, basierend auf einer In-silico-Docking-Studie (PMID 34662258), die die Konservierung der NS3-Protease der Flaviviridae-Familie über Gattungen hinweg ausnutzt – erfordert dennoch Validierung im Labor, bevor weitere Maßnahmen ergriffen werden.

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

