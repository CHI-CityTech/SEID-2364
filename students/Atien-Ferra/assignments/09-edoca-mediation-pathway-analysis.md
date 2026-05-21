# Assignment 9 - EDOCA Mediation Pathway Analysis

## Incident Selected

This report analyzes the wrongful arrest of Robert Williams by the Detroit Police Department in January 2020. Williams was arrested after police relied on an incorrect facial recognition lead connected to a 2018 shoplifting investigation at a Shinola store in Detroit. The facial recognition search compared a poor-quality surveillance image to a photo database and returned Williams as a possible match. Police then used that lead in a photo lineup and later sought an arrest warrant. Williams was detained for about thirty hours before the case unraveled.

This incident fits Assignment 9 because it involves multiple agents, including a person wrongly identified, police investigators, a facial recognition system, a photo database, a witness or loss-prevention contractor, a court warrant process, and institutional policy. It also has traceable mediation pathways. Harm did not come from one isolated mistake. It emerged as information moved through several Source-Vector-Destination transitions, with distortion, limited observability, weak control, and divided authority at each step.

Sources for the incident include the ACLU case page on *Williams v. City of Detroit*, the ACLU settlement announcement, Robert Williams’s own account through the ACLU of Michigan, and the NIST Face Recognition Vendor Test report on demographic effects in face recognition.

## 1. Incident Narrative

The pathway began with store surveillance footage of a person suspected of stealing watches. Police extracted or selected a still image from that footage and sent it for a facial recognition search. The search returned Robert Williams as a possible match, based on an expired driver’s license photo. The match was incorrect.

Instead of treating the facial recognition result only as a weak lead, police used Williams’s photo in a lineup. The lineup was shown to a Shinola loss-prevention contractor who had not witnessed the theft directly and who relied on the same poor-quality footage. Police then used the identification pathway to support an arrest warrant. Williams was arrested at his home in front of his family and detained.

The 2024 settlement in *Williams v. City of Detroit* required stronger guardrails. Detroit police cannot arrest someone based only on facial recognition results or on a lineup created directly from a facial recognition lead. The settlement also requires independent evidence, training, and audits of earlier cases.

## 2. Agents and System Components

| Agent | Role in the incident | Type of agency |
|---|---|---|
| Robert Williams | Target of the false match and arrest | Human target with little control |
| Detroit Police Department | Investigated the case, built the lineup, sought the warrant, made the arrest | Institutional and physical agency |
| Michigan State Police / facial recognition search process | Ran or supported the face recognition search | Institutional and computational agency |
| Facial recognition algorithm | Compared the probe image against a database and produced a candidate lead | Computational agency |
| Driver’s license photo database | Supplied gallery images for comparison | Infrastructural data source |
| Shinola loss-prevention contractor | Viewed lineup and contributed identification signal | Human contributor |
| Court / magistrate process | Validated the warrant pathway | Institutional authority |
| ACLU / legal advocates | Challenged the arrest and forced policy change | Accountability pathway agent |

## 3. EDOCA Analysis 2: SVD-P4, Lineup Identification

**Transition:**  
Photo lineup and surveillance image -> contractor review and identification -> identification signal

### Effort / Energy

The lineup reduced police effort by turning a computational lead into a human-facing identification process. A contractor reviewed the lineup instead of police having to build independent evidence first.

The human reviewer also took on cognitive effort. They had to compare images and make a judgment, but their judgment was shaped by the lineup that police constructed from the facial recognition lead.

### Distortion / Fidelity

This stage can create a false sense of independent confirmation. The lineup appears to add human judgment, but it is downstream from the same flawed source image and false facial recognition lead. The signal does not become independent just because a person reviews it.

The contractor did not witness the theft directly. If the reviewer relied on the same poor-quality footage, then the pathway reused the original distortion rather than correcting it.

### Observability

Police could see the lineup result. The contractor could see only the lineup and available images, not the full technical uncertainty behind the facial recognition search. Williams could not see or challenge the lineup before the arrest.

This stage increased the appearance of observability for police while leaving the target invisible and absent.

### Control

Police controlled the lineup construction. The contractor controlled only the response within the frame given to them. Williams had no control over the lineup, the comparison conditions, or the chance to provide an alibi at this stage.

### Authority

The contractor had no final legal authority, but their response gained authority inside the investigation file. Police then used that file to support the warrant path. This is an authority conversion point, where a weak contributor signal became part of state action.

## 4. EDOCA Analysis 3: SVD-P5, Warrant Application

**Transition:**  
Investigation file and identification signal -> warrant application and judicial approval -> arrest warrant

### Effort / Energy

The warrant process required police labor, documentation, and judicial review. It also required institutional trust. The court process depends on the assumption that police disclose important reliability limits.

For Williams, the effort cost appeared later. He had to endure arrest, detention, legal uncertainty, and later litigation to challenge the system.

### Distortion / Fidelity

This stage compressed the pathway. A blurry image, a false match, and a lineup response became a legal narrative. The more the file moved toward warrant approval, the less visible the earlier uncertainty became.

The ACLU case summary says the warrant application omitted significant information that would have warned the magistrate that the face recognition result and lineup procedure were unreliable. That omission is a major distortion because it changed what the court could evaluate.

### Observability

The magistrate could observe only what appeared in the warrant application. Williams could not see or contest the evidence before arrest. The public could not observe the pathway until after litigation and reporting.

Observability was therefore delayed. The system became visible only after harm occurred.

### Control

Police controlled what information entered the application. The magistrate controlled whether to approve the warrant, but that control depended on the fidelity of the submitted file. Williams had no control until after the arrest.

### Authority

This is where formal authority became strongest. The warrant converted a mediated chain of uncertain signals into legal permission for physical arrest. Authority appeared clear at the endpoint, but the reliability of that authority depended on earlier SVDs that remained weak and partly hidden.

## 5. Cumulative Distortion Across the Pathway

The incident did not fail at one point only. Distortion accumulated.

```
Surveillance footage
  -> low-quality still image
  -> facial recognition candidate lead
  -> police lineup
  -> contractor identification
  -> warrant application
  -> arrest and detention
```

The original signal was weak. Instead of preserving uncertainty, the pathway converted uncertainty into confidence. Each step made the output look more official. The computational lead became a police lead. The police lead became a lineup. The lineup became an identification. The identification became a warrant. The warrant became physical custody.

That is the key ethical problem. The system did not need one actor to intentionally create harm. Harm emerged because each SVD accepted the previous output and carried it forward with too little correction.

## 9. Mediation Pathways

### Data Pathway

Source: surveillance footage and driver’s license database  
Vector: image extraction, biometric search, candidate matching  
Destination: police investigative file

The data pathway moves from physical space to virtual space. A person in a store is captured by a camera. The video becomes digital evidence. A still image becomes a probe. The probe moves through a biometric search system. The output returns to police as a candidate lead.

### Decision Pathway

Source: candidate lead and lineup response  
Vector: police interpretation, warrant application, judicial approval  
Destination: arrest warrant and arrest action

The decision pathway moves from virtual output into institutional action. The algorithmic lead does not arrest anyone by itself. It becomes consequential when police and legal actors treat it as a usable basis for action.

### Accountability Pathway

Source: wrongful arrest and legal challenge  
Vector: complaint, litigation, discovery, settlement  
Destination: policy reform and audit requirements

The accountability pathway is delayed. Williams could challenge the system only after the arrest. The 2024 settlement created rules that require independent evidence, training, and audits. That shows that accountability existed, but it arrived after the harm.

## 6. Responsibility Distribution

Responsibility does not sit in one place.

The facial recognition system produced the false lead, but it did not decide to arrest. Police selected the image, ran or requested the search, built the lineup, interpreted the lead, and sought the warrant. The court validated the warrant based on the information presented. Department policy and training shaped whether officers treated the facial recognition result as a weak lead or as something stronger.

This is a responsibility trap. Each actor can point to another part of the pathway. The algorithm only produced a possible match. Police can say they sought human review and a warrant. The court can say it relied on the police file. The vendor or search infrastructure can say users must treat matches only as leads. Yet the combined pathway still produced an arrest.

Responsibility therefore sits mainly with the institutional users and governors of the system. Police had the practical control to decide how to use the lead. Department leadership had responsibility for policy, training, and safeguards. Courts had authority to reject weak applications, but their control depended on what police disclosed. The computational system contributed to harm, but human institutions made the output coercive.

## 7. Capability Versus Intent

This incident is best described as foreseeable harm that was not prevented. It was not necessary to show that every actor intended to arrest an innocent person. The ethical issue is that the system was capable of producing that result under normal operating conditions.

The risk was foreseeable because facial recognition can produce false positives, especially in real-world conditions such as poor image quality. NIST also documented demographic differences in false positive rates across algorithms and groups. The harmful capability existed before the arrest, but the pathway lacked enough safeguards to stop a weak signal from becoming state force.

## 8. Course Framework Connection

Using the Capability Approach, the key harm is not only the arrest itself. The system reduced Williams’s real ability to contest, understand, or prevent the outcome before it happened. He had no meaningful access to the search, the lineup construction, the warrant file, or the uncertainty embedded in the process.

Using consequentialist reasoning, the claimed benefit is faster investigation. The harm is wrongful arrest, detention, trauma, loss of trust, and the risk of repeated errors at scale. The system fails if small investigative efficiency gains come at the cost of severe and concentrated harms to people wrongly identified.

Through BBS and EDOCA, the pathway shows that ethical risk increases when control, observability, and authority separate. In this case, authority moved toward police and courts, control was split between computational and human actors, and observability for the target was nearly zero.

## 9. Conclusion

The Robert Williams incident shows how a mediated system can produce serious harm through ordinary pathway operations. A weak image became a false match. The false match became a lineup. The lineup became a warrant. The warrant became an arrest.

The most critical EDOCA findings are:

- Distortion began with poor image quality and increased through abstraction.
- Observability was highest for institutions and lowest for the person harmed.
- Control sat with police, vendors, and system designers, not with the target.
- Authority became strongest at the moment when uncertainty had already been hidden.
- Responsibility diffused across the algorithm, police, court process, and department policy.

The incident shows why EDOCA must analyze individual SVDs. The harm did not come from one broken arrow. It came from a chain of transitions that converted an uncertain signal into physical state power.
