# Citation Validator Skill - Examples

## Example 1: Validating AI Market Research Report

### Input Content
```markdown
# AI in Healthcare Market Report

The global AI in healthcare market reached $22.4 billion in 2023 and is projected
to grow at a CAGR of 37.5% through 2030 (Grand View Research, 2024).

Major hospitals using AI include Mayo Clinic, which reports 40% faster diagnoses
with their AI imaging tools (Mayo Clinic, 2024).

According to industry studies, AI diagnostic tools achieve 95% accuracy compared
to human radiologists (Smith et al., 2023).

The FDA has approved over 500 AI medical devices as of 2024 (FDA, 2024).
```

### Validation Report

```markdown
# Citation Validation Report

## Executive Summary
- **Total Claims Analyzed**: 4
- **Claims with Citations**: 4 (100%)
- **Complete Citations**: 2 (50%)
- **Accurate Citations**: 3 (75%)
- **Potential Hallucinations**: 1
- **Overall Quality Score**: 5.5/10

## Critical Issues (Immediate Action Required)

### ⚠ HALLUCINATION DETECTED
**Claim**: "The FDA has approved over 500 AI medical devices as of 2024"
**Citation**: (FDA, 2024)
**Issue**: Number is incorrect
**Verification**:
- FDA database shows: 692 AI/ML-enabled medical devices (as of Dec 2024)
- Claim says "over 500" which is technically correct but understated
- More accurate figure: 692 devices
**Correction Required**: Update to "692 AI/ML-enabled medical devices" with source

## Citation Completeness Issues

### Claim 1: AI market size and growth
**Claim**: "The global AI in healthcare market reached $22.4 billion in 2023..."
**Citation**: (Grand View Research, 2024)
**Completeness**: ✗ INCOMPLETE
**Missing**:
- Full report title
- URL/DOI to verify
- Page numbers
**Recommended Format**:
```
(Grand View Research, 2024, "AI in Healthcare Market Size, Share & Trends")
Full: Grand View Research. (2024). "Artificial Intelligence in Healthcare Market
Size, Share & Trends Analysis Report." Retrieved [date] from [URL]
```

### Claim 3: AI diagnostic accuracy
**Claim**: "AI diagnostic tools achieve 95% accuracy compared to human radiologists"
**Citation**: (Smith et al., 2023)
**Completeness**: ✗ INCOMPLETE
**Missing**:
- Full paper title
- Journal name
- DOI
- Specific study details (sample size, conditions)
**Investigation Needed**: "Smith et al." is too generic - need to identify actual paper

## Source Quality Assessment

| Citation | Type | Rating | Justification |
|----------|------|--------|---------------|
| Grand View Research (2024) | Industry Report | B | Reputable market research firm, but verify with additional sources |
| Mayo Clinic (2024) | Organizational | C | Self-reported data, potential bias, verify with independent studies |
| Smith et al. (2023) | Academic (?) | D | Incomplete citation, cannot verify quality until full details found |
| FDA (2024) | Government | A | Official FDA database, highest quality |

## Detailed Findings

### Claim 1: Market size $22.4B, CAGR 37.5%
**Citation**: (Grand View Research, 2024)
**Verification Status**: ✓ ACCURATE
**Source Check**: Grand View Research "AI in Healthcare Market" report exists
**Figure Verification**: $22.4B for 2023 ✓
**Growth Rate**: 37.5% CAGR ✓
**Recommendation**: Add second source to corroborate (e.g., MarketsandMarkets or Fortune Business Insights)

### Claim 2: Mayo Clinic 40% faster diagnoses
**Citation**: (Mayo Clinic, 2024)
**Verification Status**: ⚠ NEEDS VERIFICATION
**Source Check**: Found Mayo Clinic press release about AI imaging
**Claim Verification**: 40% figure needs specific source
**Bias Warning**: This is self-reported data
**Recommendation**: Find independent study validating Mayo Clinic's claims or present as "self-reported"

### Claim 3: 95% diagnostic accuracy
**Citation**: (Smith et al., 2023)
**Verification Status**: ✗ CANNOT VERIFY
**Issue**: Citation too generic to locate specific paper
**Search Attempted**: "Smith AI diagnostic accuracy 2023" → Multiple results, unclear which
**Action Required**: Find actual paper or remove claim
**Potential Matches** (need verification):
- Smith, A. et al. (2023). "Deep Learning for Medical Image Analysis." Nature.
- Smith, J. et al. (2023). "AI in Radiology: A Comprehensive Review." Lancet Digital Health.

### Claim 4: FDA approved 500+ AI devices
**Citation**: (FDA, 2024)
**Verification Status**: ⚠ INACCURATE NUMBER
**Actual Data**: FDA database shows 692 AI/ML-enabled medical devices (as of Dec 2024)
**Source**: FDA AI/ML-Based Medical Device Database
**Correction**: Update to "692 devices" or "nearly 700 devices"

## Recommendations (Prioritized)

### HIGH PRIORITY
1. **Fix FDA device count**: Update from 500+ to 692 with specific database link
2. **Verify Smith et al. citation**: Find complete citation or replace with verifiable source
3. **Add URL for Grand View Research**: Include direct link to report

### MEDIUM PRIORITY
4. **Corroborate market size data**: Add second source (e.g., Fortune Business Insights)
5. **Verify Mayo Clinic claim**: Find independent source or label as self-reported
6. **Add publication details for all sources**: Include full titles and URLs

### LOW PRIORITY
7. **Standardize citation format**: Use consistent format throughout document
8. **Add access dates**: For all web sources

## Corrected Bibliography

```markdown
Grand View Research. (2024). "Artificial Intelligence in Healthcare Market Size, Share &
Trends Analysis Report, 2024-2030." Retrieved December 2024 from https://www.grandviewresearch.com/
industry-analysis/artificial-intelligence-in-healthcare-market

Mayo Clinic. (2024). "AI-Powered Medical Imaging: Diagnostic Improvements." Mayo Clinic
Press Release. Retrieved December 2024 from [URL - NEEDED]
Note: Self-reported data, independent verification recommended.

[INCOMPLETE - NEEDS FULL CITATION]: Smith et al. (2023).
Action: Locate complete citation or replace with verifiable source.

U.S. Food and Drug Administration. (2024). "Artificial Intelligence and Machine Learning
(AI/ML)-Enabled Medical Devices." FDA Database. Retrieved December 2024 from
https://www.fda.gov/medical-devices/software-medical-device-samd/artificial-intelligence-and-machine-learning-aiml-enabled-medical-devices
```

## Quality Score Breakdown

- Citation Coverage: 3/3 = 100% (3 points)
- Citation Completeness: 2/4 = 50% (1 point)
- Citation Accuracy: 3/4 = 75% (2.25 points)
- Source Quality: Average rating = (B+C+D+A)/4 = (2+1.5+1+3)/4 = 1.875 (1.88 points)
- Hallucination Penalty: -1 (for inaccurate FDA figure)

**Total Score**: 3 + 1 + 2.25 + 1.88 - 1 = **6.13/10**

**Assessment**: FAIR - Significant citation quality issues that undermine credibility.
```

---

## Common Citation Patterns

### Pattern 1: Progressive Improvement
```
Draft 1: "Studies show AI is growing fast."
Draft 2: "AI market growing 37% annually (Research, 2024)."
Draft 3: "AI in healthcare growing 37.5% CAGR through 2030 (Grand View Research, 2024)."
Draft 4: "AI in healthcare market: $22.4B in 2023, 37.5% CAGR to 2030 (Grand View Research, 2024; corroborated by MarketsandMarkets, 2024)."
```

### Pattern 2: Source Quality Ladder
```
Level E: "People say..."
Level D: "According to a blog post..."
Level C: "TechCrunch reported..."
Level B: "According to Gartner research..."
Level A: "A peer-reviewed study in Nature (Smith et al., 2023) demonstrated..."
```

### Pattern 3: Claim Strength Scaling
```
Speculative: "May", "might", "could", "potentially"
Likely: "Likely", "probably", "appears to"
Certain: "Shows", "demonstrates", "proves" (requires strongest sources)
```

---

## Key Takeaways

1. **Always Verify**: Never assume a citation is correct without checking
2. **Be Specific**: "Smith et al." is not enough - need full details
3. **Check Context**: Does the source actually support the specific claim?
4. **Rate Quality**: Not all sources are equal - use A-E ratings
5. **Detect Patterns**: Multiple issues suggest systemic problems
6. **Provide Fixes**: Don't just identify problems - suggest solutions
7. **Chain-of-Verification**: For critical claims, use multiple sources
