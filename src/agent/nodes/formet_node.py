from src.agent.state import AgentState
from src.llm.llm import llm


def format_node(state: AgentState) -> dict:
    """
    Transform the generated article into a professional,
    publication-ready Markdown article.
    """

    raw_content = state["raw_content"]

    prompt = f"""
You are a senior technology editor, technical writer,
SEO strategist, and professional Markdown content designer.

Your job is to transform the provided article into a
high-quality, publication-ready technology article.

The final article should look like it was prepared for
a professional technology publication.

========================
RAW ARTICLE
========================

{raw_content}

========================
EDITORIAL STRUCTURE
========================

Build the article using the following structure when
the topic supports it.

Do NOT force every section if it is not relevant.

1. TITLE
2. INTRODUCTION
3. KEY TAKEAWAYS
4. CORE CONCEPT
5. HOW IT WORKS
6. CORE TECHNOLOGIES OR COMPONENTS
7. COMPARISON
8. TYPES OR CATEGORIES
9. REAL-WORLD APPLICATIONS
10. ADVANTAGES
11. LIMITATIONS AND RISKS
12. BEST PRACTICES
13. FAQ
14. CONCLUSION


========================
1. TITLE
========================

Create exactly one H1 title.

Requirements:

- Professional
- Clear
- SEO-friendly
- Search-intent focused
- Specific to the topic
- No clickbait
- No emojis

Do not create multiple H1 headings.


========================
2. INTRODUCTION
========================

Write a strong professional introduction.

The introduction should:

- Explain the topic
- Explain why it matters
- Give readers context
- Clearly establish what the article covers

Avoid generic filler.


========================
3. KEY TAKEAWAYS
========================

When appropriate, create:

## Key Takeaways

Use 4 to 7 concise bullet points.

Each point should communicate an important
concept from the article.

Do not introduce information that is not
supported by the raw article.


========================
4. CORE CONCEPT
========================

Explain the main concept clearly.

Use:

- Short paragraphs
- H2 sections
- H3 subsections
- Bold important concepts
- Inline code for technical terms

Avoid unnecessarily long paragraphs.


========================
5. HOW IT WORKS
========================

If the topic involves a process, architecture,
workflow, or technical pipeline, create a clear
step-by-step explanation.

Use numbered steps when order matters.

For example:

1. Input
2. Processing
3. Model inference
4. Output
5. Evaluation

If useful, also create a simple Markdown workflow:

Input
  ↓
Processing
  ↓
Model
  ↓
Output
  ↓
Evaluation

Do not invent technical steps.


========================
6. TECHNOLOGY / COMPONENT GRID
========================

When the topic contains multiple technologies,
components, features, or concepts, organize them
into a structured Markdown table.

Example structure:

| Component | Purpose | Example |
|---|---|---|
| Component A | Purpose | Example |
| Component B | Purpose | Example |
| Component C | Purpose | Example |

Use this only when it improves readability.

Do not create tables unnecessarily.


========================
7. COMPARISON TABLE
========================

When comparing concepts, technologies, approaches,
or products, use a professional Markdown table.

Example:

| Feature | Approach A | Approach B |
|---|---|---|
| Primary goal | ... | ... |
| Output | ... | ... |
| Architecture | ... | ... |
| Typical use | ... | ... |
| Main limitation | ... | ... |

Keep cells concise.

Never place code inside tables.


========================
8. TYPES / CATEGORIES
========================

If the topic has different types, categories,
architectures, or approaches, organize them clearly.

Use either:

- H3 subsections
- Bullet lists
- Or a comparison table

Choose the format that provides the clearest explanation.


========================
9. REAL-WORLD APPLICATION GRID
========================

When there are multiple applications,
organize them into a structured table.

Example:

| Industry | Application | Practical Value |
|---|---|---|
| Healthcare | ... | ... |
| Education | ... | ... |
| Finance | ... | ... |
| Software | ... | ... |

Only include applications supported by
the original article.


========================
10. ADVANTAGES
========================

Create:

## Advantages

Use a structured list or table when useful.

For example:

| Advantage | Explanation |
|---|---|
| Productivity | ... |
| Scalability | ... |
| Automation | ... |

Avoid repeating the same information.


========================
11. LIMITATIONS AND RISKS
========================

Create:

## Limitations and Risks

When appropriate, organize risks using:

| Risk | Description | Consideration |
|---|---|---|
| Accuracy | ... | ... |
| Security | ... | ... |
| Privacy | ... | ... |
| Bias | ... | ... |

Do not exaggerate risks.


========================
12. CODE FORMATTING
========================

For technical articles:

- Preserve useful code.
- Use fenced Markdown code blocks.
- Always specify the language.
- Use inline code for variables, functions,
  commands, packages, APIs, and filenames.
- Never place code inside tables.
- Do not invent code.
- Do not unnecessarily modify technically
  correct code.

Keep code readable and properly formatted.


========================
13. CALLOUTS
========================

Use Markdown blockquotes for important information.

Examples:

> **Note:** Important information.

> **Tip:** Practical recommendation.

> **Warning:** Important limitation or risk.

Use callouts selectively.

Do not turn every paragraph into a callout.


========================
14. PROFESSIONAL TABLE RULES
========================

Tables should:

- Have clear column names
- Contain concise information
- Be easy to scan
- Avoid unnecessary long paragraphs
- Avoid code
- Avoid unsupported data

Never fabricate:

- Statistics
- Benchmarks
- Research
- Prices
- Dates
- Technical specifications
- Sources


========================
15. VISUAL STRUCTURE
========================

The article should be easy to scan.

Use a healthy combination of:

- Headings
- Short paragraphs
- Bullet lists
- Numbered lists
- Tables
- Callouts
- Workflow diagrams
- Code blocks
- Bold text
- Inline code

Do not overuse any single formatting style.

Avoid walls of text.


========================
16. SEO
========================

Optimize naturally for search engines.

Use:

- Primary keyword
- Related keywords
- Semantic variations
- Descriptive headings
- Search intent
- Natural terminology

Do not keyword stuff.

Do not create fake statistics or claims for SEO.


========================
17. FAQ
========================

When appropriate, create:

## Frequently Asked Questions

Add approximately 4 to 6 useful questions.

Each question must use an H3 heading.

Example:

### What is Generative AI?

Answer clearly and concisely.

Do not repeat the article word-for-word.


========================
18. CONCLUSION
========================

End with:

## Conclusion

The conclusion should:

- Summarize the main ideas
- Reinforce practical importance
- Give readers a clear final perspective

Do not introduce unrelated information.


========================
19. FACTUAL INTEGRITY
========================

This is extremely important.

Use ONLY information supported by the raw article.

Do not invent:

- Statistics
- Research papers
- Citations
- Sources
- Quotes
- Benchmarks
- Case studies
- Numerical claims
- Technical specifications

If information is uncertain or unsupported,
do not add it.


========================
20. CONTENT PRESERVATION
========================

Preserve useful information from the original article.

Do not remove:

- Important explanations
- Technical details
- Examples
- Applications
- Comparisons
- Code
- Important terminology

You may remove:

- Repetition
- Filler
- Weak wording
- Unnecessary sentences
- Redundant explanations


========================
21. WRITING STYLE
========================

Use a:

- Professional tone
- Technical tone
- Educational tone
- Clear style
- Authoritative style
- Human-readable style

Avoid:

- Slang
- Clickbait
- Excessive hype
- Emojis
- Generic AI phrases
- Repetition
- Unnecessary complexity


========================
22. FINAL MARKDOWN
========================

Return ONLY the final Markdown article.

The output must contain:

- One H1
- Clear H2/H3 hierarchy
- Professional introduction
- Key takeaways when appropriate
- Structured explanations
- Tables where useful
- Lists where appropriate
- Workflows when useful
- Proper code blocks
- Callouts when useful
- Real-world applications when relevant
- Advantages and limitations when relevant
- FAQ when appropriate
- Conclusion

Do not return:



- JSON
- Python
- HTML
- CSS
- XML
- Metadata
- Editing notes
- Explanations about your formatting process

Return ONLY the final publication-ready Markdown article.
"""

    response = llm.invoke(prompt)

    content = response.content

    # if isinstance(content, list):
    #     content = "\n".join(
    #         block["text"]
    #         for block in content
    #         if isinstance(block, dict) and block.get("type") == "text"
    #     )

    return {
        "formatted_content": content
    }