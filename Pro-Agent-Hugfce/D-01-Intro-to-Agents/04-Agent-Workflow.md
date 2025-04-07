#  Think → Act → Observe.
#### Complete AI Agent Workflow

**The Core Components**
Agents work in a continuous cycle of: thinking (Thought) → acting (Act) and observing (Observe).

Let’s break down these actions together:

Thought: The LLM part of the Agent decides what the next step should be.
Action: The agent takes an action, by calling the tools with the associated arguments.
Observation: The model reflects on the response from the tool.


>> The Thought-Action-Observation Cycle
The three components work together in a continuous loop. To use an analogy from programming, the agent uses a while loop: the loop continues until the objective of the agent has been fulfilled.

In many Agent frameworks, the rules and guidelines are embedded directly into the system prompt, ensuring that every cycle adheres to a defined logic.
In a simplified version, our system prompt may look like this:

![alt text](/Pro-Agent-Hugfce/day01-Intro-to-Agents/images/04-img1.png)

We see here that in the System Message we defined :

The Agent’s behavior.
The Tools our Agent has access to, as we described in the previous section.
The Thought-Action-Observation Cycle, that we bake into the LLM instructions.


**USECASE: Wheather Agent**

We created Alfred, the Weather Agent.

A user asks Alfred: “What’s the weather like in New York today?”

![alt text](/Pro-Agent-Hugfce/day01-Intro-to-Agents/images/04-img2.png)

Alfred’s job is to answer this query using a weather API tool.

Think → Act → Observe.

**Thought**
Internal Reasoning:

Upon receiving the query, Alfred’s internal dialogue might be:

“The user needs current weather information for New York. I have access to a tool that fetches weather data. First, I need to call the weather API to get up-to-date details.”

This step shows the agent breaking the problem into steps: first, gathering the necessary data.

![alt text](/Pro-Agent-Hugfce/day01-Intro-to-Agents/images/04-img3.png)


**Action**
Tool Usage:

Based on its reasoning and the fact that Alfred knows about a get_weather tool, Alfred prepares a JSON-formatted command that calls the weather API tool. For example, its first action could be:

Thought: I need to check the current weather for New York.

Copied
   {
     "action": "get_weather",
     "action_input": {
       "location": "New York"
     }
   }
Here, the action clearly specifies which tool to call (e.g., get_weather) and what parameter to pass (the “location”: “New York”).

![alt text](/Pro-Agent-Hugfce/day01-Intro-to-Agents/images/04-img4.png)

**Observation**

Feedback from the Environment:

After the tool call, Alfred receives an observation. This might be the raw weather data from the API such as:

“Current weather in New York: partly cloudy, 15°C, 60% humidity.”

![alt text](/Pro-Agent-Hugfce/day01-Intro-to-Agents/images/05-img5.png)

This observation is then added to the prompt as additional context. It functions as real-world feedback, confirming whether the action succeeded and providing the needed details.

**Updated thought**
Reflecting:

With the observation in hand, Alfred updates its internal reasoning:

“Now that I have the weather data for New York, I can compile an answer for the user.”

![alt text](/Pro-Agent-Hugfce/day01-Intro-to-Agents/images/06-img1.png)

**Final Action**
Alfred then generates a final response formatted as we told it to:

Thought: I have the weather data now. The current weather in New York is partly cloudy with a temperature of 15°C and 60% humidity.”

Final answer : The current weather in New York is partly cloudy with a temperature of 15°C and 60% humidity.

This final action sends the answer back to the user, closing the loop.

![alt text](/Pro-Agent-Hugfce/day01-Intro-to-Agents/images/06-img6.png)


In this Wheather Usecase , Agents iterate through a loop until the objective is fullfilled:

Alfred’s process is cyclical. It starts with a thought, then acts by calling a tool, and finally observes the outcome. If the observation had indicated an error or incomplete data, Alfred could have re-entered the cycle to correct its approach.

Tool Integration:
The ability to call a tool (like a weather API) enables Alfred to go beyond static knowledge and retrieve real-time data, an essential aspect of many AI Agents.

Dynamic Adaptation:
Each cycle allows the agent to incorporate fresh information (observations) into its reasoning (thought), ensuring that the final answer is well-informed and accurate.

This example showcases the core concept behind the  >> ReAct cycle (a concept we’re going to develop in the next section): the interplay of Thought, Action, and Observation empowers AI agents to solve complex tasks iteratively.>>

##### By understanding and applying these principles, you can design agents that not only reason about their tasks but also effectively utilize external tools to complete them, all while continuously refining their output based on environmental feedback.