from src.agent.graph import blog_agent


question = input("Write the article topic: ")

agent = blog_agent.invoke({
    "user_title": question
})

print(agent["final_content"])