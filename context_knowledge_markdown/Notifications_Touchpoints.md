# Notifications and Touchpoints

This document outlines all notification touchpoints and communication flows across the Balance user journey.

## Overview

This comprehensive list covers all automated and manual touchpoints organized by stage in the customer journey: Acquisition, Activation, Retention, and Churn.

## Touchpoints by Stage

### Acquisition Stage

| Touchpoint Name | Channel | Tool/Platform | Condition/Rules | Trigger/Timing | Purpose/Goal | Owner | Audience | Status | Notes |
|----------------|---------|---------------|-----------------|----------------|--------------|-------|----------|--------|-------|
| Contact leads with AI | WA | Make | - | - | - | Tech/Product | Leads | Paused | - |
| Contact leads with AI 2 | WA | Make | - | - | - | Tech/Product | Leads | Paused | - |
| Whatsapp leads not answered | Email | Sendgrid | First time contact added to Whatsapp Answer but not Download App (MQLS + Contacted) | Instantly and after 4 days and after 4 days | To contact us by Whatsapp | Marketing | Leads | Paused | - |
| App Download Flow | Email | Sendgrid | First time contact added to Whatsapp Answer but not Download App (Response Received + User Interested) | Instantly and after 5 days | Invite to download the app | Marketing | Leads | Paused | - |
| App Download + Discount | Email | Make, Sendgrid | When user completes register but doesn't download the app | Immediately | App download | Tech/Product | Leads | Active | - |
| Pre-call form (Post WEB_REG) | Email | Make | After user registered on web, if PRECALL not completed | 24h and 48h after web registration | Install app | Tech/Product | Web leads | Active | - |

### Activation Stage

| Touchpoint Name | Channel | Tool/Platform | Condition/Rules | Trigger/Timing | Purpose/Goal | Owner | Audience | Status | Notes |
|----------------|---------|---------------|-----------------|----------------|--------------|-------|----------|--------|-------|
| Waiting First Medical Consultation | Email | Sendgrid | Pipeline Status is Invited to Subscribe, Deal Status is won, Deal Status is Lost | Instantly and after 3 days | Invite user to subscribe | Marketing | Leads | Paused | - |
| Welcome to Balance | Email | Sendgrid | First time contact added to won people (subscribed users) | After 3 hours of subscription | Practical Information | Marketing | New Customers | Paused | - |
| Won People - Cancellation Policy | Email | Sendgrid | First time contact added to won people | 1 day after subscription | Session cancellation policy | Marketing | New Customers | Paused | - |
| Welcome Message | Coach Chat | Backend | When user register on app | Immediately | Welcome message | Tech/Product | App leads | Active | - |
| Welcome message (web) | Coach Chat | Backend | When user installs app | Immediately | Welcome message | Tech/Product | Web leads | Active | - |
| Medical Form Reminder | Push | Backend | User sign up on app and didn't fill out medical form | 2 hours after | Invite user to do medical form | Tech/Product | App leads | Active | - |
| User registered but not complete forms | Coach Chat | Make | Patient registered on app but didn't complete medical form neither booked first call | After 24 hours | Invite to continue with the flow | OPS | App leads | Active | - |
| User registered but not complete forms 2 | WA | Make | Patient registered on app but didn't complete medical form neither booked first call | After 48 hours | Invite to continue with the flow | OPS | Leads | Paused | - |
| Notif for medical form dropped users | Push, WA | Make | Patient did medical form but didn't book a session | After 15 minutes | Invite users to book first GP call | Tech/Product | App leads, web leads | Active | - |
| Unscheduled Leads Call | Phone call | Ringover | Patient completed medical form but didn't book first call | After 2 hours | Schedule first call | OPS | Leads | Active | Let coach know where they came from |
| WEB Session booked (Post Web booking) | WA | Make | After booking first session, for users who don't have the app (with cancel and rescheduling link in WA) | Immediately after booking first session | Give users who don't have access to the app the ability to cancel and reschedule meetings | Tech/Product | Web leads | Active | - |
| Booking confirmation | Email | Calendly | If patient book a session | Immediately | Confirm booking | External | Leads, Subscribed users | Active | - |
| Confirmation VC 9am | Coach Chat, WA | Make | If patient have a booked session | Everyday at 9am | Session confirmation | OPS | Subscribed users, app leads, web leads | Active | Add WA |
| Confirmation VC 2pm | WA | Make | If patient have a booked session | Everyday at 2pm | Session confirmation | OPS | Leads, Subscribed users, web leads | Active | - |
| Confirmation First call VC 7pm | WA | Make | If patient booked a first session | Everyday at 7pm | Session confirmation | OPS | Leads | Active | - |
| First meeting reminders | WA | Make | If patient booked a first session | 4 hours and 30 minutes before VC | Send link to user | OPS | Leads | Active | Cambiar a calendly? |
| Session Cancellation | Email | Calendly | When a VC is cancelled | Immediately | Confirm cancellation | External | Leads, Subscribed users | Active | - |
| Patient meeting cancellation | Coach Chat | Make | If patient cancel a meeting | Immediately | Help patient to reschedule | OPS | Subscribed users, app leads | Active | - |
| No Show or Cancelled First Meetings Call | Phone call | Ringover | If patient cancel or do no show in first call | After 2 hours | Reschedule first call | OPS | Leads | Active | Let coach know where they came from |
| VC send link | Coach Chat | Make | If patient have a booked session | 15 minutes before VC | Send link to user | OPS | Subscribed users, app leads | Active | - |
| First Meeting Connection Reminder Call | Phone call | Ringover | If patient have a first call | After 5 minutes of session time | Connect to first call | OPS | Leads | Active | Let coach know where they came from |
| Not eligible user | Email | Backend | When patient status is changed to "not eligible" | Immediately | Let know the user is not eligible for the program | Tech/Product | Leads | Active | Where is the template? |
| Eligible users with Web | Email, WA | Make | When user is eligible and register from web | Immediately after user is marked as eligible and register from Web | Clear CTA to app + subscribe | Tech/Product | Web leads | Active | - |
| Eligible + instructions | Coach Chat | Backend | When patient is marked as Eligible | Immediately | Send instructions to subscribed | Tech/Product | App leads | Active | - |
| Post web eligibility nudge | Email, Phone call, WA | Make, Ringover | If App not installed (didn't login) / Subscription not active | 24h after user is eligible and register from Web | Install app + subscribe | Tech/Product | Web leads | Active | Phone call part reza need to add to the spreadsheet |
| Long-gap lab followup | Email, Phone call, WA | Make, Ringover | If App not installed (didn't login) / Subscription not active | 7 days after first session was held | Install app + subscribe | Tech/Product | Web leads | Active | Phone call part reza need to add to the spreadsheet |
| Invoice | Email | Stripe | When user pays | Immediately | Share with the user the invoice | External | Subscribed users | Active | - |
| Open Doctor's chat | Professional Chat | Make | If patient subscribe | Immediately | Open chat with the doctor | OPS | New Customers | Active | - |
| OTP | Email | Backend | When user forget the password | Immediately | Access to app | Tech/Product | All | Active | - |
| Invitee reward | Email, Push | Backend | When an invitee user becomes eligible, they receive notification about their discount | - | - | Tech/Product | New Customers | Active | - |

### Retention Stage

| Touchpoint Name | Channel | Tool/Platform | Condition/Rules | Trigger/Timing | Purpose/Goal | Owner | Audience | Status | Notes |
|----------------|---------|---------------|-----------------|----------------|--------------|-------|----------|--------|-------|
| First Prescription Created | Email | Backend | After doctor uploads first prescription | Immediately | Guidance on how to inject medication | Tech/Product | New Customers | Active | Where is the template? |
| Prescription created | Email | Rempe | After doctor creates prescription | Immediately | Send prescription | External | Subscribed users | Active | - |
| Prescription Created 2 | Push | Backend | After doctor uploads prescription | Immediately | User see prescription | Tech/Product | Subscribed users | Active | - |
| Injection Reminder | Push | Backend | If user didn't inject before, 7 days after last injection | Scheduled injection weekday at 10:00 AM | User register the injections | Tech/Product | Subscribed users | Active | - |
| Satiety Form Reminder | Push | Backend | After each injection recorded | 24 hours after | User register the symptoms | Tech/Product | Subscribed users | Active | We need to give it a thought to the logic |
| First injection reminder | Coach Chat | Make | If patient have a prescription and doesn't register it on app | After 4-8-12 days | Invite users to register injection | OPS | New Customers | Active | - |
| Introduction to Nutrition | Coach Chat | Make | When user register first injection | Every 3 hours | Welcome to nutrition process | OPS | Subscribed users | Active | - |
| Form Pre-Consulta Nutrition | Coach Chat | Make | 7 days after the user register first injection | Every 2 hours | Schedule first nutrition meeting | OPS | Subscribed users | Active | - |
| Open Nutritionist chat | Professional Chat | Make | When nutritionist send input form | Immediately | Open chat with the nutritionist | OPS | Subscribed users | Active | - |
| Send diet | Professional Chat | Make | 1 day after the nutritionist accept the diet | Everyday at 8:40am | Send the diet to the user | OPS | Subscribed users | Active | - |
| Send diet (email) | Email | Make | 1 day after the nutritionist accept the diet | Everyday at 8:40am | Send the diet to the user | OPS | Subscribed users | Active | - |
| Send Follow-up | Professional Chat | Make | 10 days after the user received the diet | Everyday at 12pm | Review of diet adherence | OPS | Subscribed users | Active | - |
| Nutrition Follow-up Message | Professional Chat | Make | 1 day after the user submit the follow-up form | Everyday at 2pm | Maintain interactions with the user | OPS | Subscribed users | Active | - |
| Past due | Email | Stripe | When user payment failed | Immediately | Let the user know the pending payment | External | Subscribed users | Active | - |
| NPS | Push | Backend | If patient is subscribed | At day 30, 90, 180 | To gather feedback | Tech/Product | Subscribed users | Active | - |
| Send Form 3 (following months) | Professional Chat | Make | 25 days after the user received the diet | Everyday at 3pm | Schedule the next meeting | OPS | Subscribed users | Active | - |
| Send Form 4 (following months) | Professional Chat | Make | 1 day after the user submit form 3 | Everyday at 3pm | Personalize the new diet for next month | OPS | Subscribed users | Active | - |
| Inactive Patients | WA | Make | If a patient is inactive in app and vc | 26 days after | Keep them on app | OPS | Subscribed users | Active | - |
| Arranging a user interview (NPS survey) | WA | Make | If they fill out NPS survey | Immediately | To arrange a usertest meeting | Tech/Product | Subscribed users | Active | - |
| Card that is about to expire | Email | Stripe | When a user card is about to expire | One month before expiration date | Let the user know the card is about to expire | External | Subscribed users | Active | - |

### Churn Stage

| Touchpoint Name | Channel | Tool/Platform | Condition/Rules | Trigger/Timing | Purpose/Goal | Owner | Audience | Status | Notes |
|----------------|---------|---------------|-----------------|----------------|--------------|-------|----------|--------|-------|
| Referrer reward | Email, Push | Backend | When the status of a referral becomes successful, the referrer receives notification about their reward | Immediately always sent | - | Tech/Product | Existing Customers | Active | - |

## Channel Distribution

- **Email**: Primary channel for formal communications, confirmations, and important information
- **Push Notifications**: Real-time alerts for time-sensitive actions and reminders
- **Coach Chat**: In-app messaging for personalized guidance and support
- **Professional Chat**: Direct communication with medical professionals (doctors, nutritionists)
- **WhatsApp**: Alternative channel for users without app access and urgent communications
- **Phone Call**: Manual intervention for high-priority cases (no-shows, unscheduled leads)

## Tool/Platform Stack

- **Backend**: Core application notification system
- **Make**: Automation platform for complex workflows
- **Sendgrid**: Email delivery platform
- **Stripe**: Payment and billing notifications
- **Calendly**: Appointment scheduling system
- **Ringover**: Phone call system for operations team
- **Rempe**: Prescription management system

## Owner Roles

- **Tech/Product**: Technical implementation and product features
- **OPS**: Operations team managing patient interactions
- **Marketing**: User acquisition and engagement campaigns
- **External**: Third-party systems (Stripe, Calendly, etc.)

## Status Legend

- **Active**: Currently running in production
- **Paused**: Temporarily disabled but may be reactivated
