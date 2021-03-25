from arc import train_set

from arc.evaluation import evaluate_agent

from prob_solutions.agent import HardcodedAgent

agent = HardcodedAgent()

result = evaluate_agent(agent, train_set)
print(result)
