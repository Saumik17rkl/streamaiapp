import google.generativeai as genai

# List all models available
models = genai.list_models()
for model in models:
    print(f"Model: {model.name}, Supported tasks: {model.supported_generation_methods}")


