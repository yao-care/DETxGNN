---
layout: default
title: Lidocaine
parent: Nur Modellvorhersage (L5)
nav_order: 232
evidence_level: L5
indication_count: 10
---

# Lidocaine
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

# Lidocain: Von der Lokalanästhesie zur punktförmigen epithelialen Keratokonjunktivitis

## Zusammenfassung in einem Satz

Lidocain ist ein etabliertes Amid-Lokalanästhetikum, das klinisch zur Betäubung von Gewebe für die Schmerzbekämpfung bei chirurgischen/verfahrenstechnischen Eingriffen eingesetzt wird (und in bestimmten Formulierungen als Antiarrhythmikum der Klasse Ib). Das TxGNN-Modell sagt eine mögliche neue Indikation für **punktförmige epitheliale Keratokonjunktivitis** voraus, aber diese Vorhersage wird derzeit durch **0 klinische Studien** und **0 Publikationen** gestützt – es ist ein reines Modellscore-Signal ohne externe Validierung.

## Schneller Überblick

| Eintrag | Inhalt |
|------|------|
| Ursprüngliche Indikation | Lokalanästhesie (amtlicher Indikationstext nicht verfügbar – keine Zulassungsunterlagen im Datensatz) |
| Vorhergesagte neue Indikation | Punktförmige epitheliale Keratokonjunktivitis |
| TxGNN-Vorhersage-Score | 99.99% |
| Evidence Level | L5 |
| Marktstatus Deutschland | Nicht zugelassen |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | Halten |

## Warum ist diese Vorhersage sinnvoll?

Detaillierte Wirkmechanismus-Daten für Lidocain sind in dem aktuellen DrugBank-Auszug nicht verfügbar (gekennzeichnet als Datenlücke DG002, hoher Schweregrad). Basierend auf allgemeinem pharmakologischen Wissen ist Lidocain ein Lokalanästhetikum der Amid-Klasse, das spannungsgesteuerte Natriumkanäle blockiert, um die Nervenleitung reversibel zu hemmen; es erzeugt Analgesie/Anästhesie, hat aber keine etablierte entzündungshemmende, antivirale oder immunmodulatorische Aktivität.

Punktförmige epitheliale Keratokonjunktivitis ist eine entzündliche/erosive Erkrankung des Kornea- und Bindehautepithels, typischerweise verursacht durch virale Infektion, chemische/UV-Verletzung oder immunvermittelte Prozesse. Eine Natriumkanal-Blockade kann Augenoberflächen-Schmerzen maskieren, behebt aber keinen dieser zugrunde liegenden Krankheitsmechanismen – es gibt keinen bekannten Weg, auf dem Lidocain den Verlauf dieser Erkrankung verändern würde.

Die vom Modell generierte Rationale für diese Vorhersage selbst kommt zu dem Ergebnis, dass der hohe TxGNN-Score höchstwahrscheinlich ein **semantisches Clustering-Artefakt** widerspiegelt: Lidocain erscheint häufig im Knowledge Graph neben Kontexten von „topischen ophthalmischen Arzneimitteln" (z. B. als Verfahrens-Anästhetikum bei Augenchirurgie und Injektionen), statt eine echte krankheitsmodifizierende mechanistische Beziehung widerzuspiegeln. Derzeit gibt es keine Literatur- oder Versuchsevidenz, um diese Hypothese zu testen.

## Evidenz aus klinischen Studien

Derzeit sind keine zugehörigen klinischen Studien registriert.

## Literaturevidence

Derzeit ist keine zugehörige Literatur verfügbar.

## Marktinformation Deutschland

Im aktuellen Datensatz sind keine Zulassungen vorhanden – Lidocain ist als **nicht zugelassen** verzeichnet (0 Lizenzen in den Unterlagen). Zulassungsdetails können nicht zusammengefasst werden, bis Zulassungsunterlagen hinzugefügt werden.

## Sicherheitserwägungen

Bitte beachten Sie die Packungsbeilage für Sicherheitsinformationen. (Wichtige Warnhinweise, Kontraindikationen und Wechselwirkungsdaten sind derzeit nicht verfügbar – Datenlücke DG001, blockierender Schweregrad, erfordert TFDA/BfArM-Etikett-Abruf, bevor eine Sicherheits-Vorprüfung abgeschlossen werden kann.)

## Fazit und nächste Schritte

**Entscheidung: Halten**

**Rationale:**
Diese Vorhersage hat Evidence Level L5 – ein TxGNN-Score ohne unterstützende klinische Studien oder Literatur – und die eigene Rationale des Modells identifiziert es als wahrscheinlich falsch-positiv, verursacht durch semantisches Clustering statt durch eine echte mechanistische Verbindung. Darüber hinaus bedeutet die Datenlücke im Label mit blockierendem Schweregrad (DG001), dass der Kandidat noch nicht einmal in die Sicherheits-Vorprüfung S1 eintreten kann.

**Um fortzufahren, ist Folgendes erforderlich:**
- Offizielle TFDA/BfArM-Packungsbeilage (Warnhinweise, Kontraindikationen) abrufen, um DG001 zu beheben
- Vollständige DrugBank-MOA-Daten abrufen, um DG002 zu beheben
- Unabhängige Literatur-/mechanistische Suche speziell zu Lidocain und epithelialer Heilung der Hornhaut/Bindehaut, da derzeit keine vorhanden ist
- Hinweis: Unter den top-10 vorhergesagten Indikationen dieses Kandidaten ist **atopische Konjunktivitis (Rang 5)** die einzige, die Entscheidungsstufe S1 mit einer „Forschungsfrage"-Empfehlung erreicht hat (L4, basierend auf einem plausiblen neuro-immunen Mechanismus – nasale/topische Anästhesie unterdrückt reflexvermittelte allergische Konjunktivitis-Reaktionen). Wenn weitere Arbeiten an diesem Arzneimittel durchgeführt werden, ist dieser Kandidat ein wesentlich stärkerer Ausgangspunkt als punktförmige epitheliale Keratokonjunktivitis.

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

