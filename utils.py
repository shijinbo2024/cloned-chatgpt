from langchain.chains import ConversationChain
from langchain_openai import ChatOpenAI

import os
from langchain.memory import ConversationBufferMemory


def get_chat_response(prompt, memory, openai_api_key):
    # model = ChatOpenAI(model="dall-e-3", 
    #                    openai_api_key="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",
    #                    base_url="https://api.aigc369.com/v1")
    model = ChatOpenAI(model="gpt-4-0125-preview", 
                       openai_api_key="sk-eIxdgzUkkdfvcLSYD9306822213945Bf859f2cB63d3c5d18",
                       base_url="https://api.aigc369.com/v1")
    chain = ConversationChain(llm=model, memory=memory)

    response = chain.invoke({"input": prompt})
    return response["response"]


memory = ConversationBufferMemory(return_messages=True)
# print(get_chat_response("牛顿提出过哪些知名的定律？", memory, os.getenv("OPENAI_API_KEY")))
# print(get_chat_response("我上一个问题是什么？", memory, os.getenv("OPENAI_API_KEY")))
