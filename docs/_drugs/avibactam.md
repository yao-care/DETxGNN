---
layout: default
title: Avibactam
parent: Nur Modellvorhersage (L5)
nav_order: 42
evidence_level: L5
indication_count: 6
---

# Avibactam
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **6** 
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

# Avibactam: Von der β-Laktamase-Inhibitor-Kombinationstherapie zu Streptococcal Pneumonia (Streptococcus-pneumoniae-Infektion)

## Zusammenfassung in einem Satz

Avibactam ist ein nicht-β-Laktam-β-Laktamase-Inhibitor ohne intrinsische antibakterielle Aktivität und kann klinisch nur in Kombination mit β-Laktam-Antibiotika (z. B. ceftazidime) verwendet werden, um die Wirksamkeit gegen enzymproduzierende Bakterienstämme wiederherzustellen. Es hat derzeit keine Arzneimittelzulassung in Deutschland. Das TxGNN-Modell sagt eine mögliche Wirksamkeit gegen **Streptococcal Pneumonia (Streptococcus-pneumoniae-Infektion)** voraus, aber es gibt derzeit **keine klinischen Studien und keine Literatur**, die diese Richtung unterstützen, und die Wirkmechanismus-Analyse im Evidenzpaket selbst zeigt, dass die Assoziation schwach ist.

---

## Übersichtstabelle

| Artikel | Inhalt |
|--------|---------|
| Ursprüngliche Indikation | Keine Registrierungsdaten; Avibactam selbst hat keine Monotherapie-Indikation und wird nur als β-Laktamase-Inhibitor in Kombination mit Antibiotika verwendet |
| Vorhergesagte neue Indikation | Streptococcal pneumonia (Streptococcus-pneumoniae-Infektion) |
| TxGNN-Vorhersagepunktzahl | 99.70% |
| Evidenzstufe | L5 (nur Modellvorhersage, keine eigentliche Forschung) |
| Marktstatus in Deutschland | ✗ Nicht vermarktet |
| Anzahl der Genehmigungen | 0 |
| Empfohlene Entscheidung | Hold |

---

## Warum ist diese Vorhersage rational?

Derzeit sind keine detaillierten Daten zum Wirkmechanismus (MOA) verfügbar (DrugBank-Feld ist als Datenlücke gekennzeichnet). Gemäß der im Evidenzpaket enthaltenen Wirkmechanismus-Analyse ist Avibactam ein nicht-β-Laktam-β-Laktamase-Inhibitor ohne intrinsische antibakterielle Aktivität. Seine klinische Rolle ist auf die Kombination mit β-Laktam-Antibiotika (z. B. ceftazidime) beschränkt, um die Wirksamkeit des Arzneimittels gegen enzymproduzierende gramnegative Bakterienstämme wiederherzustellen.

Die Wirkmechanismus-Analyse des Evidenzpakets für die am höchsten bewertete vorhergesagte Indikation (Streptococcus-pneumoniae-Infektion) ist jedoch **negativ**: Streptococcus-pneumoniae-Infektionen sind in den meisten Fällen von Natur aus empfindlich gegenüber Penicillinen/Cephalosporinen und sind nicht der typische Zielorganismus für β-Laktamase-Resistenz. Das heißt, selbst wenn Avibactam mit Antibiotika kombiniert wird, ist es schwierig, die zusätzliche Wirksamkeit gegen Streptococcus-pneumoniae-Infektionen durch seinen Enzym-Inhibitions-Mechanismus rational zu erklären. Die restlichen 5 vorhergesagten Indikationen (schwere Influenza, Uretertuberkulose, urogenitale Schistosomiasis, Hyperamylasämie, Hyperviskositätssyndrom) zeigen ebenfalls in ihrer Wirkmechanismus-Analyse keine rationalen biologischen Wege auf (Virusinfektionen, Mykobakterien, Parasiten, metabolische Erkrankungen, hämatologische Immunerkrankungen usw. stehen alle in keinem Zusammenhang mit dem bakteriellen β-Laktamase-Inhibitions-Mechanismus).

Zusammenfassend weisen alle 6 vorhergesagten Indikationen in dieser Runde eine schwache Wirkmechanismus-Rationalität auf. Es handelt sich um modellgestützte statistische Assoziationen statt um wirkmechanismus-getriebene Hypothesen, die mit Vorsicht zu betrachten sind.

---

## Klinische Studienevidenz

Derzeit keine einschlägigen klinischen Studien registriert.

---

## Literaturevidenz

Derzeit keine einschlägigen Literaturangaben vorhanden.

---

## Informationen zum deutschen Markt

Avibactam hat derzeit keine Arzneimittelzulassung in Deutschland (Anzahl der Genehmigungen: 0), und der Marktstatus ist „Nicht vermarktet". Da keine Registrierungsdaten vorhanden sind, können derzeit keine Darreichungsform, kein Produktname oder genehmigter Indikationstext bereitgestellt werden.

---

## Sicherheitsaspekte

Bitte konsultieren Sie die Packungsbeilage für Sicherheitsinformationen.

(TFDA-Packungsbeilage-Warnhinweise und Gegenanzeigungsdaten fehlen derzeit, sind als Blocking-Level-Datenlücke eingestuft und müssen vorrangig ergänzt werden, bevor eine S1-Sicherheitsbewertung eingeleitet werden kann.)

---

## Schlussfolgerungen und nächste Schritte

**Entscheidung: Hold**

**Begründung:**
- Die Evidenzstufe aller sechs vorhergesagten Indikationen ist L5 (nur Modellvorhersage, ohne klinische Studien oder Literaturbelege).
- Die Wirkmechanismus-Analyse der am höchsten bewerteten Vorhersage (Streptococcus-pneumoniae-Infektion) zeigt eine negative Schlussfolgerung, und die Wirkmechanismus-Assoziation der übrigen Kandidaten ist ebenfalls schwach oder nicht vorhanden.
- Es gibt Blocking-Level-Datenlücken (BfArM package insert warnings/contraindications). Nach den Richtlinien kann nicht in die S1-Sicherheitsbewertung eingeleitet werden, und auch eine Bewertung des Arzneimittel-Wechselwirkungsrisikos ist nicht möglich.

**Um voranzuschreiten, muss Folgendes ergänzt werden:**
- TFDA (oder entsprechende deutsche/EU-Behörden-) Packungsbeilage-Warnhinweise und Gegenanzeigungsdaten beschaffen (DG001, Blocking)
- Vervollständigung der MOA-Daten (Wirkmechanismus) über die DrugBank-API (DG002, High)
- Suche nach präklinischen oder fallgestützten Belegen für die am höchsten bewerteten Kandidaten-Indikationen, um zu bestätigen, ob eine weitere Untersuchung gerechtfertigt ist
- Falls weiterhin keine empirischen Belege vorhanden sind, wird empfohlen, alle 6 Kandidaten im Hold-Status zu belassen und nicht in die nächste Evaluierungsphase einzutreten

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

