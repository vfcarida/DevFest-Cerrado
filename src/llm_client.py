"""
Client module for interacting with Generative AI models.
Encapsulates Google Generative AI (Gemini) SDK usage.
"""
import logging
from typing import Optional, List, Dict, Any
import google.generativeai as genai

from src.config import GEMINI_API_KEY

logger = logging.getLogger(__name__)

class GeminiClient:
    """
    Client interface for interacting with Gemini models.
    Provides methods for generating text and handling multimodal inputs.
    """
    def __init__(self, api_key: str = GEMINI_API_KEY, model_name: str = 'gemini-1.5-flash'):
        self.api_key = api_key
        self.model_name = model_name
        self._initialize_client()

    def _initialize_client(self) -> None:
        """Configures the generative AI SDK with the provided API key."""
        if not self.api_key:
            logger.error("A tentativa de inicializar o GeminiClient falhou pois a API Key está vazia.")
            raise ValueError("API Key do Gemini é obrigatória.")
        try:
            genai.configure(api_key=self.api_key)
            self.model = genai.GenerativeModel(self.model_name)
            logger.info(f"GeminiClient inicializado com sucesso para o modelo: {self.model_name}")
        except Exception as e:
            logger.error(f"Erro ao configurar o cliente do Gemini: {e}")
            raise

    def generate_text(self, prompt: str, temperature: float = 0.7) -> str:
        """
        Generates text based on a prompt.
        
        Args:
            prompt (str): The input text to prompt the model.
            temperature (float): The sampling temperature.
            
        Returns:
            str: The generated text response.
        """
        try:
            logger.info("Enviando requisição de texto para o Gemini.")
            response = self.model.generate_content(
                prompt,
                generation_config=genai.types.GenerationConfig(
                    temperature=temperature,
                )
            )
            return response.text
        except Exception as e:
            logger.error(f"Erro durante a geração de texto: {e}", exc_info=True)
            return f"Erro na geração de conteúdo: {e}"

    def generate_multimodal(self, prompt: str, media_parts: List[Any], temperature: float = 0.7) -> str:
        """
        Generates text using both prompt and media (images, video, etc).
        
        Args:
            prompt (str): The text prompt.
            media_parts (List[Any]): List of multimodal elements (e.g., PIL Images).
            temperature (float): Sampling temperature.
            
        Returns:
            str: The generated text response.
        """
        try:
            logger.info(f"Enviando requisição multimodal para o Gemini com {len(media_parts)} anexos.")
            contents = [prompt] + media_parts
            response = self.model.generate_content(
                contents,
                generation_config=genai.types.GenerationConfig(
                    temperature=temperature,
                )
            )
            return response.text
        except Exception as e:
            logger.error(f"Erro durante a geração multimodal: {e}", exc_info=True)
            return f"Erro na geração de conteúdo multimodal: {e}"
