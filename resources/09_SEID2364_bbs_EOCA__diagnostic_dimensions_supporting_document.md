# BBS Diagnostic Dimensions
## Effort, Observability, Control, Authority (EOCA)

### Framing Narrative

In the analysis of mediation pathways within the Balanced Blended Space (BBS) framework, it is not sufficient to identify where signals originate and terminate. To meaningfully evaluate how systems behave—particularly under conditions of spatial distribution, degraded connectivity, and variable access—we require a set of diagnostic dimensions.

This document introduces four such dimensions:

- **Effort / Energy**
- **Observability**
- **Control**
- **Authority**

These dimensions do not describe *what* a system is intended to do. Instead, they describe **what a system is capable of doing under actual conditions of mediation**.

---

## 1. Effort / Energy

### Definition

Effort / Energy refers to the cost required to produce a change in system state (ΔD) at a given point in the mediation pathway.

This cost may be borne by human agents, computational systems, or distributed infrastructure.

---

### Types of Cost

Effort / Energy can be analyzed through several distinct but related cost types:

#### 1. Time Cost
- Latency, delay, and waiting
- Retries and extended interaction cycles

#### 2. Cognitive Cost
- Mental effort required to interpret, decide, or compensate
- Increased uncertainty or ambiguity

#### 3. Computational / Infrastructure Cost
- Processing, bandwidth, storage, and routing
- Often hidden from the user but critical to system function

#### 4. Physical / Operational Cost
- Manual intervention or physical action
- Movement, control, or fallback to local systems

#### 5. Opportunity Cost (Optional but significant)
- Loss of alternative actions
- Reduced capability due to system limitations

---

### Key Questions

- What types of cost are present at this point in the pathway?
- Who is bearing these costs?
- How are these costs redistributed as spatial distance changes?
- Are any costs hidden or externalized?

---

### Observations

- Remote mediation often **redistributes** cost rather than eliminating it.
- Systems may reduce local human effort while increasing hidden computational cost.
- Under degraded or unavailable conditions, cost often shifts back to local agents.

---

### Example (Flight Scenario)

- Full connectivity: low cognitive and physical cost, high infrastructure support
- Degraded connectivity: increased cognitive cost and time cost
- No connectivity: full local physical and cognitive cost

---

### Key Questions

- How much effort is required to act on the system?
- Does this effort increase with spatial distance?
- Is effort borne by a human agent, a computational system, or both?

---

### Observations

- Effort is often **redistributed** rather than increased globally.
- Remote systems may reduce local human effort while increasing hidden computational effort.
- Under degraded conditions, effort often shifts back to local human agents.

---

### Example (Flight Scenario)

- Full connectivity: low human effort (automated systems)
- Degraded connectivity: increased human effort (manual decision-making)
- No connectivity: full local effort

---

## 2. Observability

### Definition

Observability is the degree to which an agent can perceive, interpret, and understand the state of a system through available signals.

---

### Key Distinction

- **Access**: Can a connection be made?
- **Observability**: Can the system state be meaningfully understood?

Access is a precondition for observability, but does not guarantee it.

---

### Key Questions

- What information is available at this point in the pathway?
- Is the information complete, partial, delayed, or misleading?
- How does spatial distance affect visibility into the system?

---

### Observations

- Observability is **graded**, not binary.
- Increased distance often introduces:
  - latency
  - abstraction
  - black-box behavior
- Systems can remain accessible while becoming effectively opaque.

---

### Example (Flight Scenario)

- WiFi available: access exists
- Low bandwidth: partial observability
- System outputs may be delayed, incomplete, or unreliable

---

## 3. Control

### Definition

Control refers to the ability of an agent to intervene in, modify, or redirect the behavior of a system at a given point in the mediation pathway.

---

### Key Questions

- Who can change the system’s behavior?
- Where does control shift as spatial distance increases?
- Is control centralized or distributed?

---

### Observations

- Control often shifts **away from local agents** as systems become more remote.
- Under degraded or unavailable conditions, control may revert to local agents.
- Control can be **fragmented**, with different agents controlling different parts of the pathway.

---

### Example (Flight Scenario)

- Normal operation: distributed control (pilot, ATC, automated systems)
- Loss of connectivity: control shifts toward the pilot (local agent)

---

## 4. Authority

### Definition

Authority is the capacity of a system or agent to assign, validate, or enforce decisions within a mediation pathway.

---

### Key Clarification

Authority is not the same as control.

- Control: ability to act
- Authority: legitimacy of decision

These may diverge.

---

### Key Questions

- Who is recognized as the decision-maker?
- Where is decision legitimacy located?
- Does authority remain aligned with control?

---

### Observations

- Authority often remains **remote** even when control shifts locally.
- Systems may continue to assert authority even when they lack capability.
- Misalignment between authority and capability is a key source of ethical risk.

---

### Example (Flight Scenario)

- Remote systems (ATC, airline systems) maintain authority
- In degraded conditions, local agents may act outside that authority

---

## Cross-Dimensional Interaction

These four dimensions do not operate independently.

A system’s behavior emerges from their interaction.

---

### Alignment vs Divergence

A system is relatively stable when:
- Effort, observability, control, and authority are aligned

A system becomes unstable when:
- One or more dimensions diverge

---

### Example Patterns

#### Case 1: No Access
- Effort: high (local)
- Observability: local only
- Control: local
- Authority: ambiguous

#### Case 2: Access + Low Observability
- Effort: moderate
- Observability: degraded
- Control: partial
- Authority: remote

→ High risk due to opacity

#### Case 3: Authority without Capability
- Effort: low (automation)
- Observability: unclear
- Control: limited
- Authority: remote

→ Ethical instability

---

## Core Principle

A system should be evaluated not by its intended function, but by what it is capable of doing under real conditions of mediation.

---

## Summary

The EOCA framework provides a diagnostic lens for analyzing mediation pathways in BBS:

- Effort reveals where work is performed
- Observability reveals what can be known
- Control reveals who can act
- Authority reveals who is recognized as making decisions

Together, these dimensions allow for a structured analysis of how spatial distance and system design influence ethical risk.

---

## Forward Connection

This framework will be extended in future analysis to consider:

- Temporal distance (latency, delay, asynchrony)
- Signal degradation and transformation
- Multi-agent interpretation and trust

---

