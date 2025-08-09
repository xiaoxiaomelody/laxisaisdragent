# laxis_ai_sdr_agent
This is a prototype I designed and built for Laxis AI SDR development. This AI agent MVP generates draft replies to emails. It understands the context and intent of incoming emails and produces clear, polite, and relevant responses.

I chose to use OpenAI framework in my MVP because it provides state-of-the-art natural language understanding and generation capabilities that significantly accelerate development 
while delivering high-quality user experiences. OpenAI’s well-documented APIs and robust infrastructure allow for seamless integration, enabling rapid iteration and continuous improvement based on user feedback. 

I produce six sample emails following all different categories in emails.json. In main.py, I import emails.json, OpenAI API key, write helper functions and prompts to parse email, classify intent, generate response.

Import you own OpenAI API key and run python main.py to try it out!
