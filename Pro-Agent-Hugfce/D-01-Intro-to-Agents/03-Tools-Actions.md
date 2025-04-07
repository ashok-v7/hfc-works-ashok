
What Tools are, how to design them effectively, and how to integrate them into your Agent via the System Message.
By giving your Agent the right Tools—and clearly describing how those Tools work—you can dramatically increase what your AI can accomplish. 
Let’s dive in 

### How tools are made available to the agent in the system prompt.
### How AI agents are systems that can ‘reason’, plan, and interact with their environment.
### What are AI Tools?

A Tool is a function given to the LLM. This function should fulfill a clear objective.

Here are some commonly used tools in AI agents:

Tool	            Description
Web Search	     >  Allows the agent to fetch up-to-date information from the internet.
Image Generation >  Creates images based on text descriptions.
Retrieval	     >  Retrieves information from an external source.
API Interface	 >  Interacts with an external API (GitHub, YouTube, Spotify, etc.).

A good tool should be something that complements the power of an LLM.

For instance, if you need to perform arithmetic, giving a calculator tool to your LLM will provide better results than relying on the native capabilities of the model.


### A Tool should contain:
A textual description of what the function does.
A Callable (something to perform an action).
Arguments with typings.
(Optional) Outputs with typings.

### How do tools work?
LLMs,  only receive text inputs and generate text outputs. They have no way to call tools on their own. What we mean when we talk about providing tools to an Agent, is that we teach the LLM about the existence of tools, and ask the model to generate text that will invoke tools when it needs to

eg: if we provide a tool to check the weather at a location from the Internet, and then ask the LLM about the weather in Paris, the LLM will recognize that question as a relevant opportunity to use the “weather” tool we taught it about. 

The LLM will generate text, in the form of code, to invoke that tool. It is the responsibility of the Agent to parse the LLM’s output, recognize that a tool call is required, and invoke the tool on the LLM’s behalf. The output from the tool will then be sent back to the LLM, which will compose its final response for the user.

The output from a tool call is another type of message in the conversation. Tool calling steps are typically not shown to the user: the Agent retrieves the conversation, calls the tool(s), gets the outputs, adds them as a new conversation message, and sends the updated conversation to the LLM again. 
From the user’s point of view, it’s like the LLM had used the tool, but in fact it was our application code (the Agent) who did it.

### How do we give tools to an LLM?

we essentially use the system prompt to provide textual descriptions of available tools to the model:
Tool Name: calculator, Description: Multiply two integers., Arguments: a: int, b: int, Outputs: int

![alt text](/Pro-Agent-Hugfce/day01-Intro-to-Agents/images/03-img1.png)

What Tools Are: Functions that give LLMs extra capabilities, such as performing calculations or accessing external data.

How to Define a Tool: By providing a clear textual description, inputs, outputs, and a callable function.

Why Tools Are Essential: They enable Agents to overcome the limitations of static model training, handle real-time tasks, and perform specialized actions.


### what  describes an AI tool?
An executable process or external API that allows agents to perform specific tasks and interact with external environments
Tools are executable functions that agents can use to perform specific tasks and interact with external environments.

### Q2: How do AI agents use tools as a form of “acting” in an environment?
By asking the LLM to generate tool invocation code when appropriate and running tools on behalf of the model

### Q3: What is a Large Language Model (LLM)?
 A deep learning model trained on large amounts of text to understand and generate human-like language

### Q4: Which of the following best describes the role of special tokens in LLMs?
They serve specific functions like marking the end of a sequence (EOS) or separating different message roles in chat models

### Q5: How do AI chat models process user messages internally?
They convert user messages into a formatted prompt by concatenating system, user, and assistant messages

### Q6 : Extensions
Extensions
The easiest way to understand Extensions is to think of them as bridging the gap between
an API and an agent in a standardized way, allowing agents to seamlessly execute APIs
regardless of their underlying implementation. Let’s say that you’ve built an agent with a goal
of helping users book flights. You know that you want to use the Google Flights API to retrieve
flight information, but you’re not sure how you’re going to get your agent to make calls to this
API endpoint.

A Vertex AI extension is a structured API wrapper that connects a model to an API for processing real-time data or performing real-world actions.

The difference between Extensions and Functions is in the execution of the Tool. Extensions are automatically executed by Vertex AI. Whereas functions must be manually executed by the user or client.

To streamline the extension creation process, we provide prebuilt Extensions by Google for common use cases, such as code interpretation and Vertex AI Search. If your use case doesn't align with these templates, you can create your own custom extension.

### Q7 : Agents vs. models
To gain a clearer understanding of the distinction between agents and models, consider the
following chart:

![alt text](/Pro-Agent-Hugfce/day01-Intro-to-Agents/images/08-img1.png)
