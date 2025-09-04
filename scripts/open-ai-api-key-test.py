from openai import OpenAI

client = OpenAI(api_key="[SUA-CHAVE-AQUI]")

resp = client.models.list()
print([m.id for m in resp.data[:5]])