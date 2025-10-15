**Page Name:** Vault Page

**Purpose:** The Vault page serves as the central case management hub, allowing users to store, organize, and manage their legal cases with associated files and metadata.

**Key Features:**
*   **"Create case" card:** An always-present, specially styled card that, when clicked, navigates the user to the `/vault/create` page to initiate a new case record. It provides visual feedback on hover.
*   **Individual Case Cards:** Clickable cards, each representing an existing legal case. Clicking a card navigates the user to the specific case's detail page (`/vault/${caseId}`). These cards offer visual feedback on hover and support keyboard navigation.
*   **"+ Create your first case" button:** Displayed when no cases exist (empty state), this button allows users to initiate a new case record and navigates them to the `/vault/create` page. It also provides visual feedback on hover.

**Intended User Flow:**
1.  User navigates to the Vault page.
2.  The page displays either a grid of existing legal cases (each represented by a "Case Card") or an empty state message.
3.  To create a new case:
    *   User clicks the "Create case" card (which is always present at the top of the grid).
    *   **OR** (if no cases exist) User clicks the "+ Create your first case" button within the empty state container.
    *   This action navigates the user to the `/vault/create` page.
4.  To view an existing case:
    *   User clicks on any individual "Case Card" from the displayed grid.
    *   This action navigates the user to the specific case's detail page (`/vault/${caseId}`).