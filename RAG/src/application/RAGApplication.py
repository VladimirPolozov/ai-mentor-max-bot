from RAG.src.application.use_cases.BuildVectorStoreUseCase import BuildVectorStoreUseCase
from RAG.src.application.use_cases.QueryLLMUseCase import QueryLLMUseCase
from RAG.src.core.entities import QueryRequest, LLMResponse
from RAG.src.infrastructure.file_reader.FileReader import FileReader
from RAG.src.infrastructure.llm.DeepSeekLLM import DeepSeekLLM
from RAG.src.infrastructure.vector_store.ChromaVectorStore import ChromaVectorStore
from config import Config


class RAGApplication:
    def __init__(self, config: Config):
        self.config = config

        self.file_reader = FileReader()
        self.vector_store = ChromaVectorStore(
            persist_directory=config.VECTOR_STORE_PATH
        )
        self.llm_provider = DeepSeekLLM(
            api_key=config.OPENAI_API_KEY,
            base_url=config.DEEPSEEK_BASE_URL
        )

        self.build_vector_store_uc = BuildVectorStoreUseCase(
            self.file_reader, self.vector_store
        )
        self.query_llm_uc = QueryLLMUseCase(
            self.vector_store, self.llm_provider
        )

    def build_vector_store(self) -> int:
        """Построение векторной базы данных из txt файлов"""
        print(f"Building vector store from {self.config.DATA_DIRECTORY}...")
        document_count = self.build_vector_store_uc.execute(self.config.DATA_DIRECTORY)
        print(f"Vector store built successfully! Processed {document_count} documents.")
        return document_count

    async def query(self, query_request: QueryRequest) -> LLMResponse:
        """Запрос к LLM с RAG"""
        print(f"Processing query: {query_request.question}")
        response = await self.query_llm_uc.execute(query_request)

        print(f"\nResponse ({response.total_tokens} tokens):")
        print("=" * 50)
        print(response.content)
        print("=" * 50)

        return response