# Part 1 — System Structure (Descriptive Layer)
Decision Statement
A hiring algorithm determines whether a job applicant is advanced to the interview stage.

This represents one instance of a broader system that repeatedly produces hiring‑screening decisions across many applicants.

System Components
## 1. Actors
Entities that participate in or influence the system:

Hiring Company — commissions, configures, and deploys the algorithm.

HR Staff — review algorithm outputs, set criteria, and sometimes override decisions.

Algorithm Vendor — designs the model, provides updates, and defines technical constraints.

Applicants — provide data that the system evaluates.

Regulators / Labor Agencies — influence compliance requirements.

These actors collectively shape how decisions are produced, even if they do not all directly make decisions.

## 2. Targets
Who the decision acts upon:

Primary Target: The job applicant whose résumé is being evaluated.

Secondary Targets:

Applicant’s dependents (economic impact)

Hiring team (workload, team composition)

Communities affected by employment opportunities

Targets experience the consequences of the decision even if they do not participate in making it.

## 3. Determinants
Rules, criteria, and constraints that shape outcomes:

Keyword‑matching rules (e.g., required skills)

Model scoring thresholds

Company hiring policies

Legal compliance requirements

Training data patterns

These determinants define the boundaries within which the algorithm operates and strongly influence which applicants advance.

## 4. Contributors
Entities that influence outcomes without being the final decision authority:

Data annotators who labeled training data

Previous hiring managers whose historical decisions shaped the dataset

Third‑party résumé platforms that format applicant data

Technical infrastructure teams who maintain system performance

Contributors shape the system’s behavior indirectly through data, design, or operational constraints.

## 5. Information / Data Inputs
Information Inputs
Applicant résumé text

Education history

Work experience

Skills and certifications

Metadata (résumé formatting, file type)

Job description and required qualifications

Source
Applicants (self‑submitted data)

Company HR systems

External job platforms

Vendor‑provided datasets

Information Authority
HR department (validates required skills)

Algorithm vendor (defines model features)

Legal/compliance teams (define permissible data)

Trust Basis
Institutional legitimacy (company HR policies)

Historical performance of the model

Legal requirements for documentation

Assumptions that applicant‑provided data is truthful

Contrasting Example (Same System, Different Outcome)
Example:  
A candidate with a non‑traditional résumé format (e.g., creative layout) is rejected because the parser fails to extract key skills.

Contrast:  
Another candidate with identical skills but a conventional résumé layout is advanced because the parser successfully identifies keywords.

This demonstrates how different inputs and conditions within the same system produce different outcomes.

# Part 2 — Interpretive Layer (Ethical Overlay)
This section identifies how authority, ownership, responsibility, agency, and harm are distributed across the system.
(Not an ethical evaluation — only structural interpretation.)

Authority (Decision Authority)
The algorithm appears to make the decision, but

HR staff and company leadership hold formal authority by setting thresholds and approving system use.

Ownership
The company owns applicant data and the decision process.

The vendor owns the model architecture and training pipeline.

Responsibility
The company is accountable for hiring outcomes.

HR is responsible for oversight.

Vendors share responsibility for model behavior but often lack direct accountability.

Agency
The algorithm has operational agency (it performs actions).

HR staff have human agency (they can override or adjust).

Applicants have limited agency (they can only submit materials).

Harm Distribution
Applicants may experience exclusion, misclassification, or lost opportunities.

HR may face increased workload if the system produces errors.

Communities may experience downstream economic effects.

Authority, responsibility, and harm are not aligned — a central feature of distributed sociotechnical systems.

# Part 3 — System Flow (Pre‑Framework)
Information Flow Description
Applicant submits résumé through a job portal.

Data is parsed by the résumé‑processing subsystem, transforming text into structured features.

Algorithm evaluates features using model weights, historical patterns, and scoring rules.

Score is compared to thresholds set by HR or company policy.

Upstream decision point: HR defines required skills and threshold levels.

System outputs a decision (advance / reject / flag for review).

Downstream decision point: HR may override or confirm the algorithm’s recommendation.

Outcome is recorded in the applicant tracking system, influencing future training data and system behavior.

This flow shows how information originates, transforms, and contributes to distributed decision‑making across technical and human components.
