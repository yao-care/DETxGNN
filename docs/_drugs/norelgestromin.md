---
layout: default
title: Norelgestromin
parent: Nur Modellvorhersage (L5)
nav_order: 274
evidence_level: L5
indication_count: 1
---

# Norelgestromin
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

# Norelgestromin: Von der Empfängnisverhütung zur Amenorrhö

## Zusammenfassung in einem Satz

Norelgestromin ist der aktive Metabolit von Norgestimate, einem Progestin der dritten Generation, das als Gestagen-Komponente eines kombinierten transdermalen Kontrazeptivums verwendet wird. Das TxGNN-Modell prognostiziert eine mögliche neue Indikation **Amenorrhö**, die jedoch derzeit durch **null klinische Studien** und **null Publikationen** gestützt wird – und die bereitgestellte Begründung selbst kennzeichnet die Vorhersage als wahrscheinliches Artefakt reverser Kausalität, da Amenorrhö eine dokumentierte *Nebenwirkung* dieses Arzneimittels ist und keine Erkrankung, deren Behandlung bekannt wäre.

---

## Schnellübersicht

| Element | Inhalt |
|---------|--------|
| Original-Indikation | Nicht in diesem Evidence Pack enthalten (keine zugelassene Produktlizenz gefunden); das Arzneimittel wird klinisch als Komponente eines kombinierten transdermalen Kontrazeptivums verwendet |
| Prognostizierte neue Indikation | Amenorrhö |
| TxGNN-Vorhersage-Score | 99.51% |
| Evidence Level | L5 |
| Marktstatus Deutschland | Nicht vermarktet |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | Zurückhalten |

---

## Warum ist diese Vorhersage sinnvoll?

Norelgestromin ist der aktive Metabolit von Norgestimate und wirkt als Progestin der dritten Generation. Klinisch wird es als Komponente eines kombinierten transdermalen Kontrazeptivums eingesetzt, wo es die Gonadotropin-Sekretion unterdrückt, den Eisprung hemmt und das Endometrium verändert, um eine Schwangerschaft zu verhindern. Ein formal strukturiertes Wirkmechanismus-Datensatz aus DrugBank war in diesem Evidence Pack nicht verfügbar; die obige Beschreibung leitet sich aus der bekannten Pharmakologieklasse des Arzneimittels und der die Vorhersage begleitenden Begründung ab.

Die prognostizierte neue Indikation – Amenorrhö – ist mit Norelgestromin nur durch sein **bereits etabliertes Nebenwirkungsprofil** mechanistisch verbunden. Amenorrhö (ausbleibende oder verpasste Entzugsblutung) ist ein häufig angegebener Grund dafür, dass Patientinnen kombinierte hormonelle Kontrazeptiva, einschließlich des Norelgestromin/Ethinylestradiol-Pflasters, absetzen. Es gibt keinen bekannten Mechanismus, durch den Norelgestromin *therapeutisch* zur Behandlung von Amenorrhö verwendet würde; ein Progestin, das die hypothalamisch-hypophysär-ovarielle Achse unterdrückt und das Endometrium verdünnt, ist pharmakologisch weit mehr damit konsistent, Amenorrhö zu *verursachen*, als sie zu korrigieren.

Aus diesem Grund kennzeichnet das Evidence Pack selbst diese Vorhersage als wahrscheinliches Artefakt **reverser Kausalität**: TxGNN kann wie andere Knowledge-Graph-Modelle eine Arzneimittel–Nebenereignis-Kante („Norelgestromin verursacht Amenorrhö") fälschlicherweise als Arzneimittel–Indikations-Kante („Norelgestromin behandelt Amenorrhö") erlernen – ein bekannter Fallstrick bei Progestinen, bei denen Amenorrhö stark in Pharmakovigilanz-Daten kodiert ist. Der hohe TxGNN-Score (99.51%) sollte daher nicht als Bestätigung der therapeutischen Plausibilität gelesen werden; er spiegelt eher die Stärke der Arzneimittel–Amenorrhö-Assoziation wider, die durch Nebenwirkungsberichte angetrieben wird, als dass er ein echtes Behandlungssignal anzeigt.

---

## Klinische Studienevidenz

Derzeit sind keine zugehörigen klinischen Studien registriert.

---

## Literaturevidenz

Derzeit ist keine zugehörige Literatur verfügbar.

---

## Informationen zum Marktstatus Deutschland

Norelgestromin verfügt derzeit über keine archivierte Marktzulassung (Marktstatus: **Nicht vermarktet**, 0 Zulassungen). Keine Produktnamen-, Darreichungsform- oder zugelassenen Indikationsdaten sind in diesem Evidence Pack verfügbar.

---

## Sicherheitsaspekte

Bitte beachten Sie die Fachinformation für Sicherheitsinformationen.

---

## Fazit und nächste Schritte

**Entscheidung: Zurückhalten**

**Begründung:**
- Die Evidence Level ist L5 (nur Modellvorhersage, keine klinischen Studien oder Literatur), und das Entscheidungsstadium ist S0 – das früheste mögliche Stadium, ohne dass eine Sicherheits-Vorprüfung abgeschlossen wurde.
- Die mechanistische Begründung selbst deutet darauf hin, dass diese Vorhersage wahrscheinlicher ein Artefakt reverser Kausalität ist (Amenorrhö ist eine bekannte Nebenwirkung von Norelgestromin, kein plausibler Behandlungszielbereich) als ein echtes Repurposing-Signal.

**Um fortzufahren, ist folgendes erforderlich:**
- TFDA/BfArM-Fachinformationsdaten (Warnhinweise und Kontraindikationen) – derzeit eine **Blocking**-Datenlücke (DG001), erforderlich bevor irgendwelche S1-Sicherheits-Vorprüfungen beginnen können
- Bestätigter Wirkmechanismus aus der DrugBank-API – derzeit eine Datenlücke mit **hohem** Schweregrad (DG002)
- Eine unabhängige Pharmakovigilanz-/Literaturübersicht, um die Hypothese reverser Kausalität explizit zu testen und entweder zu bestätigen oder zu widerlegen, bevor weitere Bewertungen erfolgen
- Falls die Hypothese reverser Kausalität nicht gelöst wird, sollte dieser Kandidat eher als deprioritiert angesehen werden, als dass er über S0 hinaus vorgebracht wird

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

