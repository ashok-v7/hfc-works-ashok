``` Agent needs an AI Model at its core, and that LLMs are the most common type of AI models for this purpose. ```

### What is a Large Language Model?
An LLM is a type of AI model that excels at understanding and generating human language. They are trained on vast amounts of text data, allowing them to learn patterns, structure, and even nuance in language. These models typically consist of many millions of parameters.

Most LLMs nowadays are built on the Transformer architecture—a deep learning architecture based on the “Attention” algorithm, that has gained significant interest since the release of BERT from Google in 2018.

![alt text](/Pro-Agent-Hugfce/day01-Intro-to-Agents/images/02-img1.png)

There are 3 types of transformers :

**Encoders**
An encoder-based Transformer takes text (or other data) as input and outputs a dense representation (or embedding) of that text.

Example: BERT from Google
Use Cases: Text classification, semantic search, Named Entity Recognition
Typical Size: Millions of parameters

**Decoders**
A decoder-based Transformer focuses on generating new tokens to complete a sequence, one token at a time.

Example: Llama from Meta
Use Cases: Text generation, chatbots, code generation
Typical Size: Billions (in the US sense, i.e., 10^9) of parameters

**Seq2Seq (Encoder–Decoder)**
A sequence-to-sequence Transformer combines an encoder and a decoder. The encoder first processes the input sequence into a context representation, then the decoder generates an output sequence.

Example: T5, BART,
Use Cases: Translation, Summarization, Paraphrasing
Typical Size: Millions of parameters

Although Large Language Models come in various forms, LLMs are typically decoder-based models with billions of parameters. Here are some of the most well-known LLMs:

The underlying principle of an LLM is simple yet highly effective: Its objective is to predict the next token, given a sequence of previous tokens. 
A “token” is the unit of information an LLM works with. You can think of a “token” as if it was a “word”, but for efficiency reasons LLMs don’t use whole words.

For example, while English has an estimated 600,000 words, an LLM might have a vocabulary of around 32,000 tokens (as is the case with Llama 2). Tokenization often works on sub-word units that can be combined.

For instance, consider how the tokens “interest” and “ing” can be combined to form “interesting”, or “ed” can be appended to form “interested.”

You can experiment with different tokenizers in the interactive playground below:

'' https://platform.openai.com/tokenizer ''



Chat Template : 
chat templates, They act as the bridge between conversational messages (user and assistant turns) and the specific formatting requirements of your chosen LLM. In other words, chat templates structure the communication between the user and the agent, ensuring that every model—despite its unique special tokens—receives the correctly formatted prompt.

Chat templates help maintain context by preserving conversation history, storing previous exchanges between the user and the assistant. This leads to more coherent multi-turn conversations.

### Base Models vs. Instruct Models
Another point we need to understand is the difference between a Base Model vs. an Instruct Model:

A Base Model is trained on raw text data to predict the next token.

An Instruct Model is fine-tuned specifically to follow instructions and engage in conversations. For example, SmolLM2-135M is a base model, while SmolLM2-135M-Instruct is its instruction-tuned variant.

To make a Base Model behave like an instruct model, we need to format our prompts in a consistent way that the model can understand. This is where chat templates come in.
