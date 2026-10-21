# GoT Controller Skill - Examples

## Example 1: Balanced Exploration - AI in Healthcare

### Research Topic
"AI applications in clinical diagnosis and treatment"

### GoT Execution

**Iteration 1: Initial Exploration**
```markdown
**Operation**: Generate(5) from root

Launched 5 parallel research agents:
┌─────────────────────────────────────────────────────────────┐
│ Agent 1: Current Market Landscape                          │
│ Focus: Market size, adoption rates, production deployments  │
└─────────────────────────────────────────────────────────────┘
┌─────────────────────────────────────────────────────────────┐
│ Agent 2: Technology Assessment                             │
│ Focus: Accuracy, capabilities, technical maturity           │
└─────────────────────────────────────────────────────────────┘
┌─────────────────────────────────────────────────────────────┐
│ Agent 3: Implementation Challenges                          │
│ Focus: Costs, integration, regulatory barriers              │
└─────────────────────────────────────────────────────────────┘
┌─────────────────────────────────────────────────────────────┐
│ Agent 4: Vendor Landscape                                   │
│ Focus: Key players, differentiators, market shares          │
└─────────────────────────────────────────────────────────────┘
┌─────────────────────────────────────────────────────────────┐
│ Agent 5: Case Studies                                       │
│ Focus: Successful implementations, lessons learned          │
└─────────────────────────────────────────────────────────────┘

Results:
- Node 1 (Market): Score 7.8/10 - Good industry data, some gaps
- Node 2 (Technology): Score 8.9/10 - Excellent sources, comprehensive
- Node 3 (Implementation): Score 7.2/10 - Adequate, limited real-world data
- Node 4 (Vendors): Score 6.8/10 - Some bias concerns, incomplete coverage
- Node 5 (Case Studies): Score 8.5/10 - Strong examples, good citations

**Decision**: KeepBestN(4) - prune Node 4 (score < 7.0)
```

**Iteration 2: Strategic Expansion**
```markdown
**Operation**: Diversified strategy based on scores

High Score (Node 2, Technology: 8.9) → Generate(2) deeper:
├─ Node 2a: Diagnostic accuracy benchmarks → Score 9.2/10
└─ Node 2b: Comparison by medical specialty → Score 8.7/10

High Score (Node 5, Case Studies: 8.5) → Generate(1) deeper:
└─ Node 5a: ROI and cost-benefit analysis → Score 8.1/10

Medium Scores → Refine(1) each:
├─ Node 1 (Market): 7.8 → 8.2 (improved with recent data)
└─ Node 3 (Implementation): 7.2 → 7.6 (clarified regulatory aspects)
```

**Iteration 3: Aggregation**
```markdown
**Operation**: Aggregate(8)

Input nodes: [1, 2, 2a, 2b, 3, 5, 5a]
(Corrected: 7 nodes after refinement)

Aggregation process:
1. Identify consensus points across all nodes
2. Resolve contradictions (e.g., adoption rates differ)
3. Extract key insights by category
4. Create unified narrative

Result:
- Aggregated Node: Score 9.4/10
- Comprehensive synthesis combining:
  * Market landscape with latest data
  * Technical assessment with benchmarks
  * Implementation considerations
  * Real-world case studies with ROI
```

**Iteration 4: Final Polish**
```markdown
**Operation**: Refine(1) aggregated node

Refinements:
- Improved citation completeness (added missing DOIs)
- Enhanced structure (better flow between sections)
- Clarified recommendations (more actionable)
- Added visual element descriptions

Final Output Score: 9.7/10 (Excellent)
```

**Final Graph State**:
```
Nodes: 11 total
  - 5 initial (1 pruned)
  - 3 generated from high-scoring nodes
  - 2 refined
  - 1 aggregated
  - 1 final (refined aggregate)

Operations: 4 iterations
  - Generate: 5 + 3 = 8 operations
  - Score: 11 operations
  - KeepBestN: 1 operation
  - Refine: 3 operations
  - Aggregate: 1 operation

Research Quality: Excellent (9.7/10)
  - Comprehensive coverage of all aspects
  - High-quality sources throughout
  - No unresolved contradictions
  - Actionable insights for healthcare executives
```

---

## GoT Operation Quick Reference

### Decision Tree: Which Operation to Use?

```
                 ┌─────────────────────┐
                 │  Starting Research  │
                 └──────────┬──────────┘
                            │
                   ┌────────┴────────┐
                   │  Generate(k)     │
                   │  k = 3-8         │
                   └────────┬────────┘
                            │
                 ┌──────────┴──────────┐
                 │  Score All Nodes    │
                 └──────────┬──────────┘
                            │
            ┌───────────────┴───────────────┐
            │                               │
    ┌───────┴────────┐            ┌────────┴───────┐
    │ Score ≥ 7.0    │            │ Score < 7.0    │
    │                │            │                │
    │ Diversify:     │            │ Prune:         │
    │ - High: Gen(2) │            │ KeepBestN(3)   │
    │ - Med: Refine  │            │                │
    └───────┬────────┘            └────────┬───────┘
            │                             │
            └──────────┬──────────────────┘
                       │
              ┌────────┴────────┐
              │ 2-3 Rounds of   │
              │ Generate/Score  │
              └────────┬────────┘
                       │
              ┌────────┴────────┐
              │  Aggregate(k)   │
              │ Combine findings│
              └────────┬────────┘
                       │
              ┌────────┴────────┐
              │  Refine(1)      │
              │  Final polish   │
              └────────┬────────┘
                       │
              ┌────────┴────────┐
              │  Final Output   │
              │  Score ≥ 8.5    │
              └─────────────────┘
```

---

## Key Takeaways

1. **No Universal Pattern**: Choose exploration strategy based on research goals
   - Depth-first: Critical topics, technical deep-dives
   - Breadth-first: Trend analysis, landscape surveys
   - Balanced: Most general research topics

2. **Score Guides Strategy**: Let scores determine next actions
   - High scores (8-10): Explore deeper
   - Medium scores (7-8): Refine or aggregate
   - Low scores (<7): Prune

3. **Aggregate at Right Time**: Not too early, not too late
   - Too early: Missing diverse perspectives
   - Too late: Graph becomes unmanageable
   - Sweet spot: After 2-3 generation rounds

4. **Refine Selectively**: Only refine what's already good
   - Threshold: Score ≥ 7.0
   - One refinement usually sufficient
   - Focus on citation quality and clarity

5. **Track Everything**: Maintain clear graph state
   - Nodes, scores, operations, decisions
   - Enables reproducible research
   - Helps explain research choices
