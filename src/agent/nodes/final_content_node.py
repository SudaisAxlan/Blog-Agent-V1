from src.agent.state import AgentState
from src.llm.llm import llm


def final_content_node(state: AgentState) -> dict:
    """
    Perform the final editorial quality check and
    produce the final publication-ready blog.
    """

    user_title = state["user_title"]
    formatted_content = state["formatted_content"]

    prompt = f"""
You are the final senior editor for a professional
technology publication.

Review and finalize the article below.

ORIGINAL TITLE:
{user_title}

FORMATTED ARTICLE:
{formatted_content}

FINAL REVIEW:

1. Preserve the original topic and technical meaning.

2. Improve:
   - clarity
   - readability
   - grammar
   - sentence quality
   - logical flow
   - consistency
   - professional tone

3. Remove:
   - unnecessary repetition
   - filler
   - weak statements
   - irrelevant content
   - unsupported claims

4. Verify that the article has:
   - one H1 title
   - logical H2/H3 sections
   - a strong introduction
   - useful technical explanations
   - appropriate tables and lists
   - correctly formatted code blocks
   - a useful FAQ when appropriate
   - a clear conclusion

5. Review SEO naturally:
   - title should match search intent
   - headings should be descriptive
   - terminology should be relevant
   - avoid keyword stuffing

6. Do not invent:
   - statistics
   - research
   - citations
   - sources
   - quotes
   - benchmarks
   - technical specifications
   - numerical values

7. Preserve useful Markdown formatting from the formatted article.

8. Do not unnecessarily rewrite technically correct code.

9. Maintain a professional technology-publication style.

10. Return ONLY the final Markdown article.

Do not explain your changes.
Do not mention this review process.
Do not return JSON.
Do not return HTML.
Do not return Python outside code blocks.
Do not mention AI.

Return ONLY the final publication-ready Markdown article.
"""

    response = llm.invoke(prompt)

    return {
        "final_content": response.content
    }