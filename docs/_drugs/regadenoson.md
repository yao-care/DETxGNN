---
layout: default
title: Regadenoson
parent: Nur Modellvorhersage (L5)
nav_order: 387
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-28
description: "Regadenoson: vorhergesagte neue Indikation Anaphylaxie (Evidenzstufe L5). Ursprüngliche Indikation: Myokardperfusionsbildgebung"
monitor_inn: "REGADENOSON"
predicted_indications: ["anaphylaxis", "food-dependent exercise-induced anaphylaxis", "esotropia", "pseudoallergy"]
---

# Regadenoson
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **4** 
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

## Regadenoson: Von der Myokardperfusionsbildgebung zur Anaphylaxie
{: .text-alpha }

## Zusammenfassung

Regadenoson ist ein selektiver A2A-Adenosinrezeptor-Agonist und wird als diagnostisches Mittel für die Myokardperfusionsbildgebung (MPI) eingesetzt.
Das TxGNN-Modell sagt voraus, dass es bei **Anaphylaxie** wirksam sein könnte.
Für diese Richtung liegen derzeit **keine klinischen Studien** und **keine Publikationen** vor, die Vorhersage beruht allein auf dem Modell.

---

## Schnellübersicht

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Myokardperfusionsbildgebung |
| Vorhergesagte neue Indikation | Anaphylaxie |
| TxGNN-Vorhersagewert | 0,9985 |
| Evidenzstufe | L5 |
| Marktstatus in Deutschland | Im Handel (gültige Zulassungen: 1 von 1) |
| Anzahl der Zulassungen | 1 (gültig: 1) |
| Empfohlene Entscheidung | Hold |

---

## Warum ist diese Vorhersage plausibel?

Zum Wirkmechanismus liegen in den für diesen Bericht zusammengestellten Daten keine detaillierten Angaben vor. Nach allgemeinem pharmakologischem Wissen ist Regadenoson ein selektiver Agonist des A2A-Adenosinrezeptors. Die Pharmakologiedaten zeigen zudem Bindung an die Rezeptoren A1, A2B und A3.

Ein theoretischer Zusammenhang mit der Anaphylaxie ergibt sich daraus, dass die A2A-Aktivierung auf Mastzellen und anderen Immunzellen die Freisetzung von Entzündungsmediatoren dämpfen kann. Die Adenosin-Signalwege sind jedoch komplex: A2B- und A3-Rezeptoren können die Mastzell-Degranulation sogar fördern. Außerdem tragen Regadenoson-Produkte selbst Warnhinweise zu Überempfindlichkeit und Anaphylaxie als Nebenwirkung. Der hohe Vorhersagewert könnte daher eher das Nebenwirkungsprofil als einen therapeutischen Effekt widerspiegeln.

Regadenoson ist zudem eine kurz wirksame Einzeldosis-Diagnostik und eignet sich wenig zur Vorbeugung episodischer, auslöserabhängiger Ereignisse. Der Zusammenhang zur ursprünglichen Indikation (Bildgebung) ist rein pharmakologisch-hypothetisch.

**Weitere vorhergesagte Indikationen** (alle L5, ohne Studien oder Literatur, Empfehlung jeweils Hold):

| Rang | Erkrankung | TxGNN-Wert | Einschätzung |
|------|------|------|------|
| 2 | Nahrungsabhängige belastungsinduzierte Anaphylaxie | 0,9974 | Gleiche theoretische A2A-Mastzell-Hypothese. Der Wert ist vermutlich durch die Ähnlichkeit zum übergeordneten Begriff Anaphylaxie erhöht. |
| 3 | Esotropie | 0,9912 | Kein plausibler Mechanismus erkennbar. Der Score stammt vom TxGNN-Modell (Deep Learning) und kann vom Modell gelernte Ähnlichkeiten zwischen verwandten Erkrankungen widerspiegeln, nicht biologische Evidenz. |
| 4 | Pseudoallergie | 0,9912 | Spekulativ, da die Richtung der Wirkung auf Mastzellen unsicher ist. |

---

## Evidenz aus klinischen Studien

Derzeit sind keine zugehörigen klinischen Studien registriert.

---

## Evidenz aus der Literatur

Derzeit liegt keine zugehörige Literatur vor.

---

## Informationen zum Markt in Deutschland

| Zulassungsnummer | Produktname | Darreichungsform | Zugelassene Indikation |
|---------|------|------|-----------|
| EMEA/H/C/001176 | Rapiscan (GE Healthcare AS) | – | Myokardperfusionsbildgebung |

Diese Zulassung ist gültig. Derzeit ist in den Daten 1 von 1 Zulassung gültig.

---

## Sicherheitshinweise

- **Kontraindikationen laut Wissensgraph** (aus Arzneimittel-Krankheits-Beziehungen des TxGNN-Wissensgraphen, nicht aus Packungsbeilagen): Dazu zählen unter anderem
  - Atemwegserkrankungen: Asthma (einschließlich allergisches und intrinsisches Asthma), COPD, Bronchialerkrankungen;
  - Erregungsleitungsstörungen: AV-Block, Sick-Sinus-Syndrom;
  - Herzklappen und Perikard: Aortenstenose, Mitralklappenstenose, Perikarditis, Perikarderguss;
  - Gefäß- und Durchblutungsstörungen: koronare Herzkrankheit, Karotisstenose, transitorische ischämische Attacke, vertebrobasiläre Insuffizienz;
  - Blutdruck: Hypertonie, Hypotonie;
  - Weitere: Epilepsie, Erkrankungen des autonomen Nervensystems, Horner-Syndrom.
- **Wechselwirkungen** (10 Einträge, davon 6 mit Schweregrad „mäßig"): Coffein, Dipyridamol, Dyphyllin, Theophyllin, Aminophyllin und Oxtriphyllin. Methylxanthine wie Coffein und Theophyllin sind Adenosinrezeptor-Antagonisten und können die Wirkung von Regadenoson abschwächen. Dipyridamol kann die Adenosinwirkung verstärken. Weitere Einträge betreffen die Bindung an die Adenosinrezeptoren A1, A2A, A2B und A3.
- Für Anaphylaxie und Überempfindlichkeit als Nebenwirkung des Arzneimittels liegen Hinweise vor (siehe oben). Weitere Angaben zu Warnhinweisen und Kontraindikationen aus der Packungsbeilage sind nicht verfügbar. Bitte die Fachinformation heranziehen.

---

## Fazit und nächste Schritte

**Entscheidung: Hold**

**Begründung:**
Die Vorhersagen beruhen ausschließlich auf dem Modell (L5), ohne klinische Studien oder Publikationen. Der Wirkmechanismus ist bei Anaphylaxie widersprüchlich (A2A schützend, A2B/A3 fördernd), und das Arzneimittel selbst kann Anaphylaxie auslösen. Zudem ist das Arzneimittel in Deutschland derzeit mit einer gültigen Zulassung im Handel.

**Für ein Weiterkommen ist Folgendes erforderlich:**
- Daten zum Wirkmechanismus (MOA) aus DrugBank
- Warnhinweise und Kontraindikationen aus der Packungsbeilage von BfArM bzw. EMA (blockierend für die Sicherheitsprüfung)
- Prüfung, ob die Vorhersage lediglich das Nebenwirkungsprofil abbildet
- Präklinische Daten zur Wirkung von A2A-Agonisten auf Mastzellen und in Anaphylaxie-Modellen
- Klärung der Eignung von Darreichungsweg und Einzeldosis-Anwendung für die vorgeschlagene Indikation
- Klärung des Zulassungsstatus und der Verfügbarkeit in Deutschland
## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

