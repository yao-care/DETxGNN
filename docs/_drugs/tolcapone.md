---
layout: default
title: Tolcapone
parent: Nur Modellvorhersage (L5)
nav_order: 403
evidence_level: L5
indication_count: 10
---

# Tolcapone
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

# Tolcapone: Von der Parkinson-Krankheit (COMT-Hemmung) zur Rasmussen-Subakuten-Enzephalitis

## Zusammenfassung in einem Satz

Tolcapone ist ein COMT-(Catechol-O-Methyltransferase-)Hemmer; nach Angaben der Begründungsnotizen des Evidenzpakets bezieht sich seine etablierte Pharmakologie auf den Katecholamin-Stoffwechsel bei der Parkinson-Krankheit als Zusatztherapie zu Levodopa (kein formaler Taiwan-/Deutschland-Regulierungseintrag ist in diesem Datensatz verfügbar).
Die Top-Vorhersage des TxGNN-Modells ist **Rasmussen-Subakute-Enzephalitis**, aber dies ist eine reine modellgesteuerte Assoziation mit **0 klinischen Studien** und **0 Publikationen**, und das Evidenzpaket erklärt ausdrücklich, dass es keine bekannte mechanistische Überschneidung zwischen der COMT-Hemmung und der T-Zellen-vermittelten neuronalen Schädigung dieser Krankheit gibt.
Die Evidenzstärke für diese spezifische Vorhersage ist minimal (L5) und unterstützt derzeit keine weitere Entwicklung.

---

## Schnellübersicht

| Element | Inhalt |
|------|------|
| Ursprüngliche Indikation | Nicht im Taiwan-/Deutschland-Regulierungsdatensatz angegeben (nach den Begründungsnotizen des Evidenzpakets ist Tolcapone ein COMT-Hemmer, der klassischerweise als Zusatztherapie bei der Parkinson-Krankheit verwendet wird) |
| Vorhergesagte neue Indikation | Rasmussen-Subakute-Enzephalitis |
| TxGNN-Vorhersage-Score | 99.93% |
| Evidenzgrad | L5 |
| Marktatus in Deutschland | Nicht auf dem Markt |
| Anzahl der Genehmigungen | 0 |
| Empfohlene Entscheidung | Zurückstellung |

---

## Warum ist diese Vorhersage sinnvoll?

Detaillierte Daten zum Wirkmechanismus werden in diesem Evidenzpaket als Datenlücke (DG002) gekennzeichnet. Basierend auf den mechanistischen Anmerkungen, die den Vorhersagen beigefügt sind, wirkt Tolcapone als COMT-Hemmer und verändert den Katecholamin-(Dopamin-)Stoffwechsel – ein Mechanismus, dessen etablierte klinische Relevanz in dopaminergen Störungen wie der Parkinson-Krankheit liegt.

Rasmussen-Subakute-Enzephalitis ist dagegen ein Autoimmun-Epilepsie-Syndrom, dessen Kernpathologie die T-Zellen-vermittelte neuronale Zerstörung ist. Das Repurposing-Rationale des Evidenzpakets besagt, dass es **keine bekannte Schnittstelle** zwischen dem Dopamin-/Katecholamin-Stoffwechselweg und dem immunologischen Mechanismus dieser Krankheit gibt, und charakterisiert diese am höchsten bewertete Vorhersage als „datengesteuerte Assoziation eher als biologische Hypothese".

Es ist bemerkenswert, dass niedriger bewertete Vorhersagen in demselben Evidenzpaket eine vergleichsweise stärkere (wenn auch immer noch begrenzte) mechanistische Plausibilität zeigen – zum Beispiel ist Lewy-Körper-Demenz (Rang 6, L4) über DOPAL/α-synuklein-Biochemie verbunden, und Juvenile Parkinsonismus (Rang 10, L4) ist über Tolcapones etablierte dopaminerge Pharmakologie verbunden. Diese könnten separate Bewertungen verdienen, aber gemäß dem Berichtsfokus hat der am höchsten bewertete Kandidat (Rasmussen-Subakute-Enzephalitis) derzeit keine vertretbare mechanistische Begründung.

---

## Belege aus klinischen Studien

Derzeit keine verwandten klinischen Studien registriert

---

## Literaturbelege

Derzeit keine verwandte Literatur verfügbar

---

## Marktinformationen Deutschland

Keine deutschen Marktgenehmigungen in diesem Evidenzpaket gefunden (total_licenses = 0; market_status = Nicht vermarktet).

---

## Sicherheitsaspekte

Bitte beachten Sie die Packungsbeilage für Sicherheitsinformationen.

*(Anmerkung: Die TFDA/BfArM-Kennzeichnungswarnungen und Kontraindikationen werden in diesem Evidenzpaket als blockierende Datenlücke (DG001) gekennzeichnet – Sicherheitsdaten konnten für diesen Kandidaten nicht überprüft werden.)*

---

## Fazit und nächste Schritte

**Entscheidung: Zurückstellung**

**Begründung:**
Die Top-Vorhersage (Rasmussen-Subakute-Enzephalitis) hat keine unterstützenden klinischen Studien, keine Literatur und eine ausdrücklich angegebene Abwesenheit mechanistischer Plausibilität im Evidenzpaket selbst – dies ist eine reine Modell-Score-Assoziation (L5) und erfüllt die Mindestanforderungen für eine weitere Bewertung nicht.

**Um fortzufahren, ist folgendes erforderlich:**
- DG001 (Blockierung) auflösen: TFDA/BfArM-Kennzeichnungswarnungen und Kontraindikationen beschaffen, bevor eine Sicherheitsbewertung beginnen kann
- DG002 (Hoch) auflösen: Bestätigte Wirkmechanismus-Daten des Arzneimittels aus DrugBank beschaffen, um die mechanistische Verbindung richtig bewerten zu können
- Bestätigung der ursprünglichen Indikation und des Regulierungsverlaufs für Tolcapone (derzeit in diesem Evidenzpaket nicht vorhanden)
- Bei Verfolgung von Repurposing-Signalen aus diesem Datensatz sollte der Bewertungsscope auf die höher plausiblen Kandidaten des Pakets (Lewy-Körper-Demenz, Juvenile Parkinsonismus) verlagert werden, anstatt den höchst bewerteten, aber mechanistisch nicht unterstützten TxGNN-Kandidaten zu verfolgen

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

