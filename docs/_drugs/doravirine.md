---
layout: default
title: Doravirine
parent: Nur Modellvorhersage (L5)
nav_order: 149
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-14
description: "Doravirine: vorhergesagte neue Indikation Felines erworbenes Immundefizienzsyndrom (Evidenzstufe L5). Ursprüngliche Indikation: HIV-Infektionen"
monitor_inn: "DORAVIRINE"
predicted_indications: ["feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter"]
---

# Doravirine
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **3** 
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

# Doravirin: Von HIV-Infektion zu felinem erworbenem Immundefizienzsyndrom

## Zusammenfassung in einem Satz

Doravirin ist ein nicht-nukleosidischer Reverse-Transkriptase-Inhibitor (NNRTI), der ursprünglich zur Behandlung von HIV-Infektionen zugelassen wurde. Das TxGNN-Modell sagt voraus, dass er bei **felinem erworbenem Immundefizienzsyndrom** wirksam sein könnte. Für diese Vorhersage liegen jedoch **keine klinischen Studien** und **keine Publikationen** vor, die Doravirin direkt betreffen; die Evidenz beschränkt sich auf die Modellvorhersage.

---

## Schnellübersicht

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | HIV-Infektionen |
| Vorhergesagte neue Indikation | Felines erworbenes Immundefizienzsyndrom |
| TxGNN-Vorhersagewert | 99,93 % |
| Evidenzniveau | L5 |
| Marktstatus in Deutschland | Nur erloschene/zurückgezogene Zulassungen |
| Anzahl der Zulassungen | 2 (beide erloschen) |
| Empfohlene Entscheidung | Hold |

---

## Warum ist diese Vorhersage plausibel?

Zum Wirkmechanismus von Doravirin liegen in den für diesen Bericht zusammengestellten Daten keine detaillierten Angaben vor. Bekannt ist, dass Doravirin ein NNRTI ist, der die Reverse Transkriptase von HIV-1 hemmt. Seine Wirksamkeit bei HIV-Infektionen ist belegt.

Das feline Immundefizienzvirus (FIV) ist ein Lentivirus und mit HIV verwandt. Daher besteht prinzipiell eine mechanistische Begründung. Allerdings wirken NNRTIs gegen FIV im Allgemeinen schlecht, weil sich die Reverse Transkriptase von FIV in der NNRTI-Bindungstasche von der von HIV-1 unterscheidet. Der hohe TxGNN-Wert spiegelt vermutlich die Nähe zum HIV-Krankheitsknoten im Netzwerk wider und nicht eine nachgewiesene Aktivität.

Zwei weitere Vorhersagen mit gleichem oder ähnlichem Score sind ebenfalls wenig belastbar:
- **Infektion mit dem Affen-Immundefizienzvirus (SIV):** SIV, insbesondere SIVmac, ist natürlicherweise gegen viele NNRTIs resistent. Die einzige verknüpfte Publikation betrifft Islatravir, nicht Doravirin. Zudem handelt es sich um einen Tiermodellkontext, nicht um ein humanes Therapieziel.
- **Neuroentwicklungsstörung mit ataktischem Gang, fehlender Sprache und verminderter kortikaler weißer Substanz:** Es wurde kein plausibler mechanistischer Zusammenhang gefunden. Vermutlich handelt es sich um ein Artefakt der graphbasierten Vorhersage.

---

## Evidenz aus klinischen Studien

Derzeit sind keine zugehörigen klinischen Studien registriert.

---

## Evidenz aus der Literatur

Für die Top-Vorhersage (felines erworbenes Immundefizienzsyndrom) liegen derzeit keine zugehörigen Publikationen vor.

Hinweis zur zweitplatzierten Vorhersage (SIV-Infektion): Die einzige verknüpfte Publikation ist ein Übersichtsartikel zu Islatravir, einem anderen Wirkstoff, und liefert keine Doravirin-spezifische Evidenz.

| PMID | Jahr | Typ | Journal | Kernaussagen |
|------|-----|------|------|---------|
| [31658118](https://pubmed.ncbi.nlm.nih.gov/31658118/) | 2020 | Review | Current Opinion in HIV and AIDS | Übersicht zur Rolle von Islatravir (Reverse-Transkriptase-Translokationsinhibitor) bei Behandlung und Prävention von HIV-1; kein Bezug zu Doravirin |

---

## Marktinformationen Deutschland

| Zulassungsnummer | Produktname | Darreichungsform | Zugelassene Indikation |
|---------|------|------|-----------|
| EMEA/H/C/004747 | Pifeltro | – | HIV-Infektionen (erloschen) |
| EMEA/H/C/004746 | Delstrigo | – | HIV-Infektionen (erloschen) |

---

## Sicherheitsaspekte

**Arzneimittelwechselwirkungen:** Insgesamt wurden 59 Wechselwirkungen erfasst. Die wichtigsten:
- **Schwerwiegend (Major):** Dexamethason, Lumacaftor
- **Mäßig (Moderate):** Glycerolphenylbutyrat, Metreleptin, Troglitazon, Deferasirox, Praziquantel, Griseofulvin
- **Gering (Minor):** u. a. Aprepitant, Cimetidin, Clarithromycin, Clotrimazol, Miconazol, Cobicistat, Ticagrelor, Ivacaftor, Zafirlukast, Chloramphenicol, Erythromycin, Fluconazol

Für weitere Sicherheitsinformationen siehe die Fachinformation.

---

## Fazit und nächste Schritte

**Entscheidung: Hold**

**Begründung:**
Die Vorhersage beruht ausschließlich auf der Modellnähe zu HIV; es gibt weder klinische Studien noch Doravirin-spezifische Literatur. Zudem sprechen die bekannte NNRTI-Resistenz von FIV und SIV sowie der tiermedizinische Kontext gegen einen sinnvollen humanen Repurposing-Ansatz. Beide Zulassungen in Deutschland sind erloschen.

**Für ein Weiterkommen sind folgende Schritte erforderlich:**
- Daten zum Wirkmechanismus (MOA) von Doravirin ergänzen
- Warnhinweise und Gegenanzeigen aus der Fachinformation (BfArM) beschaffen, da dies für das Sicherheits-Screening erforderlich ist
- In-vitro-Daten zur Aktivität von Doravirin gegen FIV bzw. SIV erheben
- Klären, ob eine veterinärmedizinische Entwicklung überhaupt angestrebt wird
## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

