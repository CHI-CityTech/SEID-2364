# Assignment 7 - EU AI Act System Evaluation

## 1. System Description

The system is an AI-assisted hiring and applicant-screening system. Employers use it to sort, score, rank, advance, delay, or reject job applicants. The system can include a job portal, applicant tracking system, resume parser, assessment platform, scoring model, recruiter dashboard, automated messages, and audit logs.

The main actors are the applicant, employer, recruiter or hiring manager, software vendor, and technical system. The primary target is the applicant whose application is evaluated. Secondary targets include other applicants, employer teams affected by the hiring outcome, and people connected to the applicant, such as dependents.

The system performs a selection-support action. It takes applicant materials, transforms them into structured data, scores or ranks the applicant, and presents a recommendation or status option to a recruiter or hiring manager.

## 2. Mediation Pathway

The system operates through a mediated pathway rather than one isolated decision. The applicant begins the process locally by submitting materials. The platform then moves those materials into remote virtual systems, where parsing, scoring, ranking, and dashboard display occur. The hiring decision becomes visible again only when the applicant receives a status update.

### Core SVD Pathway

Applicant materials -> job portal, ATS parsing, feature extraction, scoring model, dashboard review -> applicant status change

### Detailed Pathway Map

```
    A[Applicant submits resume, forms, assessments, or interview answers] --> B[Job portal and ATS store submission]
    B --> C[Parser converts materials into structured fields and features]
    C --> D[Scoring model ranks or flags applicant]
    D --> E[Recruiter dashboard displays score, rank, or recommendation]
    E --> F[Recruiter or hiring manager advances, holds, or rejects applicant]
    F --> G[Applicant receives status update]
    F --> H[Audit logs and hiring records]
    H --> I[Compliance review, vendor review, or system update]
    I --> C
```

### Where Transformation Occurs

Transformation begins when the portal converts the applicant's physical and virtual actions into platform-readable data. A resume, assessment answer, or video response becomes a stored record. The sharpest transformation occurs when the ATS and model turn that record into features, scores, rankings, or flags. At that point, the applicant's experience is narrowed into technical signals.

### Where Visibility Is Gained or Lost

The applicant has the most visibility before submission because they can see and edit their own materials. Visibility drops after submission. The applicant usually cannot see how the portal parses the resume, how the model scores the application, or which threshold shaped the result. Recruiters gain visibility through the dashboard, but even they may only see summaries rather than the full scoring logic. Vendors may have the most technical visibility through logs and diagnostics.

### Where Regulation Could Intervene

Regulation can intervene at several points. It can regulate data quality during feature extraction, scoring, and ranking. It can require documentation and logs during model development and deployment. It can require transparency where applicants interact with chatbots or receive AI-shaped outcomes. It can require human oversight where recruiters rely on ranked outputs. It can prohibit certain video-analysis features if they infer emotions in an employment context.

## 3. EU AI Act Classification

### Core Function

The core function is to support employment recruitment and selection by analyzing applicant materials, filtering applications, evaluating candidates, and presenting ranked outputs or recommendations.

### Use Case Classification Table

| Use Case | Use Condition | EU AI Act Category | Classification Reason |
|---|---|---|---|---|
| Resume screening and applicant ranking | An employer uses AI to analyze resumes, filter applications, score assessments, or rank candidates for a job opening. | High Risk  | The system is used for recruitment or selection, including analysis and filtering of job applications and evaluation of candidates. |
| Candidate-facing chatbot for scheduling and basic questions | The chatbot answers questions, schedules interviews, or gives application status updates without scoring, ranking, or filtering applicants. | Limited Risk | The system interacts directly with natural persons, so applicants should be informed that they are interacting with AI. It is not high-risk if it does not materially influence hiring decisions. |
| Video interview analysis that infers emotions | A video-interview tool analyzes facial expression, voice, or body language to infer emotions and uses that signal in hiring. | Prohibited Risk | The Act prohibits AI systems that infer emotions of a natural person in workplace and education settings, except for medical or safety reasons. |

### Risk Escalation Pathways

A chatbot begins as limited risk when it only answers questions or schedules interviews. It escalates to high risk if it collects screening answers, ranks applicants, recommends rejection, or otherwise materially influences selection. At that point, it becomes part of the recruitment or selection pathway under Annex III, 4(a).

A basic resume parser may appear procedural if it only extracts fields for human review. It becomes high risk when the extracted fields influence ranking, filtering, shortlist generation, or rejection. If the parser profiles natural persons, Art. 6(3) makes high-risk classification harder to avoid.

A video-interview tool is high risk when it evaluates candidates without emotion inference. It becomes prohibited if it infers emotions from the applicant in an employment context, unless the use is for medical or safety reasons.

## 4. Justification Using the Act

### Use Case 1: Resume Screening and Applicant Ranking

Classification: High Risk.

Art. 6(2) states that AI systems referred to in Annex III are high-risk. Annex III, 4(a) covers AI systems used for recruitment or selection of natural persons, including systems used to analyze and filter job applications and evaluate candidates. The resume-screening and ranking version of this system fits that language directly because it analyzes applications and evaluates candidates for employment.

Art. 6(3) creates a possible exception for some Annex III systems that do not pose a significant risk, including narrow procedural or preparatory tasks. That exception does not fit the main version of this system because ranking, filtering, and scoring materially influence who moves forward. If the system profiles applicants, Art. 6(3) also states that it is always high-risk.

The main ambiguity is the line between a narrow preparatory tool and a decision-shaping tool. A parser that only organizes text may be treated differently from a parser that feeds ranking or rejection. In this system, the parser feeds scoring and shortlist generation, so the high-risk classification is stronger.

### Use Case 2: Candidate-Facing Chatbot for Scheduling and Basic Questions

Classification: Limited Risk.

Art. 50(1) requires providers to ensure that AI systems intended to interact directly with natural persons are designed so that people are informed they are interacting with AI, unless that is obvious from the context. A candidate-facing chatbot that answers basic questions or schedules interviews fits this transparency category.

This use case is not classified as high risk when it does not evaluate candidates, score answers, filter applications, or influence the hiring outcome. The legal line changes if the chatbot asks screening questions and forwards scored results to the recruiter. In that changed condition, the system enters the recruitment and selection category under Annex III, 4(a).

The ambiguity is practical. A chatbot may appear administrative while quietly collecting signals that influence ranking. The classification depends on whether the chatbot only supports communication or becomes part of the assessment pipeline.

### Use Case 3: Video Interview Analysis That Infers Emotions

Classification: Prohibited Risk.

Art. 5(1)(f) prohibits the placing on the market, putting into service, or use of AI systems to infer emotions of a natural person in the areas of workplace and education institutions, except where intended for medical or safety reasons. A video-interview tool that infers emotions from an applicant's face, voice, or body language for hiring purposes fits this prohibited use condition.

If the video feature only records, transcribes, or summarizes interview answers without emotion inference, the classification changes. It would likely fall back into high risk under Art. 6(2) and Annex III, 4(a) if it evaluates candidates or helps filter applications.

The main ambiguity is whether a vendor labels the feature as emotion recognition, personality inference, engagement scoring, communication scoring, or interview analytics. The substance matters more than the label. If the tool infers emotions in an employment context, the prohibited category is triggered.

## 5. Risk Analysis

Risk enters the system before the applicant is scored. The employer chooses job criteria, required fields, assessment formats, thresholds, and which vendor tool to use. These upstream decisions shape which applicant traits the system treats as relevant. If those criteria are poorly chosen, applicants can be disadvantaged before any individual file is reviewed.

The scoring stage creates the strongest risk concentration. The model converts applicant features into scores, ranks, flags, or recommendation labels. This stage is remote from the applicant and often hidden. The applicant usually cannot see which data mattered, whether an accommodation was considered, or whether the score came from a reliable job-related measure.

The dashboard stage spreads risk into human decision-making. Recruiters may treat the ranking as neutral or authoritative. Even when humans can override the system, the dashboard shapes what they see first, which applicants appear strongest, and which cases seem worth reviewing. This is where virtual agency can steer physical institutional action.

The main exposed party is the applicant. The harms can be economic, social, reputational, and psychological. Economic harm appears when a qualified person loses a job opportunity. Social harm appears when groups with disabilities, accents, caregiving gaps, or nonstandard work histories face repeated exclusion. Reputational harm can occur if the applicant is flagged as weak or risky inside employer records. Psychological harm can occur when the applicant receives rejection without an understandable reason.

The system can also affect secondary targets. Other applicants compete within the same ranking environment. Employer teams receive workers selected through the system. Dependents can be affected when an applicant loses income. The harm therefore does not stop at the individual rejection notice.

## 6. Research Integration

The Trustworthy AI guidelines help explain the ethical foundation behind the EU AI Act. The guidelines emphasize human agency and oversight, technical robustness, privacy and data governance, transparency, diversity and non-discrimination, societal well-being, and accountability. These ideas appear in the Act as legal obligations for high-risk systems, especially documentation, transparency, human oversight, data governance, and risk management.

The philosophical background is mixed. The Act shows rights-based and deontological reasoning because it protects fundamental rights and prohibits certain practices regardless of efficiency. It also shows justice-oriented reasoning because employment systems are regulated as high risk due to their effects on opportunity and equal access. Consequentialist reasoning appears in the risk-based structure, where obligations increase as likely harm increases.

The ECNL critique complicates this picture. ECNL argues that the Act contains loopholes, enforcement gaps, and weak participation mechanisms. That critique matters for this hiring system because the applicant's strongest problem is limited access to hidden decision stages. If affected people cannot inspect scoring, challenge outputs, or participate in oversight, formal high-risk classification may not fully protect them.

Overall, the research supports the main classification. The core hiring system is high risk under the EU AI Act when it evaluates or filters candidates. The chatbot is limited risk only if it stays outside evaluation. Emotion inference in video hiring is prohibited when it infers emotions in the employment context. The mediation pathway shows why the classification matters: risk grows as the applicant's information moves into remote, hidden, and decision-shaping systems.

