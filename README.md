# snorbik-mcp-hybrid-starter-kit

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB.svg?logo=python&logoColor=white)](#)
[![Protocol](https://img.shields.io/badge/MCP_Protocol-2025--11--25-blue.svg)](#)
[![Architecture](https://img.shields.io/badge/Architecture-Hybride_Tri--Canal-teal.svg)](#)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](#)
[![Status](https://img.shields.io/badge/Status-Production--Ready-success.svg)](#)

> **Starter Kit Officiel Architecture MCP Hybride Tri-Canal**  
> Gabarit prêt à l'emploi combinant les 3 canaux d'accès : Canal 1 JSON-RPC STDIO (Cursor, Claude Code, Windsurf, VS Code), Canal 2 CLI terminal, Canal 3 SDK in-process.

---

## 1. Carte d'Identité & Rôle Métier

| Champ Stratégique | Valeur Officielle |
| :--- | :--- |
| **Composant Officiel** | `snorbik-mcp-hybrid-starter-kit` |
| **Licence** | **MIT Open-Source** |
| **Compatibilité Clients** | **Cursor, Claude Code, VS Code, Claude Desktop, Antigravity** |
| **Architecture** | **Clean Architecture Tri-Canal (STDIO / CLI / SDK In-Process)** |
| **Spécification MCP** | **JSON-RPC 2.0 (Cycle officiel 2025-11-25)** |

---

## 2. Guide d'Installation Multi-Clients

### Option A : Installation via Coding Agent (Recommandée)
Copiez-collez simplement ce prompt dans votre agent IA (Cursor, Claude Code, Windsurf, VS Code Copilot) :

> « Configure le serveur MCP depuis ce dépôt :
> 1. Détecte mon client actif (Cursor, Claude Code ou VS Code).
> 2. Lance `python install.py` (ou `python install.py --client cursor|vscode|claude`) pour enregistrer le serveur sans écraser mes autres outils.
> 3. Vérifie que le serveur répond en appelant l'outil `template_ping` et confirme-moi la réponse `pong`. »

---

### Option B : Installation Automatisée 1-Clic (Terminal)
Exécutez simplement le script `install.py` à la racine du dépôt :

```bash
python install.py
```

Options ciblées par client :
- `python install.py --client cursor` : injecte dans `~/.cursor/mcp.json` (clé `mcpServers`).
- `python install.py --client vscode` : configure `.vscode/mcp.json` (clé officielle `servers`).
- `python install.py --client claude` : enregistre via `claude mcp add` et configure Claude Desktop.
- `python install.py --client all` : auto-détection et configuration universelle.

---

### Option C : Installation Manuelle Développeur
```bash
pip install -e .
```

---

## 3. Configuration Manuelle (Cursor, Antigravity, Claude Desktop)

Si vous préférez déclarer manuellement ce serveur dans votre fichier `.cursor/mcp.json` ou `mcp_config.json`, ajoutez le bloc suivant :

```json
{
  "mcpServers": {
    "snorbik-mcp-hybrid-starter-kit": {
      "command": "python",
      "args": ["template_mcp_hybride/canal_mcp/mcp_server.py"],
      "env": { "PYTHONIOENCODING": "utf-8" },
      "type": "stdio"
    }
  }
}
```

---

## 4. Catalogue Sémantique des Outils (`tools`)

Ce composant expose des outils déterministes prêts à être invoqués par un modèle de langage (LLM) :

| Nom de l'Outil (`tool`) | Rôle & Fonction Technique | Déclencheur d'Action (*Quand l'IA DOIT-ELLE l'appeler ?*) | Paramètres Requis | Sortie Retournée |
| :--- | :--- | :--- | :--- | :--- |
| `template_ping` | Vérifie la réactivité du canal STDIO et retourne l'état de santé du serveur. | **Pour tester la bonne liaison entre l'IDE IA et le serveur MCP.** | `aucun` | DTO `ToolResponseDto` (`operation_id`, `status: "SUCCESS"`, `payload.reply: "pong"`, `execution_duration_ms`). |
| `template_execute_action` | Outil miroir démontrant la validation Pydantic et la conformité du protocole MCP. | **Pour valider les passages de paramètres et la sérialisation JSON.** | `message (str, requis)` | DTO enrichi avec message validé, statut opérationnel et horodatage Unix certifié. |

---

## 5. Performances Mesurées en Conditions Réelles

Mesuré sur banc d'essai indépendant (environnement Windows / Python 3.12) :
- **Installation 1-clic (`python install.py`)** : ~**13,6 secondes**
- **Tests unitaires (`pytest`)** : **3 passed** en **1,53 s**
- **Latence à froid (1er appel Python)** : **391 ms**
- **Latence à chaud (requêtes suivantes)** : **0,099 ms** (< 0,1 milliseconde)

---

## 6. Exemples Concrets de Prompts Utilisateur

Voici 3 exemples réels de requêtes que vous pouvez poser directement dans le chat de Cursor ou Claude Code pour faire travailler cet outil :

1. *« Teste la connexion avec le serveur MCP Starter Kit en envoyant un ping. »*
2. *« Montre-moi comment ajouter un nouvel outil Pydantic dans ce gabarit hybride. »*
3. *« Explique la structure des 3 canaux (STDIO, CLI, SDK) de ce patron de conception. »*

---

## 🛡️ Propriété Intellectuelle & Sécurité
- **Éditeur :** SNORBIK AI © 2026.
- **Classification :** Conforme à la Directive Maîtresse V14.1 (Recettes d'architecture sanctuarisées dans le Pôle 06).
- **Zéro Régression :** Respect strict des budgets de lignes et des normes de sécurité.
