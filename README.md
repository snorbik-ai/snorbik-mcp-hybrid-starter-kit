# snorbik-mcp-hybrid-starter-kit

[![Pôle Stratégique](https://img.shields.io/badge/P%C3%B4le-05_POLE_ARCHITECTURE_CODE_CLEAN-blue.svg)](#)
[![Nature](https://img.shields.io/badge/Nature-VITRINE-orange.svg)](#)
[![Visibilité](https://img.shields.io/badge/Visibilit%C3%A9-100%-green.svg)](#)
[![Version](https://img.shields.io/badge/Version-1.0.0-purple.svg)](#)
[![Standard](https://img.shields.io/badge/Standard-V14.1%20Clean%20Architecture-teal.svg)](#)

> **VITRINE OPEN-SOURCE MONDIALE N°1 (Le Cheval de Troie)**  
> Le gabarit vierge de l'Architecture MCP Hybride Tri-Canal (Porte 1 : JSON-RPC STDIO pour Cursor/Claude/Antigravity, Porte 2 : CLI terminal, Porte 3 : SDK in-process).

---

## 1. Carte d'Identité & Rôle Métier

| Champ Stratégique | Valeur Officielle |
| :--- | :--- |
| **Composant Officiel** | `snorbik-mcp-hybrid-starter-kit` |
| **Pôle d'Appartenance** | **Pôle 5 : L'Outillage de Notoriété, Code Clean & Pattern MCP** |
| **Modèle Business** | **VITRINE OPEN-SOURCE MONDIALE N°1 (Le Cheval de Troie)** |
| **Politique de Visibilité** | **100% PUBLIC OPEN-SOURCE (MIT)** |
| **Mission Principale** | Le gabarit vierge de l'Architecture MCP Hybride Tri-Canal (Porte 1 : JSON-RPC STDIO pour Cursor/Claude/Antigravity, Porte 2 : CLI terminal, Porte 3 : SDK in-process). |
| **Architecture** | Clean Architecture Tri-Canal (STDIO / CLI / SDK In-Process) |

---

## 2. Guide d'Installation 1-Clic

### Option A : Installation Automatisée 1-Clic (Recommandée)
Exécutez simplement le script `install.py` à la racine du dépôt :

```bash
python install.py
```

Ce script effectue automatiquement :
1. La vérification de votre environnement Python (>= 3.10).
2. L'installation des dépendances requises en mode éditable (`pip install -e .` ou `npm install`).
3. La détection et l'injection automatique du serveur dans la configuration de Cursor (`%USERPROFILE%/.cursor/mcp.json`) sans écraser vos autres outils.

### Option B : Installation Manuelle Développeur
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
      "args": ["canal_mcp/mcp_classic_stdio/mcp_server.py"],
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
| `starter_ping` | Vérifie la réactivité du canal STDIO et retourne la latence de traitement. | **Pour tester la bonne liaison entre l'IDE IA et le serveur MCP.** | `aucun` | Message 'pong' avec timestamp UTC et identifiant d'instance. |
| `starter_echo` | Outil miroir démontrant la validation Pydantic et la conformité du protocole MCP. | **Pour valider les passages de paramètres et la sérialisation JSON.** | `message (str, requis)` | Message validé et enrichi des métadonnées du serveur. |

---

## 5. Exemples Concrets de Prompts Utilisateur

Voici 3 exemples réels de requêtes que vous pouvez poser directement dans le chat de Cursor ou Claude Code pour faire travailler cet outil :

1. *« Teste la connexion avec le serveur MCP Starter Kit en envoyant un ping. »*
2. *« Montre-moi comment ajouter un nouvel outil Pydantic dans ce gabarit hybride. »*
3. *« Explique la structure des 3 canaux (STDIO, CLI, SDK) de ce patron de conception. »*

---

## 🛡️ Propriété Intellectuelle & Sécurité
- **Éditeur :** SNORBIK AI © 2026.
- **Classification :** Conforme à la Directive Maîtresse V14.1 (Recettes d'architecture sanctuarisées dans le Pôle 06).
- **Zéro Régression :** Respect strict des budgets de lignes et des normes de sécurité.
