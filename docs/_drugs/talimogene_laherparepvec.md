---
layout: default
title: Talimogene Laherparepvec
parent: Nur Modellvorhersage (L5)
nav_order: 378
evidence_level: L5
indication_count: 7
---

# Talimogene Laherparepvec
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **7** 
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

# Talimogene laherparepvec: Vom Melanom zu CMM7 (Kutanes malignes Melanom, Anfälligkeitssubtyp)

## One-Sentence Summary (Zusammenfassung in einem Satz)

> Talimogene laherparepvec (T-VEC) ist eine genetisch modifizierte HSV-1-Onkolytika-Virusimmuntherapie, die bekanntermaßen für inoperable, injizierbare Melanomläsionen der Haut, des Unterhautgewebes und der Lymphknoten zugelassen ist (diese ursprüngliche Indikation ist nicht im aktuellen Nachweispaket enthalten und wird nur aus öffentlich bekanntem behördlichen Wissen zitiert).
> Das TxGNN-Modell sagt voraus, dass es für **CMM7** (einen Anfälligkeitssubtyp des kutanen malignen Melanoms) relevant sein könnte, mit einer Vorhersagepunktzahl von **99.20%**, aber **keine klinischen Studien oder Literaturangaben** sind derzeit registriert, um diese spezifische Verbindung zu unterstützen, und die mechanistische Begründung für diese höchste Vorhersage wurde noch nicht im Nachweispaket abgeschlossen.

---

## Schnelle Übersicht

| Element | Inhalt |
|------|------|
| Ursprüngliche Indikation | Nicht im aktuellen Nachweispaket erfasst (`original_indications` ist leer; Arzneimittel ist noch nicht in Taiwan vermarktet). Öffentlich bekannte Indikation: inoperable kutane/subkutane/nodale Melanomläsionen. |
| Vorhergesagte neue Indikation | CMM7 (Kutanes malignes Melanom, Anfälligkeitssubtyp 7) |
| TxGNN-Vorhersagewert | 99.20% |
| Nachweisebene | L5 (keine klinischen Studien oder Literaturangaben identifiziert; nur Modellvorhersage) |
| Marktstatus in Taiwan | ✗ Nicht vermarktet (Nicht vermarktet) |
| Anzahl der Genehmigungen | 0 |
| Empfohlene Entscheidung | Halten |

---

## Warum ist diese Vorhersage angemessen?

Derzeit sind keine detaillierten Daten zum Wirkungsmechanismus verfügbar (als Hochrisiko-Datenlücke gekennzeichnet, DG002). Basierend auf öffentlich bekannten Informationen ist Talimogene laherparepvec ein onkolytisches Herpes-Simplex-Virus Typ 1 (HSV-1), das so konstruiert wurde, dass es sich selektiv in Tumorzellen repliziert, diese lysiert und GM-CSF exprimiert, um lokale und systemische Anti-Tumor-Immunantworten zu stimulieren. Es wird ausschließlich durch direkte intralesionale Injektion verabreicht.

CMM7 ist keine eigenständige Krankheitsentität im üblichen Sinne – es bezieht sich auf einen kutanen malignen Melanom-Anfälligkeitslocus/Subtyp innerhalb der Melanom-Krankheitsfamilie, derselbe Tumorzelltyp wie die bekannte ursprüngliche Indikation von T-VEC. Mechanistisch ist diese Nähe plausibel (gleicher Tumorzelltyp, gleiche routengerechte Läsionsklasse), aber das Nachweispaket lässt `mechanistic_link` und `similarity_to_original` für diesen am höchsten bewerteten Kandidaten als **„ausstehend"** gekennzeichnet – das heißt, es wurde keine abgeschlossene Begründung aufgezeichnet, und es wurden keine unterstützenden klinischen Studien oder Literaturangaben abgerufen.

Im Gegensatz dazu wurden die sechs niedriger bewerteten Kandidaten (Ränge 2–7, siehe unten) bereits bewertet und durchgehend als **Halten** gekennzeichnet, hauptsächlich aufgrund von Inkompatibilität der Applikationsroute (tiefe/nicht erreichbare Läsionen, ZNS- oder intraokulare Erkrankung) oder mangelnder mechanistischer/histologischer Übereinstimmung mit Melanom. Da der am höchsten bewertete Kandidat (CMM7) selbst keine abgeschlossenen Nachweise und Begründungen hat und das Arzneimittel nicht in Taiwan mit einer blockierenden Sicherheitsdatenlücke (DG001) vermarktet wird, erfüllt derzeit kein Kandidat in diesem Paket die Schwelle für eine weitere Bewertung.

---

## Klinische Studienevidenz

Derzeit keine zugehörigen klinischen Studien registriert

## Literaturnachweis

Derzeit keine zugehörige Literatur verfügbar

---

## Weitere vorhergesagte Indikationen (Ränge 2–7, bereits bewertet)

| Rang | Krankheit | TxGNN-Wert | Nachweisebene | Empfehlung | Wichtigste Begründung |
|------|------------|-------------|-----------------|----------------|-----------|
| 2 | Pädiatrisches leptomeningeales Melanom | 99.15% | L5 | Halten | Intralesionale Route kann ZNS/leptomeningealen Raum nicht erreichen; keine pädiatrischen Sicherheitsdaten |
| 3 | Epitheloider uveales Melanom | 99.13% | L5 | Halten | Unterschiedliche Mutationslandschaft (GNAQ/GNA11 vs BRAF/NRAS), immunologisch privilegierter intraokulärer Ort, schlechte Immuntherapie-Reaktionsgeschichte |
| 4 | Glottisches Plattenepithelkarzinom | 99.07% | L5 | Halten | Unterschiedliche Histologie/Immunprofil; glottische Anatomie begrenzt die Durchführbarkeit intralesionaler Injektionen |
| 5 | Okkultes Lungen-Plattenepithelkarzinom | 99.05% | L5 | Halten | „Okkulter" Tumor ist per Definition nicht lokalisierbar – grundlegend inkompatibel mit intralesionaler Abgabe |
| 6 | Rektales kloacogenes Karzinom | 99.01% | L5 | Halten | Seltener histologischer Subtyp ohne gemeinsamen Mechanismus mit Melanom; keine unterstützenden Daten |
| 7 | Adenoplattiges Gallenblasen-Karzinom | 99.01% | L5 | Halten | Tief gelegene Läsion, intralesionale Injektion nicht ohne invasiven Zugang durchführbar; keine unterstützenden Daten |

Alle sechs Kandidaten wurden bereits als **Halten** im Nachweispaket bewertet, hauptsächlich aufgrund von Inkompatibilität der Applikationsroute mit T-VECs intralesionaler Applikation und dem Fehlen jeglicher unterstützenden klinischen Studien- oder Literaturnachweise.

---

## Taiwan-Marktinformationen

Keine Vermarktungsgenehmigungen gefunden. `taiwan_regulatory.market_status` = Nicht vermarktet (Nicht vermarktet), `total_licenses` = 0, `licenses` = leer. Talimogene laherparepvec ist derzeit in dieser Rechtsordnung nicht zugelassen zum Verkauf.

---

## Zytotoxizität

Talimogene laherparepvec ist eine onkolytische Virusimmuntherapie für Melanom (eine maligne Neubildung), daher gilt dieser Abschnitt. Keine DrugBank-Toxizität oder MOA-Daten sind im Nachweispaket vorhanden; die folgende Tabelle spiegelt nur öffentlich bekannte Arzneimittelklassen-Informationen wider.

| Element | Inhalt |
|------|------|
| Zytotoxizitätsklassifizierung | Immuntherapie (Onkolytische Virustherapie) – kein konventionelles zytotoxisches Agens |
| Knochenmarkssuppressionsrisiko | Gering (Mechanismus ist virale Lyse + Immunstimulation, keine DNA-schädigende Chemotherapie) |
| Emetogenitätsklassifizierung | Gering |
| Überwachungselemente | Injektionsstellenreaktionen, grippeähnliche Symptome (Fieber, Schüttelfrost, Müdigkeit), Zeichen herpetischer Infektion/Dissemination, immunvermittelte Nebenwirkungen |
| Handhabungsschutz | Erfordert Biosicherheitshandhabung für lebende Viren (Vermeidung von Kontakt mit immungeschwächten Personen/schwangeren Mitarbeitern, Nadelstichvorsorgemaßnahmen) statt Standard-Handling-Protokollen für zytotoxische Arzneimittel |

---

## Sicherheitsüberlegungen

Bitte beachten Sie die Packungsbeilage für Sicherheitsinformationen. (`key_warnings`, `contraindications` und `ddi` sind alle Datenlücken im aktuellen Nachweispaket; DG001 – TFDA-Kennzeichnungswarnungen/Kontraindikationen – ist als blockierend gekennzeichnet, was bedeutet, dass dieser Kandidat die S1-Sicherheitsvorabprüfung nicht bestehen kann, bis dies behoben ist.)

---

## Fazit und nächste Schritte

**Entscheidung: Halten**

**Begründung:**
Der am höchsten bewertete Kandidat (CMM7) hat keine klinischen Studien- oder Literaturnachweise und seine mechanistische Begründung ist noch als „ausstehend" gekennzeichnet; die sechs nächsten Kandidaten wurden bereits formal als Halten bewertet aufgrund von Inkompatibilität der Applikationsroute oder mangelnder mechanistischer Übereinstimmung. Kombiniert mit einer blockierenden Sicherheitsdatenlücke (TFDA-Kennzeichnungsdaten nicht verfügbar) und null Vermarktungsgenehmigungen in Taiwan, unterstützt derzeit kein Kandidat in diesem Paket ein Fortschreiten.

**Um fortzufahren, ist Folgendes erforderlich:**
- TFDA-zugelassene (oder gleichwertige) Packungsbeilage – Warnungen, Kontraindikationen und DDI-Daten (behebt DG001, derzeit blockierend)
- Bestätigter Wirkmechanismus aus DrugBank oder Primärliteratur (behebt DG002)
- Abschluss der `mechanistic_link` / `similarity_to_original` Begründung für den CMM7-Kandidaten (derzeit „ausstehend")
- Gezielter Literatur-/Klinische Studiensuche spezifisch für CMM7 und Melanom-Anfälligkeitssubtypen
- Bestätigung des Taiwan-Markt-/Registrierungsstatus vor jeder weiteren Bewertungsphase

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

