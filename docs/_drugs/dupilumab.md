---
layout: default
title: Dupilumab
parent: Mittlere Evidenz (L3-L4)
nav_order: 131
evidence_level: L3
indication_count: 10
---

# Dupilumab
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

# Dupilumab: Th2-getriebene Entzündungserkrankung zu Bronchitis

## Zusammenfassung in einem Satz

> Dupilumab ist ein Biologikum, das IL-4Rα-Signalisierung blockiert, um Th2-getriebene (eosinophile) Entzündung zu unterdrücken; seine etablierten ursprünglichen Indikationsdaten sind in diesem Evidenzpaket nicht verfügbar (Arzneimittel noch nicht in Taiwan vermarktet).
> Das TxGNN-Modell prognostiziert, dass es möglicherweise wirksam für **Bronchitis** ist,
> mit derzeit **1 klinischer Studie** und **6 Publikationen** identifiziert, obwohl sich die meisten dieser Evidenzen eher auf Asthma als auf Bronchitis beziehen.

---

## Schnellübersicht

| Artikel | Inhalt |
|---------|--------|
| Ursprüngliche Indikation | Nicht verfügbar — es existiert kein Taiwan-Lizenzbestand für dieses Arzneimittel (`taiwan_regulatory.licenses` ist leer) |
| Vorhergesagte neue Indikation | Bronchitis |
| TxGNN-Prognosescore | 99,92 % |
| Evidenzstufe | L3 |
| Taiwan-Marktstatus | ✗ Nicht vermarktet |
| Anzahl der Genehmigungen | 0 |
| Empfohlene Entscheidung | Halten |

---

## Warum ist diese Vorhersage sinnvoll?

Derzeit sind detaillierte Wirkungsmechanismus-Daten (`original_moa`) als eine Datenlücke gekennzeichnet und Taiwan-spezifische ursprüngliche Indikationsdaten sind nicht verfügbar, da kein Lizenzbestand für dieses Arzneimittel existiert. Jedoch beschreibt die Rationalisierung des Evidenzpakets selbst Dupilumab als einen **IL-4Rα-Antagonisten**, der IL-4/IL-13-Signalisierung blockiert, wodurch Th2-Typ-eosinophile Entzündung unterdrückt wird — ein Mechanismus mit starker, gut dokumentierter Unterstützung in eosinophilem Asthma (siehe Literaturbelege unten).

Die Verbindung zu „Bronchitis" ist mechanistisch plausibel, aber indirekt: Bronchitis ist eine breite diagnostische Kategorie, und die stärksten unterstützenden Evidenzen in diesem Paket (z.B. die TRAVERSE-Langzeitasthma-Erweiterungsstudie und die Asthma-Metaanalyse) befassen sich tatsächlich mit **mittelschwerem bis schwerem Asthma**, nicht mit Bronchitis per se. Die einzige direkt relevante klinische Studie (NCT04362501) zielt auf chronische Rhinosinusitis ohne Nasenpolypen (CRSsNP) ab, nicht auf Bronchitis, und wurde selbst als „C"-Relevanz vom internen Reasoning-Engine bewertet — was nur indirekte Th2-Weg-Unterstützung bietet.

Da eosinophile/Th2-getriebene Atemwegsentzündung sowohl Asthma als auch bestimmte Bronchitis-Phänotypen zugrunde liegt (z.B. eosinophile oder Asthma-COPD-Überlapps-Bronchitis), ist die mechanistische Erweiterung auf Bronchitis biologisch als Forschungshypothese sinnvoll, aber direkte klinische Evidenzen spezifisch für Bronchitis bleiben zu diesem Zeitpunkt begrenzt.

---

## Belege aus klinischen Studien

| Trialnummer | Phase | Status | Einschluss | Wichtigste Erkenntnisse |
|---------|------|------|------|---------|
| [NCT04362501](https://clinicaltrials.gov/study/NCT04362501) | Phase 2 | Abgeschlossen | 33 | Randomisierte, doppelblinde, placebokontrollierte Studie zu Dupilumab bei chronischer Rhinosinusitis ohne Nasenpolypen (CRSsNP); bietet indirekte Th2-Weg-Evidenz, aber untersucht nicht direkt Bronchitis (Relevanz als „C" bewertet). |

---

## Literaturbelege

| PMID | Jahr | Typ | Journal | Wichtigste Erkenntnisse |
|------|-----|------|------|---------|
| [34597534](https://pubmed.ncbi.nlm.nih.gov/34597534/) | 2022 | RCT (offene Erweiterungsstudie) | Lancet Respir Med | Langzeitsicherheit/Wirksamkeit von Dupilumab bei mittelschwerem bis schwerem Asthma über einen Zeitraum von mehr als 1 Jahr (TRAVERSE-Studie). |
| [30273510](https://pubmed.ncbi.nlm.nih.gov/30273510/) | 2019 | Systematisches Review/Metaanalyse | J Asthma | Gepoolte RCT-Daten zeigen, dass Dupilumab die Wirksamkeit und Sicherheitsergebnisse bei unkontrolliertem Asthma verbessert. |
| [32428511](https://pubmed.ncbi.nlm.nih.gov/32428511/) | 2020 | Kohortenstudie/Bildgebungsstudie | Chest | MRT-basierte Belüftungsdefekte bei schwerem eosinophilem Asthma sprechen auf Anti-T2-(Dupilumab-Klasse-)Therapie an. |
| [39904363](https://pubmed.ncbi.nlm.nih.gov/39904363/) | 2025 | Übersichtsarbeit | Tuberc Respir Dis | Umfassende Übersichtsarbeit der pharmakologischen Therapien, einschließlich Biologika, zur Prävention von COPD-Exazerbationen. |
| [30196731](https://pubmed.ncbi.nlm.nih.gov/30196731/) | 2018 | Übersichtsarbeit | Expert Opin Pharmacother | Erörterung der Behandlungschallenges bei Rauchen-induzierter Atemwegserkrankung, einschließlich chronischer Bronchitis und Asthma-COPD-Überlapps. |
| [38488768](https://pubmed.ncbi.nlm.nih.gov/38488768/) | 2024 | Übersichtsarbeit/Fallbasiert | Pediatric Pulmonology | Neuartige Therapien für eosinophile pädiatrische Kunststoffbronchitis. |

---

## Taiwan-Marktinformationen

Dieses Arzneimittel ist derzeit **nicht in Taiwan vermarktet**, und es sind keine Lizenzbestandsaufzeichnungen in diesem Evidenzpaket verfügbar (`total_licenses = 0`). Kein genehmigter Indikationstext kann zu diesem Zeitpunkt extrahiert werden.

---

## Sicherheitsüberlegungen

Bitte beachten Sie die Packungsbeilage für Sicherheitsinformationen.

*(Hinweis: Alle wichtigen Warnungen, Kontraindikationen und Arzneimittelwechselwirkungen sind als Datenlücken gekennzeichnet (DG001 — TFDA-Packungsbeilage noch nicht abgerufen) oder „nicht gefunden" in diesem Evidenzpaket, und können hier nicht zusammengefasst werden.)*

---

## Fazit und nächste Schritte

**Entscheidung: Halten**

**Rationalisierung:**
Evidenzen, die Dupilumab direkt für Bronchitis unterstützen, sind derzeit auf eine einzige Phase-2-Studie mit niedriger Relevanz begrenzt (Grad C, untersuchte eine andere Erkrankung — CRSsNP) plus mechanistische Extrapolation aus Asthma-Literatur. Dies entspricht Evidenzstufe L3 und der „Forschungsfrage"-Phase — noch nicht ausreichend zur Unterstützung des Fortschreitens in Richtung regulatorischer oder klinischer Entwicklung für diese spezifische Indikation.

**Um fortzufahren, ist Folgendes erforderlich:**
- TFDA-Packungsbeilage (Warnungen/Kontraindikationen) — derzeit eine blockierende Datenlücke (DG001)
- Bestätigte Wirkungsmechanismus-Dokumentation über DrugBank (DG002)
- Gewidmete klinische Studien oder Real-World-Evidenzen in einer definierten Bronchitis-Population (z.B. eosinophile oder Asthma-COPD-Überlapps-Bronchitis) anstelle benachbarter Atemwegs-/Nasennebenhöhlen-Indikationen
- Bestätigung des Taiwan-Regulierungs-/Lizenzierungsstatus, da das Arzneimittel derzeit hier nicht vermarktet ist

---

**Hinweis:** Unter den 10 Kandidatenindikationen in diesem Evidenzpaket zeigt **Dermatitis (atopische Dermatitis)** — von TxGNN als #2 bewertet — erheblich stärkere Evidenzen (Evidenzstufe L1, mehrere abgeschlossene Phase-3-RCTs, Empfehlung „Mit Vorsichtsmaßnahmen fortfahren") und ist eine global anerkannte genehmigte Indikation für Dupilumab. Wenn das Ziel darin besteht, die stärkste Umnutzungs-/Registrierungsgelegenheit für diesen Arzneimittelkandidaten zu priorisieren, wird ein separater Bewertungsbericht zur Dermatitisenindikation empfohlen.

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

