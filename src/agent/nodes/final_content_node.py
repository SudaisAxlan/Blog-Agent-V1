from src.agent.state import AgentState
from src.llm.llm import llm


def final_content_node(state: AgentState) -> dict:
    """
    Perform the final editorial review and produce
    a polished, publication-ready technology article.
    """

    user_title = state["user_title"]
    formatted_content = state["formatted_content"]

    prompt = f"""
You are a senior editor at a professional technology
and artificial intelligence publication.

Your task is to perform the FINAL editorial pass on
the article below.

The article has already been researched, written,
and professionally formatted.

Your job is NOT to create a completely new article.

Your job is to polish, improve, verify, and finalize
the existing article so it looks professionally
written and ready for publication.

========================
ORIGINAL TOPIC
========================

{user_title}

========================
FORMATTED ARTICLE
========================

{formatted_content}

========================
FINAL EDITORIAL REVIEW
========================

1. CONTENT PRESERVATION

Preserve the original meaning and useful information.

Do not remove important:

- Technical explanations
- Examples
- Applications
- Comparisons
- Code
- Tables
- Workflows
- Best practices
- FAQs

Only remove information when it is:

- Repetitive
- Irrelevant
- Filler
- Contradictory
- Clearly unsupported


2. PROFESSIONAL WRITING

Improve the writing so it sounds like a professional
technology publication.

Improve:

- Grammar
- Sentence structure
- Word choice
- Clarity
- Readability
- Transitions
- Professional tone
- Technical precision

Avoid:

- Slang
- Casual language
- Excessive hype
- Clickbait
- Repetitive statements
- Generic filler
- Unnecessary complexity


3. TITLE

Review the existing H1 title.

Make sure it is:

- Clear
- Professional
- Specific
- SEO-friendly
- Relevant to the search intent

Use exactly ONE H1 title.

Do not unnecessarily change a strong existing title.


4. INTRODUCTION

Review the introduction.

It should:

- Clearly explain the topic
- Explain why the topic matters
- Establish context
- Tell readers what they will learn

Make it engaging but professional.

Avoid generic openings.


5. STRUCTURE

Review the complete article structure.

Ensure the hierarchy is logical:

# H1
## H2
### H3

Do not create unnecessary headings.

Make sure sections appear in a logical order.


6. READABILITY

Improve readability by:

- Breaking long paragraphs
- Removing repetition
- Improving transitions
- Using concise sentences
- Highlighting important concepts
- Keeping related information together

Avoid turning the entire article into bullet points.


7. TABLES

Review every table.

Keep tables when they genuinely improve understanding.

Make sure:

- Headers are clear
- Information is accurate
- Cells are concise
- Formatting is consistent
- No unnecessary information is included

Do not place code inside tables.

Do not invent table information.


8. LISTS

Review bullet and numbered lists.

Use bullet lists for:

- Features
- Benefits
- Applications
- Key points
- Advantages
- Limitations
- Best practices

Use numbered lists for:

- Procedures
- Tutorials
- Sequential processes
- Workflows

Do not overuse lists.


9. WORKFLOWS

If the article contains a workflow or process,
make sure it is easy to understand.

Use a simple Markdown representation when useful.

For example:

Input
  ↓
Processing
  ↓
Model
  ↓
Output

Do not invent technical steps.


10. CODE

Review technical code carefully.

Preserve technically correct code.

Do not:

- Invent code
- Change working code unnecessarily
- Remove important code
- Put code inside tables

Use proper Markdown fenced code blocks.

Always specify the programming language.

Use inline code for:

- Variables
- Functions
- Commands
- Packages
- APIs
- Classes
- File names


11. CALLOUTS

Keep useful callouts such as:

> **Note:** ...

> **Tip:** ...

> **Warning:** ...

Remove unnecessary callouts.

Do not overuse them.


12. SEO POLISH

Improve SEO naturally.

Check:

- H1 title
- H2/H3 headings
- Keyword usage
- Search intent
- Semantic terminology
- Topic relevance

Use keywords naturally.

Never keyword stuff.

Do not add unsupported claims just for SEO.


13. FACTUAL ACCURACY

This is critical.

Do not invent:

- Statistics
- Research
- Sources
- Citations
- Quotes
- Benchmarks
- Case studies
- Prices
- Dates
- Technical specifications
- Numerical claims

If the article does not provide evidence
for a claim, do not create evidence.

Preserve existing sources and references
if they are already present.


14. TECHNICAL ACCURACY

Make sure technical terminology is used consistently.

When an abbreviation is introduced:

Full Term (ABBREVIATION)

Then use the abbreviation consistently.

Do not change the technical meaning of the article.


15. KEY TAKEAWAYS

If the article already has a Key Takeaways section,
polish it.

It should contain concise and useful points.

Do not repeat the entire article.


16. REAL-WORLD APPLICATIONS

If present, make sure applications are:

- Practical
- Clear
- Relevant
- Easy to understand

Do not add unsupported applications.


17. ADVANTAGES AND LIMITATIONS

Make sure advantages and limitations are balanced.

Avoid marketing language.

Explain realistic benefits and trade-offs.


18. BEST PRACTICES

Make best practices:

- Practical
- Specific
- Actionable
- Relevant to the topic

Avoid generic advice whenever possible.


19. FAQ

Review the FAQ section.

Keep approximately 4 to 6 useful questions
when appropriate.

Questions should address realistic reader concerns.

Answers should be concise and informative.

Do not repeat the article word-for-word.


20. CONCLUSION

Polish the conclusion.

It should:

- Summarize the article
- Reinforce the main ideas
- Explain practical importance
- End with a strong final perspective

Do not introduce unrelated information.


========================
FINAL QUALITY CHECK
========================

Before returning the article, verify:

- Exactly one H1 exists.
- Heading hierarchy is correct.
- Introduction is strong.
- Sections flow logically.
- Paragraphs are readable.
- Tables are useful.
- Lists are appropriate.
- Workflows are clear.
- Code formatting is correct.
- Code meaning is preserved.
- Callouts are used appropriately.
- Terminology is consistent.
- SEO is natural.
- No unsupported information was added.
- Repetition is minimized.
- FAQ is useful when appropriate.
- Conclusion is present.
- Overall writing sounds professional.


========================
OUTPUT RULES
========================

Return ONLY the final polished Markdown article.

Do not explain your edits.

Do not mention the editing process.

Do not mention these instructions.

Do not return JSON.

Do not return HTML.

Do not return Python outside Markdown code blocks.

Do not add metadata.

Do not add commentary before or after the article.

Return ONLY the final publication-ready Markdown article.
"""

    response = llm.invoke(prompt)

    content = response.content

    # Gemini can sometimes return structured content blocks.
    if isinstance(content, list):
        content = "\n".join(
            block["text"]
            for block in content
            if isinstance(block, dict) and block.get("type") == "text"
        )

    return {
        "final_content": content
    }