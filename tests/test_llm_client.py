import sys
from unittest.mock import MagicMock

# Mock module google.generativeai before importing llm_client
sys.modules['google'] = MagicMock()
sys.modules['google.generativeai'] = MagicMock()

# Mock dotenv
sys.modules['dotenv'] = MagicMock()

import pytest
from unittest.mock import patch
from src.llm_client import GeminiClient

@patch("src.llm_client.genai.configure")
@patch("src.llm_client.genai.GenerativeModel")
def test_gemini_client_initialization(mock_model, mock_configure):
    """Testa se a inicialização do GeminiClient configura a API corretamente."""
    client = GeminiClient(api_key="fake_key", model_name="fake_model")
    mock_configure.assert_called_once_with(api_key="fake_key")
    mock_model.assert_called_once_with("fake_model")

def test_gemini_client_missing_api_key():
    """Testa se o cliente lança erro ao inicializar sem API Key."""
    with pytest.raises(ValueError, match="API Key do Gemini é obrigatória."):
         GeminiClient(api_key="")

@patch("src.llm_client.genai.configure")
@patch("src.llm_client.genai.GenerativeModel")
def test_generate_text_success(mock_model, mock_configure):
    """Testa a geração de texto com sucesso."""
    mock_instance = MagicMock()
    mock_response = MagicMock()
    mock_response.text = "Resposta do modelo"
    mock_instance.generate_content.return_value = mock_response
    mock_model.return_value = mock_instance

    client = GeminiClient(api_key="fake_key")
    response = client.generate_text("Olá")
    
    assert response == "Resposta do modelo"
    mock_instance.generate_content.assert_called_once()

@patch("src.llm_client.genai.configure")
@patch("src.llm_client.genai.GenerativeModel")
def test_generate_text_failure(mock_model, mock_configure):
    """Testa comportamento quando ocorre um erro na API."""
    mock_instance = MagicMock()
    mock_instance.generate_content.side_effect = Exception("API indisponível")
    mock_model.return_value = mock_instance

    client = GeminiClient(api_key="fake_key")
    response = client.generate_text("Olá")
    
    assert "Erro na geração de conteúdo:" in response
