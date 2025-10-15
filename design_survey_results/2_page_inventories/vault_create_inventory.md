Here's the structured 'Product Feature & Flow Inventory' based on your page description:

---

*   **Page Name:** Vault Create Case Page
*   **Purpose:** To provide a comprehensive form interface for legal professionals to create new legal cases, input detailed case information and metadata, and store it for future reference and management within the LexAI application.
*   **Key Features:**
    *   **Page Title:** "Create New Case"
    *   **Error Display:** Conditional error messages (red text) shown above the form when errors exist.
    *   **Form Structure:** HTML form with client-side validation and asynchronous submission.
    *   **Case Name Field:** Required text input with a placeholder ("e.g. ABC Corp. v. XYZ Ltd.") and validation.
    *   **Description Field:** Optional textarea with a placeholder ("Brief description of the case…") and 3 rows.
    *   **Case Summary Field:** Optional textarea with a placeholder ("Detailed summary of the case facts…") and 4 rows.
    *   **Metadata Section Header:** "Metadata (Optional)"
    *   **Petitioner Name Field:** Optional text input with a placeholder ("e.g. ABC Corporation").
    *   **Respondent Name Field:** Optional text input with a placeholder ("e.g. XYZ Limited").
    *   **Filing Date Field:** Optional date input (YYYY-MM-DD format) for selecting a date.
    *   **Judge Name Field:** Optional text input with a placeholder ("e.g. Hon. Justice [Name]").
    *   **Submit Button:** "Create Case" button with distinct states:
        *   Normal (blue background)
        *   Hover (darker blue background)
        *   Disabled (reduced opacity, cursor-not-allowed)
        *   Loading ("Creating…")
    *   **Client-Side Validation:** Real-time validation, specifically checking for a non-empty "Case Name" and valid date formats, preventing submission if invalid.
    *   **Form Reset:** Clears all form fields after a successful submission.
    *   **Loading Indicator:** "Creating…" text displayed on the submit button during submission.
    *   **Success Feedback:** Automatic redirection to the newly created case page upon successful submission.
    *   **Responsive Design:** Adapts layout for mobile (single column, full-width inputs), tablet, and desktop (max-width container).
    *   **Accessibility:** Supports keyboard navigation, screen readers (proper labels), WCAG compliant color contrast, and clear focus indicators.
    *   **User Experience:** Intuitive layout with logical field ordering, clear labels, helpful placeholders, and clear indicators for optional fields.
    *   **Authentication:** Verifies user login status and permissions before case creation.
    *   **Data Validation & Sanitization:** Input sanitization to prevent malicious input, type checking, and format validation before Firebase storage.

*   **Intended User Flow:**
    1.  The user navigates to the Vault Create Case page.
    2.  The user views the "Create New Case" title and the form with both required and optional fields.
    3.  The user inputs the required "Case Name".
    4.  The user optionally fills in any desired details in the "Description", "Case Summary", "Petitioner Name", "Respondent Name", "Filing Date", and "Judge Name" fields.
    5.  The user clicks the "Create Case" submit button.
    6.  The system performs client-side validation; if the "Case Name" is missing or other validation rules are violated, an error message is displayed, and submission is prevented.
    7.  If validation passes, the submit button text changes to "Creating…", and the button is disabled, indicating a loading state.
    8.  The application sends the form data to Firebase, verifying user authentication and creating a new case document.
    9.  Upon successful case creation, the form is reset, and the user is automatically redirected to the newly created case page.
    10. If an error occurs during submission (e.g., network error, Firebase error), a clear error message is displayed to the user.

---