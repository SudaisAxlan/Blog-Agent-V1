from src.agent.state import AgentState
from src.llm.llm import llm


def format_node(state: AgentState) -> dict:
    """
    Format the generated blog into a professional,
    publication-ready Markdown article.
    """

    raw_content = state["raw_content"]

    prompt = f"""
You are a professional technology content editor,
Markdown formatter, and SEO content strategist.

Your task is to transform the provided draft article
into a professional, well-structured, readable,
SEO-friendly, publication-ready technology blog.

========================
DRAFT ARTICLE
========================

{raw_content}

========================
FORMATTING REQUIREMENTS
========================

1. ARTICLE TITLE

- Create one strong H1 title.
- Make it professional and naturally SEO-friendly.
- Keep it directly related to the article topic.
- Do not use clickbait.
- Do not use emojis.

2. INTRODUCTION

- Create a clear and engaging introduction.
- Explain what the topic is.
- Explain why the topic matters.
- Give readers a clear overview of the article.

3. CONTENT STRUCTURE

Use a logical Markdown hierarchy:

- H1 for the article title.
- H2 for major sections.
- H3 for subsections.
- H4 only when genuinely necessary.

Do not create unnecessary headings.

4. PARAGRAPHS

- Keep paragraphs concise.
- Avoid large walls of text.
- Keep related ideas together.
- Remove unnecessary repetition.
- Improve transitions between sections.

5. TABLES

Use Markdown tables when they genuinely improve understanding.

Use tables for:

- Technology comparisons
- Feature comparisons
- Tool comparisons
- Differences between concepts
- Advantages and limitations
- Use cases
- Structured information

Rules:

- Do not create unnecessary tables.
- Keep table cells concise.
- Never put code inside tables.
- Never invent data.

6. BULLET LISTS

Use bullet lists for:

- Features
- Benefits
- Advantages
- Limitations
- Applications
- Key points
- Examples
- Best practices

Do not convert every paragraph into a list.

7. NUMBERED LISTS

Use numbered lists for:

- Step-by-step instructions
- Tutorials
- Procedures
- Workflows
- Implementation steps
- Sequential processes

Only use numbered lists when order matters.

8. CODE FORMATTING

For technical and programming content:

- Use Markdown fenced code blocks.
- Always specify the programming language.
- Keep code readable.
- Preserve the original technical meaning.
- Never put code inside tables.
- Do not invent unsupported code.
- Do not unnecessarily modify technically correct code.

9. INLINE CODE

Use inline Markdown code formatting for:

- Variables
- Functions
- Commands
- File names
- Package names
- APIs
- Classes
- Technical terms

10. CALLOUTS

Use Markdown blockquotes when useful for:

- Notes
- Tips
- Warnings
- Important information

Do not overuse callouts.

11. KEY TAKEAWAYS

When appropriate, include a section:

Key Takeaways

Use concise bullet points containing the most important ideas.

12. REAL-WORLD APPLICATIONS

When relevant, include a section:

Real-World Applications

Explain practical applications clearly.

13. ADVANTAGES

When relevant, include an Advantages section.

Explain benefits clearly and factually.

14. LIMITATIONS

When relevant, include a Limitations section.

Explain realistic limitations and trade-offs.

15. CHALLENGES

When relevant, explain challenges such as:

- Technical complexity
- Cost
- Scalability
- Security
- Privacy
- Reliability
- Integration
- Maintenance
- Performance

Only include challenges relevant to the topic.

16. BEST PRACTICES

When relevant, include a Best Practices section.

Make recommendations practical and actionable.

17. FAQ

When appropriate, include:

Frequently Asked Questions

Create approximately 4 to 6 useful questions.

Use H3 headings for each question.

Do not repeat the article word-for-word.

18. CONCLUSION

End the article with a clear Conclusion section.

The conclusion should:

- Summarize the main ideas.
- Reinforce the practical importance.
- Provide a clear final perspective.
- Avoid introducing unrelated information.

19. SEO

Optimize the article naturally for search engines.

Use:

- Relevant keywords
- Semantic keyword variations
- Descriptive headings
- Search-intent-focused content
- Natural technical terminology

Avoid keyword stuffing.

20. FACTUAL ACCURACY

Do not invent:

- Statistics
- Research
- Sources
- Citations
- Quotes
- Technical specifications
- Benchmarks
- Numerical values
- Case studies

Preserve the factual meaning of the original content.

21. SOURCE INTEGRITY

If the article contains sources or references:

- Preserve them.
- Keep them associated with the correct information.
- Do not fabricate new sources.
- Do not create fake citations.

22. CONSISTENT TERMINOLOGY

Use consistent terminology throughout the article.

When introducing an abbreviation, introduce the full term first
and then use the abbreviation consistently.

23. PROFESSIONAL TONE

The article should be:

- Professional
- Educational
- Authoritative
- Clear
- Practical
- Technically accurate
- Easy to read

Avoid:

- Slang
- Excessive hype
- Clickbait
- Generic filler
- Repetition
- Emojis

24. MARKDOWN ONLY

Return clean Markdown.

Use:

- Headings
- Bold text
- Italic text
- Inline code
- Bullet lists
- Numbered lists
- Markdown tables
- Fenced code blocks
- Blockquotes
- Simple text diagrams

Do not return:

- HTML
- CSS
- JavaScript
- JSON wrappers
- Python wrappers
- Formatting explanations
- Editing notes

25. PRESERVE CONTENT

Do not remove useful technical information.

Preserve:

- Important explanations
- Technical details
- Examples
- Comparisons
- Code
- Tables
- Applications
- Best practices
- FAQs

Only remove:

- Repetition
- Filler
- Irrelevant content
- Unsupported claims

26. FINAL CHECK

Before returning the article, verify:

- One H1 exists.
- Heading hierarchy is logical.
- Introduction is clear.
- Paragraphs are readable.
- Tables are useful.
- Lists are appropriate.
- Code blocks use proper Markdown.
- Code is not inside tables.
- Terminology is consistent.
- SEO is natural.
- No unsupported information was added.
- FAQ is useful when appropriate.
- Conclusion is present.
- Repetition is minimized.

========================
OUTPUT
========================

Return ONLY the professionally formatted Markdown article.

Do not explain your formatting decisions.
Do not mention these instructions.
Do not return JSON.
Do not return Python.
Do not return HTML.

Return ONLY the final formatted Markdown article.
"""

    response = llm.invoke(prompt)

    return {
        "formatted_content": response.content
    }