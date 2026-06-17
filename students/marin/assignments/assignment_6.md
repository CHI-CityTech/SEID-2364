# Part 1 — System Restatement (From Assignment 5)
Decision Statement
A hiring algorithm determines whether a job applicant is advanced to the interview stage.

Actors
Hiring company

HR staff

Algorithm vendor

Applicants

Regulators / labor agencies

Primary Target
The job applicant being evaluated

Secondary Targets
Applicant’s dependents

Hiring team

Communities affected by employment opportunities

Determinants
Keyword‑matching rules

Model scoring thresholds

Company hiring policies

Legal compliance requirements

Training data patterns

Contributors
Data annotators

Historical hiring managers

Third‑party résumé platforms

Technical infrastructure teams

Key Data Inputs
Résumé text

Education history

Work experience

Skills and certifications

Job description requirements

Metadata (formatting, file type)

# Part 2 — Mediation Pathway Inventory
Below are the major pathways required by the assignment:

Data Pathway

Decision Pathway

Accountability Pathway

Each includes:

SVD syntax

BBS Quad positioning

What moves through the pathway

Physical vs. virtual agency

Information access and conditions

## Pathway 1 — Data Pathway
SVD Syntax
Applicant (Local Physical) → Résumé Portal / Parser (Virtual Vector) → Hiring Algorithm (Remote Virtual)

Source (BBS Quad)
Local Physical — The applicant, submitting data from their own device.

Vector
Virtual mediation through:

Job portal interface

Résumé parser

Data‑formatting subsystem

Destination (BBS Quad)
Remote Virtual — The algorithm’s feature‑extraction and scoring environment.

What Moves Through the Pathway
Applicant data (text, metadata)

Parsed features

Structured representations of skills/experience

Physical Agency
Applicant choosing what to submit

Applicant formatting résumé

Virtual Agency
Parser extracting features

System transforming text into model‑readable vectors

Information Access
Applicant: write‑only

Parser: read/transform

Algorithm: read/compute

HR: no access at this stage

Access Conditions
Platform permissions

File‑format constraints

Vendor parsing rules

## Pathway 2 — Decision Pathway
SVD Syntax
Hiring Algorithm (Remote Virtual) → Scoring Model + Threshold Logic (Virtual Vector) → HR Dashboard (Remote Physical/Virtual Hybrid)

Source (BBS Quad)
Remote Virtual — Algorithmic scoring environment.

Vector
Model weights

Threshold logic

Ranking subsystem

Destination (BBS Quad)
Remote Hybrid — HR dashboard accessed through physical devices.

What Moves Through the Pathway
Applicant score

Recommendation (advance/reject/flag)

Confidence metrics

Physical Agency
HR staff reviewing recommendations

HR staff overriding decisions

Virtual Agency
Model generating scores

Dashboard filtering and sorting candidates

Information Access
HR: read/override

Algorithm: compute‑only

Applicant: no access

Access Conditions
HR role permissions

Company policy

Vendor dashboard settings

## Pathway 3 — Accountability Pathway
SVD Syntax
HR Staff (Local Physical) → Compliance/Policy Systems (Institutional Vector) → Regulators / Legal Bodies (Distant Physical)

Source (BBS Quad)
Local Physical — HR staff responsible for hiring decisions.

Vector
Compliance documentation

Audit logs

Policy review processes

Destination (BBS Quad)
Distant Physical — Regulatory agencies.

What Moves Through the Pathway
Accountability claims

Documentation of decisions

Evidence of compliance

Physical Agency
HR staff preparing reports

Regulators conducting audits

Virtual Agency
Logging systems

Compliance dashboards

Information Access
HR: full access to logs

Regulators: conditional access

Applicants: limited or no access

Access Conditions
Legal requirements

Company policy

Regulatory authority

Part 3 — Relativistic Physical and Virtual Travel Description
Point of Origin (Required by Assignment)
Primary Actor: The Job Applicant

This perspective is chosen because the applicant experiences the consequences of the system most directly and has the least control over internal processes.

Pathway Travel (From Applicant POV)
Data Pathway
Physical → Virtual transition: Applicant uploads résumé from a personal device; data enters the portal.

Virtual travel: Parser extracts features; algorithm receives structured data.

Agency shift: Applicant loses agency once data enters the system; virtual agents take over.

Distance:

Portal = local virtual

Parser = remote virtual

Algorithm = remote virtual

Applicant cannot reach or view internal transformations (unreachable virtual)

Decision Pathway
Virtual → Hybrid transition: Algorithm produces a score; HR views it on a dashboard.

Agency shift: Virtual agency (model) → physical agency (HR).

Distance:

Algorithm = remote virtual

HR = remote physical

Applicant = no access (unreachable)

Accountability Pathway
Physical → Institutional transition: HR prepares compliance materials.

Institutional → Distant transition: Regulators review documentation.

Distance:

HR = remote physical

Regulators = distant physical

Applicant = fully excluded (unreachable)

Part 4 — Pathway Transformation and Friction Analysis
Data Pathway
Transformation: Résumé → parsed features → model vectors

Asymmetry: Applicant cannot see or correct parsing errors

Opacity: Parser logic hidden

Isomorphism Break:

Human résumé reading ≠ algorithmic parsing

Applicant assumes meaning is preserved; algorithm reduces meaning to tokens

Structural symmetry fails because the algorithm cannot interpret nuance or intent

Decision Pathway
Transformation: Feature vectors → score → recommendation

Agency conflict:

Algorithm acts without context

HR may override but often defers to model output

Information asymmetry:

HR sees scores

Applicant sees nothing

Friction:

Thresholds may be rigid

HR may not understand model reasoning

Accountability Pathway
Transformation: Decisions → logs → compliance reports

Authority divergence:

HR is accountable

Algorithm influences outcomes but cannot be held responsible

Ethical distance increases:

Applicant cannot challenge decisions

Regulators only see aggregated documentation



Part 7 — Source Notes
Required Readings
BBS Foundations for Ethical Analysis

Balanced Blended Space (BBS) Website

The Arc of Engineering: A Narrative on How Technologies Move from the Center to Everywhere
