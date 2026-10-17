---
layout: default
title: Imiquimod
parent: Nur Modellvorhersage (L5)
nav_order: 236
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Imiquimod: vorhergesagte neue Indikation Prämalignes Neoplasma (pre-malignant neoplasm) (Evidenzstufe L5). Ursprüngliche Indikation: Condylomata acuminata, Keratose, aktinische Keratose…"
monitor_inn: "IMIQUIMOD"
predicted_indications: ["benign neoplasm of buccal mucosa", "cervical neuroblastoma", "odontogenic cyst", "benign neoplasm of tongue", "nasopharyngeal teratoma", "cystic neoplasm", "inner ear neoplasm", "neoplasm of major salivary gland", "schwannoma of jugular foramen"]
---

# Imiquimod
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **10** 
{: .fs-6 .fw-300 }

---

## Inhaltsverzeichnis
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmazeutischer Bewertungsbericht

</div>

# Imiquimod: Von aktinischer Keratose zu prämalignen Neoplasien

## Zusammenfassung

Imiquimod ist ein topisch angewendeter Immunmodulator, der ursprünglich zur Behandlung von Feigwarzen (Condylomata acuminata), aktinischer Keratose und Basalzellkarzinom zugelassen war.
Das TxGNN-Modell sagt voraus, dass er bei **prämalignen Neoplasien** wirksam sein könnte.
Dafür liegen derzeit **2 klinische Studien** (beide klein bzw. vorzeitig beendet) und **9 Publikationen** vor, darunter zwei Cochrane-Reviews.

---

## Kurzüberblick

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Condylomata acuminata, Keratose, aktinische Keratose, Basalzellkarzinom |
| Vorhergesagte neue Indikation | Prämalignes Neoplasma (pre-malignant neoplasm) |
| TxGNN-Vorhersagewert | 99,92 % |
| Evidenzniveau | L1 (laut Bewertung der Datenzusammenstellung; siehe Hinweis unten) |
| Marktstatus in Deutschland | Nur erloschene/gelöschte Zulassungen |
| Anzahl der Zulassungen | 2 (beide erloschen) |
| Empfohlene Entscheidung | Proceed with Guardrails |

**Hinweis zur Evidenzstufe:** Die Datenzusammenstellung ordnet L1 zu. Strikt nach den Regeln (≥2 abgeschlossene Phase-3-RCTs) ist L1 jedoch nicht erfüllt: Es gibt nur eine abgeschlossene, einarmige Phase-3-Studie (n = 20) und eine vorzeitig abgebrochene Phase-3-RCT (n = 9). Die Evidenz ist daher konservativ eher als L3 (Reviews, Fallberichte) einzustufen.

---

## Warum ist diese Vorhersage plausibel?

Imiquimod ist ein Agonist des Toll-like-Rezeptors 7 (TLR7). Er löst lokal eine angeborene und adaptive Immunantwort gegen Tumorzellen aus (u. a. Interferon-alpha, TNF-alpha, IL-12). Die detaillierten Mechanismusdaten aus der Arzneimitteldatenbank lagen für diesen Bericht nicht vor; die Angaben stützen sich auf die mechanistische Bewertung der Datenzusammenstellung.

Die aktinische Keratose, eine der ursprünglichen Indikationen, ist selbst eine prämaligne Hautläsion. Es ist daher naheliegend, dass dieselbe immunvermittelte Abräumung auch bei intraepithelialen Neoplasien von Zervix, Vulva, Anus und Penis wirkt. Diese sind häufig HPV-assoziiert, und Imiquimod ist bereits bei HPV-bedingten Läsionen (Feigwarzen) etabliert.

---

## Evidenz aus klinischen Studien

| Studiennummer | Phase | Status | Teilnehmerzahl | Kernaussagen |
|---------|------|------|------|---------|
| [NCT00175643](https://clinicaltrials.gov/study/NCT00175643) | Phase 3 | Abgeschlossen | 20 | Offene Studie zu Imiquimod 5 % Creme (3×/Woche, 1–2 Zyklen) bei aktinischen Keratosen im Kopfbereich; untersucht die Wirkdauer. Klein und überlappt mit der bestehenden Indikation. |
| [NCT02329171](https://clinicaltrials.gov/study/NCT02329171) | Phase 3 | Abgebrochen | 9 | Randomisierte Studie zu topischem Imiquimod bei hochgradiger zervikaler intraepithelialer Neoplasie (CIN 2–3) als nicht-invasive Alternative zur Schlingenexzision. Wegen sehr geringer Teilnehmerzahl nicht aussagekräftig. |

---

## Literaturevidenz

| PMID | Jahr | Typ | Journal | Kernaussagen |
|------|-----|------|------|---------|
| [23235673](https://pubmed.ncbi.nlm.nih.gov/23235673/) | 2012 | Systematischer Review (Cochrane) | Cochrane Database Syst Rev | Interventionen bei analer intraepithelialer Neoplasie, einer prämalignen HPV-assoziierten Läsion |
| [21491403](https://pubmed.ncbi.nlm.nih.gov/21491403/) | 2011 | Systematischer Review (Cochrane) | Cochrane Database Syst Rev | Medikamentöse Therapien bei hochgradiger vulvärer intraepithelialer Neoplasie |
| [26516853](https://pubmed.ncbi.nlm.nih.gov/26516853/) | 2015 | Review | Int J Mol Sci | Kombinationstherapien mit photodynamischer Therapie bei nicht-melanozytärem Hautkrebs |
| [15584683](https://pubmed.ncbi.nlm.nih.gov/15584683/) | 2004 | Review | Semin Cutan Med Surg | Topische Strategien (u. a. Imiquimod) bei nicht-melanozytärem Hautkrebs und Vorstufen |
| [20505896](https://pubmed.ncbi.nlm.nih.gov/20505896/) | 2010 | Review | Skin Therapy Lett | Aktuelles Management aktinischer Keratosen als prämaligne Läsionen |
| [30284955](https://pubmed.ncbi.nlm.nih.gov/30284955/) | 2019 | Fallbericht | Int J STD AIDS | Erfolgreiche Behandlung einer hochgradigen vulvären intraepithelialen Neoplasie mit Imiquimod 5 % bei einer Nierentransplantierten |
| [15601490](https://pubmed.ncbi.nlm.nih.gov/15601490/) | 2004 | Fallbericht | Int J STD AIDS | Bowenoide Papulose des Penis erfolgreich mit Imiquimod 5 % behandelt |
| [29500135](https://pubmed.ncbi.nlm.nih.gov/29500135/) | 2018 | Präklinisch | Urol Oncol | Pharmakokinetik von TLR7-Agonisten im Rattenmodell (Blasenkrebs-Forschung) |

---

## Marktinformationen Deutschland

| Zulassungsnummer | Produktname | Darreichungsform | Zugelassene Indikation |
|---------|------|------|-----------|
| EMEA/H/C/000179 | Aldara (erloschen) | – | Condylomata acuminata, Keratose, aktinische Keratose, Basalzellkarzinom |
| EMEA/H/C/002387 | Zyclara (erloschen) | – | Keratose, aktinische Keratose |

Beide Zulassungen (Inhaber: Viatris Healthcare Limited) sind erloschen; derzeit ist keine gültige Zulassung vorhanden.

---

## Sicherheitsaspekte

- **Kontraindikationen aus dem Wissensgraphen (keine Packungsbeilagen-Angaben):** Photoparoxysmale Reaktion, Lichtüberempfindlichkeit, Autoimmunerkrankungen, Graft-versus-Host-Erkrankung, Sonnenbrand.
- **Wechselwirkungen:** Es wurden 59 mögliche Wechselwirkungen erfasst, jeweils ohne Schweregradeinstufung. Beispiele: Warfarin, Clopidogrel, Acetylsalicylsäure, Prednison, Prednisolon, Budesonid, Simvastatin, Omeprazol, Morphin, Hydroxychloroquin.
- **Hinweise aus der Literatur:** Fallberichte beschreiben unter Imiquimod eine maligne Konversion oraler Papillomatose, einen Lichen planopilaris sowie ein Erythema multiforme.

Für Warnhinweise und Kontraindikationen siehe die Fachinformation.

---

## Fazit und nächste Schritte

**Entscheidung: Proceed with Guardrails**

**Begründung:**
Der Wirkmechanismus passt gut zu prämalignen Epithelläsionen, und es gibt Cochrane-Reviews sowie Fallberichte zu intraepithelialen Neoplasien. Die Studienlage ist jedoch dünn (eine kleine einarmige Studie, eine abgebrochene RCT mit 9 Teilnehmern), und es besteht derzeit keine gültige Zulassung in Deutschland.

**Für das weitere Vorgehen erforderlich:**
- Auswertung der Fachinformation (Warnhinweise, Kontraindikationen), da diese Daten fehlen und die Sicherheitsprüfung bislang blockieren
- Detaillierte Mechanismusdaten aus der Arzneimitteldatenbank
- Adäquat gepowerte, randomisierte Studien zu CIN, VIN oder AIN
- Klärung des Zulassungsstatus und der verfügbaren Darreichungsformen
- Prüfung der Wechselwirkungen mit klinischer Schweregradeinstufung
- Sicherheitsüberwachung bei Photosensibilität, Autoimmunerkrankungen und Immunsuppression

**Weitere Vorhersagen (Kurzüberblick):** Für „benign neoplasm of buccal mucosa" und „odontogenic cyst" (Evidenz L3) besteht lediglich Forschungsbedarf. Die Indikationen „cervical neuroblastoma", „nasopharyngeal teratoma", „neoplasm of major salivary gland", „schwannoma of jugular foramen", „benign neoplasm of tongue", „cystic neoplasm" und „inner ear neoplasm" werden mangels Evidenz mit Hold bewertet.
## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

