import openai

openai.api_key = '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'
prompt = input('Enter Your Command: ')

response = openai.Completion.create(
  model="text-davinci-003",
  prompt=prompt,
  temperature=0.7,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

text = response.get('choices')[0].get('text')
print(text)