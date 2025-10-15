*   **Page Name:** Home Page
*   **Purpose:** The Home page is the main dashboard and entry point for the LexAI document management application, providing comprehensive tools for document search, browsing, management, template creation, and editing.
*   **Key Features:**
    *   Header Search Input (with clear button)
    *   Organization Switcher (Clerk component)
    *   "Template Editor" Button
    *   User Profile Button (Clerk component)
    *   Templates Gallery Search Bar (with clear button)
    *   "Import Document" Button (DocxUploader)
    *   Individual Template Items (clickable to create/customize)
    *   Template Carousel Navigation (Previous button)
    *   Template Carousel Navigation (Next button)
    *   Document Table Rows (clickable to open document)
    *   Document Row Action Menu Trigger (three-dot icon)
    *   Document Menu Item: "Rename"
    *   Document Menu Item: "Remove"
    *   Document Menu Item: "Open in a new tab"
    *   "Load more" Button (for documents table)
*   **Intended User Flow:**
    1.  User lands on the Home Page, viewing recent documents and available templates.
    2.  User utilizes the main Header Search Input to quickly find specific documents across the application.
    3.  To create a new document:
        a.  User browses templates using the Template Carousel Navigation buttons.
        b.  User searches for a specific template using the Templates Gallery Search Bar.
        c.  User clicks on a Template Item to initiate the creation or customization of a new document.
        d.  User clicks the "Import Document" button to upload a DOCX file for processing.
    4.  To manage an existing document:
        a.  User clicks a Document Table Row to open the document in the editor.
        b.  User clicks the Document Row Action Menu Trigger (three-dot icon) to reveal a dropdown of actions.
        c.  From the action menu, the user selects "Rename", "Remove", or "Open in a new tab".
    5.  User clicks the "Load more" button to retrieve additional older documents in the table.
    6.  User interacts with the Organization Switcher or User Profile Button to manage their account or switch organizations.
    7.  User clicks the "Template Editor" Button in the header to navigate to the dedicated template creation and editing interface.