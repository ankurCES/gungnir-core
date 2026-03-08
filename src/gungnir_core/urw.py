import os
from typing import List, Optional
from langchain_openai import AzureChatOpenAI, ChatOpenAI
from langchain_community.llms import Ollama
from langchain_core.messages import BaseMessage

class UniversalReasoningWrapper:
    """
    Universal Reasoning Wrapper (URW) - Tesla's Mandate.
    Standardized abstraction for Multi-Realm Reasoning (Edge, Cloud, Enterprise).
    """
    def __init__(self, realm: Optional[str] = None):
        self.realm = realm or os.getenv("GUNGNIR_REASONING_REALM", "local").lower()
        self.model = self._initialize_model()

    def _initialize_model(self):
        if self.realm == "enterprise":
            # Azure OpenAI Integration (Enterprise Realm)
            return AzureChatOpenAI(
                azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
                api_version="2023-05-15"
            )
        elif self.realm == "cloud":
            # OpenAI / Anthropic Integration (Cloud Realm)
            # Defaulting to OpenAI for Phase 1 shell
            return ChatOpenAI(model="gpt-4-turbo-preview")
        else:
            # Local Ollama Integration (Edge Realm - Default)
            return Ollama(
                base_url=os.getenv("OLLAMA_BASE_URL", "http://localhost:11434"),
                model=os.getenv("OLLAMA_MODEL", "qwen2.5-coder:7b")
            )

    def invoke(self, messages: List[BaseMessage]):
        """Unified invoke interface across all realms."""
        return self.model.invoke(messages)

# WIP Export for Lu Bu's Orchestrator
urw = UniversalReasoningWrapper()
