---
layout: default
title: Zanamivir
parent: Nur Modellvorhersage (L5)
nav_order: 431
evidence_level: L5
indication_count: 2
---

# Zanamivir
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **2** 
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

# Zanamivir: Von Influenza zu Pyelonephritis

## Zusammenfassung in einem Satz

> Zanamivir ist ein Neuraminidase-Inhibitor, der ursprünglich zur Behandlung von Influenza A/B entwickelt wurde und durch Hemmung des viralen Oberflächenenzyms wirkt, das für die Virionfreisetzung erforderlich ist.
> Das TxGNN-Modell sagt eine mögliche Wirksamkeit gegen **Pyelonephritis** voraus, aber derzeit unterstützen **0 klinische Studien** und **0 Publikationen** diese spezifische Verbindung, und die mechanistische Analyse des Evidenzpakets kennzeichnet die Vorhersage als wahrscheinlich falsch-positiv.

---

## Schnellübersicht

| Eintrag | Inhalt |
|------|------|
| Ursprüngliche Indikation | Influenza (Neuraminidase-Inhibitor; keine formale Lizensierungsdokumentation verfügbar – Arzneimittel nicht in Deutschland im Handel) |
| Vorhergesagte neue Indikation | Pyelonephritis |
| TxGNN-Vorhersage-Score | 99.84% |
| Evidenzstufe | L5 (nur Modellvorhersage, keine unterstützenden Studien) |
| Marktstatus Deutschland | Nicht im Handel |
| Zulassungsanzahl | 0 |
| Empfohlene Entscheidung | Abwarten |

---

## Warum ist diese Vorhersage angemessen?

Detaillierte Wirkmechanismus-Daten aus DrugBank sind für diesen Kandidaten nicht verfügbar (markiert als Datenlücke mit hohem Schweregrad). Die Begründung zur Arzneimittelumwidmung im Evidenzpaket bestätigt jedoch, dass Zanamivir ausschließlich als Neuraminidase-Inhibitor gegen das Oberflächenglykoprotein des Influenzavirus wirkt – es hat keinerlei antibakterielle Aktivität.

Pyelonephritis ist eine Infektion der oberen Harnwege durch Bakterien, verursacht am häufigsten durch gramnegative Organismen wie *E. coli*. Es gibt keine bekannte pharmakologische Überschneidung zwischen viraler Neuraminidase-Inhibition und der Pathogenese der bakteriellen Pyelonephritis. Das Evidenzpaket selbst besagt, dass der hohe TxGNN-Score wahrscheinlich ein **semantisches Nähe-Artefakt im Wissensgraph** widerspiegelt (beide Indikationen sind breit mit „Infektion" verknüpft), anstatt einer echten mechanistischen Beziehung.

Eine zweite, niedriger eingestufte Vorhersage („Störung des Tyrosin-Stoffwechsels", Score 99.02%) zeigt das gleiche Muster: die einzige unterstützende Literatur erörtert die H274Y/H275Y-Neuraminidase-Resistenzmutation, bei der eine Histidin→Tyrosin-Aminosäure-Substitution vorliegt – eine zufällige Namensähnlichkeit, keine Verbindung zu vererbten Tyrosin-Stoffwechselstörungen (z.B. Tyrosinämie). Keine der beiden Vorhersagen hat derzeit eine glaubwürdige mechanistische oder klinische Grundlage.

---

## Klinische Studienevidenz

Derzeit sind keine entsprechenden klinischen Studien registriert.

---

## Literaturevidenz

Derzeit ist keine entsprechende Literatur verfügbar.

---

## Marktinformation Deutschland

Zanamivir ist derzeit **nicht im Handel** in Deutschland, und keine Zulassungsunterlagen (BfArM-Lizenznummern, Produktnamen oder genehmigte Indikationstexte) sind in der Datenbank verfügbar.

---

## Sicherheitsaspekte

Für Sicherheitsinformationen wird auf die Fachinformation verwiesen.

---

## Schlussfolgerung und nächste Schritte

**Entscheidung: Abwarten**

**Begründung:**
Die beste Vorhersage (Pyelonephritis) hat null unterstützende klinische Studien oder Literatur, und die mechanistische Analyse des Evidenzpakets bewertet die Arzneimittel-Krankheits-Verbindung als biologisch implausibel und wahrscheinlich ein Wissensgraph-Artefakt anstatt eines echten pharmakologischen Signals. Die Evidenzstufe ist L5, die niedrigste Stufe (nur Modellvorhersage).

**Um fortzufahren, ist Folgendes erforderlich:**
- Behebung der blockierenden Datenlücke (DG001): TFDA/BfArM-Fachinformations-Warnungen und Kontraindikationen, erforderlich vor jeglicher S1-Sicherheitsvorabprüfung
- Bestätigte Wirkmechanismus-Daten aus DrugBank (DG002)
- Unabhängige pharmakologische oder präklinische Begründung, die Neuraminidase-Inhibition mit bakterieller Pyelonephritis verbindet, falls dieser Kandidat weiter verfolgt werden soll
- Neubewertung der TxGNN-Scoring-Methodik, um potenzielle semantische-Nähe-Falsch-Positive bei infektionsbezogenen Indikationen zu adressieren

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

