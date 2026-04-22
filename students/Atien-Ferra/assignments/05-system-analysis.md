## Part 1 - System Structure (Descriptive Layer)

-   Actors
The main actors in this case are the employers, recruiters or hiring managers, the applicant, and the vendor that builds or maintains the screening tool. The technical system also acts inside the process because it parses resumes, scores assessments, ranks candidates, or flags applications for review. NIST treats these roles as part of the broader set of AI actors involved in design, development, deployment, and use.

-   Targets
The primary target is the applicant whose file is scored, ranked, advanced, or rejected. Secondary targets include other applicants competing for the same role, the employer that depends on the hiring outcome, and people connected to the applicant, such as dependents who may be affected by loss of opportunity. 

-   Determinants
The main determinants are job requirements, screening criteria, model design, training data, assessment thresholds, accommodation rules, and employer policy. These factors shape what counts as a strong or weak application before any final human review happens. Research on algorithmic hiring shows that vendor choices about prediction targets, data collection, and validation can strongly affect results.

-   Contributors
Contributors are actors that influence the outcome without always making the final decision. These include software vendors, HR staff who configure the tool, data providers, managers who set hiring priorities, and compliance staff who decide how accommodations are handled. Their choices shape the system long before an applicant receives a result.

-   Information
The system uses resumes, application forms, test results, interview responses, job descriptions, historical hiring data, and employer-set criteria. Some systems also use chat-based screening or video interview analysis. These inputs are transformed into features, scores, and rankings that guide later decisions.

-   Source
Some information comes from the person applying, such as work history, education, assessments, and interview answers. Some comes from the employer, such as job requirements and screening thresholds. Some comes from vendors or prior datasets used to build and validate the system.

-   Authority
Applicants control the first submission of their own materials, but employers and vendors often control how those materials are stored, interpreted, and scored. Employers also control job criteria and the conditions under which the tool is used. NIST frames this as a governance issue across the AI lifecycle, while the EEOC makes clear that employers remain responsible when these tools are used in employment decisions.

-   Trust Basis
The system treats inputs as valid because they come from formal application materials, employer-defined criteria, and vendor-built tools presented as job-related and consistent. That trust may rest on institutional authority, technical claims, prior use, or internal validation. The problem is that accepted inputs can still contain gaps, bias, or barriers that affect some applicants more than others.

-   Contrasting example
One applicant submits a standard resume, completes the assessment in the expected format, and matches the training profile the system favors, so the system ranks that person highly and moves them forward. Another applicant has a caregiving gap, requests an accommodation, or communicates in a way the model does not score well, so the same system routes that person to rejection or extra review. The decision type is the same in both cases, but different conditions mean different outcomes in the system.

## Part 2 - Interpretive Layer (Ethical Overlay)

Authority sits mainly with the employer because the employer chooses the hiring process. Employers control the hiring process and applicant records in use, while vendors may control the model, scoring logic, and technical infrastructure. 

Agency is distributed across people and systems. Applicants act by submitting information, requesting accommodations, or appealing outcomes. Recruiters and managers act by setting thresholds or overriding recommendations. Vendors act upstream by defining model behavior and validation choices.

## Part 3 - System Flow (Pre-Framework)
The employer defines the role, sets job criteria, and selects an AI-assisted hiring process.
The applicant submits materials such as a resume, form responses, assessments, or interview data.
The system converts those inputs into structured features, scores, or rankings based on employer rules and vendor design choices.
Recruiters or hiring managers receive ranked outputs, flags, or recommendations and use them to advance, hold, or reject applicants.
Downstream decision points occur when a candidate is moved forward, rejected, asked for more information, or routed into appeal or accommodation processes.
The outcome feeds back into the system through recordkeeping, audit, validation, and future model or policy updates. NIST describes this as part of ongoing AI governance and risk management rather than a one-time decision.