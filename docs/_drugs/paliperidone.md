---
layout: default
title: Paliperidone
parent: Nur Modellvorhersage (L5)
nav_order: 289
evidence_level: L5
indication_count: 10
---

# Paliperidone
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

# Paliperidon: Von Schizophrenie zu Netzhautdystrophie mit oder ohne extraokulären Anomalien

## Zusammenfassung in einem Satz

> Paliperidon ist ein D2/5-HT2A-Rezeptorantagonist, der klinisch zur Behandlung von Schizophrenie eingesetzt wird.
> Die Top-Vorhersage des TxGNN-Modells ist **Netzhautdystrophie mit oder ohne extraokulären Anomalien**,
> aber dieser Kandidat hat **0 klinische Studien** und **15 Publikationen**, von denen keine Paliperidon oder seine Pharmakologie erwähnen — das Evidenzpaket des Arzneimittels selbst kennzeichnet dies als wahrscheinlich ein Falsch-Positiv der Embedding-Ähnlichkeit statt eines echten mechanistischen Signals.

---

## Schnellübersicht

| Element | Inhalt |
|---------|--------|
| Ursprüngliche Indikation | Nicht in BfArM/Regulierungsdaten dokumentiert (Produkt nicht in Deutschland zugelassen); bekannte klinische Anwendung ist Schizophrenie, hergeleitet aus Mechanismusnoten anderswo in diesem Evidenzpaket |
| Vorhergesagte neue Indikation | Netzhautdystrophie mit oder ohne extraokulären Anomalien |
| TxGNN-Vorhersage-Punktzahl | 99.92% |
| Evidenzebene | L5 |
| Marktstatus Deutschland | Nicht zugelassen |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | Halten |

---

## Warum ist diese Vorhersage angemessen?

**Das ist sie nicht.** Detaillierte MOA-Daten werden als Datenlücke im Arzneimitteldatensatz gekennzeichnet, aber das Begründungsfeld des Evidenzpakets selbst (aus dem Kandidaten auf Rang #10 gezogen) bestätigt, dass Paliperidon ein D2/5-HT2A-Rezeptorantagonist ist — ein zentral wirkendes antipsychotisches Wirkprinzip ohne bekannte Verbindung zu retinalen Entwicklungsgenen oder ophthalmischen Strukturwegen.

Die Netzhautdystrophie-Vorhersage rangiert #1329 aus der vollständigen Ausgabe des Modells und trägt einen sehr hohen Raw-Ähnlichkeitswert, aber die Magnitude des Scores allein begründet keine biologische Plausibilität. Die 15 unterstützenden Publikationen, die für diesen Kandidaten abgerufen wurden, behandeln unverwandte ophthalmologische Themen — Orbitalinfektionen, Diplopie, kongenitale Ptose, Kryptophthalmie, kongenitale kraniale Dysinnervationsstörungen — und **keine erwähnt Paliperidon, Antipsychotika oder D2/5-HT2A-Signalisierung**. Das Evidenzpaket selbst charakterisiert dies als wahrscheinlich ein Falsch-Positiv, das durch Embedding-Raum-Ähnlichkeit verursacht wird, statt einer echten mechanistischen Verbindung.

Kandidaten mit Rang #2–#9 (X-gebundene Myopie, Hydranenzephalie, angeborene Glykosylierungsstörungen, Charcot-Marie-Tooth-Krankheit Typ 1G usw.) teilen das gleiche Muster: hohe TxGNN-Punkte, null unterstützende Studien oder Literatur und keine plausible mechanistische Begründung angesichts der bekannten Pharmakologie des Arzneimittels. Im Gegensatz dazu ist der Kandidat mit Rang #10 — **therapieresistente Schizophrenie** — mechanistisch kohärent (er liegt innerhalb der bekannten therapeutischen Klasse von Paliperidon) und ist der einzige Kandidat in diesem Paket, der durch echte klinische Studien- und Literaturbelege gestützt wird (siehe Fazit).

---

## Klinische Studienevidenz

Derzeit keine registrierten verwandten klinischen Studien.

---

## Literaturbelege

| PMID | Jahr | Typ | Zeitschrift | Wichtige Erkenntnisse |
|------|------|------|-------------|----------------------|
| [9416661](https://pubmed.ncbi.nlm.nih.gov/9416661/) | 1997 | Übersicht/Fall | Semin Ultrasound CT MR | Orbitalinfektionen sekundär zur Sinusitis; nicht verwandt mit Paliperidon oder Netzhautdystrophie-Pathophysiologie |
| [20127583](https://pubmed.ncbi.nlm.nih.gov/20127583/) | 2010 | Übersicht | Semin Neurol | Diagnostischer Zugang zu Diplopie; unverwandt mit Arzneimittelmechanismus |
| [38321238](https://pubmed.ncbi.nlm.nih.gov/38321238/) | 2024 | Übersicht | Pediatr Radiol | Bildgebung pädiatrischer angeborener okularer Pathologien; keine Arzneimittelbedeutung |
| [38249493](https://pubmed.ncbi.nlm.nih.gov/38249493/) | 2023 | Übersicht | Taiwan J Ophthalmol | Angeborene Linsenform-Anomalien; keine Arzneimittelbedeutung |
| [22241537](https://pubmed.ncbi.nlm.nih.gov/22241537/) | 2012 | Übersicht | Klin Monbl Augenheilkd | Pathophysiologie der angeborenen Ptose; keine Arzneimittelbedeutung |
| [109006](https://pubmed.ncbi.nlm.nih.gov/109006/) | 1979 | Fallbericht | Am J Ophthalmol | Fallserie unilaterale Kryptophthalmie; keine Arzneimittelbedeutung |
| [7035111](https://pubmed.ncbi.nlm.nih.gov/7035111/) | 1981 | Übersicht | Doc Ophthalmol | Wagner-Stickler-Syndrom vitreoretinale Degeneration; keine Arzneimittelbedeutung |
| [33806565](https://pubmed.ncbi.nlm.nih.gov/33806565/) | 2021 | Kohorte | Int J Mol Sci | Optikusnerv-/Netzhautbefunde bei angeborenem Fibrose der extraokulären Muskeln; keine Arzneimittelbedeutung |
| [30196776](https://pubmed.ncbi.nlm.nih.gov/30196776/) | 2018 | Übersicht | J Binocul Vis Ocul Motil | Übersicht angeborener Hirnnervenstörungen; keine Arzneimittelbedeutung |
| [24932988](https://pubmed.ncbi.nlm.nih.gov/24932988/) | 2014 | Übersicht | Am J Ophthalmol | Maculopathie aus kavitären Sehnervenscheiben-Anomalien; keine Arzneimittelbedeutung |

Keine der abgerufenen Literatur erwähnt Paliperidon, Antipsychotika oder dopaminerge/serotoninerge Mechanismen — was bestätigt, dass dies thematische Co-Abruf-Übereinstimmungen sind statt mechanistischer Belege.

---

## Marktinformation Deutschland

Paliperidon ist **in Deutschland nicht zugelassen**; keine BfArM-Zulassungen sind in diesem Evidenzpaket dokumentiert.

---

## Sicherheitsüberlegungen

Bitte beachten Sie die Fachinformation für Sicherheitsinformationen.

**Hinweis:** TFDA/BfArM-Etikettendaten (Warnhinweise, Kontraindikationen) werden als **blockierende** Datenlücke in diesem Evidenzpaket gekennzeichnet (DG001) und konnten nicht abgerufen werden — dies muss behoben werden, bevor eine S1-Sicherheitsprüfung fortschreiten kann, unabhängig davon, welche Indikation verfolgt wird.

---

## Fazit und nächste Schritte

**Entscheidung: Halten**

**Begründung:**
Der Top-Kandidat (Netzhautdystrophie mit oder ohne extraokulären Anomalien) hat keine klinischen Studien, keine relevante Literatur und keine plausible mechanistische Verbindung zu Paliperidon D2/5-HT2A-Antagonismus — das Evidenzpaket selbst identifiziert es als wahrscheinlich Falsch-Positiv aus Embedding-Ähnlichkeit. Das gleiche gilt für Kandidaten mit Rang #2–#9.

**Um fortzufahren, ist Folgendes erforderlich:**
- Beheben Sie die blockierende Datenlücke: Beschaffen Sie sich TFDA/BfArM-Etikett (Warnhinweise, Kontraindikationen) vor jeder Sicherheitsprüfung
- Erhalten Sie bestätigte MOA- und ursprüngliche Indikationsdokumentation für Paliperidon (derzeit als Datenlücken gekennzeichnet)
- Falls eine Umwidmungsarbeit an diesem Arzneimittel verfolgt wird, leiten Sie die Bewertung zum **Kandidaten mit Rang #10 (therapieresistente Schizophrenie)** um, der der einzige Kandidat mit echten unterstützenden Belegen ist (L2, 4 klinische Studien einschließlich einer abgeschlossenen Phase-4-Studie, 2 Literaturübersichten) — beachten Sie, dass dies eine Indikationserweiterung innerhalb der bestehenden therapeutischen Klasse von Paliperidon darstellt und nicht ein neuartiges Umwidmungssignal, und würde trotzdem Kopf-an-Kopf-Vergleichsdaten gegen Clozapin (der aktuelle Standard für therapieresistente Schizophrenie) erfordern, bevor es über S2 hinaus fortschreitet

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

