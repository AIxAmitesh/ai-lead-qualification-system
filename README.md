# AI Lead Qualification & Smart Action System

## Overview

This project demonstrates a simple AI-powered system designed for SaaS platforms like KeaBuilder. It enhances lead handling by automatically analyzing incoming leads, classifying their intent, and suggesting the next best action.

The goal is to simulate how AI can improve funnel efficiency, lead prioritization, and automation within a real-world product.

---

## Problem

Businesses using funnel platforms receive multiple leads but often struggle to:
- Identify high-quality prospects
- Prioritize responses
- Handle spam or low-intent leads efficiently

Manual processing leads to delays and missed opportunities.

---

## Solution

An AI-driven system that:
- Analyzes lead data (name, email, message)
- Classifies:
  - Lead quality (High / Medium / Low)
  - Intent (Buying / Curious / Spam)
  - Urgency
- Suggests the next best action

---

## How It Works

1. User submits lead data (simulated input)
2. AI processes the lead using prompt engineering
3. System returns structured JSON output
4. Automation layer triggers an action based on lead score

---

## AI Design

- Uses LLM for flexible and context-aware classification
- Prompt engineered to enforce structured JSON output
- Designed to simulate real SaaS backend logic

---

## Sample Input

```json
{
  "name": "Rahul",
  "email": "rahul@gmail.com",
  "message": "I want pricing for your premium plan. Please contact me ASAP."
}