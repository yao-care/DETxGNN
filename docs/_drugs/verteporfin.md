---
layout: default
title: Verteporfin
parent: Nur Modellvorhersage (L5)
nav_order: 424
evidence_level: L5
indication_count: 1
---

# Verteporfin
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **1** 
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

# Verteporfin: Von der choroidalen Neovaskularisation zur mitochondrialen Störung der oxidativen Phosphorylierung

## Zusammenfassung in einem Satz

> Verteporfin ist ein Photosensibilisator, das ursprünglich in der photodynamischen Therapie (PDT) zur Behandlung der choroidalen Neovaskularisation (z. B. neovaskuläre altersbedingte Makuladegeneration) verwendet wurde.
> Das TxGNN-Modell sagt voraus, dass es bei der **mitochondrialen Störung der oxidativen Phosphorylierung aufgrund von nuklearen DNA-Anomalien** wirksam sein könnte,
> aber diese Vorhersage wird derzeit durch **keine klinischen Studien und keine Literatur** unterstützt — es ist ein rein modellgestütztes Signal (L5) und erfordert eine manuelle Überprüfung des Wirkmechanismus vor weiteren Maßnahmen.

---

## Schnellübersicht

| Element | Inhalt |
|---------|---------|
| Ursprüngliche Indikation | Choroidale Neovaskularisation / neovaskuläre altersbedingte Makuladegeneration (photodynamische Therapie) — basierend auf bekannter klinischer Anwendung, nicht in den bereitgestellten Lizenzierungsdaten vorhanden |
| Vorhergesagte neue Indikation | Mitochondriale Störung der oxidativen Phosphorylierung aufgrund von nuklearen DNA-Anomalien |
| TxGNN-Vorhersage-Score | 99.49% (Rang 5945) |
| Evidenzlevel | L5 |
| Marktstatus in Deutschland | Nicht vermarktet |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | Halten |

---

## Warum ist diese Vorhersage sinnvoll?

Detaillierte Daten zum Wirkmechanismus sind in der aktuellen Evidenzsammlung nicht verfügbar (gekennzeichnet als Sperrend/hochgradig schwerwiegende Datenlücke — siehe Nächste Schritte). Basierend auf bekannten Informationen wirkt Verteporfin als lichtaktivierter Photosensibilisator, der bei Laserbestrahlung reaktive Sauerstoffspezies erzeugt, um das neovaskuäre Endothel selektiv zu schädigen — dies ist die Grundlage seiner genehmigten Anwendung in der PDT für choroidale Neovaskularisation. Neben seiner lichtabhängigen Aktivität wurde Verteporfin auch als lichtunabhängiger Inhibitor der YAP/TAZ-Transkriptionsaktivatoren im Hippo-Signalweg untersucht, was Interesse in der Onkologie- und Antifibrose-Forschung geweckt hat.

Keiner dieser bekannten Mechanismen — photodynamische Gefäßablation oder YAP/TAZ-Inhibition — weist eine etablierte biochemische Verbindung zu nuklear-DNA-bedingten Störungen der Assemblierung oder Funktion von OXPHOS-Komplexen auf, die der vorhergesagten Indikation zugrunde liegen. Der sehr hohe TxGNN-Score (99.49%) spiegelt höchstwahrscheinlich **topologische Ähnlichkeit im Wissensgraph** wider (z. B. gemeinsame Gene, Signalwege oder co-auftretende Arzneistoff-/Krankheits-Nachbarn) eher als eine begründete pharmakologische Rationale. Diese Vorhersage sollte nur als hypothesengenerierendes Signal behandelt werden, in Erwartung einer manuellen Überprüfung der zugrunde liegenden Wissensgraph-Pfade und aller mitochondrial-relevanten Pharmakologiedaten für Verteporfin.

---

## Evidenz aus klinischen Studien

Derzeit keine zugehörigen klinischen Studien registriert

---

## Literaturbeweise

Derzeit keine zugehörige Literatur verfügbar

---

## Marktinformationen für Deutschland

Verteporfin wird derzeit **nicht vermarktet** in Deutschland, und keine Vermarktungsgenehmigungen sind in der Evidenzsammlung verzeichnet (total_licenses = 0).

---

## Sicherheitsaspekte

Weitere Informationen zur Sicherheit finden Sie im Beipackzettel.

---

## Schlussfolgerung und nächste Schritte

**Entscheidung: Halten**

**Begründung:**
Die Vorhersage wird durch null klinische Studien und null Literatur unterstützt (L5, rein modellgestützt), und es gibt keinen etablierten Wirkmechanismus, der Verteporfins bekannte Pharmakologie mit nuklear-DNA-bedingten OXPHOS-Störungen verbindet. Ohne ein derzeit in Deutschland vermarktetes Produkt und mit einer Sperrenden Sicherheitsdatenlücke (keine TFDA/Etikett-Warnungen abgerufen), kann dieser Kandidat nicht über S0 hinausgehen.

**Um fortzufahren, wird Folgendes benötigt:**
- Abrufen von TFDA/EMA-Etikett-Warnungen, Kontraindikationen und DDI-Daten (derzeit Sperrend — DG001)
- Abrufen verifyzierten Arzneimittel-MOA-Daten aus DrugBank oder Primärliteratur (derzeit hochgradig — DG002)
- Manuelle Überprüfung des TxGNN-Wissensgraph-Pfads/der Pfade, die diese Vorhersage antreiben, um echte Wirkmechanismus-Signale von Wissensgraph-Topologie-Artefakten zu unterscheiden
- Präklinische/Wirkmechanismus-Evidenz (z. B. Assays zur mitochondrialen Funktion) vor der Überlegung einer klinischen Hypothesengenerierung

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

