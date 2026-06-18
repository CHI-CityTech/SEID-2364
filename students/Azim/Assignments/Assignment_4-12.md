# SEID 2364 Assignments
**Name:** Azim Aydogdyyev  
**Course:** SEID 2364 – Societal and Ethical Impacts of Data Science  
 

## Note About This Document

This document is my combined version of the previous assignment drafts. Since the later assignments were connected and built on each other, I am submitting them together as one iterative document. My main thread is about AI/data systems, responsibility, harm, and platform governance. I mostly use the COVID-19 misinformation moderation case because it connects well to BBS, EDOCA, professional codes, regulation, and future AI risks.



---

## Assignment 4 – Ethical Frameworks and the Evaluation of Harm

For this part, I focused on the problem of harm in AI and platform systems. A good example is COVID-19 misinformation moderation. During the pandemic, platforms had to decide whether to remove, label, downrank, or leave up content that might be false or harmful. The ethical problem is not simple because both action and inaction can cause harm.

If platforms remove too much content, they can harm free expression and public trust. If they remove too little, false health information can spread and maybe lead people to unsafe decisions. This makes the case useful for ethical frameworks because there is no perfect answer.

From a consequentialist view, the best action is the one that reduces the most overall harm. This could support removing dangerous misinformation if it prevents illness or confusion. But consequentialism also has a weakness because it can justify too much control if the expected benefit is large enough.

From a deontological view, platforms and data professionals have duties. They should not deceive users, hide important decisions, or treat people only as data points. Even if content moderation helps public health, users still deserve transparency and some way to appeal decisions.

My first conclusion was that ethical analysis cannot only ask, “Did the system reduce harm?” It also has to ask, “Who had power, who was affected, and could people understand or challenge the decision?”

---

## Assignment 5 – System Structuring and Ethical Analysis

In Assignment 5, I moved from judging the decision to describing the system. The system I am focusing on is platform moderation of COVID-19 misinformation.

**Decision statement:** A social media platform labels, downranks, or removes a user’s post because the system classifies it as COVID-19 misinformation.

The main actors are the user, the platform, automated moderation tools, human moderators, public-health authorities, fact-checkers, and regulators. The target is first the user whose content is moderated. The secondary targets are other users who might see the content, public-health institutions, and the wider public.

The determinants include platform policy, public-health guidance, local laws, machine-learning models, and internal trust-and-safety rules. Contributors include fact-checking organizations, health agencies, content reviewers, and the users who report content.

Important data inputs include the content of the post, account history, keywords, links, engagement patterns, previous moderation decisions, and public-health guidance available at that time.

This assignment helped me see that a decision is not made by one person or one machine. It is produced by a system. The final label or removal is only the visible outcome. Behind it there are policies, model thresholds, training data, human judgment, and institutional pressure.

---

## Assignment 6 – Mediation Pathways Across Physical and Virtual Space

For Assignment 6, I used BBS to trace how information and authority move through the moderation system. My point of origin is the ordinary platform user who posts or reads health information online.

One simple mediation pathway is:

**User post → platform interface → automated classifier → moderation decision → affected audience**

The source is the user’s post. The vector is the platform system, including algorithms and moderation policies. The destination is the final public or restricted version of the post.

Another pathway is:

**Public-health authority → official guidance → platform policy team → moderation rule → user experience**

This pathway shows that authority can begin outside the platform but still become part of the platform’s technical system. A health authority may not directly remove a post, but its guidance can influence what the platform decides to remove or label.

A third pathway is:

**Moderation action → user notification → appeal system → human review → final decision**

This is important because ethical systems need contestability. If users cannot understand or appeal a decision, then the system has low observability from the user side.

BBS helped me understand that “local” and “remote” are not only physical. A decision can feel local to a user because it affects their account immediately, but the actual authority and control may be remote, inside a platform policy team or model system that the user cannot see.

---

## Assignment 7 – EU AI Act System Evaluation

For Assignment 7, I looked at how regulation can classify and control AI systems. The EU AI Act is useful because it does not only ask whether AI is good or bad. It asks what risk category the system belongs to and what obligations follow from that category.

A COVID misinformation moderation system could involve AI if it uses automated classifiers, recommender systems, or ranking tools to detect and limit content. It may not always be “high-risk” in the same way as AI used in healthcare, hiring, or policing, but it can still affect public debate, access to information, and user rights.

The EU approach is useful because it pays attention to transparency and platform accountability. For example, if users are affected by automated decisions, they should not be completely in the dark. The system should explain, at least in a basic way, why content was labeled or removed.

At the same time, regulation has limits. A law can define categories and obligations, but real systems are messy. A moderation system might be partly automated and partly human. It might work differently in different countries. Also, a rule that looks reasonable during a public-health crisis might become too broad later.

My takeaway is that law is important, but legal compliance is not the same as full ethical responsibility. A platform can follow rules and still create unfair or unclear outcomes if users cannot observe, challenge, or understand what is happening.

---

## Assignment 8 – Bias, Decision-Making, and Harm in AI-Mediated Systems

For Assignment 8, the main idea was bias. I understand bias as a pattern where a system treats people, groups, or information unfairly because of its data, design, context, or assumptions. Bias is not always intentional. Sometimes it enters through training data, labels, missing context, or the way a model defines “normal.”

Using an AI moderation or ranking system, bias can appear in different deployments. In one context, the system might be used to find dangerous health misinformation. In another context, it might be used to downrank political content. In a third context, it might be used in a country with weaker free-expression protections.

The same core technology can create different harms depending on where it is used. A classifier trained mostly on English content may work badly with other languages or local slang. A rule meant to reduce harmful misinformation may accidentally silence minority communities discussing real experiences with healthcare.

This assignment helped me understand that fairness is not just about model accuracy. A system can be accurate in a general sense and still be unfair for a specific group. Also, the decision authority matters. If the system only gives advice to a human moderator, the risk is different than if it automatically removes content at scale.

My basic position from this part is that AI systems should be tested in the actual context where they are used, not only in abstract benchmark conditions.

---

## Assignment 9 – Mediation Pathways, Capability, and Responsibility

Assignment 9 added EDOCA and the idea of capability. The question is not only whether harm was intended. A system can create foreseeable harm even if nobody says they wanted that harm.

For COVID misinformation moderation, the platform has high capability. It can remove, label, downrank, recommend, suspend, or amplify content. Users usually have much less capability. They can post, delete, or appeal, but they cannot see the full ranking or moderation logic.

Using EDOCA:

- **Effort:** Platforms invest effort in automated detection, human review, policy teams, and reporting systems.
- **Distortion:** A post can lose context when it is classified by a model. Satire, personal testimony, or uncertain scientific discussion can be misread.
- **Observability:** Platforms see much more of the system than users do. Users often only see the result.
- **Control:** Platforms control ranking, visibility, enforcement, and appeal design.
- **Authority:** Public-health authorities, regulators, and platform leadership all have different forms of authority.

The problem is that control and responsibility are not always in the same place. A government may influence public-health standards, but the platform controls enforcement. A model may make the first classification, but a company designed the model. A user may be harmed by a decision, but may not know who really made it.

This made me think that professional responsibility should include foreseeable misuse or foreseeable failure, not only direct intention.

---

## Assignment 10 – System Synthesis and Communication

Assignment 10 was about bringing the previous work together. The core ethical tension I identified is this:

**AI-mediated moderation can reduce real harm, but it can also concentrate power over information in systems that are hard for users to see or challenge.**

This tension includes regulation, bias, and responsibility at the same time. Regulation can create rules, but it may not fully solve the problem of context. Bias can enter through data and deployment. Responsibility can become spread across platforms, governments, models, moderators, and users.

A simple research question from this synthesis is:

**How should AI-mediated moderation systems balance public-harm reduction with transparency, user rights, and accountability when information is uncertain or politically sensitive?**

My possible argument is that the answer cannot be “always remove” or “never remove.” The better approach is proportional moderation: use labels or downranking when uncertainty is high, use removal for clearly harmful claims, provide clear explanations, and create real appeal options.

This also connects to my professional ethical position. Data scientists should not only build systems that work technically. They should ask how the system will be used, who can be harmed, who has control, and whether affected people can understand or challenge the outcome.

---

## Assignment 11 – ACM/IEEE COVID Case Analysis

For Assignment 11, I used the COVID-19 misinformation moderation case with ACM and IEEE professional codes.

The intervention strategy I focused on is platform labeling and downranking of COVID misinformation, instead of only removing content. This strategy is ethically complicated because it tries to reduce harm without fully silencing users. But it still affects visibility and public debate.

The ACM Code is useful because it emphasizes avoiding harm, being honest, respecting privacy, and contributing to society and human well-being. In this case, ACM would support reducing harmful misinformation, but it would also require transparency and careful design. If users are affected by moderation, the platform should explain enough for users to understand the decision.

The IEEE Code is useful because it emphasizes public safety, technical competence, honesty, and responsible judgment. In this case, IEEE would push engineers to think about whether automated moderation is reliable enough and whether errors could cause serious harm.

Both codes agree that professionals cannot hide behind “the system did it.” They have responsibility for the tools they design and deploy. The difference is that ACM feels broader and more social, while IEEE feels more technical and safety-focused.

My conclusion is that professional codes are helpful, but not enough by themselves. They give principles, but real systems still need governance: audits, appeals, transparency reports, and limits on automated enforcement.

---

## Assignment 12 – Case Study Specification

For Assignment 12, I treated COVID-19 misinformation moderation as a strategic system. The agents include platform companies, users, public-health authorities, fact-checkers, bad actors, regulators, and affected communities.

Each agent has different goals. Platforms want to reduce harm but also protect engagement and avoid public criticism. Public-health authorities want people to follow reliable guidance. Users want to speak, share, learn, and sometimes challenge official claims. Bad actors may want attention, money, or political influence. Regulators want accountability, but they may not fully understand the platform’s internal systems.

The signals in the system include posts, shares, labels, rankings, reports, public-health updates, moderation notices, and appeals. These signals can change meaning as they move. A post that starts as a personal opinion can become a viral public-health risk. A moderation label can be seen as helpful guidance by one person and censorship by another.

The ethical tension is that the system has no neutral option. Intervening can reduce harm but can also create power and trust problems. Not intervening can protect expression but can allow misinformation to spread.

A governance recommendation would be to use different levels of intervention depending on confidence and risk. The system should also include transparency reports, appeal rights, human review for serious penalties, and extra care for scientific uncertainty.

---

## Closing Reflection

Across these assignments, my thinking changed from looking for one correct ethical answer to looking at systems, pathways, and responsibility. At the beginning, I thought ethics was mostly about choosing the better side. Now I think it is more about understanding the whole structure before making a judgment.

The biggest lesson for me is that AI and data systems are not only technical tools. They are part of social and institutional systems. A model output can affect someone’s rights, opportunities, speech, privacy, or trust. Because of that, data scientists and engineers have responsibilities before and after deployment.

My current view is simple: systems should help people without hiding power from them. If a system affects people in important ways, it should be explainable enough, contestable enough, and accountable enough. If those conditions are missing, then the system should not be treated as ethically ready.

---

