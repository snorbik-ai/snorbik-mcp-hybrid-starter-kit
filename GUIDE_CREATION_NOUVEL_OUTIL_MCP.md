# 🚀 Guide Pratique : Créer un Nouvel Outil MCP Hybride en Moins de 10 Minutes

---

## 1. Philosophie & Principes Fondateurs

Le **Pattern MCP Hybride Snorbik** repose sur le découplage strict entre la logique métier et les canaux d'accès :
- **Un Cœur Métier Unique & Étanche (Clean Architecture DPN v4) :**
  - `core/domain/` : Entités Pydantic légères et typées, ports d'interfaces.
  - `core/application/` : Cas d'usage isolés avec gestion d'erreurs et audit.
  - `core/infrastructure/` : Adaptateurs techniques (base de données, APIs, système de fichiers).
- **Trois Portes d'Accès Sans Duplication de Code :**
  - **Porte 1 (IDE IA) :** `canal_mcp/mcp_server.py` — Protocole standard JSON-RPC 2.0 via `stdio` pour Cursor, Antigravity, Claude Desktop, Windsurf.
  - **Porte 2 (CLI / Terminal) :** `canal_sdk_cli/cli.py` — Interface en ligne de commande pour les développeurs humains et scripts bash/powershell.
  - **Porte 3 (In-Process / Performance) :** `canal_sdk_cli/sdk.py` — Façade Python importable directement par FastAPI, Celery ou un autre outil interne (latence < 2ms, zéro IPC).

---

## 2. Procédure Pas-à-Pas en 5 Étapes

### Étape 1 : Dupliquer le Gabarit Vierge
Copier le dossier `template_mcp_hybride/` vers votre nouveau répertoire cible dans `outils_internes/` :

```bash
# Exemple pour créer un nouvel outil :
cp -r template_mcp_hybride mon_nouvel_outil
```

### Étape 2 : Définir les Entités & Contrats dans `core/domain/`
Dans `core/domain/entities.py`, définissez vos structures de données typées :

```python
from pydantic import BaseModel, Field

class AnalyseRequestDto(BaseModel):
    target_path: str = Field(..., description="Chemin à analyser.")
    deep_scan: bool = Field(default=False)

class AnalyseResponseDto(BaseModel):
    files_analyzed: int
    findings_count: int
    score: float
```

### Étape 3 : Implémenter le Cas d'Usage dans `core/application/`
Dans `core/application/usecases.py`, isolez votre logique métier :

```python
class AnalyserProjetUseCase:
    def __init__(self, scanner_adapter):
        self.scanner = scanner_adapter

    def execute(self, request: AnalyseRequestDto) -> AnalyseResponseDto:
        # Votre logique métier protégée
        findings = self.scanner.scan(request.target_path)
        return AnalyseResponseDto(
            files_analyzed=len(findings),
            findings_count=len(findings),
            score=98.5
        )
```

### Étape 4 : Déclarer les Outils dans `canal_mcp/mcp_server.py`
Dans `canal_mcp/mcp_server.py`, configurez `TOOLS_METADATA` et complétez `handle_tool_call` :

```python
TOOLS_METADATA = [
    {
        "name": "analyser_projet",
        "description": "Exécute une analyse de conformité sur le répertoire spécifié.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "target_path": {"type": "string", "description": "Chemin du dossier."},
                "deep_scan": {"type": "boolean", "default": False}
            },
            "required": ["target_path"]
        }
    }
]

def handle_tool_call(tool_name: str, arguments: dict):
    if tool_name == "analyser_projet":
        return usecase.execute(AnalyseRequestDto(**arguments)).model_dump()
    raise ValueError(f"Outil inconnu : {tool_name}")
```

### Étape 5 : Enregistrer dans `install.py` & Déployer
1. Ajoutez votre outil dans votre registre ou script d'installation :
```python
    "mon-nouvel-outil": {
        "name": "mon-nouvel-outil",
        "command": "python",
        "script": "mon_nouvel_outil/canal_mcp/mcp_server.py",
        "description": "Description claire de la responsabilité de l'outil."
    }
```
2. Lancez l'installation automatique :
```bash
python install.py
```
3. Votre outil est instantanément disponible pour toutes les IAs (Antigravity, Cursor, Claude).

---

## 3. Checklist de Validation & Sas de Pré-Vol V26 (Obligatoire)

Avant de publier ou livrer un nouvel outil MCP, validez systématiquement les 6 sas de la Directive Transverse V26 :
1. **Tests unitaires & Intégration :** Suite `pytest` à 100% au vert.
2. **Cycle de vie MCP officiel (JSON-RPC 2.0) :** Réponse au handshake `initialize`, silence sur `notifications/initialized`, réponse valide sur `tools/list` et `tools/call`.
3. **Résilience de l'installateur :** Contrôle des returncodes système (`pip`/`npm`) et refus d'écrasement en cas de JSON corrompu (génération d'un `.corrupted.bak`).
4. **Sanctuarisation Zéro-Leak :** Absence absolue de chemins machine (`C:\Users`), de secrets, de termes internes ou de projets privés.
5. **Alignement Juridique & Métadonnées :** Fichier physique `LICENSE` (MIT) présent, `pyproject.toml` aligné, et badges shields.io testés par requête HTTP 200.
6. **Contrôle de la Source Réelle :** Vérification du commit de tête sur `origin/main` et inspection du rendu HTML public.
