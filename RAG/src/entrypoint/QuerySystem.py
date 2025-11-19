import sys
import os

from RAG.src.application.RAGApplication import RAGApplication
from RAG.src.core.entities import QueryRequest, LLMResponse

sys.path.append(os.path.dirname(os.path.dirname(__file__)))


from config import Config




class QuerySystem:
    def __init__(self):
        self.rag_app = RAGApplication(Config())
        existing_docs = self.rag_app.vector_store.get_all_documents()

        if not existing_docs:
            print("No documents found in vector store. Building...")
            self.rag_app.build_vector_store()
        else:
            print(f"Found documents in vector store.")

        print("\nRAG System Ready!")

    async def query(self, query_request: QueryRequest) -> LLMResponse | None:
        try:
            if query_request.question:
                llm_response = self.rag_app.query(query_request)
                return await llm_response

        except Exception as e:
            print(f"Error: {str(e)}")

if __name__ == "__main__":
    query_system = QuerySystem()
    query_system.query(QueryRequest("Подскажите, а где находится дирекция?"))