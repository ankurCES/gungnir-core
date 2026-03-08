# UNIVERSAL REASONING WRAPPER

## Objective
To provide a unified interface for switching between different LLM providers based on environment configuration.

## Support Providers
- **Azure OpenAI:** For enterprise deployment.
- **Cloud OpenAI/Anthropic:** For rapid cloud development.
- **Edge Ollama:** For local, private execution on the Jetson.

## Configuration (`.env`)
```bash
GUNGNIR_REASONING_REALM=edge # options: enterprise, cloud, edge
REASONING_MODEL=qwen2.5-coder:7b
```
