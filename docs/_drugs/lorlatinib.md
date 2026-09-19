---
layout: default
title: Lorlatinib
parent: Nur Modellvorhersage (L5)
nav_order: 239
evidence_level: L5
indication_count: 10
---

# Lorlatinib
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

# Lorlatinib: Von ALK-positiven nicht-kleinzelligen Lungenkarzinomen zur gingivalen Fibromatose

## Zusammenfassung in einem Satz

Lorlatinib ist ein ALK/ROS1-Tyrosinkinase-Inhibitor der dritten Generation, der klinisch für ALK-positive metastatische nicht-kleinzellige Lungenkarzinome (NSCLC) etabliert ist (dieses Evidence Pack dokumentiert jedoch weder die ursprüngliche Indikation noch den Wirkmechanismus – siehe Anmerkung unten). Die Top-Vorhersage des TxGNN-Modells für diesen Kandidaten ist **gingivale Fibromatose**, diese Vorhersage wird jedoch durch **null klinische Studien** und **null Publikationen** gestützt – es handelt sich um ein reines algorithmisches Signal ohne unterstützende Evidenz.

---

## Schnellübersicht

| Item | Inhalt |
|------|--------|
| Ursprüngliche Indikation | Nicht dokumentiert in diesem Evidence Pack (0 Lizenzen vorhanden; `original_moa` und `original_indications` sind beide Datenlücken). Klinisch ist lorlatinib als ALK/ROS1-TKI für ALK-positive NSCLC zugelassen, aber dies ist externes Wissen, nicht aus diesem Pack bezogen. |
| Prognostizierte neue Indikation | Gingivale Fibromatose |
| TxGNN-Vorhersage-Score | 99.81% (Rang 2729 unter allen Vorhersagen) |
| Evidence Level | L5 (nur Modellvorhersage – keine Studien, keine Literatur) |
| Status auf dem deutschen Markt | Nicht vermarktet |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | **Hold** |

---

## Warum ist diese Vorhersage vernünftig?

Derzeit sind detaillierte Wirkmechanismus-Daten in diesem Evidence Pack nicht verfügbar. Basierend auf bekannten Informationen ist lorlatinib ein ALK/ROS1-Tyrosinkinase-Inhibitor, dessen Wirksamkeit bei ALK-umgelagertem NSCLC gut etabliert ist (z. B. die Phase-3-CROWN-Studie), aber dieses Pack enthält keine Daten, die diesen Mechanismus mit der Biologie des gingivalen Gewebes verknüpfen.

Gingivale Fibromatose ist typischerweise eine autosomal-dominante hereditäre Erkrankung oder eine arzneimittelinduzierte gingivale Wucherung (klassischerweise assoziiert mit Calcineurin-Inhibitoren wie Ciclosporin oder Wirkstoffen wie Phenytoin) – es ist nicht bekannt, dass sie ALK oder ROS1-Signalgebung involviert. Die Begründung des Evidence Packs selbst für diese Vorhersage erklärt explizit, dass es **keine bekannte mechanistische Verbindung** gibt und charakterisiert dies als wahrscheinliches **TxGNN-Vorhersage-Rauschen**, d. h. ein Artefakt des Embedding-/Ähnlichkeitsmodells statt eines echten biologischen Signals.

**Breitere Datenqualitäts-Vorbehalte:** Bei Betrachtung aller 10 TxGNN-bewerteten Vorhersagen in diesem Pack stellt keine ein glaubwürdiges Repurposing-Signal dar. Sechs von zehn (Ränge 1, 2, 3, 7, 8, 9) haben null unterstützende Evidenz. Die restlichen vier (Ränge 4, 5, 6, 10) enthalten umfangreiche Literatur – aber bei Überprüfung ist diese Literatur fast ausschließlich über lorlatinib's **bereits zugelassene maligne NSCLC-Indikation** (z. B. CROWN Phase-3-RCT-Daten zu „benigner Lungenneoplasie"), **ALK-getriebenes Neuroblastom** (an „Lungenkeimzelltumor" angehängt) oder **lorlatinib's bekanntes Nebenwirkungsprofil** (Hyperlipidämie, ARDS, Metabolisches Syndrom – an ein unabhängiges seltenes genetisches Syndrom angehängt). Diese scheinen Krankheitsontologie-Zuordnungsfehler in der zugrunde liegenden Datenbank zu sein, nicht echte Repurposing-Signale. Dies sollte korrigiert werden, bevor der Datensatz für weitere Bewertungen oder Berichte verwendet wird.

---

## Klinische Studienevidenz

Derzeit sind keine verwandten klinischen Studien registriert.

---

## Literaturevidenz

Derzeit ist keine verwandte Literatur verfügbar.

---

## Informationen zum deutschen Markt

Lorlatinib hat derzeit keine Marktgenehmigung in Deutschland auf Datei (0 Lizenzen; Marktstatus: nicht vermarktet). Keine Produkt-/Darreichungsform-Daten sind in diesem Evidence Pack verfügbar.

---

## Zytotoxizität

Lorlatinib ist ein antineoplastisches Mittel (ALK/ROS1-Tyrosinkinase-Inhibitor der dritten Generation), basierend auf der Wirkstoffklasse, die in der an anderer Stelle in diesem Pack angegebenen Literaturevidenz beschrieben ist (z. B. CROWN-Studienreferenzen). Es ist kein konventionelles zytotoxisches Chemotherapeutikum.

| Item | Inhalt |
|------|--------|
| Zytotoxizitäts-Klassifizierung | Zielgerichtete Therapie (ALK/ROS1-TKI) |
| Myelosuppressionsrisiko | Niedrig – TKIs dieser Klasse sind nicht typischerweise mit signifikanter Myelosuppression assoziiert; keine spezifischen hämatologischen Toxizitätsdaten in diesem Pack vorhanden |
| Emetogenitäts-Klassifizierung | Niedrig (typisch für oral verabreichte Small-Molecule-TKIs) |
| Überwachungsaspekte | Lipidpanel (in der mit diesem Medikament assoziierten Literatur berichtete Hypercholesterinämie/Hypertriglyzeridämie), Leberfunktion, Gewicht/Metabolische Parameter, Stimmung/ZNS-Effekte |
| Handhabungsvorsichtsmaßnahmen | Standard-Handhabungsvorsichtsmaßnahmen für orale Antineoplastica; bitte beachten Sie die institutionellen Richtlinien und die offizielle Fachinformation für spezifische Anforderungen |

---

## Sicherheitsüberlegungen

Formale Sicherheitsfelder (`key_warnings`, `contraindications`, `ddi`) sind Datenlücken in diesem Evidence Pack. Jedoch enthält Literatur, die anderswo an andere (nicht übereinstimmende) prognostizierte Indikationen in diesem Pack angehängt ist, echte lorlatinib-Sicherheitssignale, die Aufmerksamkeit verdienen, vorbehaltlich der Bestätigung durch das offizielle Label:

- Berichte über lorlatinib-assoziierte Hyperlipidämie/Dyslipidämie und Metabolisches Syndrom (PMIDs [40287137](https://pubmed.ncbi.nlm.nih.gov/40287137/), [40157899](https://pubmed.ncbi.nlm.nih.gov/40157899/), [39537504](https://pubmed.ncbi.nlm.nih.gov/39537504/), [33789526](https://pubmed.ncbi.nlm.nih.gov/33789526/))
- Ein Fallbericht von lorlatinib-assoziiertem ARDS (PMID [31985497](https://pubmed.ncbi.nlm.nih.gov/31985497/))
- Ein pragmatischer Leitfaden zur Nebenwirkungsverwaltung für lorlatinib (PMID [38554546](https://pubmed.ncbi.nlm.nih.gov/38554546/))

Diese Befunde beziehen sich auf lorlatinib's bekanntes Sicherheitsprofil in seiner zugelassenen onkologischen Verwendung, nicht auf gingivale Fibromatose speziell, und reichen nicht aus, um die prognostizierte Indikation in diesem Bericht zu unterstützen.

---

## Fazit und nächste Schritte

**Entscheidung: Hold**

**Begründung:**
Die Top-Vorhersage (gingivale Fibromatose) hat keine klinische Studien- oder Literaturunterstützung und keine plausible mechanistische Begründung – das Pack selbst kennzeichnet es als wahrscheinliches Modellrauschen. Keine andere Vorhersage in diesem Pack stellt ein echtes, evidenzgestütztes Repurposing-Signal dar, sobald die ontologie-mismatch-Einträge ausgeschlossen sind.

**Um fortzufahren, ist Folgendes erforderlich:**
- Beheben Sie die zwei Blocking/High-Datenlücken (TFDA/BfArM-Label-Warnungen & Kontraindikationen; bestätigte ursprüngliche MOA/Indikation)
- Korrigieren Sie die Krankheitsontologie-Zuordnung für die Ränge 4, 5, 6 und 10, die derzeit bestehende ALK+ NSCLC-, Neuroblastom- und Medikamentensicherheitsliteratur zu unabhängigen Kandidaten-Erkrankungen miszuordnen
- Führen Sie die TxGNN-Bewertung/Evidenzabruf nach Ontologie-Korrektur erneut aus, bevor Sie diesen Kandidaten für weitere Staging-Phasen in Betracht ziehen

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

