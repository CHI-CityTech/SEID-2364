# 1. System Description (Concise)
The automated hiring algorithm evaluates job applicants by parsing résumés, extracting features, and generating a score or recommendation (advance / reject / flag). HR staff interact with the system through a dashboard, while applicants interact only through résumé submission. The system performs a classification and ranking action that influences access to employment opportunities.

# 2. Mediation Pathway (Revised from Assignment 6)
Source → Vector → Destination (SVD)
Applicant (Local Physical) → Résumé Portal + Parser (Virtual Vector) → Hiring Algorithm (Remote Virtual) → HR Dashboard (Remote Hybrid) → HR Decision (Remote Physical)

Where Decisions Occur
Parser: transforms applicant data into structured features

Algorithm: generates scores and recommendations

HR: final decision authority, with ability to override

Visibility
Applicant: no visibility into parsing or scoring

HR: partial visibility (scores, rankings) but not model logic

Regulators: conditional visibility through compliance documentation

Regulatory Intervention Points
Data collection and permissible features

Transparency obligations

Human oversight requirements

Documentation and logging

Risk‑management procedures

Short Explanation
The system is a multi‑stage mediated process where applicant data travels through virtual transformations before reaching human decision‑makers. Visibility decreases sharply once data enters the parser and algorithm, creating opacity that regulation may need to address. Risk emerges at each transformation point, especially where automated scoring influences downstream human decisions.

# 3. EU AI Act Classification
Core Function
The system evaluates job applicants and influences hiring decisions by generating automated recommendations.

## Use Case 1 — Standard Corporate Hiring
Context: A private company uses the algorithm to screen applicants for non‑regulated jobs.
Classification: High‑Risk AI System

Why
Annex III(4)(a) lists “AI systems intended to be used for recruitment or selection of natural persons” as high‑risk.

Art. 6(2) states that systems listed in Annex III are automatically high‑risk.

## Use Case 2 — Hiring for Safety‑Critical Roles (e.g., aviation technician)
Context: The algorithm screens candidates for roles where errors could cause physical harm.
Classification: High‑Risk, with elevated risk implications

Why
Annex III(3) covers systems determining access to education and vocational training, which may apply if the hiring process gates access to regulated training pipelines.

Annex III(1) covers systems related to safety components of regulated products; while hiring is not itself a safety component, misclassification may indirectly affect safety‑critical operations.

## Use Case 3 — Informal Pre‑Screening Tool (Non‑Decisive)
Context: A company uses the algorithm only to sort résumés for HR review, with no automated rejection.
Classification: Limited‑Risk

Why
Art. 50 requires transparency for systems interacting with humans or generating content, but does not classify them as high‑risk.

If the system does not make or meaningfully influence decisions, it may fall outside Annex III.

# 4. Justification Using the EU AI Act
Use Case 1 — High‑Risk Classification
Legal Basis: Annex III(4)(a) — “AI systems intended to be used for recruitment or selection of natural persons.”

Interpretation: The system directly determines which applicants advance, fitting the definition precisely.

Ambiguity: None; this is one of the clearest categories in the Act.

Use Case 2 — High‑Risk (Safety‑Relevant Context)
Legal Basis:

Annex III(4)(a) — recruitment

Art. 6(1) — systems that are safety components of regulated products

Interpretation: While the hiring algorithm is not itself a safety component, its outputs influence access to safety‑critical roles.

Ambiguity: The Act does not clearly define whether upstream hiring tools count as “safety‑related,” requiring interpretive judgment.

Use Case 3 — Limited‑Risk Classification
Legal Basis: Art. 50 — transparency obligations for certain AI systems

Interpretation: If the system does not reject applicants or meaningfully influence decisions, it may not meet Annex III criteria.

Ambiguity: The phrase “meaningfully influence” is not defined, creating uncertainty about borderline cases.

# 5. Risk Analysis
Where Risk Is Introduced
Parsing stage: mis‑extraction of skills

Model stage: biased scoring due to historical data

Threshold stage: rigid cutoffs excluding qualified applicants

HR stage: over‑reliance on algorithmic recommendations

How Risk Propagates
A parsing error → incorrect features → low score → rejection

Biased training data → systemic exclusion of certain groups

HR trust in algorithm → reduced human oversight

Who Is Exposed
Applicants: economic, reputational, and opportunity harms

HR: compliance risk

Company: legal and reputational risk

Communities: long‑term inequality effects

Types of Harm
Economic: lost employment

Social: reinforcement of bias

Reputational: unfair labeling of applicants

Structural: reduced workforce diversity

# 6. Regulatory Implications
If Classified as High‑Risk
The system must comply with:

Art. 9: Risk‑management system

Art. 10: High‑quality training data

Art. 11: Technical documentation

Art. 12: Logging and traceability

Art. 13: Transparency to users (HR)

Art. 14: Human oversight

Art. 15: Accuracy, robustness, and cybersecurity

Practical Implementation
Maintain detailed logs of all decisions

Provide HR with clear explanations of scoring logic

Conduct bias audits and data‑quality assessments

Implement override mechanisms and human‑in‑the‑loop review

Document all model updates and training procedures

If Classified as Limited‑Risk
Must meet transparency obligations under Art. 50

Must inform users (HR) that they are interacting with an AI system

No high‑risk obligations apply

# 7. Research Integration
Findings from External Sources

Research on AI hiring systems and EU regulation shows:

Many hiring algorithms are expected to fall under Annex III(4) due to their direct impact on employment access.

Scholars highlight ambiguity around “meaningful influence,” which affects borderline cases.

Policy analyses note that the Act reflects rights‑based and deontological principles, especially in its emphasis on human oversight, transparency, and fairness.

Critical commentary (e.g., ECNL) argues that exemptions and enforcement gaps may weaken protections for applicants.

How Research Affects This Analysis
Supports the high‑risk classification for core hiring use cases

Highlights regulatory uncertainty for pre‑screening tools

Reinforces the need for strong documentation and oversight

Shows that the Act’s ethical foundations (Trustworthy AI) are only partially realized in binding law
