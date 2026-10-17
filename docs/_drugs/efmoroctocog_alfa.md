---
layout: default
title: Efmoroctocog Alfa
parent: Nur Modellvorhersage (L5)
nav_order: 159
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Efmoroctocog Alfa: vorhergesagte neue Indikation Pseudo-von-Willebrand-Erkrankung (Evidenzstufe L5). Ursprüngliche Indikation: Hämophilie A"
monitor_inn: "EFMOROCTOCOG ALFA"
predicted_indications: ["pseudo-von Willebrand disease", "primary release disorder of platelets", "Glanzmann thrombasthenia", "Scott syndrome", "acquired coagulation factor deficiency", "bleeding diathesis due to a collagen receptor defect", "hemorrhagic disorder due to a constitutional thrombocytopenia", "fetal and neonatal alloimmune thrombocytopenia", "thrombotic thrombocytopenic purpura"]
---

# Efmoroctocog Alfa
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

# Efmoroctocog alfa: Von Hämophilie A zu pseudo-von-Willebrand-Erkrankung

## Zusammenfassung in einem Satz

Efmoroctocog alfa (Handelsname Elocta) ist ein rekombinanter, Fc-fusionierter Faktor VIII und wurde ursprünglich zur Behandlung der **Hämophilie A** eingesetzt.
Das TxGNN-Modell sagt voraus, dass der Wirkstoff bei der **pseudo-von-Willebrand-Erkrankung** wirksam sein könnte.
Für diese Vorhersage liegen jedoch **keine klinischen Studien** und **keine Publikationen** vor, sie beruht ausschließlich auf der Modellvorhersage.

---

## Schnellübersicht

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Hämophilie A |
| Vorhergesagte neue Indikation | Pseudo-von-Willebrand-Erkrankung |
| TxGNN-Vorhersagewert | 99,997 % |
| Evidenzstufe | L5 |
| Marktstatus in Deutschland | Nur erloschene/aufgehobene Zulassung |
| Anzahl der Zulassungen | 1 |
| Empfohlene Entscheidung | Hold |

---

## Warum ist diese Vorhersage plausibel?

Die Plausibilität ist hier **gering**. Detaillierte Daten zum Wirkmechanismus liegen derzeit nicht vor. Bekannt ist, dass Efmoroctocog alfa ein rekombinanter Faktor VIII mit Fc-Fusion ist, dessen Wirksamkeit bei Hämophilie A belegt ist. Er ersetzt den fehlenden Gerinnungsfaktor VIII.

Die pseudo-von-Willebrand-Erkrankung ist dagegen eine Thrombozytenerkrankung. Ursache ist ein Gain-of-Function-Defekt des Thrombozytenrezeptors GPIbα, der die Bindung an den von-Willebrand-Faktor (VWF) verstärkt und hochmolekulare VWF-Multimere abbaut. Dieser Rezeptordefekt wird durch Faktor VIII nicht behoben. Der hohe Vorhersagewert spiegelt vermutlich die Nähe im Netzwerk der Blutungserkrankungen im Wissensgraphen wider, nicht einen validierten Mechanismus.

Auch bei den übrigen neun vorhergesagten Indikationen (z. B. primäre Thrombozyten-Freisetzungsstörung, Glanzmann-Thrombasthenie, Scott-Syndrom, thrombotisch-thrombozytopenische Purpura) betrifft der Defekt meist die Thrombozyten oder andere Faktoren als Faktor VIII. Am ehesten nachvollziehbar sind:
- **Erworbener Gerinnungsfaktormangel:** Hier ist der Faktor-VIII-Mangel das gemeinsame Kernproblem. Bei erworbener Hämophilie A neutralisieren jedoch Autoantikörper den Faktor VIII, sodass rekombinanter Fc-fusionierter FVIII kaum wirkt.
- **Hämophilie A mit Gefäßanomalie:** Dies ist im Wesentlichen ein Subtyp der bereits zugelassenen Indikation und kein echtes Repurposing. Die Gefäßanomalie würde nicht behoben.

---

## Evidenz aus klinischen Studien

Derzeit sind keine zugehörigen klinischen Studien registriert.

---

## Evidenz aus der Literatur

Derzeit liegt keine zugehörige Literatur vor.

---

## Marktinformationen Deutschland

| Zulassungsnummer | Produktname | Darreichungsform | Zugelassene Indikation |
|---------|------|------|-----------|
| EMEA/H/C/003964 | Elocta | – | Hämophilie A |

Hinweis: Diese Zulassung hat den Status „erloschen/aufgehoben“. Es besteht derzeit keine gültige Zulassung.

---

## Sicherheitsaspekte

Zu den Packungsbeilage-Warnhinweisen und Gegenanzeigen liegen derzeit keine Daten vor. Für Sicherheitsinformationen siehe bitte die Packungsbeilage.

Aus den vorliegenden Daten ergibt sich ein relevanter Sicherheitshinweis: Bei der **thrombotisch-thrombozytopenischen Purpura (TTP)** ist Faktor VIII nicht der fehlende Faktor. Zusätzlicher FVIII könnte theoretisch das Thromboserisiko erhöhen. Der hohe Vorhersagewert sollte hier keinesfalls als Unterstützung gewertet werden. Die Standardtherapie besteht aus Plasmaaustausch, Immunsuppression und Caplacizumab.

Wechselwirkungen: In den vorliegenden Daten wurden keine Einträge gefunden.

---

## Fazit und nächste Schritte

**Entscheidung: Hold**

**Begründung:**
Die Vorhersage beruht ausschließlich auf einem Modell (Evidenzstufe L5), es gibt weder klinische Studien noch Publikationen. Zudem spricht der Mechanismus gegen einen Nutzen: Der Defekt liegt bei der pseudo-von-Willebrand-Erkrankung im Thrombozytenrezeptor und nicht im Faktor VIII. Die einzige deutsche Zulassung ist erloschen.

**Für ein Weiterkommen sind folgende Schritte nötig:**
- Auswertung der Packungsbeilage (Warnhinweise und Gegenanzeigen) über die BfArM-Website, da ohne diese Daten kein Sicherheitsscreening möglich ist
- Daten zum Wirkmechanismus aus DrugBank
- Systematische Literatur- und Studienrecherche zu den Indikationen mit noch am ehesten plausiblem Zusammenhang (erworbener Gerinnungsfaktormangel, Hämophilie A mit Gefäßanomalie)
- Klärung des aktuellen Zulassungs- und Verfügbarkeitsstatus in Deutschland
## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

