# Balance Home Screen - ER Diagram (Mermaid)

## Document Information
**Date:** 2025-11-07
**Source:** Balance_Home_Screen_Analysis.md
**Purpose:** Complete ER diagram showing screen hierarchy, atomic design components, navigation flows, and composition relationships

---

## Mermaid ER Diagram

```mermaid
erDiagram

%% ─── Screens ──────────────────────────
page_home {
    DESCRIPTION    string "Main landing screen after login - hub for primary actions"
    SCREENTYPE     string "screen"
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
    DESCRIPTION    string "Messaging screen with coach/nutritionist"
    SCREENTYPE     string "screen"
    SCREENELEMENT1 string "organism_app_header"
    SCREENELEMENT2 string "organism_bottom_navigation"
}

page_plan {
    DESCRIPTION    string "Progress tracking and treatment plan view"
    SCREENTYPE     string "screen"
    SCREENELEMENT1 string "organism_app_header"
    SCREENELEMENT2 string "organism_bottom_navigation"
}

page_profile {
    DESCRIPTION    string "User settings and account information"
    SCREENTYPE     string "screen"
    SCREENELEMENT1 string "organism_app_header"
    SCREENELEMENT2 string "organism_bottom_navigation"
}

page_prescription_request {
    DESCRIPTION    string "Prescription request/refill flow"
    SCREENTYPE     string "screen"
    SCREENELEMENT1 string "organism_app_header"
}

page_injection_log {
    DESCRIPTION    string "Injection tracking and logging screen"
    SCREENTYPE     string "screen"
    SCREENELEMENT1 string "organism_app_header"
}

page_symptom_tracker {
    DESCRIPTION    string "Symptom tracking and severity rating screen"
    SCREENTYPE     string "screen"
    SCREENELEMENT1 string "organism_app_header"
}

page_appointment_detail {
    DESCRIPTION    string "Detailed appointment view with reschedule options"
    SCREENTYPE     string "screen"
    SCREENELEMENT1 string "organism_app_header"
    SCREENELEMENT2 string "organism_appointment_card"
}

modal_share_sheet {
    DESCRIPTION    string "System share sheet for referral flow"
    SCREENTYPE     string "modal"
    SCREENELEMENT1 string "label_share_title"
    SCREENELEMENT2 string "button_share_contact"
    COPY_label_share_title string "Invita a un amigo a Balance"
}

%% ─── Components (Organisms) ──────────────────────────
organism_app_header {
    DESCRIPTION    string "Brand identity and personalized greeting"
    SCREENTYPE     string "component"
    SCREENELEMENT1 string "atom_logo_balance"
    SCREENELEMENT2 string "atom_text_user_greeting"
    SCREENELEMENT3 string "atom_text_welcome_headline"
    COPY_atom_text_user_greeting string "Hola, [User Name]"
    COPY_atom_text_welcome_headline string "Bienvenido a Balance"
}

organism_action_card_prescription {
    DESCRIPTION    string "Action card for prescription request"
    SCREENTYPE     string "component"
    SCREENELEMENT1 string "molecule_icon_label"
    SCREENELEMENT2 string "molecule_nav_arrow"
    COPY_molecule_icon_label string "Obtener receta"
}

organism_action_card_injection {
    DESCRIPTION    string "Action card for injection logging"
    SCREENTYPE     string "component"
    SCREENELEMENT1 string "molecule_icon_label"
    SCREENELEMENT2 string "molecule_nav_arrow"
    COPY_molecule_icon_label string "Registrar inyección"
}

organism_action_card_symptoms {
    DESCRIPTION    string "Action card for symptom tracking with helper text"
    SCREENTYPE     string "component"
    SCREENELEMENT1 string "molecule_icon_label"
    SCREENELEMENT2 string "molecule_nav_arrow"
    SCREENELEMENT3 string "atom_text_helper"
    COPY_molecule_icon_label string "Registrar síntomas"
    COPY_atom_text_helper string "Registra cómo te sientes 1-2 días después de tu inyección."
}

organism_promotional_banner {
    DESCRIPTION    string "Referral incentive banner with dismissible option"
    SCREENTYPE     string "component"
    SCREENELEMENT1 string "button_close_banner"
    SCREENELEMENT2 string "atom_text_headline_promo"
    SCREENELEMENT3 string "atom_text_body_value_prop"
    SCREENELEMENT4 string "atom_text_body_benefit"
    SCREENELEMENT5 string "atom_text_caption_disclaimer"
    SCREENELEMENT6 string "button_primary_cta"
    SCREENELEMENT7 string "atom_icon_megaphone"
    COPY_atom_text_headline_promo string "GANA UN MES GRATIS"
    COPY_atom_text_body_value_prop string "Por cada invitación, ¡obtienes 1 mes gratis!"
    COPY_atom_text_body_benefit string "Y tu amigo/a tendrá su primer mes gratis también"
    COPY_atom_text_caption_disclaimer string "*Promoción por tiempo limitado"
    COPY_button_primary_cta string "Invitar ahora"
}

organism_section_header_appointments {
    DESCRIPTION    string "Section header for upcoming appointments"
    SCREENTYPE     string "component"
    SCREENELEMENT1 string "atom_text_h2"
    COPY_atom_text_h2 string "Próximas citas"
}

organism_appointment_card {
    DESCRIPTION    string "Appointment information card with status indicator"
    SCREENTYPE     string "component"
    SCREENELEMENT1 string "molecule_status_badge"
    SCREENELEMENT2 string "molecule_icon_label_meeting"
    SCREENELEMENT3 string "molecule_professional_info"
    COPY_molecule_status_badge string "Cancelada"
    COPY_molecule_icon_label_meeting string "Balance - Primera Consulta Nutricionista"
}

organism_bottom_navigation {
    DESCRIPTION    string "Global navigation bar with four tabs"
    SCREENTYPE     string "component"
    SCREENELEMENT1 string "molecule_nav_tab_home"
    SCREENELEMENT2 string "molecule_nav_tab_chat"
    SCREENELEMENT3 string "molecule_nav_tab_plan"
    SCREENELEMENT4 string "molecule_nav_tab_profile"
}

%% ─── Molecules (Simple Component Combinations) ──────────────────────────
molecule_icon_label {
    DESCRIPTION    string "Icon with adjacent text label"
    SCREENTYPE     string "component"
    SCREENELEMENT1 string "atom_icon"
    SCREENELEMENT2 string "atom_text_body_large"
}

molecule_nav_arrow {
    DESCRIPTION    string "Navigation chevron/arrow indicator"
    SCREENTYPE     string "component"
    SCREENELEMENT1 string "atom_icon_chevron"
}

molecule_status_badge {
    DESCRIPTION    string "Status indicator with dot and label"
    SCREENTYPE     string "component"
    SCREENELEMENT1 string "atom_shape_badge_background"
    SCREENELEMENT2 string "atom_shape_dot_indicator"
    SCREENELEMENT3 string "atom_text_status"
}

molecule_professional_info {
    DESCRIPTION    string "Professional profile with photo, name, and specialty"
    SCREENTYPE     string "component"
    SCREENELEMENT1 string "atom_image_profile"
    SCREENELEMENT2 string "atom_text_professional_name"
    SCREENELEMENT3 string "atom_text_specialty"
    COPY_atom_text_professional_name string "Irene Roth Perez"
    COPY_atom_text_specialty string "Nutrición y Dietética"
}

molecule_icon_label_meeting {
    DESCRIPTION    string "Video icon with meeting type label"
    SCREENTYPE     string "component"
    SCREENELEMENT1 string "atom_icon_video"
    SCREENELEMENT2 string "atom_text_body"
}

molecule_nav_tab_home {
    DESCRIPTION    string "Home navigation tab (active state)"
    SCREENTYPE     string "component"
    SCREENELEMENT1 string "atom_icon_house"
    SCREENELEMENT2 string "atom_text_tab_label"
    COPY_atom_text_tab_label string "Inicio"
}

molecule_nav_tab_chat {
    DESCRIPTION    string "Chat navigation tab"
    SCREENTYPE     string "component"
    SCREENELEMENT1 string "atom_icon_message"
    SCREENELEMENT2 string "atom_text_tab_label"
    COPY_atom_text_tab_label string "Chat"
}

molecule_nav_tab_plan {
    DESCRIPTION    string "Plan navigation tab"
    SCREENTYPE     string "component"
    SCREENELEMENT1 string "atom_icon_chart"
    SCREENELEMENT2 string "atom_text_tab_label"
    COPY_atom_text_tab_label string "Plan"
}

molecule_nav_tab_profile {
    DESCRIPTION    string "Profile navigation tab"
    SCREENTYPE     string "component"
    SCREENELEMENT1 string "atom_icon_person"
    SCREENELEMENT2 string "atom_text_tab_label"
    COPY_atom_text_tab_label string "Perfil"
}

%% ─── Atoms (Basic Building Blocks) ──────────────────────────

%% Text Atoms
atom_text_h1 {
    DESCRIPTION    string "H1 text - welcome message headline"
    SCREENTYPE     string "component"
}

atom_text_h2 {
    DESCRIPTION    string "H2 text - section titles"
    SCREENTYPE     string "component"
}

atom_text_h3 {
    DESCRIPTION    string "H3 text - promotional headline"
    SCREENTYPE     string "component"
}

atom_text_body_large {
    DESCRIPTION    string "Body large text - action card labels"
    SCREENTYPE     string "component"
}

atom_text_body {
    DESCRIPTION    string "Body regular text - descriptive content"
    SCREENTYPE     string "component"
}

atom_text_body_small {
    DESCRIPTION    string "Body small text - secondary information"
    SCREENTYPE     string "component"
}

atom_text_caption {
    DESCRIPTION    string "Caption text - disclaimers and legal text"
    SCREENTYPE     string "component"
}

atom_text_user_greeting {
    DESCRIPTION    string "Personalized user greeting text"
    SCREENTYPE     string "component"
}

atom_text_welcome_headline {
    DESCRIPTION    string "Welcome headline text"
    SCREENTYPE     string "component"
}

atom_text_helper {
    DESCRIPTION    string "Helper/instructional text"
    SCREENTYPE     string "component"
}

atom_text_headline_promo {
    DESCRIPTION    string "Promotional headline text (red, bold)"
    SCREENTYPE     string "component"
}

atom_text_body_value_prop {
    DESCRIPTION    string "Value proposition text in banner"
    SCREENTYPE     string "component"
}

atom_text_body_benefit {
    DESCRIPTION    string "Secondary benefit text in banner"
    SCREENTYPE     string "component"
}

atom_text_caption_disclaimer {
    DESCRIPTION    string "Disclaimer text in banner"
    SCREENTYPE     string "component"
}

atom_text_status {
    DESCRIPTION    string "Status label text (e.g., Cancelada)"
    SCREENTYPE     string "component"
}

atom_text_professional_name {
    DESCRIPTION    string "Professional name text (bold, large)"
    SCREENTYPE     string "component"
}

atom_text_specialty {
    DESCRIPTION    string "Professional specialty text (gray, small)"
    SCREENTYPE     string "component"
}

atom_text_tab_label {
    DESCRIPTION    string "Navigation tab label text"
    SCREENTYPE     string "component"
}

%% Icon Atoms
atom_icon {
    DESCRIPTION    string "Generic icon element (24-32px)"
    SCREENTYPE     string "component"
}

atom_icon_chevron {
    DESCRIPTION    string "Chevron/arrow right icon"
    SCREENTYPE     string "component"
}

atom_icon_clipboard {
    DESCRIPTION    string "Clipboard icon for prescription"
    SCREENTYPE     string "component"
}

atom_icon_syringe {
    DESCRIPTION    string "Syringe icon for injection"
    SCREENTYPE     string "component"
}

atom_icon_notepad {
    DESCRIPTION    string "Notepad/edit icon for symptoms"
    SCREENTYPE     string "component"
}

atom_icon_video {
    DESCRIPTION    string "Video camera icon for virtual appointment"
    SCREENTYPE     string "component"
}

atom_icon_house {
    DESCRIPTION    string "House icon for home navigation"
    SCREENTYPE     string "component"
}

atom_icon_message {
    DESCRIPTION    string "Message bubble icon for chat navigation"
    SCREENTYPE     string "component"
}

atom_icon_chart {
    DESCRIPTION    string "Ascending chart icon for plan navigation"
    SCREENTYPE     string "component"
}

atom_icon_person {
    DESCRIPTION    string "Person silhouette icon for profile navigation"
    SCREENTYPE     string "component"
}

atom_icon_megaphone {
    DESCRIPTION    string "Megaphone illustration for promotional banner"
    SCREENTYPE     string "component"
}

atom_logo_balance {
    DESCRIPTION    string "Balance app logo with sparkle"
    SCREENTYPE     string "component"
}

%% Color Atoms
atom_color_brand_brown {
    DESCRIPTION    string "Primary brand brown color #6B4423"
    SCREENTYPE     string "component"
}

atom_color_beige {
    DESCRIPTION    string "Card background beige #F5E6D3"
    SCREENTYPE     string "component"
}

atom_color_light_peach {
    DESCRIPTION    string "Banner background light peach #FFF4E8"
    SCREENTYPE     string "component"
}

atom_color_red {
    DESCRIPTION    string "Urgent/attention red #D32F2F"
    SCREENTYPE     string "component"
}

atom_color_green {
    DESCRIPTION    string "Positive indicator green #4CAF50"
    SCREENTYPE     string "component"
}

atom_color_gray {
    DESCRIPTION    string "Inactive/secondary gray #757575"
    SCREENTYPE     string "component"
}

atom_color_black {
    DESCRIPTION    string "Primary text black #000000"
    SCREENTYPE     string "component"
}

atom_color_white {
    DESCRIPTION    string "Elevated background white #FFFFFF"
    SCREENTYPE     string "component"
}

%% Shape Atoms
atom_shape_card_background {
    DESCRIPTION    string "Card background with rounded corners (12-16px radius)"
    SCREENTYPE     string "component"
}

atom_shape_button_pill {
    DESCRIPTION    string "Pill-shaped button (20-24px radius)"
    SCREENTYPE     string "component"
}

atom_shape_badge_background {
    DESCRIPTION    string "Badge background pill shape (16px radius)"
    SCREENTYPE     string "component"
}

atom_shape_dot_indicator {
    DESCRIPTION    string "Status dot indicator (8px circle)"
    SCREENTYPE     string "component"
}

atom_shape_profile_circle {
    DESCRIPTION    string "Circular profile image container (50% radius)"
    SCREENTYPE     string "component"
}

%% Interactive Atoms
button_primary_cta {
    DESCRIPTION    string "Primary CTA button (dark brown background, white text)"
    SCREENTYPE     string "component"
    SCREENELEMENT1 string "atom_shape_button_pill"
    SCREENELEMENT2 string "atom_color_brand_brown"
    SCREENELEMENT3 string "atom_text_body"
}

button_close_banner {
    DESCRIPTION    string "X close button for dismissible banner"
    SCREENTYPE     string "component"
    SCREENELEMENT1 string "atom_icon"
}

button_share_contact {
    DESCRIPTION    string "Share contact method button in share sheet"
    SCREENTYPE     string "component"
}

%% Image Atoms
atom_image_profile {
    DESCRIPTION    string "Circular profile photo (48-56px)"
    SCREENTYPE     string "component"
    SCREENELEMENT1 string "atom_shape_profile_circle"
}

%% Label Atoms
label_share_title {
    DESCRIPTION    string "Share sheet title label"
    SCREENTYPE     string "component"
}

%% Spacing Atoms
atom_spacing_xs {
    DESCRIPTION    string "Extra small spacing unit (4px)"
    SCREENTYPE     string "component"
}

atom_spacing_s {
    DESCRIPTION    string "Small spacing unit (8px)"
    SCREENTYPE     string "component"
}

atom_spacing_m {
    DESCRIPTION    string "Medium spacing unit (12px)"
    SCREENTYPE     string "component"
}

atom_spacing_l {
    DESCRIPTION    string "Large spacing unit (16px)"
    SCREENTYPE     string "component"
}

atom_spacing_xl {
    DESCRIPTION    string "Extra large spacing unit (20px)"
    SCREENTYPE     string "component"
}

atom_spacing_xxl {
    DESCRIPTION    string "Double extra large spacing unit (24px)"
    SCREENTYPE     string "component"
}

%% ─── Relationships ───────────────────────

%% Navigation Relationships (Screen to Screen)
page_home ||--|| page_prescription_request : "organism_action_card_prescription"
page_home ||--|| page_injection_log : "organism_action_card_injection"
page_home ||--|| page_symptom_tracker : "organism_action_card_symptoms"
page_home ||--|| modal_share_sheet : "button_primary_cta"
page_home ||--|| page_appointment_detail : "organism_appointment_card"
page_home ||--|| page_chat : "molecule_nav_tab_chat"
page_home ||--|| page_plan : "molecule_nav_tab_plan"
page_home ||--|| page_profile : "molecule_nav_tab_profile"

page_chat ||--|| page_home : "molecule_nav_tab_home"
page_chat ||--|| page_plan : "molecule_nav_tab_plan"
page_chat ||--|| page_profile : "molecule_nav_tab_profile"

page_plan ||--|| page_home : "molecule_nav_tab_home"
page_plan ||--|| page_chat : "molecule_nav_tab_chat"
page_plan ||--|| page_profile : "molecule_nav_tab_profile"

page_profile ||--|| page_home : "molecule_nav_tab_home"
page_profile ||--|| page_chat : "molecule_nav_tab_chat"
page_profile ||--|| page_plan : "molecule_nav_tab_plan"

%% Component Composition Relationships (Screen contains Organism)
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

%% Organism contains Molecule Relationships
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

%% Molecule contains Atom Relationships
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

%% Button Composition Relationships
button_primary_cta ||--o{ atom_shape_button_pill : "contains"
button_primary_cta ||--o{ atom_color_brand_brown : "contains"
button_primary_cta ||--o{ atom_text_body : "contains"

button_close_banner ||--o{ atom_icon : "contains"

%% Image Composition Relationships
atom_image_profile ||--o{ atom_shape_profile_circle : "contains"

%% Action Card Styling Relationships (uses color/shape atoms)
organism_action_card_prescription }o--|| atom_color_beige : "uses_background_color"
organism_action_card_prescription }o--|| atom_shape_card_background : "uses_shape"

organism_action_card_injection }o--|| atom_color_beige : "uses_background_color"
organism_action_card_injection }o--|| atom_shape_card_background : "uses_shape"

organism_action_card_symptoms }o--|| atom_color_beige : "uses_background_color"
organism_action_card_symptoms }o--|| atom_shape_card_background : "uses_shape"

%% Banner Styling Relationships
organism_promotional_banner }o--|| atom_color_light_peach : "uses_background_color"
organism_promotional_banner }o--|| atom_shape_card_background : "uses_shape"

%% Appointment Card Styling Relationships
organism_appointment_card }o--|| atom_color_white : "uses_background_color"
organism_appointment_card }o--|| atom_shape_card_background : "uses_shape"

%% Status Badge Styling Relationships
molecule_status_badge }o--|| atom_color_red : "uses_text_color"
atom_shape_dot_indicator }o--|| atom_color_red : "uses_fill_color"

%% Navigation Active State Relationships
molecule_nav_tab_home }o--|| atom_color_brand_brown : "uses_active_color"
molecule_nav_tab_chat }o--|| atom_color_gray : "uses_inactive_color"
molecule_nav_tab_plan }o--|| atom_color_gray : "uses_inactive_color"
molecule_nav_tab_profile }o--|| atom_color_gray : "uses_inactive_color"

%% Icon Variant Relationships (specific icons used in specific molecules)
organism_action_card_prescription }o--|| atom_icon_clipboard : "uses_icon"
organism_action_card_injection }o--|| atom_icon_syringe : "uses_icon"
organism_action_card_symptoms }o--|| atom_icon_notepad : "uses_icon"

%% Spacing Relationships (demonstrating spacing usage)
organism_app_header }o--|| atom_spacing_l : "uses_padding"
organism_action_card_prescription }o--|| atom_spacing_l : "uses_padding"
organism_action_card_prescription }o--|| atom_spacing_m : "uses_gap"
```

---

## Diagram Key

### Relationship Types

1. **Navigation Relationships** (Screen → Screen via specific element):
   - `||--||` - One-to-one navigation triggered by user interaction
   - Label shows the specific UI element that triggers navigation

2. **Composition Relationships** (Container → Component):
   - `||--o{` - One-to-many composition (screen contains multiple organisms)
   - Label: "contains" - indicates structural containment

3. **Styling Relationships** (Component → Style Atom):
   - `}o--||` - Many-to-one usage (multiple components can use same color/shape)
   - Label: "uses_background_color", "uses_shape", "uses_text_color", etc.

4. **Variant Relationships** (Component → Specific Variant):
   - `}o--||` - Many-to-one (components use specific icon/text variants)
   - Label: "uses_icon", "uses_active_color", etc.

---

## Usage Notes

### For Developers

1. **Screen Implementation**: Start from page entities, identify all SCREENELEMENT fields to understand required organisms
2. **Component Building**: Build atoms → molecules → organisms following composition relationships
3. **Navigation Logic**: Follow navigation relationships to implement routing between screens
4. **Styling**: Track `uses_*` relationships to apply correct colors, shapes, and spacing

### For Designers

1. **Design System Consistency**: All styling atoms should be documented in design system library
2. **Component Reusability**: Molecules and organisms with multiple "contains" relationships should be design system components
3. **State Variants**: Create variants for different states (active/inactive, canceled/upcoming, etc.)

### For Product Managers

1. **User Flows**: Follow navigation relationships to understand user journeys
2. **Feature Priority**: Screens directly connected to page_home are primary user actions
3. **Content Requirements**: COPY_ fields show all user-facing text that needs localization/copywriting

---

## Atomic Design Hierarchy Summary

### Level 1: Atoms (58 atoms)
- **Text**: 17 text atom variants (H1, H2, H3, body, caption, etc.)
- **Icons**: 11 icon variants (clipboard, syringe, house, message, etc.)
- **Colors**: 8 color atoms (brand brown, beige, red, green, etc.)
- **Shapes**: 5 shape atoms (card background, button pill, badge, dot, circle)
- **Spacing**: 6 spacing units (XS to XXL)
- **Images**: 1 profile image atom
- **Logo**: 1 Balance logo atom

### Level 2: Molecules (10 molecules)
- **icon_label** - Combines icon + text
- **nav_arrow** - Navigation chevron
- **status_badge** - Status indicator with dot
- **professional_info** - Profile photo + name + specialty
- **icon_label_meeting** - Video icon + meeting type
- **nav_tab_home/chat/plan/profile** - Navigation tab variants (4 molecules)

### Level 3: Organisms (9 organisms)
- **app_header** - Logo + greeting + headline
- **action_card_prescription/injection/symptoms** - Action cards (3 organisms)
- **promotional_banner** - Referral incentive banner
- **section_header_appointments** - Section title
- **appointment_card** - Appointment details with status
- **bottom_navigation** - Four-tab navigation bar

### Level 4: Screens (9 screens)
- **page_home** - Main landing screen
- **page_chat** - Messaging screen
- **page_plan** - Progress tracking
- **page_profile** - User settings
- **page_prescription_request** - Prescription flow
- **page_injection_log** - Injection tracking
- **page_symptom_tracker** - Symptom logging
- **page_appointment_detail** - Appointment details
- **modal_share_sheet** - System share modal

---

## Component Reusability Map

### Highly Reusable Components

**Atoms (used in 3+ components):**
- `atom_icon` - Used in all icon contexts
- `atom_text_body` - Used throughout for body text
- `atom_color_brand_brown` - Used for active states, buttons, branding
- `atom_shape_card_background` - Used for all card-style components
- `atom_spacing_l` - Standard padding unit

**Molecules (used in 3+ organisms):**
- `molecule_icon_label` - Used in all three action cards
- `atom_text_tab_label` - Used in all four navigation tabs

**Organisms (used in 4+ screens):**
- `organism_app_header` - Used on 7 of 8 screens
- `organism_bottom_navigation` - Used on 4 primary screens (home, chat, plan, profile)

### Single-Use Specialized Components

**Organisms with unique use cases:**
- `organism_promotional_banner` - Only on home screen (dismissible)
- `organism_section_header_appointments` - Only on home screen (could be generalized)

---

## Navigation Flow Summary

### Primary User Journeys from Home

1. **Medication Management Flow**:
   ```
   page_home → page_prescription_request (via action card)
   page_home → page_injection_log (via action card)
   page_home → page_symptom_tracker (via action card)
   ```

2. **Appointment Management Flow**:
   ```
   page_home → page_appointment_detail (via appointment card)
   ```

3. **Referral Flow**:
   ```
   page_home → modal_share_sheet (via banner CTA button)
   ```

4. **Global Navigation Flow**:
   ```
   page_home ↔ page_chat ↔ page_plan ↔ page_profile (via bottom nav tabs)
   ```

### Navigation Characteristics

- **Hub-and-Spoke**: Home screen acts as central hub with direct access to primary features
- **Persistent Bottom Nav**: Chat, Plan, Profile accessible from any primary screen
- **Modal for Share**: Share sheet uses system modal rather than full-screen navigation
- **No Back Navigation Documented**: Bottom nav allows switching between primary screens without "back" pattern

---

## Design System Integration

### Figma Component Mapping

This ER diagram can be directly translated to Figma components:

1. **Atoms → Figma Styles/Primitives**:
   - Color atoms → Color styles
   - Text atoms → Text styles
   - Spacing atoms → Spacing variables
   - Icon atoms → Icon library
   - Shape atoms → Auto-layout with border-radius variables

2. **Molecules → Figma Components**:
   - Create components with variants (active/inactive states)
   - Use auto-layout for icon + label combinations
   - Define states for interactive molecules

3. **Organisms → Figma Component Sets**:
   - Complex components with multiple variants
   - Use component properties for content
   - Nested instances of molecules

4. **Screens → Figma Pages/Frames**:
   - Full screen compositions
   - Connected with prototyping links
   - Use page templates with component instances

### Code Implementation Mapping

For React/React Native:

```typescript
// Atoms
export const BrandBrownColor = '#6B4423';
export const H1Text = styled.h1`font-size: 32px; font-weight: bold;`;
export const IconClipboard = () => <Icon name="clipboard" size={24} />;

// Molecules
export const IconLabel = ({ icon, label }) => (
  <Flex gap={12}>
    <Icon name={icon} />
    <BodyLargeText>{label}</BodyLargeText>
  </Flex>
);

// Organisms
export const ActionCard = ({ icon, label, helperText, onPress }) => (
  <Card background={BeigeColor} borderRadius={16} padding={16} onPress={onPress}>
    <Flex justify="space-between">
      <IconLabel icon={icon} label={label} />
      <NavArrow />
    </Flex>
    {helperText && <HelperText>{helperText}</HelperText>}
  </Card>
);

// Screens
export const HomePage = () => (
  <Screen>
    <AppHeader />
    <ScrollView>
      <ActionCard icon="clipboard" label="Obtener receta" onPress={...} />
      <ActionCard icon="syringe" label="Registrar inyección" onPress={...} />
      <ActionCard icon="notepad" label="Registrar síntomas" helperText="..." onPress={...} />
      <PromotionalBanner />
      <SectionHeader title="Próximas citas" />
      <AppointmentCard {...appointment} />
    </ScrollView>
    <BottomNavigation activeTab="home" />
  </Screen>
);
```

---

## Future Extensions

### Additional Screens to Document

Based on the analysis, these screens need detailed ER diagrams:

1. **Prescription Request Flow** (page_prescription_request):
   - Eligibility check screen
   - Prescription selection screen
   - Pharmacy selection screen
   - Confirmation screen

2. **Injection Logging Flow** (page_injection_log):
   - Quick-log modal
   - Date/time picker
   - Dosage confirmation
   - Success confirmation

3. **Symptom Tracking Flow** (page_symptom_tracker):
   - Symptom checklist screen
   - Severity rating screen
   - Notes entry screen
   - Insights/trends screen

4. **Appointment Management Flow** (page_appointment_detail):
   - Appointment details screen
   - Reschedule screen (calendar picker)
   - Pre-appointment checklist screen
   - Join video call screen

### State Management Considerations

Future ER diagrams should document:

- **Loading states** for each screen
- **Error states** with retry mechanisms
- **Empty states** (no appointments, no prescriptions)
- **Success/confirmation states** after user actions

### Accessibility Documentation

Additional fields to add in future iterations:

- **ARIA_LABEL**: Screen reader labels
- **KEYBOARD_SHORTCUT**: Keyboard navigation
- **FOCUS_ORDER**: Tab order for form elements
- **ALT_TEXT**: Alternative text for icons and images

---

## Document Metadata

**Version:** 1.0
**Created:** 2025-11-07
**Source Analysis:** Balance_Home_Screen_Analysis.md
**Diagram Type:** Mermaid ER Diagram
**Compatibility:** Notion code blocks, GitHub markdown, Mermaid Live Editor

**Related Documents:**
- Balance_Home_Screen_Analysis.md (source)
- Balance_App_Flow.md (flow documentation)
- Vision_Balance.md (product vision)

**Maintenance Notes:**
- Update this diagram when new screens are added
- Keep COPY_ fields in sync with actual UI text
- Verify all SCREENELEMENT references exist in component definitions
- Update navigation relationships when user flows change

---

**End of ER Diagram Documentation**
