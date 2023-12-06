from openai import OpenAI

client = OpenAI(
    # api_key defaults to os.environ.get("OPENAI_API_KEY")
    api_key="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",
)

def get_completion_from_messages(messages, model='gpt-3.5-turbo', temperature=0):
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature
    )
    return response.choices[0].message.content

# openai.api_key = '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'
option = 1

if option == 1: #TONE
  added_prompt = 'generate a paraphrase filled with happy keywords for ' 
  temperature = 0.7
if option == 2: #TONE
  added_prompt = 'generate a paraphrase filled with sad keywords for ' 
  temperature = 0.7
if option == 3: #TONE
  added_prompt = 'generate a paraphrase filled with friendly keywords for ' 
  temperature = 0.7
if option == 4: #TONE
  added_prompt = 'generate a paraphrase filled with romantic keywords for ' 
  temperature = 0.7
if option == 5: #TONE
  added_prompt = 'generate a paraphrase filled with angry keywords for ' 
  temperature = 0.7
if option == 6: #TONE
  added_prompt = 'generate a paraphrase filled with professional keywords for ' 
  temperature = 0.7
elif option == 7: #EXPAND
  added_prompt = 'generate an extensively detailed paraphrase paragraph for '
  temperature = 0.7 
elif option == 8: #PARAPHRASE
  added_prompt = 'generate a paraphrased version for '
  temperature = 0.7  
elif option == 9: #SUMMARIZE
  added_prompt = 'generate a summarized version for '
  temperature = 0.7  
elif option == 10: #REPLY
  added_prompt = 'generate a reply for '
  temperature = 0.9  

user_input = input('User: ')
# message = added_prompt + 'The sleek, silver car glided down the winding mountain road, its powerful engine purring with a hint of excitement. With its aerodynamic design and cutting-edge technology, this modern marvel of automotive engineering offered both style and substance. Inside, the luxurious leather seats cradled passengers in comfort, while the state-of-the-art infotainment system provided a seamless blend of entertainment and navigation. Whether it was cruising along the open highway or navigating through the bustling city streets, this car effortlessly combined performance and elegance, making every journey an unforgettable experience.'
message = added_prompt + user_input

# Use the OpenAI API to generate responses
response = client.completions.create(
    model="gpt-3.5-turbo-instruct",  
    prompt=message,
    max_tokens=100,  
    n=1,  
    stop=None,  
    temperature=temperature,  # Higher values make responses more random, lower values make them more deterministic
)

# Extract and print the generated replies
replies = [choice.text.strip() for choice in response.choices]
print('Output: ' + replies[0])
