### Dive into the inner workings of an AI agent—its ability to reason and plan. We’ll explore how the agent leverages its internal dialogue to analyze information, break down complex problems into manageable steps, and decide what action to take next. 

#### Understanding  the Re-Act approach, a prompting technique that encourages the model to think “step by step” before acting.

Thoughts represent the Agent’s internal reasoning and planning processes to solve the task.

This utilises the agent’s Large Language Model (LLM) capacity to analyze information when presented in its prompt.

Think of it as the agent’s internal dialogue, where it considers the task at hand and strategizes its approach.

The Agent’s thoughts are responsible for accessing current observations and decide what the next action(s) should be.

Through this process, the agent can break down complex problems into smaller, more manageable steps, reflect on past experiences, and continuously adjust its plans based on new information.

Here are some examples of common thoughts:

Type of Thought	Example
Planning	        “I need to break this task into three steps: 1) gather data, 2) analyze trends, 3) generate report”
Analysis	        “Based on the error message, the issue appears to be with the database connection parameters”
Decision Making	    “Given the user’s budget constraints, I should recommend the mid-tier option”
Problem Solving	    “To optimize this code, I should first profile it to identify bottlenecks”
Memory Integration	“The user mentioned their preference for Python earlier, so I’ll provide examples in Python”
Self-Reflection	     “My last approach didn’t work well, I should try a different strategy”
Goal Setting	     “To complete this task, I need to first establish the acceptance criteria”
Prioritization	     “The security vulnerability should be addressed before adding new features”

##### Note: In the case of LLMs fine-tuned for function-calling, the thought process is optional. In case you’re not familiar with function-calling, there will be more details in the Actions section.

Scenario
A user wants to know the weather in Paris and decide whether to carry an umbrella.

1. Function Calling Approach
Step-by-Step Process
User Query:

"What’s the weather in Paris today?"

LLM Action:

The LLM identifies the need to call a weather API.

It generates a function call to the weather API with parameters:

location=Paris

date=today

Function Execution:

The weather API is called, and it returns:

json
Copy
{
  "location": "Paris",
  "date": "2023-10-25",
  "condition": "rainy",
  "temperature": "15°C"
}
LLM Response:

The LLM formats the API response and replies:

"It’s rainy in Paris today with a temperature of 15°C."

2. AI Agent Approach
Step-by-Step Process
User Query:

"Should I carry an umbrella if I’m visiting Paris today?"

Agent Action:

The agent breaks the task into smaller steps:

Fetch the weather data for Paris.

Analyze the weather condition to determine if an umbrella is needed.

Provide a recommendation.

Step 1: Fetch Weather Data:

The agent calls a weather API with parameters:

location=Paris

date=today

The API returns:

json
Copy
{
  "location": "Paris",
  "date": "2023-10-25",
  "condition": "rainy",
  "temperature": "15°C"
}
Step 2: Analyze Weather Condition:

The agent uses the LLM to reason about the weather data.

It determines that "rainy" weather implies a high chance of rain.

Step 3: Provide Recommendation:

The agent compiles the results and responds:

"It’s rainy in Paris today with a temperature of 15°C. You should carry an umbrella."

Key Differences

![alt text](/Pro-Agent-Hugfce/day01-Intro-to-Agents/images/05-img1.png)

Visual Comparison
Function Calling
Copy
User: "What’s the weather in Paris today?"
LLM: Calls weather API → "It’s rainy in Paris today with a temperature of 15°C."
AI Agent
Copy
User: "Should I carry an umbrella if I’m visiting Paris today?"
Agent:
  1. Calls weather API → "It’s rainy in Paris today with a temperature of 15°C."
  2. Reasons: "Rainy weather means I should carry an umbrella."
  3. Responds: "You should carry an umbrella."

Summary
Function Calling:

Best for simple, single-step tasks like fetching data or performing calculations.

The LLM acts as a middleman, calling a function and returning the result.

Example: Fetching weather data.

AI Agent:

Best for complex, multi-step tasks that require reasoning, planning, and decision-making.

The agent uses the LLM as its brain to analyze data, maintain context, and provide actionable recommendations.

Example: Deciding whether to carry an umbrella based on weather data.

In the weather example:

Function calling simply retrieves and displays the weather data.

AI agent goes further by analyzing the data and providing a recommendation.


#### The Re-Act Approach
A key method is the ReAct approach, which is the concatenation of “Reasoning” (Think) with “Acting” (Act).

ReAct is a simple prompting technique that appends “Let’s think step by step” before letting the LLM decode the next tokens.

Indeed, prompting the model to think “step by step” encourages the decoding process toward next tokens that generate a plan, rather than a final solution, since the model is encouraged to decompose the problem into sub-tasks.

This allows the model to consider sub-steps in more detail, which in general leads to less errors than trying to generate the final solution directly.

![alt text](/Pro-Agent-Hugfce/day01-Intro-to-Agents/images/05-img2.png)

The (d) is an example of Re-Act approach where we prompt "Let's think step by step"

**OpenAI's o1, which have been fine-tuned to "think before answering"**
These models have been trained to always include specific thinking sections (enclosed between <think> and </think> special tokens). This is not just a prompting technique like ReAct, but a training method where the model learns to generate these sections after analyzing thousands of examples that show what we expect it to do.