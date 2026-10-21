# Research Executor Skill - Examples

## Example 1: AI in Healthcare Research

### Structured Input
```markdown
### TASK
Analyze the current state and future trends of AI applications in clinical diagnosis and treatment,
with emphasis on market adoption, technology maturity, and implementation considerations for healthcare
executives making adoption decisions.

### CONTEXT/BACKGROUND
Healthcare organizations are evaluating AI tools for clinical diagnosis and treatment. This research
will inform C-suite executives (CEOs, CTOs, CMOs) at hospital systems and healthcare providers who are
considering AI adoption.

### SPECIFIC QUESTIONS OR SUBTASKS
1. Current Market Landscape: What AI clinical applications are currently in production use?
2. Technology Assessment: What is the current accuracy and reliability of AI diagnostic tools?
3. Implementation Considerations: What are the costs and integration challenges?
4. Vendor Landscape: Who are the leading vendors and what are their differentiators?
5. Future Outlook (2025-2028): What technological breakthroughs are expected?
6. Case Studies: What are detailed examples of successful AI clinical implementations?

### KEYWORDS
AI clinical diagnosis, medical AI adoption, healthcare AI market, computer vision medical imaging,
AI diagnostic accuracy, FDA AI medical devices, clinical decision support systems

### CONSTRAINTS
- Timeframe: Emphasis on 2022-present, with projections to 2028
- Geography: Global scope but prioritize US and European markets
- Source Types: Peer-reviewed clinical trials, industry market reports, FDA regulatory documents

### OUTPUT FORMAT
1. Executive Summary (2-3 pages)
2. Full Report (25-30 pages)
3. Decision Support Tools (checklists, ROI framework)
4. Visual Elements (market charts, vendor comparison tables)
```

### Research Executor Response

**Phase 2: Retrieval Planning**
```markdown
## Research Plan

### Subtopics to Research:
1. **Current Market Landscape**
   - Search queries: ["AI clinical diagnosis market size 2024", "AI healthcare adoption rates statistics",
                      "FDA approved AI medical devices list", "clinical AI production deployments 2024"]
   - Target sources: Industry reports (Gartner, McKinsey Healthcare), FDA databases, market research

2. **Technology Assessment**
   - Search queries: ["AI diagnostic accuracy vs human clinicians studies", "computer vision medical imaging benchmarks",
                      "clinical decision support system effectiveness", "AI radiology accuracy meta-analysis"]
   - Target sources: Peer-reviewed journals, clinical validation studies, systematic reviews

3. **Implementation & ROI**
   - Search queries: ["AI clinical implementation costs case study", "healthcare AI ROI analysis",
                      "EHR AI integration challenges", "AI clinical workflow integration"]
   - Target sources: Case studies, vendor whitepapers, healthcare IT publications

4. **Vendor Landscape**
   - Search queries: ["leading AI clinical diagnosis vendors 2024", "medical AI companies comparison",
                      "healthcare AI vendor market share", "AI radiology vendors evaluation"]
   - Target sources: Industry analyst reports, vendor comparison studies, G2/Capterra reviews

5. **Case Studies**
   - Search queries: ["Mayo Clinic AI implementation case study", "Cleveland Clinic AI diagnostic tools",
                      "European hospital AI deployment success stories", "AI clinical implementation failures lessons"]
   - Target sources: Hospital press releases, academic case studies, healthcare conferences

6. **Future Trends**
   - Search queries: ["AI healthcare trends 2025-2028 predictions", "emerging medical AI technologies",
                      "FDA AI regulation roadmap", "AI clinical trials future applications"]
   - Target sources: Industry trend reports, expert forecasts, regulatory roadmaps

### Multi-Agent Deployment Strategy:
- **Phase 3**: Deploy 6 parallel research agents (1 per subtopic)
- **Phase 4**: Deploy 1 cross-reference agent for fact verification
- **Phase 5**: Synthesize findings into comprehensive report

### Output Structure:
```
/datadrive/scratch/stock_research/
└── AI_Clinical_Diagnosis_2024/
    ├── README.md
    ├── executive_summary.md
    ├── full_report.md
    ├── data/
    │   ├── market_statistics.md
    │   └── vendor_comparison.md
    ├── visuals/
    │   └── charts_descriptions.md
    ├── sources/
    │   ├── bibliography.md
    │   └── source_quality_table.md
    ├── research_notes/
    │   └── agent_findings_summary.md
    └── appendices/
        └── methodology.md
```

Ready to proceed with research execution?
```

**Phase 3: Iterative Querying** (Launches 6 parallel subagents)

**Phase 7: Final Output**
```markdown
# AI in Clinical Diagnosis - Research Report

## Executive Summary
[2-3 page summary with key findings and recommendations]

## Full Report
[25-30 page comprehensive analysis with full citations]

## Sources
[Complete bibliography with A-E quality ratings]

## Research Notes
[Detailed findings from each research agent]
```

---

## Pattern Recognition

Across these examples, the Research Executor consistently:

1. **Decomposes complex topics** into 3-7 actionable subtopics
2. **Generates targeted search queries** for each subtopic
3. **Identifies appropriate sources** based on constraints
4. **Creates clear output structure** before research begins
5. **Presents plan for approval** before launching agents
6. **Launches parallel agents** for efficient research
7. **Delivers structured outputs** matching user requirements

### Key Success Factors:

- **Thorough Planning**: Research plans are detailed and specific
- **Source Awareness**: Matches sources to research domain (academic vs industry vs legal)
- **User Communication**: Presents plans clearly and seeks approval
- **Structured Outputs**: Organizes findings in accessible formats
- **Citation Discipline**: Always maintains source traceability
