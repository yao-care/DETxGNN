---
layout: default
title: Romiplostim
parent: Nur Modellvorhersage (L5)
nav_order: 410
evidence_level: L5
indication_count: 10
---

# Romiplostim
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

# Romiplostim: Von idiopathischer thrombozytopenischer Purpura zu primärer Freisetzungsstörung der Thrombozyten

## Zusammenfassung

Romiplostim (Handelsname Nplate) wurde ursprünglich zur Behandlung der idiopathischen thrombozytopenischen Purpura (ITP) zugelassen. Das TxGNN-Modell sagt voraus, dass es bei der **primären Freisetzungsstörung der Thrombozyten** wirksam sein könnte. Für diese Vorhersage liegen **keine klinischen Studien** und **nur 1 Publikation** vor, die zudem die ITP und nicht die vorhergesagte Indikation betrifft. Die Vorhersage beruht daher im Wesentlichen auf einer Modellrechnung.

---

## Schnellübersicht

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Idiopathische thrombozytopenische Purpura |
| Vorhergesagte neue Indikation | Primäre Freisetzungsstörung der Thrombozyten |
| TxGNN-Vorhersagewert | 99,99 % |
| Evidenzstufe | L5 |
| Marktstatus in Deutschland | Nur erloschene/widerrufene Zulassung (nicht mehr vermarktet) |
| Anzahl der Zulassungen | 1 (0 gültig, 1 erloschen) |
| Empfohlene Entscheidung | Hold |

---

## Warum ist diese Vorhersage plausibel?

Daten zum Wirkmechanismus liegen im für diesen Bericht zusammengestellten Datenbestand nicht vor. Aus der Pharmakologiedatenbank ist jedoch bekannt, dass Romiplostim ein Peptid ist, das den Thrombopoietin-Rezeptor (MPL) aktiviert und dadurch die Thrombozytenproduktion steigert. Seine Wirksamkeit bei ITP ist belegt.

Bei der vorhergesagten Indikation ist die mechanistische Verbindung jedoch **schwach**. Primäre Freisetzungsstörungen sind qualitative Funktionsdefekte der Thrombozyten (gestörte Granulafreisetzung). Eine Erhöhung der Thrombozytenzahl behebt diesen Defekt nicht. Die einzige gefundene Publikation (PMID 25682608) befasst sich mit ITP und zeigt, dass Autoantikörper die Bildung von Proplättchen hemmen. Sie stützt die ITP-Begründung, nicht die vorhergesagte Indikation. Der hohe TxGNN-Wert spiegelt wahrscheinlich die Nähe zur ITP im Wissensgraphen wider.

Unter den weiteren Vorhersagen ist die **fetale und neonatale alloimmune Thrombozytopenie (FNAIT)** (Rang 4, Wert 99,99 %, Evidenzstufe L4) mechanistisch am plausibelsten. Sie ist eine immunvermittelte Thrombozytopenie mit Nähe zur ITP, und thrombopoetische Substanzen wurden für die neonatale Anwendung diskutiert. Sie ist als Forschungsfrage einzustufen. Plazentagängigkeit, fetale Sicherheit und neonatale Dosierung sind ungeklärt. Außerdem kommen ein genotypabhängiges Ansprechen bei angeborenen Thrombozytopenien (Rang 6 und 9) als mögliche, aber unbewiesene Ansätze in Betracht.

---

## Evidenz aus klinischen Studien

Derzeit sind keine zugehörigen klinischen Studien registriert.

---

## Literaturevidenz

| PMID | Jahr | Typ | Journal | Kernaussagen |
|------|-----|------|------|---------|
| [25682608](https://pubmed.ncbi.nlm.nih.gov/25682608/) | 2015 | Grundlagen-/Mechanismusstudie | Haematologica | Antithrombozytäre Autoantikörper bei ITP hemmen die Proplättchenbildung der Megakaryozyten und beeinträchtigen die Thrombozytenproduktion in vitro. Betrifft ITP, nicht die vorhergesagte Indikation. |

Für die Vorhersage FNAIT liegen zusätzlich Übersichtsarbeiten und Fallberichte zu ITP vor (z. B. [31239245](https://pubmed.ncbi.nlm.nih.gov/31239245/), [20410910](https://pubmed.ncbi.nlm.nih.gov/20410910/), [34711622](https://pubmed.ncbi.nlm.nih.gov/34711622/)). Sie betreffen überwiegend pädiatrische oder schwangerschaftsbezogene ITP, nicht FNAIT selbst.

---

## Informationen zum deutschen Markt

| Zulassungsnummer | Produktname | Darreichungsform | Zugelassene Indikation |
|---------|------|------|-----------|
| EMEA/H/C/000942 | Nplate | – | Idiopathische thrombozytopenische Purpura (Status: erloschen) |

---

## Sicherheitsaspekte

- **Arzneimittelwechselwirkungen:** Es wurde eine Wechselwirkung mit Schweregrad **Major** gefunden: **Carfilzomib** (Quelle: DDInter).
- **Zielstruktur:** Romiplostim wirkt am Thrombopoietin-Rezeptor (MPL). Bei Erkrankungen mit hyperreaktiven Thrombozyten, etwa der Pseudo-von-Willebrand-Erkrankung, könnte eine Erhöhung der Thrombozytenzahl nachteilig sein.

Weitere Sicherheitsinformationen entnehmen Sie bitte der Fachinformation.

---

## Fazit und nächste Schritte

**Entscheidung: Hold**

**Begründung:**
Für die vorhergesagte Indikation gibt es weder klinische Studien noch direkt relevante Literatur (Evidenzstufe L5), und die mechanistische Verbindung ist schwach: Eine höhere Thrombozytenzahl behebt keinen qualitativen Funktionsdefekt. Zudem besteht in Deutschland keine gültige Zulassung mehr.

**Für ein Weiterkommen sind erforderlich:**
- Daten zum Wirkmechanismus (MOA) aus DrugBank
- Warnhinweise und Gegenanzeigen aus der Fachinformation (BfArM), da diese Lücke eine Sicherheitsbewertung blockiert
- Prüfung der Vorhersage zu FNAIT als vorrangige Forschungsfrage, einschließlich Studien zu Plazentagängigkeit, fetaler Sicherheit und neonataler Dosierung
- Klärung des Zulassungsstatus in Deutschland, da die einzige Zulassung erloschen ist
## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

