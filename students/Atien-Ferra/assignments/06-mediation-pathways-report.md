# Assignment 6 - Mediation Pathways Report

Part 1 - System Restatement

## Decision statement
An employer advances or rejects a job applicant through an AI-assisted hiring system.

## Actor set
The main actors are the applicant, the employer, recruiters or hiring managers, the software vendor, and the technical system itself. The technical system includes the job portal, applicant tracking system, resume parser, assessment platform, scoring model, recruiter dashboard, and audit logs.

## Primary and secondary targets
The primary target is the applicant whose application is scored, ranked, advanced, delayed, or rejected. Secondary targets include other applicants competing for the same role, employer teams affected by the hiring outcome, and people connected to the applicant such as dependents.

## Determinants and contributors
Key determinants are job requirements, employer screening criteria, model design, training data, assessment thresholds, accommodation rules, and employer policy. Key contributors are HR staff, recruiters, hiring managers, vendor engineers, compliance staff, and any data sources used to build or tune the system.

## Key data and information inputs
The system uses resumes, application forms, answers to screening questions, assessment results, interview responses, job descriptions, historical hiring data, and employer-set scoring rules. Some systems also use chat screening, asynchronous video interviews, and internal audit logs.

# Part 2 - Mediation Pathway Inventory

## Pathway 1 - Applicant data submission pathway
SVD: Applicant application materials -> job portal upload, parsing, and storage -> ATS and vendor processing systems

- Source node on the BBS Quad: local physical and local virtual boundary
- Vector: the applicant types, uploads, clicks submit, and the platform encodes that material into platform-readable data
- Destination node on the BBS Quad: remote virtual
- What moves: resume text, form entries, assessment responses, timestamps, metadata, and uploaded files
- Physical agency: the applicant chooses what to submit, uses a device, may use assistive technology, and may decide whether to disclose a disability or request an accommodation
- Virtual agency: the portal validates fields, accepts or rejects file types, timestamps the submission, and routes the data to storage and parsing tools

## Pathway 2 - Data transformation and scoring pathway
SVD: ATS applicant record -> parsing, feature extraction, model scoring, and ranking -> recruiter dashboard and candidate shortlist

- Source node on the BBS Quad: remote virtual
- Vector: resume parsing, assessment scoring, feature generation, ranking logic, filtering rules, and confidence or threshold checks
- Destination node on the BBS Quad: remote virtual
- What moves: structured candidate features, scores, rankings, flags, and recommendation labels
- Physical agency: HR staff or recruiters may configure thresholds, select required fields, or decide which outputs matter most
- Virtual agency: the parser extracts categories, the model scores the candidate, and the dashboard reorders applicants into a usable hiring queue

## Pathway 3 - Hiring decision pathway
SVD: Ranked applicant output -> recruiter or hiring-manager review and approval -> applicant status change

- Source node on the BBS Quad: remote virtual
- Vector: dashboard review, recruiter judgment, hiring-manager approval, and status update inside the employer system
- Destination node on the BBS Quad: remote physical and then local virtual for the applicant
- What moves: authority signal, decision recommendation, approval, rejection, interview invitation, or request for more information
- Physical agency: recruiters and hiring managers act in embodied institutional roles. They can advance, reject, pause, override, or escalate a case
- Virtual agency: the dashboard sorts candidates, presents summaries, sends notifications, and locks or unlocks next-step actions

## Pathway 4 - Accountability and contestation pathway
SVD: Applicant challenge, accommodation request, or complaint -> employer review, compliance review, and vendor inquiry -> revised decision, explanation, or closure

- Source node on the BBS Quad: local physical and local virtual
- Vector: email, portal message, accommodation form, HR case handling, legal review, and audit-log retrieval
- Destination node on the BBS Quad: remote physical and remote virtual, then back to local virtual
- What moves: responsibility claim, accommodation request, evidence request, audit trail, and response message
- Physical agency: the applicant can request review or accommodation. HR, compliance staff, or legal staff can open a case, investigate, and decide whether to change the result
- Virtual agency: case systems create tickets, retrieve logs, attach records, and route the issue across departments or to the vendor

## Pathway 5 - Feedback and system update pathway
SVD: Hiring outcomes and audit findings -> policy revision, model tuning, and process redesign -> future screening conditions

- Source node on the BBS Quad: remote physical and remote virtual
- Vector: audit review, validation testing, threshold change, training-data update, documentation change, and process redesign
- Destination node on the BBS Quad: remote virtual, with downstream effects on future applicants in local virtual space
- What moves: performance metrics, fairness findings, complaint patterns, validation results, and revised rules
- Physical agency: employer leadership, HR policy owners, compliance staff, and vendor engineers decide whether to change the process
- Virtual agency: audit dashboards, model retraining tools, configuration panels, and deployment systems implement those changes

# Part 3 - Relativistic Physical and Virtual Travel Description
## Travel description by pathway

### Pathway 1 travel
The pathway starts in local physical space when the applicant types, speaks, records, uploads, or clicks. It crosses into local virtual space when the applicant interacts with the portal, form, or assessment interface. It then jumps into remote virtual space when the platform stores the submission in the ATS or sends it to vendor systems.

Agency shifts fast in this pathway. The applicant acts first. The platform then takes over by validating fields, rejecting formats, or forcing the applicant into the next screen. Information access narrows after submission. Before submission, the applicant can see and edit the material. After submission, the applicant usually sees only the surface version of what was sent, while the system can parse and reformat it into hidden internal representations.

### Pathway 2 travel
This pathway lives mostly in remote virtual space. The ATS record becomes structured data, then features, then scores, then ranking labels. These transformations happen in systems the applicant cannot see directly. Recruiters may later view the output through a dashboard that exists in remote virtual space but is tied to remote physical action when a person reads and uses it.

### Pathway 3 travel
The decision pathway begins in remote virtual space when the recruiter or hiring manager receives a scored or ranked output. It moves into remote physical space when a recruiter or manager acts in their institutional role and makes or confirms a hiring decision. It returns to local virtual space when the applicant receives a status update, rejection, or invitation.

### Pathway 4 travel
The accountability pathway starts when the applicant notices a problem and uses local physical and local virtual channels to file a challenge, ask for review, or request an accommodation. The claim moves into remote physical space when HR or compliance staff receive it and into remote virtual space when they open a case, pull logs, or contact the vendor. It may return to the applicant as a portal notice, email, revised decision, or denial.

### Pathway 5 travel
The feedback pathway begins after outcomes accumulate. Complaints, audit findings, and hiring metrics are gathered in remote virtual systems and reviewed by people in remote physical roles. Those actors may update thresholds, change policies, retrain models, or disable a feature. The effects then travel forward into future applicant interactions in local virtual space.

This pathway is recursive. A destination becomes a new source. A past decision becomes input for a future design choice. From the applicant's perspective, this is often the most distant pathway because it shapes the system without being directly visible.

## Observer shift note
If the recruiter were the point of origin, the dashboard would feel local rather than remote, and applicant-facing interfaces would feel more distant. If the vendor were the point of origin, model logs and deployment systems would feel local, while applicant experience would be more remote and partly abstract. The pathway stays the same, but the map changes because BBS distance is relative to the observer.

# Part 4 - Pathway Transformation and Friction Analysis

## Pathway 1 - Applicant data submission
- Information transformation: a resume or answer becomes a structured platform record. Context is reduced when rich narrative experience is turned into fields and tokens.
- Physical and virtual agency: the applicant controls submission content only up to the point of upload. After that, the interface controls format, sequence, and required fields.
- Access asymmetry: the applicant sees the entered data. The system sees both the visible form and hidden metadata such as timestamps, completion patterns, and file properties.

## Pathway 2 - Data transformation and scoring
- Information transformation: the system turns application materials into features, scores, and ranks. This is the sharpest narrowing point in the whole system.
- Physical and virtual agency: virtual agency dominates because the model performs the scoring. Human agency still shapes the model upstream through feature selection, labels, thresholds, and design choices.
- Access asymmetry: recruiters may see scores and summaries. Applicants often see neither. Vendors may see even more through diagnostics and tuning tools.

## Pathway 3 - Hiring decision
- Information transformation: ranked outputs become a final status change. The long reasoning chain is compressed into one action label such as reject, hold, or invite.
- Physical and virtual agency: human authority is strongest here because recruiters or hiring managers can approve, reject, or override. Virtual agency still constrains the decision by shaping what is visible and how candidates are ordered.
- Access asymmetry: the recruiter may see summaries and rankings. The applicant may see only the final outcome.
- Authority and responsibility divergence: formal authority sits with the employer, but the practical influence may sit upstream in the scoring pipeline.
- Ethical distance: ethical distance grows when the person delivering the final decision did not build the model, cannot inspect its internals, and still acts on its output.

## Pathway 4 - Accountability and contestation
- Information transformation: a personal complaint becomes a case file, then a compliance issue, then a recorded response.
- Physical and virtual agency: the applicant can initiate a challenge, but institutional actors control whether the case expands, stalls, or closes. Case software also shapes what can be attached, tracked, or escalated.
- Access asymmetry: the employer can inspect much more of the system than the applicant can. The applicant often must challenge a process while seeing only a small part of it.
- Opacity increase: opacity can either decrease if a meaningful explanation is given, or increase if the review ends with a generic response.
- Feedback loops: this pathway may or may not create a loop. A single complaint can change nothing. Repeated complaints may trigger audits or redesign.
- Tool versus partner: the AI remains mostly a tool in this pathway. Humans own review, explanation, and response duties.

## Pathway 5 - Feedback and system update
- Information transformation: outcomes and complaints become metrics, audit findings, and redesign proposals.
- Physical and virtual agency: physical agency sits with policy owners, leadership, and vendor staff who authorize changes. Virtual agency sits with audit dashboards, retraining systems, and deployment tools.
- Access asymmetry: future applicants are affected by system changes they cannot inspect. Internal actors can see patterns that individual applicants cannot see.
- Authority and responsibility divergence: a vendor may make technical changes, but the employer remains responsible for how the changed system is used.
- Ethical distance: distance is high because future applicants experience the outcome of decisions made far upstream in spaces they never enter.

