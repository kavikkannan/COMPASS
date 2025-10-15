*   **Page Name:** VAULT CASE DETAIL PAGE
*   **Purpose:** The Vault Case Detail page provides comprehensive functionality for managing individual legal cases by allowing users to upload, organize, and manage case files alongside editing and maintaining detailed case metadata.
*   **Key Features:**
    *   "← Back to Vault" button
    *   File Search input (with real-time filtering)
    *   "Upload files" button
    *   "Delete" button (for selected files)
    *   Hidden file input (supports PDF, DOC, DOCX, TXT, MD, JPG, PNG, GIF, JSON, CSV)
    *   File Table (displays File Name, Type, Upload Date, Size)
    *   Individual File Checkbox selection
    *   Bulk File Selection (Select all/none)
    *   "View" file action button
    *   "Download" file action button
    *   "Delete" file action button (with confirmation dialog)
    *   File Loading state indicator
    *   File Upload progress indicator
    *   File Upload Error state display
    *   "Edit" / "Cancel" toggle button (for metadata panel)
    *   Metadata Key-Value display (with proper formatting)
    *   Metadata Empty state display ("No metadata available")
    *   Metadata Form Fields (Text inputs for Petitioner, Respondent, Judge, Case Number, Court, Jurisdiction, Case Type, Case Status, Value in Dispute, Arbitration Institution, Procedure Type, Advocates, Opposing Counsel, Bench, Sections Involved, Acts/Statutes)
    *   Metadata Form Fields (Textareas for Case Summary, Notes/Remarks)
    *   Metadata Form Fields (Date inputs for Filing Date, Hearing Date, Order/Decision Date)
    *   "Add field" dropdown (for predefined metadata fields)
    *   Custom Field creation option
    *   Remove Field button (for dynamic fields)
    *   Real-time Form Validation
    *   "Save" button (for metadata, with loading state and success feedback)
    *   "Cancel" button (for metadata form reset)
    *   General Loading indicators
    *   Success/Error messages (for various operations)
    *   Hover effects (for interactive elements)
    *   Keyboard navigation support
    *   Screen reader support (via ARIA labels)
    *   Color contrast compliance (WCAG)
    *   Focus management
    *   Optional Auto-save functionality
    *   Draft preservation
*   **Intended User Flow:**
    1.  User navigates to a specific Vault Case Detail page.
    2.  User reviews existing case files in the left column.
    3.  User views the current case metadata in the right column.
    4.  To manage files:
        a. User can search for specific files using the search input.
        b. User can select one or more files using checkboxes.
        c. User can click "View", "Download", or "Delete" for selected files (with confirmation for deletion).
        d. User can click "Upload files" to select and upload new files, observing upload progress and validation.
    5.  To edit metadata:
        a. User clicks the "Edit" button in the metadata panel.
        b. User modifies existing text, date, or textarea fields.
        c. User can add predefined or custom new fields using the "Add field" dropdown.
        d. User can remove dynamic fields if no longer needed.
        e. User observes real-time validation feedback for their entries.
        f. User clicks "Save" to commit changes (observing loading state and confirmation) or "Cancel" to discard changes.
    6.  User clicks the "← Back to Vault" button to navigate away from the case detail page.