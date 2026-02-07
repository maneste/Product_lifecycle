# Balance App - Home Screen UI Analysis

## Document Information
**Date:** 2025-11-07
**Source:** Home screen screenshot analysis
**Purpose:** Comprehensive UI element breakdown, interaction patterns, and design system documentation

---

## Visual Hierarchy & Layout Structure

### Layer 1: System Status Bar
**Position:** Top of screen
**Purpose:** OS-level information display
**Elements:**
- Time indicator (9:51) with green pill background
- Signal strength indicators
- 5G network indicator
- Battery level (57%) with green indicator

**Design Note:** Green color usage suggests positive status/healthy battery level

---

### Layer 2: App Header
**Position:** Below status bar
**Purpose:** Brand identity + user personalization

#### Elements:
1. **Balance Logo (Center-aligned)**
   - Logo with sparkle icon
   - Brand element reinforcing app identity

2. **User Greeting**
   - Primary: "Hola, Manu Nule" (brown text)
   - Secondary: "Bienvenido a Balance" (large, bold, black)
   - **UX Pattern:** Personalization to create connection
   - **Emotional Goal:** Welcome user, establish rapport

**Design System:**
- Typography: Bold for main headline, regular for greeting
- Color: Brown for personalized text, black for headline
- Spacing: Generous padding around brand and greeting

---

### Layer 3: Primary Action Cards (Core Feature Access)
**Position:** Below header, occupying prime visual real estate
**Purpose:** Quick access to essential medication management tasks

#### Card Design System:
- **Background:** Beige/tan (#F5E6D3 approximate)
- **Shape:** Rounded corners (approx 12-16px radius)
- **Layout:** Icon (left) + Label (center) + Arrow (right)
- **Spacing:** Consistent vertical stack with gaps between cards

#### Card 1: "Obtener receta" (Get Prescription)
**Icon:** Clipboard (medical context)
**Interaction:** Tap to navigate → Prescription request flow
**User Intent:** Request new prescription or refill
**Priority:** Top position suggests high importance in user journey

**Likely Flow Trigger:**
- Navigate to prescription request form
- Check eligibility for refill
- Possibly integration with pharmacy/doctor approval workflow

---

#### Card 2: "Registrar inyección" (Register Injection)
**Icon:** Syringe (direct visual metaphor)
**Interaction:** Tap to navigate → Injection logging flow
**User Intent:** Track medication administration
**Priority:** Second position suggests frequent use

**Likely Flow Trigger:**
- Quick-log injection modal
- Date/time picker
- Dosage confirmation
- Possibly connects to prescription tracking (doses remaining)

**UX Pattern:** Low-friction logging for habit formation

---

#### Card 3: "Registrar síntomas" (Register Symptoms)
**Icon:** Notepad/edit icon
**Interaction:** Tap to navigate → Symptom tracking flow
**User Intent:** Log side effects or physical response to medication
**Priority:** Third position, includes helper text

**Helper Text:** "Registra cómo te sientes 1-2 días después de tu inyección."
**UX Pattern:** Contextual guidance to educate user on timing
**Behavioral Nudge:** Encourages consistent post-injection monitoring

**Likely Flow Trigger:**
- Symptom checklist or free-text entry
- Severity rating
- Possibly time-gated (only shows after injection logged)
- Data feeds to coach/doctor dashboard

**Design Decision:** Helper text only on this card suggests it needs more explanation than the others (less intuitive task)

---

### Layer 4: Promotional Banner (Engagement/Growth)
**Position:** After primary actions, before appointments
**Purpose:** User acquisition through referral incentive

#### Visual Design:
- **Background:** Light peach (#FFF4E8 approximate)
- **Shape:** Rounded rectangle matching card style
- **Illustration:** Megaphone (brown line art, right side)
- **Close Button:** X button (top-right corner)

#### Content Hierarchy:
1. **Headline:** "GANA UN MES GRATIS" (red, bold, all caps)
   - **Color:** Red for attention/urgency
   - **Typography:** Bold, large, attention-grabbing

2. **Value Proposition:** "Por cada invitación, ¡obtienes 1 mes gratis!"
   - Clear benefit statement

3. **Secondary Benefit:** "Y tu amigo/a tendrá su primer mes gratis también"
   - Social proof/reciprocity trigger

4. **Disclaimer:** "*Promoción por tiempo limitado"
   - Small, light brown text
   - Creates urgency

5. **CTA Button:** "Invitar ahora"
   - **Color:** Dark brown (consistent with app theme)
   - **Shape:** Rounded rectangle
   - **Action:** Likely triggers share sheet or contact picker

#### Interaction Patterns:
- **Primary:** Tap "Invitar ahora" → Share flow
- **Secondary:** Tap X → Dismiss banner (likely stored in preferences)

**UX Strategy:**
- Positioned after primary tasks to avoid disrupting core workflow
- Dismissable to respect user control
- Visual style matches app design system (not intrusive)
- Referral incentive aligns with health journey context (friend support)

**Design Decision:** Placement after primary actions but before appointments balances visibility with user priorities

---

### Layer 5: Upcoming Appointments Section
**Position:** Below promotional banner, above bottom navigation
**Purpose:** Surface next scheduled appointment for awareness/preparation

#### Section Header:
- **Title:** "Próximas citas"
- **Typography:** Bold, dark text
- **Purpose:** Clear section labeling

#### Appointment Card:
**Visual Design:**
- **Background:** White (elevated from screen background)
- **Shape:** Rounded corners matching other cards
- **Layout:** Multi-line information hierarchy

#### Status Indicator:
- **Label:** "Cancelada" (Canceled)
- **Color:** Red dot + red text
- **Position:** Top-left of card
- **UX Pattern:** Prominent status display for urgent information

#### Appointment Details:
1. **Meeting Type Icon + Label**
   - Video camera icon (indicates virtual appointment)
   - Text: "Balance - Primera Consulta Nutricionista"
   - **Context:** First nutritionist consultation

2. **Professional Information**
   - **Photo:** Circular profile image
   - **Name:** "Irene Roth Perez" (large, bold)
   - **Specialty:** "Nutrición y Dietética" (gray, smaller text)

**Information Hierarchy:**
- Status (most urgent) → Meeting type → Professional identity
- Visual weight decreases down the card

#### Interaction Patterns:
**Likely Actions:**
- Tap card → View appointment details
- Reschedule option (given "Cancelada" status)
- Add to calendar
- Preparation checklist or pre-appointment forms

**UX Insights:**
- Canceled status requires immediate attention (red color choice)
- Professional photo humanizes the experience
- Specialty listed helps user remember appointment purpose
- Video icon sets expectations for virtual format

**Design Decision:** Single appointment card suggests showing only next/most urgent appointment (not full calendar view)

---

### Layer 6: Bottom Navigation Bar
**Position:** Fixed at bottom of screen
**Purpose:** Global navigation across app sections

#### Tab Structure (4 tabs):

**Tab 1: "Inicio" (Home) - ACTIVE**
- **Icon:** House
- **Color:** Brown (selected state)
- **Label:** "Inicio"
- **State:** Currently active screen

**Tab 2: "Chat"**
- **Icon:** Message bubble
- **Color:** Gray (inactive state)
- **Label:** "Chat"
- **Expected Destination:** Messaging with coach/support team

**Tab 3: "Plan"**
- **Icon:** Ascending chart/graph
- **Color:** Gray (inactive state)
- **Label:** "Plan"
- **Expected Destination:** Progress tracking, goals, or treatment plan view

**Tab 4: "Perfil" (Profile)**
- **Icon:** Person silhouette
- **Color:** Gray (inactive state)
- **Label:** "Perfil"
- **Expected Destination:** User settings, account info, personal data

#### Navigation Design System:
- **Selected State:** Brown color (matches brand)
- **Inactive State:** Gray
- **Layout:** Icon above label
- **Distribution:** Equal width tabs

**UX Pattern:** Standard bottom navigation for mobile apps
**Accessibility:** Icons + labels provide dual indicators

---

## Design System Documentation

### Color Palette:

#### Primary Colors:
- **Brand Brown:** Primary actions, selected states, emphasis (#6B4423 approximate)
- **Beige/Tan:** Card backgrounds (#F5E6D3 approximate)
- **Black:** Primary text, headlines (#000000)

#### Accent Colors:
- **Red:** Urgency, canceled status, promotional headlines (#D32F2F approximate)
- **Green:** Positive indicators (battery, time background) (#4CAF50 approximate)
- **Gray:** Secondary text, inactive states (#757575 approximate)
- **Light Peach:** Promotional banner background (#FFF4E8 approximate)

#### Functional Colors:
- **White:** Card elevated backgrounds (#FFFFFF)
- **Off-white/Cream:** Screen background (subtle warmth)

**Color Strategy:**
- Brown/beige creates warm, approachable medical experience (not clinical)
- Red reserved for urgent information (canceled appointments, limited-time offers)
- Green for positive reinforcement
- Gray for de-emphasized content

---

### Typography System:

#### Hierarchy Levels:
1. **H1 (Welcome Message):** "Bienvenido a Balance"
   - Large, bold, black
   - Use case: Primary screen headline

2. **H2 (Section Titles):** "Próximas citas"
   - Bold, dark text
   - Use case: Content section headers

3. **H3 (Promotional Headline):** "GANA UN MES GRATIS"
   - Bold, all caps, red
   - Use case: Attention-grabbing announcements

4. **Body Large (Card Labels):** "Obtener receta", "Registrar inyección"
   - Medium weight, dark text
   - Use case: Primary action labels

5. **Body Regular (Descriptive Text):** Helper text under symptom card
   - Regular weight, dark text
   - Use case: Explanatory content

6. **Body Small (Professional Specialty):** "Nutrición y Dietética"
   - Regular weight, gray
   - Use case: Secondary descriptive information

7. **Caption (Disclaimers):** "*Promoción por tiempo limitado"
   - Small, light brown
   - Use case: Legal text, disclaimers

**Typography Strategy:**
- Clear hierarchy through size and weight
- Consistent spacing between text elements
- Readable font sizes for medical context (accessibility priority)

---

### Component Library:

#### Action Card Component:
**Structure:**
```
[Icon] [Label Text]                [Arrow]
```
**Properties:**
- Background: Beige/tan
- Padding: Generous (16-20px vertical, 16-24px horizontal)
- Border-radius: 12-16px
- Icon size: 24-32px
- Arrow: Chevron or simple arrow
- Optional: Helper text below label

**States:**
- Default (as shown)
- Pressed (likely darker background)
- Disabled (not shown, likely grayed out)

---

#### Appointment Card Component:
**Structure:**
```
[Status Badge]
[Video Icon] [Appointment Type]
[Profile Photo] [Professional Name]
              [Specialty]
```
**Properties:**
- Background: White (elevated)
- Padding: 16-20px
- Border-radius: 12-16px
- Shadow: Subtle (1-2px depth)
- Status badge: Pill shape with dot indicator

**States:**
- Upcoming (not shown - likely different status color)
- Canceled (as shown - red)
- Completed (not shown - likely gray or green)

---

#### Promotional Banner Component:
**Structure:**
```
[Close Button - X]
[Headline]
[Body Text]
[Subtext]
[Disclaimer]
[CTA Button]
[Illustration - Right Side]
```
**Properties:**
- Background: Light peach
- Padding: 16-20px
- Border-radius: 12-16px
- Illustration: Decorative, doesn't obscure text
- Dismissable via X button

---

#### Navigation Tab Component:
**Structure:**
```
[Icon]
[Label]
```
**Properties:**
- Width: 25% of screen width
- Vertical layout
- Icon size: 24px
- Label: 10-12pt

**States:**
- Active: Brown icon + brown label
- Inactive: Gray icon + gray label
- Pressed: (not shown, likely slight scale or opacity change)

---

### Spacing & Layout:

#### Vertical Rhythm:
- Status bar → Header: Minimal gap
- Header → Action cards: ~24px
- Between action cards: ~12-16px
- Action cards → Promotional banner: ~24px
- Promotional banner → Appointments: ~24px
- Appointments → Bottom nav: ~24px

#### Horizontal Margins:
- Screen edge to card edge: ~16-20px
- Card internal padding: ~16-20px
- Icon to text spacing: ~12-16px

#### Card Widths:
- Full width minus margins (responsive to screen size)
- Consistent across all card types

---

## User Flow Analysis

### Flow Map by Interaction:

#### Primary Action Flows:

**1. Prescription Request Flow**
```
HOME → Tap "Obtener receta"
     → Prescription Request Screen
       → Check eligibility
       → Select prescription type
       → Submit request
       → Confirmation + Next steps
```

**Hypothesized Steps:**
- Verify insurance/eligibility
- Select medication type (if multiple options)
- Choose pharmacy
- Doctor approval notification
- Tracking status of request

---

**2. Injection Logging Flow**
```
HOME → Tap "Registrar inyección"
     → Injection Log Modal/Screen
       → Confirm date/time (pre-filled to now)
       → Confirm dosage
       → Optional: Injection site
       → Save
       → Success confirmation
```

**Hypothesized Steps:**
- Quick-log interface (minimal friction)
- Pre-filled fields for speed
- Confirmation message with next injection reminder
- Update prescription dose count

**Behavioral Design:**
- Should take <10 seconds to complete
- Possibly trigger follow-up notification for symptom logging 1-2 days later

---

**3. Symptom Tracking Flow**
```
HOME → Tap "Registrar síntomas"
     → Symptom Entry Screen
       → Select from common symptoms checklist
       → Rate severity
       → Optional: Free-text notes
       → Save
       → Confirmation + Insights
```

**Hypothesized Steps:**
- Checklist: Nausea, fatigue, headache, etc.
- Severity scale: 1-5 or mild/moderate/severe
- Timestamp automatically captured
- Data visualization of trends over time
- Coach notification if severe symptoms reported

**Behavioral Design:**
- Helper text educates on timing (1-2 days post-injection)
- Possibly time-gated: Suggests logging if injection logged recently
- Longitudinal tracking for dose adjustment discussions

---

**4. Referral Flow**
```
HOME → Tap "Invitar ahora"
     → Share Sheet / Contact Picker
       → Select contact method (WhatsApp, SMS, Email)
       → Send referral link
       → Confirmation
       → Track referral status
```

**Hypothesized Steps:**
- Generate unique referral code/link
- Pre-populated message with benefit description
- Track when friend signs up
- Credit free month to account

---

**5. Appointment Management Flow**
```
HOME → Tap Appointment Card
     → Appointment Detail Screen
       → View full details
       → Reschedule option (given canceled status)
       → Add to calendar
       → Pre-appointment preparation checklist
       → Join video call (if not canceled)
```

**Hypothesized Steps (Reschedule Path):**
- Show available time slots
- Select new date/time
- Confirm with professional's calendar
- Update confirmation email/notification
- Update home screen card

---

#### Navigation Flows:

**Home → Chat**
```
Tap "Chat" tab → Chat/Messaging Screen
                → View conversations with coach/nutritionist
                → Send new message
                → View responses
```

**Home → Plan**
```
Tap "Plan" tab → Progress Dashboard
               → Weight tracking chart
               → Medication adherence
               → Goal progress
               → Milestones
```

**Home → Perfil**
```
Tap "Perfil" tab → Profile Screen
                 → Personal information
                 → Account settings
                 → Prescription history
                 → Billing information
                 → Logout
```

---

## Information Architecture

### Content Prioritization:

**Priority 1: Core Tasks (Action Cards)**
- Prescription management
- Medication logging
- Symptom tracking

**Rationale:** These are essential to the app's value proposition (medication management for weight loss treatment)

---

**Priority 2: Upcoming Events (Appointments)**
- Next scheduled appointment
- Status visibility

**Rationale:** Time-sensitive information that requires preparation

---

**Priority 3: Engagement/Growth (Referral Banner)**
- Referral incentive

**Rationale:** Important for business, but not user's primary goal

---

**Priority 4: Navigation (Bottom Tabs)**
- Secondary features access
- Chat, Plan, Profile

**Rationale:** Available but not immediately surfaced

---

### Content Organization Strategy:

**Vertical Scroll Layout:**
- Top: Personalization + Brand
- Middle: Core actions (always visible above fold)
- Lower-middle: Time-sensitive information
- Bottom-fixed: Global navigation

**Modular Card System:**
- Each section is independently scannable
- Cards provide clear affordance for interaction
- Consistent visual language across card types

**Progressive Disclosure:**
- Home screen shows summary/entry points
- Detail screens (behind taps) contain full information
- Reduces cognitive load on main screen

---

## UX Patterns & Design Decisions

### Pattern 1: Personalized Greeting
**Element:** "Hola, Manu Nule" + "Bienvenido a Balance"

**Purpose:**
- Establish emotional connection
- Confirm user is logged in as correct account
- Humanize medical experience

**Behavioral Psychology:**
- Personalization increases engagement
- Welcoming tone reduces anxiety around medical tasks

---

### Pattern 2: Icon + Label + Arrow Cards
**Element:** Three primary action cards

**Purpose:**
- Clear call-to-action
- Visual metaphor (icon) aids recognition
- Arrow indicates navigation to detail screen

**Usability:**
- Large tap targets (accessibility)
- Visual consistency aids learning
- Minimal text = quick scanning

**Design Trade-off:**
- Pro: Clean, uncluttered
- Con: No preview of content (must tap to see)

---

### Pattern 3: Contextual Helper Text
**Element:** Helper text under "Registrar síntomas"

**Purpose:**
- Educate user on optimal timing
- Reduce ambiguity about when to use feature

**Behavioral Nudge:**
- Suggests action 1-2 days after injection
- Encourages consistency in tracking

**Design Decision:**
- Only one card has helper text (avoid clutter)
- Chosen for the least intuitive task

---

### Pattern 4: Status-First Appointment Display
**Element:** "Cancelada" status badge

**Purpose:**
- Surface urgent information immediately
- Prevent user from missing cancellation notice

**Visual Hierarchy:**
- Red color = attention
- Top-left position = first thing seen
- Larger than other appointment details

**UX Impact:**
- Reduces no-shows due to missed cancellations
- Prompts user to reschedule

---

### Pattern 5: Dismissible Promotional Content
**Element:** Referral banner with X button

**Purpose:**
- Respect user control
- Avoid banner blindness (can be removed)
- Balance business goals with user experience

**Best Practice:**
- User can dismiss (not forced to engage)
- Limited-time framing creates urgency without pressure
- Positioned to be visible but not disruptive

---

### Pattern 6: Bottom Navigation for Global Features
**Element:** Four-tab bottom navigation

**Purpose:**
- Standard mobile pattern (familiar)
- Thumb-reachable on large screens
- Persistent access to key sections

**IA Decision:**
- Home (primary landing page)
- Chat (support/communication)
- Plan (progress tracking)
- Profile (account management)

**Trade-off:**
- Pro: Quick switching between sections
- Con: Limited to 4-5 tabs (can't show everything)

---

## Interaction Pattern Summary

### Tap Interactions:
1. **Action Cards:** Navigate to task-specific screen
2. **Appointment Card:** View appointment details/reschedule
3. **Referral Banner CTA:** Open share sheet
4. **Referral Banner X:** Dismiss banner
5. **Bottom Nav Tabs:** Switch between main app sections

### Swipe Interactions (Inferred):
- Likely: Swipe to dismiss promotional banner
- Possibly: Swipe between home content sections

### Long-Press Interactions (Inferred):
- Possibly: Long-press action card for shortcuts
- Example: Long-press "Registrar inyección" → Quick-log modal

### System Interactions:
- Push notifications (appointment reminders, prescription ready)
- Calendar integration (add appointments)
- Share sheet (referral flow)

---

## Accessibility Considerations

### Observed Strengths:
1. **High Color Contrast:** Black text on light backgrounds
2. **Large Tap Targets:** Action cards are generously sized
3. **Icon + Label Redundancy:** Navigation uses both (not icon-only)
4. **Clear Visual Hierarchy:** Size and color indicate importance

### Potential Improvements (Not Observed):
1. **Screen Reader Support:** Ensure all elements have descriptive labels
2. **Dynamic Type:** Text should scale with system font size settings
3. **VoiceOver Order:** Logical reading order for screen readers
4. **Color Blindness:** Don't rely solely on red for "Cancelada" status

---

## Design System Insights

### Brand Identity Characteristics:
- **Warm:** Brown/beige palette (not clinical white/blue)
- **Approachable:** Rounded corners throughout
- **Human:** Personalized greeting, professional photos
- **Supportive:** Helper text, clear guidance

**Strategic Positioning:**
- Not a typical healthcare app (cold, clinical)
- More like a wellness coach (warm, supportive)
- Reduces stigma around weight loss medication

---

### Visual Consistency:
- **Card-based UI:** All content modules use consistent rounded cards
- **Spacing System:** Regular rhythm between sections
- **Color Coding:** Functional colors (red = urgent, brown = brand, gray = inactive)
- **Iconography:** Simple line icons throughout

---

### Component Reusability:
- **Action Card:** Reusable for any navigation task
- **Information Card:** Used for appointments, could be used for messages, updates
- **Banner Component:** Reusable for promotions, announcements, tips
- **Bottom Nav:** Standard across app

---

## Recommendations for Balance_App_Flow.md Integration

### Flow Nodes to Document:

**SCN_HOME (This Screen)**
- Entry point after login
- Hub for all primary actions
- Persistent navigation base

**From SCN_HOME:**
- `ACT_TAP_GET_PRESCRIPTION` → `SCN_PRESCRIPTION_REQUEST`
- `ACT_TAP_LOG_INJECTION` → `SCN_INJECTION_LOG`
- `ACT_TAP_LOG_SYMPTOMS` → `SCN_SYMPTOM_TRACKER`
- `ACT_TAP_REFER_FRIEND` → `SYS_SHARE_SHEET`
- `ACT_TAP_APPOINTMENT` → `SCN_APPOINTMENT_DETAIL`
- `ACT_TAP_CHAT_TAB` → `SCN_CHAT`
- `ACT_TAP_PLAN_TAB` → `SCN_PROGRESS_DASHBOARD`
- `ACT_TAP_PROFILE_TAB` → `SCN_PROFILE`

---

### Open Questions for Flow Design:

1. **Injection Logging:**
   - Is this a quick modal or full-screen flow?
   - Does it trigger a follow-up notification for symptom logging?

2. **Symptom Tracking:**
   - Checklist format or free-text?
   - How is data visualized over time?
   - Does severe symptom entry trigger coach notification?

3. **Prescription Request:**
   - What's the approval workflow?
   - How are users notified of status changes?
   - Is there a refill reminder system?

4. **Appointment Management:**
   - How does rescheduling work (especially for canceled appointments)?
   - Is there a pre-appointment checklist?
   - How do users join video calls?

5. **Referral System:**
   - How is the referral link generated?
   - Where do users track referral status?
   - How is the free month credit applied?

---

## Behavioral Design Elements

### Habit Formation Mechanisms:
1. **Injection Logging:** Quick access encourages consistent tracking
2. **Symptom Timing Guidance:** Helper text establishes routine
3. **Appointment Visibility:** Reduces missed consultations

### Motivation Triggers:
1. **Personalized Greeting:** Creates sense of relationship
2. **Referral Incentive:** Social sharing + financial reward
3. **Professional Photos:** Humanizes care team

### Friction Reduction:
1. **One-Tap Actions:** Minimal steps to core features
2. **Pre-filled Data:** (Inferred) Quick logging with smart defaults
3. **Contextual Help:** Helper text only where needed

---

## Conclusion

The Balance home screen demonstrates thoughtful UX design for a sensitive health context:

**Strengths:**
- Clear visual hierarchy prioritizes core medication management tasks
- Warm, approachable design reduces medical app anxiety
- Consistent design system enables scalability
- Behavioral nudges encourage adherence (helper text, visible appointments)
- Respects user control (dismissible banner, clear navigation)

**Strategic Design Choices:**
- Card-based modularity allows flexible content updates
- Personalization establishes connection
- Status-first information surfacing prevents missed actions
- Bottom navigation provides escape hatches from home hub

**Alignment with Product Vision:**
- Design supports sustainable weight loss through medication adherence
- Combines clinical needs (prescription, injection tracking) with behavioral support (symptom awareness, appointments)
- Human + AI collaboration evident (coach chat access, professional photos)

**Design System Maturity:**
- Defined color palette with functional coding
- Consistent component library (cards, navigation, buttons)
- Clear typography hierarchy
- Reusable spacing system

This analysis provides the foundation for documenting flows and designing new features that maintain consistency with the established Balance design language.

---

## Atomic Design Breakdown

### Overview
The Balance home screen follows atomic design principles, building from simple elements (atoms) to complex components (organisms) to the full page template.

---

### Atoms (Basic Building Blocks)

#### 1. Text Elements
**H1 Text Atom:**
- Font: Bold, large (32-36pt estimated)
- Color: Black (#000000)
- Example: "Bienvenido a Balance"

**H2 Text Atom:**
- Font: Bold, medium (20-24pt estimated)
- Color: Black (#000000)
- Example: "Próximas citas"

**H3 Text Atom:**
- Font: Bold, all caps (18-20pt estimated)
- Color: Red (#D32F2F)
- Example: "GANA UN MES GRATIS"

**Body Large Atom:**
- Font: Medium weight (16-18pt estimated)
- Color: Dark brown (#6B4423)
- Example: "Obtener receta", "Registrar inyección"

**Body Regular Atom:**
- Font: Regular weight (14-16pt estimated)
- Color: Black (#000000)
- Example: Helper text under symptom card

**Body Small Atom:**
- Font: Regular weight (12-14pt estimated)
- Color: Gray (#757575)
- Example: "Nutrición y Dietética"

**Caption Atom:**
- Font: Regular weight (10-12pt estimated)
- Color: Light brown (#A0826D)
- Example: "*Promoción por tiempo limitado"

---

#### 2. Icon Elements
**System Icons (24-32px):**
- Clipboard icon (prescription)
- Syringe icon (injection)
- Notepad/edit icon (symptoms)
- Video camera icon (virtual appointment)
- House icon (home nav)
- Message bubble icon (chat nav)
- Ascending chart icon (plan nav)
- Person silhouette icon (profile nav)
- Megaphone icon (promotional illustration)

**Navigation Icons (24px):**
- Chevron/arrow right (navigation affordance)
- X close button (dismiss action)

---

#### 3. Color Atoms
**Brand Colors:**
- Primary Brown: `#6B4423`
- Beige/Tan: `#F5E6D3`
- Light Peach: `#FFF4E8`

**Functional Colors:**
- Red (Urgent): `#D32F2F`
- Green (Positive): `#4CAF50`
- Gray (Inactive): `#757575`
- Black (Text): `#000000`
- White (Elevated): `#FFFFFF`

---

#### 4. Shape Atoms
**Border Radius:**
- Card corners: 12-16px
- Button corners: 20-24px (pill shape)
- Profile image: 50% (circular)
- Status badge: 16px (pill shape)

**Spacing Units:**
- XS: 4px
- S: 8px
- M: 12px
- L: 16px
- XL: 20px
- XXL: 24px

---

#### 5. Interactive Atoms
**Button Atom (Primary):**
- Background: Dark brown (#6B4423)
- Text: White
- Border-radius: 20-24px
- Padding: 12px vertical, 24px horizontal
- Example: "Invitar ahora"

**Status Badge Atom:**
- Background: Light red (#FFEBEE)
- Text: Red (#D32F2F)
- Dot indicator: Red circle (8px)
- Border-radius: 16px
- Padding: 4px 12px
- Example: "Cancelada"

---

### Molecules (Simple Component Combinations)

#### 1. Navigation Arrow Molecule
**Composition:**
- Icon atom (chevron right)
- Color: Brown or gray
- Size: 20-24px

**Purpose:** Indicates navigation/tap affordance

---

#### 2. Icon + Label Molecule
**Composition:**
- Icon atom (left)
- Spacing: 12-16px
- Text atom (right)

**Examples:**
- Clipboard + "Obtener receta"
- Syringe + "Registrar inyección"
- Video camera + "Balance - Primera Consulta Nutricionista"

**Layout:** Horizontal, center-aligned

---

#### 3. Status Badge Molecule
**Composition:**
- Status badge atom (background + border-radius)
- Dot indicator atom (colored circle)
- Text atom (status label)

**Variants:**
- Canceled: Red dot + red text
- Upcoming: Green dot + green text (inferred)
- Completed: Gray dot + gray text (inferred)

---

#### 4. Professional Info Molecule
**Composition:**
- Profile image atom (circular, 48-56px)
- Professional name text atom (bold, large)
- Specialty text atom (regular, small, gray)

**Layout:** Horizontal, profile image left, text stacked right

---

#### 5. Time Display Molecule (Status Bar)
**Composition:**
- Background pill shape (green)
- Text atom (white, time)

**Purpose:** OS-level time indicator with visual distinction

---

#### 6. Navigation Tab Molecule
**Composition:**
- Icon atom (top)
- Spacing: 4-8px
- Label text atom (bottom)

**Layout:** Vertical, center-aligned

**States:**
- Active: Brown icon + brown text
- Inactive: Gray icon + gray text

---

### Organisms (Complex UI Components)

#### 1. Action Card Organism
**Composition:**
- Container (beige background, rounded corners)
- Icon + Label molecule (left-aligned)
- Navigation arrow molecule (right-aligned)
- Optional: Helper text atom (below label)

**Variants:**
1. **Simple Action Card** (Prescription, Injection)
   - Icon + Label + Arrow only

2. **Action Card with Helper Text** (Symptoms)
   - Icon + Label + Arrow
   - Helper text below label

**Layout:**
- Flexbox: space-between
- Padding: 16-20px
- Gap between cards: 12-16px

**Behavior:**
- Tap: Navigate to destination screen
- Visual feedback: Likely darker background on press

---

#### 2. Appointment Card Organism
**Composition:**
- Container (white background, rounded corners, shadow)
- Status badge molecule (top-left)
- Icon + Label molecule (appointment type)
- Professional info molecule
- Spacing between elements: 8-12px

**Layout:**
- Vertical stack
- Padding: 16-20px
- Elevated appearance (subtle shadow)

**Information Hierarchy:**
- Status (most prominent) → Meeting type → Professional identity

**Behavior:**
- Tap: Navigate to appointment details
- Potential actions: Reschedule, add to calendar, join call

---

#### 3. Promotional Banner Organism
**Composition:**
- Container (light peach background, rounded corners)
- Close button molecule (top-right)
- Headline text atom (H3, red, bold)
- Body text atoms (stacked)
- Primary button atom ("Invitar ahora")
- Megaphone illustration (decorative, right side)

**Layout:**
- Padding: 16-20px
- Text left-aligned
- Illustration positioned to not obscure text
- Z-index: Close button on top

**Behavior:**
- Tap CTA button: Open share sheet
- Tap X: Dismiss banner (store preference)
- Possibly auto-dismisses after N views or days

---

#### 4. Bottom Navigation Organism
**Composition:**
- Container (fixed position, bottom)
- 4x Navigation tab molecules (equal width)
- Active state indicator (color change)

**Layout:**
- Horizontal distribution: 25% width each
- Border-top: 1px light gray (separator from content)
- Background: White
- Padding: 8-12px vertical

**Behavior:**
- Tap tab: Switch to selected screen
- Active tab updates color to brown
- Smooth transition between screens

---

#### 5. App Header Organism
**Composition:**
- Container (top of screen)
- Balance logo atom (centered)
- User greeting text atom ("Hola, Manu Nule")
- Welcome headline text atom ("Bienvenido a Balance")

**Layout:**
- Vertical stack, center-aligned
- Spacing: 8-12px between elements
- Padding: 16-20px

**Purpose:**
- Brand reinforcement
- Personalization
- Screen identification

---

#### 6. Section Header Organism
**Composition:**
- Heading text atom (H2)
- Optional: Action link or icon (right-aligned)

**Example:**
- "Próximas citas"

**Layout:**
- Horizontal, space-between if action included
- Margin-bottom: 12-16px

---

### Templates (Page-Level Layouts)

#### Home Screen Template
**Structure:**
```
┌─────────────────────────────┐
│ System Status Bar           │ (OS-level)
├─────────────────────────────┤
│ App Header Organism         │
├─────────────────────────────┤
│                             │
│ [Scrollable Content Area]   │
│                             │
│ - Action Card Organism      │
│ - Action Card Organism      │
│ - Action Card Organism      │
│                             │
│ - Promotional Banner Org    │
│                             │
│ - Section Header Organism   │
│ - Appointment Card Organism │
│                             │
│ [Bottom Padding]            │
│                             │
├─────────────────────────────┤
│ Bottom Navigation Organism  │ (Fixed)
└─────────────────────────────┘
```

**Layout Specifications:**
- Horizontal margins: 16-20px
- Vertical spacing between sections: 24px
- Vertical spacing between cards: 12-16px
- Safe area insets: Top (status bar), bottom (nav bar)

**Scroll Behavior:**
- Header: Scrolls with content (not sticky)
- Navigation: Fixed at bottom (always visible)
- Content area: Vertical scroll, bounce effect

---

### Pages (Specific Instances)

#### Balance Home Screen (Current Instance)
**Personalized Content:**
- User: "Manu Nule"
- Appointment status: "Cancelada"
- Professional: "Irene Roth Perez"
- Specialty: "Nutrición y Dietética"

**Active Features:**
- 3 action cards (prescription, injection, symptoms)
- Referral promotion banner (active/visible)
- 1 upcoming appointment (canceled status)

**Navigation State:**
- Active tab: "Inicio" (Home)
- Other tabs available: Chat, Plan, Perfil

---

### Atomic Design Benefits for Balance App

#### 1. Scalability
- **Atoms** can be reused across all screens
- Consistent color palette, typography, spacing
- Easy to add new action cards by reusing molecule patterns

#### 2. Consistency
- **Molecules** ensure uniform component behavior
- Icon + Label pattern used throughout app
- Status badge molecule can be applied to messages, tasks, etc.

#### 3. Maintenance
- **Organisms** define complex components once
- Updating action card styling updates all instances
- Design system changes cascade from atoms upward

#### 4. Collaboration
- **Templates** show layout structure for developers
- Designers can modify atoms without affecting page structure
- Clear handoff between design and development

#### 5. Testing
- **Atoms** can be unit tested
- **Molecules** can be tested in isolation
- **Organisms** can be tested with various data states
- **Pages** can be tested with real user scenarios

---

### Design System Implementation Guide

#### For Developers:

**1. Create Atom Components First:**
```typescript
// Example: Text atoms
const H1Text = styled.h1`
  font-size: 32px;
  font-weight: bold;
  color: #000000;
`;

const BodyText = styled.p`
  font-size: 16px;
  font-weight: normal;
  color: #000000;
`;

// Example: Color atoms
const colors = {
  brandBrown: '#6B4423',
  beige: '#F5E6D3',
  red: '#D32F2F',
  gray: '#757575',
};
```

**2. Compose Molecules from Atoms:**
```typescript
// Example: Icon + Label molecule
const IconLabel = ({ icon, label }) => (
  <Flex align="center" gap="12px">
    <Icon name={icon} size={24} />
    <BodyText>{label}</BodyText>
  </Flex>
);
```

**3. Build Organisms from Molecules:**
```typescript
// Example: Action Card organism
const ActionCard = ({ icon, label, helperText, onTap }) => (
  <Card background={colors.beige} borderRadius="16px" padding="16px" onPress={onTap}>
    <Flex justify="space-between" align="center">
      <IconLabel icon={icon} label={label} />
      <NavArrow />
    </Flex>
    {helperText && <HelperText>{helperText}</HelperText>}
  </Card>
);
```

**4. Assemble Templates:**
```typescript
// Example: Home screen template
const HomeTemplate = ({ user, actions, appointment, banner }) => (
  <Screen>
    <AppHeader user={user} />
    <ScrollView>
      {actions.map(action => (
        <ActionCard key={action.id} {...action} />
      ))}
      {banner && <PromotionalBanner {...banner} />}
      <SectionHeader title="Próximas citas" />
      <AppointmentCard {...appointment} />
    </ScrollView>
    <BottomNavigation />
  </Screen>
);
```

---

### Component Reusability Map

#### Atoms Used Across Multiple Organisms:
- **Body Text Atom:** Used in action cards, appointment cards, banner, navigation
- **Icon Atom:** Used in action cards, navigation, appointment cards
- **Brand Brown Color:** Used in buttons, active nav state, text highlights
- **Border Radius (16px):** Used in all card organisms

#### Molecules Used Across Multiple Organisms:
- **Icon + Label:** Used in action cards, appointment cards, navigation tabs
- **Navigation Arrow:** Used in all action cards, potentially in list views
- **Status Badge:** Used in appointment cards, could be used for message status, task status

#### Organisms That Can Be Reused:
- **Action Card:** Can be used for any navigation task (not just home screen)
- **Section Header:** Can be used to divide any screen into sections
- **Bottom Navigation:** Used globally across all main screens

---

### Atomic Design Documentation Best Practices

#### 1. Naming Conventions:
- **Atoms:** Descriptive + type (e.g., `H1Text`, `PrimaryButton`, `BrandBrownColor`)
- **Molecules:** Function + structure (e.g., `IconLabel`, `StatusBadge`, `NavArrow`)
- **Organisms:** Component name (e.g., `ActionCard`, `AppointmentCard`, `BottomNavigation`)
- **Templates:** Screen name + "Template" (e.g., `HomeTemplate`, `ChatTemplate`)
- **Pages:** Screen name (e.g., `HomeScreen`, `ProfileScreen`)

#### 2. Documentation Structure:
- **Atoms:** List all variants, specs (size, color, weight)
- **Molecules:** Show composition diagram, props, states
- **Organisms:** Show full component, layout specs, behavior, variants
- **Templates:** Show wireframe, responsive breakpoints, scroll behavior
- **Pages:** Show with real content, all states (loading, error, empty, populated)

#### 3. Variant Management:
- Document all variants at each level
- Example: ActionCard has 2 variants (with/without helper text)
- Example: StatusBadge has 3 variants (canceled, upcoming, completed)

---

### Figma Organization (Recommended)

**Atomic Design File Structure:**
```
Balance Design System/
├── 📄 Atoms
│   ├── Colors
│   ├── Typography
│   ├── Icons
│   ├── Shapes
│   └── Spacing
├── 📄 Molecules
│   ├── Icon + Label
│   ├── Status Badge
│   ├── Navigation Arrow
│   └── Professional Info
├── 📄 Organisms
│   ├── Action Card
│   ├── Appointment Card
│   ├── Promotional Banner
│   └── Bottom Navigation
├── 📄 Templates
│   ├── Home Screen Layout
│   ├── Detail Screen Layout
│   └── Modal Layout
└── 📄 Pages (Examples)
    ├── Home - Default State
    ├── Home - No Appointments
    └── Home - Multiple Banners
```

---

### Next Steps for Atomic Design Implementation

1. **Audit Existing Screens:**
   - Identify all atoms currently in use
   - Document variants and specs
   - Ensure consistency across screens

2. **Build Figma Component Library:**
   - Create atoms as Figma styles (colors, text styles)
   - Build molecules as components
   - Build organisms as complex components with variants
   - Create templates with auto-layout

3. **Developer Handoff:**
   - Map Figma components to code components
   - Document props and states
   - Provide usage examples

4. **Design System Documentation:**
   - Create living documentation site (Storybook, Zeroheight)
   - Show all components with interactive examples
   - Include do's and don'ts

5. **Governance:**
   - Establish process for adding new atoms
   - Review process for modifying existing components
   - Version control for design system updates

---

## Next Steps for Flow Documentation

1. **Map SCN_HOME in Balance_App_Flow.md**
   - Document all exit points from home screen
   - Link to destination screens (when designed)

2. **Design Missing Flows**
   - Prescription request end-to-end
   - Injection logging + symptom tracking loop
   - Appointment rescheduling

3. **Create Component Library**
   - Action Card component spec
   - Appointment Card component spec
   - Banner component spec
   - Document in design system file

4. **Define Interaction Patterns**
   - Tap, swipe, long-press behaviors
   - Modal vs. full-screen navigation decisions
   - Success/error state patterns

5. **Accessibility Audit**
   - Screen reader testing
   - Color contrast verification
   - Dynamic type support

---

**Document Version:** 1.0
**Last Updated:** 2025-11-07
**Author:** Flow Designer Agent
**Related Documents:**
- Balance_App_Flow.md
- Vision_Balance.md
- Design_System_Specifications.md (to be created)
