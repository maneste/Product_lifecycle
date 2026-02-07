# Development & Deployment Guide for Claude Code Projects

**Reference Guide for Setting Up, Building, and Deploying Features**

---

## Table of Contents

1. [Repository Setup After Cloning](#repository-setup-after-cloning)
2. [Common Claude Code Development Workflow](#common-claude-code-development-workflow)
3. [Easy Deployment Platforms](#easy-deployment-platforms)
4. [Recommended Stack for Your MVP](#recommended-stack-for-your-mvp)
5. [Quick Start Guides](#quick-start-guides)
6. [Platform Comparison](#platform-comparison)
7. [Recommended Workflow](#recommended-workflow)
8. [Experiment & Analytics Tools](#experiment--analytics-tools)

---

## Repository Setup After Cloning

After cloning this repository, several folders need to be created manually because they are either gitignored or require local symlinks. Follow these steps in order.

### What You Get After Cloning (Tracked in Git)

These folders and files are already included in the repository:

| Folder | Description |
|--------|-------------|
| `.claude/agents/` | Custom agent configurations (prdDiscovery, flowDesigner, frontendUI, backend) |
| `.claude/commands/` | Custom slash commands (/init-context, /update-*, /transcripts) |
| `AI_Output/` | Agent-generated feature documentation (staging area) |
| `context_knowledge/` | Private knowledge base (opportunity tree, benchmarks, personas, etc.) |
| `context_knowledge_markdown/` | Markdown versions of context knowledge files |
| `User_discovery/` | User interview processing scripts and tools |
| `feature-template/` | Code and implementation templates |

### What You Need to Create (Not in Git)

These folders are gitignored and must be recreated on each machine:

| Folder | Purpose | Sync Method |
|--------|---------|-------------|
| `features/` | Finalized feature docs & research outputs | OneDrive symlink |
| `Transcriptions/` | Raw transcripts & processed interview outputs | Google Drive symlinks + local folder |
| `.env` files | API keys for scripts | Manual creation |

---

### Step 1: Set Up the `features/` Folder (OneDrive Symlink)

The `features/` folder stores finalized feature documentation and user research outputs. It syncs via OneDrive.

**Prerequisites:** OneDrive desktop app installed and signed in.

```bash
cd Feature_Building

# Create the OneDrive folder (first time only, on your primary device)
mkdir -p ~/Library/CloudStorage/OneDrive-Personal/Claude_Balance_Features

# Create symlink from repository to OneDrive
ln -s ~/Library/CloudStorage/OneDrive-Personal/Claude_Balance_Features features

# Verify
ls -la features
# Should show: features -> /Users/.../OneDrive-Personal/Claude_Balance_Features
```

**What goes here:**
- `features/doc_[Feature_Name]/` - Finalized PRDs, flows, specs (moved from AI_Output after review)
- `features/doc_User_Research/outputs/` - User research pipeline outputs (CSV, JSON, reports)

**On a new device** (OneDrive already has the data):
```bash
# Just create the symlink - OneDrive syncs the content automatically
ln -s ~/Library/CloudStorage/OneDrive-Personal/Claude_Balance_Features features
```

---

### Step 2: Set Up the `Transcriptions/` Folder (Google Drive Symlinks)

The `Transcriptions/` folder provides access to raw transcript files from Google Drive and stores processed interview outputs locally.

**Prerequisites:** Google Drive desktop app installed, signed in, and synced.

```bash
cd Feature_Building

# Create the Transcriptions folder
mkdir -p Transcriptions

cd Transcriptions

# Create symlink to user research interview transcripts
ln -s ~/Library/CloudStorage/GoogleDrive-m.lema@findbalance_app/Mi\ unidad/Meet\ Recordings/Trans_MD transcription_source

# Create symlink to first consultation transcripts
ln -s ~/Library/CloudStorage/GoogleDrive-m.lema@findbalance_app/Mi\ unidad/Meet\ Recordings/1st_DoctorTranscript 1st_consultation_source

# Create the processed interviews folder (output from User_discovery scripts)
mkdir -p processed_interviews

cd ..
```

**Verify setup:**
```bash
ls -la Transcriptions/
# Should show:
#   transcription_source -> /Users/.../GoogleDrive-.../Trans_MD
#   1st_consultation_source -> /Users/.../GoogleDrive-.../1st_DoctorTranscript
#   processed_interviews/   (empty directory)

# Test symlinks work
ls Transcriptions/transcription_source/
ls Transcriptions/1st_consultation_source/
```

**What goes here:**

| Subfolder | Type | Description |
|-----------|------|-------------|
| `transcription_source/` | Symlink | Google Drive user research transcripts (input) |
| `1st_consultation_source/` | Symlink | Google Drive first consultation transcripts (input) |
| `processed_interviews/` | Local folder | Output from User_discovery processing (markdown + JSON per interview) |

**Different Google account?** Adjust the symlink paths:
```bash
# List available Google Drive accounts
ls ~/Library/CloudStorage/ | grep GoogleDrive

# Use your account path
ln -s ~/Library/CloudStorage/GoogleDrive-YOUR_EMAIL/Mi\ unidad/Meet\ Recordings/Trans_MD transcription_source
```

---

### Step 3: Set Up Environment Variables

Several scripts require API keys stored in `.env` files (which are gitignored).

**User_discovery scripts (OpenAI):**
```bash
# Create .env file in User_discovery/
cat > User_discovery/.env << 'EOF'
OPENAI_API_KEY=your-openai-api-key-here
EOF
```

**User_research scripts (Latitude API):**
```bash
# If using the user_research pipeline, check its docs for required env vars
# See: user_research/docs/RUN_WITHOUT_AI.md
```

---

### Step 4: Verify Everything Works

Run this verification checklist:

```bash
cd Feature_Building

# 1. Check features/ symlink
echo "--- features/ ---"
ls -la features 2>/dev/null || echo "MISSING: features symlink not created"

# 2. Check Transcriptions/ folder and symlinks
echo "--- Transcriptions/ ---"
ls -la Transcriptions/ 2>/dev/null || echo "MISSING: Transcriptions folder not created"

# 3. Check transcription_source symlink works
echo "--- transcription_source ---"
ls Transcriptions/transcription_source/ > /dev/null 2>&1 && echo "OK" || echo "BROKEN: transcription_source symlink"

# 4. Check 1st_consultation_source symlink works
echo "--- 1st_consultation_source ---"
ls Transcriptions/1st_consultation_source/ > /dev/null 2>&1 && echo "OK" || echo "BROKEN: 1st_consultation_source symlink"

# 5. Check processed_interviews folder exists
echo "--- processed_interviews ---"
ls -d Transcriptions/processed_interviews/ > /dev/null 2>&1 && echo "OK" || echo "MISSING: processed_interviews folder"

# 6. Check context_knowledge exists (should be in git)
echo "--- context_knowledge ---"
ls context_knowledge/opportunity_tree.json > /dev/null 2>&1 && echo "OK" || echo "MISSING: context_knowledge files"

# 7. Check .env exists for User_discovery
echo "--- .env ---"
ls User_discovery/.env > /dev/null 2>&1 && echo "OK" || echo "MISSING: User_discovery/.env (needed for OpenAI scripts)"
```

**Expected result:** All checks should show "OK".

---

### Quick Reference: Complete Setup Commands

Copy-paste this block to set up everything at once on a new machine:

```bash
# Clone the repository
git clone <your-repo-url>
cd Feature_Building

# 1. features/ → OneDrive symlink
ln -s ~/Library/CloudStorage/OneDrive-Personal/Claude_Balance_Features features

# 2. Transcriptions/ folder with Google Drive symlinks
mkdir -p Transcriptions
ln -s ~/Library/CloudStorage/GoogleDrive-m.lema@findbalance_app/Mi\ unidad/Meet\ Recordings/Trans_MD Transcriptions/transcription_source
ln -s ~/Library/CloudStorage/GoogleDrive-m.lema@findbalance_app/Mi\ unidad/Meet\ Recordings/1st_DoctorTranscript Transcriptions/1st_consultation_source
mkdir -p Transcriptions/processed_interviews

# 3. Environment variables
echo 'OPENAI_API_KEY=your-key-here' > User_discovery/.env

# Done! Verify with:
ls -la features Transcriptions/
```

---

### Folder Map: What's Tracked vs. Not Tracked

```
Feature_Building/
│
│   TRACKED (in git - available after clone)
├── .claude/agents/                    # Agent configs
├── .claude/commands/                  # Slash commands
├── AI_Output/                         # Feature docs staging area
├── context_knowledge/                 # Knowledge base (opportunity tree, personas, etc.)
├── context_knowledge_markdown/        # Markdown versions
├── User_discovery/                    # Interview processing scripts
├── feature-template/                  # Code templates
├── CLAUDE.md                          # Project instructions
├── Development_and_Deployment_Guide.md # This file
├── .gitignore
│
│   NOT TRACKED (must be created after clone)
├── features/                          # → OneDrive symlink (Step 1)
├── Transcriptions/                    # Google Drive symlinks + local data (Step 2)
│   ├── transcription_source/          # → Google Drive symlink
│   ├── 1st_consultation_source/       # → Google Drive symlink
│   └── processed_interviews/          # Local folder for outputs
└── User_discovery/.env                # API keys (Step 3)
```

---

### Troubleshooting Setup

**Symlink shows "No such file or directory":**
- Cloud storage app (OneDrive/Google Drive) may not be synced yet
- Check the app is running and signed in
- Wait for initial sync to complete

**Different machine path:**
- OneDrive path may differ. Check: `ls ~/Library/CloudStorage/ | grep OneDrive`
- Google Drive email may differ. Check: `ls ~/Library/CloudStorage/ | grep GoogleDrive`

**features/ already exists as a regular folder:**
```bash
# Move existing content, then create symlink
mv features features_backup
ln -s ~/Library/CloudStorage/OneDrive-Personal/Claude_Balance_Features features
mv features_backup/* features/
rm -rf features_backup
```

---

## Common Claude Code Development Workflow

### Typical Development Pattern

**1. Ideation & Planning**
- Use Claude Code to create PRDs, flow diagrams
- Generate implementation specs
- Break down complex features into tasks

**2. Local Development**
- Claude Code helps write code, fix bugs, refactor
- Run tests locally
- Iterate quickly with AI assistance

**3. Git Integration**
- Commit frequently (Claude Code can help with git commands)
- Push to GitHub/GitLab
- Deploy from repository

**4. Deploy & Experiment**
- Deploy to cloud platform
- Run experiments with real users
- Collect data and iterate

---

## Easy Deployment Platforms

### Best Options for Quick Deployment

#### 1. Vercel - Best for Full-Stack Web Apps

**Use For:** React, Next.js, static sites, serverless functions

**Why Choose Vercel:**
- Deploy in 60 seconds
- Automatic HTTPS
- Preview deployments for every git push
- Zero configuration needed
- Excellent developer experience

**Quick Setup:**
```bash
npm install -g vercel
vercel  # That's it!
```

**Pricing:**
- Free tier: Perfect for experiments and MVP
- Pro: $20/month (if you need more)

**Best For:**
- Your Pre-Consultation Report (frontend + serverless backend)
- Any web application with API needs
- Landing pages and marketing sites

**Pros:**
- Easiest deployment experience
- Excellent documentation
- Automatic CI/CD from GitHub
- Edge functions (serverless)
- Global CDN

**Cons:**
- Not ideal for long-running background jobs
- Serverless functions have 10s timeout (free tier)

---

#### 2. Railway - Best for Backend & Databases

**Use For:** Python/Node backends, PostgreSQL, Redis, Docker containers

**Why Choose Railway:**
- Zero config deployment
- Automatic deployments from GitHub
- Built-in databases (PostgreSQL, MySQL, Redis)
- Simple pricing model

**Quick Setup:**
1. Connect GitHub repository
2. Railway auto-detects your stack
3. Click "Deploy"
4. Done!

**Pricing:**
- Free tier: $5/month credit (enough for experiments)
- Pay-as-you-go after free credit

**Best For:**
- Your report generation backend
- APIs with database requirements
- Background job processors

**Pros:**
- Includes databases out of the box
- No timeout limits
- Simple environment variable management
- Great for monolithic apps

**Cons:**
- Can get expensive with scale
- Less mature than AWS/Vercel

---

#### 3. Replit - Best for Quick Prototypes

**Use For:** Quick prototypes, testing ideas immediately, collaborative coding

**Why Choose Replit:**
- Code in browser (no local setup)
- Instant deploy with live URL
- Collaborative (multiplayer coding)
- Built-in database (Replit DB)

**Quick Setup:**
1. Go to replit.com
2. Create new Repl (choose language)
3. Paste/write your code
4. Click "Run"
5. Get instant live URL

**Pricing:**
- Free tier: Basic features, public Repls
- Hacker: $7/month (private Repls, always-on)

**Best For:**
- Testing MVP concepts this week
- Quick demos for stakeholders
- Learning and experimentation

**Pros:**
- Zero setup required
- Fastest time to live deployment
- Great for collaboration
- Built-in AI assistant

**Cons:**
- Not recommended for production
- Performance limitations
- Limited customization

---

#### 4. Other Options

**Render** (Similar to Railway)
- Good for Docker deployments
- Free tier available
- $7/month for basic apps

**Heroku** (Traditional PaaS)
- No longer has free tier
- Starting at $7/month
- Good for legacy apps
- More complex than modern alternatives

**AWS/GCP/Azure** (Enterprise Scale)
- Most powerful, most complex
- Cheapest at scale (but complex pricing)
- Steep learning curve
- Use only if you need specific services

---

## Recommended Stack for Your MVP

### Pre-Consultation Engagement Report Architecture

```
┌─────────────────────────────────────┐
│  Typeform (Pre-call Form)           │
│  - Form submission trigger          │
│  - Webhook to backend               │
└──────────────┬──────────────────────┘
               │
               │ POST webhook
               ↓
┌─────────────────────────────────────┐
│  Backend (Railway or Vercel)        │
│  - Python Flask/FastAPI             │
│  - Generate personalized report     │
│  - Calculate BMI                    │
│  - Store report in database         │
│  - Queue email job                  │
└──────────────┬──────────────────────┘
               │
               │ API call
               ↓
┌─────────────────────────────────────┐
│  Sendgrid (Email Delivery)          │
│  - Send personalized email          │
│  - Track opens and clicks           │
└──────────────┬──────────────────────┘
               │
               │ User clicks link
               ↓
┌─────────────────────────────────────┐
│  Report Page (Vercel/Railway)       │
│  - Static HTML with personalization │
│  - Mobile responsive                │
│  - Google Analytics tracking        │
│  - CTA buttons                      │
└─────────────────────────────────────┘
```

**Estimated Cost:** $0-15/month during MVP phase

**Components:**
- **Typeform:** Free plan (or existing subscription)
- **Backend:** Railway free tier ($5 credit)
- **Sendgrid:** Free tier (100 emails/day)
- **Hosting:** Vercel free tier
- **Database:** Railway PostgreSQL (included)
- **Analytics:** Google Analytics (free)

---

## Quick Start Guides

### Option A: Vercel (Recommended)

**Why:** Single platform for frontend + serverless backend, super easy

**Complete Setup:**

```bash
# 1. Create project structure
mkdir balance-report-mvp
cd balance-report-mvp

# 2. Initialize project
npm init -y

# 3. Create project structure
mkdir -p api public/templates

# 4. Create files
touch api/webhook.py
touch api/report.py
touch public/templates/report.html
touch vercel.json
touch requirements.txt

# 5. Install Vercel CLI
npm install -g vercel

# 6. Deploy
vercel

# Follow prompts:
# - Link to existing project? No
# - Project name? balance-report-mvp
# - Directory? ./
# - Build command? (leave empty)
```

**You get:**
- Live URL: `https://balance-report-mvp.vercel.app`
- Automatic HTTPS
- Preview URLs for every git push
- Environment variables management

**File Structure:**
```
balance-report-mvp/
├── api/
│   ├── webhook.py          # Typeform webhook handler
│   └── report.py           # Report page renderer
├── public/
│   ├── templates/
│   │   └── report.html     # Report template
│   └── styles.css
├── vercel.json             # Vercel config
├── requirements.txt        # Python dependencies
└── package.json
```

**vercel.json Example:**
```json
{
  "version": 2,
  "builds": [
    {
      "src": "api/*.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/api/(.*)",
      "dest": "/api/$1"
    },
    {
      "src": "/(.*)",
      "dest": "/public/$1"
    }
  ]
}
```

**requirements.txt Example:**
```
flask==2.3.0
sendgrid==6.10.0
psycopg2-binary==2.9.6
python-dotenv==1.0.0
```

**Deploying Updates:**
```bash
# Just push to git or run:
vercel --prod
```

---

### Option B: Railway (For Backend + Database)

**Why:** Best if you need a persistent database and background jobs

**Complete Setup:**

```bash
# 1. Create project
mkdir balance-backend
cd balance-backend

# 2. Initialize git
git init
git add .
git commit -m "Initial commit"

# 3. Push to GitHub
# (Create repo on GitHub first)
git remote add origin https://github.com/yourusername/balance-backend.git
git push -u origin main

# 4. Go to railway.app
# - Sign up with GitHub
# - "New Project" → "Deploy from GitHub repo"
# - Select your repository
# - Railway auto-detects and deploys!

# 5. Add PostgreSQL
# - Click "New" → "Database" → "Add PostgreSQL"
# - Automatically connected to your app

# 6. Add environment variables
# - Go to Variables tab
# - Add SENDGRID_API_KEY, etc.
```

**You get:**
- Live backend URL
- PostgreSQL database
- Automatic deployments on git push
- Environment variables management
- Free $5/month credit

**Project Structure:**
```
balance-backend/
├── main.py                 # Flask/FastAPI app
├── models.py               # Database models
├── utils/
│   ├── bmi_calculator.py
│   ├── email_sender.py
│   └── report_generator.py
├── requirements.txt
├── Procfile               # Railway uses this
└── runtime.txt            # Python version
```

**Procfile Example:**
```
web: gunicorn main:app
```

---

### Option C: Replit (Fastest for Prototyping)

**Why:** Test the concept in 10 minutes, zero setup

**Complete Setup:**

1. Go to [replit.com](https://replit.com)
2. Click "Create Repl"
3. Choose "Python" or "Flask"
4. Name it "balance-report-mvp"
5. Paste your code into `main.py`
6. Click "Run"
7. You get instant live URL!

**Example Flask App:**
```python
from flask import Flask, render_template_string, request

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    # Process Typeform data
    return {"status": "success"}

@app.route('/report/<token>')
def report(token):
    # Load report data
    html = """
    <!DOCTYPE html>
    <html>
    <head><title>Balance Report</title></head>
    <body>
        <h1>Your Personalized Report</h1>
        <p>Report token: {{ token }}</p>
    </body>
    </html>
    """
    return render_template_string(html, token=token)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
```

**You get:**
- Instant URL: `https://balance-report-mvp.yourname.repl.co`
- Built-in database (Replit DB)
- Version control
- Collaborative editing

---

## Platform Comparison

| Platform | Best For | Setup Time | Monthly Cost | Difficulty | Production Ready |
|----------|----------|------------|--------------|------------|------------------|
| **Vercel** | Full-stack web apps | 5 min | Free-$20 | Easy | Yes |
| **Railway** | Backends + databases | 10 min | $5+ | Easy | Yes |
| **Replit** | Quick prototypes | 2 min | Free-$7 | Easiest | Limited |
| **Render** | Docker apps | 10 min | $7+ | Easy | Yes |
| **Heroku** | Traditional apps | 15 min | $7+ | Medium | Yes |
| **AWS** | Enterprise scale | Hours | $10+ | Hard | Yes |

### Decision Matrix

**Choose Vercel if:**
- Building a web app with frontend + API
- Want the easiest deployment experience
- Need fast iteration with preview deployments
- Want automatic scaling

**Choose Railway if:**
- Need a persistent database
- Running background jobs
- Want simple pricing
- Prefer traditional backend architecture

**Choose Replit if:**
- Testing a concept quickly
- Collaborating with others
- Learning and experimenting
- Not for production (yet)

---

## Recommended Workflow

### Phase 1: Prototype (Week 1)

**Goal:** Validate concept with stakeholders

**Platform:** Replit (fastest)

**Tasks:**
```
1. Build quick prototype on Replit
2. Use fake/mock data
3. Create basic report page
4. Demo to stakeholders
5. Collect feedback
```

**Deliverable:** Working prototype with live URL

---

### Phase 2: MVP Development (Weeks 2-4)

**Goal:** Build production-ready MVP

**Platform:** Vercel (frontend + API) + Railway (database)

**Tasks:**
```
1. Set up Vercel project
   - Serverless webhook handler
   - Report page templates
   - Environment variables

2. Set up Railway database
   - PostgreSQL for reports
   - Store user data
   - Track engagement

3. Integrate Sendgrid
   - Email templates
   - Webhook tracking

4. Connect to real Typeform
   - Configure webhook
   - Test with real data

5. Deploy to production
   - Custom domain (optional)
   - Analytics tracking
   - Error monitoring
```

**Deliverable:** Production MVP with real users

---

### Phase 3: Experiment & Iterate (Weeks 5-8)

**Goal:** Measure impact, iterate based on data

**Platform:** Same as Phase 2 + Analytics

**Tasks:**
```
1. Add PostHog for tracking
   - User events
   - Conversion funnels
   - Feature flags

2. Run A/B experiment
   - 50% get report (treatment)
   - 50% don't (control)
   - Track both cohorts

3. Measure no-show rates
   - Pull data weekly
   - Calculate statistical significance
   - Compare cohorts

4. Collect user feedback
   - 5-10 interviews
   - Survey via email
   - Qualitative insights

5. Iterate based on data
   - If success: Scale to 100%, plan V2
   - If failure: Iterate on content/timing
```

**Deliverable:** Data-driven decision on next steps

---

## Experiment & Analytics Tools

### PostHog (Recommended)

**Why:** Open-source, privacy-friendly, all-in-one

**Features:**
- Product analytics
- Session recording
- Feature flags
- A/B testing
- Event tracking

**Pricing:**
- Free: 1M events/month
- Paid: $0.00031 per event after free tier

**Setup:**
```html
<!-- Add to your report page -->
<script>
    !function(t,e){var o,n,p,r;e.__SV||(window.posthog=e,e._i=[],e.init=function(i,s,a){function g(t,e){var o=e.split(".");2==o.length&&(t=t[o[0]],e=o[1]),t[e]=function(){t.push([e].concat(Array.prototype.slice.call(arguments,0)))}}(p=t.createElement("script")).type="text/javascript",p.async=!0,p.src=s.api_host+"/static/array.js",(r=t.getElementsByTagName("script")[0]).parentNode.insertBefore(p,r);var u=e;for(void 0!==a?u=e[a]=[]:a="posthog",u.people=u.people||[],u.toString=function(t){var e="posthog";return"posthog"!==a&&(e+="."+a),t||(e+=" (stub)"),e},u.people.toString=function(){return u.toString(1)+".people (stub)"},o="capture identify alias people.set people.set_once set_config register register_once unregister opt_out_capturing has_opted_out_capturing opt_in_capturing reset isFeatureEnabled onFeatureFlags getFeatureFlag getFeatureFlagPayload reloadFeatureFlags group updateEarlyAccessFeatureEnrollment getEarlyAccessFeatures getActiveMatchingSurveys getSurveys".split(" "),n=0;n<o.length;n++)g(u,o[n]);e._i.push([i,s,a])},e.__SV=1)}(document,window.posthog||[]);
    posthog.init('YOUR_PROJECT_API_KEY', {api_host: 'https://app.posthog.com'})
</script>

<!-- Track custom events -->
<script>
    // Track report view
    posthog.capture('report_viewed', {
        report_id: '{{ report.id }}',
        experiment_group: 'mvp_treatment'
    });

    // Track CTA click
    function trackCTA() {
        posthog.capture('cta_clicked', {
            cta_type: 'confirm_attendance'
        });
    }
</script>
```

---

### Google Analytics 4 (Simple Alternative)

**Why:** Free, familiar, good for basic tracking

**Setup:**
```html
<!-- Global site tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=GA_MEASUREMENT_ID"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'GA_MEASUREMENT_ID');

  // Custom events
  gtag('event', 'report_view', {
    'event_category': 'engagement',
    'report_id': '{{ report.id }}'
  });
</script>
```

---

### A/B Testing Setup

**Using Feature Flags (PostHog):**

```python
# Backend: Assign users to cohorts
from posthog import Posthog

posthog = Posthog('YOUR_PROJECT_API_KEY')

def should_send_report(user_email):
    # 50/50 split based on email hash
    import hashlib
    hash_val = int(hashlib.md5(user_email.encode()).hexdigest(), 16)
    return hash_val % 2 == 0  # 50% get report

# In webhook handler
if should_send_report(user_data['email']):
    generate_and_send_report(user_data)
    posthog.capture(user_data['email'], 'assigned_to_treatment')
else:
    posthog.capture(user_data['email'], 'assigned_to_control')
```

---

## Quick Reference Commands

### Vercel

```bash
# Install CLI
npm install -g vercel

# Login
vercel login

# Deploy to preview
vercel

# Deploy to production
vercel --prod

# View logs
vercel logs

# List deployments
vercel ls

# Set environment variable
vercel env add SENDGRID_API_KEY
```

### Railway

```bash
# Install CLI
npm install -g @railway/cli

# Login
railway login

# Link to project
railway link

# View logs
railway logs

# Run command in Railway environment
railway run python main.py

# Open in browser
railway open
```

### Git Workflow

```bash
# Create feature branch
git checkout -b feature/report-mvp

# Commit changes
git add .
git commit -m "Add report generation"

# Push to GitHub
git push origin feature/report-mvp

# Merge to main (after review)
git checkout main
git merge feature/report-mvp
git push origin main

# Both Vercel and Railway auto-deploy on push to main
```

---

## Environment Variables

### Required Variables

**Backend (.env file):**
```bash
# Database
DATABASE_URL=postgresql://user:password@host:5432/dbname

# Email
SENDGRID_API_KEY=SG.xxxxxxxxxxxxx
SENDGRID_FROM_EMAIL=reports@balance.com

# Typeform
TYPEFORM_WEBHOOK_SECRET=xxxxxxxxx

# App
SECRET_KEY=your-secret-key-here
ENVIRONMENT=production

# Analytics
POSTHOG_API_KEY=phc_xxxxxxxxx
GA_MEASUREMENT_ID=G-XXXXXXXXXX
```

**How to Set in Vercel:**
```bash
vercel env add DATABASE_URL
vercel env add SENDGRID_API_KEY
# etc...
```

**How to Set in Railway:**
- Go to project dashboard
- Click "Variables" tab
- Add each variable
- Railway auto-restarts app

---

## Monitoring & Debugging

### Vercel Logs

```bash
# Real-time logs
vercel logs --follow

# Recent logs
vercel logs

# Specific function logs
vercel logs api/webhook.py
```

### Railway Logs

```bash
# Via CLI
railway logs --tail 100

# Or in dashboard
# Go to project → Deployments → View logs
```

### Error Tracking

**Sentry (Recommended for Production):**

```python
# Install
pip install sentry-sdk

# Initialize
import sentry_sdk
sentry_sdk.init(
    dsn="YOUR_SENTRY_DSN",
    traces_sample_rate=1.0
)

# Errors automatically captured
```

**Free tier:** 5,000 errors/month

---

## Checklist: Before Going Live

### Pre-Launch Checklist

**Technical:**
- [ ] All environment variables set
- [ ] Database migrations run
- [ ] HTTPS enabled (automatic on Vercel/Railway)
- [ ] CORS configured if needed
- [ ] Rate limiting implemented
- [ ] Error logging setup (Sentry)
- [ ] Backup strategy for database

**Testing:**
- [ ] Test webhook with real Typeform
- [ ] Test email delivery (Sendgrid sandbox mode)
- [ ] Test report page on mobile devices
- [ ] Test all links and CTAs
- [ ] Load testing (if expecting high volume)
- [ ] Edge cases tested (missing data, etc.)

**Analytics:**
- [ ] Google Analytics / PostHog installed
- [ ] Custom events configured
- [ ] Conversion funnels set up
- [ ] A/B test cohorts defined

**Legal & Compliance:**
- [ ] Privacy policy updated
- [ ] Terms of service mention report feature
- [ ] GDPR compliance (if applicable)
- [ ] Medical disclaimer included in report
- [ ] Unsubscribe link in emails

**Monitoring:**
- [ ] Uptime monitoring (UptimeRobot or similar)
- [ ] Error alerts configured
- [ ] Performance monitoring
- [ ] Email delivery monitoring

---

## Cost Estimates

### MVP Phase (Months 1-3)

| Service | Tier | Monthly Cost |
|---------|------|--------------|
| Vercel | Hobby (Free) | $0 |
| Railway | Free credits | $0-5 |
| Sendgrid | Free (100/day) | $0 |
| Google Analytics | Free | $0 |
| PostHog | Free (1M events) | $0 |
| Domain (optional) | .com | $12/year |
| **Total** | | **$0-5/month** |

### Growth Phase (100+ users/day)

| Service | Tier | Monthly Cost |
|---------|------|--------------|
| Vercel | Pro | $20 |
| Railway | Pro | $20 |
| Sendgrid | Essentials | $15 |
| PostHog | Growth | $0 (pay per use) |
| Sentry | Team | $26 |
| **Total** | | **$81/month** |

---

## Resources & Documentation

### Official Docs

- **Vercel:** https://vercel.com/docs
- **Railway:** https://docs.railway.app
- **Replit:** https://docs.replit.com
- **PostHog:** https://posthog.com/docs
- **Sendgrid:** https://docs.sendgrid.com

### Community & Support

- **Vercel Discord:** https://vercel.com/discord
- **Railway Discord:** https://discord.gg/railway
- **PostHog Slack:** https://posthog.com/slack

### Tutorials

- **Vercel + Python:** https://vercel.com/docs/frameworks/python
- **Railway Quickstart:** https://docs.railway.app/quick-start
- **A/B Testing Guide:** https://posthog.com/docs/experiments

---

## Next Steps

### Ready to Start?

1. **Set up the repository** (follow [Repository Setup](#repository-setup-after-cloning) above)
2. **Choose your platform** (Recommendation: Vercel for MVP)
3. **Set up account** (5 minutes)
4. **Create basic project** (30 minutes)
5. **Deploy hello world** (5 minutes)
6. **Iterate with real feature** (ongoing)

### Need Help?

Ask Claude Code to:
- Generate complete Vercel/Railway setup
- Write serverless functions
- Create deployment configs
- Set up analytics tracking
- Debug deployment issues

---

**Last Updated:** February 2026

**Maintained by:** Your Engineering Team

**Questions?** Update this guide as you learn!
