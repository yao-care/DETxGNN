---
layout: default
title: Dibotermin Alfa
parent: Nur Modellvorhersage (L5)
nav_order: 123
evidence_level: L5
indication_count: 9
---

# Dibotermin Alfa
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **9** 
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

# Dibotermin Alfa: Von Knochenregeneration zu Esotropie

## Zusammenfassung in einem Satz

> Dibotermin alfa (rekombinantes humanes BMP-2) ist ein knocheninduktiver Wachstumsfaktor, der bei Wirbelsäulenfusionen und offenen Tibiafrakturen verwendet wird.
> Die beste Vorhersage des TxGNN-Modells ist **Esotropie**, aber dieser Kandidat wird von **null klinischen Versuchen** und **null Publikationen** gestützt,
> und das Informationspaket des Arzneimittels selbst vermerkt explizit, dass es keine bekannte biologische Verbindung zwischen BMP-2-Signalisierung und Störungen der extraokularen Muskulatur gibt.

---

## Schnellübersicht

| Punkt | Inhalt |
|------|--------|
| Ursprüngliche Indikation | Knochenregeneration (Wirbelsäulenfusion / offene Tibiafraktur) — abgeleitet aus mechanistischer Begründung; nicht separat bestätigt in diesem Informationspaket |
| Vorhergesagte neue Indikation | Esotropie |
| TxGNN-Vorhersage-Score | 99.97% |
| Evidenzstufe | L5 (nur Modellvorhersage, keine unterstützenden Studien) |
| Marktstatus Deutschland | ✗ Nicht vermarktet |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | Zurückhalten |

---

## Warum ist diese Vorhersage sinnvoll?

Derzeit sind detaillierte Daten zum Wirkmechanismus in diesem Informationspaket nicht verfügbar (original_moa = Datenlücke). Basierend auf anderen Informationen im Paket ist Dibotermin alfa rekombinantes humanes BMP-2 (rhBMP-2), ein Wachstumsfaktor, dessen bekannte biologische Wirkung die Induktion osteogener Differenzierung ist; es wird klinisch bei Wirbelsäulenfusionen und bei der Knochenregeneration offener Tibiafrakturen verwendet.

Esotropie ist eine neuromuskuläre Kontrollstörung der extraokularen Muskulatur. Es gibt keine bekannte mechanistische Verbindung zwischen BMP-2-osteoinduktiver Signalisierung und Ausrichtung oder neuromuskulärer Kontrolle der extraokularen Muskulatur. Das Informationspaket selbst besagt in seiner Begründung explizit, dass dieser Kandidat „keine biologische Plausibilität" hat und einen reinen Netzwerk-Assoziations-Artefakt des TxGNN-Modells darstellt, anstatt eine fundierte Umwidmungshypothese zu sein.

Da es keine mechanistische Verbindung, keine abgeschlossenen oder laufenden klinischen Versuche und keine Literatur gibt, sollte diese Vorhersage als ein **Signal mit niedriger Konfidenz, das unabhängige biologische Validierung erfordert**, nicht als eine umsetzbare Umwidmungsmöglichkeit behandelt werden.

---

## Evidenz aus klinischen Versuchen

Derzeit sind keine damit verbundenen klinischen Versuche registriert.

---

## Evidenz aus der Literatur

Derzeit ist keine damit verbundene Literatur verfügbar.

---

## Informationen zum Marktstatus Deutschland

Dibotermin alfa hält derzeit keine Zulassung in Deutschland (0 Lizenzen in den Unterlagen); das Arzneimittel wird in diesem Markt nicht vermarktet.

---

## Sicherheitsüberlegungen

Bitte beachten Sie die Packungsbeilage für Sicherheitsinformationen.

---

## Zusätzliche Anmerkung: Weitere überprüfte Vorhersage-Indikationen

Acht weitere TxGNN-vorhergesagte Indikationen wurden neben Esotropie überprüft (Ränge 2–9), alle mit L5 / Zurückhalten bewertet, ohne unterstützende klinische Versuche. Folgende zwei Punkte verdienen besondere Aufmerksamkeit von Entscheidungsträgern:

- **HER2-positives Mammakarzinom und damit verbundene Brustkrebssubtypen (Ränge 2, 3, 4, 6)**: Literatur über BMP-2-Signalisierung in Brusttumor-Biologie deutet generell auf Tumorförderung (Proliferation, EMT, Knochenmetastasen) hin, nicht auf eine therapeutische Wirkung. Diese sollten als ein **mögliches Sicherheitssignal** interpretiert werden, nicht als Umwidmungsmöglichkeit.
- **„Brusttumor luminal A oder B" (Rang 5)**: Die 19 Literaturquellen, die diesem Kandidaten zugeordnet sind, sind ein **Datenqualitäts-Artefakt** — sie betreffen B-Zell-Immunologie und Hepatitis-B-Impfstoffe, offensichtlich durch das Schlüsselwort „B" fehlerhaft zugeordnet und ohne Bezug zu Brustkrebs oder BMP-2. Dies sollte aus jeder Evidenzzählung ausgeschlossen werden.

---

## Schlussfolgerung und nächste Schritte

**Entscheidung: Zurückhalten**

**Begründung:**
Der höchstplatzierte Kandidat (Esotropie) hat keine klinischen, Literatur- oder mechanistischen Belege, und das Informationspaket selbst vermerkt, dass es keine biologische Plausibilität gibt. Kein Kandidat in der Gesamtheit der Vorhersagen erreicht auch nur L3-Evidenz, und zwei Kandidaten weisen ein mögliches Sicherheitssignal (pro-tumorigene BMP-2-Aktivität bei Brustkrebs) auf, statt einer therapeutischen Begründung.

**Um weiterzukommen, ist das Folgende erforderlich:**
- Auflösung der blockierenden Datenlücke DG001 (TFDA/BfArM-Warnhinweise und -Kontraindikationen), bevor ein S1-Sicherheits-Screening durchgeführt werden kann
- Auflösung von DG002 (bestätigter Wirkmechanismus) zur angemessenen Bewertung der mechanistischen Plausibilität
- Unabhängige, zielgerichtete Literaturrecherche für BMP-2 und die Biologie der extraokularen Muskulatur und des Strabismus (bisherige Literatursuche ergab keine relevanten Treffer)
- Falls das Brustkrebssignal weiter untersucht wird, sollte es als **Risikobewertung** (verschlechtert BMP-2-Exposition die Ergebnisse bei Brustkrebs) behandelt werden, nicht als Umwidmungsmöglichkeit
- Da das Arzneimittel in Deutschland nicht vermarktet wird und für keinen Kandidaten klinische Belege vorhanden sind, werden derzeit keine weiteren Maßnahmen empfohlen, außer der Überwachung neuer Literatur und klinischer Versuche

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

