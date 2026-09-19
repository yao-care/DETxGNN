---
layout: default
title: Susoctocog Alfa
parent: Nur Modellvorhersage (L5)
nav_order: 374
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

# Susoctocog alfa: Von erworbener Hämophilie A zur primären Sekretionsstörung der Blutplättchen

## Zusammenfassung in einem Satz

> Susoctocog alfa (rekombinantes B-Domänen-deletiertes porcines Faktor-VIII, an anderer Stelle unter dem Markennamen Obizur® vermarktet) wird zur Blutungskontrolle bei **erworbener Hämophilie A** verwendet – ein Fakt, der durch das Literaturpaket selbst bestätigt wird, obwohl das Feld `original_indications` leer ist (Datenlücke).
> TxGNNs am höchsten bewertete Vorhersage, **primäre Sekretionsstörung der Blutplättchen**, wird durch **null unterstützende klinische Studien oder Publikationen** gestützt, und die eigene mechanistische Begründung des Modells kennzeichnet sie als biologisch implausibel.
> Die einzigen Vorhersagen in diesem Paket, die echte klinische Evidenz tragen (Hämophilie; erworbener Gerinnungsfaktor-Mangel), überschneiden sich weitgehend mit der bekannten ursprünglichen Verwendung des Arzneimittels, statt eine echte neuartige Indikation darzustellen.

---

## Schnellübersicht

| Element | Inhalt |
|---------|--------|
| Ursprüngliche Indikation | Erworbene Hämophilie A (aus der zitierten Literatur abgeleitet, z. B. PMID 27098420; das Feld `original_indications` selbst ist leer – Datenlücke) |
| Vorhergesagte neue Indikation (TxGNN Rang #1) | Primäre Sekretionsstörung der Blutplättchen |
| TxGNN-Vorhersage-Score | 99.94% |
| Evidenzstufe | L5 (nur Modellvorhersage, keine unterstützenden Studien) |
| Marktstellung | Nicht vermarktet |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | **Halten** |

---

## Warum ist diese Vorhersage sinnvoll?

Detaillierte Wirkungsmechanismus-Daten sind nicht verfügbar (`original_moa: [Data Gap]`). Basierend auf der Wirkstoffklasse und der Literatur im Evidenzpaket ist susoctocog alfa ein rekombinantes porcines Faktor-VIII-Produkt, das die Thrombingeneration durch direkte Ersetzung der FVIII-Aktivität wiederherstellt – klinisch verwendet zur Blutungskontrolle bei Patienten mit erworbener Hämophilie A (Autoantikörper-vermittelter FVIII-Inhibition).

TxGNNs am höchsten bewertete Vorhersage, **primäre Sekretionsstörung der Blutplättchen**, ist ein Defekt in der Blutplättchen-Granula-Sekretion, ein Mechanismus, der vollständig oberhalb und unabhängig von der Gerinnungsfaktor-Kaskade liegt, auf die susoctocog alfa wirkt. Die `repurposing_rationale` des Evidenzpakets selbst macht dies deutlich: die mechanistische Verbindung ist schwach, und der hohe Score wird wahrscheinlich durch einen „Blutungsneigung"-Semantik-Cluster im TxGNN-Wissensgraph angetrieben, anstatt durch echte biologische Relevanz. Dasselbe Muster gilt für die Ränge 2, 3, 6, 7, 8, 9 und 10 (Pseudo-von-Willebrand-Krankheit, Glanzmann-Thrombasthenie, Scott-Syndrom, Blutungsneigung bei Kollagen-Rezeptor-Defekt, konstitutionelle Thrombozytopenie, kongenitaler Faktor-XIII-Mangel und Adenosindesaminase-Mangel) – alle sind Blutplättchen-Funktions-, andere Gerinnungsfaktor- oder völlig unabhängige (Immundefekt-)Störungen, die durch FVIII-Ersatz nicht mechanistisch korrigiert werden können, und keine davon hat irgendwelche Unterstützung durch klinische Studien oder Literatur.

Die einzigen Kandidaten mit echtem mechanistischem Zusammenhang und realen Evidenzen sind **Hämophilie** (Rang 4) und **erworbener Gerinnungsfaktor-Mangel** (Rang 5) – aber beide sind im Wesentlichen Umformulierungen der bekannten zugelassenen Verwendung des Arzneimittels für erworbene Hämophilie A, keine neuartigen Umwidmungschancen. Dies deutet darauf hin, dass das `original_indications`-Feld des Evidenzpakets diese Indikation hätte erfassen sollen, und seine Leere ist ein Datenvollständigkeitsproblem, nicht ein Beweis, dass keine ursprüngliche Indikation existiert.

---

## Klinische Studienevidenz (Rang #1: Primäre Sekretionsstörung der Blutplättchen)

Derzeit keine verwandten klinischen Studien registriert.

## Literaturevidenz (Rang #1: Primäre Sekretionsstörung der Blutplättchen)

Derzeit keine verwandte Literatur verfügbar.

---

## Zusätzlich: Vollständiger TxGNN-Ranking-Überblick

Da dieses Evidenzpaket mehrere Kandidaten-Indikationen bewertet, wird das vollständige Ranking nachfolgend zur Transparenz zusammengefasst:

| Rang | Vorhergesagte Indikation | Score | Evidenzstufe | Empfehlung | Anmerkung |
|------|--------------------------|-------|--------------|------------|----------|
| 1 | Primäre Sekretionsstörung der Blutplättchen | 99.94% | L5 | Halten | Keine Evidenz; mechanistisch schwach |
| 2 | Pseudo-von-Willebrand-Krankheit | 99.93% | L5 | Halten | Keine Evidenz; mechanistisch schwach |
| 3 | Glanzmann-Thrombasthenie | 99.88% | L5 | Halten | Keine Evidenz; mechanistisch schwach |
| 4 | Hämophilie | 99.74% | L3 | Fortfahren mit Schutzmaßnahmen | 1 PMS-Studie + 21 Publikationen, aber überlappt mit bekannter ursprünglicher Indikation |
| 5 | Erworbener Gerinnungsfaktor-Mangel | 99.64% | L3 | Fortfahren mit Schutzmaßnahmen | Mehrere Real-World/Kohort-Studien, gleiche Überlapps-Einschränkung |
| 6 | Scott-Syndrom | 99.60% | L5 | Halten | Keine Evidenz; mechanistisch schwach |
| 7 | Blutungsneigung (Kollagen-Rezeptor-Defekt) | 99.17% | L5 | Halten | Keine Evidenz; mechanistisch schwach |
| 8 | Blutungsstörung (konstitutionelle Thrombozytopenie) | 99.17% | L5 | Halten | Keine Evidenz; mechanistisch schwach |
| 9 | Kongenitaler Faktor-XIII-Mangel | 99.15% | L5 | Halten | Keine Evidenz; anderer Schritt der Gerinnungskaskade |
| 10 | Adenosindesaminase-Mangel | 99.04% | L5 | Halten | Wahrscheinlich spurios; keine biologische Relevanz zur Gerinnung |

### Am besten gestützter Kandidat: Hämophilie (Rang 4)

| Studiennummer | Phase | Status | Einschluss | Wichtigste Erkenntnisse |
|---------|------|------|------|---------|
| [NCT06461533](https://clinicaltrials.gov/study/NCT06461533) | N/A | In Rekrutierung | 25 | Japanische Post-Marketing-All-Case-Überwachung von IV susoctocog alfa bei Blutungsereignissen der erworbenen Hämophilie A; Erfassung von Beobachtungsdaten zur Sicherheit/Wirksamkeit |

| PMID | Jahr | Typ | Journal | Wichtigste Erkenntnisse |
|------|-----|------|------|---------|
| [39158833](https://pubmed.ncbi.nlm.nih.gov/39158833/) | 2024 | Phase II/III offen | Int J Hematol | Wirksamkeit/Sicherheit von rpFVIII bei japanischen AHA-Patienten (NCT04580407) |
| [37510704](https://pubmed.ncbi.nlm.nih.gov/37510704/) | 2023 | Fallserie/Review | J Clin Med | Chirurgische Prophylaxe mit susoctocog-alfa bei AHA |
| [40812597](https://pubmed.ncbi.nlm.nih.gov/40812597/) | 2025 | PK-Studie | J Thromb Haemost | PK-gesteuerte Dosierungsstrategien für präzise FVIII-Kontrolle |
| [32698943](https://pubmed.ncbi.nlm.nih.gov/32698943/) | 2020 | Real-World-Register | Blood Transfus | 9 ältere AHA-Patienten, italienische multizentrische Real-World-Erfahrung |
| [27098420](https://pubmed.ncbi.nlm.nih.gov/27098420/) | 2016 | Review | Drugs | Umfassender Review, ursprüngliche Pivot-Phase-II/III-Studie (n=28) zur Unterstützung der Zulassung |

---

## Marktinformation

Nicht vermarktet; keine Zulassungen in der Datenbank (`total_licenses: 0`, `licenses: []`).

---

## Sicherheitsüberlegungen

Bitte beachten Sie die Packungsbeilage für Sicherheitsinformationen.

> Hinweis: Daten zu TFDA/Etikett-Warnungen und Kontraindikationen werden in diesem Evidenzpaket als **blockierende** Datenlücke (DG001) gekennzeichnet – dies allein verhindert eine vollständige Sicherheitsbewertung (S1) unabhängig von der Evidenzbewertung der Wirksamkeit.

---

## Fazit und nächste Schritte

**Entscheidung: Halten**

**Begründung:**
Die am höchsten bewertete TxGNN-Vorhersage (primäre Sekretionsstörung der Blutplättchen) hat keine klinischen Studien- oder Literaturbelege und wird durch die eigene Begründung des Modells als wahrscheinliches Wissensgraph-Artefakt gekennzeichnet. Die einzigen mechanistisch sinnvollen, evidenzgestützten Kandidaten (Hämophilie, erworbener Gerinnungsfaktor-Mangel) sind nicht wirklich neuartig – sie überschneiden sich mit der bekannten ursprünglichen Indikation des Arzneimittels – daher unterstützt dieses Paket derzeit keine neue Umwidmungschance. Eine blockierende Sicherheitsdatenlücke (Etikett-Warnungen/Kontraindikationen) verhindert darüber hinaus das Voranschreiten.

**Um fortfahren zu können, wird Folgendes benötigt:**
- Datenlücke DG001 beheben: TFDA/EMA-Etikett-Warnungen, Kontraindikationen und Arzneimittelwechselwirkungsdaten vor jeder Sicherheitsbewertung abrufen
- Datenlücke DG002 beheben: bestätigte Wirkmechanismus-Daten von DrugBank abrufen
- Das Feld `original_indications` korrigieren, um die tatsächliche zugelassene Verwendung des Arzneimittels (erworbene Hämophilie A) widerzuspiegeln, damit zukünftige TxGNN-Vorhersagen ordnungsgemäß gegen bekannte Indikationen gefiltert werden
- Wenn eine wirklich neuartige Indikation gewünscht ist, Vorhersage erneut durchführen, wobei Hämophilie-nahe Krankheits-Cluster ausgeschlossen werden, und ≥L3-Evidenz erforderlich machen, bevor mit der Schutzmaßnahmen-Überprüfung fortgefahren wird

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

