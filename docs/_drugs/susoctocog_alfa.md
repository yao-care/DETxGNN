---
layout: default
title: Susoctocog Alfa
parent: Nur Modellvorhersage (L5)
nav_order: 439
evidence_level: L5
indication_count: 10
---

# Susoctocog Alfa
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

# Susoctocog alfa: Von Hämophilie A zu Hämophilie (erworbene Hämophilie A)

## Zusammenfassung in einem Satz

Susoctocog alfa ist ein rekombinanter Faktor VIII mit Schweine-Sequenz (B-Domäne deletiert) und wurde ursprünglich zur Behandlung der **Hämophilie A** zugelassen.
Das TxGNN-Modell sagt als bestplatzierte klinisch gestützte Indikation **Hämophilie** voraus (insbesondere die erworbene Hämophilie A). Dafür liegen **1 klinische Studie** und **19 Publikationen** vor, überwiegend Fallberichte, Reviews und Real-World-Daten.

---

## Schnellübersicht

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Hämophilie A |
| Vorhergesagte neue Indikation | Primäre Thrombozyten-Freisetzungsstörung (Rang 1 des Modells, ohne Evidenz); klinisch gestützt ist Rang 4: Hämophilie (erworbene Hämophilie A) |
| TxGNN-Vorhersagewert | 99,94 % (Rang 1); 99,74 % (Hämophilie, Rang 4) |
| Evidenzniveau | L5 (Rang 1); L3 (Hämophilie, Rang 4) |
| Marktstatus in Deutschland | Nur erloschene Zulassung |
| Anzahl der Zulassungen | 1 |
| Empfohlene Entscheidung | Proceed with Guardrails (für Hämophilie / erworbene Hämophilie A); Hold für alle übrigen Vorhersagen |

Hinweis: Die höchstbewertete Vorhersage (primäre Thrombozyten-Freisetzungsstörung) hat keinerlei Studien- oder Literaturgrundlage und ist mechanistisch nicht plausibel. Dieser Bericht konzentriert sich daher auf die Indikation **Hämophilie** (Rang 4), die als einzige substanziell belegt ist.

---

## Warum ist diese Vorhersage plausibel?

Zum Wirkmechanismus liegen in den für diesen Bericht zusammengestellten Daten keine detaillierten Angaben vor. Bekannt ist: Susoctocog alfa ist ein rekombinanter Faktor VIII mit Schweine-Sequenz und deletierter B-Domäne. Er ersetzt den fehlenden Faktor VIII und kann mechanistisch auch bei Hämophilie-Formen angewendet werden, bei denen neutralisierende Antikörper gegen humanen FVIII vorliegen.

Bei der erworbenen Hämophilie A bilden Autoantikörper (Inhibitoren) gegen humanen Faktor VIII. Das Schweine-Protein wird von diesen Antikörpern nur eingeschränkt gebunden (geringe Kreuzreaktivität) und kann daher funktionelle FVIII-Aktivität liefern. Das ist die zentrale mechanistische Begründung für die Erweiterung von der angeborenen auf die erworbene Form. Ergänzend zeigen Laborbefunde, dass Schweine-FVIII die Thrombinbildung in Plasma von Patienten mit angeborener Hämophilie A und Inhibitoren korrigiert.

Die übrigen neun vorhergesagten Indikationen (z. B. Glanzmann-Thrombasthenie, Pseudo-von-Willebrand-Erkrankung, Scott-Syndrom, Faktor-XIII-Mangel) betreffen Thrombozytenfunktionsstörungen oder andere Defekte, die durch FVIII-Ersatz nicht korrigiert werden. Die hohen Scores sind vermutlich Netzwerkeffekte ohne biologische Grundlage.

---

## Klinische Studien

| Studiennummer | Phase | Status | Teilnehmerzahl | Zentrale Ergebnisse |
|---------|------|------|------|---------|
| [NCT06461533](https://clinicaltrials.gov/study/NCT06461533) | N/A | Rekrutierend | 25 | Japanische Anwendungsbeobachtung (alle Fälle) zu Obizur bei Blutungsereignissen der erworbenen Hämophilie A; erfasst Nebenwirkungen und Wirksamkeit. Beobachtungsstudie ohne Kontrollarm. |

Hinweis: Die Literatur nennt zudem die japanische Phase-II/III-Studie NCT04580407, die in den hinterlegten Studiendaten nicht als eigener Eintrag geführt wird.

---

## Literaturevidenz

| PMID | Jahr | Typ | Journal | Zentrale Ergebnisse |
|------|-----|------|------|---------|
| [39158833](https://pubmed.ncbi.nlm.nih.gov/39158833/) | 2024 | Offene Phase-II/III-Studie | Int J Hematol | Wirksamkeit und Sicherheit von rpFVIII bei japanischen Erwachsenen mit erworbener Hämophilie A und schweren Blutungen (Startdosis 200 E/kg) |
| [38317504](https://pubmed.ncbi.nlm.nih.gov/38317504/) | 2024 | Phase-3-Studie, einarmig | Haemophilia | rpFVIII bei angeborener Hämophilie A mit Inhibitoren bei Operationen |
| [37584309](https://pubmed.ncbi.nlm.nih.gov/37584309/) | 2023 | Real-World-Kohorte | Haemophilia | Nicht-interventionelle Sicherheitsstudie nach Zulassung zu Sicherheit und Wirksamkeit bei erworbener Hämophilie A |
| [32698943](https://pubmed.ncbi.nlm.nih.gov/32698943/) | 2020 | Kohorte | Blood Transfus | Italienische Multizenter-Erfahrung bei neun älteren Patienten mit erworbener Hämophilie A |
| [27098420](https://pubmed.ncbi.nlm.nih.gov/27098420/) | 2016 | Review | Drugs | Übersicht zu Susoctocog alfa; wirksam und gut verträglich in der multinationalen Phase-II/III-Studie (n = 28 auswertbar) |
| [37510704](https://pubmed.ncbi.nlm.nih.gov/37510704/) | 2023 | Fallserie/Review | J Clin Med | Operationen und Prophylaxe mit Susoctocog alfa bei erworbener Hämophilie |
| [40812597](https://pubmed.ncbi.nlm.nih.gov/40812597/) | 2025 | Pharmakokinetikstudie | J Thromb Haemost | Pharmakokinetische Strategien zur präzisen FVIII-Steuerung |
| [35765670](https://pubmed.ncbi.nlm.nih.gov/35765670/) | 2022 | In-vitro-Studie | Res Pract Thromb Haemost | rpFVIII korrigiert die Thrombinbildung in Plasma von Patienten mit angeborener Hämophilie A und Inhibitoren |
| [31448877](https://pubmed.ncbi.nlm.nih.gov/31448877/) | 2020 | Studiendaten | J Thromb Haemost | Kreuzreagierende Inhibitoren gegen rpFVIII bei erworbener Hämophilie A (GTH-AH 01/2010) |
| [41436689](https://pubmed.ncbi.nlm.nih.gov/41436689/) | 2025 | Fallbericht | CEN Case Rep | Erfolgreicher Hämodialysebeginn bei erworbener Hämophilie A unter Susoctocog alfa und Emicizumab |

---

## Marktinformationen Deutschland

| Zulassungsnummer | Produktname | Darreichungsform | Zugelassene Indikation |
|---------|------|------|-----------|
| EMEA/H/C/002792 | Obizur | – | Hämophilie A (Status: erloschen; Zulassungsinhaber Baxalta Innovations GmbH) |

---

## Sicherheitshinweise

Bitte die Packungsbeilage zu Sicherheitsinformationen heranziehen. Für diese Substanz liegen in den zusammengestellten Daten keine Warnhinweise, Gegenanzeigen oder Wechselwirkungsdaten vor. Ein Hinweis aus der Literatur: Kreuzreagierende Inhibitoren gegen Schweine-FVIII können auftreten, und die Überwachung sollte mit dem Einstufentest erfolgen (chromogene Tests können die Aktivität unterschätzen).

---

## Fazit und nächste Schritte

**Entscheidung: Proceed with Guardrails** (für Hämophilie bzw. erworbene Hämophilie A; **Hold** für alle übrigen vorhergesagten Indikationen)

**Begründung:**
- Für die erworbene Hämophilie A gibt es einen klaren mechanistischen Hintergrund und konsistente klinische Daten (Phase-II/III-Studie, Real-World-Daten, Fallserien), jedoch keine randomisierte Phase-3-Studie, daher Evidenzniveau L3. Der Marktstatus „nur erloschene Zulassung" erfordert eine Klärung vor einer Empfehlung.

**Für das weitere Vorgehen erforderlich:**
- Klärung des Zulassungsstatus in Deutschland (erloschene Zulassung) und der aktuellen Verfügbarkeit
- Auswertung der Packungsbeilage (Warnhinweise, Gegenanzeigen), da dieser Sicherheitsdatenpunkt derzeit blockierend fehlt
- Detaillierte Wirkmechanismus-Daten (MOA) aus DrugBank
- Prüfung des Inhibitor-Kreuzreaktivitätsrisikos und Überwachungskonzepts (Einstufentest)
- Die Vorhersagen mit Thrombozytendefekten (Rang 1–3, 6–8) sowie Faktor-XIII-Mangel und Adenosin-Desaminase-Mangel nicht weiterverfolgen, solange keine Evidenz vorliegt
## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

