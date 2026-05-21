# Assignment 08 - Bias, Decision-Making, and Harm in AI-Mediated Systems

## Selected System

I selected the AI Content Moderation System from the course system selection set. 

The analysis below still uses the same structural method from my earlier work: actors, targets, information flow, mediation pathways, decision points, visibility, accountability, and harm distribution.

---

# 1. System Definition

The core system is an AI content moderation system. It evaluates user-generated content and produces outputs about whether that content should remain visible, be removed, be downranked, be flagged for human review, or be labeled with a warning.

The system performs text classification, ranking, filtering, and recommendation. In some deployments, it may also classify images, video, or links. Its main inputs are user posts, comments, messages, reports, moderation policies, labeled training data, platform history, and user metadata. Its main outputs are moderation labels, confidence scores, risk flags, visibility changes, removal recommendations, and appeal records.

The core technical function stays the same across all scenarios: the system transforms user expression into policy-relevant categories that shape visibility and access.

---

# 2. Bias and Fairness Synthesis

Bias means that a system, person, dataset, or process treats some people, groups, language patterns, or viewpoints unfairly because of built-in assumptions or uneven representation. The Stanford Encyclopedia of Philosophy explains implicit bias as prejudice or stereotyping that can shape action without conscious intent. For this assignment, that matters because bias does not need to be deliberate to affect moderation outcomes. A model can inherit biased labels from human annotators, or a moderator can treat one dialect as more aggressive than another without intending to discriminate.

Fairness means more than equal technical treatment. The SEP entry on algorithmic fairness shows that fairness is contested because different metrics protect different values. A moderation system may have the same accuracy rate across groups while still over-removing speech from a minority group. It may also reduce harmful content overall while making some users less able to participate. Fairness therefore requires attention to outcomes, error distribution, visibility, and process.

One tension between implicit bias and algorithmic fairness is that implicit bias often appears in context-specific judgment, while algorithmic fairness often tries to measure bias through formal metrics. A toxic-language classifier may look fair under one metric but still encode biased interpretations of dialect, sarcasm, reclaimed slurs, or political speech. The fairness metric may simplify what the implicit-bias problem actually is.

Search and ranking ethics clarifies a core risk in content moderation because moderation is also a visibility system. The SEP entry on search ethics emphasizes that ranked systems shape what people can find, see, and access. A moderation system does the same thing by suppressing, promoting, hiding, or routing content. That means bias is not only about removal. It also appears in ranking, review priority, appeal visibility, and the way users experience digital public space.

---

# 3. Deployment Scenarios

## Deployment 1 - Public Social Media Hate Speech Moderation

The system is deployed by a large public social media platform. It screens posts and comments for hate speech, harassment, and threats. It can automatically remove high-confidence violations, downrank uncertain content, or send items to a human moderation queue.

What changed from the baseline: the system now operates at mass public scale and has partial decision-making authority. This matters because visibility, public participation, and reputational harm are high. A single classification can silence a user, protect a target from harassment, or fail to stop harmful content.

User group: public platform users.  
Institutional context: commercial social media platform.  
Decision authority: mixed. The AI can automatically act in some cases and recommend action in others.  
Level of consequence: high for users whose speech is removed and high for targets of harmful content if the system fails.

## Deployment 2 - University Discussion Board Moderation

The same content moderation system is deployed inside a university learning management system. It screens discussion-board posts for harassment, threats, plagiarism-related abuse, or disruptive language. It sends flags to instructors or teaching assistants, who decide whether to remove content or contact a student.

What changed from the baseline: the system is now advisory and operates in an educational setting. This matters because the same moderation label can affect classroom participation, grades, disciplinary records, and a student’s willingness to speak.

User group: students and instructors.  
Institutional context: university course platform.  
Decision authority: advisory. Human instructors make final decisions.  
Level of consequence: medium to high, depending on whether a flag affects grading or discipline.

## Deployment 3 - Workplace Internal Communication Moderation

The same system is deployed inside a workplace messaging platform. It screens employee messages for harassment, threats, discrimination, policy violations, or security-sensitive content. It routes flags to HR, legal, security, or management.

What changed from the baseline: this is a secondary use of content moderation. The system no longer only manages public speech. It becomes part of workplace monitoring and employee governance. This matters because moderation outputs can affect employment, discipline, promotion, or termination.

User group: employees, managers, HR staff, and compliance staff.  
Institutional context: workplace communication system.  
Decision authority: advisory at first, but outputs can trigger formal HR action.  
Level of consequence: high because errors can affect income, reputation, and employment status.

---


## Comparative Bias Analysis Across Deployments

Consistent bias locations appear across all three deployments. First, bias can enter through training data and labels. If annotators or policy designers misread dialect, cultural language, sarcasm, or conflict language, the model can reproduce that judgment. Second, bias can enter through thresholds. A low threshold may over-flag certain groups, while a high threshold may fail to protect targets of harassment. Third, bias appears at the interface level. Dashboards, risk colors, confidence scores, and queue order can frame the user as suspicious before a human reviews the content. Fourth, bias can become recursive when past moderation outcomes feed future training or policy updates.

Some bias risks are deployment-specific. In the public social media scenario, the main added risk is public speech suppression and uneven platform visibility. In the university scenario, the risk is educational participation and instructor attention. In the workplace scenario, the added risk is employment discipline and surveillance. The same model output becomes more severe when it enters a stronger institutional pathway.

Changing the deployment context creates new bias risks because decision authority changes. In a public platform, the AI may act directly. In a university, it may shape instructor attention without formally deciding. In the workplace, it may create a record that HR treats as evidence. The bias does not stay inside the model. It changes as it passes through the institution that uses the model.

---

# 4. Decision Pathway Analysis

## Deployment 1 - Public Social Media

The system produces a violation label, confidence score, and action recommendation. The platform receives the output and may remove content automatically, downrank it, attach a warning, or send it to human review. If the output is wrong, the user may lose speech visibility, followers may not see the content, and the targeted person may remain exposed to harassment if harmful content stays online.

Human judgment enters when content is routed to a moderator or appeal reviewer. It exits when high-confidence cases are automated. Accountability is diffused because the model, policy team, moderator, and platform all shape the outcome. The user is visible mainly as a content object, while the target of harassment may be visible only if the policy or interface captures harm context.

## Deployment 2 - University Discussion Board

The system produces a flag or risk label for the instructor. The instructor or teaching assistant receives the output and decides whether to remove the post, warn the student, ignore the flag, or escalate the issue. If the output is wrong, a student may be unfairly disciplined, embarrassed, or discouraged from participating. If the system misses harmful content, another student may experience harassment or exclusion in the course space.

Human judgment remains formally present, but the AI shapes what the instructor sees first. Accountability is clearer than in the public platform scenario because the instructor or university makes the final decision. It is still partially diffused if the instructor relies on a model they do not understand. Students are visible through posts and flags, but their intent, disability context, language background, and prior classroom dynamics may not be visible.

# 5. Harm Analysis

## Direct Harm

Direct harms are harms that follow closely from the system output. In the public platform scenario, direct harm includes wrongful removal, downranking, account restrictions, failure to remove harassment, and loss of audience access. In the university scenario, direct harm includes unfair warnings, chilling participation, grade-related effects, or failure to protect students from hostile class discussion. In the workplace scenario, direct harm includes HR investigation, warning, suspension, termination risk, or failure to stop harassment.

## Indirect Harm

Indirect harm emerges through the structures that use the moderation output. One indirect pathway is: biased label -> repeated flags -> lower trust from moderators or HR -> stricter review -> more flags in the future. This can turn one classification error into an institutional pattern.

Another indirect pathway is self-censorship. If users learn that certain dialects, political viewpoints, identity terms, or emotional styles are likely to trigger moderation, they may reduce participation. This harm is indirect because it does not require a formal removal. It flows through anticipation, fear, and unequal visibility.

In the workplace scenario, indirect harm can spread to teams. If employees believe internal messages are being monitored unfairly, they may avoid reporting problems or organizing collectively. That can hide workplace harm instead of reducing it.

## Distribution of Harm

Harms are not evenly distributed. Users whose language differs from the dominant training data may face more false positives. Targets of harassment may face more false negatives if coded abuse is difficult for the model to detect. Students with nonstandard writing patterns, disabled students, multilingual speakers, or students from marginalized groups may face more scrutiny in the university deployment. Workers in heavily monitored teams may face higher risk in the workplace deployment.

This connects to the harm vocabulary from prior course work because harm is distributed across direct and secondary targets. The direct target may be the speaker whose content is removed. A secondary target may be the person harmed by content that remains visible. Another secondary target may be the community whose speech norms are reshaped by repeated moderation decisions. Harm is material, social, reputational, institutional, and psychological.

---

# 7. Critical Reflection

Responsibility for bias-related harm does not sit in only one place. It sits in the system, in the people who deploy it, and in the surrounding structures. These layers are connected. The system can encode bias through training data, labels, thresholds, policy categories, and interface design. People make choices about where to deploy it, how much authority to give it, and how much review or appeal to provide. The surrounding institution decides what a moderation output means.

The search ethics reading shows that ranking and filtering systems shape access to information. That is important because content moderation is not only about deleting bad content. It also decides what becomes visible, what gets buried, what receives human attention, and what enters an appeal queue. The ethical problem is therefore structural. It concerns the distribution of visibility and voice.

Across the three deployments, responsibility shifts but never disappears. On a public platform, the company carries major responsibility because it sets policies, controls the model, designs appeals, and profits from the space. In a university, responsibility sits with the institution and instructor because the system is advisory and humans still interpret the output. In a workplace, responsibility sits strongly with the employer because moderation becomes part of employment power. The vendor also carries responsibility in all three cases because it shapes the classifier, training process, and interface.

My position is that bias-related harm sits most heavily with the deploying institution. The model creates risk, but the institution decides what that risk can do. A false flag inside a test environment is limited. The same false flag inside a workplace HR pipeline can affect someone’s job. Deployment turns technical error into social consequence. That does not erase system responsibility or vendor responsibility. It means the strongest accountability belongs to the actor that connects the output to authority.