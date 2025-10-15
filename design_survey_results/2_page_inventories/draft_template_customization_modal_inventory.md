*   **Page Name:** Template Customization Modal
*   **Purpose:** This modal allows users to choose between using a selected template as-is or customizing it with AI based on their answers to specific questions.
*   **Key Features:**
    *   Modal Dialog with Header, Preview, Options, (Conditional) Customization Questions, and Footer.
    *   "Customize Template" title with FileText icon in Header.
    *   Template Preview section displaying template image, title, and a dynamic description.
    *   "Choose an option:" section with two selectable options:
        *   "Use Template As-Is" card (with FileText icon).
        *   "Customize with AI" card (conditional, with Sparkles icon).
    *   "Customization Questions:" section (conditional) displaying a list of text input fields (Shadcn Textarea) for each query.
    *   Footer section with three buttons:
        *   "Cancel" button (outline variant).
        *   "Use As-Is" button (secondary variant, with FileText icon).
        *   "Create Customized" button (conditional, primary variant, with Sparkles icon or spinning loader).
    *   Validation logic for required answers before customization.
    *   Loading states (e.g., "Customizing..." text with spinner).
    *   Full keyboard navigation and screen reader support.
*   **Intended User Flow:**
    1.  User clicks on a template from the home page, templates gallery, or search results.
    2.  The "Template Customization Modal" appears, showing a preview of the selected template and two main options: "Use Template As-Is" and "Customize with AI" (if applicable).
    3.  **Scenario A: User chooses "Use Template As-Is"**
        a. User clicks the "Use Template As-Is" card *or* the "Use As-Is" button in the footer.
        b. The `onSkip` callback is triggered with the template, and the modal closes.
    4.  **Scenario B: User chooses "Customize with AI" (only if template has queries)**
        a. User clicks the "Customize with AI" card.
        b. The "Customization Questions" section appears, displaying a text area for each query.
        c. User answers the questions by typing into the respective text areas, updating the `answers` state.
        d. Once all answers are provided, the "Create Customized" button in the footer becomes enabled.
        e. User clicks the "Create Customized" button.
        f. The `isCustomizing` state is set to `true`, the button text changes to "Customizing..." with a spinner, and the `onCustomize` callback is triggered with the template and provided answers.
        g. Upon successful customization (or error), the `isCustomizing` state is reset, and the modal closes.
    5.  **Scenario C: User cancels**
        a. User clicks the "Cancel" button in the footer or presses the `Escape` key.
        b. The `onClose` callback is triggered, and the modal closes without further action.