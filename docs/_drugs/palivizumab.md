---
layout: default
title: Palivizumab
parent: Nur Modellvorhersage (L5)
nav_order: 339
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-28
monitor_inn: "PALIVIZUMAB"
predicted_indications: ["benign neoplasm of tongue", "epiglottis neoplasm", "cervical neuroblastoma", "benign neoplasm of hypopharynx", "benign neoplasm of floor of mouth", "tumor of testis and paratestis", "cystic neoplasm", "schwannoma of jugular foramen", "mesenchymoma", "thyroglossal duct cyst"]
description: "Palivizumab: vorhergesagte neue Indikation Benign neoplasm of tongue (Evidenzstufe L5). Ursprüngliche Indikation: Respiratory Syncytial Virus Infections"
---

# Palivizumab
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

## Palivizumab: Benign neoplasm of tongue
{: .text-alpha }

## Zusammenfassung in einem Satz

Palivizumab ist ein humanisierter monoklonaler Antikörper gegen das F-Protein des Respiratorischen Synzytial-Virus (RSV) und wurde ursprünglich zur Vorbeugung von RSV-Infektionen eingesetzt.
Das TxGNN-Modell sagt eine mögliche Wirksamkeit bei **gutartiger Neubildung der Zunge** voraus,
allerdings gibt es dafür **keine klinischen Studien** und **keine Publikationen**; die Vorhersage beruht ausschließlich auf dem Modell.

---

## Schnellübersicht

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Respiratory Syncytial Virus Infections |
| Vorhergesagte neue Indikation | Benign neoplasm of tongue |
| TxGNN-Vorhersagewert | 0.9994 |
| Evidenzstufe | L5 |
| Marktstatus in Deutschland | Im Handel (gültige Zulassungen: 1 von 1) |
| Anzahl der Zulassungen | 1 (gültig: 1) |
| Empfohlene Entscheidung | Hold |

---

## Warum ist diese Vorhersage (nicht) plausibel?

Laut ChEMBL (EMBL-EBI) ist für Palivizumab folgender Wirkmechanismus erfasst (inoffizielle Übersetzung): „Inhibitor des Fusionsglykoproteins F0“ Englischer Originalwortlaut: "Fusion glycoprotein F0 inhibitor" ([ChEMBL CHEMBL1201586 (palivizumab): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL1201586), CC BY-SA 3.0; abgerufen am 2026-11-19). Bekannt ist, dass Palivizumab ein humanisierter monoklonaler Antikörper ist, der das F-Protein von RSV bindet und das Virus neutralisiert. Seine Wirksamkeit bei der Prävention schwerer RSV-Erkrankungen der unteren Atemwege ist die ursprüngliche Anwendung.

Ein mechanistischer Zusammenhang zu gutartigen Zungentumoren ist nicht erkennbar. Das Zielprotein (RSV-F-Protein) spielt in der Biologie solcher Neubildungen keine bekannte Rolle, und Palivizumab hat keine bekannte tumorgerichtete Aktivität. Der hohe Vorhersagewert stammt vom TxGNN-Modell (Deep Learning) und kann Ähnlichkeiten widerspiegeln, die das Modell zwischen verwandten Erkrankungen gelernt hat (z. B. Neubildungen im Kopf-Hals-Bereich), nicht eine biologische Begründung.

Auch die übrigen Top-10-Vorhersagen (u. a. Neubildung der Epiglottis, zervikales Neuroblastom, Schwannom des Foramen jugulare, Hodentumoren) zeigen durchgehend Werte um 99,93–0,9994, jedoch ebenfalls ohne mechanistische Verbindung und ohne klinische oder literarische Evidenz.

---

## Evidenz aus klinischen Studien

Derzeit sind keine zugehörigen klinischen Studien registriert.

---

## Evidenz aus der Literatur

Derzeit sind keine zugehörigen Publikationen verfügbar.

---

## Marktinformationen Deutschland

| Zulassungsnummer | Produktname | Darreichungsform | Zugelassene Indikation |
|---------|------|------|-----------|
| EMEA/H/C/000257 | Synagis (AstraZeneca AB) – Status: gültig | – | Respiratory Syncytial Virus Infections |

---

## Sicherheitshinweise

Für Sicherheitsinformationen beachten Sie bitte die Fachinformation. Für die vorgeschlagene neue Indikation liegen keine Sicherheitsdaten vor, und Wechselwirkungsdaten wurden nicht gefunden.

---

## Fazit und nächste Schritte

**Entscheidung: Hold**

**Begründung:**
Die Vorhersage beruht allein auf einem Computermodell (Evidenzstufe L5). Es gibt weder klinische Studien noch Publikationen, und ein plausibler Wirkmechanismus fehlt. Das Arzneimittel ist in Deutschland derzeit mit einer gültigen Zulassung (1 von 1) im Handel.

**Für ein Weiterkommen sind folgende Punkte erforderlich:**
- Daten zum Wirkmechanismus (MOA), um eine mögliche biologische Verbindung zu prüfen
- Auswertung der Fachinformation (Warnhinweise und Gegenanzeigen), da diese Sicherheitsdaten fehlen und die Sicherheitsprüfung sonst nicht fortgesetzt werden kann
- Präklinische Hinweise, die eine tumorbezogene Aktivität stützen würden
- Klärung der Anwendungswege (Verabreichungsroute) für die vorgeschlagene Indikation
- Überprüfung, ob die hohe Vorhersage lediglich auf vom Modell gelernten Ähnlichkeiten zwischen verwandten Erkrankungen beruht

<!-- review:begin log -->

## Prüfprotokoll

Nachfolgend das Prüfprotokoll dieser Seite. Die Aussage, dass keine Daten zum Wirkmechanismus vorliegen, wurde durch einen Auszug aus der angegebenen amtlichen Fachinformation (mit inoffizieller Übersetzung) ersetzt; Modellvorhersagen, Evidenzstufen und Schlussfolgerungen wurden nicht umgeschrieben.

| Prüfdatum | Punkt | Maßnahme | Quelle |
|------|------|------|------|
| 2026-11-19 | Aussage „keine Daten zum Wirkmechanismus“ durch Auszug aus der US-Fachinformation ersetzt | Aussage, dass keine Daten zum Wirkmechanismus vorliegen, durch einen belegten Auszug ersetzt | [ChEMBL CHEMBL1201586 (palivizumab): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL1201586) |

<!-- review:end log -->

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

