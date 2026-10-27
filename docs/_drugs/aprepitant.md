---
layout: default
title: Aprepitant
parent: Nur Modellvorhersage (L5)
nav_order: 36
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Aprepitant: vorhergesagte neue Indikation Nephrogenes Syndrom der inadäquaten Antidiurese (NSIAD) (Evidenzstufe L5). Ursprüngliche Indikation: Erbrechen"
monitor_inn: "APREPITANT"
predicted_indications: ["nephrogenic syndrome of inappropriate antidiuresis", "hypertrichosis (disease)", "pulmonary hypertension", "leprosy", "Ambras type hypertrichosis universalis congenita", "malformation syndrome with odontal and/or periodontal component", "kyphoscoliotic heart disease", "syndrome with a Dandy-Walker malformation as major feature", "subarachnoid hemorrhage (disease)", "isolated genetic hair shaft abnormality"]
---

# Aprepitant
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

## Aprepitant: Von Erbrechen und Übelkeit zum nephrogenen Syndrom der inadäquaten Antidiurese (NSIAD)
{: .text-alpha }

## Zusammenfassung

Aprepitant wurde ursprünglich zur Behandlung von Erbrechen, postoperativer Übelkeit und Erbrechen sowie in Verbindung mit Krebserkrankungen (Chemotherapie-induzierte Übelkeit) eingesetzt. Das TxGNN-Modell sagt voraus, dass es bei dem **nephrogenen Syndrom der inadäquaten Antidiurese (NSIAD)** wirksam sein könnte. Für diese Vorhersage liegen jedoch **keine klinischen Studien und keine Publikationen** vor; sie beruht ausschließlich auf der Modellvorhersage.

---

## Schnellübersicht

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Erbrechen; postoperative Übelkeit und Erbrechen; Krebs |
| Vorhergesagte neue Indikation | Nephrogenes Syndrom der inadäquaten Antidiurese (NSIAD) |
| TxGNN-Vorhersagewert | 99,97 % |
| Evidenzlevel | L5 |
| Marktstatus in Deutschland | Nur gelöschte/erloschene Zulassung |
| Anzahl der Zulassungen | 1 (davon 0 gültig, 1 erloschen) |
| Empfohlene Entscheidung | Hold |

---

## Warum ist diese Vorhersage plausibel?

Aktuell liegen keine detaillierten Daten zum Wirkmechanismus vor. Bekannt ist, dass Aprepitant ein Neurokinin-1-(NK1)-Rezeptorantagonist ist und seine Wirksamkeit bei Erbrechen und Übelkeit belegt ist.

Die mechanistische Verbindung zum NSIAD ist **spekulativ**. Denkbar wäre ein Zusammenhang über die Substanz-P-Signalübertragung und die zentrale Regulation von Vasopressin. NSIAD wird jedoch durch aktivierende Mutationen des Vasopressin-V2-Rezeptors (AVPR2) verursacht, und genau dieser Mechanismus wird durch eine NK1-Blockade nicht direkt beeinflusst. Die Vorhersage sollte daher als reine Modellvorhersage betrachtet werden.

Auch die weiteren vom Modell vorhergesagten Indikationen (u. a. Hypertrichose, pulmonale Hypertonie, Lepra, subarachnoidale Blutung) haben ähnlich hohe Werte (jeweils über 99,8 %), jedoch ebenfalls keine belastbare Evidenz. Bei der pulmonalen Hypertonie und der subarachnoidalen Blutung gibt es lediglich schwache, präklinische Hinweise auf eine Beteiligung der Substanz-P/NK1-Signalübertragung.

---

## Klinische Studien

Derzeit sind keine zugehörigen klinischen Studien registriert.

---

## Literaturevidenz

Derzeit ist keine zugehörige Literatur verfügbar.

---

## Informationen zum deutschen Markt

| Zulassungsnummer | Produktname | Darreichungsform | Zugelassene Indikation |
|---------|------|------|-----------|
| EMEA/H/C/000527 | Emend | – | Erbrechen; postoperative Übelkeit und Erbrechen; Krebs |

Diese Zulassung (Merck Sharp & Dohme B.V.) ist erloschen bzw. gelöscht; es existiert keine gültige Zulassung.

---

## Zytotoxizität

| Punkt | Inhalt |
|------|------|
| Zytotoxizitätsklassifikation | Kein Zytostatikum; Supportivtherapie (Antiemetikum, NK1-Rezeptorantagonist) |
| Myelosuppressionsrisiko | Nicht zutreffend; bitte Warnhinweise und Vorsichtsmaßnahmen der Fachinformation beachten |
| Emetogenitätsklassifikation | Nicht zutreffend (Aprepitant wirkt antiemetisch) |
| Überwachungsparameter | Leberfunktion (siehe Hinweis zu Leberversagen unten) |
| Handhabungsschutz | Bitte Warnhinweise und Vorsichtsmaßnahmen der Fachinformation beachten |

---

## Sicherheitsaspekte

- **Kontraindikationen (aus Wissensgraph, nicht aus der Fachinformation):** Im TxGNN-Wissensgraphen (PrimeKG) ist **Leberversagen** als Kontraindikation hinterlegt.
- **Arzneimittelwechselwirkungen:** Die Abfrage ergab insgesamt 100 Wechselwirkungen. Beispiele aus den vorliegenden Daten:
  - **Schwerwiegend (Major):** Fentanyl, Alfentanil, Acalabrutinib
  - **Moderat:** u. a. Paclitaxel, Abemaciclib, Nifedipin, Ibuprofen, Levonorgestrel, Hydrocortison, Lidocain, Dihydrocodein, Rabeprazol, Albendazol, Fluvoxamin, Fosamprenavir, Fosphenytoin, Fostamatinib, Gefitinib, Abametapir (topisch)
  - **Gering (Minor):** Dolutegravir

Für weitere Sicherheitsinformationen (Warnhinweise, Kontraindikationen laut Label) bitte die Fachinformation heranziehen.

---

## Fazit und nächste Schritte

**Entscheidung: Hold**

**Begründung:**
Der hohe TxGNN-Wert (99,97 %) wird weder durch klinische Studien noch durch Literatur gestützt, und der Zusammenhang zwischen NK1-Antagonismus und der AVPR2-vermittelten Pathologie des NSIAD ist mechanistisch nicht überzeugend. Zudem besteht in Deutschland keine gültige Zulassung.

**Für ein Weiterkommen sind folgende Schritte erforderlich:**
- Daten zum Wirkmechanismus (MOA) ergänzen (z. B. über die DrugBank-API)
- Warnhinweise und Kontraindikationen aus der Fachinformation der Zulassungsbehörde beschaffen und auswerten (sicherheitsrelevante Voraussetzung)
- Präklinische Studien (Zellmodelle oder Tiermodelle mit AVPR2-Aktivierung) zur Prüfung der biologischen Plausibilität
- Systematische Literaturrecherche zu NK1-Antagonisten und Wasserhaushalt/Vasopressin-Regulation
- Prüfung des Zulassungsstatus und der Verfügbarkeit in Deutschland, da die einzige Zulassung erloschen ist
## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

