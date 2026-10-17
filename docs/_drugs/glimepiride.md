---
layout: default
title: Glimepiride
parent: Nur Modellvorhersage (L5)
nav_order: 212
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-14
description: "Glimepiride: vorhergesagte neue Indikation Fokales Stiff-Limb-Syndrom (Evidenzstufe L5). Ursprüngliche Indikation: Diabetes mellitus Typ 2"
monitor_inn: "GLIMEPIRIDE"
predicted_indications: ["focal stiff limb syndrome", "classic stiff person syndrome", "opsismodysplasia", "thiamine-responsive dysfunction syndrome", "drug-induced localized lipodystrophy", "centrifugal lipodystrophy", "pressure-induced localized lipoatrophy", "idiopathic localized lipodystrophy", "pancreatic agenesis"]
---

# Glimepiride
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **9** 
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

# Glimepirid: Von Diabetes mellitus Typ 2 zum Stiff-Limb-Syndrom (fokal)

## Zusammenfassung

Glimepirid ist ein Sulfonylharnstoff, der ursprünglich zur Behandlung von Diabetes mellitus Typ 2 eingesetzt wird.
Das TxGNN-Modell sagt voraus, dass es bei **fokalem Stiff-Limb-Syndrom** wirksam sein könnte.
Dafür liegen jedoch **keine klinischen Studien** und **keine Publikationen** vor. Die Vorhersage beruht ausschließlich auf einer Modellberechnung.

---

## Kurzüberblick

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Diabetes mellitus Typ 2 |
| Vorhergesagte neue Indikation | Fokales Stiff-Limb-Syndrom |
| TxGNN-Vorhersagewert | 99,75 % |
| Evidenzgrad | L5 |
| Marktstatus in Deutschland | Nur erloschene/aufgehobene Zulassung |
| Anzahl der Zulassungen | 1 (erloschen) |
| Empfohlene Entscheidung | Hold |

---

## Warum ist diese Vorhersage plausibel (oder nicht)?

Zum Wirkmechanismus von Glimepirid liegen in den für diesen Bericht zusammengestellten Daten keine detaillierten Angaben vor. Bekannt ist, dass Glimepirid zu den Sulfonylharnstoffen gehört: Es schließt die ATP-sensitiven Kaliumkanäle (KATP) der Betazellen der Bauchspeicheldrüse und fördert so die Insulinfreisetzung. Zusätzlich werden moderate extrapankreatische Effekte auf die Insulinempfindlichkeit beschrieben.

Das Stiff-Limb-Syndrom gehört zum Spektrum der Stiff-Person-Erkrankungen. Diese sind häufig autoimmun bedingt (Anti-GAD65-Antikörper) und treten gehäuft gemeinsam mit Diabetes auf. Die hohe Vorhersage spiegelt vermutlich dieses Komorbiditätsnetzwerk wider und nicht einen therapeutischen Effekt.

Ein mechanistischer Zusammenhang ist nicht erkennbar: Die Steifigkeit entsteht über GABAerge und glycinerge Signalwege, auf die Glimepirid nach bisherigem Wissen keinen Einfluss hat. Die Standardtherapie (Benzodiazepine, Baclofen, IVIG) setzt an diesen Mechanismen bzw. am Immunsystem an.

**Weitere vorhergesagte Indikationen (alle Evidenzgrad L5, Entscheidung Hold):**

| Rang | Erkrankung | Score | Einschätzung |
|---|---|---|---|
| 2 | Klassisches Stiff-Person-Syndrom | 99,75 % | Wahrscheinlich Artefakt der Diabetes-/GAD65-Assoziation; kein Mechanismus für Glimepirid |
| 3 | Opsismodysplasie | 99,74 % | Spekulativer, indirekter Bezug über den PI3K-/Insulin-Signalweg (INPPL1/SHIP2); rein hypothetisch |
| 4 | Thiamin-responsives Dysfunktionssyndrom | 99,73 % | Sulfonylharnstoffe könnten allenfalls den diabetischen Anteil symptomatisch behandeln; Thiamin bleibt Standardtherapie |
| 5 | Arzneimittelinduzierte lokalisierte Lipodystrophie | 99,62 % | Kein bekanntes Ziel von Sulfonylharnstoffen; rein graphbasiert |
| 6 | Zentrifugale Lipodystrophie | 99,60 % | Kein etablierter Mechanismus |
| 7 | Druckinduzierte lokalisierte Lipoatrophie | 99,59 % | Kein direkter pharmakologischer Ansatz |
| 8 | Idiopathische lokalisierte Lipodystrophie | 99,56 % | Ätiologie unbekannt, rein spekulativ |
| 9 | Pankreasagenesie | 99,55 % | Mechanistisch unplausibel: Ohne funktionierende Betazellen ist ein Sekretagogum wirkungslos |

---

## Klinische Studien

Derzeit sind keine zugehörigen klinischen Studien registriert.

---

## Literaturevidenz

Für die Hauptvorhersage (fokales Stiff-Limb-Syndrom) liegen derzeit keine zugehörigen Publikationen vor.

Für die Vorhersage mit Rang 9 (Pankreasagenesie) wurde eine Arbeit gefunden, die jedoch nicht zum Thema passt:

| PMID | Jahr | Typ | Journal | Kernaussage |
|------|-----|------|------|---------|
| [12720536](https://pubmed.ncbi.nlm.nih.gov/12720536/) | 2003 | Review | European Journal of Endocrinology | Fallstricke der endosonographischen Bildgebung bei vermuteten Insulinomen; weder Pankreasagenesie noch Glimepirid werden behandelt |

---

## Marktinformationen Deutschland

| Zulassungsnummer | Produktname | Darreichungsform | Zugelassene Indikation |
|---------|------|------|-----------|
| EMEA/H/C/000680 | Tandemact (CHEPLAPHARM Arzneimittel GmbH) | – | Diabetes mellitus Typ 2 |

Diese Zulassung ist erloschen bzw. aufgehoben.

---

## Sicherheitshinweise

**Kontraindikationen aus dem Wissensgraphen (PrimeKG, keine Packungsbeilagen-Angaben):**
Im Wissensgraphen sind unter anderem folgende Erkrankungen als Gegenanzeigen verknüpft:
- Nieren- und Lebererkrankungen
- Gallenblasenerkrankungen
- Herzinsuffizienz
- Hypophysenunterfunktion (inkl. Wachstumshormonmangel, Kallmann-Syndrom, Sheehan-Syndrom, hypogonadotroper Hypogonadismus)
- Thymuserkrankungen
- Osteoporose (inkl. postmenopausale Osteoporose)
- Infektionskrankheiten

**Arzneimittelwechselwirkungen:** Es wurden 100 Wechselwirkungen erfasst, die meisten mit Schweregrad „moderat". Beispiele:
- Beta-Agonisten bzw. Sympathomimetika: Salbutamol, Formoterol, Epinephrin, Phenylephrin, Pseudoephedrin
- Betablocker: Acebutolol
- Entzündungshemmer: Ibuprofen, Ketorolac, Hydrocortisone
- Magensäureblocker: Famotidin, Ranitidin
- Weitere: Acetazolamid, Acitretin, Ethinylestradiol, Hydrochlorothiazid, Nitazoxanid, Albiglutid, Ethanol

Geringfügige Wechselwirkungen bestehen u. a. mit topischem Hydrocortison und topischem Alclometason.

Angaben aus der Packungsbeilage (Warnhinweise, Gegenanzeigen) sind nicht verfügbar; bitte die Fachinformation heranziehen.

---

## Fazit und nächste Schritte

**Entscheidung: Hold**

**Begründung:**
Die Vorhersage beruht allein auf einer Modellberechnung (Evidenzgrad L5). Es gibt weder Studien noch Literatur, und ein pharmakologischer Zusammenhang zwischen dem KATP-Kanal-Mechanismus von Glimepirid und der GABAergen/autoimmunen Pathophysiologie des Stiff-Limb-Syndroms ist nicht erkennbar. Zudem besteht in Deutschland derzeit keine gültige Zulassung.

**Für ein Weiterverfolgen wären erforderlich:**
- Systematische Literaturrecherche zu Sulfonylharnstoffen bei Stiff-Person-Spektrum-Erkrankungen
- Detaillierte Wirkmechanismus-Daten (MOA) aus DrugBank
- Auswertung der Fachinformation (Warnhinweise, Gegenanzeigen) vom BfArM; derzeit blockiert die fehlende Sicherheitsgrundlage die weitere Sicherheitsprüfung
- Klärung des Zulassungsstatus in Deutschland
- Präklinische Belege für einen plausiblen Mechanismus, bevor klinische Studien erwogen werden
## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

