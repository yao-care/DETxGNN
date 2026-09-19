---
layout: default
title: Benralizumab
parent: Nur Modellvorhersage (L5)
nav_order: 50
evidence_level: L5
indication_count: 5
---

# Benralizumab
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **5** 
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

# Benralizumab: Bewertung von Thrombozytopenie aufgrund von Immunzerstörung als neue Indikation

> Hinweis: Das Evidenzpaket enthält keine Daten zur ursprünglichen zugelassenen Indikation von Benralizumab (`drug.original_indications` ist leer und `taiwan_regulatory.licenses` ist leer). Dieser Bericht nennt daher keine ursprüngliche Indikation, um die Darstellung unverifizierten Informationen zu vermeiden.

## Zusammenfassung in einem Satz

> Die ursprüngliche zugelassene Indikation von Benralizumab ist in diesem Evidenzpaket nicht dokumentiert, und das Arzneimittel hat derzeit keine Marktgenehmigung in dieser Gerichtsbarkeit (0 Lizenzen, nicht vermarktet).
> Das TxGNN-Modell prognostiziert, dass es für **Thrombozytopenie aufgrund von Immunzerstörung** wirksam sein könnte,
> aber diese Vorhersage wird derzeit durch **0 klinische Studien** und **0 Publikationen** unterstützt — es handelt sich um ein rein modellbasiertes Signal (L5) mit einer explizit gekennzeichneten mechanistischen Nichtübereinstimmung.

## Schnellübersicht

| Punkt | Inhalt |
|-------|--------|
| Ursprüngliche Indikation | Im Evidenzpaket nicht verfügbar |
| Vorhergesagte neue Indikation | Thrombozytopenie aufgrund von Immunzerstörung |
| TxGNN-Vorhersage-Score | 99.34% |
| Evidenzstufe | L5 |
| Marktstatus in Deutschland | ✗ Nicht vermarktet |
| Anzahl der Genehmigungen | 0 |
| Empfohlene Entscheidung | Zurückhalten |

## Warum ist diese Vorhersage angemessen?

Derzeit ist kein formales Wirkmechanismus-Datensatz für Benralizumab in diesem Evidenzpaket verfügbar (`original_moa` = Datenlücke). Basierend auf der eigenen Umwidmungslogik des Modells wird Benralizumab als monoklonaler Anti-IL-5Rα-Antikörper beschrieben, der Eosinophile und Basophile primär durch antikörperabhängige zellvermittelte Zytotoxizität (ADCC) abbaut.

Die Immune Thrombozytopenie (ITP) hingegen wird pathologisch durch autoantikörperbedeckte Blutplättchen angetrieben, die durch Fc-Rezeptor-vermittelte Phagozytose beseitigt werden, zusammen mit dysregulierten T- und B-Zell-Antworten. Es gibt keinen etablierten direkten Zusammenhang zwischen der IL-5/Eosinophil-Achse und der Beseitigung von Blutplättchen-Autoantikörpern.

Die mechanistische Bewertung des Evidenzpakets ist zu diesem Punkt eindeutig: Der hohe TxGNN-Score spiegelt wahrscheinlich indirekte Nähe zwischen Benralizumab und ITP durch einen gemeinsamen „Immunmodulation"-Knoten im Wissensgraphen wider, statt einer spezifischen, biologisch validierten Bahn. Mit anderen Worten: Das Modellsignal existiert, aber es gibt derzeit keine mechanistische oder klinische Grundlage, die die IL-5Rα-Blockade mit der ITP-Pathophysiologie verbindet.

## Evidenz aus klinischen Studien

Derzeit sind keine verwandten klinischen Studien registriert.

## Evidenz aus der Literatur

Derzeit ist keine verwandte Literatur verfügbar.

## Informationen zum Marktstatus in Deutschland

Es sind keine Marktgenehmigungen dokumentiert. Der Marktstatus des Arzneimittels wird als **nicht vermarktet** mit **0 Gesamtgenehmigungen** aufgeführt, daher sind keine Produkt-/Darreichungsform-Informationen für diese Gerichtsbarkeit verfügbar.

## Sicherheitsaspekte

Bitte beachten Sie die Packungsbeilage für Sicherheitsinformationen. (Wichtige Warnungen, Gegenanzeigen und Arzneimittelwechselwirkungsdaten sind alle als Datenlücken in diesem Evidenzpaket gekennzeichnet; eine formale Sicherheitsüberprüfung der Kennzeichnung durch die TFDA ist noch nicht abgeschlossen — siehe blockierende Datenlücke DG001 unten.)

## Fazit und nächste Schritte

**Entscheidung: Zurückhalten**

**Begründung:**
Dieser Kandidat befindet sich in der Entscheidungsstufe S0 mit Evidenzstufe L5 — eine Modellvorhersage ohne unterstützende klinische Studien, ohne unterstützende Literatur und ohne vermarktete Darreichungsform in dieser Gerichtsbarkeit. Die mechanistische Analyse des Evidenzpakets deutet ferner darauf hin, dass die Vorhersage wahrscheinlich indirekte Wissensgraph-Nähe widerspiegelt statt einer validierten biologischen Bahn zwischen IL-5Rα-Blockade und ITP.

**Zum Fortschreiten ist Folgendes erforderlich:**
- Sicherheitsdaten aus der Packungsbeilage (Warnungen/Gegenanzeigen) — derzeit eine **blockierende** Lücke (DG001); ohne diese kann der Kandidat nicht zur S1-Sicherheitsvorabeinschätzung fortschreiten
- Verifizierte Wirkmechanismus-Daten über DrugBank — derzeit eine **Hochschwere**-Lücke (DG002), erforderlich für eine ordnungsgemäße Bewertung der mechanistischen Plausibilität
- Präklinische oder fallbasierte Evidenz, die direkt die Eosinophil-/IL-5Rα-Biologie mit der ITP-Pathophysiologie verbindet
- Mindestens Fallberichte oder Beobachtungsdaten, bevor diese Indikation über L5 neu bewertet werden kann

---

**Zusätzliche Anmerkung (Kontext, nicht Teil der primären Nachweiskette):** Unter den anderen TxGNN-vorhergesagten Indikationen für Benralizumab in diesem Evidenzpaket hat **Dermatitis** (Rang 2, Score 99.16%) erheblich mehr Nachweise — 6 klinische Studien und 20 Publikationen mit einer Evidenzstufe L2/Entscheidungsstufe S1. Die Nachweise sind jedoch gesamthaft negativ: Die pivotale Phase-2-Studie HILLIER (NCT04605094) wurde **wegen unzureichender Wirksamkeit beendet**, und eine Begleitpublikation (PMID 37178404, „Fehlende Wirkung von Benralizumab bei Zeichen und Symptomen einer moderaten bis schweren atopischen Dermatitis") bestätigt, dass die Eosinophil-Depletion in Hautläsionen (PMID 40781582) keine klinischen Vorteile gebracht hat. Diese Indikation erhält auch die Bewertung **Zurückhalten**, aber aus einem anderen Grund — Mechanismus bestätigt, Wirksamkeit widerlegt — statt wegen Mangel an Daten. Bei einer breiten Bewertung der Benralizumab-Umwidmung ist dieses Dermatitis-Ergebnis aussagekräftiger als das obige ITP-Signal und kann einen separaten Bericht rechtfertigen.

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

