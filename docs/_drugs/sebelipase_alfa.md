---
layout: default
title: Sebelipase Alfa
parent: Nur Modellvorhersage (L5)
nav_order: 359
evidence_level: L5
indication_count: 10
---

# Sebelipase Alfa
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

# Sebelipase alfa: Von Lysosomaler Säurelipase-Mangel zum Scheie-Syndrom

## Einzeilenzusammenfassung

> Sebelipase alfa (Kanuma®) ist eine Enzymersatztherapie mit rekombinantem humanem lysosomalen Säurelipase (rhLAL), die ursprünglich für **Lysosomalen Säurelipase (LAL)-Mangel** entwickelt wurde, einschließlich Wolman-Erkrankung und Cholesterylester-Speicherkrankheit (CESD).
> Der nach dem TxGNN-Modell am höchsten bewertete neue Kandidat ist **Scheie-Syndrom** (eine milde Form von Mukopolysaccharidose Typ I),
> aber diese spezifische Vorhersage wird derzeit von **0 klinischen Studien** und **0 Publikationen** unterstützt — es ist ein rein modellgestütztes Signal ohne mechanistische Bestätigung.

---

## Schnellübersicht

| Element | Inhalt |
|---------|--------|
| Ursprüngliche Indikation* | Lysosomaler Säurelipase (LAL)-Mangel (inkl. Wolman-Erkrankung, CESD) |
| Vorhergesagte neue Indikation | Scheie-Syndrom |
| TxGNN-Vorhersagepunktzahl | 99.80% |
| Evidenzebene | L5 |
| Marktstellung Deutschland | Nicht im Handel |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | Aussetzen |

\* Es existiert kein BfArM-Zulassungseintrag für dieses Produkt (Arzneimittel ist in Deutschland nicht im Handel, `total_licenses = 0`). Die oben angegebene ursprüngliche Indikation wird aus der Literaturreferenz rekonstruiert, die diesem Dossier beigefügt ist (z. B. PMID 26452566 „Sebelipase alfa: first global approval"), nicht aus einem formalen Zulassungstext.

---

## Warum ist diese Vorhersage berechtigt?

Derzeit sind detaillierte Daten zum Wirkmechanismus (MOA) in der strukturierten Arzneimitteldatenbank nicht verfügbar (`original_moa: [Data Gap]`). Basierend auf den in diesem Dossier enthaltenen Literaturquellen ist Sebelipase alfa eine Enzymersatztherapie mit rekombinantem humanem lysosomalen Säurelipase (rhLAL). Seine Wirksamkeit beim LAL-Mangel — einschließlich des Wolman-Erkrankungs-Phänotyps mit Manifestation im Säuglingsalter und des später manifesten CESD-Phänotyps — ist durch abgeschlossene Phase-2/3-Studien (z. B. die ARISE-Studie, NCT01757184) gut dokumentiert und ist weltweit in der EU, den USA und Japan zugelassen.

Das Scheie-Syndrom ist jedoch eine eigenständige lysosomale Speicherkrankheit, verursacht durch einen Mangel an **Alpha-L-Iduronidase**, einem Enzym, das für den Abbau von Glykosaminoglukanen (GAG) verantwortlich ist — ein völlig anderes lysosomales Enzymsystem als LAL, das Cholesterylester und Triglyceride hydrolysiert. Die beiden Erkrankungen weisen nur breite, für lysosomale Speicherkrankheiten gemeinsame phänotypische Merkmale auf (Organomegalie, multisystemische Ansammlung), was mit dem bereits an anderer Stelle in diesem Vorhersagesatz identifizierten Muster konsistent ist: andere Kandidaten wie Morbus Gaucher und Tay-Sachs-Erkrankung erhielten aus demselben Grund dieselbe **Aussetzen**-Empfehlung — TxGNN scheint seine Vorhersagen eher auf Phänotyp-Ähnlichkeiten bei lysosomalen Speicherkrankheiten zu stützen als auf echter Enzym-Substrat-Übereinstimmung.

Mechanistisch ist die Enzymersatztherapie hochgradig enzymspezifisch: Sebelipase alfa kann nur das fehlende LAL-Enzym ersetzen und kann einen Alpha-L-Iduronidase-Mangel nicht kompensieren. Es gibt keine biochemische Grundlage, die die Wirksamkeit beim Scheie-Syndrom unterstützt, und dies spiegelt sich in der vollständigen Abwesenheit von klinischen oder Literaturquellen für diese spezifische Kombination wider.

---

## Klinische Studienhinweise

Derzeit keine zugehörigen registrierten klinischen Studien

---

## Literaturbeweise

Derzeit keine einschlägige Literatur verfügbar

---

## Sicherheitserwägungen

Bitte beachten Sie die Packungsbeilage für Sicherheitsinformationen.

---

## Fazit und nächste Schritte

**Entscheidung: Aussetzen**

**Begründung:**
Die am höchsten bewertete Vorhersage (Scheie-Syndrom) hat keine unterstützenden klinischen Studien oder Literaturquellen, und der zugrunde liegende Enzymmangelzustand (Alpha-L-Iduronidase) ist mechanistisch nicht mit dem LAL-Ersatzmechanismus von Sebelipase alfa verwandt. Dies ist ein reines Modellsignal (L5) ohne bestätigende biologische oder klinische Begründung.

**Um fortzufahren, wird Folgendes benötigt:**
- Präklinische oder biochemische Evidenz, dass rhLAL eine Kreuzreaktivität oder GAG-Weg-Relevanz in MPS I/Scheie-Syndrom hat (derzeit keine identifiziert)
- TFDA/BfArM-Etikett und Sicherheitsdaten (derzeit `[Data Gap]` — blockiert für jeden S1-Sicherheits-Vorcheck)
- Bestätigter DrugBank-MOA-Eintrag zum Ersetzen der aktuellen Datenlücke

**Hinweis für Pipeline-Überprüfung:** Rang 4 in diesem Vorhersagesatz (Cholesterylester-Speicherkrankheit) hat bereits eine abgeschlossene Phase-3-RCT (ARISE, NCT01757184) und 9 registrierte Studien — dies ist kein neuer Umwidmungskandidat, sondern eine bereits bekannte und bereits zugelassene Indikation des Arzneimittels. Es wird empfohlen, dies als Triage-/Datenqualitätsproblem zu kennzeichnen, anstatt es als neues Signal zu präsentieren.

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

