*   **Page Name:** CALENDAR PAGE
*   **Purpose:** The Calendar page provides a Google Calendar-integrated interface for legal professionals to manage specialized legal event types, schedules, court dates, deadlines, and meetings.
*   **Key Features:**
    *   Month View toggle button
    *   Week View toggle button
    *   Day View toggle button
    *   Agenda View toggle button
    *   Previous date navigation button
    *   Next date navigation button
    *   Clickable Calendar Events (to view/manage details)
    *   "Add Event" trigger (implied, to open the Add Event Modal)
    *   **Within Add Event Modal:**
        *   Title text input field
        *   Event Type dropdown (options: Hearing, Meeting, Deadline, General)
        *   Start Date/Time input field (datetime-local)
        *   End Date/Time input field (datetime-local)
        *   Description textarea
        *   Cancel button
        *   Add button
    *   **Within Event Details Modal:**
        *   Close button
        *   Delete button (with JavaScript confirmation)
    *   "Connect Google Calendar" button (displayed when authentication is required)
*   **Intended User Flow:**
    1.  User accesses the Calendar page.
    2.  If Google Calendar authentication is required, the user clicks "Connect Google Calendar" and completes the authentication process.
    3.  The user views their legal calendar, initially in the default Month View.
    4.  The user can switch between Month, Week, Day, or Agenda views using the View Toggle Buttons.
    5.  The user navigates to different dates or time periods using the Previous/Next navigation buttons.
    6.  The user initiates the "Add Event" process (e.g., by clicking an "Add Event" button on the calendar, though not explicitly described).
    7.  The "Add Event Modal" appears, prompting the user to input the event Title, select an Event Type, specify Start Date/Time and End Date/Time, and optionally add a Description.
    8.  The user clicks "Add" to create the event and synchronize it with Google Calendar, or "Cancel" to dismiss the modal.
    9.  The user can click on an existing event displayed on the calendar grid to open the "Event Details Modal".
    10. In the "Event Details Modal", the user reviews the event's information.
    11. From the "Event Details Modal", the user can click "Delete" to remove the event (after a confirmation dialog) or "Close" to dismiss the modal.