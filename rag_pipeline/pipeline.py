from typing import List


class RAGPipeline:
    def __init__(self):
        pass

    def run(self, user_input: str) -> str:
        raise NotImplementedError

    def get_relevant_documents(self, adjusted_user_input: str):
        raise NotImplementedError

    def adjust_user_question(self, user_input: str):
        raise NotImplementedError

    def get_answer_from_llm(self, user_input: str, relevant_docs: List[str]):
        raise NotImplementedError
