---
layout: default
title: Empagliflozin
parent: Nur Modellvorhersage (L5)
nav_order: 144
evidence_level: L5
indication_count: 3
---

# Empagliflozin
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **3** 
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

# Empagliflozin: Von Diabetes mellitus Typ 2 zum klassischen Stiff-Person-Syndrom

## Zusammenfassung in einem Satz

Empagliflozin ist ein bekannter SGLT2-Inhibitor (Natrium-Glukose-Kotransporter-2), dessen ursprüngliche Indikation (Diabetes mellitus Typ 2 und verwandte kardiorenale Anwendungen) nicht in diesem Bewertungspaket erfasst ist. Das TxGNN-Modell sagt eine mögliche Wirksamkeit bei **Klassischem Stiff-Person-Syndrom** voraus, aber die Vorhersage wird derzeit durch **0 klinische Studien** und **0 Publikationen** gestützt – dies ist ein reines Modellsignal (Evidenzstufe L5) mit einer Empfehlung „Halten".

---

## Schnellübersicht

| Element | Inhalt |
|---------|--------|
| Ursprüngliche Indikation | Nicht in diesem Bewertungspaket erfasst (Datenlücke — `original_indications` ist leer). Empagliflozin ist öffentlich bekannt als SGLT2-Inhibitor für Diabetes mellitus Typ 2. |
| Vorhergesagte neue Indikation | Klassisches Stiff-Person-Syndrom |
| TxGNN-Vorhersage-Punktzahl | 99.06% |
| Evidenzstufe | L5 (nur Modellvorhersage, keine unterstützenden Studien) |
| Marktstatus in Taiwan | ✗ Nicht auf dem Markt (Not Marketed) |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | Halten |

---

## Warum ist diese Vorhersage angemessen?

Derzeit sind detaillierte Wirkmechanismus-Daten nicht verfügbar (in diesem Bewertungspaket als Datenlücke **DG002** gekennzeichnet, Schweregrad: Hoch). Basierend auf bekannten Informationen wirkt Empagliflozin als SGLT2-Inhibitor und reduziert die renale Glukosereabsorption; seine etablierte Wirkung beschränkt sich auf die renale Glukose-Transportphysiologie und nachgelagerte metabolische/kardiorenale Effekte.

Klassisches Stiff-Person-Syndrom (SPS) ist eine autoimmunologische neurologische Störung, die primär durch Anti-GAD65-Antikörper getrieben wird, die die GABAerge Neurotransmission beeinträchtigen. Es gibt keine etablierte mechanistische Überlappung zwischen SGLT2-Inhibition und GABAerger Signalisierung oder autoimmunologischer Neuro-Modulation. Da `original_moa` eine Datenlücke ist, können wir nicht überprüfen, ob ein indirekter Weg (z. B. metabolisch–neuroimmunologisch) dieser Vorhersage zugrunde liegt.

Zwei Beobachtungen schwächen das Vertrauen in dieses spezifische Signal: (1) Die nahezu identischen TxGNN-Werte zwischen Rang 1 (klassisches Stiff-Person-Syndrom, 99.06%) und Rang 2 (fokal Stiff-Limb-Syndrom, 99.06%) deuten darauf hin, dass das Modell einen ganzen Krankheitscluster bewertet, anstatt ein indikationsspezifisches Signal zu erzeugen; und (2) es gibt keine klinischen Studien, Registereinträge oder Literatur, um die Vorhersage zu unterstützen. Der Wert spiegelt wahrscheinlich die topologische Nähe der Wissensgraph-Knoteneinbettung wider (z. B. topologische Nähe zu anderen neuromuskulären oder metabolisch-komorbiden Knoten) anstelle einer validierten pharmakologischen Begründung.

---

## Evidenz aus klinischen Studien

Derzeit sind keine verwandten klinischen Studien registriert.

---

## Literaturbelege

Derzeit ist keine verwandte Literatur verfügbar.

---

## Marktstatus in Taiwan

Es sind derzeit keine Marktzulassungsdatensätze für Empagliflozin in diesem Bewertungspaket verfügbar (`total_licenses = 0`, Marktstatus: Nicht auf dem Markt / Not Marketed).

---

## Sicherheitsaspekte

Bitte beachten Sie die Packungsbeilage für Sicherheitsinformationen.

Hinweis: Dieses Bewertungspaket kennzeichnet **DG001** (Warnungen/Kontraindikationen der TFDA-Packungsbeilage — Schweregrad: **Blockierend**), was bedeutet, dass wichtige Warnungen, Kontraindikationen und Arzneimittelwechselwirkungsdaten nicht abgerufen werden konnten. Dies blockiert den Fortschritt zur Sicherheits-Vorbewertung S1 und muss vor weiterer Bewertung gelöst werden.

---

## Weitere vorhergesagte Indikationen (Same Evidence Pack)

Zwei weitere TxGNN-Vorhersagen wurden neben dem Hauptkandidaten zurückgegeben. Beide haben dasselbe evidentielle Profil — keine klinischen Studien, keine Literatur, Evidenzstufe L5, Entscheidungsstufe S0, Empfehlung Halten — und werden hier der Vollständigkeit halber vermerkt:

| Rang | Krankheit | TxGNN-Wert | Hinweis |
|------|-----------|-----------|--------|
| 2 | Fokal Stiff-Limb-Syndrom | 99.06% | Nahezu identischer Wert zu Rang 1; wahrscheinlich das Ergebnis der gleichen Krankheitscluster-Einbettung, nicht eines unterschiedlichen Signals |
| 3 | Opsismodysplasie | 99.03% | Seltene pädiatrische Skelettdysplasie (INPPL1/SHIP2-getrieben); jeder Zusammenhang mit SGLT2-Inhibition ist spekulativ und wird durch Daten nicht gestützt |

---

## Fazit und nächste Schritte

**Entscheidung: Halten**

**Begründung:**
Die Vorhersage basiert ausschließlich auf einem TxGNN-Modellwert (Evidenzstufe L5) ohne bestätigende klinische Studien oder Literatur, und die Wirkmechanismus-Daten des Arzneimittels selbst sind nicht verfügbar. Eine Datenlücke mit Sperrschweregrad (TFDA-Warnungen/Kontraindikationen) verhindert auch eine vorläufige Sicherheitsbewertung, sodass dieser Kandidat nicht über S0 hinaus voranschreiten kann.

**Um fortzufahren, ist Folgendes erforderlich:**
- Beheben Sie DG001: Rufen Sie die TFDA-Packungsbeilage ab (Warnungen, Kontraindikationen, Arzneimittelwechselwirkungen), um die S1-Sicherheits-Vorbewertung zu ermöglichen
- Beheben Sie DG002: Erhalten Sie bestätigte ursprüngliche MOA von DrugBank/Produktbeilage, um die mechanistische Plausibilität zu bewerten
- Legen Sie ursprüngliche Indikation und Taiwan/internationale Zulassungsstatus fest, um den Vergleich „ursprüngliche vs. vorhergesagte Indikation" zu unterstützen
- Führen Sie eine gezielte Literatur-/Präklinische-Suche durch nach einem SGLT2i–GABAergen oder SGLT2i–autoimmunologischen neurologischen Mechanismus, da derzeit keiner vorhanden ist
- Angesichts des Clustering-Musters in den Rängen 1–2 sollten Sie in Betracht ziehen, zu überprüfen, ob die zugrunde liegende Wissensgraph-Knotenstruktur ein gemeinsames falsch positives Signal im gesamten Spektrum des Stiff-Person-Syndroms antreibt, bevor Sie weitere Evaluierungsressourcen einsetzen

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

