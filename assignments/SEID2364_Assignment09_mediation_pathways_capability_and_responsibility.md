# SEID 2364 – Assignment 9
## Mediation Pathways, Capability, and Responsibility

Instructor: Dr. David B. Smith  
Course: SEID 2364 – Societal and Ethical Impacts of Data Science  
Date Assigned: Week 9  
Due: Week 10

---

## Purpose

In prior assignments, you:

- identified harm (Assignment 3)
- evaluated harm using ethical frameworks (Assignment 4)
- described systems structurally (Assignment 5)
- traced mediation pathways across physical and virtual space (Assignment 6)
- evaluated systems under regulation (Assignment 7)
- analyzed bias across deployments (Assignment 8)

This assignment shifts the focus again.

> Not just *where bias or harm exists*, but *how harm emerges through mediation pathways under real conditions of system capability*.

A critical question emerges: **Is the harm truly unintended, or is it foreseeable but not prevented?**

Drawing from strategic analysis (Sun Tzu, Clausewitz), we treat ethics not as intention, but as **capability under constraint**.

A system is therefore evaluated by:

- what it **can do**
- under **actual conditions of access, visibility, and control**
- whether harmful capabilities were **known but not constrained**
- whether responsibility was **distributed to avoid accountability**

---

## EDOCA: Dimensions of Mediation Assessment

> In BBS terms, a mediation pathway can be understood as **S → V → D**, where the **Vector (V)** is the **transition** that transforms a source state into a destination state.
>
> The goal of analysis is to evaluate the **efficacy of V**: its ability to **maintain the intended signal from S to D** under real conditions.

This assignment introduces **EDOCA** as a formal diagnostic framework for evaluating mediation transitions.

EDOCA is ordered intentionally to reflect how mediation is analyzed:

- **Effort** — what resources are applied
- **Distortion** — what happens to the signal as a result
- **Observability** — who can see the result
- **Control** — who can act on the result
- **Authority** — who can permit or constrain action

This ordering reflects a causal chain: resources produce transformations, transformations produce distortion, distortion produces outcomes that are variably visible, actionable, and governable.

At each critical transition, you must evaluate:

- **Effort / Energy** — the cost required to produce or sustain the transition (time, computation, human labor, infrastructure, attention)
- **Distortion (Fidelity)**
- How effectively does this transition (V) preserve the intended signal from S to D? — how much the signal changes during the transition (noise, ambiguity, translation loss, compression, abstraction, representation mismatch)
- **Observability** — who can see or understand what is happening, and to what degree
- **Control** — who can initiate, modify, redirect, or influence the transition
- **Authority** — who can assign, enable, restrict, or halt capability

> EDOCA is applied at **specific transitions (Vectors, V)**, not to the system as a whole.
>
> Each transition (V) is evaluated based on how well it preserves or transforms the signal from **Source (S)** to **Destination (D)**.

Effort and distortion are deeply related but not identical. In some cases, increased effort (validation, redundancy, higher computation, human review) may reduce distortion and improve fidelity. In other cases, additional transformations or processing may preserve or amplify distortion. You should therefore ask not only how much effort is present, but whether that effort improves or degrades the quality of the mediated signal.

---

## Assignment Overview

You will analyze a real-world AI-related incident by reconstructing the **mediation pathways that produced a harmful outcome**.

Your task is to:

- describe the event clearly (no analysis)
- identify all major **agents** involved
- reconstruct **multiple mediation pathways**
- identify **critical transitions**
- apply **EDOCA at those transitions**
- evaluate **capability vs intent**
- analyze how **responsibility is distributed across the system**

---

## Part 0 – Repository Preparation and Incident Selection

Create a new file in your repository:

`assignment-09/pathways.md`

All work for this assignment must appear in this file.

### Incident Selection

Before beginning, select a real-world incident that involves multiple agents, traceable mediation pathways, and sufficient documentation.

For guidance on what makes a suitable incident and where to find current examples, see:

[Incident Selection Guide](../resources/09-SEID2364_Assignment09_incident_selection_guide.md)

This guide provides:
- Criteria for evaluating potential incidents
- Domain examples (AI hiring, content moderation, healthcare, autonomous systems, data/privacy)
- Where to find current, well-documented incidents
- What NOT to select
- How to vet your choice

You are responsible for finding your own incident. The guide is a resource, not a prescribed list.

---

## Part 1 — Narrative Description (Descriptive Only)

Provide a narrative answering:

> What happened, to whom, by whom, and what was harmed?

Requirements:

- 1–2 paragraphs
- descriptive only (no analysis)

Do NOT include:

- explanations
- causes
- ethical evaluation

---

## Part 2 — Originating Agents

Identify the primary agents involved.

Include (where applicable):

- End user / operator  
- AI system (LLM / agent)  
- AI developer / manufacturer  
- Platform / infrastructure (APIs, cloud systems)  
- Intermediate tools or environments  

Each agent may initiate **distinct mediation pathways**.

---

## Part 3 — Mediation Pathways (Multi-Agent)

Construct mediation pathways organized by **originating agent**.

Requirements:

- At least **2 agents** must be analyzed
- Each agent must have **at least one pathway** (max 2–3 per agent)
- Each pathway must include **minimum 3 stages**
- Focus on **critical pathways only**

Format:

```
Agent → Stage 1 → Stage 2 → Stage 3 → Outcome
```

For each stage, identify:

- Space type: Personal / Local / Remote / Unreachable
- Transition type (where relevant):
  - physical ↔ virtual
  - symbolic ↔ computational
  - local ↔ remote

---

## Part 4 — EDOCA Assessment of Critical Transitions

> Each selected transition corresponds to a **Vector (V)** in an S → V → D structure. Your task is to evaluate how effectively that transition maintains or transforms the signal between states.

Select at least **two transitions** across your pathways.

For each:

### 1. Identify the Transition (Vector V)
- What state change occurs (S → D)?
- What transformation (V) produces that change?
- Between which spaces or representations does this occur?

### 2. Apply EDOCA

**Effort / Energy**  
- What resources are required?  
- Who provides them?

**Observability**  
- Who can observe this transition?  
- What is hidden, partial, delayed, or opaque?

**Control**  
- Who initiates or modifies the transition?  
- Who is read-only?

**Authority**  
- Who can enable, restrict, or halt this transition?  
- Is authority aligned with control?

**Distortion / Fidelity**  
- How does the signal change during this transition?  
- What forms of distortion are introduced, reduced, preserved, or amplified?  
- Does the transition improve fidelity, degrade fidelity, or leave the signal mostly unchanged?

### 3. Synthesis

> How does this EDOCA configuration contribute to potential harm?

---

## Part 5 — Signal and State Integrity

Because distortion is now included directly in EDOCA, this section should focus on the consequences of distortion and on the difference between signal failure and state failure.

For selected transitions, identify:

- **Signal degradation / distortion** — already described through the Distortion / Fidelity dimension of EDOCA
- **State divergence** — where the internal system model does not match the actual system state
  - example: the system believes an action succeeded when it did not

Distinguish between:

- **Symbolic failure** — errors introduced during representation, translation, or interpretation
- **State failure** — errors introduced when system state becomes inconsistent with reality
- **Bias** — patterned distortion that systematically affects certain people, groups, outputs, or decisions

Additionally, indicate:

> Where does distortion first appear, and where is it amplified across subsequent transitions?

> At what point does distortion become error, bias, or harm?

---

## Part 6 — Capability vs Intent and Unintended Consequences

This section asks you to distinguish between what was **intended** and what was **foreseeable but not prevented**.

### Step 1: Identify Stated Intent
- What was the system designed and marketed to do?
- What did the developers, operators, or institution claim was its purpose?
- What outcomes were publicly promised or expected?

### Step 2: Identify Actual Capability
- What could the system actually do under real conditions?
- What were the known limitations, failure modes, or edge cases?
- What risks were identified but not addressed (in documentation, internal reviews, or research)?

### Step 3: Analyze the Consequence

Answer this question rigorously:

> Is the harm that occurred truly **unintended**, or is it more accurately **foreseeable but not prevented**?

Distinguish between:

- **Genuinely unintended**: The consequence emerged through causal chains no one could reasonably predict (novel interaction, unprecedented context, unforeseen adoption)
  - *Example*: A medication's unexpected side effect in a rare genetic subgroup not tested in trials

- **Foreseeable but not prevented**: The risk was known, documented, or predictable from available information, but no mechanism prevented it
  - *Example*: Facial recognition known to fail on darker skin tones (documented in academic literature) deployed without mitigation, leading to wrongful arrest

- **Designed with plausible deniability**: The system was built in ways that predictably produce harm, but the design distributes responsibility so that no single actor appears responsible
  - *Example*: Algorithm that amplifies divisive content, flagged in internal reviews, but kept because it increases engagement; when polarization emerges, blamed on "unintended user behavior"

Your analysis should use EDOCA findings: where was capability known? Where was control held? Where did authority fail to constrain known risks?

---

**Note on incident scope:** This assignment analyzes incidents where harmful capabilities emerged through system mediation, even if not intentionally designed. If the primary harm comes from deliberate deception, fraud, or intentional misuse by malicious actors, that belongs to a different analytical framework. You should select incidents where system structure and mediation pathways are the primary focus—not cases where the core problem is bad faith or criminal intent.

---

## Part 7 — Responsibility Distribution

Using your pathways:

- Where does responsibility appear to reside?
- Where does it become distributed or unclear?

Focus on mismatches between:

- Authority
- Control
- Capability

---

## Part 8 — Reflection

Respond briefly:

> How did reconstructing mediation pathways change your understanding of how harm is produced in complex systems?

---

## Example (Outline Only)

### Originating Agent — Developer

Developer → Prompt (Local symbolic) → AI Agent (Remote computational) → API (Remote infrastructure) → System State Change

### Originating Agent — AI System

Internal State → Plan Generation → Execution Commands → System State

### Originating Agent — Infrastructure

API Design → Permission Scope → Execution → Data Outcome

---

## Deliverables

Submit to GitHub:

```
/students/yourname/assignment-09/pathways.md
```

---

## Evaluation Criteria

- Pathway clarity and structure  
- Correct identification of agents  
- EDOCA application precision  
- Signal/state distinction accuracy  
- Capability vs intent reasoning  
- Responsibility analysis depth  
- Clarity and organization  

---

## TL;DR

- Describe what happened (no analysis)
- Identify agents
- Build mediation pathways
- Select critical transitions
- Apply EDOCA
- Analyze signal vs state
- Evaluate capability vs intent
- Identify responsibility
- Commit and push

---

## Reminder

> Systems are not evaluated by what they are designed to do, but by what they are capable of doing under real conditions.

