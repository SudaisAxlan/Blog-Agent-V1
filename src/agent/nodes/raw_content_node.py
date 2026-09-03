from src.agent.state import AgentState
from src.llm.llm import llm


def raw_content_node(state: AgentState) -> dict:
    user_title = state["user_title"]
    google_search = state["google_search"]

    prompt = f"""
You are a professional AI technology writer and research analyst.

Your task is to create a deeply researched, publication-ready blog article.

ARTICLE TITLE:
{user_title}

RESEARCH DATA:
{google_search}

INSTRUCTIONS:

1. Analyze the provided research carefully.
2. Create a strong, SEO-friendly title.
3. Write a compelling introduction.
4. Explain the topic deeply and accurately.
5. Use clear H2 and H3 sections.
6. Include practical examples where relevant.
7. Include comparison tables when they improve understanding.
8. Include bullet points and numbered lists where appropriate.
9. Explain technical concepts in simple but professional language.
10. Include real-world applications and use cases.
11. Discuss advantages and limitations.
12. Include important considerations, challenges, and best practices.
13. Include relevant statistics or facts only when supported by the research.
14. Do not invent sources, statistics, facts, or quotations.
15. Avoid unnecessary repetition.
16. Maintain a professional, authoritative tone.
17. Optimize naturally for search engines without keyword stuffing.
18. Make the article useful to both beginners and technical readers.
19. Use Markdown formatting.
20. End with a concise conclusion.
21. Add a FAQ section containing relevant questions and answers.

IMPORTANT:
- Use the research data as the factual foundation.
- Do not fabricate information.
- Do not mention that you are an AI.
- Do not describe your writing process.
- Return only the completed article.

Generate the complete article now.
"""

    response = llm.invoke(prompt)

    return {
        "raw_content": response.content,
    }