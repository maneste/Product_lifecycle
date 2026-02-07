# Balance App - Atomic Design Component Structure

## Document Information
**Date:** 2025-11-07
**Source:** Balance_Home_Screen_Analysis.md
**Purpose:** Complete atomic design hierarchy showing component composition and styling relationships (Atoms → Molecules → Organisms → Templates → Pages)

---

## Mermaid ER Diagram - Atomic Design Structure

```mermaid
erDiagram

%% ═══════════════════════════════════════════════════════════════
%% PAGES (Level 5 - Specific Instances)
%% ═══════════════════════════════════════════════════════════════

page_home {
    LEVEL          string "Page - Specific Instance"
    DESCRIPTION    string "Main landing screen after login - hub for primary actions"
    SCREENELEMENT1 string "organism_app_header"
    SCREENELEMENT2 string "organism_action_card_prescription"
    SCREENELEMENT3 string "organism_action_card_injection"
    SCREENELEMENT4 string "organism_action_card_symptoms"
    SCREENELEMENT5 string "organism_promotional_banner"
    SCREENELEMENT6 string "organism_section_header_appointments"
    SCREENELEMENT7 string "organism_appointment_card"
    SCREENELEMENT8 string "organism_bottom_navigation"
}

page_chat {
    LEVEL          string "Page - Specific Instance"
    DESCRIPTION    string "Messaging screen with coach/nutritionist"
    SCREENELEMENT1 string "organism_app_header"
    SCREENELEMENT2 string "organism_bottom_navigation"
}

page_plan {
    LEVEL          string "Page - Specific Instance"
    DESCRIPTION    string "Progress tracking and treatment plan view"
    SCREENELEMENT1 string "organism_app_header"
    SCREENELEMENT2 string "organism_bottom_navigation"
}

page_profile {
    LEVEL          string "Page - Specific Instance"
    DESCRIPTION    string "User settings and account information"
    SCREENELEMENT1 string "organism_app_header"
    SCREENELEMENT2 string "organism_bottom_navigation"
}

page_prescription_request {
    LEVEL          string "Page - Specific Instance"
    DESCRIPTION    string "Prescription request/refill flow"
    SCREENELEMENT1 string "organism_app_header"
}

page_injection_log {
    LEVEL          string "Page - Specific Instance"
    DESCRIPTION    string "Injection tracking and logging screen"
    SCREENELEMENT1 string "organism_app_header"
}

page_symptom_tracker {
    LEVEL          string "Page - Specific Instance"
    DESCRIPTION    string "Symptom tracking and severity rating screen"
    SCREENELEMENT1 string "organism_app_header"
}

page_appointment_detail {
    LEVEL          string "Page - Specific Instance"
    DESCRIPTION    string "Detailed appointment view with reschedule options"
    SCREENELEMENT1 string "organism_app_header"
    SCREENELEMENT2 string "organism_appointment_card"
}

modal_share_sheet {
    LEVEL          string "Page - Modal Instance"
    DESCRIPTION    string "System share sheet for referral flow"
    SCREENELEMENT1 string "label_share_title"
    SCREENELEMENT2 string "button_share_contact"
}

%% ═══════════════════════════════════════════════════════════════
%% ORGANISMS (Level 3 - Complex UI Components)
%% ═══════════════════════════════════════════════════════════════

organism_app_header {
    LEVEL          string "Organism - Complex Component"
    DESCRIPTION    string "Brand identity and personalized greeting"
    SCREENELEMENT1 string "atom_logo_balance"
    SCREENELEMENT2 string "atom_text_user_greeting"
    SCREENELEMENT3 string "atom_text_welcome_headline"
    COPY           string "Hola [User], Bienvenido a Balance"
}

organism_action_card_prescription {
    LEVEL          string "Organism - Complex Component"
    DESCRIPTION    string "Action card for prescription request"
    SCREENELEMENT1 string "molecule_icon_label"
    SCREENELEMENT2 string "molecule_nav_arrow"
    COPY           string "Obtener receta"
}

organism_action_card_injection {
    LEVEL          string "Organism - Complex Component"
    DESCRIPTION    string "Action card for injection logging"
    SCREENELEMENT1 string "molecule_icon_label"
    SCREENELEMENT2 string "molecule_nav_arrow"
    COPY           string "Registrar inyección"
}

organism_action_card_symptoms {
    LEVEL          string "Organism - Complex Component"
    DESCRIPTION    string "Action card for symptom tracking with helper text"
    SCREENELEMENT1 string "molecule_icon_label"
    SCREENELEMENT2 string "molecule_nav_arrow"
    SCREENELEMENT3 string "atom_text_helper"
    COPY           string "Registrar síntomas | Registra cómo te sientes 1-2 días después de tu inyección"
}

organism_promotional_banner {
    LEVEL          string "Organism - Complex Component"
    DESCRIPTION    string "Referral incentive banner with dismissible option"
    SCREENELEMENT1 string "button_close_banner"
    SCREENELEMENT2 string "atom_text_headline_promo"
    SCREENELEMENT3 string "atom_text_body_value_prop"
    SCREENELEMENT4 string "atom_text_body_benefit"
    SCREENELEMENT5 string "atom_text_caption_disclaimer"
    SCREENELEMENT6 string "button_primary_cta"
    SCREENELEMENT7 string "atom_icon_megaphone"
}

organism_section_header_appointments {
    LEVEL          string "Organism - Complex Component"
    DESCRIPTION    string "Section header for upcoming appointments"
    SCREENELEMENT1 string "atom_text_h2"
    COPY           string "Próximas citas"
}

organism_appointment_card {
    LEVEL          string "Organism - Complex Component"
    DESCRIPTION    string "Appointment information card with status indicator"
    SCREENELEMENT1 string "molecule_status_badge"
    SCREENELEMENT2 string "molecule_icon_label_meeting"
    SCREENELEMENT3 string "molecule_professional_info"
}

organism_bottom_navigation {
    LEVEL          string "Organism - Complex Component"
    DESCRIPTION    string "Global navigation bar with four tabs"
    SCREENELEMENT1 string "molecule_nav_tab_home"
    SCREENELEMENT2 string "molecule_nav_tab_chat"
    SCREENELEMENT3 string "molecule_nav_tab_plan"
    SCREENELEMENT4 string "molecule_nav_tab_profile"
}

%% ═══════════════════════════════════════════════════════════════
%% MOLECULES (Level 2 - Simple Component Combinations)
%% ═══════════════════════════════════════════════════════════════

molecule_icon_label {
    LEVEL          string "Molecule - Component Combination"
    DESCRIPTION    string "Icon with adjacent text label"
    SCREENELEMENT1 string "atom_icon"
    SCREENELEMENT2 string "atom_text_body_large"
}

molecule_nav_arrow {
    LEVEL          string "Molecule - Component Combination"
    DESCRIPTION    string "Navigation chevron/arrow indicator"
    SCREENELEMENT1 string "atom_icon_chevron"
}

molecule_status_badge {
    LEVEL          string "Molecule - Component Combination"
    DESCRIPTION    string "Status indicator with dot and label"
    SCREENELEMENT1 string "atom_shape_badge_background"
    SCREENELEMENT2 string "atom_shape_dot_indicator"
    SCREENELEMENT3 string "atom_text_status"
}

molecule_professional_info {
    LEVEL          string "Molecule - Component Combination"
    DESCRIPTION    string "Professional profile with photo, name, and specialty"
    SCREENELEMENT1 string "atom_image_profile"
    SCREENELEMENT2 string "atom_text_professional_name"
    SCREENELEMENT3 string "atom_text_specialty"
}

molecule_icon_label_meeting {
    LEVEL          string "Molecule - Component Combination"
    DESCRIPTION    string "Video icon with meeting type label"
    SCREENELEMENT1 string "atom_icon_video"
    SCREENELEMENT2 string "atom_text_body"
}

molecule_nav_tab_home {
    LEVEL          string "Molecule - Component Combination"
    DESCRIPTION    string "Home navigation tab (active state)"
    SCREENELEMENT1 string "atom_icon_house"
    SCREENELEMENT2 string "atom_text_tab_label"
    COPY           string "Inicio"
}

molecule_nav_tab_chat {
    LEVEL          string "Molecule - Component Combination"
    DESCRIPTION    string "Chat navigation tab"
    SCREENELEMENT1 string "atom_icon_message"
    SCREENELEMENT2 string "atom_text_tab_label"
    COPY           string "Chat"
}

molecule_nav_tab_plan {
    LEVEL          string "Molecule - Component Combination"
    DESCRIPTION    string "Plan navigation tab"
    SCREENELEMENT1 string "atom_icon_chart"
    SCREENELEMENT2 string "atom_text_tab_label"
    COPY           string "Plan"
}

molecule_nav_tab_profile {
    LEVEL          string "Molecule - Component Combination"
    DESCRIPTION    string "Profile navigation tab"
    SCREENELEMENT1 string "atom_icon_person"
    SCREENELEMENT2 string "atom_text_tab_label"
    COPY           string "Perfil"
}

%% ═══════════════════════════════════════════════════════════════
%% ATOMS (Level 1 - Basic Building Blocks)
%% ═══════════════════════════════════════════════════════════════

%% ─── Text Atoms ───
atom_text_h1 {
    LEVEL       string "Atom - Text Element"
    DESCRIPTION string "H1 text - welcome message headline"
    SIZE        string "32-36pt"
    WEIGHT      string "Bold"
    COLOR       string "Black #000000"
}

atom_text_h2 {
    LEVEL       string "Atom - Text Element"
    DESCRIPTION string "H2 text - section titles"
    SIZE        string "20-24pt"
    WEIGHT      string "Bold"
    COLOR       string "Black #000000"
}

atom_text_h3 {
    LEVEL       string "Atom - Text Element"
    DESCRIPTION string "H3 text - promotional headline"
    SIZE        string "18-20pt"
    WEIGHT      string "Bold"
    COLOR       string "Red #D32F2F"
}

atom_text_body_large {
    LEVEL       string "Atom - Text Element"
    DESCRIPTION string "Body large text - action card labels"
    SIZE        string "16-18pt"
    WEIGHT      string "Medium"
    COLOR       string "Dark brown #6B4423"
}

atom_text_body {
    LEVEL       string "Atom - Text Element"
    DESCRIPTION string "Body regular text - descriptive content"
    SIZE        string "14-16pt"
    WEIGHT      string "Regular"
    COLOR       string "Black #000000"
}

atom_text_body_small {
    LEVEL       string "Atom - Text Element"
    DESCRIPTION string "Body small text - secondary information"
    SIZE        string "12-14pt"
    WEIGHT      string "Regular"
    COLOR       string "Gray #757575"
}

atom_text_caption {
    LEVEL       string "Atom - Text Element"
    DESCRIPTION string "Caption text - disclaimers and legal text"
    SIZE        string "10-12pt"
    WEIGHT      string "Regular"
    COLOR       string "Light brown #A0826D"
}

atom_text_user_greeting {
    LEVEL       string "Atom - Text Element"
    DESCRIPTION string "Personalized user greeting text"
    SIZE        string "14-16pt"
    WEIGHT      string "Regular"
    COLOR       string "Brown #6B4423"
}

atom_text_welcome_headline {
    LEVEL       string "Atom - Text Element"
    DESCRIPTION string "Welcome headline text"
    SIZE        string "32-36pt"
    WEIGHT      string "Bold"
    COLOR       string "Black #000000"
}

atom_text_helper {
    LEVEL       string "Atom - Text Element"
    DESCRIPTION string "Helper/instructional text"
    SIZE        string "14-16pt"
    WEIGHT      string "Regular"
    COLOR       string "Black #000000"
}

atom_text_headline_promo {
    LEVEL       string "Atom - Text Element"
    DESCRIPTION string "Promotional headline text"
    SIZE        string "18-20pt"
    WEIGHT      string "Bold"
    COLOR       string "Red #D32F2F"
}

atom_text_body_value_prop {
    LEVEL       string "Atom - Text Element"
    DESCRIPTION string "Value proposition text in banner"
    SIZE        string "14-16pt"
    WEIGHT      string "Regular"
    COLOR       string "Black #000000"
}

atom_text_body_benefit {
    LEVEL       string "Atom - Text Element"
    DESCRIPTION string "Secondary benefit text in banner"
    SIZE        string "14-16pt"
    WEIGHT      string "Regular"
    COLOR       string "Black #000000"
}

atom_text_caption_disclaimer {
    LEVEL       string "Atom - Text Element"
    DESCRIPTION string "Disclaimer text in banner"
    SIZE        string "10-12pt"
    WEIGHT      string "Regular"
    COLOR       string "Light brown #A0826D"
}

atom_text_status {
    LEVEL       string "Atom - Text Element"
    DESCRIPTION string "Status label text"
    SIZE        string "12-14pt"
    WEIGHT      string "Medium"
    COLOR       string "Red #D32F2F (or status-dependent)"
}

atom_text_professional_name {
    LEVEL       string "Atom - Text Element"
    DESCRIPTION string "Professional name text"
    SIZE        string "18-20pt"
    WEIGHT      string "Bold"
    COLOR       string "Black #000000"
}

atom_text_specialty {
    LEVEL       string "Atom - Text Element"
    DESCRIPTION string "Professional specialty text"
    SIZE        string "12-14pt"
    WEIGHT      string "Regular"
    COLOR       string "Gray #757575"
}

atom_text_tab_label {
    LEVEL       string "Atom - Text Element"
    DESCRIPTION string "Navigation tab label text"
    SIZE        string "10-12pt"
    WEIGHT      string "Regular"
    COLOR       string "Brown #6B4423 (active) or Gray #757575 (inactive)"
}

%% ─── Icon Atoms ───
atom_icon {
    LEVEL       string "Atom - Icon Element"
    DESCRIPTION string "Generic icon element"
    SIZE        string "24-32px"
}

atom_icon_chevron {
    LEVEL       string "Atom - Icon Element"
    DESCRIPTION string "Chevron/arrow right icon"
    SIZE        string "20-24px"
    COLOR       string "Brown or Gray"
}

atom_icon_clipboard {
    LEVEL       string "Atom - Icon Element"
    DESCRIPTION string "Clipboard icon for prescription"
    SIZE        string "24-32px"
    COLOR       string "Brown #6B4423"
}

atom_icon_syringe {
    LEVEL       string "Atom - Icon Element"
    DESCRIPTION string "Syringe icon for injection"
    SIZE        string "24-32px"
    COLOR       string "Brown #6B4423"
}

atom_icon_notepad {
    LEVEL       string "Atom - Icon Element"
    DESCRIPTION string "Notepad/edit icon for symptoms"
    SIZE        string "24-32px"
    COLOR       string "Brown #6B4423"
}

atom_icon_video {
    LEVEL       string "Atom - Icon Element"
    DESCRIPTION string "Video camera icon for virtual appointment"
    SIZE        string "24px"
    COLOR       string "Black #000000"
}

atom_icon_house {
    LEVEL       string "Atom - Icon Element"
    DESCRIPTION string "House icon for home navigation"
    SIZE        string "24px"
    COLOR       string "Brown #6B4423 (active) or Gray #757575 (inactive)"
}

atom_icon_message {
    LEVEL       string "Atom - Icon Element"
    DESCRIPTION string "Message bubble icon for chat navigation"
    SIZE        string "24px"
    COLOR       string "Brown #6B4423 (active) or Gray #757575 (inactive)"
}

atom_icon_chart {
    LEVEL       string "Atom - Icon Element"
    DESCRIPTION string "Ascending chart icon for plan navigation"
    SIZE        string "24px"
    COLOR       string "Brown #6B4423 (active) or Gray #757575 (inactive)"
}

atom_icon_person {
    LEVEL       string "Atom - Icon Element"
    DESCRIPTION string "Person silhouette icon for profile navigation"
    SIZE        string "24px"
    COLOR       string "Brown #6B4423 (active) or Gray #757575 (inactive)"
}

atom_icon_megaphone {
    LEVEL       string "Atom - Icon Element"
    DESCRIPTION string "Megaphone illustration for promotional banner"
    SIZE        string "Large decorative"
    COLOR       string "Brown line art"
}

atom_logo_balance {
    LEVEL       string "Atom - Logo Element"
    DESCRIPTION string "Balance app logo with sparkle"
    SIZE        string "Variable"
}

%% ─── Color Atoms ───
atom_color_brand_brown {
    LEVEL       string "Atom - Color Token"
    DESCRIPTION string "Primary brand brown color"
    HEX         string "#6B4423"
    USAGE       string "Buttons, active states, brand elements"
}

atom_color_beige {
    LEVEL       string "Atom - Color Token"
    DESCRIPTION string "Card background beige"
    HEX         string "#F5E6D3"
    USAGE       string "Action card backgrounds"
}

atom_color_light_peach {
    LEVEL       string "Atom - Color Token"
    DESCRIPTION string "Banner background light peach"
    HEX         string "#FFF4E8"
    USAGE       string "Promotional banner background"
}

atom_color_red {
    LEVEL       string "Atom - Color Token"
    DESCRIPTION string "Urgent/attention red"
    HEX         string "#D32F2F"
    USAGE       string "Status indicators, promotional headlines"
}

atom_color_green {
    LEVEL       string "Atom - Color Token"
    DESCRIPTION string "Positive indicator green"
    HEX         string "#4CAF50"
    USAGE       string "Success states, positive feedback"
}

atom_color_gray {
    LEVEL       string "Atom - Color Token"
    DESCRIPTION string "Inactive/secondary gray"
    HEX         string "#757575"
    USAGE       string "Inactive states, secondary text"
}

atom_color_black {
    LEVEL       string "Atom - Color Token"
    DESCRIPTION string "Primary text black"
    HEX         string "#000000"
    USAGE       string "Body text, headlines"
}

atom_color_white {
    LEVEL       string "Atom - Color Token"
    DESCRIPTION string "Elevated background white"
    HEX         string "#FFFFFF"
    USAGE       string "Card elevated backgrounds, buttons"
}

%% ─── Shape Atoms ───
atom_shape_card_background {
    LEVEL         string "Atom - Shape Token"
    DESCRIPTION   string "Card background with rounded corners"
    BORDER_RADIUS string "12-16px"
}

atom_shape_button_pill {
    LEVEL         string "Atom - Shape Token"
    DESCRIPTION   string "Pill-shaped button"
    BORDER_RADIUS string "20-24px"
}

atom_shape_badge_background {
    LEVEL         string "Atom - Shape Token"
    DESCRIPTION   string "Badge background pill shape"
    BORDER_RADIUS string "16px"
}

atom_shape_dot_indicator {
    LEVEL         string "Atom - Shape Token"
    DESCRIPTION   string "Status dot indicator"
    SIZE          string "8px circle"
}

atom_shape_profile_circle {
    LEVEL         string "Atom - Shape Token"
    DESCRIPTION   string "Circular profile image container"
    BORDER_RADIUS string "50% (fully circular)"
}

%% ─── Spacing Atoms ───
atom_spacing_xs {
    LEVEL       string "Atom - Spacing Token"
    DESCRIPTION string "Extra small spacing unit"
    VALUE       string "4px"
}

atom_spacing_s {
    LEVEL       string "Atom - Spacing Token"
    DESCRIPTION string "Small spacing unit"
    VALUE       string "8px"
}

atom_spacing_m {
    LEVEL       string "Atom - Spacing Token"
    DESCRIPTION string "Medium spacing unit"
    VALUE       string "12px"
}

atom_spacing_l {
    LEVEL       string "Atom - Spacing Token"
    DESCRIPTION string "Large spacing unit"
    VALUE       string "16px"
}

atom_spacing_xl {
    LEVEL       string "Atom - Spacing Token"
    DESCRIPTION string "Extra large spacing unit"
    VALUE       string "20px"
}

atom_spacing_xxl {
    LEVEL       string "Atom - Spacing Token"
    DESCRIPTION string "Double extra large spacing unit"
    VALUE       string "24px"
}

%% ─── Image Atoms ───
atom_image_profile {
    LEVEL       string "Atom - Image Element"
    DESCRIPTION string "Circular profile photo"
    SIZE        string "48-56px"
    SHAPE       string "Circular (50% border-radius)"
}

%% ─── Button Atoms ───
button_primary_cta {
    LEVEL       string "Atom - Interactive Element"
    DESCRIPTION string "Primary CTA button"
    BACKGROUND  string "Dark brown #6B4423"
    TEXT_COLOR  string "White #FFFFFF"
    SHAPE       string "Pill (20-24px radius)"
}

button_close_banner {
    LEVEL       string "Atom - Interactive Element"
    DESCRIPTION string "X close button for dismissible banner"
    SIZE        string "24px"
}

button_share_contact {
    LEVEL       string "Atom - Interactive Element"
    DESCRIPTION string "Share contact method button in share sheet"
}

label_share_title {
    LEVEL       string "Atom - Label Element"
    DESCRIPTION string "Share sheet title label"
}

%% ═══════════════════════════════════════════════════════════════
%% COMPOSITION RELATIONSHIPS (Contains)
%% ═══════════════════════════════════════════════════════════════

%% Pages contain Organisms
page_home ||--o{ organism_app_header : "contains"
page_home ||--o{ organism_action_card_prescription : "contains"
page_home ||--o{ organism_action_card_injection : "contains"
page_home ||--o{ organism_action_card_symptoms : "contains"
page_home ||--o{ organism_promotional_banner : "contains"
page_home ||--o{ organism_section_header_appointments : "contains"
page_home ||--o{ organism_appointment_card : "contains"
page_home ||--o{ organism_bottom_navigation : "contains"

page_chat ||--o{ organism_app_header : "contains"
page_chat ||--o{ organism_bottom_navigation : "contains"

page_plan ||--o{ organism_app_header : "contains"
page_plan ||--o{ organism_bottom_navigation : "contains"

page_profile ||--o{ organism_app_header : "contains"
page_profile ||--o{ organism_bottom_navigation : "contains"

page_prescription_request ||--o{ organism_app_header : "contains"
page_injection_log ||--o{ organism_app_header : "contains"
page_symptom_tracker ||--o{ organism_app_header : "contains"

page_appointment_detail ||--o{ organism_app_header : "contains"
page_appointment_detail ||--o{ organism_appointment_card : "contains"

%% Organisms contain Molecules/Atoms
organism_app_header ||--o{ atom_logo_balance : "contains"
organism_app_header ||--o{ atom_text_user_greeting : "contains"
organism_app_header ||--o{ atom_text_welcome_headline : "contains"

organism_action_card_prescription ||--o{ molecule_icon_label : "contains"
organism_action_card_prescription ||--o{ molecule_nav_arrow : "contains"

organism_action_card_injection ||--o{ molecule_icon_label : "contains"
organism_action_card_injection ||--o{ molecule_nav_arrow : "contains"

organism_action_card_symptoms ||--o{ molecule_icon_label : "contains"
organism_action_card_symptoms ||--o{ molecule_nav_arrow : "contains"
organism_action_card_symptoms ||--o{ atom_text_helper : "contains"

organism_promotional_banner ||--o{ button_close_banner : "contains"
organism_promotional_banner ||--o{ atom_text_headline_promo : "contains"
organism_promotional_banner ||--o{ atom_text_body_value_prop : "contains"
organism_promotional_banner ||--o{ atom_text_body_benefit : "contains"
organism_promotional_banner ||--o{ atom_text_caption_disclaimer : "contains"
organism_promotional_banner ||--o{ button_primary_cta : "contains"
organism_promotional_banner ||--o{ atom_icon_megaphone : "contains"

organism_section_header_appointments ||--o{ atom_text_h2 : "contains"

organism_appointment_card ||--o{ molecule_status_badge : "contains"
organism_appointment_card ||--o{ molecule_icon_label_meeting : "contains"
organism_appointment_card ||--o{ molecule_professional_info : "contains"

organism_bottom_navigation ||--o{ molecule_nav_tab_home : "contains"
organism_bottom_navigation ||--o{ molecule_nav_tab_chat : "contains"
organism_bottom_navigation ||--o{ molecule_nav_tab_plan : "contains"
organism_bottom_navigation ||--o{ molecule_nav_tab_profile : "contains"

%% Molecules contain Atoms
molecule_icon_label ||--o{ atom_icon : "contains"
molecule_icon_label ||--o{ atom_text_body_large : "contains"

molecule_nav_arrow ||--o{ atom_icon_chevron : "contains"

molecule_status_badge ||--o{ atom_shape_badge_background : "contains"
molecule_status_badge ||--o{ atom_shape_dot_indicator : "contains"
molecule_status_badge ||--o{ atom_text_status : "contains"

molecule_professional_info ||--o{ atom_image_profile : "contains"
molecule_professional_info ||--o{ atom_text_professional_name : "contains"
molecule_professional_info ||--o{ atom_text_specialty : "contains"

molecule_icon_label_meeting ||--o{ atom_icon_video : "contains"
molecule_icon_label_meeting ||--o{ atom_text_body : "contains"

molecule_nav_tab_home ||--o{ atom_icon_house : "contains"
molecule_nav_tab_home ||--o{ atom_text_tab_label : "contains"

molecule_nav_tab_chat ||--o{ atom_icon_message : "contains"
molecule_nav_tab_chat ||--o{ atom_text_tab_label : "contains"

molecule_nav_tab_plan ||--o{ atom_icon_chart : "contains"
molecule_nav_tab_plan ||--o{ atom_text_tab_label : "contains"

molecule_nav_tab_profile ||--o{ atom_icon_person : "contains"
molecule_nav_tab_profile ||--o{ atom_text_tab_label : "contains"

%% ═══════════════════════════════════════════════════════════════
%% STYLING RELATIONSHIPS (Uses Design Tokens)
%% ═══════════════════════════════════════════════════════════════

%% Action Cards use Colors and Shapes
organism_action_card_prescription }o--|| atom_color_beige : "uses_background_color"
organism_action_card_prescription }o--|| atom_shape_card_background : "uses_shape"

organism_action_card_injection }o--|| atom_color_beige : "uses_background_color"
organism_action_card_injection }o--|| atom_shape_card_background : "uses_shape"

organism_action_card_symptoms }o--|| atom_color_beige : "uses_background_color"
organism_action_card_symptoms }o--|| atom_shape_card_background : "uses_shape"

%% Banner uses Colors and Shapes
organism_promotional_banner }o--|| atom_color_light_peach : "uses_background_color"
organism_promotional_banner }o--|| atom_shape_card_background : "uses_shape"

%% Appointment Card uses Colors and Shapes
organism_appointment_card }o--|| atom_color_white : "uses_background_color"
organism_appointment_card }o--|| atom_shape_card_background : "uses_shape"

%% Status Badge uses Colors
molecule_status_badge }o--|| atom_color_red : "uses_text_color"
atom_shape_dot_indicator }o--|| atom_color_red : "uses_fill_color"

%% Navigation Tabs use Colors
molecule_nav_tab_home }o--|| atom_color_brand_brown : "uses_active_color"
molecule_nav_tab_chat }o--|| atom_color_gray : "uses_inactive_color"
molecule_nav_tab_plan }o--|| atom_color_gray : "uses_inactive_color"
molecule_nav_tab_profile }o--|| atom_color_gray : "uses_inactive_color"

%% Action Cards use Specific Icons
organism_action_card_prescription }o--|| atom_icon_clipboard : "uses_icon"
organism_action_card_injection }o--|| atom_icon_syringe : "uses_icon"
organism_action_card_symptoms }o--|| atom_icon_notepad : "uses_icon"

%% Spacing Usage Examples
organism_app_header }o--|| atom_spacing_l : "uses_padding"
organism_action_card_prescription }o--|| atom_spacing_l : "uses_padding"
organism_action_card_prescription }o--|| atom_spacing_m : "uses_internal_gap"

```

---

## Atomic Design Hierarchy Summary

### Component Count

- **Level 1 - Atoms**: 58 atoms
  - Text: 17 variants
  - Icons: 11 variants
  - Colors: 8 tokens
  - Shapes: 5 tokens
  - Spacing: 6 tokens
  - Images: 1 element
  - Logo: 1 element
  - Interactive elements: 3 buttons/labels

- **Level 2 - Molecules**: 10 molecules
  - icon_label, nav_arrow, status_badge, professional_info, icon_label_meeting
  - nav_tab_home, nav_tab_chat, nav_tab_plan, nav_tab_profile

- **Level 3 - Organisms**: 8 organisms
  - app_header, action_card (3 variants), promotional_banner
  - section_header_appointments, appointment_card, bottom_navigation

- **Level 4 - Templates**: Not explicitly defined (pages act as templates)

- **Level 5 - Pages**: 9 pages/modals
  - 8 full screens + 1 modal

---

## Relationship Types

### 1. Composition (contains)
**Format:** `||--o{`
- Shows hierarchical structure
- Indicates which components are composed of which subcomponents
- Example: `organism_app_header ||--o{ atom_logo_balance : "contains"`

### 2. Styling (uses_*)
**Format:** `}o--||`
- Shows which design tokens are used by which components
- Labels: `uses_background_color`, `uses_shape`, `uses_icon`, etc.
- Example: `organism_action_card_prescription }o--|| atom_color_beige : "uses_background_color"`

---

## Reusability Analysis

### Highly Reusable Components

**Atoms (used in 5+ places):**
- `atom_text_body` - Used throughout for standard text
- `atom_color_brand_brown` - Used for active states, buttons, emphasis
- `atom_shape_card_background` - Used for all card-style components
- `atom_spacing_l` - Standard padding unit

**Molecules (used in 3+ organisms):**
- `molecule_icon_label` - Used in all three action cards
- `atom_text_tab_label` - Used in all four navigation tabs

**Organisms (used in 5+ screens):**
- `organism_app_header` - Used on 7 of 8 screens
- `organism_bottom_navigation` - Used on 4 primary screens

---

## Design System Guidelines

### Creating New Components

**When to create an Atom:**
- Basic building block (text, icon, color, shape)
- No internal structure
- Pure visual primitive

**When to create a Molecule:**
- Combines 2-5 atoms
- Simple interaction pattern
- Reusable across multiple contexts

**When to create an Organism:**
- Complex component with multiple molecules
- Specific business logic or behavior
- May be screen-specific or reusable

**When to create a Page:**
- Full screen composition
- Combines multiple organisms
- Represents a complete user view

---

## Implementation Notes

### For React/React Native Developers

```typescript
// 1. Define Atoms as Constants/Primitives
export const Colors = {
  brandBrown: '#6B4423',
  beige: '#F5E6D3',
  // ...
};

export const Spacing = {
  xs: 4, s: 8, m: 12, l: 16, xl: 20, xxl: 24
};

// 2. Create Molecules as Simple Components
const IconLabel = ({ icon, label }) => (
  <Flex gap={Spacing.m}>
    <Icon name={icon} size={24} />
    <Text style={styles.bodyLarge}>{label}</Text>
  </Flex>
);

// 3. Build Organisms from Molecules
const ActionCard = ({ icon, label, helperText, onPress }) => (
  <Pressable
    style={[styles.card, { backgroundColor: Colors.beige }]}
    onPress={onPress}
  >
    <Flex justify="space-between">
      <IconLabel icon={icon} label={label} />
      <NavArrow />
    </Flex>
    {helperText && <HelperText>{helperText}</HelperText>}
  </Pressable>
);

// 4. Assemble Pages
const HomePage = () => (
  <Screen>
    <AppHeader />
    <ScrollView>
      <ActionCard icon="clipboard" label="Obtener receta" onPress={...} />
      <ActionCard icon="syringe" label="Registrar inyección" onPress={...} />
      <ActionCard
        icon="notepad"
        label="Registrar síntomas"
        helperText="Registra cómo te sientes 1-2 días después de tu inyección."
        onPress={...}
      />
    </ScrollView>
    <BottomNavigation activeTab="home" />
  </Screen>
);
```

---

## Version Information

**Version:** 1.0
**Created:** 2025-11-07
**Source:** Balance_Home_Screen_Analysis.md
**Related Documents:**
- Balance_Screen_Navigation_Flow.md (navigation relationships)
- Balance_App_Flow.md (complete app flows)
