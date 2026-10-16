---
layout: default
title: Bedaquiline
parent: Nur Modellvorhersage (L5)
nav_order: 54
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Bedaquiline: vorhergesagte neue Indikation Inaktive Tuberkulose (Evidenzstufe L5). Ursprüngliche Indikation: Multiresistente Tuberkulose"
monitor_inn: "Bedaquiline"
predicted_indications: ["tuberculosis, bovine", "inactive tuberculosis", "tuberculous ascites", "tuberculosis, avian", "tuberculoma", "vulvovaginal candidiasis", "fascioliasis", "urea cycle disorder", "cutaneous tuberculosis", "esophageal candidiasis"]
---

# Bedaquiline
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

# Bedaquilin: Von multiresistenter Tuberkulose zu inaktiver Tuberkulose

## Zusammenfassung

Bedaquilin wird zur Behandlung der multiresistenten Tuberkulose (MDR-TB) eingesetzt.
Das TxGNN-Modell sagt voraus, dass es auch bei **inaktiver (latenter) Tuberkulose** wirksam sein könnte.
Dafür liegen derzeit **3 klinische Studien** und **19 Publikationen** vor, wobei die einzige direkt relevante Studie zur Prävention noch rekrutiert und keine Ergebnisse hat.

---

## Schnellübersicht

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Multiresistente Tuberkulose |
| Vorhergesagte neue Indikation | Inaktive Tuberkulose |
| TxGNN-Vorhersagewert | 99,96 % |
| Evidenzstufe | L1 (laut den für diesen Bericht zusammengestellten Daten; die Einstufung beruht auf dem Studiendesign und der Evidenz aus der Behandlungsphase, nicht auf Wirksamkeitsdaten zur Prävention) |
| Marktstatus in Deutschland | Nur erloschene Zulassung |
| Anzahl der Zulassungen | 1 (erloschen) |
| Empfohlene Entscheidung | Proceed with Guardrails |

---

## Warum ist diese Vorhersage plausibel?

Zum Wirkmechanismus liegen in den zusammengestellten Daten keine detaillierten Angaben aus der Arzneimitteldatenbank vor. Bekannt ist, dass Bedaquilin die mykobakterielle ATP-Synthase (Untereinheit c der F-ATP-Synthase) hemmt. Seine Wirksamkeit bei MDR-TB ist belegt.

Eine inaktive (latente) Tuberkulose ist ein Zustand, in dem *M. tuberculosis* in einem Zustand geringer Replikation persistiert. Die ATP-Synthase ist auch für den Energiestoffwechsel nicht replizierender Bakterien notwendig. Eine Wirkung gegen persistierende Erreger ist daher mechanistisch plausibel.

Die Prävention bei Kontaktpersonen mit MDR-TB und bei Menschen mit HIV wird derzeit in einer Phase-2/3-Studie (BREACH-TB) geprüft. Da diese noch rekrutiert, gibt es bisher keine Wirksamkeitsergebnisse.

---

## Klinische Studienevidenz

| Studiennummer | Phase | Status | Teilnehmerzahl | Kernaussagen |
|---------|------|------|------|---------|
| [NCT06568484](https://clinicaltrials.gov/study/NCT06568484) | Phase 2/3 | Rekrutierend | 2530 | 4 Wochen Bedaquilin vs. Standardregime zur Prävention von Tuberkulose bei Menschen mit HIV und Hochrisiko-Kontaktpersonen (offen, Nichtunterlegenheit); direkt relevant, noch keine Ergebnisse |
| [NCT05766267](https://clinicaltrials.gov/study/NCT05766267) | Phase 2/3 | Aktiv, nicht rekrutierend | 288 | CRUSH-TB: 17-Wochen-Kurzzeitregime mit Bedaquilin, Moxifloxacin, Pyrazinamid plus Rifabutin oder Delamanid bei Lungentuberkulose; betrifft aktive Erkrankung, daher nur indirekt relevant |
| [NCT07069582](https://clinicaltrials.gov/study/NCT07069582) | Phase 1 | Noch nicht rekrutierend | 60 | Pharmakokinetik von Antituberkulotika (u. a. Bedaquilin) in Plasma und Muttermilch stillender Frauen; keine Wirksamkeitsdaten |

---

## Literaturevidenz

| PMID | Jahr | Typ | Journal | Kernaussagen |
|------|-----|------|------|---------|
| [28625141](https://pubmed.ncbi.nlm.nih.gov/28625141/) | 2018 | Review | Recent Patents on Anti-Infective Drug Discovery | Bedaquilin als Hoffnung für kürzere und bessere Tuberkulose-Regime |
| [39766559](https://pubmed.ncbi.nlm.nih.gov/39766559/) | 2024 | Review | Antibiotics (Basel) | Inhibitoren und Zielstrukturen der F-ATP-Synthase von *M. tuberculosis*; Bedeutung für ruhende Bakterien |
| [39301910](https://pubmed.ncbi.nlm.nih.gov/39301910/) | 2025 | Review | Infectious Disorders Drug Targets | Neue Darreichungssysteme für Bedaquilin; Wirkung auch gegen persistierende bzw. latente Formen |
| [36915977](https://pubmed.ncbi.nlm.nih.gov/36915977/) | 2022 | Review | Zhejiang Da Xue Xue Bao Yi Xue Ban | Fortschritte bei Diagnose und Behandlung der latenten Tuberkulose-Infektion |
| [39887565](https://pubmed.ncbi.nlm.nih.gov/39887565/) | 2025 | Review | Respirology | Aktueller Überblick für Kliniker; Tuberkulose als Krankheitsspektrum mit subklinischen Formen |
| [36982277](https://pubmed.ncbi.nlm.nih.gov/36982277/) | 2023 | Review | Int J Mol Sci | Pathogenese, aktuelle Therapieregime und neue Zielstrukturen |
| [33837535](https://pubmed.ncbi.nlm.nih.gov/33837535/) | 2021 | Review | Clin Pharmacol Ther | Behandlung der Tuberkulose (latent und aktiv) |
| [37316702](https://pubmed.ncbi.nlm.nih.gov/37316702/) | 2023 | Review | Innere Medizin (Heidelberg) | Neuerungen in der Tuberkulosetherapie |
| [28776518](https://pubmed.ncbi.nlm.nih.gov/28776518/) | 2017 | Review | Int J Mycobacteriol | Wirkstoffe gegen nicht replizierende Tuberkulosebakterien |
| [29580819](https://pubmed.ncbi.nlm.nih.gov/29580819/) | 2018 | Review | Lancet Infect Dis | Fortschritte bei neuen Wirkstoffen, Therapieregimen und wirtsgerichteten Therapien |

Bei den aufgeführten Arbeiten handelt es sich ausschließlich um Übersichtsarbeiten; randomisierte kontrollierte Studien zur Prävention liegen nicht vor.

---

## Informationen zum Markt in Deutschland

| Zulassungsnummer | Produktname | Darreichungsform | Zugelassene Indikation |
|---------|------|------|-----------|
| EMEA/H/C/002614 | Sirturo | – | Multiresistente Tuberkulose |

Die Zulassung ist erloschen (Status: nur erloschene Zulassung).

---

## Sicherheitsaspekte

**Wechselwirkungen:** In den zusammengestellten Daten sind 100 Wechselwirkungen verzeichnet. Zu den Wechselwirkungen mit Einstufung „schwerwiegend" (Major) zählen u. a.:
- Dexamethason
- Clarithromycin
- Dolasetron
- Palonosetron
- Picosulfat
- Polyethylenglykol (3350 mit Elektrolyten)
- Natriumsulfat

Weitere Wechselwirkungen sind als „mäßig" eingestuft, darunter Acarbose, Famotidin, Doxycyclin, Pioglitazon, Loperamid, Bupropion, Minocyclin, Tetracyclin und Naltrexon.

**Weitere Hinweise aus der Bewertung:** Zu beachten sind QT-Verlängerung und Hepatotoxizität. Bei HIV-Koinfektion ist besondere Vorsicht bei gleichzeitiger Gabe von CYP3A4-Induktoren oder -Inhibitoren geboten.

Für Warnhinweise und Gegenanzeigen der Fachinformation liegen keine Daten vor. Bitte die Fachinformation zu Rate ziehen.

---

## Fazit und nächste Schritte

**Entscheidung: Proceed with Guardrails**

**Begründung:**
Der Wirkmechanismus ist für persistierende Bakterien plausibel, und Bedaquilin ist bei MDR-TB gut etabliert. Mit BREACH-TB läuft eine Phase-2/3-Studie direkt zur Prävention, deren Ergebnisse jedoch noch ausstehen. Die Evidenzstufe L1 stützt sich auf das Studiendesign und die Behandlungsevidenz, nicht auf Wirksamkeitsdaten zur Prävention.

**Für das weitere Vorgehen sind erforderlich:**
- Ergebnisse der Studie BREACH-TB (NCT06568484)
- Daten aus der Fachinformation zu Warnhinweisen und Gegenanzeigen (derzeit blockierende Datenlücke für das Sicherheits-Screening)
- Detaillierte Wirkmechanismus-Daten aus der Arzneimitteldatenbank
- Sicherheitsüberwachungsplan (QT-Intervall, Leberwerte, Wechselwirkungsmanagement, insbesondere bei HIV-Koinfektion)
- Klärung des Zulassungsstatus in Deutschland, da die einzige erfasste Zulassung erloschen ist
## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

