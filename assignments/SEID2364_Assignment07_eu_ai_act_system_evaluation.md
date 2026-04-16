# Assignment: EU AI Act System Evaluation

**Course:** SEID 2364  
**Instructor:** Dr. David B. Smith  
**Date Assigned:** [Insert Date]  
**Due Date:** [Insert Date]  

---

## Framing

This assignment marks a shift from selecting and applying ethical frameworks toward operating within a fixed regulatory structure. In prior work, you evaluated systems using multiple frameworks of your choosing. Here, that flexibility is intentionally removed. You will instead evaluate your system using the EU AI Act, a formal regulatory instrument that defines categories, constraints, and obligations.

The goal is not only to classify your system, but to understand how regulation constrains interpretation, exposes ambiguity, and forces concrete decisions under incomplete information.

This assignment also continues the use of **mediation pathways (BBS)** from previous work. You should use your prior analysis to inform how your system produces, transmits, and exposes risk.

---

## Assignment Overview

You will evaluate **your own system** (developed in prior assignments) using the EU AI Act.

This assignment treats classification as **context-dependent** rather than intrinsic. You are not labeling your system in isolation; you are evaluating how it would be interpreted under specific conditions of use defined by the regulation.

Your work must:
- Classify your system within the EU AI Act risk categories
- Justify that classification using the Act
- Analyze how risk is produced, distributed, or mitigated
- Support your analysis with external research
- Document sources in Zotero

---

## Required Reading Strategy

The four reading steps below are designed to be read in sequence and used together. They move from ethical foundations, to regulatory structure, to legal text, to critical policy analysis. Each layer informs the next. Your classification and analysis should reflect all four.

### Step 1 — Ethical Foundations (Required)

Read both of the following:

- [Ethics Guidelines for Trustworthy AI](https://digital-strategy.ec.europa.eu/en/library/ethics-guidelines-trustworthy-ai) — European Commission High-Level Expert Group on AI
- [EU AI Act: High-Level Summary](https://artificialintelligenceact.eu/high-level-summary/) — artificialintelligenceact.eu

**How they work together:**
The Ethics Guidelines for Trustworthy AI (2019) established the philosophical and governance foundations that informed the EU AI Act's design. Principles including human agency, transparency, accountability, and robustness appear in the guidelines as ethical recommendations and then reappear in the Act as regulatory obligations. Reading both together lets you trace that movement from principle to law.

As you read, note explicitly where a Trustworthy AI recommendation became a regulatory requirement in the Act, and where it did not.

---

### Step 2 — Legal Text (Required)

Use the EU AI Act directly to support your classification.

Focus on:

- [Article 5 — Prohibited AI Practices](https://artificialintelligenceact.eu/article/5/)
- [Article 6 — Classification Rules for High-Risk AI Systems](https://artificialintelligenceact.eu/article/6/) + [Annex III — High-Risk AI Systems](https://artificialintelligenceact.eu/annex/3/)
- [Article 50 — Transparency Obligations for Certain AI Systems](https://artificialintelligenceact.eu/article/50/)
- (Skim [Articles 8–15](https://artificialintelligenceact.eu/section/3-2/) for high-risk system requirements)

Use these links for direct legal navigation. Add all legal sources you reference to Zotero.

**How this connects to Step 1:**
This is where the ethical principles from Step 1 become binding legal language. As you read the Act, consider which Trustworthy AI principles made it into the legal text and which were weakened, narrowed, or omitted entirely.

---

### Step 3 — Critical Policy Analysis (Required)

Read the following legal rights-based critique of the Act:

- [Packed with Loopholes: Why the AI Act Fails to Protect Civic Space and Rule of Law](https://ecnl.org/news/packed-loopholes-why-ai-act-fails-protect-civic-space-and-rule-law) — European Center for Not-for-Profit Law (ECNL)

**How this connects to Steps 1 and 2:**
This piece evaluates the gap between the Act's stated ethical ambitions (as established in the Trustworthy AI guidelines) and its actual legal provisions. It argues that significant exemptions and enforcement gaps undermine the protections the Act was designed to provide, particularly for civil society and democratic governance.

Reading this after Steps 1 and 2 allows you to assess whether the movement from ethical recommendation to regulatory obligation is complete, partial, or contradicted. Consider:
- Where does the critique identify structural weaknesses in the Act's design?
- Do those weaknesses affect the classification or compliance analysis you are conducting for your own system?
- Does your system sit in a space where the gaps identified by ECNL might apply?

You are not required to agree with the critique, but you must engage with it analytically in your work.

---

### Step 4 — Research (Required)

Identify **2–3 credible sources** that specifically address your system type — or a closely comparable system — **in relation to the EU AI Act or AI regulation more broadly**.

You are not looking for separate sources about your system on one hand and about the Act on the other. You are looking for sources that put them together: scholarly articles, policy analyses, legal commentary, or case studies that examine how systems like yours are categorised, scrutinised, or governed under AI regulation.

Good sources for this assignment might:
- Analyse how a specific AI application domain (e.g. hiring, healthcare, content moderation) maps onto EU AI Act risk categories
- Examine how a real system similar to yours has been evaluated or challenged under the Act or comparable regulation
- Discuss regulatory gaps or classification ambiguities for systems with the characteristics yours has

**How this connects to the previous steps:**
Steps 1–3 gave you the ethical foundations, the legal structure, and a critique of where the Act falls short. Step 4 grounds all of that in existing scholarship about systems like yours. Use your sources to test, support, or challenge the analysis you are building — not to replace it.

Add all sources — including the ECNL source from Step 3 — to the shared Zotero library.

---

## Important Instruction

The high-level summary from artificialintelligenceact.eu helps you understand the structure, but your classification must ultimately be justified using the EU AI Act legal text.

---

## Tasks

The following steps should be completed as a structured document in your GitHub repository. Think of this not as a short response, but as a **technical analysis artifact** that could be read by another researcher, designer, or regulator. Each section should be written in clear prose (not bullet-only), with diagrams or structured elements included where appropriate.

You are encouraged to revise and reuse prior work, but this submission should represent a **refined and integrated version** of your system analysis.

No strict word limit is imposed. Prioritize structural completeness, clarity, and precision over length.

---

### 1. System Description (Concise)

Briefly restate your system:
- What it does
- Who interacts with it
- What decision or action it performs

Keep this focused and technical.

---

### 2. Mediation Pathway (From Previous Assignment)

Use your prior BBS work to describe how your system operates as a mediated process.

Rather than simply restating your previous diagram, revise it with the following in mind:
- Does the pathway reveal where decisions are actually being made?
- Are there points where visibility is limited or obscured?
- Where might regulation “intervene” in this pathway?

Include:
- Source(s)
- Vector(s)
- Destination(s)

Indicate:
- Where transformation occurs
- Where visibility is gained or lost

You may include a diagram, but it must be accompanied by a short explanatory paragraph.

---

### 3. EU AI Act Classification

Using the EU AI Act, determine how your system would be classified.

This is a **constrained classification problem**. Categories are defined externally by regulation, not by your interpretation.

**Important:** You are not classifying your system in isolation. You are classifying how your system behaves under **specific use conditions**.

Proceed as follows:

1. **Define Core Function**  
   Briefly state what your system is designed to do.

2. **Identify 1–3 Concrete Use Cases**  
   Describe realistic scenarios of deployment (who uses it, where, for what purpose).

3. **Classify Each Use Case**  
   For each scenario, assign a category:
   - Prohibited Risk  
   - High Risk  
   - Limited Risk  
   - Minimal / No Risk  

Your system may span multiple categories depending on context, domain, or implementation. If so, you must explicitly describe those conditions.

Where relevant, consider **risk escalation pathways**:
- How a system that begins as minimal or limited risk could become high risk through scaling, integration, or repurposing

**Constraint:** Do not force multiple categories. Only identify multiple classifications when clearly supported by distinct use cases.

---

### 4. Justification Using the Act

This is the core analytical section of the assignment.

You must support each classification (per use case) by referencing the EU AI Act directly. This includes:
- Specific articles (e.g., Article 5, Article 6)
- Definitions
- Annex III (if applicable)

Your writing should demonstrate:
- How each use case aligns with (or challenges) the definitions in the Act
- Where interpretation is required
- Where ambiguity exists

At least one explicit reference to the Act is required for each classification.

Use a consistent citation format in this section. For each claim, cite the Act in-line using this pattern:

- Article citation: `Art. X` or `Art. X(Y)`
- Annex citation: `Annex III, Y`

For each use case, include at least:

- one direct legal reference (article and/or annex), and
- one brief explanatory sentence connecting that legal text to the specific use condition.

Avoid vague justification. Your goal is to show how the regulation constrains your interpretation under specific conditions of use.

---

### 5. Risk Analysis

Building on your mediation pathway, analyze how risk emerges within your system.

This section should move beyond general statements and instead identify:
- Where risk is introduced in the system
- How it propagates through the mediation pathway
- Who is exposed to that risk and in what way

Consider:
- Types of harm (economic, social, reputational, physical)
- Direct vs indirect effects
- Whether the system amplifies or reduces existing inequalities

Your analysis should connect clearly back to both your system design and the EU classification.

---

### 6. Regulatory Implications

Based on your classification, determine what the EU AI Act would require of your system.

This section should **build directly on your classification and justification** (do not repeat them). Instead, focus on consequences.

Identify:
- What obligations apply under the Act
- What changes would be required for compliance

This may include:
- Transparency requirements
- Documentation and record-keeping
- Human oversight mechanisms
- Risk management procedures

Be specific and practical. Describe what compliance would look like in implementation, not in abstract terms.

---

### 7. Research Integration

Incorporate your external sources:
- Compare your system to existing examples
- Identify whether similar systems have been discussed in relation to regulation
- Identify which philosophical or ethical frameworks appear to have informed the development of the EU AI Act (for example, rights-based, deontological, consequentialist, virtue-oriented, or justice-oriented reasoning)
- Briefly explain how those frameworks are reflected in specific parts of the Act or related policy framing documents

**Process Requirement:**
Complete your initial classification and justification before consulting external sources. Use research to challenge, refine, or support your conclusions—not to replace them.

Your research should function as a **pressure test** of your analysis, not a substitute for it.

All sources must be:
- Added to Zotero
- Properly cited

---

## Deliverables

Students should submit this assignment by uploading their work to their GitHub site/repository.

You may submit in either format:

- Markdown (.md)
- PDF (.pdf)

Both formats are accepted for this assignment.

Recommended filename:

- `07-eu-ai-act-system-evaluation.md` (or `.pdf` if submitting as PDF)

If submitting in Markdown:

- Use clear section headings that match the tasks above
- Ensure diagrams/images are properly linked and render in the repository

If submitting in PDF:

- Include all required sections in one well-structured document
- Integrate diagrams/images directly into the PDF (not as separate unreferenced files)

Your GitHub submission should include:

- The final assignment file (.md or .pdf)
- Any supporting assets (images, diagrams, drafts if applicable)
- Completed Zotero entries for all referenced sources

Your README should briefly describe:

- What the system is
- What this submission contains

---

## Assessment Criteria

Your work will be evaluated based on:

- Accuracy of EU AI Act classification
   - Excellent: classification is context-specific and legally defensible across stated use cases
   - Competent: classification is mostly accurate but misses edge conditions or nuance
   - Needs Revision: categories are misapplied, unsupported, or overly generalized
- Strength of justification using the Act
   - Excellent: clear, explicit article/annex references with strong claim-to-text alignment
   - Competent: references are present but unevenly connected to claims
   - Needs Revision: references are vague, missing, or not tied to analysis
- Integration of mediation pathway analysis
   - Excellent: pathway analysis clearly explains where risk and visibility shift
   - Competent: pathway is included but only partially connected to classification
   - Needs Revision: pathway is superficial, disconnected, or missing key transitions
- Depth of risk analysis
   - Excellent: identifies introduction, propagation, exposure, and distribution of harms with specificity
   - Competent: identifies risks but with limited propagation or stakeholder detail
   - Needs Revision: risk discussion remains generic or unstructured
- Quality and relevance of research sources
   - Excellent: sources are credible, directly relevant, and used to pressure-test conclusions
   - Competent: sources are credible but weakly integrated into argumentation
   - Needs Revision: sources are sparse, low quality, or used as substitutes for analysis
- Clarity and organization of writing
   - Excellent: structured, readable, and analytically coherent across sections
   - Competent: generally clear with minor structural or clarity issues
   - Needs Revision: difficult to follow, incomplete, or poorly structured

---

## Notes

- You are not expected to fully master the legal text. You are expected to engage with it meaningfully.
- Ambiguity is expected. Your task is to reason through it, not eliminate it.
- This assignment is preparatory for more formal system evaluation and design work.

---

## Reflection (Journal Entry)

Do not include reflection in this submission. Instead, record your reflection in your course journal as your next journal entry.

Address the following:

- How did working within a regulation differ from using a framework?
- Where did the Act clarify your thinking?
- Where did it constrain or complicate it?
- How did the critical policy analysis (Step 3) affect your reading of the Act?

---

End of Assignment

